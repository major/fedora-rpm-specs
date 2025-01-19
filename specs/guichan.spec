%define microversion 0.8.1

Name:           guichan
Version:        0.8.2
Release:        33%{?dist}
Summary:        Portable C++ GUI library for games using Allegro, SDL and OpenGL

License:        BSD-3-Clause
URL:            http://guichan.sourceforge.net
#Source0:        http://downloads.sourceforge.net/guichan/%{name}-%{version}.tar.gz
Source0:        http://guichan.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         guichan-0.8.1-extended-utf8-support.patch
#Patch1:         guichan-mircoversion.patch

BuildRequires:  gcc-c++
BuildRequires:  allegro-devel, SDL-devel, SDL_image-devel, libGL-devel, libtool, automake
BuildRequires: make

%description
Guichan is a small, efficient C++ GUI library designed for games. It comes
with a standard set of widgets and can use several different objects for 
displaying graphics and grabbing user input.

%package devel
Summary:        Header and libraries for guichan development
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package includes header and libraries files for development using
guichan, a small and efficient C++ GUI library designed for games. This
package is needed to build programs written using guichan.

%prep
%setup -q
%patch -P0 -p1
#%patch1 -p0


%build
autoreconf -if
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Removing Libtool archives and static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%ldconfig_scriptlets



%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/libguichan-%{microversion}.so.1
%{_libdir}/libguichan-%{microversion}.so.1.1.0
%{_libdir}/libguichan_allegro-%{microversion}.so.1
%{_libdir}/libguichan_allegro-%{microversion}.so.1.1.0
%{_libdir}/libguichan_opengl-%{microversion}.so.1
%{_libdir}/libguichan_opengl-%{microversion}.so.1.1.0
%{_libdir}/libguichan_sdl-%{microversion}.so.1
%{_libdir}/libguichan_sdl-%{microversion}.so.1.1.0

%files devel
%{_includedir}/guichan.hpp
%{_includedir}/guichan/
%{_libdir}/libguichan.so
%{_libdir}/libguichan_allegro.so
%{_libdir}/libguichan_opengl.so
%{_libdir}/libguichan_sdl.so
%{_libdir}/pkgconfig/guichan-0.8.pc
%{_libdir}/pkgconfig/guichan_opengl-0.8.pc
%{_libdir}/pkgconfig/guichan_sdl-0.8.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.2-28
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.2-11
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.2-10
- Rebuilt for GCC 5 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Jon Ciesla <limburgher@gmail.com> - 0.8.2-7
- Run autoreconf to support aarch64, BZ 925528.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Jon Ciesla <limburgher@gmail.com> - 0.8.2-3
- Revert microversion patch, BZ 804698.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 27 2011 Bruno Wolff III <bruno@wolff.to> - 0.8.2-1
- Upstream 0.8.2 http://mac.softpedia.com/progChangelog/Guichan-Changelog-47183.html
- Replace instance of incorrect hard coded micro version.
- Add pkgconfig files

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 31 2009 Wart <wart@kobold.org> 0.8.1-4
- Add patch for extended utf8 support (bz #549867)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul  28 2008 Wart <wart@kobold.org> 0.8.1-1
- Update to 0.8.1

* Fri Apr  4 2008 Wart <wart@kobold.org> 0.7.1-1
- Update to 0.7.1

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.1-3
- Autorebuild for GCC 4.3

* Tue Aug  21 2007 Wart <wart@kobold.org> 0.6.1-2
- Rebuild for gcc BUILDID

* Sat Apr  7 2007 Wart <wart@kobold.org> 0.6.1-1
- Update to 0.6.1
- Use better sf download url
- Remove BR: glut-devel as upstream no longer uses it.
- Add patch to add soname to shared libraries

* Wed Oct  4 2006 Hugo Cisneiros <hugo@devin.com.br> 0.5.0-1
- Upstream update
- Add freeglut-devel BR for the new release
- Removed unusued patches for this new version

* Wed Sep 13 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.0-3
- Rebuilt for FC6

* Sat Jun 10 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.0-2
- Using libGL-devel instead of mesa-libGL-devel in BuildRequires
- Put documentation under -devel instead of a whole -doc
- Touch "autoxxx" files to take out autoxxx commands use in devel
- Add proper location do doc files (/usr/share/doc/xxx/html)

* Fri Jun  9 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.0-1
- Initial RPM release
