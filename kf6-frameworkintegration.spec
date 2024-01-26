%global framework frameworkintegration

Name:    kf6-%{framework}
Version: 5.248.0
Release: 3%{?dist}
Summary: KDE Frameworks 6 Tier 4 workspace and cross-framework integration plugins
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Package)
BuildRequires:  kf6-rpm-macros
BuildRequires:  libXcursor-devel
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
# Package requires at least v1.0 of AppStreamQt which isn't out yet. This is optional,
# and will be enabled once available.
# BuildRequires:  cmake(AppStreamQt) >= 1.0
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  cmake(KF6ColorScheme)
Requires:  kf6-filesystem

%description
Framework Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

Applications do not need to link to this directly.

%package        libs
Summary:        Runtime libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6IconThemes)
Requires:       cmake(KF6ConfigWidgets)

%description    devel
The %{name}-devel package contains files to develop for %{name}.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/knotifications6/plasma_workspace.notifyrc
%dir %{_kf6_libexecdir}/kpackagehandlers
%{_kf6_libexecdir}/kpackagehandlers/knshandler

%files libs
%{_kf6_libdir}/libKF6Style.so.*
%{_kf6_plugindir}/FrameworkIntegrationPlugin.so
# Version in fedora is too old, uncomment when it is updated
#%%{_kf6_libexecdir}/kpackagehandlers/appstreamhandler

%files devel
%{_kf6_includedir}/FrameworkIntegration/
%{_kf6_includedir}/KStyle/
%{_kf6_libdir}/libKF6Style.so
%{_kf6_libdir}/cmake/KF6FrameworkIntegration/

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Wed Dec 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.247.0-1
- 5.247.0

* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 5.246.0-1
- Update to 5.246.0

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231003.064310.c062482-2
- Rebuild (qt6)

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.064310.c062482-1
- Initial release
