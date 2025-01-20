# Fedora spec file for php-pecl-event
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global with_tests  0%{!?_without_tests:1}
%global pecl_name   event
%global ini_name    40-%{pecl_name}.ini

%global upstream_version 3.1.4
#global upstream_prever  RC3
#global upstream_postver r1
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}

Summary:       Provides interface to libevent library
Name:          php-pecl-%{pecl_name}
Version:       %{upstream_version}%{?upstream_prever:~%{upstream_prever}}%{?upstream_postver:+%{upstream_postver}}
Release:       5%{?dist}
License:       PHP-3.01
URL:           https://pecl.php.net/package/event
Source0:       https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: gcc
BuildRequires: make
BuildRequires: php-devel
BuildRequires: php-pear
BuildRequires: libevent-devel >= 2.0.2
BuildRequires: openssl-devel
BuildRequires: pkgconfig

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}
Requires:      php-sockets%{?_isa}

Provides:      php-%{pecl_name} = %{version}
Provides:      php-%{pecl_name}%{?_isa} = %{version}
Provides:      php-pecl(%{pecl_name}) = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
This is an extension to efficiently schedule I/O, time and signal based
events using the best I/O notification mechanism available for specific
platform. This is a port of libevent to the PHP infrastructure.

Version 1.0.0 introduces:
* new OO API breaking backwards compatibility
* support of libevent 2+ including HTTP, DNS, OpenSSL and the event listener.

Documentation: http://php.net/event


%prep
%setup -q -c 

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
DIR=$(%{__php} -r 'echo "php" . PHP_MAJOR_VERSION;')
extver=$(sed -n '/#define PHP_EVENT_VERSION/{s/.* "//;s/".*$//;p}' $DIR/php_event.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}%{?upstream_postver}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}%{?upstream_postver}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension = %{pecl_name}.so
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-event-libevent-dir=%{_prefix} \
    --with-openssl-dir=%{_prefix} \
    --with-libdir=%{_lib} \
    --with-event-core \
    --with-event-extra \
    --with-event-openssl \
    --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Install the configuration file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the package XML file
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}

if [ -f %{php_extdir}/sockets.so ]; then
  OPTS="-d extension=sockets.so"
fi

: Minimal load test for the extension
%{__php} --no-php-ini $OPTS  \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with_tests}
: Upstream test suite for the extension
SKIP_ONLINE_TESTS=1 \
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n $OPTS -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Remi Collet <remi@fedoraproject.org> - 3.1.4-4
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 3.1.4-3
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Remi Collet <remi@remirepo.net> - 3.1.4-1
- update to 3.1.4

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 3.1.3-2
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Mon Jan 29 2024 Remi Collet <remi@remirepo.net> - 3.1.3-1
- update to 3.1.3

* Wed Jan 24 2024 Remi Collet <remi@remirepo.net> - 3.1.2-1
- update to 3.1.2

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1
- build out of sources tree

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 3.0.8-5
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 3.0.8-2
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov  9 2022 Remi Collet <remi@remirepo.net> - 3.0.8-1
- update to 3.0.8

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 3.0.7-3
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Remi Collet <remi@remirepo.net> - 3.0.7-1
- update to 3.0.7

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 3.0.6-2
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Sep 24 2021 Remi Collet <remi@remirepo.net> - 3.0.6-1
- update to 3.0.6

* Thu Sep 23 2021 Remi Collet <remi@remirepo.net> - 3.0.5-1
- update to 3.0.5
- add patch for OpenSSL 3.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.0.3-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 27 2021 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 3.0.2+r1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Tue Feb 16 2021 Remi Collet <remi@remirepo.net> - 3.0.2+r1-1
- update to 3.0.2r1 (stable)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2 (beta)

* Wed Dec  2 2020 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1 (beta)

* Thu Oct 29 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0 (beta)

* Tue Sep 15 2020 Remi Collet <remi@remirepo.net> - 2.5.7-2
- rebuild for new libevent

* Mon Sep  7 2020 Remi Collet <remi@remirepo.net> - 2.5.7-1
- update to 2.5.7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Remi Collet <remi@remirepo.net> - 2.5.6-1
- update to 2.5.6

* Wed May 13 2020 Remi Collet <remi@remirepo.net> - 2.5.5-1
- update to 2.5.5

* Mon Feb 24 2020 Remi Collet <remi@remirepo.net> - 2.5.4-1
- update to 2.5.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 2.5.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0

* Fri Apr 19 2019 Remi Collet <remi@remirepo.net> - 2.4.4-1
- update to 2.4.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Remi Collet <remi@remirepo.net> - 2.4.2-1
- update to 2.4.2

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 2.4.1-2
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Aug 17 2018 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  2 2018 Remi Collet <remi@remirepo.net> - 2.3.0-8
- rebuild for libevent

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 2.3.0-6
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 2.3.0-5
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Remi Collet <remi@remirepo.net> - 2.3.0-2
- rebuild with new libevent and test suite fully enabled

* Sun Mar 26 2017 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0 (stable)

* Wed Feb 15 2017 Remi Collet <remi@fedoraproject.org> - 2.3.0-0.3.RC1
- ignore 2 failed tests, fix FTBFS

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-0.2.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 2.3.0-0.1.RC1
- Update to 2.3.0RC1

* Wed Jun 08 2016 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Fri Apr 22 2016 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4 (no change)

* Thu Apr 21 2016 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3 (no change)

* Fri Apr  1 2016 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Thu Mar 17 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Thu Feb 11 2016 Remi Collet <remi@fedoraproject.org> - 1.11.3-1
- Update to 1.11.3

* Wed Feb 10 2016 Remi Collet <remi@fedoraproject.org> - 1.11.1-4
- drop scriptlets (replaced by file triggers in php-pear)
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Remi Collet <remi@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1 (stable)
- don't provide test suite

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Remi Collet <remi@fedoraproject.org> - 1.10.3-1
- Update to 1.10.3 (no change)

* Fri Jun 20 2014 Remi Collet <remi@fedoraproject.org> - 1.10.2-1
- Update to 1.10.2 (stable)

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 1.10.1-3
- rebuild for https://fedoraproject.org/wiki/Changes/Php56

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Remi Collet <remi@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (stable)

* Wed Apr 23 2014 Remi Collet <rcollet@redhat.com> - 1.9.1-2
- add numerical prefix to extension configuration file

* Sun Mar 23 2014 Remi Collet <remi@fedoraproject.org> - 1.9.1-1
- Update to 1.9.1 (stable)

* Sun Mar 23 2014 Remi Collet <remi@fedoraproject.org> - 1.9.0-2
- add patch for php 5.6
  https://bitbucket.org/osmanov/pecl-event/pull-request/7

* Fri Jan 17 2014 Remi Collet <remi@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0 (stable)
- add option to disable tests during build

* Sat Jan 11 2014 Remi Collet <remi@fedoraproject.org> - 1.8.1-2
- install doc in pecl doc_dir
- install tests in pecl test_dir
- open https://bitbucket.org/osmanov/pecl-event/pull-request/6

* Mon Oct 07 2013 Remi Collet <remi@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1 (stable)
- drop patch merged upstream
- patch for https://bitbucket.org/osmanov/pecl-event/pull-request/4

* Sun Oct 06 2013 Remi Collet <remi@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0
- patch for https://bitbucket.org/osmanov/pecl-event/pull-request/3

* Mon Sep 16 2013 Remi Collet <remi@fedoraproject.org> - 1.7.8-1
- Update to 1.7.8

* Sun Sep 08 2013 Remi Collet <remi@fedoraproject.org> - 1.7.6-1
- Update to 1.7.6

* Mon Aug 19 2013 Remi Collet <remi@fedoraproject.org> - 1.7.5-1
- Update to 1.7.5

* Sun Jul 28 2013 Remi Collet <remi@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Fri Jul 26 2013 Remi Collet <remi@fedoraproject.org> - 1.7.1-2
- cleanups before review

* Wed Jul 24 2013 Remi Collet <remi@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Thu Jul 18 2013 Remi Collet <remi@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Thu Jul 18 2013 Remi Collet <remi@fedoraproject.org> - 1.6.2-2
- missing requires php-sockets
- enable thread safety for ZTS extension

* Thu Jul 18 2013 Remi Collet <remi@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Sat Apr 20 2013 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- initial package, version 1.6.1
- upstream bugs:
  https://bugs.php.net/64678 missing License
  https://bugs.php.net/64679 buffer overflow
  https://bugs.php.net/64680 skip online test
