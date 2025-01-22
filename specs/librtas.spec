Summary: Libraries to provide access to RTAS calls and RTAS events
Name:    librtas
Version: 2.0.6
Release: 3%{?dist}
URL:     https://github.com/ibm-power-utilities/librtas
License: LGPL-2.0-or-later

Source0: https://github.com/ibm-power-utilities/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: make

ExclusiveArch: %{power64}

%description
The librtas shared library provides userspace with an interface
through which certain RTAS calls can be made.  The library uses
either of the RTAS User Module or the RTAS system call to direct
the kernel in making these calls.

The librtasevent shared library provides users with a set of
definitions and common routines useful in parsing and dumping
the contents of RTAS events.

%package devel
Summary:  C header files for development with librtas
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The librtas-devel packages contains the header files necessary for
developing programs using librtas.

%prep
%autosetup -p1

%build
./autogen.sh
%configure --disable-silent-rules --disable-static
%make_build CFLAGS="$CFLAGS"

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f  %{buildroot}/%{_docdir}/librtas/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING.LESSER
%doc README Changelog
%{_libdir}/librtas.so.*
%{_libdir}/librtasevent.so.*

%files devel
%{_libdir}/librtas.so
%{_libdir}/librtasevent.so
%{_includedir}/librtas.h
%{_includedir}/librtasevent.h
%{_includedir}/librtasevent_v4.h
%{_includedir}/librtasevent_v6.h

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 02 2024 Than Ngo <than@redhat.com> - 2.0.6-1
- update to 2.0.6

* Fri Apr 05 2024 Than Ngo <than@redhat.com> - 2.0.5-2
- cleanup, dropped libversion.patch

* Tue Mar 05 2024 Than Ngo <than@redhat.com> - 2.0.5-1
- update to 2.0.5

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 16 2023 Than Ngo <than@redhat.com> - 2.0.4-2
- migrated to SPDX license

* Wed Jan 25 2023 Than Ngo <than@redhat.com> - 2.0.4-1
- 2.0.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Than Ngo <than@redhat.com> - 2.0.3-1
- 2.0.3
- updated url and source

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 10 2021 Than Ngo <than@redhat.com> - 2.0.2-10
- Fix License tag

* Tue Apr 06 2021 Than Ngo <than@redhat.com> - 2.0.2-9
- improve coverity fix

* Fri Mar 26 2021 Than Ngo <than@redhat.com> - 2.0.2-8
- Fix coverity issues

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Sinny Kumari <sinnykumari@fedoraproject.org> - 2.0.2-1
- Rebase to 2.0.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Sinny Kumari <sinnykumari@fedoraproject.org> - 2.0.1-1
- Rebase to 2.0.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.0-2
- Package cleanup, update URLs
- Use %%license

* Wed Apr 06 2016 Sinny Kumari <sinnykumari@fedoraproject.org> - 2.0.0-1
- Update to upstream release 2.0.0
- do-not-enable-debug-message patch is available in this release

* Mon Mar 21 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.4.0-2
- Do not enable debug message by default

* Fri Mar 11 2016 Sinny Kumari <sinnykumari@fedoraproject.org> - 1.4.0-1
- Update to latest upstream 1.4.0
- License change from CPL to LGPL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.3.14
- Update to latest upstream 1.3.14

* Fri Jul 03 2015 Jakub Čajka - 1.3.13-3
- Fix byteswapping see http://sourceforge.net/p/librtas/code/ci/4e46c718f42bf05e797c7fcfdd6cfc2a21fb4c91/

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 03 2014 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.3.13
- Update to latest upstream 1.3.13

* Mon Sep 22 2014 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.3.12
- Update to latest upstream 1.3.12

* Fri Aug 01 2014 Brent Baude <bbaude@redhat.com> - 1.3.9-6
- NVR bump for Fedora 21 build on merged koji

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Jakub Čajka <jcajka@redhat.com> 1.3.9-4
- Spec file clean up

* Fri Mar 07 2014 Karsten Hopp <karsten@redhat.com> 1.3.9-3
- fix CFLAGS

* Thu Mar 06 2014 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.3.9-2
- Disable "-Werror=format-security" gcc option

* Tue Mar 04 2014 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.3.9
- Update to latest upstream 1.3.9

* Wed Oct 09 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.3.8-3
- Add ppc64le architecture

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Vasant Hegde <hegdevasant@fedoraproject.org> - 1.3.8
- Update to latest upstream 1.3.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Jiri Skala <jskala@redhat.com> 1.3.6-1
- update to latest upstream 1.3.6

* Mon Aug 08 2011 Jiri Skala <jskala@redhat.com> 1.3.5-1
- update to latest upstream 1.3.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 11 2010 Parag Nemade <paragn AT fedoraproject.org> 2.30.3-3
- Merge-review cleanup (#226059)

* Mon Sep 21 2009 Roman Rakus <rrakus@redhat.com> - 1.3.4-1
- Upstream release 1.3.4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 David Cantrell <dcantrell@redhat.com> - 1.3.3-3
- Rebuild for gcc-4.3

* Tue Dec 18 2007 David Cantrell <dcantrell@redhat.com> - 1.3.3-2
- Spec cleanups

* Tue Dec 18 2007 David Cantrell <dcantrell@redhat.com> - 1.3.3-1
- Upgraded to librtas-1.3.3 (#253522)

* Mon Sep 10 2007 David Cantrell <dcantrell@redhat.com> - 1.3.2-1
- Upgraded to librtas-1.3.2
- Cleaned up spec file to conform to Fedora packaging guidelines

* Tue Aug 21 2007 David Cantrell <dcantrell@redhat.com> - 1.2.4-4
- Rebuild

* Sat Mar 31 2007 David Woodhouse <dwmw2@redhat.com> - 1.2.4-3
- Install libraries into /usr/lib64 on PPC64.

* Tue Aug 01 2006 Paul Nasrat <pnasrat@redhat.com> - 1.2.4-2
- Backport syscall fix from upstream 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.4-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.2.4-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.2.4-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 03 2005 Paul Nasrat <pnasrat@redhat.com> 1.2.4-1
- Update to latest version

* Thu Nov 03 2005 Paul Nasrat <pnasrat@redhat.com> 1.2.2-1
- Initial release
