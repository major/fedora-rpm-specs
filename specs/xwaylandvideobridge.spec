Name:           xwaylandvideobridge
Version:        0.4.0
Release:        8%{?dist}
Summary:        Utility to allow streaming Wayland windows to X applications

License:        (GPL-2.0-only or GPL-3.0-only) and LGPL-2.0-or-later and BSD-3-Clause
URL:            https://invent.kde.org/system/xwaylandvideobridge
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  cmake(KPipeWire) >= 6.0.0

Requires:       hicolor-icon-theme

%description
By design, X11 applications can't access window or screen contents
for wayland clients. This is fine in principle, but it breaks screen
sharing in tools like Discord, MS Teams, Skype, etc and more.

This tool allows us to share specific windows to X11 clients,
but within the control of the user at all times.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6 \
    -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_sysconfdir}/xdg/autostart/org.kde.%{name}.desktop


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 0.4.0-7
- Rebuild (qt6)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 0.4.0-5
- Rebuild (qt6)

* Wed Mar 13 2024 Marie Loise Nolden <loise@kde.org> - 0.4.0-4
- build with QT_MAJOR_VERSION=6
- precisely require kpipewire >= 6.0.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 0.4.0-3
- Rebuild (qt6)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0.4.0-1
- 0.4.0

* Mon Dec 04 2023 Alessandro Astone <ales.astone@gmail.com> - 0.3.0-4
- Do not start in an X11 session
- Opt out of session managment
- Skip the task switcher

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 0.3.0-3
- Rebuild (qt6)

* Sat Nov 18 2023 Alessandro Astone <ales.astone@gmail.com> - 0.3.0-2
- Build against Qt6/KF6

* Thu Nov 09 2023 Alessandro Astone <ales.astone@gmail.com> - 0.3.0-1
- Update to 0.3
- Autostart on login

* Fri Oct 27 2023 Alessandro Astone <ales.astone@gmail.com> - 0.2-1
- Update to tagged release 0.2

* Mon Sep 18 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20230917.9b27c3f-1
- Bump to new git snapshot

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20230504.3445aff-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20230504.3445aff-2
- Add dependency on hicolor-icon-theme

* Wed May 10 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20230504.3445aff-1
- Initial package
