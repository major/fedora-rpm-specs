Name:           kunifiedpush
Version:        25.07.90
Release:        1%{?dist}
Summary:        UnifiedPush client library and distributor daemon
License:        BSD-2-Clause AND CC0-1.0 AND BSD-3-Clause AND LGPL-2.0-or-later
URL:            https://invent.kde.org/libraries/kunifiedpush

Source :        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils
# Qt dependencies
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6DBus)
# KF dependencies
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Solid)

BuildRequires:  openssl-devel

%description
%{summary}.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kcm_push_notifications

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_push_notifications.desktop

%files -f kcm_push_notifications.lang
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKUnifiedPush.so.%{version}
%{_kf6_libdir}/libKUnifiedPush.so.1
%{_bindir}/kunifiedpush-distributor
%{_sysconfdir}/xdg/autostart/org.kde.kunifiedpush-distributor.desktop
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_push_notifications.so
%{_kf6_datadir}/applications/kcm_push_notifications.desktop
%{_sysconfdir}/xdg/KDE/kunifiedpush-distributor.conf
%{_kf6_datadir}/qlogging-categories6/org_kde_kunifiedpush.categories
%{_userunitdir}/graphical-session.target.wants/kunifiedpush-distributor.service
%{_userunitdir}/kunifiedpush-distributor.service

%files devel
%{_kf6_libdir}/libKUnifiedPush.so
%{_includedir}/KUnifiedPush/
%{_kf6_libdir}/cmake/KUnifiedPush/

%changelog
* Fri Jul 25 2025 Steve Cossette <farchord@gmail.com> - 25.07.90-1
- 25.07.90

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 11 2025 Steve Cossette <farchord@gmail.com> - 25.07.80-1
- 25.07.80

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 25.04.3-1
- 25.04.3

* Wed Jun 04 2025 Steve Cossette <farchord@gmail.com> - 25.04.2-1
- 25.04.2

* Wed May 14 2025 Steve Cossette <farchord@gmail.com> - 25.04.1-1
- 25.04.1

* Sat Apr 12 2025 Steve Cossette <farchord@gmail.com> - 25.04.0-1
- 25.04.0

* Thu Mar 20 2025 Steve Cossette <farchord@gmail.com> - 25.03.80-1
- 25.03.80 (Beta)

* Tue Mar 04 2025 Steve Cossette <farchord@gmail.com> - 24.12.3-1
- 24.12.3

* Fri Feb 21 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-2
- Rebuild for ppc64le enablement

* Wed Feb 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Tue Nov 19 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 19 2024 Steve Cossette <farchord@gmail.com> - 1.0.0-2
- Bump for rebuild on f41/f40

* Sun Nov 3 2024 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- Initial build
