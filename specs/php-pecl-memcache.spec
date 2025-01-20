# Fedora spec file for php-pecl-memcache
#
# Copyright (c) 2007-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#

%bcond_without     tests

%global pecl_name  memcache
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Summary:      Extension to work with the Memcached caching daemon
Name:         php-pecl-memcache
Version:      8.2
Release:      10%{?dist}
Source0:      https://pecl.php.net/get/%{sources}.tgz
License:      PHP-3.01
Group:        Development/Languages
URL:          https://pecl.php.net/package/%{pecl_name}

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 8.0
BuildRequires: php-pear
BuildRequires: zlib-devel
%if %{with tests}
BuildRequires: memcached
%endif

Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}

Provides:     php-pecl(%{pecl_name}) = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:     php-%{pecl_name} = %{version}
Provides:     php-%{pecl_name}%{?_isa} = %{version}


%description
Memcached is a caching daemon designed especially for
dynamic web applications to decrease database load by
storing objects in memory.

This extension allows you to work with memcached through
handy OO and procedural interfaces.

Memcache can be used as a PHP session handler.


%prep 
%setup -c -q

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

pushd %{sources}
extver=$(sed -n '/#define PHP_MEMCACHE_VERSION/{s/.* "//;s/".*$//;p}' src/php_memcache.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream version is now ${extver}, expecting %{version}%{?prever:-%{prever}}
   : Update the pdover macro and rebuild.
   exit 1
fi
popd

cat >%{ini_name} << 'EOF'
; ----- Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; ----- Options for the %{pecl_name} module
; see http://www.php.net/manual/en/memcache.ini.php

;  Whether to transparently failover to other servers on errors
;memcache.allow_failover=1
;  Data will be transferred in chunks of this size
;memcache.chunk_size=32768
;  Autocompress large data
;memcache.compress_threshold=20000
;  The default TCP port number to use when connecting to the memcached server 
;memcache.default_port=11211
;  Hash function {crc32, fnv}
;memcache.hash_function=crc32
;  Hash strategy {standard, consistent}
;memcache.hash_strategy=consistent
;  Defines how many servers to try when setting and getting data.
;memcache.max_failover_attempts=20
;  The protocol {ascii, binary} : You need a memcached >= 1.3.0 to use the binary protocol
;  The binary protocol results in less traffic and is more efficient
;memcache.protocol=ascii
;  Redundancy : When enabled the client sends requests to N servers in parallel
;memcache.redundancy=1
;memcache.session_redundancy=2
;  Lock Timeout
;memcache.lock_timeout = 15

;memcache.prefix_host_key = Off
;memcache.prefix_host_key_remove_www = On
;memcache.prefix_host_key_remove_subdomain = Off
;memcache.prefix_static_key = ''

; ----- Options to use the memcache session handler

; RPM note : save_handler and save_path are defined
; for mod_php, in /etc/httpd/conf.d/php.conf
; for php-fpm, in /etc/php-fpm.d/*conf

;  Use memcache as a session handler
;session.save_handler=memcache
;  Defines a comma separated of server urls to use for session storage
;  Only used when memcache.session_save_path is not set
;session.save_path="tcp://localhost:11211?persistent=1&weight=1&timeout=1&retry_interval=15"
;memcache.session_prefix_host_key = Off
;memcache.session_prefix_host_key_remove_www = On
;memcache.session_prefix_host_key_remove_subdomain = Off
;memcache.session_prefix_static_key = ''
;memcache.session_save_path = ''
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --with-php-config=%{__phpconfig}
%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Drop in the bit of configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -Dpm 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep '<file .* role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    -m | grep %{pecl_name}

%if %{with tests}
cd %{sources}
: ignore test with erratic results
rm tests/040.phpt
rm tests/056.phpt
rm tests/100c.phpt

: Configuration for tests
sed -e "s:/var/run/memcached/memcached.sock:$PWD/memcached.sock:" \
    -i tests/connect.inc

: Launch the daemons
memcached -p 11211 -U 11211      -d -P $PWD/memcached1.pid
memcached -p 11212 -U 11212      -d -P $PWD/memcached2.pid
memcached -s $PWD/memcached.sock -d -P $PWD/memcached3.pid

: Upstream test suite for the extension
ret=0
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension_dir=$PWD/modules -d extension=%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php --show-diff || ret=1

: Cleanup
if [ -f memcached2.pid ]; then
   kill $(cat memcached?.pid)
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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 8.2-8
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 8.2-6
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 8.2-3
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May  2 2023 Remi Collet <remi@remirepo.net> - 8.2-1
- update to 8.2
- drop patches merged upstream

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 8.0-7
- use SPDX license ID

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 8.0-6
- rebuild for https://fedoraproject.org/wiki/Changes/php82
- add patch for PHP 8.2 from
  https://github.com/websupport-sk/pecl-memcache/pull/104

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 8.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php81
- add patch for PHP 8.1 from
  https://github.com/websupport-sk/pecl-memcache/pull/88

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 8.0-1
- update to 8.0
- raise dependency on PHP 8.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Remi Collet <remi@remirepo.net> - 4.0.5.2-1
- update to 4.0.5.2 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Remi Collet <remi@remirepo.net> - 4.0.5.1-1
- update to 4.0.5.1 (no change)
- enable test suite

* Thu Dec 19 2019 Remi Collet <remi@remirepo.net> - 4.0.5-1
- update to 4.0.5
- switch back to sources from PECL

* Thu Oct  3 2019 Remi Collet <remi@remirepo.net> - 4.0.4-1
- update to 4.0.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3
- drop patches merged upstream
- open https://github.com/websupport-sk/pecl-memcache/pull/48 version

* Tue Mar 19 2019 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2 from https://github.com/websupport-sk/pecl-memcache
- add patch for PHP < 7.2 from
  https://github.com/websupport-sk/pecl-memcache/pull/40
- add patch to allow session.save_path from
  https://github.com/websupport-sk/pecl-memcache/pull/45

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-0.12.20170802.e702b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 3.0.9-0.11.20170802.e702b5f
- Rebuild for https://fedoraproject.org/wiki/Changes/php73
- add patch for PHP 7.3 from
  https://github.com/websupport-sk/pecl-memcache/pull/30

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-0.10.20170802.e702b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-0.9.20170802.e702b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 3.0.9-0.8.20170802.e702b5f
- undefine _strict_symbol_defs_build

* Fri Oct  6 2017 Remi Collet <remi@remirepo.net> - 3.0.9-0.7.20170802.e702b5f
- refresh to more recent snapshot
- add patch from https://github.com/websupport-sk/pecl-memcache/issues/23

* Tue Oct  3 2017 Remi Collet <remi@remirepo.net> - 3.0.9-0.6.20161124gitdf7735e
- refresh

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-0.5.20160311git4991c2f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-0.4.20160311git4991c2f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-0.3.20160311git4991c2f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 3.0.9-0.2.20160311git4991c2f
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <rcollet@redhat.com> - 3.0.9-0.1.20160311git4991c2f
- git snapshopt for PHP 7
- sources from https://github.com/websupport-sk/pecl-memcache (for PHP 7)
- don't install/register tests
- fix license installation

* Wed Feb 10 2016 Remi Collet <remi@fedoraproject.org> - 3.0.8-10
- drop scriptlets (replaced by file triggers in php-pear)
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 Remi Collet <rcollet@redhat.com> - 3.0.8-7
- fix gcc 5 FTBFS

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 3.0.8-5
- rebuild for https://fedoraproject.org/wiki/Changes/Php56

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Remi Collet <rcollet@redhat.com> - 3.0.8-3
- add numerical prefix to extension configuration file
- install doc in pecl_docdir
- install tests in pecl_testdir

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 08 2013 Remi Collet <remi@fedoraproject.org> - 3.0.8-1
- Update to 3.0.8
- enable conditional ZTS extension build

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 3.0.7-7
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 29 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-5
- add patch for https://bugs.php.net/59602
  segfault in getExtendedStats
- also provides php-memcache

* Fri Oct 19 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-4
- improve comment in configuration about session.

* Tue Sep 25 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-3
- switch back to previous patch as possible memleak
  more acceptable than certain segfault

* Sun Sep 23 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-2
- use upstream patch instead of our (memleak)

* Sun Sep 23 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-1
- update to 3.0.7
- drop patches merged upstream
- cleanup spec

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Joe Orton <jorton@redhat.com> - 3.0.6-4
- fix php_stream_cast() usage
- fix memory corruption after unserialization (Paul Clifford)
- package license

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 3.0.6-3
- rebuild against PHP 5.4, with patch
- fix filters

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 11 2011 Remi Collet <Fedora@FamilleCollet.com> 3.0.6-1
- update to 3.0.6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 23 2010  Remi Collet <Fedora@FamilleCollet.com> 3.0.5-2
- add filter_provides to avoid private-shared-object-provides memcache.so

* Tue Oct 05 2010 Remi Collet <Fedora@FamilleCollet.com> 3.0.5-1
- update to 3.0.5

* Thu Sep 30 2010 Remi Collet <Fedora@FamilleCollet.com> 3.0.4-4
- patch for bug #599305 (upstream #17566)
- add minimal load test in %%check

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Remi Collet <Fedora@FamilleCollet.com> 3.0.4-2
- rebuild for new PHP 5.3.0 ABI (20090626)

* Sat Feb 28 2009 Remi Collet <Fedora@FamilleCollet.com> 3.0.4-1
- new version 3.0.4

* Tue Jan 13 2009 Remi Collet <Fedora@FamilleCollet.com> 3.0.3-1
- new version 3.0.3

* Thu Sep 11 2008 Remi Collet <Fedora@FamilleCollet.com> 3.0.2-1
- new version 3.0.2

* Thu Sep 11 2008 Remi Collet <Fedora@FamilleCollet.com> 2.2.4-1
- new version 2.2.4 (bug fixes)

* Sat Feb  9 2008 Remi Collet <Fedora@FamilleCollet.com> 2.2.3-1
- new version

* Thu Jan 10 2008 Remi Collet <Fedora@FamilleCollet.com> 2.2.2-1
- new version

* Thu Nov 01 2007 Remi Collet <Fedora@FamilleCollet.com> 2.2.1-1
- new version

* Sat Sep 22 2007 Remi Collet <Fedora@FamilleCollet.com> 2.2.0-1
- new version
- add new INI directives (hash_strategy + hash_function) to config
- add BR on php-devel >= 4.3.11 

* Mon Aug 20 2007 Remi Collet <Fedora@FamilleCollet.com> 2.1.2-1
- initial RPM

