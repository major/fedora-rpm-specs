Summary: A Differential X Protocol Compressor
Name:    dxpc
Version: 3.9.2
Release: 29%{?dist}

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     http://www.vigor.nu/%{name}/
Source:  http://www.vigor.nu/%{name}/%{name}-%{version}.tgz
Patch0: dxpc-3.9.0-mandir.patch
Patch1: dxpc-3.9.0-dxpcssh.patch
Patch2: dxpc-3.9.1b1-destdir.patch

BuildRequires:  gcc-c++
BuildRequires: lzo-devel >= 1.08
%if 0%{?fedora} > 4
BuildRequires: libXt-devel
%else
BuildRequires: xorg-x11-devel
%endif
BuildRequires: make

%description
dxpc is an X protocol compressor designed to improve the
speed of X11 applications run over low-bandwidth links
(such as dialup PPP connections or ADSL).


%prep
%setup -q

%patch -P0 -p1 -b .mandir
%patch -P1 -p0 -b .dxpcssh
%patch -P2 -p0 -b .destdir


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install



%files
%doc README CHANGES TODO
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.9.2-28
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.9.2-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 01 2012 Adam Jackson <ajax@redhat.com> 3.9.2-1
- dxpc 3.9.2

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 10 2008 John Guthrie <guthrie@counterexample.org> - 3.9.1-1
- Added %%dist tag back to the release tag that had been inadvertently deleted
  by the previous update.

* Tue Sep 09 2008 John Guthrie <guthrie@counterexample.org> - 3.9.1-1
- Upgraded source code to 3.9.1-1

* Mon Jul 07 2008 Adam Jackson <ajax@redhat.com> 3.9.1-0.3.b1.1
- Fix %%fedora string comparison to be integer comparison.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.9.1-0.3.b1
- Autorebuild for GCC 4.3

* Sun Feb 04 2007 John Guthrie <guthrie[AT]counterexample.org> - 3.9.1-0.2.b1
- Patched Makefile.in so that we can use the DESTDIR variable

* Fri Feb 02 2007 John Guthrie <guthrie[AT]counterexample.org> - 3.9.1-0.1.b1
- Upgraded source code to 3.9.1-0.1.b1

* Mon Jan 29 2007 John Guthrie <guthrie[AT]counterexample.org> - 3.9.0-3
- Removed test for %%{buildroot}
- Cleaned up warnings from rpmlint
- Removed README.mingw from the documentation as it had no relevance to
  Linux

* Mon Jan 22 2007 John Guthrie <guthrie[AT]counterexample.org> - 3.9.0-3
- Added patch to Makefile.in to make it install dxpcssh

* Mon Jan 22 2007 John Guthrie <guthrie[AT]counterexample.org> - 3.9.0-2
- Updated to 3.9.0
- Added mandir patch that was used in 3.8.2
- Changed $RPM_BUILD_ROOT to %%{buildroot} in scriptlets for consistency

* Wed Mar 1 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- fc5: gcc/glibc respin

* Mon Jan 30 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.8.2-3
- drop BR: XFree86-devel (#179283)
- add BR: xorg-x11-devel/libXt-devel (#179283)

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Jul 11 2003 Rex Dieter <rexdieter at sf.net> 0:3.8.2-0.fdr.1
- BuildRequires: XFree86-devel (fedora bug #381)

* Tue Jun 17 2003 Rex Dieter <rexdieter at sf.net> 0:3.8.2-0.fdr.0
- 3.8.2
