# Fedora spec file for php-rlerdorf-geoip
# without SCL compatibility from:
#
# remirepo spec file for php-rlerdorf-geoip
#
# SPDX-FileCopyrightText:  Copyright 2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without           tests

# Extension
%global ext_name         geoip
%global ini_name         40-%{ext_name}.ini
# PIE / packagist
%global pie_vend         rlerdorf
%global pie_proj         %{ext_name}
# Github forge
%global gh_vend          %{pie_vend}
%global gh_proj          %{pie_proj}
%global forgeurl         https://github.com/%{gh_vend}/%{gh_proj}
%global tag              %{version}

Name:           php-%{pie_vend}-%{pie_proj}
Summary:        Legacy GeoIP (v1) PHP extension
License:        PHP-3.01
Version:        1.4.0
Release:        1%{?dist}
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgesource}

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel
BuildRequires:  GeoIP-devel

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Extension
Provides:       php-%{ext_name}                  = %{version}
Provides:       php-%{ext_name}%{?_isa}          = %{version}
# PIE
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
# Package is a fork with same API
Obsoletes:      php-pecl-%{ext_name}             < 1.2
Provides:       php-pecl-%{ext_name}             = %{version}
Provides:       php-pecl-%{ext_name}%{?_isa}     = %{version}
Provides:       php-pecl(%{ext_name})            = %{version}
Provides:       php-pecl(%{ext_name})%{?_isa}    = %{version}


%description
This is the legacy (v1) GeoIP PHP extension.

Unless you have old code that needs this, you might be better off using
- php-maxmind-db-reader library (maxmind-db/reader)
- php-maxminddb extension (maxmind-db/reader-ext)


%prep
%forgesetup

: Sanity check, really often broken
extver=$(sed -n '/#define PHP_GEOIP_VERSION/{s/.* "//;s/".*$//;p}' php_geoip.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi

: Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable the %{summary}
extension=%{ext_name}.so
EOF


%build
phpize
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-geoip \
    --with-libdir=%{_lib}

%make_build


%install
%make_install

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}


%check
: Minimal load test for the extension
php --no-php-ini \
    --define extension=%{buildroot}/%{php_extdir}/%{ext_name}.so \
    --modules | grep '^%{ext_name}$'

%if %{with tests}
: Upstream test suite for the extension
TEST_PHP_ARGS="-n -d extension=%{buildroot}/%{php_extdir}/%{ext_name}.so" \
php -n run-tests.php -P -q --show-diff %{?_smp_mflags}

%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{ext_name}.so


%changelog
* Thu Apr 23 2026 Remi Collet <remi@remirepo.net> - 1.4.0-1
- initial package
- obsoletes php-pecl-geoip
