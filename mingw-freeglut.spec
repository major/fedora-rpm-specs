%{?mingw_package_header}

Name:           mingw-freeglut
Version:        2.8.1
Release:        22%{?dist}
Summary:        Fedora MinGW alternative to the OpenGL Utility Toolkit (GLUT)

License:        MIT

URL:            http://freeglut.sourceforge.net
Source0:        http://downloads.sourceforge.net/freeglut/freeglut-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

BuildRequires:  dos2unix


%description
freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library with an OSI approved free software
license. GLUT was originally written by Mark Kilgard to support the
sample programs in the second edition OpenGL 'RedBook'. Since then,
GLUT has been used in a wide variety of practical applications because
it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing
OpenGL contexts on a wide range of platforms and also read the mouse,
keyboard and joystick functions.

# Win32
%package -n mingw32-freeglut
Summary:        Fedora MinGW alternative to the OpenGL Utility Toolkit (GLUT)

%description -n mingw32-freeglut
freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library with an OSI approved free software
license. GLUT was originally written by Mark Kilgard to support the
sample programs in the second edition OpenGL 'RedBook'. Since then,
GLUT has been used in a wide variety of practical applications because
it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing
OpenGL contexts on a wide range of platforms and also read the mouse,
keyboard and joystick functions.

# Win64
%package -n mingw64-freeglut
Summary:        Fedora MinGW alternative to the OpenGL Utility Toolkit (GLUT)

%description -n mingw64-freeglut
freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library with an OSI approved free software
license. GLUT was originally written by Mark Kilgard to support the
sample programs in the second edition OpenGL 'RedBook'. Since then,
GLUT has been used in a wide variety of practical applications because
it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing
OpenGL contexts on a wide range of platforms and also read the mouse,
keyboard and joystick functions.


%?mingw_debug_package


%prep
%setup -q -n freeglut-%{version}

dos2unix -k FrequentlyAskedQuestions


%build
%mingw_configure --disable-static --enable-shared
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libglut.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libglut.la


%files -n mingw32-freeglut
%doc AUTHORS COPYING FrequentlyAskedQuestions NEWS README README.win32 TODO
%{mingw32_bindir}/libglut-0.dll
%{mingw32_libdir}/libglut.dll.a
%{mingw32_includedir}/GL/freeglut.h
%{mingw32_includedir}/GL/freeglut_ext.h
%{mingw32_includedir}/GL/freeglut_std.h
%{mingw32_includedir}/GL/glut.h

%files -n mingw64-freeglut
%doc AUTHORS COPYING FrequentlyAskedQuestions NEWS README README.win32 TODO
%{mingw64_bindir}/libglut-0.dll
%{mingw64_libdir}/libglut.dll.a
%{mingw64_includedir}/GL/freeglut.h
%{mingw64_includedir}/GL/freeglut_ext.h
%{mingw64_includedir}/GL/freeglut_std.h
%{mingw64_includedir}/GL/glut.h


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.8.1-17
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.0-2
- Added win64 support
- Automatically generate debuginfo subpackages

* Sun Jun 03 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0
- Dropped upstreamed patches

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.0-0.5.rc1
- Renamed the source package to mingw-freeglut (RHBZ #800866)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.0-0.4.rc1
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 14 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-0.1.rc1
- Initial RPM release.
