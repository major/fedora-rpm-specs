%global upstream_name union

Name:           plasma-union
Version:        6.6.90
Release:        1%{?dist}
Summary:        A Qt style supporting both QtQuick and QtWidgets

License:        BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:            https://invent.kde.org/plasma/union

Source0: http://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{upstream_name}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{upstream_name}-%{version}.tar.xz.sig

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Config)

BuildRequires:  cmake(Breeze)
BuildRequires:  cmake(cxx-rust-cssparser)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{upstream_name}-%{version} -p1


%build
%cmake_kf6 -DBUILD_OUTPUT_QTWIDGETS=ON
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/union-ruleinspector
%{_kf6_libdir}/libUnion.so.6
%{_kf6_libdir}/libUnionQuickImpl.so.6
%{_kf6_libdir}/libUnionQuickStyle.so.6
%{_kf6_libdir}/libUnion.so.%{version}
%{_kf6_libdir}/libUnionQuickImpl.so.%{version}
%{_kf6_libdir}/libUnionQuickStyle.so.%{version}
%{_kf6_qtplugindir}/kf6/kirigami/platform/org.kde.union.so
%{_kf6_qtplugindir}/styles/UnionWidgetsStyle.so
%{_kf6_qtplugindir}/union/
%{_kf6_qmldir}/org/kde/union/
%{_kf6_qmldir}/org/kde/kirigami/styles/org.kde.union/
%{_kf6_datadir}/qlogging-categories6/union.categories
%{_kf6_datadir}/union/


%files devel
%{_includedir}/union/
%{_kf6_libdir}/cmake/Union/
%{_kf6_libdir}/libUnion.so
%{_kf6_libdir}/libUnionQuickImpl.so
%{_kf6_libdir}/libUnionQuickStyle.so

%changelog
* Tue May 12 2026 Steve Cossette <farchord@gmail.com> - 6.6.90-1
- Initial Release
