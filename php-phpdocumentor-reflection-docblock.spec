# Fedora/remirepo spec file for php-phpdocumentor-reflection-docblock
#
# Copyright (c) 2017-2021 Remi Collet, Shawn Iwinski
#               2014-2015 Remi Collet
#
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    4aada1f93c72c35e22fb1383b47fee43b8f1d157
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpDocumentor
%global gh_project   ReflectionDocBlock
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-phpdocumentor-reflection-docblock
Version:        3.2.2
Release:        13%{?dist}
Summary:        DocBlock parser

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}

# GitHub export does not include tests.
# Run php-phpdocumentor-reflection-docblock-get-source.sh to create full source.
Source0:       %{name}-%{version}-%{gh_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Minimal fix for PHP 8
Patch0:        %{name}-php8.patch

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 5.5
BuildRequires: (php-composer(phpdocumentor/reflection-common) >= 1.0   with php-composer(phpdocumentor/reflection-common) < 2)
BuildRequires: (php-composer(phpdocumentor/type-resolver)     >= 0.3.0 with php-composer(phpdocumentor/type-resolver)     < 1.0)
BuildRequires: (php-composer(webmozart/assert)                >= 1.0   with php-composer(webmozart/assert)                < 2)
BuildRequires:  php-composer(phpunit/phpunit)
# From phpcompatinfo report for 3.2.1
BuildRequires:  php-filter
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
%endif

# From composer.json, require
#        "php": ">=5.5"
#        "phpdocumentor/reflection-common": "^1.0@dev",
#        "phpdocumentor/type-resolver": "^0.3.0",
#        "webmozart/assert": "^1.0"
Requires:       php(language) >= 5.5
Requires:      (php-composer(phpdocumentor/reflection-common) >= 1.0   with php-composer(phpdocumentor/reflection-common) < 2)
Requires:      (php-composer(phpdocumentor/type-resolver)     >= 0.3.0 with php-composer(phpdocumentor/type-resolver)     < 1.0)
Requires:      (php-composer(webmozart/assert)                >= 1.0   with php-composer(webmozart/assert)                < 2)
# From phpcompatinfo report for 3.2.1
Requires:       php-filter
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpdocumentor/reflection-docblock) = %{version}

Conflicts:      drush < 8.1.10-2
Conflicts:      php-bartlett-PHP-Reflect < 4.0.2-3
Conflicts:      php-consolidation-annotated-command < 2.4.8
Conflicts:      php-phpdocumentor-reflection < 1.0.7-3
Conflicts:      php-phpspec-prophecy < 1.7.0-4


%description
The ReflectionDocBlock component of phpDocumentor provides a DocBlock
parser that is fully compatible with the PHPDoc standard.

With this component, a library can provide support for annotations via
DocBlocks or otherwise retrieve information that is embedded in a DocBlock.


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1


%build
phpab \
  --template fedora \
  --output src/DocBlock/autoload.php \
  src/

cat <<AUTOLOAD | tee -a src/DocBlock/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/phpDocumentor/Reflection/autoload-common.php',
    '%{_datadir}/php/phpDocumentor/Reflection/autoload-type-resolver.php',
    '%{_datadir}/php/Webmozart/Assert/autoload.php',
]);
AUTOLOAD


%install
mkdir -p   %{buildroot}%{_datadir}/php/phpDocumentor
cp -pr src %{buildroot}%{_datadir}/php/phpDocumentor/Reflection


%check
%if %{with_tests}
sed -e '/autoload.php/d' -i examples/*.php examples/*/*.php

: Drop listener
(head -n 26 <phpunit.xml.dist ; tail -n1 <phpunit.xml.dist) > phpunit.xml
: Skip Mockery usage
find tests -name \*.php -exec grep -q Mockery {} \; -delete -print

phpab \
  --template fedora \
  --output bootstrap.php \
  tests/unit/

# use auto_prepend_file to ensure build version used first
RETURN_CODE=0
for PHP_EXEC in php php73 php74 php80; do
    if which $PHP_EXEC; then
        $PHP_EXEC -d auto_prepend_file=%{buildroot}%{_datadir}/php/phpDocumentor/Reflection/DocBlock/autoload.php \
            %{_bindir}/phpunit --verbose \
                --bootstrap bootstrap.php \
                || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/phpDocumentor


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 3.2.2-10
- drop mockery/mockery usage

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec  7 2018 Remi Collet <remi@remirepo.net> - 3.2.2-4
- use range dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug  8 2017 Remi Collet <remi@remirepo.net> - 3.2.2-1
- Update to 3.2.2

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 3.2.1-2
- add patch to fix BC break, thanks to Koschei,  from
  https://github.com/phpDocumentor/ReflectionDocBlock/pull/113

* Sat Aug 05 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.1-1
- Update to 3.2.1 (RHBZ #1471379)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.0-1
- Update to 3.2.0 (RHBZ #1471379)

* Fri May  5 2017 Shawn Iwinski <shawn@iwin.ski>, Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1
- raise dependency on PHP 5.5
- add dependency on phpdocumentor/reflection-common
- add dependency on phpdocumentor/type-resolver
- add dependency on webmozart/assert
- switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- update to 2.0.4
- LICENSE is in upstream archive

* Tue Feb  3 2015 Remi Collet <remi@fedoraproject.org> - 2.0.3-2
- add LICENSE from upstream repository

* Fri Dec 19 2014 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- initial package
- open https://github.com/phpDocumentor/ReflectionDocBlock/issues/40
  for missing LICENSE file
