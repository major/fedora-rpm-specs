# Fedora spec file for php-pecl-xpass
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-xpass
#
# SPDX-FileCopyrightText:  Copyright 2024-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global php_base         php

%bcond_without           tests

%global pie_vend         remi
%global pie_proj         xpass
%global pecl_name        xpass
%global ini_name         40-%{pecl_name}.ini
%global upstream_version 1.2.1
#global upstream_prever  RC2

# Github forge
%global gh_vend          remicollet
%global gh_proj          php-xpass
%global forgeurl         https://github.com/%{gh_vend}/%{gh_proj}
%global tag              v%{upstream_version}%{?upstream_prever}

Name:           %{php_base}-pecl-%{pecl_name}
Summary:        Extended password extension
License:        BSD-3-Clause
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgesource}

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libxcrypt) >= 4.4
BuildRequires:  libxcrypt-devel
BuildRequires:  %{php_base}-devel >= 8.0

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Extension
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
# PECL
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
# PIE
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

%if "%{php_base}" != "php"
Requires:       %{php_base}-common%{?_isa}
Conflicts:      php-pecl-%{pecl_name}
Provides:       php-pecl-%{pecl_name} = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
%endif


%description
This extension provides password hashing algorithms used by Linux
distributions, using extended crypt library (libxcrypt):

* sha512 provided for legacy as used on some old distributions
* yescrypt used on modern distributions
* sm3crypt
* sm3yescrypt

It also provides additional functions from libxcrypt missing in core PHP:

* crypt_preferred_method
* crypt_gensalt
* crypt_checksalt

See PHP documentation on https://www.php.net/xpass


%prep
%forgesetup

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_XPASS_VERSION/{s/.* "//;s/".*$//;p}' php_xpass.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' extension module
extension=%{pecl_name}.so
EOF


%build
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --enable-xpass \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build


%install
%make_install

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}


%check
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
%license LICENSE
%doc composer.json
%doc *.md
%doc CREDITS
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Fri Apr 17 2026 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1
- PHP License updated from version 3 to version 4 (BSD-3-Clause)

* Wed Mar 11 2026 Remi Collet <remi@remirepo.net> - 1.2.0-3
- drop pear/pecl dependency
- sources from github

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Jan 13 2026 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Tue Oct 28 2025 Remi Collet <remi@remirepo.net> - 1.1.0-7
- add php_base option to create namespaced packages

* Thu Sep 18 2025 Remi Collet <remi@remirepo.net> - 1.1.0-6
- rebuild for https://fedoraproject.org/wiki/Changes/php85
- re-license spec file to CECILL-2.1
- add pie virtual provides

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1.1.0-4
- Add explicit BR: libxcrypt-devel

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
