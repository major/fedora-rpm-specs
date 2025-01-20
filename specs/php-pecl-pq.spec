# Fedora spec file for php-pecl-pq
# without SCL compatibility, from
#
# remirepo spec file for php-pecl-pq
#
# Copyright (c) 2014-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Build using "--without tests" to disable tests
%bcond_without     tests

%global pecl_name  pq
%global ini_name   50-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Summary:        PostgreSQL client library (libpq) binding
Name:           php-pecl-%{pecl_name}
Version:        2.2.3
Release:        6%{?dist}
License:        BSD-2-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}%{?rcver}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  libpq-devel > 9
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 7.0
BuildRequires:  php-pear
BuildRequires:  php-json
BuildRequires:  php-pecl-raphf-devel >= 1.1.0
%if %{with tests}
BuildRequires:  postgresql-server
BuildRequires:  postgresql-contrib
%endif

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-json%{?_isa}
Requires:       php-raphf%{?_isa}  >= 1.1.0

Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
PostgreSQL client library (libpq) binding.

Documents: http://devel-m6w6.rhcloud.com/mdref/pq

Highlights:
* Nearly complete support for asynchronous usage
* Extended type support by pg_type
* Fetching simple multi-dimensional array maps
* Working Gateway implementation


%prep
%setup -q -c

# Don't install tests nor LICENSE
sed -e '/role="test"/d' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_PQ_VERSION/{s/.* "//;s/".*$//;p}' php_pq.h)
if test "x${extver}" != "x%{version}%{?rcver}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?rcver}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable "%{summary}" extension module
extension=%{pecl_name}.so
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-libdir=%{_lib} \
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

: Install  Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: ignore tests with erratic results
rm %{sources}/tests/cancel001.phpt
rm %{sources}/tests/flush001.phpt


OPT="-n"
[ -f %{php_extdir}/json.so ]  && OPT="$OPT -d extension=json.so"
[ -f %{php_extdir}/raphf.so ] && OPT="$OPT -d extension=raphf.so"

: Minimal load test for NTS extension
%{__php} $OPT \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
RET=0

: Running a server
DATABASE=$PWD/data
%ifarch x86_64
PORT=5440
%else
PORT=5436
%endif
pg_ctl initdb -D $DATABASE
cat <<EOF >>$DATABASE/postgresql.conf
unix_socket_directories = '$DATABASE'
port = $PORT
EOF
pg_ctl -D $DATABASE -l $PWD/server.log -w -t 200  start
createdb -h localhost -p $PORT rpmtest

cd %{sources}
sed -e "/PQ_DSN/s/\"host.*\"/'host=localhost port=$PORT dbname=rpmtest'/" \
    -i tests/_setup.inc

: Upstream test suite  for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="$OPT -d extension=$PWD/../NTS/modules/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php -q --show-diff || RET=1

cd ..
: Cleanup
psql -h localhost -p $PORT -c "SELECT version()" rpmtest
pg_ctl -D $DATABASE -w stop
rm -rf $DATABASE

exit $RET
%endif


%files
%doc %{pecl_docdir}/%{pecl_name}
%license %{sources}/LICENSE
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 17 2024 Remi Collet <remi@fedoraproject.org> - 2.2.3-5
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 2.2.3-4
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 2.2.3-2
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Tue Feb  6 2024 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3
- drop patch merged upstream

* Mon Jan 29 2024 Remi Collet <remi@remirepo.net> - 2.2.2-5
- Fix incompatible pointer types using patch from
  https://github.com/m6w6/ext-pq/pull/52

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 2.2.2-3
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2
- build out of sources tree

* Fri Mar  3 2023 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 2.2.0-5
- rebuild for https://fedoraproject.org/wiki/Changes/php82
- add upstream patch for 8.2 and from
  https://github.com/m6w6/ext-pq/pull/44

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 2.2.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Wed Sep  1 2021 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 2.1.8-4
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 2.1.8-3
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 24 2020 Remi Collet <remi@remirepo.net> - 2.1.8-1
- update to 2.1.8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 2.1.7-1
- update to 2.1.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 2.1.6-1
- update to 2.1.6

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 2.1.5-4
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Remi Collet <remi@remirepo.net> - 2.1.5-1
- update to 2.1.5

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 2.1.4-3
- Rebuild for https://fedoraproject.org/wiki/Changes/php73
- add upstream patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Remi Collet <remi@remirepo.net> - 2.1.4-1
- update to 2.1.4 (stable)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 2.1.3-2
- undefine _strict_symbol_defs_build

* Wed Jan 10 2018 Remi Collet <remi@remirepo.net> - 2.1.3-1
- Update to 2.1.3 (stable)

* Fri Nov 10 2017 Remi Collet <remi@fedoraproject.org> - 2.1.2-6
- ignore 1 test with erratic results

* Mon Oct 23 2017 Remi Collet <remi@fedoraproject.org> - 2.1.2-5
- fix botstraping for postgresql 10, FTBFS from Koschei

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 2.1.2-4
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul  3 2017 Remi Collet <remi@remirepo.net> - 2.1.2-1
- Update to 2.1.2 (stable)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Remi Collet <remi@fedoraproject.org> - 2.1.1-3
- add upstream patch for 7.1
  https://github.com/m6w6/ext-pq/issues/23

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 2.1.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- update to 2.1.1 (php 7, stable)

* Fri May 20 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1 (php 5, stable)
- open https://github.com/m6w6/ext-pq/issues/19 failed tests
  so temporarily ignore them with pgsql < 9.3 on EL-7
- open https://github.com/m6w6/ext-pq/issues/18 pgsql < 9.3

* Wed May  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (stable)

* Tue Jan 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- cleanup for Fedora review #1299907
- drop scriptlets (replaced by file triggers in php-pear)
- ignore 1 failed test with PHP 5.4.16

* Tue Jan 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 (stable)

* Mon Dec  7 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.RC1
- Update to 1.0.0RC1 (beta)

* Sat Sep  5 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0 (beta)

* Wed Jul 29 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-0.3.RC2
- allow build against rh-php56 (as more-php56)

* Tue Jul 28 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-0.2.RC2
- Update to 0.6.0RC2 (beta)
- raise dependency on raphf 1.1.0

* Wed Jun 10 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-0.1.RC1
- Update to 0.6.0RC1
- drop runtime dependency on pear, new scriptlets

* Wed Dec 24 2014 Remi Collet <remi@fedoraproject.org> - 0.5.5-1.1
- Fedora 21 SCL mass rebuild

* Sat Oct 25 2014 Remi Collet <remi@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5

* Sat Oct 18 2014 Remi Collet <remi@fedoraproject.org> - 0.5.2-2
- launch a postgresql server for test
- enable upstream test suite during build

* Fri Oct 17 2014 Remi Collet <remi@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Thu Oct 16 2014 Remi Collet <remi@fedoraproject.org> - 0.5.1-1
- initial package, version 0.5.1 (beta)
