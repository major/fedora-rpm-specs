Summary: Disk based hash library
Name: dbh
Version: 5.0.16
Release: 23%{?dist}
URL: http://dbh.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/lib%{name}2-%{version}.tar.gz
Patch0: %{name}-5.0.13-bigendian.patch
Epoch: 1
License: GPL-3.0-or-later
BuildRequires:  gcc
BuildRequires: glib2-devel
BuildRequires: make

%description 
Disk based hashes is a method to create multidimensional binary trees on disk.
This library permits the extension of database concept to a plethora of 
electronic data, such as graphic information. With the multidimensional binary 
tree it is possible to mathematically prove that access time to any 
particular record is minimized (using the concept of critical points from 
calculus), which provides the means to construct optimized databases for 
particular applications.

%package devel
Summary: Header files for disk based hash library
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
This package includes the static libraries and header files you will need
to compile applications for dbh.

%prep
%setup -qn lib%{name}2-%{version}
%patch -P0 -p1 -b .bigendian


%build
%configure --disable-rpath --disable-static

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/usr/share/gtk-doc .
rm -rf $RPM_BUILD_ROOT/usr/share/dbh


rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*

%files devel
%doc examples/*.c examples/Makefile* doc/html gtk-doc
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
#%{_mandir}/man1/dbh*
%{_mandir}/man3/dbh*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:5.0.16-18
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 08 2014 Jon Ciesla <limburgher@gmail.com> - 1:5.0.16-1
- Update to 5.0.16, BZ 1150454.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Jon Ciesla <limburgher@gmail.com> - 1:5.0.15-1
- Update to 5.0.15, BZ 1082279.

* Wed Jan 22 2014 Dan Horák <dan[at]danny.cz> - 1:5.0.13-2
- Fix build on big endian arches

* Mon Jan 06 2014 Jon Ciesla <limburgher@gmail.com> - 1:5.0.13-1
- Update to 5.0.13, BZ 1045249.

* Fri Dec 20 2013 Jon Ciesla <limburgher@gmail.com> - 1:5.0.11-1
- Update to 5.0.11, BZ 1045249.

* Thu Oct 24 2013 Jon Ciesla <limburgher@gmail.com> - 1:5.0.8-1
- Update to 5.0.8, BZ 1021194.

* Mon Sep 30 2013 Jon Ciesla <limburgher@gmail.com> - 1:5.0.7-1
- Update to 5.0.7, BZ 1013710.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Jon Ciesla <limburgher@gmail.com> - 1:1.0.24-12
- Fixed FTBFS.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.0.24-7
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:1.0.24-6
- Autorebuild for GCC 4.3

* Tue Aug 29 2006 Kevin Fenzi <kevin@tummy.com> - 1:1.0.24-5
- Rebuild for fc6

* Thu Feb 16 2006 Kevin Fenzi <kevin@tummy.com> - 1:1.0.24-4.fc5
- Rebuild for fc5 

* Fri Dec 23 2005 Kevin Fenzi <kevin@tummy.com> - 1:1.0.24-3.fc5
- Bump release to fix tagging issue

* Thu Dec 22 2005 Kevin Fenzi <kevin@tummy.com> - 1:1.0.24-2.fc5
- Remove hard coded dist tag (fixes bug 176471)
- Remove zero length TODO and NEWS files
- Remove static libs
- Remove .la files

* Tue May 17 2005 Kevin Fenzi <kevin@tummy.com> - 1:1.0.24-1.fc4
- Update to 1.0.24

* Fri Mar 25 2005 Kevin Fenzi <kevin@tummy.com> - 1:1.0.22-3.fc4
- lowercase Release

* Sat Mar 19 2005 Warren Togami <wtogami@redhat.com> - 1:1.0.22-2
- remove stuff

* Tue Mar 15 2005 Kevin Fenzi <kevin@tummy.com> - 1:1.0.22-1
- Updated to 4.2.1 version
- Rediffed rpath patch for new version

* Tue Mar  8 2005 Kevin Fenzi <kevin@tummy.com> - 1:1.0.20-3
- Removed generic INSTALL doc

* Sun Mar  6 2005 Kevin Fenzi <kevin@tummy.com> - 1:1.0.20-2
- Changed license to LGPL

* Wed Dec 08 2004 Than Ngo <than@redhat.com> 1:1.0.20-1
- update to 1.0.20

* Tue Sep 28 2004 Than Ngo <than@redhat.com> 1:1.0.18-5
- fix file conflicts

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 13 2004 Than Ngo <than@redhat.com> 1:1.0.18-3
- get rid of rpath

* Sun Apr 18 2004 Warren Togami <wtogami@redhat.com> 1:1.0.18-2
- #121140 explicit epoch in -devel dep

* Thu Apr 15 2004 Than Ngo <than@redhat.com> 1:1.0.18-1
- update to 1.0.18

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Dec 16 2003 Than Ngo <than@redhat.com> 1.0.15-1
- initial build
