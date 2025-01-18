Name:           compat-guichan05
Version:        0.5.0
Release:        42%{?dist}
Summary:        Compatibility libraries for older guichan versions

License:        BSD-3-Clause
URL:            http://guichan.sourceforge.net
Source0:        http://downloads.sourceforge.net/guichan/guichan-%{version}-src.tar.gz
Patch0:         compat-guichan05-configure-c99.patch
Obsoletes:      guichan < 0.6.0

BuildRequires:  allegro-devel, SDL-devel, SDL_image-devel, libGL-devel
BuildRequires:  freeglut-devel, gcc-c++
BuildRequires: make

%description
Guichan is a small, efficient C++ GUI library designed for games. It comes
with a standard set of widgets and can use several different objects for 
displaying graphics and grabbing user input.

This package contains compatibility libraries for guichan 0.5

%package devel
Summary:        Header and libraries for guichan development
Requires:       %{name} = %{version}-%{release}

%description devel
This package includes header and libraries files for development using
guichan, a small and efficient C++ GUI library designed for games. This
package is needed to build programs written using guichan.

%prep
%autosetup -p1 -n guichan-%{version}-src

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Removing Libtool and static archives
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# Move some things around for the compat package
mkdir -p $RPM_BUILD_ROOT%{_includedir}/guichan-0.5
mv $RPM_BUILD_ROOT%{_includedir}/guichan $RPM_BUILD_ROOT%{_includedir}/guichan-0.5
mv $RPM_BUILD_ROOT%{_includedir}/guichan.hpp $RPM_BUILD_ROOT%{_includedir}/guichan-0.5

mkdir -p $RPM_BUILD_ROOT%{_libdir}/guichan-0.5
for lib in libguichan libguichan_allegro libguichan_glut libguichan_opengl libguichan_sdl ; do
    rm -f $RPM_BUILD_ROOT%{_libdir}/${lib}.so
    ln -s ../${lib}.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/guichan-0.5/${lib}.so
done


%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/libguichan.so.*
%{_libdir}/libguichan_allegro.so.*
%{_libdir}/libguichan_glut.so.*
%{_libdir}/libguichan_opengl.so.*
%{_libdir}/libguichan_sdl.so.*

%files devel
%doc docs/html
%{_includedir}/guichan-0.5
%dir %{_libdir}/guichan-0.5
%{_libdir}/guichan-0.5/libguichan.so
%{_libdir}/guichan-0.5/libguichan_allegro.so
%{_libdir}/guichan-0.5/libguichan_glut.so
%{_libdir}/guichan-0.5/libguichan_opengl.so
%{_libdir}/guichan-0.5/libguichan_sdl.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.5.0-37
- migrated to SPDX license

* Thu Feb 02 2023 Florian Weimer <fweimer@redhat.com> - 0.5.0-36
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.5.0-26
- BR fix.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.0-18
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 Wart <wart@kobold.org> 0.5.0-8
- Rebuild for gcc 4.3

* Tue Aug 21 2007 Wart <wart@kobold.org> 0.5.0-7
- Rebuild for gcc BUILDID

* Tue Apr 10 2007 Wart <wart@kobold.org> 0.5.0-6
- Fix Obsoletes: version to avoid matching some guichan 0.5.0 releases

* Mon Apr 9 2007 Wart <wart@kobold.org> 0.5.0-5
- Remove Provides: that was added by mistake

* Mon Apr 9 2007 Wart <wart@kobold.org> 0.5.0-4
- Add missing Provides: for the package that this obsoletes

* Sat Apr 7 2007 Wart <wart@kobold.org> 0.5.0-3
- Remove .soname from shared libs for this initial compat package
  to avoid breaking compatibility with existing packages that
  may be linked against guichan0.5.

* Sun Mar 18 2007 Wart <wart@kobold.org> 0.5.0-2
- initial compat package

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
