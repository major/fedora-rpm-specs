# Define handlers for php
%define php /usr/bin/php-cgi
%define apr /usr/bin/apr-1-config
%if 0%{?fedora}
	%define handler php5-script
%endif
%if 0%{?rhel}
	%define handler x-httpd-php
%endif

%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}

Name: mod_suphp
Version: 0.7.2
Release: 26%{?dist}
Summary: An apache2 module for executing PHP scripts with the permissions of their owners

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.suphp.org/
Source0: http://www.suphp.org/download/suphp-%{version}.tar.gz
Source1: suphp.conf
Source2: mod_suphp.conf
Source3: README.fedora
Source4: mod_suphp.module.conf
Patch0: mod_suphp-0.7.2-Apache24.patch
Patch1: mod_suphp-c99.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: httpd-devel >= 2.0, apr-devel, autoconf, libtool
Requires: httpd >= 2.0, %{php}
Requires: httpd-mmn = %{_httpd_mmn}


%description
suPHP is an Apache module for executing PHP scripts with the permissions of
their owners. It consists of an Apache module (mod_suphp) and a setuid root
binary (suphp) that is called by the Apache module to change the uid of the
process executing the PHP interpreter.

Please take a look at %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}/README.fedora for
installation instructions.


%prep
%setup -q -n suphp-%{version}
%patch -P0 -p 1 -b .ap24
%patch -P1 -p1


# fill placeholders
sed -e 's|###PHP-BIN###|%{php}|g; s|###HANDLER###|%{handler}|g;' %{SOURCE1} > suphp.conf
sed -e 's|###HANDLER###|%{handler}|g;' %{SOURCE3} > README.fedora

%if 0%{?fedora}
	cp -a %{SOURCE4} mod_suphp.module.conf
	sed -e '/###LOAD###/d; s|###HANDLER###|%{handler}|g;' %{SOURCE2} > mod_suphp.conf
%endif

%if 0%{?rhel}
	sed -e 's|###LOAD###|LoadModule suphp_module modules/mod_suphp.so|; s|###HANDLER###|%{handler}|g;' %{SOURCE2} > mod_suphp.conf
%endif


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
aclocal
libtoolize --force
automake --add-missing
autoreconf

echo "Building mod_suphp with %{php} as PHP interpreter and %{apr} for the apr configuration script."
echo "%{handler} is used as a AddHandler."
%configure \
	--with-apr=%{apr} \
	--with-apxs=%{_httpd_apxs} \
	--with-apache-user=apache \
	--with-min-uid=500 \
	--with-min-gid=500 \
	--with-logfile=/var/log/httpd/suphp_log \
	--with-setid-mode=owner 

pushd src
make %{?_smp_mflags} suphp
popd

pushd src/apache2
%{_httpd_apxs} -c mod_suphp.c
mv .libs/mod_suphp.so .
popd


%install
rm -rf %{buildroot}
%{__install} -c -m 4755 -D src/suphp %{buildroot}%{_sbindir}/suphp
%{__install} -m 755 -D src/apache2/mod_suphp.so %{buildroot}%{_libdir}/httpd/modules/mod_suphp.so

# Install the config files
%{__install} -m 644 -D suphp.conf %{buildroot}%{_sysconfdir}/suphp.conf
%{__install} -m 644 -D mod_suphp.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_suphp.conf
%if 0%{?fedora}
	%{__install} -m 644 -D mod_suphp.module.conf %{buildroot}%{_sysconfdir}/httpd/conf.modules.d/02-mod_suphp.conf
%endif

# Rename docs
cp doc/CONFIG CONFIG.suphp
cp doc/apache/CONFIG CONFIG.apache



%files
%doc README COPYING CONFIG.suphp CONFIG.apache README.fedora
%attr (4550, root, apache) %{_sbindir}/suphp
%{_libdir}/httpd/modules/*.so
%config(noreplace) %{_sysconfdir}/suphp.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_suphp.conf
%if 0%{?fedora}
	%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/02-mod_suphp.conf
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.2-25
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Florian Weimer <fweimer@redhat.com> - 0.7.2-20
- Fix C99 compatibility issue

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 0.7.2-13
- Use C++14 as this code is not C++17 ready

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 23 2015 Andreas Thienemann <andreas@bawue.net> - 0.7.2-1
- Upgraded to new upstream release.
- Got rid of Fedora 5 and older compatibility.
- Fixed module loading on EL.
- Removed userdir handler patch. Seems not necessarily anymore.
- Reworked specfile.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 0.6.3-14
- fix _httpd_mmn expansion in absence of httpd-devel

* Wed Dec 11 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.3-13
- Fix %%description path to README.fedora if doc dir is unversioned (#993976).
- Fix bogus date in %%changelog.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Jan Kaluza <jkaluza@redhat.com> - 0.6.3-9
- Fix compilation issues with httpd-2.4 (#809750)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-8
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 07 2008 Andreas Thienemann <andreas@bawue.net> - 0.6.3-3
- Fix conditionals, fix FTBFS #449578

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.3-2
- fix license tag

* Sun Mar 30 2008 Andreas Thienemann <andreas@bawue.net> - 0.6.3-1
- Updated to 0.6.3 fixing two security problems. #439687

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.2-2
- Autorebuild for GCC 4.3

* Sat Mar 10 2007 Andreas Thienemann <andreas@bawue.net> - 0.6.2-1
- Updated to 0.6.2
- Reverted our double free patch. Upstream fixed their SmartPointer
  implementation.
- Reverted our apr Patch, upstream is working correctly with Apache 2.2 now

* Fri Nov 10 2006 Andreas Thienemann <andreas@bawue.net> - 0.6.1-4
- Fix double free corruption. For real this time. :-/

* Fri Sep 08 2006 Andreas Thienemann <andreas@bawue.net> - 0.6.1-3
- Finally fixed double free corruption #192415
- Fixed up configuration creation

* Wed May 24 2006 Andreas Thienemann <andreas@bawue.net> - 0.6.1-2
- Corrected handler for mod_suphp.conf
- Minor cleanups and fixes

* Mon Feb 06 2006 Andreas Thienemann <andreas@bawue.net> 0.6.1-1
- Updated to 0.6.1

* Sat Jul 09 2005 Andreas Thienemann <andreas@bawue.net> 0.5.2-8
- Added a dependency on a specific httpd-mmn

* Tue Jul 05 2005 Andreas Thienemann <andreas@bawue.net> 0.5.2-7
- Bumped up the releasever

* Tue Jul 05 2005 Andreas Thienemann <andreas@bawue.net> 0.5.2-6
- Added correct name to %%setup macro

* Thu Jun 30 2005 Andreas Thienemann <andreas@bawue.net> 0.5.2-5
- Rollback of namechange. Now we're mod_suphp again.

* Thu Jun 30 2005 Andreas Thienemann <andreas@bawue.net> 0.5.2-4
- Cleanup of specfile, incorporated suggestions from "spot"
- Modified configure command to use cgi-php for FC4, php otherwise

* Sat Nov 13 2004 Andreas Thienemann <andreas@bawue.net> 0.5.2-3
- Added "--disable-checkpath" in order to allow /~user URLs

* Sat Nov 13 2004 Andreas Thienemann <andreas@bawue.net> 0.5.2-2
- Fixed the wrong path in the logfile directive

* Sat Nov 13 2004 Andreas Thienemann <andreas@bawue.net> 0.5.2-1
- initial package
