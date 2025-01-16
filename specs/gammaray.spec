%ifarch %{ix86}
    %global arch i686
%else
    %global arch %{_arch}
%endif

%ifarch %{?qt6_qtwebengine_arches}
%global webengine 1
%endif

%global qt5_ver %(echo %{_qt5_version} | cut -d. -f1,2)
%global qt5_target %(echo qt%{qt5_ver}-%{arch} | sed 's/\\./_/g')
  
%global qt6_ver %(echo %{_qt6_version} | cut -d. -f1,2)
%global qt6_target %(echo qt%{qt6_ver}-%{arch} | sed 's/\\./_/g')

%global gammaray_ver 3.1
%global gammaray_ver_minor 0
%global gammaray_version %{gammaray_ver}.%{gammaray_ver_minor}

Name:    gammaray
Version: 3.1.0
Release: 5%{?dist}
Summary: A tool for examining internals of Qt applications
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://github.com/KDAB/GammaRay

Source0: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Patch1:  gammaray-fix-build-with-qt6.8.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: desktop-file-utils

BuildRequires: elfutils-devel
BuildRequires: binutils-devel
BuildRequires: libdwarf-devel
BuildRequires: libunwind-devel

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules

# to build the documentation
BuildRequires: doxygen
BuildRequires: qt6-doc-devel
BuildRequires: qt6-doc-html
BuildRequires: qt6-doctools

# Qt6 GUI and probe
BuildRequires: qt6-qtbase-private-devel
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt63DAnimation)
BuildRequires: cmake(Qt63DExtras)
BuildRequires: cmake(Qt63DInput)
BuildRequires: cmake(Qt63DLogic)
BuildRequires: cmake(Qt63DRender)
BuildRequires: cmake(Qt63DQuick)
BuildRequires: cmake(Qt6Bluetooth)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6Location)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6ShaderTools)
%if 0%{?webengine}
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WaylandCompositor)
BuildRequires: wayland-devel

# optional dependencies
BuildRequires: cmake(Qt6Scxml)
BuildRequires: cmake(Qt6StateMachine)
BuildRequires: cmake(KF6SyntaxHighlighting)

# for building the probe qt5 for introspection of Qt5 apps
BuildRequires:	qt5-qt3d-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtbase-doc
BuildRequires:	qt5-qtbase-private-devel
BuildRequires:	qt5-qtdeclarative-devel
BuildRequires:	qt5-qtscript-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	qt5-qtscxml-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtwayland-devel
%ifarch %{?qt5_qtwebengine_arches}
BuildRequires: qt5-qtwebengine-devel
%endif


Requires:	%{name}-probe = %{version}-%{release}
Recommends:	(%{name}-probe-qt5%{?_isa} = %{version}-%{release} if qt5-qtbase)
Recommends:	(%{name}-probe-qt6%{?_isa} = %{version}-%{release} if qt6-qtbase)
# When -doc subpkg was removed
Obsoletes: %{name}-doc <= 2.2.1

# omit provides from plugins
%global __provides_exclude_from \
         ^((%{_qt5_libdir}|%{_qt6_libdir})/libgammaray.*\\.so)$
         
%description
A tool to poke around in a Qt-application and also to manipulate
the application to some extent. It uses various DLL injection
techniques to hook into an application at run-time and provide
access to a lot of interesting information.

GammaRay can introspect Qt 6 and Qt 5 applications.


%package probe-qt5
Summary:	Qt 5 probe for GammaRay
Provides:	%{name}-probe = %{version}-%{release}
Obsoletes:	%{name}-qt5 < %{version}-%{release}
Requires:	qt5-qtbase%{?_isa} = %{_qt5_version}
Requires:	%{name} = %{version}-%{release}

%description probe-qt5
Provides a Qt 5 probe for GammaRay that allows introspecting Qt 5
applications. It is possible to install probes for different
architectures or Qt versions as well. GammaRay will then be able
to inspect those applications too.


%package probe-qt5-devel
Summary:        Development files for %{name} Qt5 probe
Requires:       %{name}-probe-qt5%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description probe-qt5-devel
The %{name}probe-qt5-devel package contains development libraries for
the %{name} Qt5 integration.


%package probe-qt6
Summary:    Qt 6 probe for GammaRay
Provides:   %{name}-probe = %{version}-%{release}
Requires:   qt6-qtbase%{?_isa} = %{_qt6_version}
Requires:   %{name} = %{version}-%{release}

%description probe-qt6
Provides a Qt 6 probe for GammaRay that allows introspecting Qt 6
applications. It is possible to install probes for different
architectures or Qt versions as well. GammaRay will then be able
to inspect those applications too.

%package probe-qt6-devel
Summary:        Development files for %{name} Qt6 probe
Requires:       %{name}-probe-qt6%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description probe-qt6-devel
The %{name}probe-qt6-devel package contains development libraries for
the %{name} Qt6 integration.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-probe-qt6-devel%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing plugins for %{name}.

	
%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.


%prep
%autosetup -n %{name}-%{version} -p1


%build

%define _vpath_builddir %{_target_platform}_client
%cmake_qt6 \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=TRUE \
    -DQt6_DIR=%{_libdir}/cmake/Qt6 \
    -DQT_VERSION_MAJOR=6 \
    -DGAMMARAY_QT6_BUILD:BOOL=TRUE \
    -DGAMMARAY_CLIENT_ONLY_BUILD:BOOL=TRUE \
    -DGAMMARAY_BUILD_DOCS:BOOL=TRUE \
    -DGAMMARAY_INSTALL_QT_LAYOUT:BOOL=FALSE \
    -DLIBEXEC_INSTALL_DIR=libexec \
    -DECM_MKSPECS_INSTALL_DIR=%{_qt6_mkspecsdir}/modules \
    -DQCH_INSTALL_DIR=%{_qt6_docdir} \
    -DQT_INSTALL_BINS=%{_qt6_libexecdir} \
    -DQDOC_INDEX_DIR=%{_qt6_docdir} \
    -DQDOC_TEMPLATE_DIR=%{_qt6_docdir}

%cmake_build

# build the Qt6 probe only
%define _vpath_builddir %{_target_platform}_qt6
%cmake_qt6 \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=TRUE \
    -DQt6_DIR=%{_libdir}/cmake/Qt6 \
    -DQT_VERSION_MAJOR=6 \
    -DGAMMARAY_QT6_BUILD:BOOL=TRUE \
    -DGAMMARAY_BUILD_UI:BOOL=FALSE \
    -DGAMMARAY_BUILD_DOCS:BOOL=FALSE \
    -DGAMMARAY_PROBE_ONLY_BUILD:BOOL=TRUE \
    -DGAMMARAY_INSTALL_QT_LAYOUT:BOOL=FALSE \
    -DLIBEXEC_INSTALL_DIR=libexec

%cmake_build

# build the Qt5 probe only
%define _vpath_builddir %{_target_platform}_qt5
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=TRUE \
    -DQt5_DIR=%{_libdir}/cmake/Qt5 \
    -DQt_DIR=%{_libdir}/cmake/Qt5 \
    -DQT_VERSION_MAJOR=5 \
    -DGAMMARAY_QT6_BUILD:BOOL=FALSE \
    -DGAMMARAY_BUILD_UI:BOOL=FALSE \
    -DGAMMARAY_BUILD_DOCS:BOOL=FALSE \
    -DGAMMARAY_PROBE_ONLY_BUILD:BOOL=TRUE \
    -DGAMMARAY_INSTALL_QT_LAYOUT:BOOL=FALSE \
    -DLIBEXEC_INSTALL_DIR=libexec

%cmake_build


%install

%define _vpath_builddir %{_target_platform}_client
%cmake_install
%define _vpath_builddir %{_target_platform}_qt6
%cmake_install
%define _vpath_builddir %{_target_platform}_qt5
%cmake_install

# We install the license manually
rm -fv %{buildroot}%{_docdir}/gammaray/LICENSE.txt
rm -rfv %{buildroot}%{_docdir}/gammaray/LICENSES

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/GammaRay.desktop

%files
%doc README.md
%license LICENSES/*
%{_bindir}/gammaray
%{_qt6_libdir}/libgammaray_client.so.*
%{_qt6_libdir}/libgammaray_launcher.so.*
%{_qt6_libdir}/libgammaray_launcher_ui.so.*
%{_qt6_libdir}/libgammaray_kuserfeedback.so.*
%{_qt6_libdir}/gammaray/libexec/gammaray-launcher
%{_qt6_libdir}/gammaray/libexec/gammaray-client
%{_datadir}/applications/GammaRay.desktop
%{_datadir}/icons/hicolor/*/apps/GammaRay.png
%{_datadir}/metainfo/com.kdab.GammaRay.metainfo.xml
%{_datadir}/zsh/site-functions/_gammaray
%lang(de) %{_datadir}/gammaray/translations/gammaray_de.qm
%lang(en) %{_datadir}/gammaray/translations/gammaray_en.qm

%files probe-qt5
%{_qt5_libdir}/libgammaray_common-%{qt5_target}.so.*
%{_qt5_libdir}/libgammaray_core-%{qt5_target}.so.*
%{_qt5_libdir}/libgammaray_kitemmodels-%{qt5_target}.so.*
%{_qt5_libdir}/gammaray/%{gammaray_ver}/%{qt5_target}/

%files probe-qt5-devel
%{_qt5_libdir}/libgammaray_common-%{qt5_target}.so
%{_qt5_libdir}/libgammaray_core-%{qt5_target}.so
%{_qt5_libdir}/libgammaray_kitemmodels-%{qt5_target}.so
  
%files probe-qt6
%{_qt6_libdir}/libgammaray_ui-%{qt6_target}.so.*
%{_qt6_libdir}/libgammaray_common-%{qt6_target}.so.*
%{_qt6_libdir}/libgammaray_core-%{qt6_target}.so.*
%{_qt6_libdir}/libgammaray_kitemmodels-%{qt6_target}.so.*
%{_qt6_libdir}/gammaray/%{gammaray_ver}/%{qt6_target}/

%files probe-qt6-devel
%{_qt6_libdir}/libgammaray_ui-%{qt6_target}.so
%{_qt6_libdir}/libgammaray_common-%{qt6_target}.so
%{_qt6_libdir}/libgammaray_core-%{qt6_target}.so
%{_qt6_libdir}/libgammaray_kitemmodels-%{qt6_target}.so
%{_qt6_libdir}/gammaray/%{gammaray_ver}/%{qt6_target}/

%files devel
%{_includedir}/gammaray
%{_qt6_libdir}/libgammaray_client.so
%{_qt6_libdir}/libgammaray_launcher.so
%{_qt6_libdir}/libgammaray_launcher_ui.so
%{_qt6_libdir}/libgammaray_kuserfeedback.so
%{_libdir}/cmake/GammaRay/
# this is an error in the sources, it should go to qt6
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayCommon.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayCore.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayUi.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayClient.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayKItemModels.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayLauncher.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayLauncherUi.pri

%files doc
%{_mandir}/man1/gammaray.1.gz
%{_qt6_docdir}/gammaray-api.qch
%{_qt6_docdir}/gammaray-manual.qch
%{_qt6_docdir}/gammaray.qhc


%changelog
* Tue Jan 14 2025 Jan Grulich <jgrulich@redhat.com> - 3.1.0-5
- Rebuild (qt5)

* Mon Dec 09 2024 Jan Grulich <jgrulich@redhat.com> - 3.1.0-4
- Rebuild (qt6)

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 3.1.0-3
- Rebuild (qt6)

* Thu Sep 05 2024 Jan Grulich <jgrulich@redhat.com> - 3.1.0-2
- Rebuild (qt5)

* Tue Aug 06 2024 Jan Grulich <jgrulich@redhat.com> - 3.1.0-1
- 3.1.0

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Jan Grulich <jgrulich@redhat.com> - 3.0.0-7
- Rebuild (qt6)

* Thu May 30 2024 Jan Grulich <jgrulich@redhat.com> - 3.0.0-6
- Rebuild (qt5)

* Thu May 30 2024 Jan Grulich <jgrulich@redhat.com> - 3.0.0-5
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 3.0.0-4
- Rebuild (qt6)

* Fri Mar 15 2024 Jan Grulich <jgrulich@redhat.com> - 3.0.0-3
- Rebuild (qt5)

* Fri Mar 08 2024 FeRD (Frank Dana) <ferdnyc@gmail.com> - 3.0.0-2
- after merging the last PR to move to Qt6, merge the remaining features
  on behalf of Frank Dana (by Marie Loise Nolden <loise@kde.org>:
- Build Qt6-based client with both Qt6 and Qt5 probes
  
* Fri Feb 23 2024 Marie Loise Nolden <loise@kde.org> - 3.0.0-1
- update to 3.0.0 using Qt6

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Jan Grulich <jgrulich@redhat.com> - 2.11.3-14
- Rebuild (qt5)

* Mon Oct 09 2023 Jan Grulich <jgrulich@redhat.com> - 2.11.3-13
- Drop BR: qtwebkit and add BR: qtwebengine instead

* Mon Oct 09 2023 Jan Grulich <jgrulich@redhat.com> - 2.11.3-12
- Rebuild (qt5)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Jan Grulich <jgrulich@redhat.com> - 2.11.3-10
- Rebuild (qt5)

* Wed Apr 12 2023 Jan Grulich <jgrulich@redhat.com> - 2.11.3-9
- Rebuild (qt5)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Jan Grulich <jgrulich@redhat.com> - 2.11.3-7
- Rebuild (qt5)

* Mon Oct 31 2022 Jan Grulich <jgrulich@redhat.com> - 2.11.3-6
- Rebuild (qt5)

* Fri Sep 23 2022 Jan Grulich <jgrulich@redhat.com> - 2.11.3-5
- Rebuild (qt5)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 2.11.3-3
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 2.11.3-2
- Rebuild (qt5)

* Fri May 13 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2.11.3-1
- Update to 2.11.3 (rhbz #2014949 + #2063072) and Iñaki Úcar's dependency PR

* Tue Mar 22 2022 Jan Grulich <jgrulich@redhat.com> - 2.11.2-7
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Petr Viktorin <pviktori@redhat.com> - 2.11.2-3
- Remove BuildRequires on python2-devel

* Mon Nov 23 07:52:16 CET 2020 Jan Grulich <jgrulich@redhat.com> - 2.11.2-2
- rebuild (qt5)

* Fri Sep 25 2020 Jan Grulich <jgrulich@redhat.com> - 2.11.2-1
- 2.11.2

* Thu Sep 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.11.4-5
- %%undefine __cmake_in_source_build

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 2.11.1-4
- rebuild (qt5)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.11.1-1
- 2.11.1

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.11.0-6
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 2.11.0-4
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 2.11.0-3
- rebuild (qt5)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Jan Grulich <jgrulich@redhat.com> - 2.11.0-1
- 2.11.0
- drop Qt4

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 2.10.0-3
- rebuild (qt5)

* Thu Jun 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.10.0-2
- rebuild (qt5)

* Sun Mar 17 2019 Orion Poplawski <orion@nwra.com> - 2.10.0-1
- Update to 2.10.0

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - -2.9.0-10
- rebuild (qt5)

* Tue Feb 26 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-9
- Drop BR on vtk-devel - not needed with Qt5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.9.0-7
- rebuild (qt5)

* Sat Oct 27 2018 Orion Poplawski <orion@cora.nwra.com> - 2.9.0-6
- Rebuild for VTK 8.1

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 2.9.0-5
- rebuild (qt5)

* Thu Aug 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.9.0-4
- drop mkspecs hack causing FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.9.0-2
- rebuild (qt5)

* Sat Jun 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.9.0-1
- gammayray-2.9.0
- make qt4 support optional (off for now)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.8.1-9
- rebuild (qt5)

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.8.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> -  2.8.1-7
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.1-5
- Remove obsolete scriptlets

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 2.8.1-4
- rebuild (qt5)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.8.1-3
- rebuild (qt5)

* Tue Oct 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.8.1-2
- rebuild (qt5)

* Wed Sep 06 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 2.8.1-1
- update to GammaRay 2.8.1

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 2.8.0-5
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.8.0-2
- rebuild (qt5)

* Thu Jun 08 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 2.8.0-1
- update to GammaRay 2.8.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun May 07 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 2.7.0-4
- rebuild (qt5)

* Fri Mar 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.7.0-3
- rebuild (qt5)

* Sat Feb 18 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 2.7.0-2
- add kf5-syntax-highligting dependency
- fix Qt4 source lookup

* Wed Feb 15 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 2.7.0-1
- update to GammaRay 2.7.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 2.6.0-1.2
- Qt5 rebuild

* Mon Nov 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.6.0-1.1
- branch rebuild (qt5)

* Sun Nov 06 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 2.6.0-1
- update to GammaRay 2.6.0

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.4.1-4
- rebuild (qt 5.7.0), simplify qt5 versioning macro usage

* Fri Jun 10 2016 Jan Grulich <jgrulich@redhat.com> - 2.4.1-3
- Rebuild (qt5-qtbase)

* Sun Apr 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.4.1-2
- -qt5: BR: qt5-qtbase-private-devel

* Thu Mar 17 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 2.4.1-1
- GammaRay 2.4.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Jan Grulich <jgrulich@redhat.com> - 2.4.0-1
- GammaRay 2.4.0

* Sun Dec 06 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 2.3.0-5
- Rebuild against Qt 5.6.0 update on rawhide

* Thu Oct 29 2015 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-4
- Rebuild for vtk 6.3.0

* Mon Oct 12 2015 Daniel Vrátil <dvratil@redhat.com> - 2.3.0-3
- Rebuild against Qt 5.5.1 update on rawhide

* Tue Sep 01 2015 Daniel Vrátil <dvratil@redhat.com> - 2.3.0-2
- Rebuild against new Qt 5.5 on F21+

* Tue Jul 14 2015 Daniel Vrátil <dvratil@redhat.com> - 2.3.0-1
- GammaRay 2.3.0

* Tue Jun 30 2015 Daniel Vrátil <dvratil@redhat.com> - 2.2.1-11
- Rebuild on Qt 5.5 in rawhide

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jan Grulich <jgrulich@redhat.com> - 2.2.1-9
- rebuild (qt-5.4.2)

* Mon May 18 2015 Daniel Vrátil <dvratil@redhat.com> - 2.2.1-8
- probes require the main UI (otherwise they are not very useful)
- update to Qt 4.8.7 in rawhide

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-7
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 27 2015 Daniel Vrátil <dvratil@redhat.com> - 2.2.1-6
- rebuild (qt-5.4.1)

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-5
- use %%_qt5_version macro instead for runtime deps, ie depend on the
  version of qt5 used during the build, not some hard-coded value.

* Thu Feb 26 2015 Rex Dieter <rdieter@fedoraproject.org> 2.2.1-4
- rebuild (qt-5.4.1)

* Tue Feb 03 2015 Daniel Vrátil <dvratil@redhat.com> - 2.2.1-3
- fix typo

* Tue Feb 03 2015 Daniel Vrátil <dvratil@redhat.com> - 2.2.1-2
- drop ambiguous BuildArch

* Tue Feb 03 2015 Daniel Vrátil <dvratil@redhat.com> - 2.2.1-1
- Update to 2.2.1
- Default to Qt 5 build now
- Provide probes for Qt 5 and Qt 4 in -qt5 and -qt4 subpackages

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1.1-2
- Rebuild for hdf5 1.8.4

* Tue Sep 23 2014 Richard Hughes <richard@hughsie.com> - 2.1.1-1
- Update to new upstream release.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  8 2014 Tom Callaway <spot@fedoraproject.org> - 2.0.2-1
- update to 2.0.2

* Mon Jan 27 2014 Daniel Vrátil <dvratil@redhat.com> - 2.0.0-2
- rebuilt against VTK

* Thu Jan 23 2014 Daniel Vrátil <dvratil@redhat.com> - 2.0.0-1
- GammaRay 2.0.0
- require specific version of Qt
- point CMake to VTK dir
- enforce Qt 4 build (GammaRay automatically switches to Qt 5 build when it finds it installed)
- remove rpath workaround
- fix installation destination of libexec binaries

* Thu Jan 02 2014 Daniel Vrátil <dvratil@redhat.com> - 1.3.2-2
- Rebuilt against new VTK
- BR blas-devel
- BR lapack-devel
- BR netcdf-devel

* Thu Dec 05 2013 Daniel Vrátil <dvratil@redhat.com> - 1.3.2-1
- GammaRay 1.3.2

* Tue Aug 27 2013 Daniel Vrátil <dvratil@redhat.com> - 1.3.1-3
- fix duplicate documentation files (#1001275)

* Tue Aug 27 2013 Daniel Vrátil <dvratil@redhat.com> - 1.3.1-2
- update Qt sources
- fix build against VTK 6.0

* Mon Aug 05 2013 Daniel Vrátil <dvratil@redhat.com> - 1.3.1-1
- GammaRay 1.3.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Daniel Vrátil <dvratil@redhat.com> - 1.3.0-4
- add perl-podlators to BR as they've been split from perl pkg in rawhide

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Feb 05 2013 Daniel Vrátil <dvratil@redhat.com> - 1.3.0-2
- rename docs subpackage to doc
- use %%global instead of %%define

* Tue Jan 29 2013 Daniel Vrátil <dvratil@redhat.com> - 1.3.0-1
- first attempt
