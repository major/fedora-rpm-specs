# Fedora spec file for php-pecl-xmlrpc
# Without SCL compatibility, from
#
# remirepo spec file for php-pecl-xmlrpc
#
# Copyright (c) 2020-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests

%global with_zts    0%{!?_without_zts:%{?__ztsphp:1}}
%global pecl_name   xmlrpc
%global upver       1.0.0
%global rcver       RC3
%global rclower     rc3
# After 20-xml
%global ini_name    30-%{pecl_name}.ini
%global sources     %{pecl_name}-%{upver}%{?rcver}
%global _configure  ../%{sources}/configure


Summary:        Functions to write XML-RPC servers and clients
Name:           php-pecl-%{pecl_name}
Version:        %{upver}%{?rclower:~%{rclower}}
Release:        14%{?dist}

# Extension is PHP
# Library is MIT
License:        PHP-3.01 AND MIT
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

Patch0:         %{pecl_name}-tests.patch

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 8.0
BuildRequires:  php-pear
BuildRequires:  php-xml

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-xml%{?_isa}

# Set epoch so 1:1.0 > 0:8.0
Obsoletes:      php-%{pecl_name}               < 8.0.0
Provides:       php-%{pecl_name}               = 1:%{version}
Provides:       php-%{pecl_name}%{?_isa}       = 1:%{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
This extension provides functions to write XML-RPC servers and clients.

You can find more information about XML-RPC at http://www.xmlrpc.com/,
and more documentation on this extension and its functions at
https://www.php.net/xmlrpc.

The extension is unbundled from php-src as of PHP 8.0.0, because the underlying
libxmlrpc has obviously been abandoned. It is recommended to reevaluate using
this extension.


%prep
%setup -qc

sed -e 's/role="test"/role="src"/' \
    -e '/COPYING/s/role="doc"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
%patch -P0 -p1 -b .up

# Check version as upstream often forget to update this
extver=$(sed -n '/#define PHP_XMLRPC_VERSION/{s/.* "//;s/".*$//;p}' php_xmlrpc.h)
if test "x${extver}" != "x%{upver}%{?rcver}%{?gh_date:-dev}"; then
   : Error: Upstream RECODE version is ${extver}, expecting %{upver}%{?rcver}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable "%{pecl_name}" extension module
extension=%{pecl_name}
EOF

mkdir NTS
%if %{with_zts}
mkdir ZTS
%endif


%build
peclconf() {
%configure \
    --with-xmlrpc \
    --with-php-config=$1
}

cd %{sources}
%{__phpize}

cd ../NTS
peclconf %{__phpconfig}
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
peclconf %{__ztsphpconfig}
make %{?_smp_mflags}
%endif


%install
# Install the NTS stuff
make -C NTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Install the ZTS stuff
%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Test & Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 %{sources}/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=xml \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with_zts}

: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=xml \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%endif

%if %{with tests}
: Run upstream test suite
TEST_PHP_ARGS="-n -d extension=xml -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif



%files
%license %{sources}/LICENSE
%license %{sources}/libxmlrpc/COPYING
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%{php_ztsextdir}/%{pecl_name}.so
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%endif


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~rc3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.0.0~rc3-13
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~rc3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 1.0.0~rc3-11
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Mon Jan 29 2024 Remi Collet <remi@remirepo.net> - 1.0.0~rc3-10
- adapt tests for new libxml

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~rc3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~rc3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.0.0~rc3-8
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Thu Aug 24 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~rc3-7
- build out of sources tree and fix FTBFS

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~rc3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 1.0.0~rc3-5
- use SPDX license ID

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.0.0~rc3-4
- rebuild for https://fedoraproject.org/wiki/Changes/php82
- add upstream patch for PHP 8.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~rc3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~rc3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec  6 2021 Remi Collet <remi@remirepo.net> - 1.0.0~rc3-1
- update to 1.0.0RC3 (beta)

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 1.0.0~rc2-4
- rebuild for https://fedoraproject.org/wiki/Changes/php81
- add upstream patch for PHP 8.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~rc2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar  6 2021 Remi Collet <remi@remirepo.net> - 1.0.0~rc2-2
- clean for Fedora review

* Fri Jan 15 2021 Remi Collet <remi@remirepo.net> - 1.0.0~rc2-1
- update to 1.0.0RC2 (beta)

* Tue Jan  5 2021 Remi Collet <remi@remirepo.net> - 1.0.0~rc1-1
- update to 1.0.0RC1 (beta)

* Wed Sep 30 2020 Remi Collet <remi@remirepo.net> - 1.0.0~DEV.20200602-4
- rebuild for PHP 8.0.0RC1

* Wed Sep  2 2020 Remi Collet <remi@remirepo.net> - 1.0.0~DEV.20200202-3
- rebuild for PHP 8.0.0beta3

* Wed Aug  5 2020 Remi Collet <remi@remirepo.net> - 1.0.0~DEV.20200202-2
- rebuild for 8.0.0beta1

* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 1.0.0~DEV.20200202-1
- initial package, version 1.0.0-dev
