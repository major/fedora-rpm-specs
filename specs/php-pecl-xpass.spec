# Fedora spec file for php-pecl-xpass
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-xpass
#
# Copyright (c) 2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests

%global pecl_name        xpass
%global ini_name         40-%{pecl_name}.ini
%global upstream_version 1.1.0
#global upstream_prever  RC2
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}

Summary:        Extended password extension
Name:           php-pecl-%{pecl_name}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        3%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libxcrypt) >= 4.4
BuildRequires:  php-devel >= 8.0
BuildRequires:  php-pear

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name}               = %{version}
Provides:       php-%{pecl_name}%{?_isa}       = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
This extension provides password hashing algorithms used by Linux
distributions, using extended crypt library (libxcrypt):

* sha512 provided for legacy as used on some old distributions
* yescrypt used on modern distributions

It also provides additional functions from libxcrypt missing in core PHP:

* crypt_preferred_method
* crypt_gensalt
* crypt_checksalt


%prep
%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_XPASS_VERSION/{s/.* "//;s/".*$//;p}' php_xpass.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
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
    --enable-xpass \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build


%install
%make_install -C %{sources}

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 %{sources}/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}
# Minimal load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
# Upstream test suite
TEST_PHP_ARGS="-n -d extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}
%endif


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.1.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Thu Sep 26 2024 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Mon Sep  9 2024 Remi Collet <remi@remirepo.net> - 1.0.0-1
- update to 1.0.0

* Mon Sep  2 2024 Remi Collet <remi@remirepo.net> - 1.0.0~RC2-1
- update to 1.0.0RC2

* Wed Aug 28 2024 Remi Collet <remi@remirepo.net> - 1.0.0~RC1-1
- initial package, version 1.0.0RC1
