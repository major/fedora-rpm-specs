# Fedora spec file for php-pecl-uopz
# Without SCL compatibility stuff, from:
#
# remirepo spec file for php-pecl-uopz
#
# Copyright (c) 2014-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global with_zts   0%{!?_without_zts:%{?__ztsphp:1}}
%global pecl_name  uopz
%global ini_name   05-%{pecl_name}.ini

Summary:        User Operations for Zend
Name:           php-pecl-%{pecl_name}
Version:        7.1.1
Release:        14%{?dist}
License:        PHP-3.01
URL:            http://pecl.php.net/package/%{pecl_name}
Source0:        http://pecl.php.net/get/%{pecl_name}-%{version}.tgz

Patch0:         %{pecl_name}-build.patch

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 8.0
BuildRequires:  php-pear

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name}               = %{version}
Provides:       php-%{pecl_name}%{?_isa}       = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}

Conflicts:      php-pecl-xdebug < 2.9.4


%description
The uopz extension is focused on providing utilities to aid with unit testing PHP code.

It supports the following activities:
- Intercepting function execution
- Intercepting object creation
- Hooking into function execution
- Manipulation of function statics
- Manipulation of function flags
- Redefinition of constants
- Deletion of constants
- Runtime creation of functions and methods

Note: All of the above activities are compatible with opcache

Documentation: http://php.net/uopz


%prep
%setup -q -c
mv %{pecl_name}-%{version} NTS

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd NTS
%patch -P0 -p1

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_UOPZ_VERSION/{s/.* "//;s/".*$//;p}' uopz.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

# Create configuration files
cat << EOF | tee %{ini_name}
; Enable '%{summary}' extension module
extension=%{pecl_name}.so

; Configuration
; See http://php.net/manual/en/uopz.configuration.php

; If enabled, uopz should stop having any effect on the engine.
;uopz.disable = 0

; Whether to allow the execution of exit opcodes or not.
; This setting can be overridden during runtime by calling uopz_allow_exit().
;uopz.exit = 0
EOF

%if %{with_zts}
# Duplicate source tree for NTS / ZTS build
cp -pr NTS ZTS
%endif


%build
cd NTS
%{_bindir}/phpize
%configure \
    --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
    --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
make -C NTS install INSTALL_ROOT=%{buildroot}

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
%if "%{php_version}" >= "8.1"
# https://github.com/krakjoe/uopz/issues/160
rm ?TS/tests/012.phpt
%endif
%if "%{php_version}" >= "8.2"
rm ?TS/tests/019.phpt
%endif
%if "%{php_version}" >= "8.3"
rm ?TS/tests/007.phpt
%endif

cd NTS
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite  for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php

%if %{with_zts}
cd ../ZTS
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite  for ZTS extension
TEST_PHP_EXECUTABLE=%{_bindir}/zts-php \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{_bindir}/zts-php -n run-tests.php
%endif


%files
%license NTS/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 7.1.1-12
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 7.1.1-9
- rebuild for https://fedoraproject.org/wiki/Changes/php83
- skip 1 test failing with 8.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 7.1.1-7
- use SPDX license ID

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 7.1.1-6
- rebuild for https://fedoraproject.org/wiki/Changes/php82
- skip tests failing with 8.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec  3 2021 Remi Collet <remi@remirepo.net> - 7.1.1-3
- fix FTBFS with 8.1.1

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 7.1.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Tue Oct 19 2021 Remi Collet <remi@remirepo.net> - 7.1.1-1
- update to 7.1.1

* Fri Aug  6 2021 Remi Collet <remi@remirepo.net> - 7.1.0-1
- update to 7.1.0

* Wed Jul 28 2021 Remi Collet <remi@remirepo.net> - 7.0.0-1
- update to 7.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar  5 2021 Remi Collet <remi@remirepo.net> - 6.1.2-4
- rebuild for https://fedoraproject.org/wiki/Changes/php80
- add upstream patches for PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Remi Collet <remi@remirepo.net> - 6.1.2-1
- update to 6.1.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 6.1.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Wed Sep 18 2019 Remi Collet <remi@remirepo.net> - 6.1.1-1
- update to 6.1.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Remi Collet <remi@remirepo.net> - 6.1.0-1
- update to 6.1.0

* Wed Feb  6 2019 Remi Collet <remi@remirepo.net> - 6.0.1-2
- update to 6.0.1
- update provided default configuration
- update package description from upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Remi Collet <remi@remirepo.net> - 6.0.0-1
- update to 6.0.0

* Wed Jan  2 2019 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0
- raise dependency on PHP 7.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 5.0.2-3
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 5.0.2-2
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug  3 2017 Remi Collet <remi@remirepo.net> - 5.0.2-1
- update to 5.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 5.0.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Thu Oct 13 2016 Remi Collet <remi@fedoraproject.org> - 5.0.1-1
- cleanup for Fedora review

* Wed Sep 14 2016 Remi Collet <remi@fedoraproject.org> - 5.0.1-3
- rebuild for PHP 7.1 new API version

* Thu Jun  9 2016 Remi Collet <remi@fedoraproject.org> - 5.0.1-2
- add upstream patch for PHP 7.1

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 5.0.1-1
- update to 5.0.1

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 5.0.0-1
- update to 5.0.0 for PHP 7
- sources from github (not yet released on pecl)

* Tue Mar  8 2016 Remi Collet <remi@fedoraproject.org> - 2.0.7-2
- adapt for F24

* Wed Mar 04 2015 Remi Collet <remi@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7
- drop runtime dependency on pear, new scriptlets

* Wed Dec 24 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1.1
- Fedora 21 SCL mass rebuild

* Wed Oct 15 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6
- don't provide test suite

* Tue Aug 26 2014 Remi Collet <rcollet@redhat.com> - 2.0.5-2
- improve SCL build

* Thu Jun 05 2014 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5 (stable)

* Tue Apr  8 2014 Remi Collet <remi@fedoraproject.org> - 2.0.4-2
- add numerical prefix to extension configuration files

* Fri Apr 04 2014 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4 (stable)
- improve uopz.ini (comments)

* Thu Apr 03 2014 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3 (stable)

* Wed Apr 02 2014 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2 (stable)

* Tue Apr 01 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 (stable)

* Mon Mar 31 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0 (2014-03-31 06:00:49, stable)

* Sun Mar 30 2014 Remi Collet <remi@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11 (2014-03-30 14:05:44, beta)

* Fri Mar 28 2014 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 (2014-03-28 00:48:31, beta)

* Thu Mar 27 2014 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4 (2014-03-27 18:34:03, beta)

* Thu Mar 27 2014 Remi Collet <remi@fedoraproject.org> - 1.0.4-0
- pre-release test build

* Tue Mar 25 2014 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 (2014-03-24 19:37:04, beta)

* Mon Mar 24 2014 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (2014-03-24 10:34:02, beta)

* Mon Mar 24 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (2014-03-23 19:03:27, beta)

* Sun Mar 23 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package, version 1.0.0 (12:55, beta)
