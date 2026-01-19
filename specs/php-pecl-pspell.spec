# Fedora spec file for php-pecl-pspell
# Without SCL compatibility from:
#
# remirepo spec file for php-pecl-pspell
#
# SPDX-FileCopyrightText:  Copyright 2023-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without         tests

%global pecl_name      pspell
%global ini_name       30-%{pecl_name}.ini
%global sources        %{pecl_name}-%{version}

Summary:      Spell checker extension
Name:         php-pecl-%{pecl_name}
Version:      1.0.1
Release:      4%{?dist}
License:      PHP-3.01
URL:          https://pecl.php.net/package/pspell

Source0:      https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
# 8.1+ is supported by upstream but part of php-src until 8.4
BuildRequires: php-devel >= 8.4
BuildRequires: aspell-devel >= 0.50.0
BuildRequires: php-pear
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
%setup -c -q

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_PSPELL_VERSION/{s/.* "//;s/".*$//;p}' php_pspell.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

: Create the configuration file
cat >%{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
  --with-pspell \
  --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}
%make_install
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}
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
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
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
