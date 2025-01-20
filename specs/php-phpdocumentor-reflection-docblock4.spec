# Fedora/remirepo spec file for php-phpdocumentor-reflection-docblock4
#
# Copyright (c) 2017-2021 Remi Collet, Shawn Iwinski
#               2014-2015 Remi Collet
#
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    da3fd972d6bafd628114f7e7e036f45944b62e9c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpDocumentor
%global gh_project   ReflectionDocBlock
%global major        4
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-phpdocumentor-reflection-docblock%{major}
Version:        4.3.4
Release:        14%{?dist}
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
BuildRequires:  php(language) >= 7.0
BuildRequires: (php-composer(phpdocumentor/reflection-common) >= 1.0.0 with php-composer(phpdocumentor/reflection-common) <  3)
BuildRequires: (php-composer(phpdocumentor/type-resolver)     >= 0.4.0 with php-composer(phpdocumentor/type-resolver)     <  0.5)
BuildRequires: (php-composer(webmozart/assert)                >= 1.0   with php-composer(webmozart/assert)                <  2)
# From composer.json, require-dev
#        "mockery/mockery": "^1.0",
#        "phpdocumentor/type-resolver": "0.4.*",
#        "phpunit/phpunit": "^6.4",
#        "doctrine/instantiator": "^1.0.5"
BuildRequires: (php-composer(mockery/mockery) >= 1.0 with php-composer(mockery/mockery) <  2)
BuildRequires:  phpunit7
# From phpcompatinfo report for 4.3.2
BuildRequires:  php-reflection
BuildRequires:  php-filter
BuildRequires:  php-pcre
BuildRequires:  php-spl
%endif

# From composer.json, require
#        "php": ">=7.0"
#        "phpdocumentor/reflection-common": "^1.0.0 || ^2.0.0",
#        "phpdocumentor/type-resolver": "~0.4 || ^1.0.0",
#        "webmozart/assert": "^1.0"
Requires:       php(language) >= 7.0
Requires:      (php-composer(phpdocumentor/reflection-common) >= 1.0.0 with php-composer(phpdocumentor/reflection-common) < 3)
Requires:      (php-composer(phpdocumentor/type-resolver)     >= 0.4.0 with php-composer(phpdocumentor/type-resolver)     < 2)
Requires:      (php-composer(webmozart/assert)                >= 1.0   with php-composer(webmozart/assert)                < 2)
# From phpcompatinfo report for 4.3.2
Requires:       php-reflection
Requires:       php-filter
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpdocumentor/reflection-docblock) = %{version}


%description
The ReflectionDocBlock component of phpDocumentor provides a DocBlock
parser that is fully compatible with the PHPDoc standard.

With this component, a library can provide support for annotations via
DocBlocks or otherwise retrieve information that is embedded in a DocBlock.

Autoloader: %{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1

sed 's#vendor/mockery/mockery/library/Mockery#%{_datadir}/php/Mockery1#' phpunit.xml.dist \
    > phpunit.xml

# single directory tree
mv src/*php src/DocBlock/


%build
phpab \
  --template fedora \
  --output src/DocBlock/autoload.php \
  src/

cat <<AUTOLOAD | tee -a src/DocBlock/autoload.php

\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/phpDocumentor/Reflection2/autoload-common.php',
        '%{_datadir}/php/phpDocumentor/Reflection/autoload-common.php',
    ], [
        '%{_datadir}/php/phpDocumentor/Reflection2/autoload-type-resolver.php',
        '%{_datadir}/php/phpDocumentor/Reflection/autoload-type-resolver.php',
    ],
    '%{_datadir}/php/Webmozart/Assert/autoload.php',
]);
AUTOLOAD


%install
mkdir -p            %{buildroot}%{_datadir}/php/phpDocumentor/Reflection
cp -pr src/DocBlock %{buildroot}%{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}


%check
%if %{with_tests}
sed -e '/autoload.php/d' -i examples/*.php examples/*/*.php

phpab \
  --template fedora \
  --output bootstrap.php \
  tests/unit/

cat <<BOOTSTRAP | tee -a bootstrap.php

\Fedora\Autoloader\Dependencies::required([
	// only v0.4 at buidtime
    '%{_datadir}/php/phpDocumentor/Reflection/autoload-type-resolver.php',
    '%{buildroot}%{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}/autoload.php',
    '%{_datadir}/php/Mockery1/autoload.php',
]);
BOOTSTRAP

# use auto_prepend_file to ensure build version used first
RETURN_CODE=0
for PHP_EXEC in php php73 php74 php80; do
    if which $PHP_EXEC; then
        $PHP_EXEC -d auto_prepend_file=$PWD/bootstrap.php \
            %{_bindir}/phpunit7 \
                --no-coverage \
                --bootstrap bootstrap.php \
                --verbose || RETURN_CODE=1
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
%dir %{_datadir}/php/phpDocumentor/Reflection
     %{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 4.3.4-5
- fix FTBFS with PHP 8

* Fri Jan 29 2021 Remi Collet <remi@remirepo.net> - 4.3.4-4
- switch to phpunit7 and fix FTBFS

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 4.3.4-1
- update to 4.3.4

* Fri Dec 20 2019 Remi Collet <remi@remirepo.net> - 4.3.3-1
- update to 4.3.3

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 4.3.2-1
- update to 4.3.2
- allow reflection-common 1.0
- allow type-resolver 1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May  2 2019 Remi Collet <remi@remirepo.net> - 4.3.1-1
- update to 4.3.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 31 2018 Remi Collet <remi@remirepo.net> - 4.3.0-1
- Update to 4.3.0

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 4.2.0-1
- Update to 4.2.0
- rename to php-phpdocumentor-reflection-docblock4
- move to /usr/share/php/phpDocumentor/Reflection/DocBlock4
- raise dependency on PHP 7.0
- raise dependency on phpdocumentor/type-resolver 0.4.0
- use phpunit6 and php-mockery for test suite

* Tue Aug  8 2017 Remi Collet <remi@remirepo.net> - 3.2.2-1
- Update to 3.2.2

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 3.2.1-2
- add patch to fix BC break, thanks to Koschei,  from
  https://github.com/phpDocumentor/ReflectionDocBlock/pull/113

* Sat Aug 05 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.1-1
- Update to 3.2.1 (RHBZ #1471379)

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
