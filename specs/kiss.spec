%global qt6_minver 6.6.0
%global kf6_minver 6.5.0

%global commit ade79620520979709869b72cb9c03fd942963398
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20250524

%global orgname org.kde.initialsystemsetup

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags
%global _hardened_build 1

Name:           kiss
Version:        0.1.0~%{date}git%{shortcommit}
Release:        2%{?dist}
Summary:        Initial setup for systems using KDE Plasma
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/system/%{name}
Source:         %{url}/-/archive/%{commit}/kiss-%{shortcommit}.tar.bz2
BuildRequires:  cmake(Qt6Core) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_minver}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_minver}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_minver}
BuildRequires:  cmake(KF6I18n) >= %{kf6_minver}
BuildRequires:  cmake(KF6Package) >= %{kf6_minver}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_minver}
BuildRequires:  cmake(KF6Config) >= %{kf6_minver}
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cracklib-devel
BuildRequires:  extra-cmake-modules >= %{kf6_minver}
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

# Do not check .so files in an application-specific library directory
%global __provides_exclude_from ^%{_kf6_qmldir}/org/kde/initialsystemsetup/.*\\.so.*$


%description
%{summary}.


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

rm -fv %{buildroot}%{_kf6_libdir}/libcomponentspluginplugin.a


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{orgname}.*.xml


%files
%license LICENSES/*
%{_kf6_bindir}/kde-initial-system-setup
%{_kf6_qmldir}/org/kde/initialsystemsetup/
%{_kf6_plugindir}/packagestructure/kde_initialsystemsetup.so
%{_kf6_metainfodir}/%{orgname}.*.xml
%{_kf6_datadir}/plasma/packages/org.kde.initialsystemsetup.*/


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~20250524gitade7962-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 26 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0~20250524gitade7962-1
- Rebase to new rewrite

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0~20211207git22cf331-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Marc Deop marcdeop@fedoraproject.org - 0~20211207git22cf331-1
- Initial Release

