%global qt6minver 6.6.0
%global kf6minver 6.2

Name:           krdp
Summary:        Desktop sharing using RDP
Version:        6.3.0
Release:        1%{?dist}

License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/plasma/krdp
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  extra-cmake-modules >= %{kf6minver}
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Crash) >= %{kf6minver}
BuildRequires:  cmake(KF6Config) >= %{kf6minver}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6minver}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6minver}
BuildRequires:  cmake(KF6I18n) >= %{kf6minver}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6minver}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6minver}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6minver}
BuildRequires:  cmake(Qt6Core) >= %{qt6minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6minver}
BuildRequires:  cmake(Qt6Network) >= %{qt6minver}
BuildRequires:  cmake(Qt6DBus) >= %{qt6minver}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6minver}
BuildRequires:  cmake(Qt6Keychain)
# Constrain to FreeRDP 2 for now: https://invent.kde.org/plasma/krdp/-/issues/15
BuildRequires:  (cmake(FreeRDP) >= 2.10 with cmake(FreeRDP) < 3)
BuildRequires:  (cmake(WinPR) >= 2.10 with cmake(WinPR) < 3)
BuildRequires:  (cmake(FreeRDP-Server) >= 2.10 with cmake(FreeRDP-Server) < 3)
BuildRequires:  cmake(KPipeWire) >= 5.27.80
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  /usr/bin/winpr-makecert
Requires:       /usr/bin/openssl

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-server < 6.0.90
Provides:       %{name}-server = %{version}-%{release}
Provides:       %{name}-server%{?_isa} = %{version}-%{release}

%description
%{summary}.


%package libs
Summary:        Library for creating an RDP server
Requires:       /usr/bin/winpr-makecert
Conflicts:      %{name} < 6.0.90
Conflicts:      %{name}-server < 6.0.90

%description libs
%{summary}.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html --all-name


%files -f %{name}.lang
%doc README.md
%{_kf6_bindir}/krdpserver
%{_kf6_datadir}/applications/kcm_krdpserver.desktop
%{_kf6_datadir}/applications/org.kde.krdp.desktop
%{_kf6_datadir}/qlogging-categories6/kcm_krdpserver.categories
%{_kf6_datadir}/qlogging-categories6/krdp.categories
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_krdpserver.so
%{_userunitdir}/app-org.kde.krdpserver.service

%files libs
%license LICENSES/LGPL-*.txt LICENSES/LicenseRef-KDE-*
%{_kf6_libdir}/libKRdp.so.6{,.*}

%files devel
%{_kf6_libdir}/libKRdp.so
%{_kf6_libdir}/cmake/KRdp/


%changelog
* Thu Feb 06 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Thu Jan 23 2025 Steve Cossette <farchord@gmail.com> - 6.2.91-1
- 6.2.91

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Steve Cossette <farchord@gmail.com> - 6.2.90-1
- Beta 6.2.90

* Tue Dec 31 2024 Steve Cossette <farchord@gmail.com> - 6.2.5-1
- 6.2.5

* Tue Nov 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.4-1
- 6.2.4

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 6.2.3-1
- 6.2.3

* Tue Oct 22 2024 Steve Cossette <farchord@gmail.com> - 6.2.2-1
- 6.2.2

* Tue Oct 15 2024 Steve Cossette <farchord@gmail.com> - 6.2.1-1
- 6.2.1

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 6.2.0-2
- Rebuild (qt6)

* Thu Oct 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Thu Sep 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.90-1
- 6.1.90

* Tue Sep 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.5-1
- 6.1.5

* Fri Aug 09 2024 Steve Cossette <farchord@gmail.com> - 6.1.4-1
- 6.1.4

* Wed Jul 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-3
- rebuilt

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-1
- 6.1.3

* Wed Jul 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.2-1
- 6.1.2

* Tue Jun 25 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.1-1
- 6.1.1

* Thu Jun 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Sat Jun 01 2024 Neal Gompa <ngompa@fedoraproject.org> - 6.0.90-2
- Fix required dependencies on winpr-makecert and openssl binaries

* Thu May 30 2024 Neal Gompa <ngompa@fedoraproject.org> - 6.0.90-1
- Rebase to 6.0.90
- Restructure package to more closely match krfb

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~git20240131.f36bf16-6
- Rebuild (qt6)

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~git20240131.f36bf16-5
- Rebuild (qt6)

* Tue Feb 13 2024 Alessandro Astone <ales.astone@gmail.com> - 5.27.80~git20240131.f36bf16-4
- krdp-server requires openssl binary

* Fri Feb 09 2024 Neal Gompa <ngompa@fedoraproject.org> - 5.27.80~git20240131.f36bf16-1
- Bump to new git snapshot
- Restrict to FreeRDP 2.x for now

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~git20231227.4931015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~git20231227.4931015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.27.80~git20231227.4931015-1
- Initial package
