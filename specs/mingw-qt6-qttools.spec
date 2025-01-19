%{?mingw_package_header}

# Disable debugsource packages
%undefine _debugsource_packages

%global qt_module qttools
#global pre rc2

#global commit 769fa282ac8a4b98698dada6969452363e0eb415
#global shortcommit %(c=%{commit}; echo ${c:0:7})

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
Summary:        Qt6 for Windows - QtTools component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

# Add qt6 suffix to tools to avoid collision with qt5 tools
Patch0:         qttools-qt6-suffix.patch

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  qt6-qttools-devel = %{version}%{?pre:~%pre}

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtactiveqt = %{version}
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qtdeclarative = %{version}
BuildRequires:  mingw32-vulkan-loader

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtactiveqt = %{version}
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtdeclarative = %{version}
BuildRequires:  mingw64-vulkan-loader


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtTools component
# Dependency for host tools
Requires:       qt6-qttools-devel = %{version}%{?pre:~%pre}

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtTools component
# Dependency for host tools
Requires:       qt6-qttools-devel = %{version}%{?pre:~%pre}

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
# Need -DFEATURE_windeployqt=OFF to avoid cmake aborting with Qt6::windeployqt target not found
%mingw_cmake -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DFEATURE_windeployqt=OFF
%mingw_ninja


%install
%mingw_ninja_install

# Link native Qt6LinguistToolsMacros
ln -s %{_libdir}/cmake/Qt6LinguistTools %{buildroot}%{mingw32_libdir}/cmake/Qt6LinguistTools
ln -s %{_libdir}/cmake/Qt6LinguistTools %{buildroot}%{mingw64_libdir}/cmake/Qt6LinguistTools


# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/qdbus-qt6.exe
%{mingw32_bindir}/qdbusviewer-qt6.exe
%{mingw32_bindir}/qtdiag-qt6.exe
%{mingw32_bindir}/qtplugininfo-qt6.exe
%{mingw32_bindir}/Qt6DesignerComponents.dll
%{mingw32_bindir}/Qt6Designer.dll
%{mingw32_bindir}/Qt6Help.dll
%{mingw32_bindir}/Qt6UiTools.dll
%{mingw32_includedir}/qt6/QtDesigner/
%{mingw32_includedir}/qt6/QtDesignerComponents/
%{mingw32_includedir}/qt6/QtQDocCatch/
%{mingw32_includedir}/qt6/QtQDocCatchConversions/
%{mingw32_includedir}/qt6/QtQDocCatchGenerators/
%{mingw32_includedir}/qt6/QtHelp/
%{mingw32_includedir}/qt6/QtTools/
%{mingw32_includedir}/qt6/QtUiPlugin/
%{mingw32_includedir}/qt6/QtUiTools/
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtToolsTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6DesignerComponentsPrivate/
%{mingw32_libdir}/cmake/Qt6Designer/
%{mingw32_libdir}/cmake/Qt6QDocCatchConversionsPrivate/
%{mingw32_libdir}/cmake/Qt6QDocCatchGeneratorsPrivate/
%{mingw32_libdir}/cmake/Qt6QDocCatchPrivate/
%{mingw32_libdir}/cmake/Qt6/FindWrapLibClang.cmake
%{mingw32_libdir}/cmake/Qt6Help/
%{mingw32_libdir}/cmake/Qt6Linguist/
%{mingw32_libdir}/cmake/Qt6LinguistTools
%{mingw32_libdir}/cmake/Qt6Tools/
%{mingw32_libdir}/cmake/Qt6UiPlugin/
%{mingw32_libdir}/cmake/Qt6UiTools/
%{mingw32_libdir}/pkgconfig/Qt6Designer.pc
%{mingw32_libdir}/pkgconfig/Qt6Help.pc
%{mingw32_libdir}/pkgconfig/Qt6Linguist.pc
%{mingw32_libdir}/pkgconfig/Qt6UiPlugin.pc
%{mingw32_libdir}/pkgconfig/Qt6UiTools.pc
%{mingw32_libdir}/libQt6DesignerComponents.dll.a
%{mingw32_libdir}/libQt6Designer.dll.a
%{mingw32_libdir}/libQt6Help.dll.a
%{mingw32_libdir}/libQt6UiTools.dll.a
%{mingw32_libdir}/qt6/metatypes/qt6designercomponentsprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6designer_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6help_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6uitools_relwithdebinfo_metatypes.json
%{mingw32_libdir}/Qt6DesignerComponents.prl
%{mingw32_libdir}/Qt6Designer.prl
%{mingw32_libdir}/Qt6Help.prl
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_designercomponents_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_designer.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_designer_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qdoccatch_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qdoccatchconversions_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qdoccatchgenerators_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_help.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_help_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_linguist.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_tools_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_uiplugin.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_uitools.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_uitools_private.pri
%{mingw32_libdir}/qt6/plugins/designer/
%{mingw32_libdir}/Qt6UiTools.prl
%{mingw32_libdir}/qt6/modules/DesignerComponentsPrivate.json
%{mingw32_libdir}/qt6/modules/Designer.json
%{mingw32_libdir}/qt6/modules/Help.json
%{mingw32_libdir}/qt6/modules/Linguist.json
%{mingw32_libdir}/qt6/modules/QDocCatchConversionsPrivate.json
%{mingw32_libdir}/qt6/modules/QDocCatchGeneratorsPrivate.json
%{mingw32_libdir}/qt6/modules/QDocCatchPrivate.json
%{mingw32_libdir}/qt6/modules/Tools.json
%{mingw32_libdir}/qt6/modules/UiPlugin.json
%{mingw32_libdir}/qt6/modules/UiTools.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx
%{mingw32_datadir}/qt6/phrasebooks/


# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/qdbus-qt6.exe
%{mingw64_bindir}/qdbusviewer-qt6.exe
%{mingw64_bindir}/qtdiag-qt6.exe
%{mingw64_bindir}/qtplugininfo-qt6.exe
%{mingw64_bindir}/Qt6DesignerComponents.dll
%{mingw64_bindir}/Qt6Designer.dll
%{mingw64_bindir}/Qt6Help.dll
%{mingw64_bindir}/Qt6UiTools.dll
%{mingw64_includedir}/qt6/QtDesigner/
%{mingw64_includedir}/qt6/QtDesignerComponents/
%{mingw64_includedir}/qt6/QtQDocCatch/
%{mingw64_includedir}/qt6/QtQDocCatchConversions/
%{mingw64_includedir}/qt6/QtQDocCatchGenerators/
%{mingw64_includedir}/qt6/QtHelp/
%{mingw64_includedir}/qt6/QtTools/
%{mingw64_includedir}/qt6/QtUiPlugin/
%{mingw64_includedir}/qt6/QtUiTools/
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtToolsTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6DesignerComponentsPrivate/
%{mingw64_libdir}/cmake/Qt6Designer/
%{mingw64_libdir}/cmake/Qt6QDocCatchConversionsPrivate/
%{mingw64_libdir}/cmake/Qt6QDocCatchGeneratorsPrivate/
%{mingw64_libdir}/cmake/Qt6QDocCatchPrivate/
%{mingw64_libdir}/cmake/Qt6/FindWrapLibClang.cmake
%{mingw64_libdir}/cmake/Qt6Help/
%{mingw64_libdir}/cmake/Qt6Linguist/
%{mingw64_libdir}/cmake/Qt6LinguistTools
%{mingw64_libdir}/cmake/Qt6Tools/
%{mingw64_libdir}/cmake/Qt6UiPlugin/
%{mingw64_libdir}/cmake/Qt6UiTools/
%{mingw64_libdir}/pkgconfig/Qt6Designer.pc
%{mingw64_libdir}/pkgconfig/Qt6Help.pc
%{mingw64_libdir}/pkgconfig/Qt6Linguist.pc
%{mingw64_libdir}/pkgconfig/Qt6UiPlugin.pc
%{mingw64_libdir}/pkgconfig/Qt6UiTools.pc
%{mingw64_libdir}/libQt6DesignerComponents.dll.a
%{mingw64_libdir}/libQt6Designer.dll.a
%{mingw64_libdir}/libQt6Help.dll.a
%{mingw64_libdir}/libQt6UiTools.dll.a
%{mingw64_libdir}/qt6/metatypes/qt6designercomponentsprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6designer_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6help_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6uitools_relwithdebinfo_metatypes.json
%{mingw64_libdir}/Qt6DesignerComponents.prl
%{mingw64_libdir}/Qt6Designer.prl
%{mingw64_libdir}/Qt6Help.prl
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_designercomponents_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_designer.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_designer_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qdoccatch_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qdoccatchconversions_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qdoccatchgenerators_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_help.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_help_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_linguist.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_tools_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_uiplugin.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_uitools.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_uitools_private.pri
%{mingw64_libdir}/qt6/plugins/designer/
%{mingw64_libdir}/Qt6UiTools.prl
%{mingw64_libdir}/qt6/modules/DesignerComponentsPrivate.json
%{mingw64_libdir}/qt6/modules/Designer.json
%{mingw64_libdir}/qt6/modules/Help.json
%{mingw64_libdir}/qt6/modules/Linguist.json
%{mingw64_libdir}/qt6/modules/QDocCatchConversionsPrivate.json
%{mingw64_libdir}/qt6/modules/QDocCatchGeneratorsPrivate.json
%{mingw64_libdir}/qt6/modules/QDocCatchPrivate.json
%{mingw64_libdir}/qt6/modules/Tools.json
%{mingw64_libdir}/qt6/modules/UiPlugin.json
%{mingw64_libdir}/qt6/modules/UiTools.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx
%{mingw64_datadir}/qt6/phrasebooks/


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

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Fri Apr 29 2022 Sandro Mani <manisandro@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Wed Mar 30 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-7
- Make package arched, otherwise symlink to native Qt6LinguistToolsMacros cmake
  dir may point to the wrong location

* Wed Mar 30 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-6
- Link native Qt6LinguistToolsMacros cmake dir
- Add qt6 suffix to tools at cmake level

* Mon Mar 28 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-5
- Remove leftover ExclusiveArch

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-4
- Rebuild with mingw-gcc-12

* Sun Mar 06 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-3
- Re-enable s390x build

* Sat Feb 19 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-2
- Bump release

* Tue Feb 08 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Sandro Mani <manisandro@gmail.com> - 6.2.2-2
- Fix unowned dir

* Fri Jan 14 2022 Sandro Mani <manisandro@gmail.com> - 6.2.2-1
- Initial package
