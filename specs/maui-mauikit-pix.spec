Name:          maui-mauikit-pix
Version:       4.0.0
Release:       2%{?dist}
License:       GPL-3.0-or-later AND BSD-3-Clause AND MIT
Summary:       Image gallery manager built on the maui framework
URL:           https://mauikit.org/apps/pix/

# Doesn't build on i686.
ExcludeArch:   %{ix86}

Source0:       https://download.kde.org/stable/maui/pix/%{version}/maui-pix-%{version}.tar.xz

# One license in LICENSES/ is no longer used and one was missing.
# https://invent.kde.org/maui/maui-pix/-/merge_requests/16
Patch0:        16.patch

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(MauiKitFileBrowsing4)
BuildRequires: cmake(MauiKitImageTools4)
BuildRequires: cmake(MauiKit4)
BuildRequires: pkgconfig(exiv2)

Requires:      hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -p1 -n maui-pix-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.pix.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang pix --with-man --with-qt --all-name

%files -f pix.lang
%license LICENSES/*
%{_datadir}/icons/hicolor/scalable/apps/pix.svg
%{_datadir}/applications/org.kde.pix.desktop
%{_metainfodir}/org.kde.pix.appdata.xml
%{_kf6_bindir}/pix

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 8 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
