Summary: Control operation of a CD-ROM when playing audio CDs
Name: libcdaudio
Version: 0.99.12p2
Release: 44%{?dist}
# COPYING is a copy of GPLv2, but the code and the README clearly indicate
# that the code is LGPLv2+. Probably want to let upstream know about COPYING.
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: http://libcdaudio.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/libcdaudio/%{name}-%{version}.tar.gz
Patch0: libcdaudio-0.99.12-buffovfl.patch
Patch1: libcdaudio-0.99.12p2-libdir.patch
Patch2: libcdaudio-0.99-CAN-2005-0706.patch
Patch3: libcdaudio-0.99.12-segfault.patch
Patch4: libcdaudio-0.99.12p2-c99.patch
BuildRequires: gcc-c++
BuildRequires: make

%description
libcdaudio is a library designed to provide functions to control
operation of a CD-ROM when playing audio CDs.  It also contains
functions for CDDB and CD Index lookup.

%package devel
Summary: Development files for libcdaudio
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains development files for linking against libcdaudio.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p0
%patch -P4 -p1

%build
%configure \
  --enable-dependency-tracking \
  --disable-static \
  --enable-threads
make

%install
make install DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%doc README NEWS
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%exclude %{_libdir}/*.la
%{_bindir}/%{name}-config
%{_datadir}/aclocal/%{name}.m4
%{_libdir}/pkgconfig/libcdaudio.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.99.12p2-43
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Peter Fordham <peter.fordham@gmail.com> - 0.99.12p2-37
- Port configure script to C99.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 07 2016 Sérgio Basto <sergio@serjux.com> - 0.99.12p2-23
- Add license tag.
- Add patch libcdaudio-0.99.12-segfault.patch, from
  https://sourceforge.net/p/libcdaudio/patches/5/
- Spec clean-up.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.12p2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12p2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 27 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.99.12p2-11
- Fix CVE-2005-0706.

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.99.12p2-10
- took COPYING out of doc (it is simply wrong)
- fixed license tag

* Fri Dec 29 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.99.12p2-8
- Change Group tag.
- Fix libcdaudio-config for libdir != %%{_prefix}/lib.

* Wed Dec 27 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.99.12p2-7
- Update to 0.99.12p2.

* Tue Sep 13 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Patch to fix buffer overflow by Brian C. Huffman
  <huffman@graze.net>.

* Sat Jul 23 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.99.12.

* Wed May 14 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.


