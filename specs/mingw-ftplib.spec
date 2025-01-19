%?mingw_package_header

Name:           mingw-ftplib
Version:        4.0
Release:        22%{?dist}
Summary:        MinGW Library of FTP routines

License:        Artistic-2.0
URL:            http://nbpfaus.net/~pfau/ftplib/
Source0:        http://nbpfaus.net/~pfau/ftplib/ftplib-%{version}.tar.gz
Source1:        ftplib-rc.rc
Patch0:         ftplib-3.1-1-modernize.patch
Patch1:         ftplib-4.0-mingw.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

BuildRequires:  autoconf, automake, libtool


%description
ftplib is a set of routines that implement the FTP protocol. They allow
applications to create and access remote files through function calls
instead of needing to fork and exec an interactive ftp client program.
This library is cross-compiled for MinGW.


%package -n mingw32-ftplib
Summary:        MinGW Library of FTP routines


%description -n mingw32-ftplib
ftplib is a set of routines that implement the FTP protocol. They allow
applications to create and access remote files through function calls
instead of needing to fork and exec an interactive ftp client program.
This library is cross-compiled for MinGW.


%package -n mingw64-ftplib
Summary:        MinGW Library of FTP routines


%description -n mingw64-ftplib
ftplib is a set of routines that implement the FTP protocol. They allow
applications to create and access remote files through function calls
instead of needing to fork and exec an interactive ftp client program.
This library is cross-compiled for MinGW.


%?mingw_debug_package


%prep
%setup -q -n ftplib-%{version}
%patch -P0 -p1
%patch -P1 -p1
cp -p %{SOURCE1} src/


%build
cd src/
mkdir build_win{32,64}
ln -s %{_builddir}/%{buildsubdir}/src/*.c ./build_win32/
ln -s %{_builddir}/%{buildsubdir}/src/*.h ./build_win32/
ln -s %{_builddir}/%{buildsubdir}/src/*.c ./build_win64/
ln -s %{_builddir}/%{buildsubdir}/src/*.h ./build_win64/
ln -s %{_builddir}/%{buildsubdir}/src/*.rc ./build_win32/
ln -s %{_builddir}/%{buildsubdir}/src/*.rc ./build_win64/
ln -s %{_builddir}/%{buildsubdir}/src/Makefile ./build_win32/
ln -s %{_builddir}/%{buildsubdir}/src/Makefile ./build_win64/
%{mingw32_env}
make -C build_win32 libftp.dll
%{mingw64_env}
make -C build_win64 libftp.dll


%install
mkdir -p $RPM_BUILD_ROOT/%{mingw32_bindir}
mkdir -p $RPM_BUILD_ROOT/%{mingw32_libdir}
mkdir -p $RPM_BUILD_ROOT/%{mingw32_includedir}
mkdir -p $RPM_BUILD_ROOT/%{mingw64_bindir}
mkdir -p $RPM_BUILD_ROOT/%{mingw64_libdir}
mkdir -p $RPM_BUILD_ROOT/%{mingw64_includedir}
cd src/
cp -p build_win32/libftp.dll $RPM_BUILD_ROOT/%{mingw32_bindir}
cp -p build_win32/libftp.dll.a $RPM_BUILD_ROOT/%{mingw32_libdir}
cp -p build_win32/ftplib.h $RPM_BUILD_ROOT/%{mingw32_includedir}
cp -p build_win64/libftp.dll $RPM_BUILD_ROOT/%{mingw64_bindir}
cp -p build_win64/libftp.dll.a $RPM_BUILD_ROOT/%{mingw64_libdir}
cp -p build_win64/ftplib.h $RPM_BUILD_ROOT/%{mingw64_includedir}


%files -n mingw32-ftplib
%license LICENSE
# Docs are provided by native package
%{mingw32_bindir}/libftp.dll
%{mingw32_libdir}/libftp.dll.a
%{mingw32_includedir}/ftplib.h


%files -n mingw64-ftplib
%license LICENSE
# Docs are provided by native package
%{mingw64_bindir}/libftp.dll
%{mingw64_libdir}/libftp.dll.a
%{mingw64_includedir}/ftplib.h


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0-20
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 4.0-14
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Michael Cronenworth <mike@cchtml.com> - 4.0-1
- New upstream release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 29 2013 Michael Cronenworth <mike@cchtml.com> - 3.1-8
- Modernize RPM spec
- Add 64-bit package

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1-5
- Rebuild against the mingw-w64 toolchain

* Thu Feb  9 2012 Michael Cronenworth <mike@cchtml.com> - 3.1-4
- Add COPYING file.

* Mon Jan 30 2012 Michael Cronenworth <mike@cchtml.com> - 3.1-3
- Update patch to work across arches.

* Fri Dec  2 2011 Michael Cronenworth <mike@cchtml.com> - 3.1-2
- Updated to new packaging policy.

* Wed Nov 23 2011 Michael Cronenworth <mike@cchtml.com> - 3.1-1
- Initial RPM release.

