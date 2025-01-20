# Fedora spec file for php-geos
# Without SCL compatibility stuff, from:
#
# remirepo spec file for php-geos
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without tests

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global pecl_name  geos
%global with_zts   0%{!?_without_zts:%{?__ztsphp:1}}
%global ini_name   40-%{pecl_name}.ini
%global sources    %{name}
%global _configure ../%{sources}/configure

Name:           php-%{pecl_name}
Version:        1.0.0
Release:        35%{?dist}

Summary:        PHP module for GEOS

# See COPYING
License:        LGPL-2.1-or-later AND MIT
URL:            http://trac.osgeo.org/geos
Source0:        https://git.osgeo.org/gogs/geos/php-geos/archive/%{version}%{?prever}.tar.gz

# https://git.osgeo.org/gitea/geos/php-geos/issues/20
Patch0:         0001-fix-test-for-7.3-int-vs-integer.patch
Patch1:         0002-fix-error-message-with-php-7-Wformat-warnings-raised.patch
# https://git.osgeo.org/gitea/geos/php-geos/issues/24
Patch2:         0003-add-all-arginfo-and-fix-build-with-PHP-8.patch
Patch4:         0005-fix-for-8.0.0RC1.patch
# https://git.osgeo.org/gitea/geos/php-geos/issues/25
Patch3:         0004-fix-all-zend_parse_parameters-call-to-use-zend_long.patch
# https://git.osgeo.org/gitea/geos/php-geos/issues/27
Patch5:         0006-fix-__toString-with-8.2.patch
# https://git.osgeo.org/gitea/geos/php-geos/issues/32
Patch6:         0001-Fix-incompatible-pointer-types.patch

ExcludeArch:    %{ix86}

BuildRequires:  php-devel
BuildRequires:  php-pear
# Test failures with 3.3 (EL-6)
BuildRequires:  geos-devel >= 3.4

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Dropped from geos
Obsoletes:      geos-php        <= 3.5.0
Provides:       geos-php         = 1:%{version}-%{release}
Provides:       geos-php%{?_isa} = 1:%{version}-%{release}


%description
PHP module for GEOS.


%prep
%setup -q -c

cd %{sources}
%patch -P0 -p1 -b .test
%patch -P1 -p1 -b .wformat
%patch -P2 -p1 -b .arginfo
%patch -P3 -p1 -b .zendlong
%patch -P4 -p1 -b .arg
%patch -P5 -p1 -b .php82
%patch -P6 -p1 -b .pointers

sed -e '/PHP_GEOS_VERSION/s/"0.0"/"%{version}%{?prever}"/' -i php_geos.h

# Check extension version
ver=$(sed -n '/define PHP_GEOS_VERSION/{s/.* "//;s/".*$//;p}' php_geos.h)
if test "$ver" != "%{version}%{?prever}%{?gh_date:-dev}"; then
   : Error: Upstream VERSION version is ${ver}, expecting %{version}%{?prever}%{?gh_date:-dev}.
   exit 1
fi
cd ..

cat  << 'EOF' | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

mkdir NTS
%if %{with_zts}
mkdir ZTS
%endif


%build
cd %{sources}
%{__phpize}

cd ../NTS
%configure --with-php-config=%{__phpconfig}
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%configure --with-php-config=%{__ztsphpconfig}
make %{?_smp_mflags}
%endif


%install
make -C NTS install INSTALL_ROOT=%{buildroot}

# install configuration
install -Dpm 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -Dpm 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif


%check
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with_zts}
: Minimal load test for NTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%endif

%if %{with tests}
cd %{sources}
if pkg-config geos --atleast-version 3.12; then
# See https://git.osgeo.org/gitea/geos/php-geos/issues/31
# ignore failing test with geos 3.12
rm tests/002_WKTWriter.phpt
rm tests/004_WKBWriter.phpt
rm tests/005_WKBReader.phpt
fi
if pkg-config geos --atleast-version 3.8; then
# See https://git.osgeo.org/gitea/geos/php-geos/issues/23
# ignore failing test with geos 3.8
rm tests/001_Geometry.phpt
fi
%ifarch ppc64 ppc64le aarch64 armv7hl s390 s390x
# see https://git.osgeo.org/gogs/geos/php-geos/issues/17
# ignore failing tests
rm -f tests/001_Geometry.phpt
rm -f tests/005_WKBReader.phpt
%endif

: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php -q --show-diff || ret=1

%if %{with_zts}
: Upstream test suite for ZTS extension
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
%{__ztsphp} -n run-tests.php -q --show-diff || ret=1
%endif

exit $ret
%endif


%files
%license %{sources}/{COPYING,LGPL-2,MIT-LICENSE}
%doc %{sources}/{CREDITS,NEWS,README.md,TODO}

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.0.0-34
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 1.0.0-32
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Mon Jan 29 2024 Remi Collet <remi@remirepo.net> - 1.0.0-31
- fix incompatible pointer types
  using patch from https://git.osgeo.org/gitea/geos/php-geos/issues/32

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.0.0-28
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Wed Jul 26 2023 Remi Collet <remi@remirepo.net> - 1.0.0-27
- build out of sources tree
- ignore 3 tests failing with libgeos 3.12 #2226098

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Remi Collet <remi@remirepo.net> - 1.0.0-27
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.0.0-25
- rebuild for https://fedoraproject.org/wiki/Changes/php82
- add patch for PHP 8.2 from
  https://git.osgeo.org/gitea/geos/php-geos/issues/27

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 1.0.0-22
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 1.0.0-21
- Rebuild (geos)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Sandro Mani <manisandro@gmail.com> - 1.0.0-19
- Rebuild (geos)

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 1.0.0-18
- rebuild for https://fedoraproject.org/wiki/Changes/php80
- open https://git.osgeo.org/gitea/geos/php-geos/issues/24 missing arginfo
- open https://git.osgeo.org/gitea/geos/php-geos/issues/25 zend_long usage

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 1.0.0-17
- Rebuild (geos)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Remi Collet <remi@remirepo.net> - 1.0.0-15
- ignore 1 test failing with geos 3.8, FTBFS #1865218

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.0.0-13
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.0.0-10
- Rebuild for https://fedoraproject.org/wiki/Changes/php73
- open https://git.osgeo.org/gitea/geos/php-geos/issues/20
  fix -Wformat issues + test for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 1.0.0-7
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.0.0-6
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Dan Horák <dan[at]danny.cz> - 1.0.0-2
- ignore failed tests also on s390(x)

* Sat Dec 24 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- update to 1.0.0

* Fri Dec 16 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.4.rc3
- cleanup for Fedora review

* Fri Dec 16 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.rc3
- update to 1.0.0-rc3

* Mon Dec 12 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.rc2
- update to 1.0.0-rc2
- open https://git.osgeo.org/gogs/geos/php-geos/pulls/13 - fix for tests

* Sun Dec 11 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.rc1
- Initial packaging of 1.0.0rc1

