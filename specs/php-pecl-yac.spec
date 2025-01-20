# Fedora spec file for php-pecl-yac (previously php-yac)
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests

%global pecl_name   yac
# after 40-igbinary and 40-msgpack
%global ini_name    50-%{pecl_name}.ini
%global sources     %{pecl_name}-%{version}

Summary:        Lockless user data cache
Name:           php-pecl-%{pecl_name}
Version:        2.3.1
Release:        15%{?dist}

License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  php-pecl-msgpack-devel
BuildRequires:  php-pecl-igbinary-devel
BuildRequires:  fastlz-devel

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-igbinary%{?_isa}
Requires:       php-msgpack%{?_isa}

# Package have be renamed
Obsoletes:      php-%{pecl_name} < %{version}
Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
Yac (Yet Another Cache) is a shared memory user data cache for PHP.

It can be used to replace APC or local memcached.

Yac is lockless, that means, it is very fast, but there could be a
chance you will get a wrong data(depends on how many key slots are
allocated and how many keys are stored), so you'd better make sure
that your product is not very sensitive to that.


%prep
%setup -qc

# Don't install (register) the tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# drop bundled fastlz to ensure it is not used
sed -e '\:name="compressor/fastlz:d' -i ../package.xml
rm -r compressor/fastlz

# Check version as upstream often forget to update this
extver=$(sed -n '/#define PHP_YAC_VERSION/{s/.* "//;s/".*$//;p}' php_yac.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream YAC version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat > %{ini_name} << 'EOF'
; Enable Yet Another Cache extension module
extension = %{pecl_name}.so

;yac.enable=1
;yac.enable_cli=0
;yac.debug=0
;yac.keys_memory_size=4M
;yac.values_memory_size=64M
;yac.compress_threshold=-1
;yac.serializer=php
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --enable-json \
    --enable-msgpack \
    --enable-igbinary \
    --with-system-fastlz \
    --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Install the configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install Test and Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}

OPTS="-n"
[ -f %{php_extdir}/igbinary.so ] && OPTS="$OPTS -d extension=igbinary.so"
[ -f %{php_extdir}/msgpack.so  ] && OPTS="$OPTS -d extension=msgpack.so"

: Minimal load test for the extension
%{__php} $OPTS  \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Upstream test suite for the extension
TEST_PHP_ARGS="$OPTS -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%else
: Upstream test suite disabled
%endif


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Remi Collet <remi@fedoraproject.org> - 2.3.1-14
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 2.3.1-13
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 2.3.1-11
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 2.3.1-8
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 2.3.1-6
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 2.3.1-4
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Remi Collet <remi@remirepo.net> - 2.3.1-1
- update to 2.3.1
- drop patch merge upstream

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 2.3.0-5
- rebuild for https://fedoraproject.org/wiki/Changes/php81
- add patch for test suite with 8.1.0beta2 from
  https://github.com/laruence/yac/pull/120

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar  5 2021 Remi Collet <remi@fedoraproject.org> - 2.3.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Tue Mar 31 2020 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- enable json, igbinary and msgpack serializers
- rename configuration file to 50-yac.ini to ensure proper load order

* Fri Mar 27 2020 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2

* Wed Mar 25 2020 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan  6 2020 Remi Collet <remi@remirepo.net> - 2.0.3-1
- update to 2.0.3

* Fri Oct 04 2019 Remi Collet <remi@remirepo.net> - 2.0.2-9
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 2.0.2-6
- Rebuild for https://fedoraproject.org/wiki/Changes/php73
- add patch for PHP 7.3 from
  https://github.com/laruence/yac/pull/89

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 2.0.2-3
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 2.0.2-2
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 2.0.2-1
- Update to 2.0.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Sat Jul  2 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1 (php 7)

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0 (php 7)

* Sat Feb 13 2016 Remi Collet <remi@fedoraproject.org> - 0.9.2-4
- drop scriptlets (replaced by file triggers in php-pear)
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 25 2014 Remi Collet <remi@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Sat Sep  6 2014 Remi Collet <remi@fedoraproject.org> - 0.9.1-3
- cleanup for review
- build with system fastlz
- don't install the tests

* Tue Aug 26 2014 Remi Collet <rcollet@redhat.com> - 0.9.1-2
- improve SCL build

* Fri Jul 25 2014 Remi Collet <remi@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1 (beta)

* Thu Jul 24 2014 Remi Collet <remi@fedoraproject.org> - 0.9.0-1
- upstream move to pecl
- rename from php-yac to php-pecl-yac
- update to 0.9.0 (beta)

* Thu Apr 17 2014 Remi Collet <remi@fedoraproject.org> - 0.1.1-3
- add numerical prefix to extension configuration file (php 5.6)

* Tue Mar 25 2014 Remi Collet <remi@fedoraproject.org> - 0.1.1-2
- allow SCL build

* Sun Mar 16 2014 Remi Collet <remi@fedoraproject.org> - 0.1.1-1
- version 0.1.1

* Sat Mar 23 2013 Remi Collet <remi@fedoraproject.org> - 0.1.0-0.1.git57fe00d
- initial package, version 0.1.0 (experimental)
