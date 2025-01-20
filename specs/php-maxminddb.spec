# Fedora spec file for php-maxminddb
# Without SCL compatibility from:
#
# remirepo spec file for php-maxminddb
#
# Copyright (c) 2018-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit   5b2d7a721dedfaef9dc20822c5fe7d26f9f8eb90
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner    maxmind
%global gh_project  MaxMind-DB-Reader-php
# Extension
%global pecl_name   maxminddb
%global ini_name    40-%{pecl_name}.ini
# pure PHP library
%global pk_vendor    maxmind-db
%global pk_project   reader
%global _configure   ../ext/configure

%if 0%{?fedora}
%bcond_without       tests
%else
%bcond_with          tests
%endif

Summary:       MaxMind DB Reader extension
Name:          php-maxminddb
Version:       1.12.0
Release:       2%{?dist}
License:       Apache-2.0
URL:           https://github.com/%{gh_owner}/%{gh_project}

Source0:       %{name}-%{version}-%{gh_short}.tgz
Source1:       makesrc.sh

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 7.2
BuildRequires: php-pear  >= 1.10
BuildRequires: pkgconfig(libmaxminddb) >= 1.0.0

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

# Weak dependencies on databases
Recommends:    geolite2-country
Suggests:      geolite2-city

# PECL
Provides:       php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
MaxMind DB is a binary file format that stores data indexed by
IP address subnets (IPv4 or IPv6).

This optional PHP C Extension is a drop-in replacement for
MaxMind\Db\Reader.

Databases are available in geolite2-country and geolite2-city packages.


%package -n php-%{pk_vendor}-%{pk_project}
Summary:       MaxMind DB Reader

BuildArch:     noarch
BuildRequires: php-fedora-autoloader-devel
%if %{with tests}
BuildRequires: php-bcmath
BuildRequires: php-gmp
# from composer.json "require-dev": {
#        "friendsofphp/php-cs-fixer": "*",
#        "phpunit/phpunit": ">=8.0.0,<10.0.0",
#        "php-coveralls/php-coveralls": "^2.1",
#        "phpunit/phpcov": ">=6.0.0",
#        "squizlabs/php_codesniffer": "3.*"
BuildRequires: phpunit8
%endif

# from composer.json "require": {
#        "php": ">=7.2"
Requires:      php(language) >= 7.2
# from composer.json "suggest": {
#        "ext-bcmath": "bcmath or gmp is required for decoding larger integers with the pure PHP decoder",
#        "ext-gmp": "bcmath or gmp is required for decoding larger integers with the pure PHP decoder",
#        "ext-maxminddb": "A C-based database decoder that provides significantly faster lookups"
Recommends:    php-bcmath
Recommends:    php-gmp
Recommends:    php-maxminddb
# from composer.json "conflict": {
#        "ext-maxminddb": "<1.11.1,>=2.0.0"
Conflicts:     php-maxminddb < %{version}
# Weak dependencies on databases
Recommends:    geolite2-country
Suggests:      geolite2-city
# From phpcompatifo report for 1.3.0
Requires:      php-filter
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

Provides:      php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description -n php-%{pk_vendor}-%{pk_project}
MaxMind DB Reader PHP API.

MaxMind DB is a binary file format that stores data indexed by
IP address subnets (IPv4 or IPv6).

Databases are available in geolite2-country and geolite2-city packages.

The extension available in php-maxminddb package allow better
performance.

Autoloader: %{_datadir}/php/MaxMind/Db/Reader/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%{_bindir}/phpab \
    --template fedora \
    --output src/MaxMind/Db/Reader/autoload.php \
    src/MaxMind/Db

cd ext
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_MAXMINDDB_VERSION/{s/.* "//;s/".*$//;p}'  php_maxminddb.h)
if test "x${extver}" != "x%{version}%{?gh_date:-dev}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat << 'EOF' | tee %{ini_name}
; Enable '%{pecl_name}' extension module
extension = %{pecl_name}.so
EOF


%build
cd ext
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-php-config=%{__phpconfig} \
    --with-libdir=%{_lib} \
    --with-maxminddb

%make_build


%install
: Install the extension
%make_install -C ext

: Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the extension
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the library
mkdir -p                %{buildroot}%{_datadir}/php/MaxMind
cp -pr src/MaxMind/Db   %{buildroot}%{_datadir}/php/MaxMind/Db


%check
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

ret=0

cd ext
: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff || ret=1

%if %{with tests}
cd ..
: Upstream test suite for the library
for cmd in php80 php81 php82 php83 php84; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 \
      --bootstrap %{buildroot}%{_datadir}/php/MaxMind/Db/Reader/autoload.php \
      --verbose || ret=1
  fi
done

: Upstream test suite for the library with the extension
php --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
  %{_bindir}/phpunit8 \
    --bootstrap %{buildroot}%{_datadir}/php/MaxMind/Db/Reader/autoload.php \
    --verbose || ret=1
%endif
exit $ret


%files
%license LICENSE
%doc *.md
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%files -n php-%{pk_vendor}-%{pk_project}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/MaxMind
     %{_datadir}/php/MaxMind/Db


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 15 2024 Remi Collet <remi@remirepo.net> - 1.12.0-1
- update to 1.12.0

* Fri Oct 18 2024 Remi Collet <remi@fedoraproject.org> - 1.11.1-7
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.11.1-6
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 1.11.1-4
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec  4 2023 Remi Collet <remi@remirepo.net> - 1.11.1-1
- update to 1.11.1

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.11.0-11
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Mon Oct  2 2023 Remi Collet <remi@remirepo.net> - 1.11.0-10
- add missing dependency on fedora/autoloader
- build out of sources tree

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Remi Collet <remi@remirepo.net> - 1.11.0-8
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.11.0-6
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Remi Collet <remi@remirepo.net> - 1.11.0-3
- disable library test suite for EL build

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 1.11.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Tue Oct 19 2021 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1

* Fri Mar  5 2021 Remi Collet <remi@fedoraproject.org> - 1.10.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Feb 10 2021 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 2021 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.9.0

* Fri Oct  2 2020 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0
- now available on pecl
- raise dependency on PHP 7.2
- switch to phpunit8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.5.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Tue Oct  1 2019 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 5.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan  5 2019 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Wed Nov 21 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- cleanup for Fedora review

* Wed Nov 21 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- open https://github.com/maxmind/MaxMind-DB-Reader-php/issues/79
  to report test failure on 32-bit

* Wed Nov 14 2018 Remi Collet <remi@remirepo.net> - 1.3.0-3
- add php-maxmind-db-reader sub-package providing the library
- open https://github.com/maxmind/MaxMind-DB-Reader-php/issues/77
  to report test failures on 32-bit

* Thu Nov  8 2018 Remi Collet <remi@remirepo.net> - 1.3.0-2
- add upstream patches from merged PRs
- add weak dependencies on geolite2 databases

* Wed Nov  7 2018 Remi Collet <remi@remirepo.net> - 1.3.0-1
- new package, version 1.3.0
- open https://github.com/maxmind/MaxMind-DB-Reader-php/pull/73 pkg-config
- open https://github.com/maxmind/MaxMind-DB-Reader-php/pull/74 MINFO
- open https://github.com/maxmind/MaxMind-DB-Reader-php/pull/75 arginfo
