
%global qt_module qtwayland

#global unstable 1
%if 0%{?unstable}
%global prerelease rc2
%endif

%global examples 1

Summary: Qt6 - Wayland platform support and QtCompositor module
Name:    qt6-%{qt_module}
Version: 6.5.2
Release: 2%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

# Upstream patches

# Upstreamable patches


# filter qml provides
%global __provides_exclude_from ^%{_qt6_archdatadir}/qml/.*\\.so$

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-static
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel

BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libinput)

BuildRequires:  libXext-devel

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# BuildRequires: qt6-qtwayland-devel >= %{version}
%description examples
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6 -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%doc README
%license LICENSES/*
%{_qt6_libdir}/libQt6WaylandCompositor.so.6*
%{_qt6_libdir}/libQt6WaylandClient.so.6*
%{_qt6_libdir}/libQt6WaylandCompositor.so.6*
%{_qt6_libdir}/libQt6WaylandClient.so.6*
%{_qt6_libdir}/libQt6WaylandEglClientHwIntegration.so.6*
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.so.6*
%{_qt6_libdir}/libQt6WlShellIntegration.so.6*
%{_qt6_plugindir}/wayland-decoration-client/
%{_qt6_plugindir}/wayland-graphics-integration-server
%{_qt6_plugindir}/wayland-graphics-integration-client
%{_qt6_plugindir}/wayland-shell-integration
%{_qt6_plugindir}/platforms/libqwayland-egl.so
%{_qt6_plugindir}/platforms/libqwayland-generic.so
#{_qt6_plugindir}/platforms/libqwayland-xcomposite-egl.so
#{_qt6_plugindir}/platforms/libqwayland-xcomposite-glx.so
%{_qt6_qmldir}/QtWayland/

%files devel
%{_qt6_libexecdir}/qtwaylandscanner
%{_qt6_headerdir}/QtWaylandCompositor/
%{_qt6_headerdir}/QtWaylandClient/
%{_qt6_headerdir}/QtWaylandEglClientHwIntegration/
%{_qt6_headerdir}/QtWaylandEglCompositorHwIntegration/
%{_qt6_headerdir}/QtWlShellIntegration/
%{_qt6_headerdir}/QtWaylandGlobal/
%{_qt6_libdir}/libQt6WaylandCompositor.so
%{_qt6_libdir}/libQt6WaylandClient.so
%{_qt6_libdir}/libQt6WaylandEglClientHwIntegration.so
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.so
%{_qt6_libdir}/libQt6WlShellIntegration.so
%{_qt6_libdir}/libQt6WaylandCompositor.prl
%{_qt6_libdir}/libQt6WaylandClient.prl
%{_qt6_libdir}/libQt6WaylandEglClientHwIntegration.prl
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.prl
%{_qt6_libdir}/libQt6WlShellIntegration.prl
%{_qt6_libdir}/cmake/Qt6WaylandCompositor/Qt6WaylandCompositorConfig*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWaylandTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Gui/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6WaylandCompositor/
%{_qt6_libdir}/cmake/Qt6WaylandCompositor/
%dir %{_qt6_libdir}/cmake/Qt6WaylandClient/
%{_qt6_libdir}/cmake/Qt6WaylandClient/
%dir %{_qt6_libdir}/cmake/Qt6WaylandScannerTools/
%{_qt6_libdir}/cmake/Qt6WaylandScannerTools/
%dir %{_qt6_libdir}/cmake/Qt6WaylandEglClientHwIntegrationPrivate/
%{_qt6_libdir}/cmake/Qt6WaylandEglClientHwIntegrationPrivate/
%dir %{_qt6_libdir}/cmake/Qt6WaylandEglCompositorHwIntegrationPrivate/
%{_qt6_libdir}/cmake/Qt6WaylandEglCompositorHwIntegrationPrivate/
%dir %{_qt6_libdir}/cmake/Qt6WlShellIntegrationPrivate/
%{_qt6_libdir}/cmake/Qt6WlShellIntegrationPrivate/
%dir  %{_qt6_libdir}/cmake/Qt6WaylandGlobalPrivate/
%{_qt6_libdir}/cmake/Qt6WaylandGlobalPrivate/
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc


%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/wayland/
%endif

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 21 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.2-1
- 6.5.2

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-3
- Rebuild for qtbase private API version change

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-2
- Rebuild for qtbase private API version change

* Mon May 22 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-1
- 6.5.1

* Tue Apr 04 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.0-1
- 6.5.0

* Thu Mar 23 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.3-1
- 6.4.3

* Tue Jan 31 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.2-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.2-1
- 6.4.2

* Wed Nov 23 2022 Jan Grulich <jgrulich@redhat.com> - 6.4.1-1
- 6.4.1

* Mon Oct 31 2022 Jan Grulich <jgrulich@redhat.com> - 6.4.0-1
- 6.4.0

* Fri Jul 29 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.1-4
- Do not take decoration shadows into account when placing popups

* Tue Jul 26 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.1-3
- Keep toplevel windows in the top left corner of the screen

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.1-1
- 6.3.1

* Wed May 25 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.0-2
- Enable examples

* Wed Apr 13 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.0-1
- 6.3.0

* Fri Feb 25 2022 Jan Grulich <jgrulich@redhat.com> - 6.2.3-2
- Enable s390x builds

* Mon Jan 31 2022 Jan Grulich <jgrulich@redhat.com> - 6.2.3-1
- 6.2.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.2-1
- 6.2.2

* Fri Oct 29 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.1-1
- 6.2.1

* Thu Sep 30 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0-1
- 6.2.0

* Mon Sep 27 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc2-1
- 6.2.0 - rc2

* Sat Sep 18 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc-1
- 6.2.0 - rc

* Mon Sep 13 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~beta4-1
- 6.2.0 - beta4

* Thu Aug 12 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.2-1
- 6.1.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.1-1
- 6.1.1

* Thu May 06 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.0-1
- 6.1.0

* Mon Apr 05 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.3-1
- 6.0.3

* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0
- 6.0.0
