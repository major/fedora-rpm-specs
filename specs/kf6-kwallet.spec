%global framework kwallet

Name:    kf6-%{framework}
Version: 6.11.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for password management

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6ConfigWidgets)

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(Gpgmepp)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf6-filesystem
Requires:       pinentry-gui

%description
KWallet is a secure and unified container for user passwords.

%package        libs
Summary:        KWallet framework libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    libs
Provides API to access KWallet data from applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kwallet-query
%{_kf6_bindir}/kwalletd6
%{_kf6_datadir}/applications/org.kde.kwalletd6.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.kwalletd5.service
%{_kf6_datadir}/dbus-1/services/org.kde.kwalletd6.service
%{_kf6_datadir}/knotifications6/kwalletd6.notifyrc
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_datadir}/xdg-desktop-portal/portals/kwallet.portal
%{_mandir}/man1/kwallet-query.1*


%files libs
%{_kf6_libdir}/libKF6Wallet.so.*
%{_libdir}/libKF6WalletBackend.so.*

%files devel
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.KWallet.xml
%{_kf6_includedir}/KWallet/
%{_kf6_libdir}/cmake/KF6Wallet/
%{_kf6_libdir}/libKF6Wallet.so
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Fri Feb 07 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.11.0-1
- 6.11.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 03 2025 Steve Cossette <farchord@gmail.com> - 6.10.0-1
- 6.10.0

* Sat Dec 14 2024 Steve Cossette <farchord@gmail.com> - 6.9.0-1
- 6.9.0

* Sat Nov 02 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.8.0-1
- 6.8.0

* Fri Oct 04 2024 Steve Cossette <farchord@gmail.com> - 6.7.0-1
- 6.7.0

* Mon Sep 16 2024 Steve Cossette <farchord@gmail.com> - 6.6.0-1
- 6.6.0

* Sat Aug 10 2024 Steve Cossette <farchord@gmail.com> - 6.5.0-1
- 6.5.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.0-1
- 6.4.0

* Sat Jun 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Fri May 24 2024 Steve Cossette <farchord@gmail.com> - 6.2.1-1
- 6.2.1

* Sat May 04 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Wed Apr 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Sat Mar 09 2024 Marie Loise Nolden <loise@kde.org> - 6.0.0-2
- add missing BuildArch: noarch to -doc package

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.249.0-1
- 5.249.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 5.247.0-2
- add doc package for KF6 API

* Wed Dec 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.247.0-1
- 5.247.0

* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 5.246.0-1
- Update to 5.246.0

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sun Oct 15 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20231012.021308.7a2c863-1

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.213013.7c91f3d-1
- Initial Release
