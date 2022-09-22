Name:    ksystemstats
Version: 5.25.90
Release: 1%{?dist}
Summary: KSystemStats is a daemon that collects statistics about the running system.
 
# KDE e.V. may determine that future GPL versions are accepted
License: GPLv2 or GPLv3
URL:     https://invent.kde.org/plasma/%{name}
 
%global majmin %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
 
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libksysguard-devel >= %{majmin}
 
BuildRequires: kf5-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires: extra-cmake-modules >= 5.82
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5WindowSystem)
 
BuildRequires: cmake(KF5NetworkManagerQt)
 
BuildRequires: cmake(Qt5Widgets)
 
BuildRequires:  libnl3-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(libpcap)
 
%description
KSystemStats is a daemon that collects statistics about the running system.
 
%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.
 
 
%prep
%autosetup -n %{name}-%{version}


%build
%cmake_kf5

%cmake_build


%install
%cmake_install
%find_lang ksystemstats_plugins


%files -f ksystemstats_plugins.lang
%doc README.md
%license LICENSES/*
%{_kf5_bindir}/ksystemstats
%{_kf5_bindir}/kstatsviewer
%{_datadir}/dbus-1/services/org.kde.ksystemstats.service
%{_userunitdir}/plasma-ksystemstats.service
%{_qt5_plugindir}/ksystemstats/


%changelog
* Sat Sep 17 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.90-1
- 5.25.90

* Wed Sep 07 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.5-1
- 5.25.5

* Wed Aug 03 2022 Justin Zobel <justin@1707.io> - 5.25.4-1
- Update to 5.25.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.3-1
- 5.25.3

* Tue Jun 28 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.2-1
- 5.25.2

* Tue Jun 21 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.1-1
- 5.25.1

* Thu Jun 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.0-1
- 5.25.0

* Fri May 20 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.90-1
- 5.24.90

* Tue May 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.5-1
- 5.24.5

* Thu Mar 31 2022 Justin Zobel <justin@1707.io> - 5.24.4-1
- Update to 5.24.4

* Tue Mar 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.3-1
- 5.24.3

* Tue Feb 22 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.24.2-1
- 5.24.2

* Tue Feb 15 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.1-1
- 5.24.1

* Thu Feb 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.0-1
- 5.24.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.23.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.23.90-1
- 5.23.90

* Tue Jan 04 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.23.5-1
- 5.23.5

* Tue Dec 14 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.4-1
- 5.23.4

* Wed Nov 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.23.3-1
- 5.23.3

* Tue Oct 26 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.23.2-1
- 5.23.2

* Sat Oct 23 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.1-1
- 5.23.1

* Fri Oct 08 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.0-1
- 5.23.0
- Add BuildRequires: systemd-rpm-macros

* Fri Sep 17 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.22.90-1
- 5.22.90

* Tue Aug 31 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.5-1
- 5.22.5

* Tue Jul 27 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.4-1
- 5.22.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Onuralp SEZER <thudnerbirdtr@fedoraproject.org> - 5.22.3-1
- 5.22.3

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.2.1-1
- 5.22.2.1

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.2-1
- 5.22.2

* Tue Jun 15 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.1-1
- 5.22.1

* Tue Jun 08 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.0-1
- 5.22.0

* Tue May 18 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.21.90-2
- and comment about licensing
- .spec cosmetics

* Tue May 18 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.21.90-1
- Initial Package
