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
Version:        6.9.1
Release:        2%{?dist}
Summary:        Qt6 for Windows - QtMultimedia component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif
# Fix header case
Patch0:         qtmultimedia-header-case.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 107
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qtshadertools = %{version}

BuildRequires:  mingw64-filesystem >= 107
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtshadertools = %{version}


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
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
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
%{mingw32_includedir}/qt6/QtMultimediaTestLib/
%{mingw32_includedir}/qt6/QtMultimediaWidgets/
%{mingw32_includedir}/qt6/QtSpatialAudio/
%{mingw32_libdir}/cmake/Qt6/FindAVFoundation.cmake
%{mingw32_libdir}/cmake/Qt6/FindFFmpeg.cmake
%{mingw32_libdir}/cmake/Qt6/FindPipeWire.cmake
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
%{mingw32_libdir}/cmake/Qt6MultimediaPrivate/
%{mingw32_libdir}/cmake/Qt6MultimediaTestLibPrivate/
%{mingw32_libdir}/cmake/Qt6MultimediaWidgets/
%{mingw32_libdir}/cmake/Qt6MultimediaWidgetsPrivate/
%{mingw32_libdir}/cmake/Qt6SpatialAudio/
%{mingw32_libdir}/cmake/Qt6SpatialAudioPrivate/
%{mingw32_libdir}/pkgconfig/Qt6Multimedia.pc
%{mingw32_libdir}/pkgconfig/Qt6MultimediaWidgets.pc
%{mingw32_libdir}/pkgconfig/Qt6SpatialAudio.pc
%{mingw32_libdir}/libQt6BundledResonanceAudio.a
%{mingw32_libdir}/libQt6Multimedia.dll.a
%{mingw32_libdir}/libQt6MultimediaTestLib.a
%{mingw32_libdir}/libQt6MultimediaWidgets.dll.a
%{mingw32_libdir}/libQt6SpatialAudio.dll.a
%{mingw32_libdir}/Qt6MultimediaWidgets.prl
%{mingw32_libdir}/Qt6Multimedia.prl
%{mingw32_libdir}/Qt6MultimediaTestLib.prl
%{mingw32_libdir}/Qt6SpatialAudio.prl
%dir %{mingw32_libdir}/qt6/plugins/multimedia/
%{mingw32_libdir}/qt6/plugins/multimedia/windowsmediaplugin.dll
%{mingw32_libdir}/qt6/mkspecs/features/ios/add_ios_ffmpeg_libraries.prf
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimedia.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimediatestlibprivate_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio_private.pri
%{mingw32_libdir}/qt6/metatypes/qt6multimedia_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6multimediatestlibprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6multimediawidgets_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6spatialaudio_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/modules/Multimedia.json
%{mingw32_libdir}/qt6/modules/MultimediaTestLibPrivate.json
%{mingw32_libdir}/qt6/modules/MultimediaWidgets.json
%{mingw32_libdir}/qt6/modules/SpatialAudio.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx


# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Multimedia.dll
%{mingw64_bindir}/Qt6MultimediaWidgets.dll
%{mingw64_bindir}/Qt6SpatialAudio.dll
%{mingw64_includedir}/qt6/QtMultimedia/
%{mingw64_includedir}/qt6/QtMultimediaTestLib/
%{mingw64_includedir}/qt6/QtMultimediaWidgets/
%{mingw64_includedir}/qt6/QtSpatialAudio/
%{mingw64_libdir}/cmake/Qt6/FindAVFoundation.cmake
%{mingw64_libdir}/cmake/Qt6/FindFFmpeg.cmake
%{mingw64_libdir}/cmake/Qt6/FindPipeWire.cmake
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
%{mingw64_libdir}/cmake/Qt6MultimediaPrivate/
%{mingw64_libdir}/cmake/Qt6MultimediaTestLibPrivate/
%{mingw64_libdir}/cmake/Qt6MultimediaWidgets/
%{mingw64_libdir}/cmake/Qt6MultimediaWidgetsPrivate/
%{mingw64_libdir}/cmake/Qt6SpatialAudio/
%{mingw64_libdir}/cmake/Qt6SpatialAudioPrivate/
%{mingw64_libdir}/pkgconfig/Qt6Multimedia.pc
%{mingw64_libdir}/pkgconfig/Qt6MultimediaWidgets.pc
%{mingw64_libdir}/pkgconfig/Qt6SpatialAudio.pc
%{mingw64_libdir}/libQt6BundledResonanceAudio.a
%{mingw64_libdir}/libQt6Multimedia.dll.a
%{mingw64_libdir}/libQt6MultimediaTestLib.a
%{mingw64_libdir}/libQt6MultimediaWidgets.dll.a
%{mingw64_libdir}/libQt6SpatialAudio.dll.a
%{mingw64_libdir}/Qt6MultimediaWidgets.prl
%{mingw64_libdir}/Qt6Multimedia.prl
%{mingw64_libdir}/Qt6MultimediaTestLib.prl
%{mingw64_libdir}/Qt6SpatialAudio.prl
%dir %{mingw64_libdir}/qt6/plugins/multimedia/
%{mingw64_libdir}/qt6/plugins/multimedia/windowsmediaplugin.dll
%{mingw64_libdir}/qt6/mkspecs/features/ios/add_ios_ffmpeg_libraries.prf
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimedia.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimediatestlibprivate_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio_private.pri
%{mingw64_libdir}/qt6/metatypes/qt6multimedia_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6multimediatestlibprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6multimediawidgets_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6spatialaudio_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/modules/Multimedia.json
%{mingw64_libdir}/qt6/modules/MultimediaTestLibPrivate.json
%{mingw64_libdir}/qt6/modules/MultimediaWidgets.json
%{mingw64_libdir}/qt6/modules/SpatialAudio.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx


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

* Wed Oct 18 2023 Sandro Mani <manisandro@gmail.com> - 6.6.0-2
- Don't disable SIMD

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

