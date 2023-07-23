# Fedora spec file for php-pecl-var-representation
# without SCL compatibility from
#
# remirepo spec file for php-pecl-var-representation
#
# Copyright (c) 2021-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%bcond_without      tests
%global with_zts    0%{!?_without_zts:%{?__ztsphp:1}}
%global pecl_name   var_representation
%global ini_name    40-%{pecl_name}.ini

%global upstream_version 0.1.4
#global upstream_prever  RC1

Summary:        A compact, more readable alternative to var_export
Name:           php-pecl-var-representation
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        3%{?dist}

License:        BSD-3-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{upstream_version}%{?upstream_prever}.tgz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 7.2
BuildRequires:  php-pear

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
mv %{pecl_name}-%{upstream_version}%{?upstream_prever} NTS

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/COPYING/s/role="doc"/role="src"/' \
    -i package.xml

cd NTS
# Check version as upstream often forget to update this
extver=$(sed -n '/define PHP_VAR_REPRESENTATION_VERSION/{s/.* "//;s/".*$//;p}' php_var_representation.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}%{?gh_date:-dev}"; then
   : Error: Upstream version is ${extver}, expecting %{upstream_version}%{?upstream_prever}%{?gh_date:-dev}.
   exit 1
fi
cd ..


%if %{with_zts}
# duplicate for ZTS build
cp -pr NTS ZTS
%endif

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

cd NTS
%{_bindir}/phpize
peclconf %{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
peclconf %{_bindir}/zts-php-config
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

# Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do [ -f NTS/$i ] &&  install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: Minimal load test for NTS extension
%{_bindir}/php --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with_zts}
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%endif

%if %{with tests}
cd NTS
: Run upstream test suite
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif


%files
%license NTS/COPYING
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%{php_ztsextdir}/%{pecl_name}.so
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%endif


%changelog
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
