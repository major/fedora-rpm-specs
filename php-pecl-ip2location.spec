# Fedora spec file for php-pecl-ip2location
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-ip2location
#
# Copyright (c) 2017-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global pecl_name  ip2location
%global with_zts   0%{!?_without_zts:%{?__ztsphp:1}}
%global ini_name   40-%{pecl_name}.ini

%global upstream_version 8.1.2
#global upstream_prever  RC1

Summary:        Get geo location information of an IP address
Name:           php-pecl-%{pecl_name}
License:        PHP-3.01
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        2%{?dist}
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{upstream_version}%{?upstream_prever}.tgz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-pear
BuildRequires:  php-devel
BuildRequires:  IP2Location-devel >= 8.4

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
mv %{pecl_name}-%{upstream_version}%{?upstream_prever} NTS

# Don't install tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -e '/README.TXT/s/role="doc"/role="test"/' \
    -i package.xml

cd NTS
sed -e "s/\r//" -i LICENSE CREDITS *.md *.c *.h


# Check version
extver=$(sed -n '/#define PHP_IP2LOCATION_VERSION/{s/.* "//;s/".*$//;p}' php_ip2location.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

%if %{with_zts}
cp -r NTS ZTS
%endif

cat <<EOF | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF


%build
cd NTS
%{_bindir}/phpize
%configure --with-php-config=%{_bindir}/php-config
%make_build

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure --with-php-config=%{_bindir}/zts-php-config
%make_build
%endif


%install
make install -C NTS INSTALL_ROOT=%{buildroot}

install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install the ZTS stuff
%if %{with_zts}
make install -C ZTS INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: simple NTS module load test
%{_bindir}/php --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

: upstream test suite
cd NTS
TEST_PHP_EXECUTABLE=%{_bindir}/php \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{_bindir}/php -n run-tests.php -q --show-diff

%if %{with_zts}
: simple ZTS module load test
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

: upstream test suite
cd ../ZTS
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
%{__ztsphp} -n run-tests.php -q --show-diff
%endif


%files
%doc %{pecl_docdir}/%{pecl_name}
%config(noreplace) %{php_inidir}/%{ini_name}

%{php_extdir}/%{pecl_name}.so
%{pecl_xmldir}/%{name}.xml

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%changelog
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
