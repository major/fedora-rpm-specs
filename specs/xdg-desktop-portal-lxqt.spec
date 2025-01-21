Name:          xdg-desktop-portal-lxqt
Version:       1.1.0
Release:       2%{?dist}
Summary:       A backend implementation for xdg-desktop-portal that is using Qt/KF5/libfm-qt
License:       LGPL-2.0-or-later
URL:           https://lxqt-project.org
Source0:       https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: qt6-qtbase-private-devel
BuildRequires: pkgconfig(libfm-qt6)
BuildRequires: cmake(KF6WindowSystem)

BuildRequires: pkgconfig(Qt5X11Extras)

BuildRequires: libexif-devel
Requires:      dbus-common
Requires:      xdg-desktop-portal
Requires:      libfm-qt-qt6

%description
%{summary}

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG README.md
%license LICENSE
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/lxqt.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.lxqt.service
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.lxqt.desktop
%{_datadir}/xdg-desktop-portal/lxqt-portals.conf
%{_libexecdir}/xdg-desktop-portal-lxqt

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- 1.1.0

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 1.0.2-2
- Rebuild (qt6)

* Tue Jul 16 2024 Steve Cossette <farchord@gmail.com> - 1.0.2-1
- 1.0.2

* Thu Apr 18 2024 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- 1.0.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Zamir SUN <sztsian@gmail.com> - 0.5.0-1
- Update version to 0.5.0

* Fri Jul 28 2023 Zamir SUN <sztsian@gmail.com> - 0.4.0-1
- Update version to 0.4.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 0.3.0-1
- Update version to 0.3.0

* Thu Sep 15 2022 Zamir SUN <sztsian@gmail.com> - 0.2.0-1
- Initial packaging
