%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}

%global qt_module qttools
#global pre beta

#global commit 769fa282ac8a4b98698dada6969452363e0eb415
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
Summary:        Qt5 for Windows - QtTools component

# Automatically converted from old format: GPLv3 with exceptions or LGPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv3-with-exceptions OR LGPL-2.0-or-later WITH FLTK-exception
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

# Fix undefined references when buildling qaxwidget designer plugin
Patch0:         qttools-fix-qaxwidget-build.patch
# Run tools with -qt5 suffix
Patch1:         qttools-qt5-suffix.patch
# gcc-11 related fixes
Patch2:         qttools-gcc11.patch
# Fix passing incompatible pointer
Patch3:         qttools-incompatible-pointer.patch

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtbase-devel = %{version}
BuildRequires:  mingw32-qt5-qmldevtools-devel = %{version}
BuildRequires:  mingw32-qt5-qtactiveqt = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtbase-devel = %{version}
BuildRequires:  mingw64-qt5-qmldevtools-devel = %{version}
BuildRequires:  mingw64-qt5-qtactiveqt = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtTools component
BuildArch:      noarch

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - QtTools component
Obsoletes:      mingw32-qt5-%{qt_module}-lrelease < 5.1.2-1
Provides:       mingw32-qt5-%{qt_module}-lrelease = 5.1.2-1

# Some tools depend on libQt5QmlDevTools.so.5 which is in
# a non-default path so the regular RPM dependency generator
# doesn't automatically add the correct Requires tag
# https://bugzilla.redhat.com/show_bug.cgi?id=1301577
Requires:       mingw32-qt5-qmldevtools-devel >= 5.6.0

%description -n mingw32-qt5-%{qt_module}-tools
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtTools component
BuildArch:      noarch

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - QtTools component
Obsoletes:      mingw64-qt5-%{qt_module}-lrelease < 5.1.2-1
Provides:       mingw64-qt5-%{qt_module}-lrelease = 5.1.2-1

# Some tools depend on libQt5QmlDevTools.so.5 which is in
# a non-default path so the regular RPM dependency generator
# doesn't automatically add the correct Requires tag
# https://bugzilla.redhat.com/show_bug.cgi?id=1301577
Requires:       mingw64-qt5-qmldevtools-devel >= 5.6.0

%description -n mingw64-qt5-%{qt_module}-tools
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

# The .dll's are installed in both %%{mingw32_bindir} and %%{mingw32_libdir}
# One copy of the .dll's is sufficient
rm -f %{buildroot}%{mingw32_libdir}/*.dll
rm -f %{buildroot}%{mingw64_libdir}/*.dll

# Make sure the executables don't conflict with their mingw-qt4 counterpart
for fn in %{buildroot}%{mingw32_bindir}/*.exe %{buildroot}%{mingw64_bindir}/*.exe ; do
    fn_new=$(echo $fn | sed s/'.exe$'/'-qt5.exe'/)
    mv $fn $fn_new
done

# Create symlinks for the tools lconvert, lupdate and lrelease tools
mkdir -p %{buildroot}%{_bindir}

for tool in lconvert lupdate lrelease; do
    ln -s ../%{mingw32_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw32_target}-$tool-qt5
    ln -s ../%{mingw64_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw64_target}-$tool-qt5
done


# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt5Designer.dll
%{mingw32_bindir}/Qt5DesignerComponents.dll
%{mingw32_bindir}/Qt5Help.dll
%{mingw32_bindir}/assistant-qt5.exe
%{mingw32_bindir}/designer-qt5.exe
%{mingw32_bindir}/linguist-qt5.exe
%{mingw32_bindir}/pixeltool-qt5.exe
%{mingw32_bindir}/qcollectiongenerator-qt5.exe
%{mingw32_bindir}/qdbus-qt5.exe
%{mingw32_bindir}/qdbusviewer-qt5.exe
%{mingw32_bindir}/qhelpgenerator-qt5.exe
%{mingw32_bindir}/qtdiag-qt5.exe
%{mingw32_bindir}/qdistancefieldgenerator-qt5.exe
%{mingw32_bindir}/qtpaths-qt5.exe
%{mingw32_bindir}/qtplugininfo-qt5.exe
%{mingw32_includedir}/qt5/QtDesigner/
%{mingw32_includedir}/qt5/QtDesignerComponents/
%{mingw32_includedir}/qt5/QtHelp/
%{mingw32_includedir}/qt5/QtUiPlugin/
%{mingw32_includedir}/qt5/QtUiTools/
%{mingw32_libdir}/*.prl
%{mingw32_libdir}/libQt5Designer.dll.a
%{mingw32_libdir}/libQt5DesignerComponents.dll.a
%{mingw32_libdir}/libQt5Help.dll.a
# QtUiTools is only built as static library by default
%{mingw32_libdir}/libQt5UiTools.a
%{mingw32_libdir}/qt5/plugins/designer/
%{mingw32_libdir}/cmake/Qt5AttributionsScannerTools/
%{mingw32_libdir}/cmake/Qt5Designer/
%{mingw32_libdir}/cmake/Qt5DesignerComponents/
%{mingw32_libdir}/cmake/Qt5Help/
%{mingw32_libdir}/cmake/Qt5LinguistTools/
%{mingw32_libdir}/cmake/Qt5UiPlugin/
%{mingw32_libdir}/cmake/Qt5UiTools/
%{mingw32_libdir}/pkgconfig/Qt5Designer.pc
%{mingw32_libdir}/pkgconfig/Qt5Help.pc
%{mingw32_libdir}/pkgconfig/Qt5UiTools.pc
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_designer.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_designer_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_designercomponents_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_help.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_help_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_uiplugin.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_uitools.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_uitools_private.pri
%{mingw32_datadir}/qt5/phrasebooks/

%files -n mingw32-qt5-%{qt_module}-tools
%{_bindir}/%{mingw32_target}-lconvert-qt5
%{_bindir}/%{mingw32_target}-lupdate-qt5
%{_bindir}/%{mingw32_target}-lrelease-qt5
%{_prefix}/%{mingw32_target}/bin/qt5/lconvert
%{_prefix}/%{mingw32_target}/bin/qt5/lupdate
%{_prefix}/%{mingw32_target}/bin/qt5/lupdate-pro
%{_prefix}/%{mingw32_target}/bin/qt5/lprodump
%{_prefix}/%{mingw32_target}/bin/qt5/lrelease
%{_prefix}/%{mingw32_target}/bin/qt5/lrelease-pro
%{_prefix}/%{mingw32_target}/bin/qt5/qtattributionsscanner
%{_prefix}/%{mingw32_target}/bin/qt5/windeployqt

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5Designer.dll
%{mingw64_bindir}/Qt5DesignerComponents.dll
%{mingw64_bindir}/Qt5Help.dll
%{mingw64_bindir}/assistant-qt5.exe
%{mingw64_bindir}/designer-qt5.exe
%{mingw64_bindir}/linguist-qt5.exe
%{mingw64_bindir}/pixeltool-qt5.exe
%{mingw64_bindir}/qcollectiongenerator-qt5.exe
%{mingw64_bindir}/qdbus-qt5.exe
%{mingw64_bindir}/qdbusviewer-qt5.exe
%{mingw64_bindir}/qhelpgenerator-qt5.exe
%{mingw64_bindir}/qtdiag-qt5.exe
%{mingw64_bindir}/qdistancefieldgenerator-qt5.exe
%{mingw64_bindir}/qtpaths-qt5.exe
%{mingw64_bindir}/qtplugininfo-qt5.exe
%{mingw64_includedir}/qt5/QtDesigner/
%{mingw64_includedir}/qt5/QtDesignerComponents/
%{mingw64_includedir}/qt5/QtHelp/
%{mingw64_includedir}/qt5/QtUiPlugin/
%{mingw64_includedir}/qt5/QtUiTools/
%{mingw64_libdir}/*.prl
%{mingw64_libdir}/libQt5Designer.dll.a
%{mingw64_libdir}/libQt5DesignerComponents.dll.a
%{mingw64_libdir}/libQt5Help.dll.a
# QtUiTools is only built as static library by default
%{mingw64_libdir}/libQt5UiTools.a
%{mingw64_libdir}/qt5/plugins/designer/
%{mingw64_libdir}/cmake/Qt5AttributionsScannerTools/
%{mingw64_libdir}/cmake/Qt5Designer/
%{mingw64_libdir}/cmake/Qt5DesignerComponents/
%{mingw64_libdir}/cmake/Qt5Help/
%{mingw64_libdir}/cmake/Qt5LinguistTools/
%{mingw64_libdir}/cmake/Qt5UiPlugin/
%{mingw64_libdir}/cmake/Qt5UiTools/
%{mingw64_libdir}/pkgconfig/Qt5Designer.pc
%{mingw64_libdir}/pkgconfig/Qt5Help.pc
%{mingw64_libdir}/pkgconfig/Qt5UiTools.pc
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_designer.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_designer_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_designercomponents_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_help.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_help_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_uiplugin.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_uitools.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_uitools_private.pri
%{mingw64_datadir}/qt5/phrasebooks/

%files -n mingw64-qt5-%{qt_module}-tools
%{_bindir}/%{mingw64_target}-lconvert-qt5
%{_bindir}/%{mingw64_target}-lupdate-qt5
%{_bindir}/%{mingw64_target}-lrelease-qt5
%{_prefix}/%{mingw64_target}/bin/qt5/lconvert
%{_prefix}/%{mingw64_target}/bin/qt5/lupdate
%{_prefix}/%{mingw64_target}/bin/qt5/lupdate-pro
%{_prefix}/%{mingw64_target}/bin/qt5/lprodump
%{_prefix}/%{mingw64_target}/bin/qt5/lrelease
%{_prefix}/%{mingw64_target}/bin/qt5/lrelease-pro
%{_prefix}/%{mingw64_target}/bin/qt5/qtattributionsscanner
%{_prefix}/%{mingw64_target}/bin/qt5/windeployqt


%changelog
* Wed Jan 22 2025 Sandro Mani <manisandro@gmail.com> - 5.15.16-1
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

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 5.15.3-2
- Rebuild with mingw-gcc-12

* Tue Mar 15 2022 Sandro Mani <manisandro@gmail.com> - 5.15.3-1
- Update to 5.15.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 22 2021 Jan Blackquill <uhhadd@gmail.com> - 5.15.2-3
- Don't strip .prl files from build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 18:37:54 CET 2020 Sandro Mani <manisandro@gmail.com> - 5.15.2-1
- Update to 5.15.2

* Fri Oct 30 2020 Jeff Law <law@redhat.com> - 5.15.1-2
- Fix missing #include for gcc-11

* Wed Oct  7 11:16:24 CEST 2020 Sandro Mani <manisandro@gmail.com> - 5.15.1-1
- Update to 5.15.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-2
- Rebuild for fixed create_cmake.prf in qtbase

* Wed Apr 08 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-1
- Update to 5.14.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-1
- Update to 5.13.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Sep 26 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-1
- Update to 5.12.5

* Tue Aug 27 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-3
- Rebuild to fix pkg-config files (#1745257)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-1
- Update to 5.12.4

* Thu Apr 18 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-1
- Update to 5.12.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Sandro Mani <manisandro@gmail.com> - 5.11.3-1
- Update to 5.11.3

* Sun Sep 23 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-1
- Update to 5.11.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Sandro Mani <manisandro@gmail.com> - 5.11.1-1
- Update to 5.11.1

* Wed May 30 2018 Sandro Mani <manisandro@gmail.com> - 5.11.0-1
- Update to 5.11.0

* Wed Mar 07 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-2
- Add missing BR: gcc-c++, make

* Fri Feb 16 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-1
- Update to 5.10.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Sandro Mani <manisandro@gmail.com> - 5.10.0-1
- Update to 5.10.0

* Mon Nov 27 2017 Sandro Mani <manisandro@gmail.com> - 5.9.3-1
- Update to 5.9.3

* Wed Oct 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-1
- Update to 5.9.2

* Wed Aug 09 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-4
- Force old debuginfo package logic for now

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

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

* Sat May  7 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.6.0-2
- Some .dll.a files accidently got lost since previous build

* Thu Apr  7 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.6.0-1
- Update to 5.6.0
- Prevent .dll.debug files in the main packages

* Sat Feb  6 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.1-3
- Add manual Requires tags for dependencies which RPM doesn't add automatically (RHBZ #1301577)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.1-1
- Update to 5.5.1

* Thu Aug  6 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 21 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.1-1
- Update to 5.4.1

* Mon Dec 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0

* Sat Sep 20 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.2-1
- Update to 5.3.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul  6 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.0-2
- Disable c++11 support on arm to workaround internal compiler error in mingw-gcc 4.9

* Sat May 24 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0

* Mon Mar 24 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-2
- Fix invalid reference to the tools in the CMake files (the native tools don't have the .exe extension)

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Tue Jan  7 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-2
- Dropped manual rename of import libraries

* Sun Jan  5 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0

* Fri Nov 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-0.1.rc1
- Update to 5.2.0 RC1
- Renamed the -lrelease subpackage to -tools

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1

* Tue Jul 30 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-2
- Rebuild due to the introduction of arm as primary architecture

* Thu Jul 11 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0
- Changed URL to http://qt-project.org/

* Tue Apr 30 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2

* Sat Feb  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Fri Jan 11 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-1
- Update to Qt 5.0.0 Final
- Added new subpackages which contain the native binary for the lrelease tool
- Added BR: mingw32-qt5-qtbase-devel mingw64-qt5-qtbase-devel as it contains
  files needed to build the lrelease tool

* Mon Nov 12 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.2.beta1.git20121112.769fa282
- Update to 20121112 snapshot (rev 769fa282)
- Rebuild against latest mingw-qt5-qtbase
- Dropped pkg-config rename hack as it's unneeded now
- Dropped upstreamed patch

* Thu Sep 13 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.1.beta1
- Initial release

