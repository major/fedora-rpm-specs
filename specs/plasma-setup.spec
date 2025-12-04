%global qt6_minver 6.6.0
%global kf6_minver 6.5.0

%global commit b8bc62355f0169aca6c1facfc73eb3b54207897c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20251201

%global orgname org.kde.plasmasetup

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags
%global _hardened_build 1

Name:           plasma-setup
Version:        0.1.0~%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Initial setup for systems using KDE Plasma
License:        (GPL-2.0-or-later or GPL-3.0-or-later) and GPL-2.0-or-later and GPL-3.0-or-later and (LGPL-2.0-or-later or LGPL-3.0-or-later) and (LGPL-2.1-or-later or LGPL-3.0-or-later) and LGPL-2.1-or-later and BSD-2-Clause and CC0-1.0
URL:            https://invent.kde.org/plasma/%{name}
Source:         %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.bz2

Patch:          https://invent.kde.org/plasma/plasma-setup/-/merge_requests/55.patch

BuildRequires:  cmake(Qt6Core) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_minver}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_minver}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_minver}
BuildRequires:  cmake(KF6I18n) >= %{kf6_minver}
BuildRequires:  cmake(KF6Package) >= %{kf6_minver}
BuildRequires:  cmake(KF6Auth) >= %{kf6_minver}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_minver}
BuildRequires:  cmake(KF6Config) >= %{kf6_minver}
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cracklib-devel
BuildRequires:  extra-cmake-modules >= %{kf6_minver}
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  systemd-rpm-macros
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  qt6qml(org.kde.plasma.private.kcm_keyboard)

Requires:       qt6qml(org.kde.plasma.private.kcm_keyboard)

Requires:       dbus-common
Requires:       kf6-filesystem
Requires:       kf6-kauth

# Renamed from KDE Initial System Setup / kiss
Obsoletes:      kiss < %{version}-%{release}
Provides:       kiss = %{version}-%{release}
Provides:       kiss%{?_isa} = %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Do not check .so files in an application-specific library directory
%global __provides_exclude_from ^%{_kf6_qmldir}/org/kde/plasmasetup/.*\\.so.*$


%description
%{summary}.


%prep
%autosetup -n %{name}-%{commit} -S git_am


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{orgname} --all-name
rm -fv %{buildroot}%{_kf6_libdir}/libcomponentspluginplugin.a


%preun
%systemd_preun %{name}.service


%post
%systemd_post %{name}.service


%postun
%systemd_postun %{name}.service


%files -f %{orgname}.lang
%license LICENSES/*
%config(noreplace) %{_sysconfdir}/xdg/plasmasetuprc
%{_libexecdir}/%{name}*
%{_kf6_libexecdir}/kauth/%{name}*
%{_kf6_qmldir}/org/kde/plasmasetup/
%{_kf6_plugindir}/packagestructure/plasmasetup.so
%{_kf6_datadir}/plasma/packages/%{orgname}.*/
%license %{_kf6_datadir}/plasma/packages/%{orgname}.finished/contents/ui/konqi-calling.png.license
%{_unitdir}/%{name}*
%{_sysusersdir}/%{name}*
%{_tmpfilesdir}/%{name}*
%{_datadir}/dbus-1/*/%{orgname}.*
%{_datadir}/polkit-1/actions/%{orgname}.*
%{_datadir}/polkit-1/rules.d/%{name}*
%{_datadir}/qlogging-categories6/plasmasetup.categories
%{_datadir}/%{name}/


%changelog
* Tue Dec 02 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0~20251201gitb8bc623-1
- Bump to new git snapshot
- Add patch to handle existing users on firstboot setup

* Sun Nov 30 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0~20251130git84b5d3c-1
- Bump to new git snapshot

* Tue Nov 25 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0~20251123git180844b-2
- Add patch to change self-disable behavior to use a flag file

* Mon Nov 24 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0~20251123git180844b-1
- Bump to new git snapshot

* Sat Sep 27 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0~20250926giteeeb5a1-1
- Bump to new git snapshot
- Rename to plasma-setup

* Sun Sep 07 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0~20250906git69c6007-2
- Drop i686 support as required dependencies are no longer available

* Sat Sep 06 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0~20250906git69c6007-1
- Bump to new git snapshot

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

* Tue Dec 07 2021 Marc Deop <marcdeop@fedoraproject.org> - 0~20211207git22cf331-1
- Initial Release

