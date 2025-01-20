# Fedora spec file for php-pecl-var-representation
# without SCL compatibility from
#
# remirepo spec file for php-pecl-var-representation
#
# Copyright (c) 2021-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests
%global pecl_name   var_representation
%global ini_name    40-%{pecl_name}.ini

%global upstream_version 0.1.5
#global upstream_prever  RC1
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
%global _configure       ../%{sources}/configure

Summary:        A compact, more readable alternative to var_export
Name:           php-pecl-var-representation
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        3%{?dist}

License:        BSD-3-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 7.2
BuildRequires:  php-pear
# used by tests
BuildRequires:  tzdata

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name}               = %{version}
Provides:       php-%{pecl_name}%{?_isa}       = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
# Notice pecl_name != name
Provides:       php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}


%description
var_representation is a compact alternative to var_export that
properly escapes control characters.


%prep
%setup -qc

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/COPYING/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Check version as upstream often forget to update this
extver=$(sed -n '/define PHP_VAR_REPRESENTATION_VERSION/{s/.* "//;s/".*$//;p}' php_var_representation.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}%{?gh_date:-dev}"; then
   : Error: Upstream version is ${extver}, expecting %{upstream_version}%{?upstream_prever}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Create configuration file
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF


%build
peclconf() {
%configure \
    --with-var_representation \
    --with-php-config=$1
}

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

peclconf %{__phpconfig}
%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Install the configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
cd %{sources}
: Run upstream test suite
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif


%files
%license %{sources}/COPYING
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 17 2024 Remi Collet <remi@fedoraproject.org> - 0.1.5-2
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 0.1.5-1
- update to 0.1.5
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 0.1.4-8
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct  4 2023 Remi Collet <remi@remirepo.net> - 0.1.4-5
- build out of sources tree

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 0.1.4-4
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 0.1.4-2
- use SPDX license ID

* Mon Oct 17 2022 Remi Collet <remi@remirepo.net> - 0.1.4-1
- update to 0.1.4

* Fri Oct 14 2022 Remi Collet <remi@remirepo.net> - 0.1.3-1
- update to 0.1.3

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 0.1.2-2
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Thu Sep  8 2022 Remi Collet <remi@remirepo.net> - 0.1.2-1
- update to 0.1.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 0.1.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Wed Sep  1 2021 Remi Collet <remi@remirepo.net> - 0.1.1-1
- update to 0.1.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 Remi Collet <remi@remirepo.net> - 0.1.0-1
- update to 0.1.0

* Tue Jun 22 2021 Remi Collet <remi@remirepo.net> - 0.1.0~RC1-1
- initial package
- open https://github.com/TysonAndre/var_representation/pull/1
  missing file (stub.php)
- open https://github.com/TysonAndre/var_representation/pull/3
  add version in phpinfo
- open https://github.com/TysonAndre/var_representation/pull/4
  missing tests in pecl archive
