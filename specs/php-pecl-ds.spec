# Fedora spec file for php-pecl-ds
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-ds
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%if 0%{?fedora}
%bcond_without       tests
%else
%bcond_with          tests
%endif

%global pecl_name    ds
# After json
%global ini_name     40-%{pecl_name}.ini
%global sources      %{pecl_name}-%{version}

# For test suite, see https://github.com/php-ds/tests/commits/master
%global gh_commit    3d14aa6f8c25d38d79c90924150c51636544e4a8
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-ds
%global gh_project   tests


Summary:        Data Structures for PHP
Name:           php-pecl-%{pecl_name}
Version:        1.5.0
Release:        8%{?dist}
License:        MIT
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz
# Only use for tests during the build, no value to be packaged separately
# in composer.json:  "require-dev": {  "php-ds/tests": "^1.5.0" }
Source1:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{gh_short}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 7.4
BuildRequires:  php-pear
BuildRequires:  php-gmp
BuildRequires:  php-json
%if %{with tests}
BuildRequires:  %{_bindir}/phpunit9
BuildRequires:  %{_bindir}/phpab
%endif

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-json%{?_isa}

Provides:       php-%{pecl_name}               = %{version}
Provides:       php-%{pecl_name}%{?_isa}       = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
An extension providing specialized data structures as efficient alternatives
to the PHP array.


%prep
%setup -q -c -a 1
mv %{gh_project}-%{gh_commit} tests

# Don't install/register tests, install examples as doc
%{?_licensedir:sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml}

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_DS_VERSION/{s/.* "//;s/".*$//;p}' php_ds.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever:-%{prever}}.
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
    --enable-ds \
    --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Install config file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Generate autoloader for tests
%{_bindir}/phpab \
   --output tests/autoload.php \
   tests

: Run upstream test suite
%{__php} \
   -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
   %{_bindir}/phpunit9 \
      --do-not-cache-result \
      --bootstrap tests/autoload.php \
      --verbose tests
%endif


%files
%{?_licensedir:%license %{sources}/LICENSE}
%{!?_licensedir:%doc %{pecl_docdir}/%{pecl_name}}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 24 2024 Remi Collet <remi@fedoraproject.org> - 1.5.0-7
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.5.0-6
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 1.5.0-4
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 7.4
- build out of sources tree

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.4.0-7
- rebuild for https://fedoraproject.org/wiki/Changes/php83
- add upstream patch for PHP 8.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.4.0-4
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on PHP 7.3
- drop all patches merged upstream
- switch to phpunit8, disable tests on EL

* Wed Nov  3 2021 Remi Collet <remi@remirepo.net> - 1.3.0-6
- add patches for PHP 8.1 from upstream and from
  https://github.com/php-ds/ext-ds/pull/187

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Remi Collet <remi@remirepo.net> - 1.3.0-4
- switch to phpunit7

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 1.3.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0
- fix segfault using patch from
  https://github.com/php-ds/ext-ds/pull/165

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.2.9-3
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Remi Collet <remi@remirepo.net> - 1.2.9-1
- update to 1.2.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Remi Collet <remi@remirepo.net> - 1.2.8-1
- update to 1.2.8

* Mon Nov 19 2018 Remi Collet <remi@remirepo.net> - 1.2.7-1
- update to 1.2.7

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.2.6-3
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Remi Collet <remi@remirepo.net> - 1.2.6-1
- update to 1.2.6

* Mon Mar 12 2018 Remi Collet <remi@remirepo.net> - 1.2.5-1
- update to 1.2.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 1.2.4-2
- undefine _strict_symbol_defs_build

* Wed Nov 29 2017 Remi Collet <remi@remirepo.net> - 1.2.4-1
- Update to 1.2.4
- switch to phpunit 6

* Wed Oct 04 2017 Remi Collet <remi@fedoraproject.org> - 1.2.3-2
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Wed Aug 16 2017 Remi Collet <remi@remirepo.net> - 1.2.3-1
- Update to 1.2.3

* Fri Jul  7 2017 Remi Collet <remi@remirepo.net> - 1.1.10-1
- cleanup for Fedora review

* Thu Jun 22 2017 Remi Collet <remi@remirepo.net> - 1.1.10-1
- Update to 1.1.10

* Fri Mar 24 2017 Remi Collet <remi@remirepo.net> - 1.1.8-1
- Update to 1.1.8

* Mon Feb 13 2017 Remi Collet <remi@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 1.1.6-3
- rebuild with PHP 7.1.0 GA

* Wed Sep 14 2016 Remi Collet <remi@fedoraproject.org> - 1.1.6-2
- rebuild for PHP 7.1 new API version

* Sun Sep 04 2016 Remi Collet <remi@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6

* Thu Sep 01 2016 Remi Collet <remi@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5

* Mon Aug 08 2016 Remi Collet <remi@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4

* Mon Aug 08 2016 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3
- Fix License tag

* Fri Aug 05 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2 (stable)

* Wed Aug 03 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (stable)

* Wed Aug 03 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (stable)

* Mon Aug 01 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4 (stable)

* Mon Aug 01 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 (stable)

* Sat Jul 30 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (stable)

* Thu Jul 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Jul 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package, version 1.0.0 (devel)
  open tests/tests/Map/sort.php
  open https://github.com/php-ds/extension/pull/26

