Name:    libksane
Summary: SANE Library interface for KDE
Version: 24.02.0
Release: 1%{?dist}

License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/graphics/%{name}
Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gettext

BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KSaneCore)

BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KSaneCore6)

BuildRequires: pkgconfig(sane-backends)

%description
%{summary}.

%package qt5
Summary: Qt5 library providing logic to interface scanners
Requires: %{name}-common = %{version}-%{release}
Obsoletes: kf5-libksane < 24.01
Provides:  kf5-libksane = %{version}-%{release}
%description qt5
%{summary}.

%package qt5-devel
Summary: Development files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Widgets)
Obsoletes: kf5-libksane-devel < 24.01
Provides:  kf5-libksane-devel = %{version}-%{release}
%description qt5-devel
%{summary}.

%package qt6
Summary: Qt6 library providing logic to interface scanners
Requires: %{name}-common = %{version}-%{release}
%description qt6
%{summary}.

%package qt6-devel
Summary:  Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Widgets)
%description qt6-devel
%{summary}.

%package common
Summary: Files shared between the Qt5 and Qt6 versions of the library
Conflicts: kf5-libksane < 24.01
%description common
%{summary}.
Provides internationalization files.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%global _vpath_builddir %{_target_platform}-qt5
%cmake_kf5 -DBUILD_WITH_QT6=OFF
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%find_lang %{name} --all-name --with-html


%files common -f %{name}.lang
%doc AUTHORS
%license COPYING*
%license LICENSES/*
%{_datadir}/icons/hicolor/*/actions/*

%files qt5
%{_libdir}/libKF5Sane.so.{6,%{version}}
%{_datadir}/icons/hicolor/*/actions/*

%files qt5-devel
%{_includedir}/KF5/KSane/
%{_libdir}/libKF5Sane.so
%{_libdir}/cmake/KF5Sane/

%files qt6
%{_libdir}/libKSaneWidgets6.so.{6,%{version}}

%files qt6-devel
%{_includedir}/KSaneWidgets6/
%{_libdir}/libKSaneWidgets6.so
%{_libdir}/cmake/KSaneWidgets6/

%changelog
* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Wed Dec 13 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-2
- Explicit conflicts libksane-common

* Mon Dec 11 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-1
- Replaces kf5-libksane, providing both a qt5 and a qt6 build
