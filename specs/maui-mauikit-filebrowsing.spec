Name:          maui-mauikit-filebrowsing
Version:       4.0.0
Release:       3%{?dist}
License:       CC0-1.0 AND BSD-2-Clause AND LGPL-2.1-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later
Summary:       MauiKit File Browsing utilities and controls
URL:           https://invent.kde.org/maui/mauikit-filebrowsing/

Source0:       https://download.kde.org/stable/maui/mauikit-filebrowsing/%{version}/mauikit-filebrowsing-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Network)

BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)

BuildRequires: cmake(MauiKit4)

%description
FileBrowsing is a MauiKit Framework to work with local and remote files.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.


%prep
%autosetup -p1 -n mauikit-filebrowsing-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang mauikitfilebrowsing

%files -f mauikitfilebrowsing.lang
%license LICENSES/*
%{_kf6_libdir}/libMauiKitFileBrowsing4.so.4
%{_kf6_libdir}/libMauiKitFileBrowsing4.so.%{version}
%{_kf6_qmldir}/org/mauikit/filebrowsing/

%files devel
%{_includedir}/MauiKit4/FileBrowsing/
%{_kf6_libdir}/cmake/MauiKitFileBrowsing4/
%{_kf6_libdir}/libMauiKitFileBrowsing4.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 24 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-2
- Moved a file from devel subpackage

* Tue May 14 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
