%global commit0 22cf331deb82116fea63fd8e6529b1b30022e0ec
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20211207

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags
%global _hardened_build 1

Name:           kiss
Version:        0~%{date}git%{shortcommit0}
Release:        4%{?dist}
Summary:        Initial setup for systems using Plasma
License:        GPLv3
URL:            https://invent.kde.org/system/%{name}
Source:         %{url}/-/archive/%{commit0}/kiss-%{commit0}.tar.bz2
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cracklib-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  systemd-rpm-macros

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit0}

%build
%{cmake_kf5}
%{cmake_build}

%install
%{cmake_install}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_scriptlets
%post
%systemd_post org.kde.initialsystemsetup.service

%preun
%systemd_preun org.kde.initialsystemsetup.service

%files
%{_kf5_bindir}/org.kde.initialsystemsetup
%{_unitdir}/org.kde.initialsystemsetup.service

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0~20211207git22cf331-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Marc Deop marcdeop@fedoraproject.org - 0~20211207git22cf331-1
- Initial Release

