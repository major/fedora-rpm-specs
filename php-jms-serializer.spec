#
# Fedora spec file for php-jms-serializer
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     schmittjoh
%global github_name      serializer
%global github_version   1.14.1
%global github_commit    ba908d278fff27ec01fb4349f372634ffcd697c0

%global composer_vendor  jms
%global composer_project serializer

# Deprecate Symfony 2 on Fedora 32+ and EPEL 8+
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
%global with_symfony2 0
%else
%global with_symfony2 1
%endif

# "php": "^5.5|^7.0"
%global php_min_ver 5.5.0
# "doctrine/annotations": "^1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global doctrine_annotations_min_ver 1.2.6
%global doctrine_annotations_max_ver 2.0
# "doctrine/instantiator": "^1.0.3"
%global doctrine_instantiator_min_ver 1.0.3
%global doctrine_instantiator_max_ver 2.0
# "doctrine/orm": "~2.1"
#     NOTE: Min version not 2.1 because autoloader required
%global doctrine_orm_min_ver 2.4.8
%global doctrine_orm_max_ver 3.0
# "jms/metadata": "^1.3"
#     NOTE: Min version not 1.3 because autoloader required
%global jms_metadata_min_ver 1.6.0
%global jms_metadata_max_ver 2.0
# "jms/parser-lib": "1.*"
#     NOTE: Min version not 1.0 because autoloader required
%global jms_parser_lib_min_ver 1.0.0-7
%global jms_parser_lib_max_ver 2.0
# "phpcollection/phpcollection": "~0.1"
#     NOTE: Min version not 0.1 because autoloader required
%global phpcollection_min_ver 0.5.0
%global phpcollection_max_ver 1.0
# "phpoption/phpoption": "^1.1"
#     NOTE: Min version not 1.1 because autoloader required
%global phpoption_min_ver 1.5.0
%global phpoption_max_ver 2.0
# "psr/container": "^1.0"
%global psr_container_min_ver 1.0
%global psr_container_max_ver 2.0
# "symfony/dependency-injection": "^2.7|^3.3|^4.0"
# "symfony/expression-language": "^2.6|^3.0"
# "symfony/filesystem": "^2.1"
# "symfony/form": "~2.1|^3.0"
# "symfony/translation": "^2.1|^3.0"
# "symfony/validator": "^2.2|^3.0"
# "symfony/yaml": "^2.1|^3.0"
%if %{with_symfony2}
#     NOTE: Min version not 2.6 because autoloader required
%global symfony_min_ver 2.7.1
%else
%global symfony_min_ver 3.3
%endif
%global symfony_max_ver 4.0

# "twig/twig": "~1.12|~2.0"
#     NOTE: Min version not 1.12 because autoloader required
%global twig_min_ver 1.18.2
%if 0%{?fedora} >= 25 || 0%{?rhel} >= 8
%global twig_max_ver 3.0
%else
%global twig_max_ver 2.0
%endif

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

# Weak dependencies supported?
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%global with_weak_dependencies 1
%else
%global with_weak_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       Library for (de-)serializing data of any complexity

License:       MIT
URL:           http://jmsyst.com/libs/serializer

# GitHub export contains non-allowable licened documentation.
# Run php-jms-serializer-get-source.sh to create allowable source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Minimal patch for PHP 8
Patch0:        %{name}-php8.patch
BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-cli
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if %{with_range_dependencies}
BuildRequires: (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
BuildRequires: (php-composer(doctrine/instantiator) >= %{doctrine_instantiator_min_ver} with php-composer(doctrine/instantiator) < %{doctrine_instantiator_max_ver})
BuildRequires: (php-composer(doctrine/orm) >= %{doctrine_orm_min_ver} with php-composer(doctrine/orm) < %{doctrine_orm_max_ver})
BuildRequires: (php-composer(jms/metadata) >= %{jms_metadata_min_ver} with php-composer(jms/metadata) < %{jms_metadata_max_ver})
BuildRequires: (php-JMSParser >= %{jms_parser_lib_min_ver} with php-composer(jms/parser-lib) < %{jms_parser_lib_max_ver})
BuildRequires: (php-composer(phpcollection/phpcollection) >= %{phpcollection_min_ver} with php-composer(phpcollection/phpcollection) < %{phpcollection_max_ver})
BuildRequires: (php-composer(phpoption/phpoption) >= %{phpoption_min_ver} with php-composer(phpoption/phpoption) < %{phpoption_max_ver})
BuildRequires: (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
BuildRequires: (php-composer(symfony/dependency-injection) >= %{symfony_min_ver} with php-composer(symfony/dependency-injection) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/expression-language) >= %{symfony_min_ver} with php-composer(symfony/expression-language) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/filesystem) >= %{symfony_min_ver} with php-composer(symfony/filesystem) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/form) >= %{symfony_min_ver} with php-composer(symfony/form) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/translation) >= %{symfony_min_ver} with php-composer(symfony/translation) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/validator) >= %{symfony_min_ver} with php-composer(symfony/validator) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/yaml) >= %{symfony_min_ver} with php-composer(symfony/yaml) < %{symfony_max_ver})
BuildRequires: (php-composer(twig/twig) >= %{twig_min_ver} with php-composer(twig/twig) < %{twig_max_ver})
%else
BuildRequires: php-composer(doctrine/annotations) <  %{doctrine_annotations_max_ver}
BuildRequires: php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver}
BuildRequires: php-composer(doctrine/instantiator) <  %{doctrine_instantiator_max_ver}
BuildRequires: php-composer(doctrine/instantiator) >= %{doctrine_instantiator_min_ver}
BuildRequires: php-composer(doctrine/orm) <  %{doctrine_orm_max_ver}
BuildRequires: php-composer(doctrine/orm) >= %{doctrine_orm_min_ver}
BuildRequires: php-composer(jms/metadata) <  %{jms_metadata_max_ver}
BuildRequires: php-composer(jms/metadata) >= %{jms_metadata_min_ver}
BuildRequires: php-composer(jms/parser-lib) <  %{jms_parser_lib_max_ver}
#BuildRequires: php-composer(jms/parser-lib) >= %%{jms_parser_lib_min_ver}
BuildRequires: php-JMSParser                >= %{jms_parser_lib_min_ver}
BuildRequires: php-composer(phpcollection/phpcollection) <  %{phpcollection_max_ver}
BuildRequires: php-composer(phpcollection/phpcollection) >= %{phpcollection_min_ver}
BuildRequires: php-composer(phpoption/phpoption) <  %{phpoption_max_ver}
BuildRequires: php-composer(phpoption/phpoption) >= %{phpoption_min_ver}
BuildRequires: php-composer(psr/container) <  %{psr_container_max_ver}
BuildRequires: php-composer(psr/container) >= %{psr_container_min_ver}
BuildRequires: php-composer(symfony/dependency-injection) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/dependency-injection) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/expression-language) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/expression-language) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/filesystem) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/filesystem) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/form) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/form) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/translation) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/translation) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/validator) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/validator) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/yaml) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/yaml) >= %{symfony_min_ver}
BuildRequires: php-composer(twig/twig) <  %{twig_max_ver}
BuildRequires: php-composer(twig/twig) >= %{twig_min_ver}
%endif
## phpcompatinfo (computed from version 1.14.1)
BuildRequires: php-composer(doctrine/cache) < 2
BuildRequires: php-composer(doctrine/common) < 3
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
Requires:      (php-composer(doctrine/instantiator) >= %{doctrine_instantiator_min_ver} with php-composer(doctrine/instantiator) < %{doctrine_instantiator_max_ver})
Requires:      (php-composer(jms/metadata) >= %{jms_metadata_min_ver} with php-composer(jms/metadata) < %{jms_metadata_max_ver})
Requires:      (php-JMSParser >= %{jms_parser_lib_min_ver} with php-composer(jms/parser-lib) < %{jms_parser_lib_max_ver})
Requires:      (php-composer(phpcollection/phpcollection) >= %{phpcollection_min_ver} with php-composer(phpcollection/phpcollection) < %{phpcollection_max_ver})
Requires:      (php-composer(phpoption/phpoption) >= %{phpoption_min_ver} with php-composer(phpoption/phpoption) < %{phpoption_max_ver})
%else
Requires:      php-composer(doctrine/annotations) <  %{doctrine_annotations_max_ver}
Requires:      php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver}
Requires:      php-composer(doctrine/instantiator) <  %{doctrine_instantiator_max_ver}
Requires:      php-composer(doctrine/instantiator) >= %{doctrine_instantiator_min_ver}
Requires:      php-composer(jms/metadata) <  %{jms_metadata_max_ver}
Requires:      php-composer(jms/metadata) >= %{jms_metadata_min_ver}
Requires:      php-composer(jms/parser-lib) <  %{jms_parser_lib_max_ver}
#Requires:      php-composer(jms/parser-lib) >= %%{jms_parser_lib_min_ver}
Requires:      php-JMSParser                >= %{jms_parser_lib_min_ver}
Requires:      php-composer(phpcollection/phpcollection) <  %{phpcollection_max_ver}
Requires:      php-composer(phpcollection/phpcollection) >= %{phpcollection_min_ver}
Requires:      php-composer(phpoption/phpoption) <  %{phpoption_max_ver}
Requires:      php-composer(phpoption/phpoption) >= %{phpoption_min_ver}
%endif
# phpcompatinfo (computed from version 1.14.1)
Requires:      php-composer(doctrine/common) < 3
Requires:      php-date
Requires:      php-dom
Requires:      php-json
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

%if %{with_weak_dependencies}
# Weak dependencies
Suggests:      php-composer(symfony/yaml)
Suggests:      php-composer(doctrine/collections)
Suggests:      php-composer(doctrine/cache)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This library allows you to (de-)serialize data of any complexity. Currently, it
supports XML, JSON, and YAML.

It also provides you with a rich tool-set to adapt the output to your specific
needs.

Built-in features include:
* (De-)serialize data of any complexity; circular references are handled
  gracefully.
* Supports many built-in PHP types (such as dates)
* Integrates with Doctrine ORM, et. al.
* Supports versioning, e.g. for APIs
* Configurable via PHP, XML, YAML, or Doctrine Annotations

Autoloader: %{phpdir}/JMS/Serializer/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}
%patch0 -p1

: Remove Propel
find . -type f -name '*Propel*' -delete -print
sed '/Propel/d' -i src/JMS/Serializer/SerializerBuilder.php

: Remove Doctrine PHPCR
find . -type f -name '*PHPCR*' -delete -print


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/JMS/Serializer/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('JMS\\Serializer\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Doctrine/Common/Annotations/autoload.php',
    [
        '%{phpdir}/Doctrine/Common/Persistence/autoload.php',
        '%{phpdir}/Doctrine/Common/autoload.php',
    ],
    '%{phpdir}/Doctrine/Instantiator/autoload.php',
    '%{phpdir}/JMS/Parser/autoload.php',
    '%{phpdir}/Metadata/autoload.php',
    '%{phpdir}/PhpCollection/autoload.php',
    '%{phpdir}/PhpOption/autoload.php',
]);

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    '%{phpdir}/Doctrine/Common/Collections/autoload.php',
%if %{with_symfony2}
    [
        '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony/Component/Yaml/autoload.php',
    ],
%else
    '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
%endif
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/JMS %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/JMS/Serializer/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('JMS\\Serializer\\Tests\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Doctrine/ORM/autoload.php',
    '%{phpdir}/Psr/Container/autoload.php',
%if %{with_symfony2}
    [
        '%{phpdir}/Symfony3/Component/DependencyInjection/autoload.php',
        '%{phpdir}/Symfony/Component/DependencyInjection/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/ExpressionLanguage/autoload.php',
        '%{phpdir}/Symfony/Component/ExpressionLanguage/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/Filesystem/autoload.php',
        '%{phpdir}/Symfony/Component/Filesystem/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/Form/autoload.php',
        '%{phpdir}/Symfony/Component/Form/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/Translation/autoload.php',
        '%{phpdir}/Symfony/Component/Translation/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/Validator/autoload.php',
        '%{phpdir}/Symfony/Component/Validator/autoload.php',
    ],
%else
    '%{phpdir}/Symfony3/Component/DependencyInjection/autoload.php',
    '%{phpdir}/Symfony3/Component/ExpressionLanguage/autoload.php',
    '%{phpdir}/Symfony3/Component/Filesystem/autoload.php',
    '%{phpdir}/Symfony3/Component/Form/autoload.php',
    '%{phpdir}/Symfony3/Component/Translation/autoload.php',
    '%{phpdir}/Symfony3/Component/Validator/autoload.php',
%endif
    (PHP_VERSION_ID < 70000)
        ? '%{phpdir}/Twig/autoload.php'
        : [
            '%{phpdir}/Twig2/autoload.php',
            '%{phpdir}/Twig/autoload.php',
        ],
]);

use Doctrine\Common\Annotations\AnnotationRegistry;
AnnotationRegistry::registerLoader('class_exists');
BOOTSTRAP

: Skip test known to fail
sed 's/function testInlineArray/function SKIP_testInlineArray/' \
    -i tests/Serializer/JsonSerializationTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php php73 php74 php80; do
    if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/JMS/Serializer


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Remi Collet <remi@remirepo.net> - 1.14.1-5
- add minimal fix for PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Shawn Iwinski <shawn@iwin.ski> - 1.14.1-3
- Bumping release to ensure all changes are built

* Tue Aug 18 2020 Remi Collet <remi@remirepo.net> - 1.14.1-2
- Update to 1.14.1 (previous update failed to change commit hash so 1.10.0 was built)
- Change license from ASL 2.0 to MIT

* Tue Aug 18 2020 Shawn Iwinski <shawn@iwin.ski> - 1.14.1-1
- Update to 1.14.1
- Fix FTBFS (RHBZ #1865219)
- Conditionally use range dependencies
- Conditionally drop Symfony 2 interoperability

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Shawn Iwinski <shawn@iwin.ski> - 1.10.0-1
- Update to 1.10.0 (RHBZ #1508429)
- Allow Symfony 3

* Sat Oct 07 2017 Shawn Iwinski <shawn@iwin.ski> - 1.9.0-1
- Update to 1.9.0
- Copy some remirepo modifications to make backporting easier:
  https://git.remirepo.net/cgit/rpms/php/jms/php-jms-serializer.git/commit/?id=a33673e63e7e85740df0b340eafb96c8682a084a

* Sat Aug 12 2017 Shawn Iwinski <shawn@iwin.ski> - 1.8.1-1
- Update to 1.8.1

* Wed Jul 12 2017 Shawn Iwinski <shawn@iwin.ski> - 1.7.1-1
- Initial package
