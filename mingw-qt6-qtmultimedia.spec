%{?mingw_package_header}

%global qt_module qtmultimedia
#global pre rc2

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.4.2
Release:        1%{?dist}
Summary:        Qt6 for Windows - QtMultimedia component

License:        LGPL-3.0-only OR GPL-2.0-only
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

# Disable SIMD on mingw
Patch0:         qtmultimedia-simd.patch
# Fix WMF detection on mingw
Patch1:         qtmultimedia-wmf.patch
# Fix gstreamer plugin symbols not exported
Patch2:         qtmultimedia-dllexport.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 107
BuildRequires:  mingw32-angleproject
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gstreamer1
BuildRequires:  mingw32-gstreamer1-plugins-base
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qtshadertools = %{version}
BuildRequires:  mingw32-openal-soft

BuildRequires:  mingw64-filesystem >= 107
BuildRequires:  mingw64-angleproject
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gstreamer1
BuildRequires:  mingw64-gstreamer1-plugins-base
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtshadertools = %{version}
BuildRequires:  mingw64-openal-soft


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtMultimedia component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtMultimedia component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}


%build
%mingw_cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja


%install
%mingw_ninja_install


# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6Multimedia.dll
%{mingw32_bindir}/Qt6MultimediaWidgets.dll
%{mingw32_bindir}/Qt6SpatialAudio.dll
%{mingw32_includedir}/qt6/QtMultimedia/
%{mingw32_includedir}/qt6/QtMultimediaWidgets/
%{mingw32_includedir}/qt6/QtSpatialAudio/
%{mingw32_libdir}/cmake/Qt6/FindAVFoundation.cmake
%{mingw32_libdir}/cmake/Qt6/FindFFmpeg.cmake
%{mingw32_libdir}/cmake/Qt6/FindGObject.cmake
%{mingw32_libdir}/cmake/Qt6/FindGStreamer.cmake
%{mingw32_libdir}/cmake/Qt6/FindMMRendererCore.cmake
%{mingw32_libdir}/cmake/Qt6/FindVAAPI.cmake
%{mingw32_libdir}/cmake/Qt6/FindWrapBundledResonanceAudioConfigExtra.cmake
%{mingw32_libdir}/cmake/Qt6/FindWrapPulseAudio.cmake
%{mingw32_libdir}/cmake/Qt6/FindWMF.cmake
%{mingw32_libdir}/cmake/Qt6/FindMMRenderer.cmake
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtMultimediaTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6BundledResonanceAudio/
%{mingw32_libdir}/cmake/Qt6Multimedia/
%{mingw32_libdir}/cmake/Qt6MultimediaWidgets/
%{mingw32_libdir}/cmake/Qt6SpatialAudio/
%{mingw32_libdir}/pkgconfig/Qt6Multimedia.pc
%{mingw32_libdir}/pkgconfig/Qt6MultimediaWidgets.pc
%{mingw32_libdir}/pkgconfig/Qt6SpatialAudio.pc
%{mingw32_libdir}/libQt6BundledResonanceAudio.a
%{mingw32_libdir}/libQt6Multimedia.dll.a
%{mingw32_libdir}/libQt6MultimediaWidgets.dll.a
%{mingw32_libdir}/libQt6SpatialAudio.dll.a
%{mingw32_libdir}/Qt6MultimediaWidgets.prl
%{mingw32_libdir}/Qt6Multimedia.prl
%{mingw32_libdir}/Qt6SpatialAudio.prl
%dir %{mingw32_libdir}/qt6/plugins/multimedia/
%{mingw32_libdir}/qt6/plugins/multimedia/gstreamermediaplugin.dll
%{mingw32_libdir}/qt6/plugins/multimedia/windowsmediaplugin.dll
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimedia.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio_private.pri
%{mingw32_libdir}/metatypes/qt6multimedia_relwithdebinfo_metatypes.json
%{mingw32_libdir}/metatypes/qt6multimediawidgets_relwithdebinfo_metatypes.json
%{mingw32_libdir}/metatypes/qt6spatialaudio_relwithdebinfo_metatypes.json
%{mingw32_datadir}/qt6/modules/Multimedia.json
%{mingw32_datadir}/qt6/modules/MultimediaWidgets.json
%{mingw32_datadir}/qt6/modules/SpatialAudio.json


# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Multimedia.dll
%{mingw64_bindir}/Qt6MultimediaWidgets.dll
%{mingw64_bindir}/Qt6SpatialAudio.dll
%{mingw64_includedir}/qt6/QtMultimedia/
%{mingw64_includedir}/qt6/QtMultimediaWidgets/
%{mingw64_includedir}/qt6/QtSpatialAudio/
%{mingw64_libdir}/cmake/Qt6/FindAVFoundation.cmake
%{mingw64_libdir}/cmake/Qt6/FindFFmpeg.cmake
%{mingw64_libdir}/cmake/Qt6/FindGObject.cmake
%{mingw64_libdir}/cmake/Qt6/FindGStreamer.cmake
%{mingw64_libdir}/cmake/Qt6/FindMMRendererCore.cmake
%{mingw64_libdir}/cmake/Qt6/FindVAAPI.cmake
%{mingw64_libdir}/cmake/Qt6/FindWrapBundledResonanceAudioConfigExtra.cmake
%{mingw64_libdir}/cmake/Qt6/FindWrapPulseAudio.cmake
%{mingw64_libdir}/cmake/Qt6/FindWMF.cmake
%{mingw64_libdir}/cmake/Qt6/FindMMRenderer.cmake
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtMultimediaTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6BundledResonanceAudio/
%{mingw64_libdir}/cmake/Qt6Multimedia/
%{mingw64_libdir}/cmake/Qt6MultimediaWidgets/
%{mingw64_libdir}/cmake/Qt6SpatialAudio/
%{mingw64_libdir}/pkgconfig/Qt6Multimedia.pc
%{mingw64_libdir}/pkgconfig/Qt6MultimediaWidgets.pc
%{mingw64_libdir}/pkgconfig/Qt6SpatialAudio.pc
%{mingw64_libdir}/libQt6BundledResonanceAudio.a
%{mingw64_libdir}/libQt6Multimedia.dll.a
%{mingw64_libdir}/libQt6MultimediaWidgets.dll.a
%{mingw64_libdir}/libQt6SpatialAudio.dll.a
%{mingw64_libdir}/Qt6MultimediaWidgets.prl
%{mingw64_libdir}/Qt6Multimedia.prl
%{mingw64_libdir}/Qt6SpatialAudio.prl
%dir %{mingw64_libdir}/qt6/plugins/multimedia/
%{mingw64_libdir}/qt6/plugins/multimedia/gstreamermediaplugin.dll
%{mingw64_libdir}/qt6/plugins/multimedia/windowsmediaplugin.dll
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimedia.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio_private.pri
%{mingw64_libdir}/metatypes/qt6multimedia_relwithdebinfo_metatypes.json
%{mingw64_libdir}/metatypes/qt6multimediawidgets_relwithdebinfo_metatypes.json
%{mingw64_libdir}/metatypes/qt6spatialaudio_relwithdebinfo_metatypes.json
%{mingw64_datadir}/qt6/modules/Multimedia.json
%{mingw64_datadir}/qt6/modules/MultimediaWidgets.json
%{mingw64_datadir}/qt6/modules/SpatialAudio.json


%changelog
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

* Fri Apr 29 2022 Sandro Mani <manisandro@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-4
- Rebuild with mingw-gcc-12

* Sun Mar 06 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-3
- Re-enable s390x build

* Wed Mar 02 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-2
- Enable gstreamer backend

* Tue Feb 08 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Sandro Mani <manisandro@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Wed Sep 29 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.rc2
- Update to 6.2.0-rc2

* Fri Sep 24 2021 Sandro Mani <manisandro@gmail.coM> - 6.2.0-0.1.rc
- Initial package

