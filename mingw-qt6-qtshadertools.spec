%{?mingw_package_header}

%global qt_module qtshadertools
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
Version:        6.4.3
Release:        1%{?dist}
Summary:        Qt6 for Windows - Qt Shader Tools component

License:        GPL-3.0-only
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif
Patch0:         qtshadertools_gcc13.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  qt6-qtshadertools-devel = %{version}%{?pre:~%pre}

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-vulkan-headers

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-vulkan-headers


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt Serial Port component
# Dependency for host tools
Requires:       qt6-qtshadertools-devel = %{version}%{?pre:~%pre}

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt Serial Port component
# Dependency for host tools
Requires:       qt6-qtshadertools-devel = %{version}%{?pre:~%pre}

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}


%build
%mingw_cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja


%install
%mingw_ninja_install


# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6ShaderTools.dll
%{mingw32_libdir}/cmake/Qt6ShaderTools/
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtShaderToolsTestsConfig.cmake
%{mingw32_libdir}/libQt6ShaderTools.dll.a
%{mingw32_libdir}/Qt6ShaderTools.prl
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_shadertools_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_shadertools.pri
%{mingw32_libdir}/metatypes/qt6shadertools_relwithdebinfo_metatypes.json
%{mingw32_libdir}/pkgconfig/Qt6ShaderTools.pc
%{mingw32_datadir}/qt6/modules/ShaderTools.json
%{mingw32_includedir}/qt6/QtShaderTools/


# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6ShaderTools.dll
%{mingw64_libdir}/cmake/Qt6ShaderTools/
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtShaderToolsTestsConfig.cmake
%{mingw64_libdir}/libQt6ShaderTools.dll.a
%{mingw64_libdir}/Qt6ShaderTools.prl
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_shadertools_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_shadertools.pri
%{mingw64_libdir}/metatypes/qt6shadertools_relwithdebinfo_metatypes.json
%{mingw64_libdir}/pkgconfig/Qt6ShaderTools.pc
%{mingw64_datadir}/qt6/modules/ShaderTools.json
%{mingw64_includedir}/qt6/QtShaderTools/


%changelog
* Wed Mar 29 2023 Sandro Mani <manisandro@gmail.com> - 6.4.3-1
- Update to 6.4.3

* Tue Mar 28 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Fri Nov 25 2022 Sandro Mani <manisandro@gmail.com> - 6.4.1-1
- Update to 6.4.1

* Thu Nov 03 2022 Sandro Mani <manisandro@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Thu Apr 28 2022 Sandro Mani <manisandro@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-3
- Rebuild with mingw-gcc-12

* Sat Mar 05 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-2
- Re-enable s390x build

* Tue Feb 01 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Thu Sep 30 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.rc2
- Initial package
