# Fedora spec file for php-smbclient
# with SCL compatibility removed, from
#
# remirepo spec file for php-smbclient
#
# Copyright (c) 2015-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global pecl_name  smbclient
%global ini_name   40-%{pecl_name}.ini
# Test suite requires a Samba server and configuration file
%bcond_with        tests
%global sources    %{pecl_name}-%{version}%{?prever}

Name:           php-smbclient
Version:        1.1.2
Release:        2%{?dist}
Summary:        PHP wrapper for libsmbclient

License:        BSD-2-Clause
URL:            https://github.com/eduardok/libsmbclient-php
Source0:        https://pecl.php.net/get/%{sources}.tgz
%if %{with tests}
Source2:        %{pecl_name}-phpunit.xml
%endif

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  libsmbclient-devel > 3.6
%if %{with tests}
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires:  samba
%endif

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Renamed (and "php -m" reports both smbclient and libsmbclient)
Obsoletes:      php-libsmbclient         < 0.8.0-0.2
Provides:       php-libsmbclient         = %{version}-%{release}
Provides:       php-libsmbclient%{?_isa} = %{version}-%{release}
# PECL
Provides:       php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
%{pecl_name} is a PHP extension that uses Samba's libsmbclient
library to provide Samba related functions and 'smb' streams
to PHP programs.


%prep
%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Check extension version
ver=$(sed -n '/define PHP_SMBCLIENT_VERSION/{s/.* "//;s/".*$//;p}' php_smbclient.h)
if test "$ver" != "%{version}%{?prever}"; then
   : Error: Upstream VERSION version is ${ver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

cat  << 'EOF' | tee %{ini_name}
; Enable %{summary} extension module
extension=%{pecl_name}.so
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Install configuration
install -Dpm 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with tests}
: Upstream test suite for the extension
cp %{SOURCE2} phpunit.xml

%{__php} \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    %{_bindir}/phpunit --verbose
%endif


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Wed Oct 16 2024 Remi Collet <remi@fedoraproject.org> - 1.1.1-11
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.1.1-10
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Thu Aug 22 2024 Remi Collet <remi@remirepo.net> - 1.1.1-9
- rebuild for broken ABI in 8.3.10, fixed in 8.3.11RC2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 1.1.1-7
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Mon Jan 29 2024 Remi Collet <remi@remirepo.net> - 1.1.1-6
- fix incompatible pointer types using upstream patch
- build out of sources tree

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.1.1-3
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1
- drop patch merged upstream

* Tue Apr  4 2023 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- drop patch merged upstream
- add workaround for regression in libsmbclient 4.16.9/4.17.5
  from https://github.com/eduardok/libsmbclient-php/pull/100

* Fri Mar 31 2023 Remi Collet <remi@remirepo.net> - 1.0.6-9
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.0.6-7
- rebuild for https://fedoraproject.org/wiki/Changes/php82
- add fix from https://github.com/eduardok/libsmbclient-php/pull/94

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 1.0.6-4
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 1.0.6-2
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Mon Mar  1 2021 Remi Collet <remi@remirepo.net> - 1.0.6-1
- update to 1.0.6

* Mon Feb 15 2021 Remi Collet <remi@remirepo.net> - 1.0.5-1
- update to 1.0.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Remi Collet <remi@remirepo.net> - 1.0.4-1
- update to 1.0.4

* Thu Jan 21 2021 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3

* Thu Jan 21 2021 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Tue Jan  5 2021 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.0.0-4
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- update to 1.0.0

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 0.9.0-8
- Rebuild for https://fedoraproject.org/wiki/Changes/php73
- add patch for PHP 7.3 from
  https://github.com/eduardok/libsmbclient-php/pull/60

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 0.9.0-5
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 0.9.0-4
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Remi Collet <remi@fedoraproject.org> - 0.9.0-1
- update to 0.9.0 (stable)

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 0.8.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 0.8.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Wed Mar  2 2016 Remi Collet <remi@fedoraproject.org> - 0.8.0-1
- update to 0.8.0 (stable, no change)
- drop scriptlets (replaced by file triggers in php-pear)
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.5.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  8 2015 Remi Collet <remi@fedoraproject.org> - 0.8.0-0.4.RC1
- now available on PECL
- use sources from pecl
- add virtual provides
- add scriptlets for pecl registry (un)registration

* Thu Sep 17 2015 Remi Collet <remi@fedoraproject.org> - 0.8.0-0.3.rc1
- cleanup SCL compatibility for Fedora

* Wed Sep 16 2015 Remi Collet <rcollet@redhat.com> - 0.8.0-0.2.rc1
- update to 0.8.0-rc1
- rename from php-libsmbclient to php-smbclient
  https://github.com/eduardok/libsmbclient-php/pull/26

* Thu Sep  3 2015 Remi Collet <rcollet@redhat.com> - 0.8.0-0.1.20150909gita65127d
- update to 0.8.0-dev
- https://github.com/eduardok/libsmbclient-php/pull/20 streams support
- https://github.com/eduardok/libsmbclient-php/pull/23 PHP 7

* Thu Sep  3 2015 Remi Collet <rcollet@redhat.com> - 0.7.0-1
- Update to 0.7.0
- drop patches merged upstream
- license is now BSD

* Wed Sep  2 2015 Remi Collet <rcollet@redhat.com> - 0.6.1-1
- Initial packaging of 0.6.1
- open https://github.com/eduardok/libsmbclient-php/pull/17
  test suite configuration
- open https://github.com/eduardok/libsmbclient-php/pull/18
  add reflection and improve phpinfo
- open https://github.com/eduardok/libsmbclient-php/issues/19
  missing license file
