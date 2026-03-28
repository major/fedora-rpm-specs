# Fedora spec file for php-pecl-pspell
# Without SCL compatibility from:
#
# remirepo spec file for php-pecl-pspell
#
# SPDX-FileCopyrightText:  Copyright 2023-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without         tests

%global pecl_name      pspell
%global ini_name       30-%{pecl_name}.ini

# Github forge
%global gh_vend        php
%global gh_proj        pecl-text-pspell
%global forgeurl       https://github.com/%{gh_vend}/%{gh_proj}
%global tag            %{version}

Name:         php-pecl-%{pecl_name}
Summary:      Spell checker extension
License:      PHP-3.01
Version:      1.0.1
Release:      5%{?dist}
%forgemeta
URL:          %{forgeurl}
Source0:      %{forgesource}

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
# 8.1+ is supported by upstream but part of php-src until 8.4
BuildRequires: php-devel >= 8.4
BuildRequires: aspell-devel >= 0.50.0
%if %{with tests}
BuildRequires: aspell-en
%endif

Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}

Provides:     php-pecl(%{pecl_name})         = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}
# Package removed from php-src in 8.4
# Set epoch so provides is > 0:8.4
Obsoletes:    php-%{pecl_name}         < 8.4
Provides:     php-%{pecl_name}         = 1:%{version}-%{release}
Provides:     php-%{pecl_name}%{?_isa} = 1:%{version}-%{release}


%description
This extension allows you to check the spelling of a word and offer suggestions,
using GNU Aspell library and dictionaries.


%prep 
%forgesetup

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_PSPELL_VERSION/{s/.* "//;s/".*$//;p}' php_pspell.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi

: Create the configuration file
cat >%{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}
EOF


%build
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
  --with-pspell \
  --with-php-config=%{__phpconfig}

%make_build


%install
%make_install
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}


%check
: minimal load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

OPT="%{?_smp_mflags} -q --show-diff"

%if %{with tests}
: upstream test suite
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php $OPT
%endif


%files
%license LICENSE
%doc CREDITS

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Thu Mar 26 2026 Remi Collet <remi@remirepo.net> - 1.0.1-4
- drop pear/pecl dependency
- sources from github

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Sep 17 2025 Remi Collet <remi@remirepo.net> - 1.0.1-3
- rebuild for https://fedoraproject.org/wiki/Changes/php85

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Apr 10 2025 Remi Collet <remi@remirepo.net> - 1.0.1-1
- cleanup for Fedora

* Tue Sep 24 2024 Remi Collet <remi@remirepo.net> - 1.0.1-2
- rebuild for 8.4.0RC1

* Thu Nov 23 2023 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1
- drop patch merged upstream

* Thu Nov 23 2023 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package for version 1.0.0 (PHP 8.4)
- open https://github.com/php/pecl-text-pspell/pull/2 tests and version
