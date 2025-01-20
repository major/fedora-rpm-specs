#
# Fedora spec file for php-masterminds-html5
#
# Copyright (c) 2015-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Masterminds
%global github_name      html5-php
%global github_version   2.7.6
%global github_commit    897eb517a343a2281f11bc5556d6548db7d93947

%global composer_vendor  masterminds
%global composer_project html5

# "php" : ">=5.3.0"
%global php_min_ver 5.3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       7%{?dist}
Summary:       An HTML5 parser and serializer

License:       MIT
URL:           http://masterminds.github.io/html5-php
# GitHub export does not include tests.
# Run php-league-container-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Autoload generation
BuildRequires: %{_bindir}/phpab
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit8
BuildRequires: php-ctype
BuildRequires: php-dom
## phpcompatinfo (computed from version 2.7.0)
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-ctype
Requires:      php-dom
# phpcompatinfo (computed from version 2.7.0)
Requires:      php-iconv
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# notice: xml only detected for utf8_decode

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The need for an HTML5 parser in PHP is clear. This project initially began with
the seemingly abandoned html5lib project original source. But after some initial
refactoring work, we began a new parser.

* An HTML5 serializer
* Support for PHP namespaces
* Composer support
* Event-based (SAX-like) parser
* DOM tree builder
* Interoperability with QueryPath


%prep
%setup -qn %{github_name}-%{github_commit}

: Docs
mkdir -p docs/{Parser,Serializer}
mv composer.json *.md docs/
mv src/HTML5/Parser/*.md docs/Parser/
mv src/HTML5/Serializer/*.md docs/Serializer/


%build
: Generate autoloader
# Vendor-level autoloader to pick up "Masterminds/HTML5" class
%{_bindir}/phpab --nolower --output src/autoload-html5.php src


%install
mkdir -p  %{buildroot}%{phpdir}/Masterminds
cp -pr src/* %{buildroot}%{phpdir}/Masterminds/
# Project-level autoloader for consistency with other pkgs
ln -s ../autoload-html5.php %{buildroot}%{phpdir}/Masterminds/HTML5/autoload.php


%check
%if %{with_tests}
: Generate test autoloader
%{_bindir}/phpab --nolower --output test/autoload.php test

: Create mock Composer autoloader
mkdir vendor
cat > vendor/autoload.php <<'AUTOLOAD'
<?php

require '%{buildroot}%{phpdir}/Masterminds/HTML5/autoload.php';
require __DIR__ . '/../test/autoload.php';
AUTOLOAD

: fix for phpunit8
find test \
  -name \*.php \
  -exec sed \
    -e 's/function setUp()/function setUp():void/' \
    -i {} \;

sed -e 's/assertContains(/assertStringContainsString(/' \
    -i test/HTML5/Html5Test.php

grep -v blacklist < phpunit.xml.dist | \
  grep -v '<file' > phpunit.xml

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in "" php74 php80 php81 php82; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc docs/*
%{phpdir}/Masterminds


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 12 2022 Remi Collet <remi@remirepo.net> - 2.7.6-1
- update to 2.7.6

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul  2 2021 Remi Collet <remi@remirepo.net> - 2.7.5-1
- update to 2.7.5

* Wed Mar 17 2021 Remi Collet <remi@remirepo.net> - 2.7.4-1
- update to 2.7.4
- drop patch merged upstream
- switch to phpunit8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0
- add patch for PHP 7.4 from
  https://github.com/Masterminds/html5-php/pull/170

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.6.0-1
- Update to 2.6.0 (RHBZ #1687215)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.0-1
- Update to 2.3.0 (RHBZ #1488271)
- Test with SCLs if available

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 25 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.2-1
- Updated to 2.2.2 (RHBZ #1378444)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1.2-1
- Updated to 2.1.2 (RHBZ #1229011)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1.1-1
- Initial package
