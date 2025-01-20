# Fedora spec file for php-pecl-memcached
#
# Copyright (c) 2009-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests

%global pecl_name   memcached
# After 40-igbinary, 40-json, 40-msgpack
%global ini_name    50-%{pecl_name}.ini

%global upstream_version 3.3.0
#global upstream_prever  RC1
# upstream use    dev => alpha => beta => RC
# make RPM happy  DEV => alpha => beta => rc
#global upstream_lower   rc1
%global sources    %{pecl_name}-%{upstream_version}%{?upstream_prever}

Summary:      Extension to work with the Memcached caching daemon
Name:         php-pecl-memcached
Version:      %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:      2%{?dist}
License:      PHP-3.01
URL:          https://pecl.php.net/package/%{pecl_name}

Source0:      https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 7
BuildRequires: php-pear
BuildRequires: php-json
BuildRequires: php-pecl-igbinary-devel
%ifnarch ppc64
BuildRequires: php-pecl-msgpack-devel
%endif
BuildRequires: libevent-devel  > 2
BuildRequires: libmemcached-devel >= 1.0.18
BuildRequires: zlib-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: fastlz-devel
BuildRequires: libzstd-devel
%if %{with tests}
BuildRequires: memcached
%endif

Requires:     php-json%{?_isa}
Requires:     php-igbinary%{?_isa}
Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}
%ifnarch ppc64
Requires:     php-msgpack%{?_isa}
%endif

Provides:     php-%{pecl_name} = %{version}
Provides:     php-%{pecl_name}%{?_isa} = %{version}
Provides:     php-pecl(%{pecl_name}) = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
This extension uses libmemcached library to provide API for communicating
with memcached servers.

memcached is a high-performance, distributed memory object caching system,
generic in nature, but intended for use in speeding up dynamic web 
applications by alleviating database load.

It also provides a session handler (memcached). 


%prep 
%setup -c -q
# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -e '/name=.fastlz/d' \
    -i package.xml

cd %{sources}
rm -r fastlz

# Chech version as upstream often forget to update this
extver=$(sed -n '/#define PHP_MEMCACHED_VERSION/{s/.* "//;s/".*$//;p}' php_memcached.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever:%{upstream_prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever:%{upstream_prever}}.
   : Update the macro and rebuild.
   exit 1
fi
cd ..

cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; ----- Options to use the memcached session handler

; RPM note : save_handler and save_path are defined
; for mod_php, in /etc/httpd/conf.d/php.conf
; for php-fpm, in /etc/php-fpm.d/*conf

;  Use memcache as a session handler
;session.save_handler=memcached
;  Defines a comma separated list of server urls to use for session storage
;session.save_path="localhost:11211"

; ----- Configuration options
; http://php.net/manual/en/memcached.configuration.php

EOF

# default options with description from upstream
cat %{sources}/memcached.ini >>%{ini_name}


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --enable-memcached-igbinary \
           --enable-memcached-json \
           --enable-memcached-sasl \
%ifnarch ppc64
           --enable-memcached-msgpack \
%endif
           --enable-memcached-protocol \
           --with-system-fastlz \
           --with-zstd \
           --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Drop in the bit of configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
OPT="-n"
[ -f %{php_extdir}/igbinary.so ] && OPT="$OPT -d extension=igbinary.so"
[ -f %{php_extdir}/json.so ]     && OPT="$OPT -d extension=json.so"
[ -f %{php_extdir}/msgpack.so ]  && OPT="$OPT -d extension=msgpack.so"

: Minimal load test for NTS extension
%{__php} $OPT \
    -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
cd %{sources}
# XFAIL and very slow so no value
rm tests/expire.phpt
rm tests/flush_buffers.phpt
rm tests/touch_binary.phpt

ret=0

: Launch the Memcached service
port=$(%{__php} -r 'echo 10000 + PHP_MAJOR_VERSION*100 + PHP_MINOR_VERSION*10 + PHP_INT_SIZE;')
memcached -p $port -U $port      -d -P $PWD/memcached.pid
sed -e "s/11211/$port/" -i tests/*

: Port for MemcachedServer
port=$(%{__php} -r 'echo 11000 + PHP_MAJOR_VERSION*100 + PHP_MINOR_VERSION*10 + PHP_INT_SIZE;')
sed -e "s/3434/$port/" -i tests/*

: Run the upstream test Suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="$OPT -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php -q -x --show-diff || ret=1

# Cleanup
if [ -f memcached.pid ]; then
   kill $(cat memcached.pid)
   sleep 1
fi

exit $ret
%endif


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0
- enable zstd compression support

* Wed Oct 16 2024 Remi Collet <remi@fedoraproject.org> - 3.2.0-13
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 3.2.0-12
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 3.2.0-10
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Tue Jan 30 2024 Remi Collet <remi@remirepo.net> - 3.2.0-9
- build out of sources tree
- fix incompatible pointer types using patch from
  https://github.com/php-memcached-dev/php-memcached/pull/555

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 3.2.0-7
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 3.2.0-5
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 3.2.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php82
- add upstream patches for PHP 8.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 24 2022 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0

* Mon Mar  7 2022 Remi Collet <remi@remirepo.net> - 3.2.0~rc1-1
- update to 3.2.0RC1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 3.1.5-8
- rebuild for https://fedoraproject.org/wiki/Changes/php81
- add patch got PHP 8.1 from
  https://github.com/php-memcached-dev/php-memcached/pull/486
  https://github.com/php-memcached-dev/php-memcached/pull/487
- add patch to report about libmemcached-awesome from
  https://github.com/php-memcached-dev/php-memcached/pull/488

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 3.1.5-6
- rebuild for https://fedoraproject.org/wiki/Changes/php80
- add patches for PHP 8 from
  https://github.com/php-memcached-dev/php-memcached/pull/461
  https://github.com/php-memcached-dev/php-memcached/pull/463
  https://github.com/php-memcached-dev/php-memcached/pull/465
  https://github.com/php-memcached-dev/php-memcached/pull/467
  https://github.com/php-memcached-dev/php-memcached/pull/468
  https://github.com/php-memcached-dev/php-memcached/pull/469
  https://github.com/php-memcached-dev/php-memcached/pull/472
  https://github.com/php-memcached-dev/php-memcached/pull/473

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Remi Collet <remi@remirepo.net> - 3.1.5-4
- rebuild for new libevent

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec  4 2019 Remi Collet <remi@remirepo.net> - 3.1.5-1
- Update to 3.1.5

* Mon Oct  7 2019 Remi Collet <remi@remirepo.net> - 3.1.4-1
- Update to 3.1.4

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 3.1.3-4
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Remi Collet <remi@remirepo.net> - 3.1.3-1
- Update to 3.1.3

* Fri Dec 21 2018 Remi Collet <remi@remirepo.net> - 3.1.1-1
- Update to 3.1.1

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 3.0.4-6
- Rebuild for https://fedoraproject.org/wiki/Changes/php73
- add upstream patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  2 2018 Remi Collet <remi@remirepo.net> - 3.0.4-4
- rebuild for libevent

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 3.0.4-2
- undefine _strict_symbol_defs_build

* Tue Nov 21 2017 Remi Collet <remi@remirepo.net> - 3.0.4-1
- Update to 3.0.4

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 3.0.3-4
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.3 (php 7, stable)
- build with --enable-memcached-protocol option

* Mon Feb 13 2017 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- update to 3.0.2 (php 7, stable)

* Thu Feb  9 2017 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- update to 3.0.1 (php 7, stable)
- switch to pecl sources
- enable test suite
- open https://github.com/php-memcached-dev/php-memcached/pull/319
  fix test suite for 32bits build

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-0.2.20160217git6ace07d
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <rcollet@redhat.com> - 3.0.0-0.1.20160217git6ace07d
- git snapshopt for PHP 7
- don't install/register tests
- fix license installation

* Wed Feb 10 2016 Remi Collet <remi@fedoraproject.org> - 2.2.0-8
- drop scriptlets (replaced by file triggers in php-pear)
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 2.2.0-4
- rebuild for https://fedoraproject.org/wiki/Changes/Php56

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Remi Collet <rcollet@redhat.com> - 2.2.0-2
- add numerical prefix to extension configuration file

* Wed Apr  2 2014  Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0 (stable)
- add all ini options in configuration file (comments)
- install doc in pecl doc_dir
- install tests in pecl test_dir
- add dependency on pecl/msgpack (except on ppc64)
- add --with tests option to run upstream test suite during build

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 2.1.0-7
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012  Remi Collet <remi@fedoraproject.org> - 2.1.0-5
- requires libmemcached >= build version

* Sat Nov 17 2012  Remi Collet <remi@fedoraproject.org> - 2.1.0-4
- rebuild for libmemcached 1.0.14 (with SASL)
- switch to upstream patch
- add patch to report about SASL support in phpinfo

* Fri Oct 19 2012 Remi Collet <remi@fedoraproject.org> - 2.1.0-3
- improve comment in configuration about session.

* Sat Sep 22 2012 Remi Collet <remi@fedoraproject.org> - 2.1.0-2
- rebuild for new libmemcached
- drop sasl support

* Tue Aug 07 2012 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- add patch to lower libmemcached required version

* Tue Jul 31 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-4
- bump release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012  Remi Collet <remi@fedoraproject.org> - 2.0.1-3
- enable ZTS extension

* Sat Mar 03 2012  Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1

* Sat Mar 03 2012  Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.1.1736623
- update to git snapshot (post 2.0.0b2) for php 5.4 build

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 17 2011  Remi Collet <remi@fedoraproject.org> - 1.0.2-7
- rebuild against libmemcached 0.52
- adapted filter
- clean spec

* Thu Jun 02 2011  Remi Collet <Fedora@FamilleCollet.com> - 1.0.2-6
- rebuild against libmemcached 0.49

* Thu Mar 17 2011  Remi Collet <Fedora@FamilleCollet.com> - 1.0.2-5
- rebuilt with igbinary support
- add arch specific provides/requires

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 23 2010  Remi Collet <Fedora@FamilleCollet.com> - 1.0.2-3
- add filter_provides to avoid private-shared-object-provides memcached.so

* Fri Oct 01 2010 Remi Collet <fedora@famillecollet.com> - 1.0.2-2
- rebuild against libmemcached 0.44 with SASL support

* Tue May 04 2010 Remi Collet <fedora@famillecollet.com> - 1.0.2-1
- update to 1.0.2 for libmemcached 0.40

* Sat Mar 13 2010 Remi Collet <fedora@famillecollet.com> - 1.0.1-1
- update to 1.0.1 for libmemcached 0.38

* Sun Feb 07 2010 Remi Collet <fedora@famillecollet.com> - 1.0.0-3.1
- bump release

* Sat Feb 06 2010 Remi Collet <fedora@famillecollet.com> - 1.0.0-3
- rebuilt against new libmemcached
- add minimal %%check

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Remi Collet <fedora@famillecollet.com> - 1.0.0-1
- Update to 1.0.0 (First stable release)

* Sat Jun 27 2009 Remi Collet <fedora@famillecollet.com> - 0.2.0-1
- Update to 0.2.0 + Patch for HAVE_JSON constant

* Wed Apr 29 2009 Remi Collet <fedora@famillecollet.com> - 0.1.5-1
- Initial RPM

