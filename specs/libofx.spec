Summary: A library for supporting Open Financial Exchange (OFX)
Name: libofx
Version: 0.10.9
Release: 7%{?dist}
URL: https://github.com/libofx/libofx
License: GPL-2.0-or-later
Source: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: fix-ftbfs-gcc4.7.diff
BuildRequires: gcc-c++
BuildRequires: opensp-devel
BuildRequires: curl-devel
BuildRequires: libxml++-devel
BuildRequires: make
BuildRequires: cmake

%description
This is the LibOFX library.  It is a API designed to allow applications to
very easily support OFX command responses, usually provided by financial
institutions.  See http://www.ofx.net/ofx/default.asp for details and
specification. 

%package -n ofx
Summary: Tools for manipulating OFX data
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n ofx
The ofx package contains tools for manipulating OFX data from the
command line; they are often used when testing libofx.

%package devel
Summary: Development files needed for accessing OFX data
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The libofx-devel contains the header files and libraries necessary
for building applications that use libofx.

%prep
%setup -q
%patch -P0 -p1 -b .gcc47

chmod 644 ./doc/ofx_sample_files/*

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build

%install
%cmake_install

rm -rf $RPM_BUILD_ROOT%{_libdir}/lib*.la $RPM_BUILD_ROOT%{_datadir}/doc

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING ChangeLog NEWS README totest.txt
%{_libdir}/libofx.so.7*
%{_datadir}/libofx/

%files -n ofx
%{_bindir}/ofx*

%files devel
%doc doc/ofx_sample_files
%{_includedir}/libofx/
%{_libdir}/pkgconfig/libofx.pc
%{_libdir}/libofx.so
%{_libdir}/cmake/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.10.9-2
- migrated to SPDX license

* Mon Feb 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.10.9-1
- 0.10.9

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.10.8-1
- 0.10.8

* Mon Sep 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.10.8-1
- Patches from BZ 2127755.

* Fri Sep 09 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.10.7-1
- 0.10.7

* Tue Sep 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.10.6-1
- 0.10.6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.10.4-1
- 0.10.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.10.3-1
- 0.10.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 0.9.13-7
- Do not force C++11 mode

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Bill Nottingham <notting@splat.cc> - 0.9.13-1
- update to 0.9.13 (#1657007)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Bill Nottingham <notting@splat.cc> - 0.9.12-1
- update to 0.9.12 (#1492203)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 07 2016 Bill Nottingham <notting@splat.cc> - 0.9.10-1
- update to 0.9.10

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.9-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.9.9-2
- Don't ship editor backup files

* Mon Sep 23 2013 Bill Nottingham <notting@redhat.com> - 0.9.9-1
- update to 0.9.9

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.9.5-2
- enumerate %%files a bit, so abi bumps aren't a surprise
- tighten subpkg deps via %%_isa
- -devel: drop Requires: opensp-devel

* Mon Jul 09 2012 Bill Nottingham <notting@redhat.com> - 0.9.5-1
- update to 0.9.5 (#838473)

* Sat Apr 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.4-4
- Add patch to fix FTBFS on gcc 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Apr 19 2011 Bill Nottingham <notting@redhat.com> - 0.9.4-1
- update to 0.9.4

* Mon Feb 14 2011 Bill Nottingham <notting@redhat.com> - 0.9.2-1
- update to 0.9.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Bill Nottingham <notting@redhat.com> - 0.9.1-1
- update to 0.9.1
- remove xml++ support - we've never built it

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep  9 2008 Bill Nottingham <notting@redhat.com> - 0.9.0-1
- update to 0.9.0

* Thu Feb 14 2008 Bill Nottingham <notting@redhat.com> - 0.8.3-5
- fix build with gcc-4.3
- add patch for other account types (#415961)

* Wed Oct 10 2007 Bill Nottingham <notting@redhat.com> - 0.8.3-4
- rebuild for buildid

* Fri Aug  3 2007 Bill Nottingham <notting@redhat.com>
- tweak license tag

* Tue Jan  9 2007 Bill Nottingham <notting@redhat.com> - 0.8.3-3
- update to 0.8.3
- add in (not used) xml++ support pending upstream
- add opensp-devel buildreq, remove INSTALL
- split off binaries into ofx package

* Mon Jan  8 2007 Bill Nottingham <notting@redhat.com> - 0.8.2-3
- spec tweaks

* Mon Aug 28 2006 Bill Nottingham <notting@redhat.com> - 0.8.2-1
- update to 0.8.2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.8.0-3.1
- rebuild

* Tue Jul 11 2006 Bill Nottingham <notting@redhat.com> - 0.8.0-3
- own %%{_datadir}/libofx (#169336)

* Mon May 15 2006 Brian Pepple <bdpepple@ameritech.net> - 0.8.0-2.3
- Add BR for curl-devel.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.8.0-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.8.0-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan  6 2006 Nalin Dahyabhai <nalin@redhat.com> 0.8.0-2
- rebuild

* Tue Dec 20 2005 Bill Nottingham <notting@redhat.com> 0.8.0-1
- update to 0.8.0

* Tue Dec 13 2005 Tim Waugh <twaugh@redhat.com> 0.7.0-4
- Build requires: openjade-devel -> opensp-devel.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon May 23 2005 Bill Nottingham <notting@redhat.com> 0.7.0-3
- remove static libs

* Tue Mar  8 2005 Bill Nottingham <notting@redhat.com> 0.7.0-2
- fix build with gcc4

* Wed Feb  9 2005 Bill Nottingham <notting@redhat.com> 0.7.0-1
- update to 0.7.0

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com> 0.6.6-2
- rebuilt
- Add gcc 3.4 patch

* Fri Mar 12 2004 Bill Nottingham <notting@redhat.com> 0.6.6-1
- split off from gnucash, adapt upstream spec, add -devel package
