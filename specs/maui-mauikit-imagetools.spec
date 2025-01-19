Name:          maui-mauikit-imagetools
Version:       4.0.0
Release:       6%{?dist}
License:       GPL-3.0-or-later AND BSD-2-Clause AND GPL-2.0-only AND LGPL-2.1-or-later AND LGPL-2.1-only AND LGPL-2.0-or-later AND CC0-1.0 AND LGPL-3.0-or-later AND GPL-3.0-only AND LGPL-3.0-only
Summary:       MauiKit Image Tools Components
URL:           https://invent.kde.org/maui/mauikit-imagetools/

Source0:       https://download.kde.org/stable/maui/mauikit-imagetools/%{version}/mauikit-imagetools-%{version}.tar.xz

# Apps depending on imagetools fail to start because of a path issue with some qml files
# https://invent.kde.org/maui/mauikit-imagetools/-/merge_requests/7
Patch0:        7.patch

# Doesn't build on i686.
ExcludeArch:   %{ix86}

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(exiv2)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)

BuildRequires: cmake(MauiKit4)
BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(Tesseract)
BuildRequires: cmake(OpenCV)

Requires:      %{name}-cities

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.

%package cities
Summary:        %{name} cities database
BuildArch: noarch

%description cities
Cities database required for geolocation for %{name}.

%prep
%autosetup -p1 -n mauikit-imagetools-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang mauikitimagetools

%files -f mauikitimagetools.lang
%license LICENSES/*
%{_kf6_libdir}/libMauiKitImageTools4.so.4
%{_kf6_libdir}/libMauiKitImageTools4.so.%{version}
%{_kf6_qmldir}/org/mauikit/imagetools/

%files devel
%{_kf6_libdir}/cmake/MauiKitImageTools4/
%{_kf6_libdir}/libMauiKitImageTools4.so
%{_includedir}/MauiKit4/FileBrowsing/imagetools_version.h
%{_includedir}/MauiKit4/ImageTools/

%files cities
%{_kf6_datadir}/org/mauikit/imagetools/cities.db

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 12 2024 Sandro Mani <manisandro@gmail.com> - 4.0.0-5
- Rebuild (tesseract)

* Fri Nov 08 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-4
- Apps depending on imagetools fail to start because of a path issue in qml
  files

* Wed Sep 25 2024 Michel Lind <salimma@fedoraproject.org> - 4.0.0-3
- Rebuild for tesseract-5.4.1-3 (soversion change from 5.4.1 to just 5.4)

* Sat Sep 21 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-2
- Disable i686 building, as it doesn't build on that arch

* Tue May 14 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
