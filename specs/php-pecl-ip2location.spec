# Fedora spec file for php-pecl-ip2location
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-ip2location
#
# Copyright (c) 2017-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global pecl_name  ip2location
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{upstream_version}%{?upstream_prever}

%global upstream_version 8.2.0
#global upstream_prever  RC1
%global libversion       8.6

Summary:        Get geo location information of an IP address
Name:           php-pecl-%{pecl_name}
License:        PHP-3.01
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        10%{?dist}
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-pear
BuildRequires:  php-devel
# ensure proper version is used with all features
BuildRequires:  IP2Location-devel >= %{libversion}
Requires:       IP2Location-libs%{?_isa} >= %{libversion}

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name}                = %{version}
Provides:       php-%{pecl_name}%{?_isa}        = %{version}
Provides:       php-pecl(%{pecl_name})          = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}  = %{version}


%description
This PHP extension enables you to get the geo location information of
an IP address, such as country, region or state, city, latitude and
longitude, US ZIP code, time zone, Internet Service Provider (ISP) or
company name, domain name, net speed, area code, weather station code,
weather station name, mobile country code (MCC), mobile network code
(MNC) and carrier brand, elevation, and usage type.


%prep
%setup -q -c

# Don't install tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -e '/README.TXT/s/role="doc"/role="test"/' \
    -i package.xml

cd %{sources}
sed -e "s/\r//" -i LICENSE CREDITS *.md *.c *.h

# Check version
extver=$(sed -n '/#define PHP_IP2LOCATION_VERSION/{s/.* "//;s/".*$//;p}' php_ip2location.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

cat <<EOF | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --with-php-config=%{__phpconfig}
%make_build


%install

install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

cd %{sources}
%make_install

# Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: simple module load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

: upstream test suite
cd %{sources}
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff


%files
%doc %{pecl_docdir}/%{pecl_name}
%config(noreplace) %{php_inidir}/%{ini_name}

%{php_extdir}/%{pecl_name}.so
%{pecl_xmldir}/%{name}.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 16 2024 Remi Collet <remi@fedoraproject.org> - 8.2.0-9
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 8.2.0-8
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 8.2.0-6
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 8.2.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Remi Collet <remi@remirepo.net> - 8.2.0-1
- update to 8.2.0
- raise dependency on IP2location library version 8.6

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 8.1.2-2
- use SPDX license ID

* Wed Nov  9 2022 Remi Collet <remi@remirepo.net> - 8.1.2-1
- update to 8.1.2

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 8.1.1-8
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 8.1.1-5
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 8.1.1-3
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Remi Collet <remi@remirepo.net> - 8.1.1-1
- update to 8.1.1

* Thu Nov 19 2020 Remi Collet <remi@remirepo.net> - 8.1.0-1
- update to 8.1.0
- drop all patches merged upstream

* Wed Sep 30 2020 Remi Collet <remi@remirepo.net> - 8.0.1-8
- add patches for library version 8.1.4 and for PHP 8 from
  https://github.com/chrislim2888/IP2Location-PECL-Extension/pull/12

* Fri Sep 25 2020 Remi Collet <remi@remirepo.net> - 8.0.1-6
- add patches for library version 8.1 and for PHP 8 from
  https://github.com/chrislim2888/IP2Location-PECL-Extension/pull/8
  https://github.com/chrislim2888/IP2Location-PECL-Extension/pull/9
  https://github.com/chrislim2888/IP2Location-PECL-Extension/pull/10
  https://github.com/chrislim2888/IP2Location-PECL-Extension/pull/11

* Tue Sep 03 2019 Remi Collet <remi@remirepo.net> - 8.0.1-5
- rebuild for 7.4.0RC1

* Tue Jul 23 2019 Remi Collet <remi@remirepo.net> - 8.0.1-4
- rebuild for 7.4.0beta1

* Thu Aug 16 2018 Remi Collet <remi@remirepo.net> - 8.0.1-3
- rebuild for 7.3.0beta2 new ABI

* Wed Jul 18 2018 Remi Collet <remi@remirepo.net> - 8.0.1-2
- rebuld for 7.3.0alpha4 new ABI

* Wed Nov  8 2017 Remi Collet <remi@remirepo.net> - 8.0.1-1
- Update to 8.0.1 (no change)
- License is PHP

* Sun Nov  5 2017 Remi Collet <remi@remirepo.net> - 8.0.0-1
- initital RPM
- open https://github.com/chrislim2888/IP2Location-PECL-Extension/issues/6
  for LICENSE clarification
- open https://github.com/chrislim2888/IP2Location-PECL-Extension/pull/5
  for a minimal test suite
