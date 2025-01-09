Name:    kosmindoormap
Version: 24.12.1
Release: 1%{?dist}
Summary: OSM multi-floor indoor map renderer

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND MIT AND ODbL-1.0
URL:     https://invent.kde.org/libraries/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  zlib-devel
BuildRequires:  cmake(KOpeningHours)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  osmctools
BuildRequires:  rsync
BuildRequires:  protobuf-devel
BuildRequires:  openssl-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  protobuf-lite-devel

BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(KOpeningHours)

Requires:       kf6-filesystem

%description
A library and QML component for rendering multi-level OSM indoor
maps of for example a (large) train station.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKOSM.so.*
%{_kf6_libdir}/libKOSMIndoorMap.so.*
%{_qt6_qmldir}/org/kde/kosmindoormap/
%{_qt6_qmldir}/org/kde/osm/editorcontroller/libkosmeditorcontrollerplugin.so
%{_qt6_qmldir}/org/kde/osm/editorcontroller/qmldir
%{_qt6_qmldir}/org/kde/osm/editorcontroller/kde-qmlmodule.version
%{_qt6_qmldir}/org/kde/osm/editorcontroller/kosmeditorcontrollerplugin.qmltypes
%{_datadir}/qlogging-categories6/org_kde_kosmindoormap.categories
%{_qt6_qmldir}/org/kde/kosmindoorrouting/
%{_kf6_libdir}/libKOSMIndoorRouting.so.*

%files devel
%{_includedir}/KOSMIndoorMap/
%{_includedir}/kosm/
%{_includedir}/kosmindoormap/
%{_includedir}/kosmindoormap_version.h
%{_includedir}/KOSM/
%{_includedir}/KOSMIndoorRouting/
%{_includedir}/kosmindoorrouting/
%{_kf6_libdir}/cmake/KOSMIndoorMap/
%{_kf6_libdir}/libKOSM.so
%{_kf6_libdir}/libKOSMIndoorMap.so
%{_kf6_libdir}/libKOSMIndoorRouting.so

%changelog
* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 24.08.2-2
- Rebuild (qt6)

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 24.02.1-2
- Rebuild (qt6)

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 24.01.95-2
- Rebuild (qt6)

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Mon Dec 18 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
