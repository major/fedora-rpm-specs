%global gitdate 20231011.024115
%global cmakever 5.240.0
%global commit0 17e9362d66fa6fa6808b881fac7ac4dbe4cfe594
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kparts

Name:    kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for KParts

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  pkgconfig(xkbcommon)
Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 3 solution for KParts

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6KIO)
Requires:       cmake(KF6TextWidgets)
Requires:       cmake(KF6XmlGui)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html
# create/own parts plugin dir
mkdir -p %{buildroot}%{_kf6_plugindir}/parts/

%files -f %{name}.lang
%doc README.md AUTHORS
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Parts.so.*
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%dir %{_kf6_plugindir}/parts/

%files devel
%{_kf6_includedir}/KParts/
%{_kf6_libdir}/libKF6Parts.so
%{_kf6_libdir}/cmake/KF6Parts/
%dir %{_kf6_datadir}/kdevappwizard/
%dir %{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_datadir}/kdevappwizard/templates/kparts6-app.tar.bz2

%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.024115.17e9362-1
- Initial release
