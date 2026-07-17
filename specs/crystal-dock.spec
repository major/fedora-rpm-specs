%global short_version 2.16

Name:           crystal-dock
Summary:        Modern cross-desktop dock for the Linux Desktop
Version:        2.16.0
Release:        2%{?dist}

License:        GPL-3.0-only
URL:            https://github.com/dangvd/crystal-dock

Source0:        %{url}/archive/refs/tags/v%{short_version}.tar.gz

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
* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Tue Jul 07 2026 Steve Cossette <farchord@gmail.com> - 2.16.0-1
- 2.16.0

* Thu May 14 2026 Jan Grulich <jgrulich@redhat.com> - 2.14.0-7
- Rebuild (qt6)

* Thu Apr 16 2026 Jan Grulich <jgrulich@redhat.com> - 2.14.0-6
- Rebuild (qt6)

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Sep 30 2025 Jan Grulich <jgrulich@redhat.com> - 2.14.0-3
- Rebuild (qt6)

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu May 22 2025 Steve Cossette <farchord@gmail.com> - 2.14.0-1
- 2.14.0
