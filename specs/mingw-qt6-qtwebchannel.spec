%{?mingw_package_header}

%global qt_module qtwebchannel
#global pre rc2

#global commit e5133f4f0bb7c01d7bd7fc499d8c148c03a5b500
#global shortcommit %%(c=%%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.8.1
Release:        2%{?dist}
Summary:        Qt6 for Windows - QtWebChannel component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qtdeclarative = %{version}
BuildRequires:  mingw32-qt6-qtwebsockets = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtdeclarative = %{version}
BuildRequires:  mingw64-qt6-qtwebsockets = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtWebchannel component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtWebchannel component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
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
%{mingw32_bindir}/Qt6WebChannel.dll
%{mingw32_bindir}/Qt6WebChannelQuick.dll
%{mingw32_includedir}/qt6/QtWebChannel/
%{mingw32_includedir}/qt6/QtWebChannelQuick/
%{mingw32_libdir}/qt6/metatypes/qt6webchannel_relwithdebinfo_metatypes.json
%{mingw32_libdir}/cmake/Qt6WebChannel/
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebChannelTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6WebChannelQuick*
%{mingw32_libdir}/cmake/Qt6WebChannelQuick/
%{mingw32_libdir}/pkgconfig/Qt6WebChannel.pc
%{mingw32_libdir}/pkgconfig/Qt6WebChannelQuick.pc
%{mingw32_libdir}/libQt6WebChannel.dll.a
%{mingw32_libdir}/libQt6WebChannelQuick.dll.a
%{mingw32_libdir}/qt6/metatypes/qt6webchannelquick_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_webchannel.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_webchannel_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_webchannelquick.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_webchannelquick_private.pri
%{mingw32_libdir}/qt6/qml/QtWebChannel/
%{mingw32_libdir}/Qt6WebChannel.prl
%{mingw32_libdir}/Qt6WebChannelQuick.prl
%{mingw32_libdir}/qt6/modules/WebChannel.json
%{mingw32_libdir}/qt6/modules/WebChannelQuick.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6WebChannel.dll
%{mingw64_bindir}/Qt6WebChannelQuick.dll
%{mingw64_includedir}/qt6/QtWebChannel/
%{mingw64_includedir}/qt6/QtWebChannelQuick/
%{mingw64_libdir}/qt6/metatypes/qt6webchannel_relwithdebinfo_metatypes.json
%{mingw64_libdir}/cmake/Qt6WebChannel/
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebChannelTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6WebChannelQuick*
%{mingw64_libdir}/cmake/Qt6WebChannelQuick/
%{mingw64_libdir}/pkgconfig/Qt6WebChannel.pc
%{mingw64_libdir}/pkgconfig/Qt6WebChannelQuick.pc
%{mingw64_libdir}/libQt6WebChannel.dll.a
%{mingw64_libdir}/libQt6WebChannelQuick.dll.a
%{mingw64_libdir}/qt6/metatypes/qt6webchannelquick_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_webchannel.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_webchannel_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_webchannelquick.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_webchannelquick_private.pri
%{mingw64_libdir}/qt6/qml/QtWebChannel/
%{mingw64_libdir}/Qt6WebChannel.prl
%{mingw64_libdir}/Qt6WebChannelQuick.prl
%{mingw64_libdir}/qt6/modules/WebChannel.json
%{mingw64_libdir}/qt6/modules/WebChannelQuick.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 07 2024 Sandro Mani <manisandro@gmail.com> - 6.8.1-1
- Update to 6.8.1

* Wed Oct 23 2024 Sandro Mani <manisandro@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Sandro Mani <manisandro@gmail.com> - 6.7.2-1
- Update to 6.7.2

* Sun May 26 2024 Sandro Mani <manisandro@gmail.com> - 6.7.1-1
- Update to 6.7.1

* Tue Apr 09 2024 Sandro Mani <manisandro@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Sun Feb 18 2024 Sandro Mani <manisandro@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 03 2023 Sandro Mani <manisandro@gmail.com> - 6.6.1-1
- Update to 6.6.1

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

* Thu Jan 19 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Sat Nov 26 2022 Sandro Mani <manisandro@gmail.com> - 6.4.1-1
- Update to 6.4.1

* Fri Nov 04 2022 Sandro Mani <manisandro@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Fri Oct 21 2022 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Thu Mar 31 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Wed Sep 29 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.rc2
- Initial package
