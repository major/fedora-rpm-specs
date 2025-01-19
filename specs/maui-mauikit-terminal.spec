Name:          maui-mauikit-terminal
Version:       4.0.0
Release:       2%{?dist}
License:       LGPL-2.0-or-later AND GPL-3.0-or-later AND CC0-1.0 AND GPL-2.0-or-later
Summary:       Terminal support components for Maui applications
URL:           https://invent.kde.org/maui/mauikit-terminal

Source0:       https://download.kde.org/stable/maui/mauikit-terminal/%{version}/mauikit-terminal-4.0.0.tar.xz

# Licenses are missing. Created a PR upstream to add them to the project.
# https://invent.kde.org/maui/mauikit-terminal/-/merge_requests/1
Patch0:        licenses.patch

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Pty)

BuildRequires: cmake(MauiKit4)

%description
%{summary}.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.

%prep
%autosetup -p1 -n mauikit-terminal-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang mauikitterminal

%files -f mauikitterminal.lang
%license LICENSES/*
%{_kf6_qmldir}/org/mauikit/terminal/
%{_kf6_libdir}/libMauiKitTerminal4.so.%{version}
%{_kf6_libdir}/libMauiKitTerminal4.so.4

%files devel
%{_kf6_libdir}/cmake/MauiKitTerminal4/
%{_includedir}/MauiKit4/Terminal/
%{_kf6_libdir}/libMauiKitTerminal4.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue May 14 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
