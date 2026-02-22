%bcond qt5 %[!(0%{?rhel} >= 10)]

%global sover 2.4

Name:           kddockwidgets
Version:        2.4.0
Release:        5%{?dist}
Summary:        Qt dock widget library

License:        GPL-3.0-only AND GPL-2.0-only AND BSD-3-Clause
URL:            https://github.com/KDAB/KDDockWidgets
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
%if %{with qt5}
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  qt5-qtbase-private-devel
%endif
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  cmake(spdlog)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(nlohmann_json)

# .qch generation
BuildRequires:  doxygen
BuildRequires:  cmake(Qt6ToolsTools)

%{?_qt5:Requires:       %{_qt5}%{?_isa} = %{_qt5_version}}

%description
Qt dock widget library written by KDAB, suitable for replacing QDockWidget
and implementing advanced functionalities missing in Qt.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        qt6
Summary:        Qt dock widget library for Qt 6

%{?_qt6:Requires:       %{_qt6}%{?_isa} = %{_qt6_version}}

%description    qt6
%{description}

%package        qt6-devel
Summary:        Development files for %{name}-qt6

Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
%description    qt6-devel
The %{name}-qt6-devel package contains libraries and header files for
developing applications that use %{name}-qt6.


%prep
%autosetup -n KDDockWidgets-%{version}


%build
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DECM_MKSPECS_INSTALL_DIR=%{_qt5_archdatadir}/mkspecs/modules \
    -DKDDockWidgets_QT6=OFF
%cmake_build
%endif

%global _vpath_builddir %{_target_platform}-qt6
# qhelpgenerator needs to be in $PATH to be detected
export PATH=$(%{_qt6_qmake} -query QT_HOST_LIBEXECS):$PATH
%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DECM_MKSPECS_INSTALL_DIR=%{_qt6_archdatadir}/mkspecs/modules \
    -DKDDockWidgets_QT6=ON \
    -DKDDockWidgets_DOCS=ON
%cmake_build

%install
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
rm -r %{buildroot}%{_datadir}/doc
%endif

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
mkdir -p %{buildroot}%{_qt6_docdir}
mv %{buildroot}%{_docdir}/KDDockWidgets-qt6/*.qch %{buildroot}%{_qt6_docdir}/
mv %{buildroot}%{_docdir}/KDDockWidgets-qt6/*.tags %{buildroot}%{_qt6_docdir}/
rm -r %{buildroot}%{_datadir}/doc/KDDockWidgets-qt6

%if %{with qt5}
%files
%license LICENSES/* LICENSE.txt
%doc CONTRIBUTORS.txt Changelog README.md
%{_libdir}/libkddockwidgets.so.%{sover}*
%{_libdir}/libkddockwidgets.so.3

%files devel
%{_includedir}/kddockwidgets
%{_libdir}/cmake/KDDockWidgets
%{_libdir}/libkddockwidgets.so
%{_qt5_archdatadir}/mkspecs/modules/qt_KDDockWidgets.pri
%endif

%files qt6
%license LICENSES/* LICENSE.txt
%doc CONTRIBUTORS.txt Changelog README.md
%{_libdir}/libkddockwidgets-qt6.so.%{sover}*
%{_libdir}/libkddockwidgets-qt6.so.3
%{_qt6_docdir}/kddockwidgets.tags

%files doc
%{_qt6_docdir}/kddockwidgets-api.qch

%files qt6-devel
%{_includedir}/kddockwidgets-qt6
%{_libdir}/cmake/KDDockWidgets-qt6
%{_libdir}/libkddockwidgets-qt6.so
%{_qt6_archdatadir}/mkspecs/modules/qt_KDDockWidgets.pri



%changelog
* Fri Feb 20 2026 Yaakov Selkowitz <yselkowi@redhat.com> - 2.4.0-5
- Disable qt5 for EPEL 10+

* Wed Feb 11 2026 Jan Grulich <jgrulich@redhat.com> - 2.4.0-4
- Rebuild (qt6)

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Nov 29 2025 Marie Loise Nolden <loise@kde.org> - 2.4.0-2
- add qch docs for Qt Creator/KDevelop

* Sun Nov 16 2025 Steve Cossette <farchord@gmail.com> - 2.4.0-1
- 2.4.0

* Tue Nov 04 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-29
- Rebuild (qt5)

* Thu Oct 30 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-28
- Rebuild (qt6)

* Wed Oct 08 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-27
- Rebuild (qt6)

* Tue Sep 30 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-26
- Rebuild (qt6)

* Mon Sep 01 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-25
- Rebuild (qt6)

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jun 06 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-23
- Rebuild (qt6)

* Mon May 26 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-22
- Rebuild (qt5)

* Thu Apr 03 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 1.7.0-21
- Rebuild (qt6)

* Tue Mar 25 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-20
- Rebuild (qt6)

* Mon Feb 03 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-19
- Rebuild (qt6)

* Wed Jan 22 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-18
- Rebuild (qt5)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Jan Grulich <jgrulich@redhat.com> - 1.7.0-16
- Rebuild (qt5)

* Wed Dec 11 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-15
- Rebuild (qt6)

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-14
- Rebuild (qt6)

* Thu Sep 05 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-13
- Rebuild (qt5)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Vasiliy Glazov <vascom2@gmail.com> - 1.7.0-11
- Rebuild (qt6)

* Thu May 30 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-10
- Rebuild (qt5)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-9
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-8
- Rebuild (qt6)

* Fri Mar 15 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-7
- Rebuild (qt5)

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-6
- Rebuild (qt6)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-3
- Rebuild (qt5)

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 1.7.0-2
- Rebuild (qt6)

* Tue Oct 31 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-13
- Rebuild (qt6)

* Mon Oct 09 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-12
- Rebuild (qt5)

* Thu Oct 05 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-11
- Rebuild (qt6)

* Mon Jul 24 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-10
- Rebuild (qt6)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-8
- Rebuild for qtbase private API version change

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-7
- Rebuild for qtbase private API version change

* Wed Jun 14 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-6
- Rebuild (qt5)

* Fri May 26 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-5
- Rebuild (qt6)

* Fri Apr 14 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.6.0-3
- Rebuild for new Qt 5 version

* Tue Apr 11 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.6.0-3
- Add Qt6 version

* Tue Mar 28 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.6.0-2
- Pin Qt5 version

* Fri Mar 24 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.6.0-1
- Initial packaging.
