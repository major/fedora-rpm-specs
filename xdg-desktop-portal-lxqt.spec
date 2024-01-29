Name: xdg-desktop-portal-lxqt
Version: 0.5.0
Release: 2%{?dist}
Summary: A backend implementation for xdg-desktop-portal that is using Qt/KF5/libfm-qt
License: LGPL-2.0-or-later
URL: https://lxqt-project.org
Source0: https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires: make
BuildRequires: %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires: pkgconfig(lxqt) >= 1.1.0
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: qt5-qtbase-private-devel
BuildRequires: pkgconfig(libfm-qt)
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: gcc-c++
BuildRequires: libexif-devel
Requires: dbus-common
Requires: xdg-desktop-portal
Requires: libfm-qt

%description
%{summary}

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
	%{cmake_lxqt} -DBUILD_DOCUMENTATION=ON -DPULL_TRANSLATIONS=NO -S .. -B .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} -C %{_target_platform}

%files
%doc CHANGELOG README.md
%license LICENSE
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/lxqt.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.lxqt.service
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.lxqt.desktop
%{_libexecdir}/xdg-desktop-portal-lxqt

%changelog
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
