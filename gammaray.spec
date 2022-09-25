%undefine __cmake_in_source_build
%ifarch %{ix86}
    %global arch i686
%else
    %global arch %{_arch}
%endif

%global qt5_ver %(echo %{_qt5_version} | cut -d. -f1,2)
%global qt5_target %(echo qt%{qt5_ver}-%{arch} | sed 's/\\./_/g')

%global gammaray_ver 2.11
%global gammaray_ver_minor 3
%global gammaray_version %{gammaray_ver}.%{gammaray_ver_minor}

Name:		gammaray
Version:	%{gammaray_version}
Release:	5%{?dist}
Summary:	A tool for examining internals of Qt applications
License:	GPLv2+
URL:		https://github.com/KDAB/GammaRay
Source0:	%{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:		qt-system-paths.patch

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-syntax-highlighting-devel
BuildRequires:  qt5-qt3d-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtbase-doc
BuildRequires:	qt5-qtbase-private-devel
BuildRequires:	qt5-qtdeclarative-devel
BuildRequires:	qt5-qtscript-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	qt5-qtscxml-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtwayland-devel
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	wayland-devel
Requires:	%{name}-qt5 = %{version}-%{release}
# When -doc subpkg was removed
Obsoletes:	%{name}-doc <= 2.2.1

# omit provides from plugins
%global __provides_exclude_from ^(%{_qt5_libdir}/gammaray.*\\.so)$

%description
A tool to poke around in a Qt-application and also to manipulate
the application to some extent. It uses various DLL injection
techniques to hook into an application at run-time and provide
access to a lot of interesting information.

By default GammaRay can only introspect Qt 5 applications.

%package qt5
Summary:	Qt 5 probe for GammaRay
Requires:	qt5-qtbase%{?_isa} = %{_qt5_version}
Requires:	%{name} = %{version}-%{release}

%description qt5
Provides a Qt 5 probe for GammaRay that allows introspecting Qt 5
applications. This probe is installed by default. It is possible
to install probes for different architectures as well, GammaRay
will then be able to inspect those applications too.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing plugins for %{name}.

%package doc
Summary:	Developer documentation for %{name}
BuildArch:	noarch

%description doc
This package includes developer documentation in HTML format.


%prep
%setup -q -n %{name}-%{version}

%build
%global _target_platform_qt5 %{_target_platform}_qt5

%cmake .. \
        -DLIBEXEC_INSTALL_DIR=libexec \
	-DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt5/mkspecs/modules \
        -DQCH_INSTALL_DIR=%{_docdir}/gammaray

%cmake_build
make docs

%install
%cmake_install

# We install the license manually
rm -fv %{buildroot}%{_docdir}/gammaray/LICENSE.*

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/GammaRay.desktop

%files
%doc README.txt
%license LICENSE*
%{_bindir}/gammaray
%{_qt5_libdir}/libgammaray_client.so.*
%{_qt5_libdir}/libgammaray_launcher.so.*
%{_qt5_libdir}/libgammaray_launcher_ui.so.*
%{_qt5_libdir}/libgammaray_kuserfeedback.so.*
%{_qt5_libdir}/gammaray/libexec/gammaray-launcher
%{_qt5_libdir}/gammaray/libexec/gammaray-client
%{_datadir}/applications/GammaRay.desktop
%{_datadir}/icons/hicolor/*/apps/GammaRay.png
%{_datadir}/metainfo/com.kdab.GammaRay.metainfo.xml
%{_mandir}/man1/gammaray.1.gz
%{_docdir}/gammaray/gammaray-api.qch
%{_docdir}/gammaray/gammaray-manual.qch
%{_docdir}/gammaray/gammaray.qhc
%lang(de) %{_datadir}/gammaray/translations/gammaray_de.qm
%lang(en) %{_datadir}/gammaray/translations/gammaray_en.qm

%files qt5
%{_qt5_libdir}/libgammaray_ui-%{qt5_target}.so.*
%{_qt5_libdir}/libgammaray_common-%{qt5_target}.so.*
%{_qt5_libdir}/libgammaray_core-%{qt5_target}.so.*
%{_qt5_libdir}/libgammaray_kitemmodels-%{qt5_target}.so.*
%{_qt5_libdir}/gammaray/%{gammaray_ver}/%{qt5_target}/

%files devel
%{_includedir}/gammaray
%{_qt5_libdir}/libgammaray_client.so
%{_qt5_libdir}/libgammaray_launcher.so
%{_qt5_libdir}/libgammaray_launcher_ui.so
%{_qt5_libdir}/libgammaray_kuserfeedback.so
%{_qt5_libdir}/libgammaray_ui-%{qt5_target}.so
%{_qt5_libdir}/libgammaray_common-%{qt5_target}.so
%{_qt5_libdir}/libgammaray_core-%{qt5_target}.so
%{_qt5_libdir}/libgammaray_kitemmodels-%{qt5_target}.so
%{_libdir}/cmake/GammaRay/
%{_qt5_archdatadir}/mkspecs/modules/qt_GammaRayCommon.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_GammaRayCore.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_GammaRayUi.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_GammaRayClient.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_GammaRayKItemModels.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_GammaRayLauncher.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_GammaRayLauncherUi.pri

%ldconfig_scriptlets
%ldconfig_scriptlets qt5


%changelog
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
