%{?mingw_package_header}

%global qt_module qtimageformats
#global pre rc2

#global commit a0ec617b21d9ce0c562e8e7c0dc59bc4d08c509b
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.9.1
Release:        2%{?dist}
Summary:        Qt6 for Windows - QtImageFormats component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

# Fix build: search for Threads ourself instead of promoting imported target
Patch0:         qtimageformats-fix-build.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-jasper
BuildRequires:  mingw32-libmng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-qt6-qtbase = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-jasper
BuildRequires:  mingw64-libmng
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-qt6-qtbase = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtImageFormats component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtImageFormats component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}

%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja


%install
%mingw_ninja_install


# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_libdir}/qt6/plugins/imageformats/qicns.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qjp2.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qmng.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qtga.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qtiff.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qwbmp.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qwebp.dll
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx
%{mingw32_libdir}/cmake/Qt6/FindLibmng.cmake
%{mingw32_libdir}/cmake/Qt6/FindWrapJasper.cmake
%{mingw32_libdir}/cmake/Qt6/FindWrapWebP.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QICNSPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QJp2Plugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QMngPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QTgaPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QTiffPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QWbmpPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QWebpPlugin*.cmake


# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_libdir}/qt6/plugins/imageformats/qicns.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qjp2.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qmng.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qtga.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qtiff.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qwbmp.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qwebp.dll
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx
%{mingw64_libdir}/cmake/Qt6/FindLibmng.cmake
%{mingw64_libdir}/cmake/Qt6/FindWrapJasper.cmake
%{mingw64_libdir}/cmake/Qt6/FindWrapWebP.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QICNSPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QJp2Plugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QMngPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QTgaPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QTiffPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QWbmpPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QWebpPlugin*.cmake


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 09 2025 Sandro Mani <manisandro@gmail.com> - 6.9.1-1
- Update to 6.9.1

* Fri Apr 04 2025 Sandro Mani <manisandro@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Tue Feb 04 2025 Sandro Mani <manisandro@gmail.com> - 6.8.2-1
- Update to 6.8.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 07 2024 Sandro Mani <manisandro@gmail.com> - 6.8.1-1
- Update to 6.8.1

* Sat Oct 19 2024 Sandro Mani <manisandro@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Sandro Mani <manisandro@gmail.com> - 6.7.2-1
- Update to 6.7.2

* Sun May 26 2024 Sandro Mani <manisandro@gmail.com> - 6.7.1-1
- Update to 6.7.1

* Mon Apr 08 2024 Sandro Mani <manisandro@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Sun Feb 18 2024 Sandro Mani <manisandro@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 03 2023 Sandro Mani <manisandro@gmail.com> - 6.6.1-1
- Update to 6.6.1

* Fri Dec 01 2023 Sandro Mani <manisandro@gmail.com> - 6.6.0-2
- Rebuild (jasper)

* Wed Oct 18 2023 Sandro Mani <manisandro@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Wed Oct 04 2023 Sandro Mani <manisandro@gmail.com> - 6.5.3-1
- Update to 6.5.3

* Sun Jul 30 2023 Sandro Mani <manisandro@gmail.com> - 6.5.2-1
- Update to 6.5.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Sandro Mani <manisandro@gmail.com> - 6.5.1-1
- Update to 6.5.1

* Fri Apr 07 2023 Sandro Mani <manisandro@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Wed Mar 29 2023 Sandro Mani <manisandro@gmail.com> - 6.4.3-1
- Update to 6.4.3

* Tue Mar 28 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Sat Nov 26 2022 Sandro Mani <manisandro@gmail.com> - 6.4.1-1
- Update to 6.4.1

* Fri Nov 04 2022 Sandro Mani <manisandro@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Mon Jul 04 2022 Sandro Mani <manisandro@gmail.com> - 6.3.0-2
- Rebuild (jasper)

* Fri Apr 29 2022 Sandro Mani <manisandro@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-3
- Rebuild with mingw-gcc-12

* Sun Mar 06 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-2
- Re-enable s390x build

* Tue Feb 08 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Mon Nov 01 2021 Sandro Mani <manisandro@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-3
- Update to 6.2.0

* Mon Sep 27 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-2.rc2
- Update to 6.2.0-rc2

* Wed Sep 22 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1.rc
- Update to 6.2.0-rc

* Sat Aug 14 2021 Sandro Mani <manisandro@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Thu Jul 08 2021 Sandro Mani <manisandro@gmail.com> - 6.1.1-1
- Initial package
