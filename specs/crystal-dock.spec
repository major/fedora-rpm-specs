%global short_version 2.14

Name:           crystal-dock
Summary:        Modern cross-desktop dock for the Linux Desktop
Version:        2.14.0
Release:        3%{?dist}

License:        GPL-3.0-only
URL:            https://github.com/dangvd/crystal-dock

Source0:        %{url}/archive/refs/tags/v%{short_version}.tar.gz

Patch0:         crystal-dock-fix-build-against-qt-6-10.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  cmake(LayerShellQt)

%description
Crystal Dock is a cool dock (desktop panel) for Linux desktop, with the
focus on attractive user interface, being simple and easy to customize,
and cross-desktop support.


%prep
%autosetup -p1 -n %{name}-%{short_version}


%build
cd src
%cmake
%cmake_build


%install
cd src
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/crystal-dock
%{_datadir}/applications/crystal-dock.desktop

%changelog
* Tue Sep 30 2025 Jan Grulich <jgrulich@redhat.com> - 2.14.0-3
- Rebuild (qt6)

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu May 22 2025 Steve Cossette <farchord@gmail.com> - 2.14.0-1
- 2.14.0
