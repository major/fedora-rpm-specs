#
# Fedora spec file for php-phpdocumentor-reflection-docblock2
#
# Copyright (c) 2017-2021 Remi Collet, Shawn Iwinski
#               2014-2015 Remi Collet
#
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    e6a969a640b00d8daa3c66518b0405fb41ae0c4b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpDocumentor
%global gh_project   ReflectionDocBlock
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-phpdocumentor-reflection-docblock2
Version:        2.0.5
Release:        18%{?dist}
Summary:        DocBlock parser (Version 2)

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-composer(phpunit/phpunit)
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, require
#        "php": ">=5.3.3"
# From composer.json, suggest
#        "dflydev/markdown": "1.0.*",
#        "erusev/parsedown": "~0.7"
Requires:       php(language) >= 5.3.3
# From phpcompatinfo report for 2.0.3
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpdocumentor/reflection-docblock) = %{version}

# Package rename (php-phpdocumentor-reflection-docblock => php-phpdocumentor-reflection-docblock2)
Obsoletes:      php-phpdocumentor-reflection-docblock < 2.0.4-5
Provides:       php-phpdocumentor-reflection-docblock = %{version}-%{release}
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

mv src/phpDocumentor/Reflection/DocBlock src/phpDocumentor/Reflection/DocBlock2
mv src/phpDocumentor/Reflection/DocBlock.php src/phpDocumentor/Reflection/DocBlock2.php


%build
phpab \
  --template fedora \
  --output   src/phpDocumentor/Reflection/DocBlock2/autoload.php \
  src/phpDocumentor/Reflection


%install
mkdir -p     %{buildroot}%{_datadir}/php
cp -pr src/* %{buildroot}%{_datadir}/php


%check
%if %{with_tests}
mkdir vendor
touch vendor/autoload.php

: Skip test known to fail
sed 's/function testInvalidTagBlock/function SKIP_testInvalidTagBlock/' \
  -i tests/phpDocumentor/Reflection/DocBlockTest.php

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in %{_bindir}/php %{?rhel:php54 php55} php56 php70 php71 php72 php73 php74 php80 php81; do
    if [ "%{_bindir}/php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC -d allow_url_include=1 \
          -d auto_prepend_file=%{buildroot}%{_datadir}/php/phpDocumentor/Reflection/DocBlock2/autoload.php \
          %{_bindir}/phpunit --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/phpDocumentor
%dir %{_datadir}/php/phpDocumentor/Reflection
     %{_datadir}/php/phpDocumentor/Reflection/DocBlock2*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Shawn Iwinski <shawn@iwin.ski> - 2.0.5-10
- Fix "FTBFS in Fedora rawhide/f35" (RHBZ #1987851)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Remi Collet <remi@remirepo.net> - 2.0.5-1
- Update to 2.0.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May  5 2017 Remi Collet <remi@remirepo.net> - 2.0.4-6
- fix autoloader order in test suite

* Thu Apr 13 2017 Shawn Iwinski <shawn@iwin.ski> - 2.0.4-5
- Package rename (php-phpdocumentor-reflection-docblock =>
  php-phpdocumentor-reflection-docblock2)
- Switch autoloader to php-composer(fedora/autoloader)

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
