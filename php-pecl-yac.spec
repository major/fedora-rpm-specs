# Fedora spec file for php-pecl-yac (previously php-yac)
#
# Copyright (c) 2013-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global with_zts    0%{?__ztsphp:1}
%global pecl_name   yac
%global with_tests  %{!?_without_tests:1}%{?_without_tests:0}
# after 20-json, 40-igbinary and 40-msgpack
%global ini_name    50-%{pecl_name}.ini

Summary:        Lockless user data cache
Name:           php-pecl-%{pecl_name}
Version:        2.3.1
Release:        5%{?dist}

License:        PHP
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}.tgz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 7.0
BuildRequires:  php-pear
BuildRequires:  php-json
BuildRequires:  php-pecl-msgpack-devel
BuildRequires:  php-pecl-igbinary-devel
BuildRequires:  fastlz-devel

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-json%{?_isa}
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
mv %{pecl_name}-%{version} NTS

# Don't install (register) the tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd NTS
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


%if %{with_zts}
# duplicate for ZTS build
cp -pr NTS ZTS
%endif


%build
peclconf() {
%configure \
    --enable-json \
    --enable-msgpack \
    --enable-igbinary \
    --with-system-fastlz \
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

# Test & Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
OPTS="-n"
[ -f %{php_extdir}/json.so     ] && OPTS="$OPTS -d extension=json.so"
[ -f %{php_extdir}/igbinary.so ] && OPTS="$OPTS -d extension=igbinary.so"
[ -f %{php_extdir}/msgpack.so  ] && OPTS="$OPTS -d extension=msgpack.so"

cd NTS

: Minimal load test for NTS extension
%{_bindir}/php $OPTS  \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with_tests}
: Upstream test suite for NTS extension
TEST_PHP_ARGS="$OPTS -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%else
: Upstream test suite disabled
%endif

%if %{with_zts}
cd ../ZTS

: Minimal load test for ZTS extension
%{__ztsphp} $OPTS \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with_tests}
: Upstream test suite for ZTS extension
TEST_PHP_ARGS="$OPTS -d extension=$PWD/modules/%{pecl_name}.so" \
%{__ztsphp} -n run-tests.php -q --show-diff
%else
: Upstream test suite disabled
%endif
%endif


%files
%license NTS/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%{php_ztsextdir}/%{pecl_name}.so
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%endif


%changelog
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
