Summary:      Miniature XML development library
Name:         mxml
Version:      3.3.1
Release:      7%{?dist}
License:      ASL 2.0 with exception
URL:          http://www.msweet.org/blog.php?L+Z3
Source0:      https://github.com/michaelrsweet/mxml/archive/v%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc

%description
Mini-XML is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
non-standard libraries.

%package devel
Summary:  Libraries, includes, etc to develop mxml applications
Requires: mxml = %{version}-%{release}
Requires: pkgconfig

%description devel
Libraries, include files, etc you can use to develop mxml
applications.

%prep
%setup -q

%build
# Run autoconf since we patched configure.in.
%configure --enable-shared
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make BUILDROOT=%{buildroot} install

# Configuring with --disable-static doesn't work, so let's just delete
# the .a file by hand.
rm %{buildroot}%{_libdir}/libmxml.a

# remove extra docs
rm -rf %{buildroot}%{_datadir}/doc/mxml/

# remove rendered man pages
rm -f %{buildroot}%{_datadir}/man/cat*/*

%files
%license LICENSE
%doc README.md
%{_libdir}/libmxml.so.1*

%files devel
%doc CHANGES.md doc/*.html doc/*.png
%{_includedir}/*.h
%{_libdir}/libmxml.so
%{_mandir}/*/*
%{_libdir}/pkgconfig/mxml.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Kevin Fenzi <kevin@scrye.com> - 3.3.1-1
- Update to 3.3.1. Fixes rhbz#2110721

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 07 2021 Kevin Fenzi <kevin@scrye.com> - 3.3-1
- Update to 3.3. Fixes rhbz#2020915

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Kevin Fenzi <kevin@scrye.com> - 3.2-3
- Update to 3.2. Fixes bug #1886993

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Kevin Fenzi <kevin@scrye.com> - 3.1-1
- Update to 3.1. Fixes bug #1747106

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Kevin Fenzi <kevin@scrye.com> - 3.0-1
- Upgrade to 3.0. Fixes bug #1684794
- CVE-2018-20004 CVE-2018-20592 CVE-2018-20593

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 2.11-4
- Fix FTBFS bug #1604905.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Kevin Fenzi <kevin@scrye.com> - 2.11-1
- Update to 2.11. Fixes bug #1459753

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 11 2016 Kevin Fenzi <kevin@scrye.com> - 2.9-1
- Update to 2.9
- Add patch from debian to fix CVE-2016-4570 and CVE-2016-4571. Bug #1334648 and #1334649
- Fix rpath usage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 06 2014 Brendan Jones <brendan.jones.it@gmail.com> 2.8-1
- Update to 2.8

* Tue Dec 03 2013 Brendan Jones <brendan.jones.it@gmail.com> 2.6-1
- Update to 2.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 28 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.5-5
- Fix typo in the .pc file (RHBZ#503628). Patch by Robert Szalai

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.5-2
- fix license tag

* Tue Jul 08 2008 Anthony Green <green@redhat.com> 2.5
- Upgrade source.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.2-8
- Autorebuild for GCC 4.3

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.2.2-7
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 2.2.2-6
- Fix release tag.

* Mon Sep 18 2006 Anthony Green <green@redhat.com> 2.2.2-5.1
- Rebuild.

* Mon Sep  4 2006 Anthony Green <green@redhat.com> 2.2.2-5
- devel package must Require pkgconfig.

* Wed Jul 19 2006 Anthony Green <green@redhat.com> 2.2.2-4
- Fix /usr/share references.

* Sat Jul 15 2006 Anthony Green <green@redhat.com> 2.2.2-3
- Fix /usr/lib reference when deleting libmxml.a.

* Sat Jul 15 2006 Anthony Green <green@redhat.com> 2.2.2-2
- Fix License (LGPL, not GPL).
- Move programming documentation to devel package.
- Build shared library, and no static library.
- Add %%post(un).
- Remove rpath with mxml-no-rpath.patch.
- First Fedora Extras build.

* Fri Sep 23 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.2-1
- updated to 2.2.2 (zynaddsubfx needs 2.2 at least)
* Mon Dec 27 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file cleanup
* Wed Aug  4 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.0-1
- initial build.


