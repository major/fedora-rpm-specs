%{?mingw_package_header}

%global qt_module qtactiveqt
#global pre rc

#global commit 435fac3bc7d12771a3c80556e748a2388e914cf7
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-%{qt_module}
Version:        5.15.16
Release:        1%{?dist}
Summary:        Qt5 for Windows - QtActiveQt component

# Automatically converted from old format: GPLv3 with exceptions or LGPLv2 with exceptions or BSD - review is highly recommended.
License:        LicenseRef-Callaway-GPLv3-with-exceptions OR LGPL-2.0-or-later WITH FLTK-exception OR LicenseRef-Callaway-BSD
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}

# Don't try to build stuff which requires windows.h with the native Linux gcc
Patch0:         qtactiveqt-fix-host-build.patch

# dumpcpp and MetaObjectGenerator::readClassInfo do not handle win64
# https://bugreports.qt.io/browse/QTBUG-46827
Patch1:         qtactiveqt-win64.patch

# qt_sendSpontaneousEvent is not part of libQt5Core.a?!
Patch2:         qtactiveqt-spontaneous-event.patch


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtActiveQt component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtActiveQt component

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif


%build
%mingw_qmake_qt5 ../%{qt_module}.pro
%mingw_make_build


%install
%mingw_make install INSTALL_ROOT=%{buildroot}

# .prl files aren't interesting for us
find %{buildroot} -name "*.prl" -delete


# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.GPL3-EXCEPT
%{mingw32_bindir}/dumpcpp.exe
%{mingw32_bindir}/dumpdoc.exe
%{mingw32_bindir}/idc.exe
%{mingw32_bindir}/testcon.exe
%{mingw32_includedir}/qt5/ActiveQt/
%{mingw32_libdir}/libQt5AxBase.a
%{mingw32_libdir}/libQt5AxContainer.a
%{mingw32_libdir}/libQt5AxServer.a
%{mingw32_libdir}/cmake/Qt5AxBase/
%{mingw32_libdir}/cmake/Qt5AxContainer/
%{mingw32_libdir}/cmake/Qt5AxServer/
%{mingw32_libdir}/pkgconfig/Qt5AxBase.pc
%{mingw32_libdir}/pkgconfig/Qt5AxContainer.pc
%{mingw32_libdir}/pkgconfig/Qt5AxServer.pc
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axbase.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axbase_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axcontainer.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axcontainer_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axserver.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axserver_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.GPL3-EXCEPT
%{mingw64_bindir}/dumpcpp.exe
%{mingw64_bindir}/dumpdoc.exe
%{mingw64_bindir}/idc.exe
%{mingw64_bindir}/testcon.exe
%{mingw64_includedir}/qt5/ActiveQt/
%{mingw64_libdir}/libQt5AxBase.a
%{mingw64_libdir}/libQt5AxContainer.a
%{mingw64_libdir}/libQt5AxServer.a
%{mingw64_libdir}/cmake/Qt5AxBase/
%{mingw64_libdir}/cmake/Qt5AxContainer/
%{mingw64_libdir}/cmake/Qt5AxServer/
%{mingw64_libdir}/pkgconfig/Qt5AxBase.pc
%{mingw64_libdir}/pkgconfig/Qt5AxContainer.pc
%{mingw64_libdir}/pkgconfig/Qt5AxServer.pc
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axbase.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axbase_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axcontainer.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axcontainer_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axserver.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axserver_private.pri


%changelog
* Tue Jan 21 2025 Sandro Mani <manisandro@gmail.com> - 5.15.16-1
- Update to 5.15.16

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 06 2024 Sandro Mani <manisandro@gmail.com> - 5.15.15-1
- Update to 5.15.15

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.15.14-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Sandro Mani <manisandro@gmail.com> - 5.15.14-1
- Update to 5.15.14

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 5.15.13-1
- Update to 5.15.13

* Thu Feb 15 2024 Sandro Mani <manisandro@gmail.com> - 5.15.12-1
- Update to 5.15.12

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 14 2023 Sandro Mani <manisandro@gmail.com> - 5.15.11-1
- Update to 5.15.11

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Sandro Mani <manisandro@gmail.com> - 5.15.10-1
- Update to 5.15.10

* Thu Apr 13 2023 Sandro Mani <manisandro@gmail.com> - 5.15.9-1
- Update to 5.15.9

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Sandro Mani <manisandro@gmail.com> - 5.15.8-1
- Update to 5.15.8

* Fri Nov 04 2022 Sandro Mani <manisandro@gmail.com> - 5.15.7-1
- Update to 5.15.7

* Thu Sep 22 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-1
- Update to 5.15.6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Sandro Mani <manisandro@gmail.com> - 5.15.5-1
- Update to 5.15.5

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 5.15.4-1
- Update to 5.15.4

* Mon Mar 28 2022 Sandro Mani <manisandro@gmail.com> - 5.15.3-2
- BR: mingw-gcc-c++

* Tue Mar 15 2022 Sandro Mani <manisandro@gmail.com> - 5.15.3-1
- Update to 5.15.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 16:47:54 CET 2020 Sandro Mani <manisandro@gmail.com> - 5.15.2-1
- Update to 5.15.2

* Tue Oct 06 2020 Sandro Mani <manisandro@gmail.com> - 5.15.1-1
- Update to 5.15.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-2
- Rebuild for fixed create_cmake.prf in qtbase

* Tue Apr 07 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-1
- Update to 5.14.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-1
- Update to 5.13.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Wed Sep 25 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-1
- Update to 5.12.5

* Mon Aug 26 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-3
- Rebuild to fix pkg-config files (#1745257)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-1
- Update to 5.12.4

* Wed Apr 17 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-1
- Update to 5.12.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Sandro Mani <manisandro@gmail.com> - 5.11.3-1
- Update to 5.11.3

* Sat Sep 22 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-1
- Update to 5.11.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Sandro Mani <manisandro@gmail.com> - 5.11.1-1
- Update to 5.11.1

* Wed May 30 2018 Sandro Mani <manisandro@gmail.com> - 5.11.0-1
- Update to 5.11.0

* Thu Feb 15 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-1
- Update to 5.10.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Sandro Mani <manisandro@gmail.com> - 5.10.0-1
- Update to 5.10.0

* Mon Nov 27 2017 Sandro Mani <manisandro@gmail.com> - 5.9.3-1
- Update to 5.9.3

* Tue Oct 10 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-1
- Update to 5.9.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-1
- Update to 5.9.1

* Wed Jun 28 2017 Sandro Mani <manisandro@gmail.com> - 5.9.0-1
- Update to 5.9.0

* Tue May 09 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-2
- Rebuild for dropped 0022-Allow-usage-of-static-version-with-CMake.patch in qtbase

* Thu May 04 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-1
- Update to 5.8.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Sandro Mani <manisandro@gmail.com> - 5.7.1-1
- Update to 5.7.1

* Sun Apr 10 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.6.0-1
- Update to 5.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.1-1
- Update to 5.5.1

* Fri Aug  7 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Sat Jun 27 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.2-1
- Update to 5.4.2
- Changed URL to http://qt.io/
- Use the %%license tag and use BSD license
- dumpcpp and MetaObjectGenerator::readClassInfo do not handle win64 (QTBUG-46827)

* Tue Mar 24 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.1-1
- Update to 5.4.1

* Thu Jan  1 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0

* Sun May 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Fri Jan 10 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-2
- Added license files

* Sun Jan  5 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0

* Fri Nov 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-0.1.rc1
- Update to 5.2.0 RC1

* Sun Jul 14 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0

* Fri May 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2

* Sat Feb  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Thu Jan  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0 Final

* Sun Nov 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.2.beta1.git20121111.435fac3b
- Update to 20121111 snapshot (rev 4cbcad7f)
- Rebuild against latest mingw-qt5-qtbase

* Mon Sep 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.1.beta1
- Initial release

