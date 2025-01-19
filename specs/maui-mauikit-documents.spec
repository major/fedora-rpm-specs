Name:          maui-mauikit-documents
Version:       4.0.0
Release:       3%{?dist}
License:       MIT AND GPL-3.0-or-later AND LGPL-2.0-or-later AND CC0-1.0 AND BSD-2-Clause AND LGPL-2.1-or-later
Summary:       MauiKit QtQuick plugins for text editing
URL:           https://invent.kde.org/maui/mauikit-documents/

Source0:       https://download.kde.org/stable/maui/mauikit-documents/%{version}/mauikit-documents-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Concurrent)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake(MauiKit4)
BuildRequires: poppler-qt6-devel

%description
%{summary}.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.


%prep
%autosetup -p1 -n mauikit-documents-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang mauikitdocuments

%files -f mauikitdocuments.lang
%license LICENSES/*
%{_kf6_qmldir}/org/mauikit/documents/
%{_kf6_libdir}/libMauiKitDocuments4.so.4
%{_kf6_libdir}/libMauiKitDocuments4.so.%{version}

%files devel
%{_includedir}/MauiKit4/Documents/
%{_kf6_libdir}/cmake/MauiKitDocuments4/
%{_kf6_libdir}/libMauiKitDocuments4.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 4.0.0-2
- Rebuild (qt6)

* Tue May 14 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
