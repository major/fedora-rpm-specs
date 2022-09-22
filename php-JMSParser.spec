#
# Fedora spec file for php-JMSParser
#
# Copyright (c) 2013-2017 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner      schmittjoh
%global github_name       parser-lib
%global github_version    1.0.0
%global github_commit     c509473bc1b4866415627af0e1c6cc8ac97fa51d

%global composer_vendor   jms
%global composer_project  parser-lib

# "phpoption/phpoption": ">=0.9,<2.0-dev"
#     NOTE: Min version not 0.9 because autoloader required
%global phpoption_min_ver 1.5.0
%global phpoption_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-JMSParser
Version:       %{github_version}
Release:       22%{?dist}
Summary:       Library for writing recursive-descent parsers

License:       ASL 2.0
URL:           http://jmsyst.com/libs/%{github_name}

# GitHub export contains non-allowable licened documentation.
# Run php-JMSParser-get-source.sh to create allowable source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php-composer(phpoption/phpoption) <  %{phpoption_max_ver}
BuildRequires: php-composer(phpoption/phpoption) >= %{phpoption_min_ver}
## phpcompatinfo (computed from version 1.0.0)
BuildRequires: php(language) >= 5.3.0
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php-composer(phpoption/phpoption) <  %{phpoption_max_ver}
Requires:      php-composer(phpoption/phpoption) >= %{phpoption_min_ver}
# phpcompatinfo (computed from version 1.0.0)
Requires:      php(language) >= 5.3.0
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/JMS/Parser/autoload.php


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/JMS/Parser/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('JMS\\Parser\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/PhpOption/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/JMS %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/JMS/Parser/autoload.php \
            || RETURN_CODE=1
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
%dir %{phpdir}/JMS
     %{phpdir}/JMS/Parser


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-12
- Bump release for rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-9
- Switched autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-7
- Added spec license
- New source script %%{name}-get-source.sh instead of %%{name}-strip.sh
- Added autoloader
- Added standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming provides
- Added php-composer(jms/parser-lib) provide
- %%license usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-3
- Added %%{name}-strip.sh as Source1

* Sat Mar 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-2
- Added phpoption_min_ver and phpoption_max_ver globals
- Bad licensed files stripped from source
- php-common => php(language)
- Removed tests sub-package

* Thu Jan 24 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-1
- Initial package
