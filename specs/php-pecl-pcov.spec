# Fedora spec file for php-pecl-pcov
# with SCL stuff removed from:
#
# remirepo spec file for php-pecl-pcov
#
# Copyright (c) 2019-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global pecl_name pcov
%global ini_name  40-%{pecl_name}.ini
%global sources   %{pecl_name}-%{version}

Summary:        Code coverage driver
Name:           php-pecl-%{pecl_name}
Version:        1.0.12
Release:        2%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 7.1
BuildRequires:  php-pear

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name}               = %{version}
Provides:       php-%{pecl_name}%{?_isa}       = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
A self contained php-code-coverage compatible driver for PHP7.


%prep
%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_PCOV_VERSION/{s/.* "//;s/".*$//;p}' php_pcov.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever:-%{prever}}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; Configuration

; The recommended defaults for production should be:
pcov.enabled = 0

; The recommended defaults for development should be:
;pcov.enabled = 1
;pcov.directory = /path/to/your/source/directory
;pcov.exclude = ''
;pcov.initial.memory = 65536
;pcov.initial.files = 64
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --enable-pcov \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Install config file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=modules/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

: Upstream test suite for NTS extension
TEST_PHP_ARGS="-n -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q -P --show-diff


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec  4 2024 Remi Collet <remi@remirepo.net> - 1.0.12-1
- update to 1.0.12
- drop patch merged upstream

* Thu Oct 17 2024 Remi Collet <remi@fedoraproject.org> - 1.0.11-13
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.0.11-12
- rebuild for https://fedoraproject.org/wiki/Changes/php84
- add patch for PHP 8.4 from
  https://github.com/krakjoe/pcov/pull/111

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 1.0.11-10
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.0.11-7
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 1.0.11-5
- use SPDX license ID

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.0.11-4
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Remi Collet <remi@remirepo.net> - 1.0.11-1
- update to 1.0.11

* Wed Nov 24 2021 Remi Collet <remi@remirepo.net> - 1.0.10-1
- update to 1.0.10

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 1.0.9-3
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Remi Collet <remi@remirepo.net> - 1.0.9-1
- update to 1.0.9

* Fri Mar 19 2021 Remi Collet <remi@remirepo.net> - 1.0.7-1
- update to 1.0.7

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 1.0.6-5
- rebuild for https://fedoraproject.org/wiki/Changes/php80
- add upstream patch for test suite with PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.0.6-1
- update to 1.0.6
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Remi Collet <remi@remirepo.net> - 1.0.5-1
- update to 1.0.5

* Mon Jun  3 2019 Remi Collet <remi@remirepo.net> - 1.0.4-1
- update to 1.0.4

* Mon May  6 2019 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3

* Sun Mar 31 2019 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Mon Mar 25 2019 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Fri Feb  1 2019 Remi Collet <remi@remirepo.net> - 1.0.0-2
- cleanup SCL stuff for Fedora review

* Wed Jan 30 2019 Remi Collet <remi@remirepo.net> - 1.0.0-1
- update to 1.0.0 (stable)
- raise dependency on PHP 7.1
- switch to production recommended configuration

* Tue Jan 22 2019 Remi Collet <remi@remirepo.net> - 0.9.0-1
- initial package, version 0.9.0 (beta)
