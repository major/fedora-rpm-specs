# Fedora spec file for php-zstd
# without SCL compatibility from:
#
# remirepo spec file for php-zstd
#
# Copyright (c) 2018-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global pecl_name   zstd
%global ini_name    40-%{pecl_name}.ini
%global sources     %{pecl_name}-%{version}

Summary:       Zstandard extension
Name:          php-%{pecl_name}
Version:       0.14.0
Release:       2%{?dist}
License:       MIT
URL:           https://pecl.php.net/package/%{pecl_name}
Source0:       https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 7.0
BuildRequires: php-pecl-apcu-devel
BuildRequires: php-pear
BuildRequires: pkgconfig(libzstd)

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

Provides:       php-pecl-%{pecl_name}          = %{version}
Provides:       php-pecl-%{pecl_name}%{?_isa}  = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
PHP extension for compression and decompression with Zstandard library.


%package devel
Summary:       %{name} developer files (header)
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}

%description devel
These are the files needed to compile programs using %{name}.


%prep
%setup -qc

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml
sed -e '\:"zstd/:d' -i package.xml

cd %{sources}
# Use the system library
rm -r zstd

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_ZSTD_VERSION/{s/.* "//;s/".*$//;p}' php_zstd.h)
if test "x${extver}" != "x%{version}%{?gh_date:-dev}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' extension module
extension = %{pecl_name}.so
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-php-config=%{__phpconfig} \
    --with-libzstd \
    --with-libdir=%{_lib} \
    --enable-zstd

%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Install Configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install Test and Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}

export REPORT_EXIT_STATUS=1
%ifarch s390x
: ignore test with erratic results
rm tests/streams_*phpt
%endif

: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Check that apcu is aware of zstd serializer
%{__php} --no-php-ini \
    --define extension=apcu.so \
    --define apc.enabled=1 \
    --define apc.enable_cli=1 \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --ri apcu | grep '%{pecl_name}'

: Upstream test suite for the extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --offline --show-diff


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%files devel
%doc %{pecl_testdir}/%{pecl_name}
%{php_incldir}/ext/%{pecl_name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov  6 2024 Remi Collet <remi@remirepo.net> - 0.14.0-1
- update to 0.14.0

* Thu Oct 17 2024 Remi Collet <remi@fedoraproject.org> - 0.13.3-5
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 0.13.3-4
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 0.13.2-2
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Mon Jan 29 2024 Remi Collet <remi@remirepo.net> - 0.13.2-1
- update to 0.13.3
- drop patch merged upstream

* Sat Jan 27 2024 Remi Collet <remi@remirepo.net> - 0.13.2-5
- add patch for GCC 14

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Remi Collet <remi@remirepo.net> - 0.13.2-1
- update to 0.13.2 (no change)

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 0.13.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Thu Sep  7 2023 Remi Collet <remi@remirepo.net> - 0.13.1-1
- update to 0.13.1 (no change)

* Wed Sep  6 2023 Remi Collet <remi@remirepo.net> - 0.13.0-1
- update to 0.13.0
- fix tests installation path
- build out of sources tree

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May  2 2023 Remi Collet <remi@remirepo.net> - 0.12.3-1
- update to 0.12.3
- drop patch merged upstream

* Fri Apr 28 2023 Remi Collet <remi@remirepo.net> - 0.12.2-1
- update to 0.12.2
- fix extension version and build warnings, using patch from
  https://github.com/kjdev/php-ext-zstd/pull/57

* Mon Jan 23 2023 Remi Collet <remi@remirepo.net> - 0.12.1-1
- update to 0.12.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Remi Collet <remi@remirepo.net> - 0.12.0-1
- update to 0.12.0

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 0.11.0-5
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 0.11.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Mon Oct  4 2021 Remi Collet <remi@remirepo.net> - 0.11.0-1
- update to 0.11.0

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 0.10.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Remi Collet <remi@remirepo.net> - 0.10.0-1
- update to 0.10.0
- enable apcu serializer

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Remi Collet <remi@remirepo.net> - 0.9.0-1
- update to 0.9.0 (stable)

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 0.8.0-1
- update to 0.8.0
- sources from pecl

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Remi Collet <remi@remirepo.net> - 0.7.3-3
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Remi Collet <remi@remirepo.net> - 0.7.3-1
- cleanup for Fedora review

* Wed Apr 24 2019 Remi Collet <remi@remirepo.net> - 0.7.3-1
- update to 0.7.3

* Tue Apr 23 2019 Remi Collet <remi@remirepo.net> - 0.7.2-1
- update to 0.7.2
- use bundled libzstd 1.4.0

* Fri Apr 19 2019 Remi Collet <remi@remirepo.net> - 0.7.1-1
- update to 0.7.1

* Tue Apr 16 2019 Remi Collet <remi@remirepo.net> - 0.7.0-1
- update to 0.7.0

* Mon Apr 15 2019 Remi Collet <remi@remirepo.net> - 0.6.1-2
- test build for Stream implementation, from
  https://github.com/kjdev/php-ext-zstd/pull/17

* Thu Apr  4 2019 Remi Collet <remi@remirepo.net> - 0.6.1-1
- update to 0.6.1

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 0.6.0-1
- update to 0.6.0

* Mon Jan  7 2019 Remi Collet <remi@remirepo.net> - 0.5.0-1
- update to 0.5.0

* Thu Aug 16 2018 Remi Collet <remi@remirepo.net> - 0.4.14-4
- ignore test suite results with newer system library

* Thu Aug 16 2018 Remi Collet <remi@remirepo.net> - 0.4.14-3
- rebuild for 7.3.0beta2 new ABI

* Wed Jul 18 2018 Remi Collet <remi@remirepo.net> - 0.4.14-2
- rebuild for 7.3.0alpha4 new ABI

* Tue Jun 19 2018 Remi Collet <remi@remirepo.net> - 0.4.14-1
- update to 0.4.14

* Mon Apr  9 2018 Remi Collet <remi@remirepo.net> - 0.4.13-1
- update to 0.4.13

* Wed Jan 31 2018 Remi Collet <remi@remirepo.net> - 0.4.12-1
- update to 0.4.12 (no change, PR merged upstream)

* Tue Jan 30 2018 Remi Collet <remi@remirepo.net> - 0.4.11-1
- new package, version 0.4.11
- add patch to build with system libzstd from
  https://github.com/kjdev/php-ext-zstd/pull/7
