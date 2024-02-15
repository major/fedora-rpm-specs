%global commit f36bf16487d4c1b4dcdc3cce520d0fafe17d19df
%global commitdate 20240131
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global qt6minver 6.4.0
%global kf6minver 5.240.0

Name:           krdp
Version:        5.27.80~git%{commitdate}.%{shortcommit}
Release:        4%{?dist}
Summary:        Library for creating an RDP server

License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/plasma/krdp
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  extra-cmake-modules >= %{kf6minver}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6minver}
BuildRequires:  cmake(Qt6Core) >= %{qt6minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6minver}
BuildRequires:  cmake(Qt6Network) >= %{qt6minver}
BuildRequires:  cmake(Qt6DBus) >= %{qt6minver}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6minver}
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
Requires:       /usr/bin/winpr-makecert

%description
%{summary}.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%package server
Summary:        Simple RDP server using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       /usr/bin/openssl

%description server
%{summary}.


%prep
%autosetup -n %{name}-%{commit} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/LGPL-*.txt LICENSES/LicenseRef-KDE-*
%doc README.md
%{_kf6_libdir}/libKRdp.so.5{,.*}

%files devel
%{_kf6_libdir}/libKRdp.so
%{_kf6_libdir}/cmake/KRdp/

%files server
%{_kf6_bindir}/krdpserver
%{_kf6_datadir}/applications/org.kde.krdp.desktop
%{_kf6_datadir}/qlogging-categories6/krdp.categories


%changelog
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
