# Fedora spec file for php-pecl-rpminfo
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-rpminfo
#
# SPDX-FileCopyrightText:  Copyright 2024 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pecl_name  rpminfo
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Summary:        RPM information
Name:           php-pecl-%{pecl_name}
Version:        1.2.0
Release:        2%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(rpm) >= 4.13
BuildRequires:  php-devel >= 8.0
BuildRequires:  php-pear

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name}               = %{version}
Provides:       php-%{pecl_name}%{?_isa}       = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:       php-pie(remi/%{pecl_name})     = %{version}


%description
Retrieve RPM information using librpm, from local
RPM file or from installed packages database.

Documentation: https://www.php.net/rpminfo


%prep
%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_RPMINFO_VERSION/{s/.* "//;s/".*$//;p}' php_rpminfo.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' extension module
extension=%{pecl_name}.so
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --enable-rpminfo \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}
%make_install

# install config file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}

# Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

# Upstream test suite  for NTS extension
TEST_PHP_ARGS="-n -d extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 19 2024 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.1.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Tue Sep  3 2024 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 1.1.0-4
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 10 2023 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Fri Oct 13 2023 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Fri Oct 13 2023 Remi Collet <remi@remirepo.net> - 1.0.0-2
- add upstream patch to avoid stack smashing on 32-bit

* Fri Oct 13 2023 Remi Collet <remi@remirepo.net> - 1.0.0-1
- update to 1.0.0

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 0.7.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Tue Sep 26 2023 Remi Collet <remi@remirepo.net> - 0.7.0-1
- update to 0.7.0
- build out of sources tree

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 19 2023 Remi Collet <remi@remirepo.net> - 0.6.0-9
- rebuild for librpm

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 0.6.0-8
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 0.6.0-6
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 0.6.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Remi Collet <remi@remirepo.net> - 0.6.0-1
- update to 0.6.0

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 0.5.1-3
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Remi Collet <remi@remirepo.net> - 0.5.1-1
- update to 0.5.1

* Fri Aug 21 2020 Remi Collet <remi@remirepo.net> - 0.5.0-2
- improve package description
- ignore 2 (expected) failed tests on F33, FTBFS #1865223

* Tue Apr  7 2020 Remi Collet <remi@remirepo.net> - 0.5.0-1
- update to 0.5.0

* Wed Mar 25 2020 Remi Collet <remi@remirepo.net> - 0.4.2-1
- update to 0.4.2

* Wed Mar 18 2020 Remi Collet <remi@remirepo.net> - 0.4.1-1
- update to 0.4.1

* Fri Mar 13 2020 Remi Collet <remi@remirepo.net> - 0.4.0-1
- update to 0.4.0 (stable)

* Thu Mar 12 2020 Remi Collet <remi@remirepo.net> - 0.3.1-1
- update to 0.3.1

* Thu Mar 12 2020 Remi Collet <remi@remirepo.net> - 0.3.0-1
- update to 0.3.0

* Wed Mar 11 2020 Remi Collet <remi@remirepo.net> - 0.2.3-1
- update to 0.2.3

* Wed Mar 11 2020 Remi Collet <remi@remirepo.net> - 0.2.2-1
- update to 0.2.2

* Tue Sep 03 2019 Remi Collet <remi@remirepo.net> - 0.2.1-5
- rebuild for 7.4.0RC1

* Tue Jul 23 2019 Remi Collet <remi@remirepo.net> - 0.2.1-4
- rebuild for 7.4.0beta1

* Thu Aug 16 2018 Remi Collet <remi@remirepo.net> - 0.2.1-3
- rebuild for 7.3.0beta2 new ABI

* Wed Jul 18 2018 Remi Collet <remi@remirepo.net> - 0.2.1-2
- rebuild for 7.3.0alpha4 new ABI

* Mon Feb 12 2018 Remi Collet <remi@remirepo.net> - 0.2.1-1
- update to 0.2.1 (beta)

* Thu Feb  8 2018 Remi Collet <remi@remirepo.net> - 0.2.0-1
- update to 0.2.0 (beta)

* Thu Feb  8 2018 Remi Collet <remi@remirepo.net> - 0.1.2-1
- update to 0.1.2

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 0.1.1-1
- initial package, version 0.1.1 (alpha)
