# spec file for php-zmq
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?php_inidir:  %global php_inidir  %{_sysconfdir}/php.d}
%{!?__pecl:      %global __pecl      %{_bindir}/pecl}

%global with_zts   0%{?__ztsphp:1}
%global pecl_name  zmq
%global with_tests %{?_without_tests:0}%{!?_without_tests:1}
%if "%{php_version}" < "5.6"
%global ini_name   %{pecl_name}.ini
%else
%global ini_name   40-%{pecl_name}.ini
%endif

Summary:        ZeroMQ messaging
Name:           php-%{pecl_name}
Version:        1.1.3
Release:        33%{?dist}
License:        BSD-3-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}.tgz

Patch0:         https://patch-diff.githubusercontent.com/raw/zeromq/php-zmq/pull/216.patch
Patch1:         https://patch-diff.githubusercontent.com/raw/zeromq/php-zmq/pull/222.patch
Patch2:         https://patch-diff.githubusercontent.com/raw/zeromq/php-zmq/pull/228.patch

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel > 5.2
BuildRequires:  php-pear
BuildRequires:  zeromq-devel

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# 1.0.7 is the first pecl release.
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
ZeroMQ is a software library that lets you quickly design and implement
a fast message-based applications.


%prep
%setup -q -c

# fix new default of MAX_SOCKETS
# Using current version, so this can be checked in next version and removed
# if appropriate. (still not fixed in 1.1.2, maybe later)
sed -i "s/int(1024)/int(1023)/g" %{pecl_name}-%{version}/tests/032-contextopt.phpt

mv %{pecl_name}-%{version} NTS

cd NTS
%patch -P0 -p1 -b .pr216
%patch -P1 -p1 -b .pr222
%patch -P2 -p1 -b .pr228
cd ..

%if %{with_zts}
# Duplicate source tree for NTS / ZTS build
cp -pr NTS ZTS
%endif

# Create configuration file
cat << 'EOF' | tee  %{ini_name}
; Enable %{summary} extension module
extension=%{pecl_name}.so
EOF


%build
cd NTS
%{_bindir}/phpize
%configure \
    --with-zmq \
    --with-libdir=%{_lib} \
    --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
    --with-zmq \
    --with-libdir=%{_lib} \
    --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
make -C NTS \
     install INSTALL_ROOT=%{buildroot}

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

%if %{with_zts}
make -C ZTS \
     install INSTALL_ROOT=%{buildroot}

install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Test & Documentation
for i in $(grep 'role="test"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd NTS
: Minimal load test for NTS extension
php --no-php-ini \
    --define extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_tests}
: upstream test suite for NTS extension
export TEST_PHP_ARGS="-n -d extension_dir=$PWD/modules -d extension=%{pecl_name}.so"
export REPORT_EXIT_STATUS=1
export TEST_PHP_EXECUTABLE=%{_bindir}/php
%{_bindir}/php -n run-tests.php -q --show-diff
%endif

%if %{with_zts}
cd ../ZTS
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}/%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_tests}
: upstream test suite for ZTS extension
export TEST_PHP_ARGS="-n -d extension_dir=$PWD/modules -d extension=%{pecl_name}.so"
export TEST_PHP_EXECUTABLE=%{_bindir}/zts-php
%{_bindir}/zts-php -n run-tests.php -q --show-diff
%endif
%endif


%files
%doc %{pecl_docdir}/%{pecl_name}
%doc %{pecl_testdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.1.3-32
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 1.1.3-30
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.1.3-27
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Remi Collet <remi@remirepo.net> - 1.1.3-25
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.1.3-23
- rebuild for https://fedoraproject.org/wiki/Changes/php82
- add patch for PHP 8.2 from https://github.com/zeromq/php-zmq/pull/228

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov  3 2021 Remi Collet <remi@fedoraproject.org> - 1.1.3-20
- rebuild for https://fedoraproject.org/wiki/Changes/php81
- add patch for PHP 8.1 from https://github.com/zeromq/php-zmq/pull/222

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar  5 2021 Remi Collet <remi@fedoraproject.org> - 1.1.3-18
- rebuild for https://fedoraproject.org/wiki/Changes/php80
- add patch for PHP 8 from https://github.com/zeromq/php-zmq/pull/216

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Remi Collet <remi@remirepo.net> - 1.1.3-13
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Remi Collet <remi@remirepo.net> - 1.1.3-10
- add patch for 7.3 from
  https://github.com/mkoppanen/php-zmq/pull/195
- add patch to fix build with old GCC
  from https://github.com/mkoppanen/php-zmq/pull/170

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.1.3-7
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.1.3-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.1.3-2
- rebuild for https://fedoraproject.org/wiki/Changes/php71
- ignore 2 failed tests with PHP 7.1

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- update to 1.1.3
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Thu Feb 25 2016 Remi Collet <remi@fedoraproject.org> - 1.0.8-10
- drop scriptlets (replaced by file triggers in php-pear) #1310546

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.0.8-8
- rebuilt for new zeromq 4.1.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.0.8-6
- build against zeromq-4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 1.0.8-4
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 25 2013 Remi Collet <remi@fedoraproject.org> - 1.0.8-2
- cleanups

* Thu Oct 24 2013 Remi Collet <remi@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8
- run upstream test suite during build
- install tests in pecl test_dir

* Thu Oct 24 2013 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- initial package, version 1.0.7 (beta)
- open https://github.com/mkoppanen/php-zmq/pull/108
  to fix build warnings and include tests
- rewrite spec file.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-11.20120613git516bd6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 0.6.0-10.20120613git516bd6f
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9.20120613git516bd6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Ralph Bean <rbean@redhat.com> - 0.6.0-8.20120613git516bd6f
 - Add ABI check to conform with PHP guidelines.
* Mon Oct 22 2012 Ralph Bean <rbean@redhat.com> - 0.6.0-7.20120613git516bd6f
 - Rebuilt against zeromq3.
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6.20120613git516bd6f
 - Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.6.0-5.20120613git516bd6f
 - Fixed the license field back to just "BSD".  The files thought to be
   PHP-licensed were in fact generated by "phpize" in the %%build section.
* Thu Jun 14 2012 Ralph Bean <rbean@redhat.com> - 0.6.0-4.20120613git516bd6f
 - Fixed the private-shared-object-provides for reals with John Ciesla's help.
* Wed Jun 13 2012 Ralph Bean <rbean@redhat.com> - 0.6.0-3.20120613git516bd6f
 - Updated License to BSD and PHP.
 - Removed spurious gcc BuildRequires.
 - Fixed private-shared-object-provides.
* Wed Jun 13 2012 Ralph Bean <rbean@redhat.com> - 0.6.0-2.20120613git516bd6f
 - Using tarball of git checkout since the 0.6.0 release won't build anymore.
 - Using valid shortname for BSD license.
 - Added README and LICENSE to the doc
 - Use %%global instead of %%define.
 - Changed 0MQ to 0MQ/zmq/zeromq in Summary and Description to help with
   search.
 - Fully qualified Source URL.
 - Updated to modern BuildRequires.
 - Separated %%build out into %%build and %%install.
 - Removed unnecessary references to buildroot.
 - Removed unnecessary %%defattr.
 - Changed Group from Web/Applications to Development/Libraries.
 - Removed hardcoded Packager tag.
 - Added %%check section.
 - Marked /etc/php.d/zmq.ini as a config file.
* Wed Jun 15 2011 Rick Moran <moran@morangroup.org>
 - Minor Changes.
* Thu Apr 8 2010 Mikko Koppanen <mkoppanen@php.net>
 - Initial spec file
