Name:          maui-mauikit-texteditor
Version:       4.0.0
Release:       2%{?dist}
License:       BSD-2-Clause AND LGPL-2.1-or-later AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later AND BSD-3-Clause
Summary:       MauiKit Text Editor components
URL:           https://invent.kde.org/maui/mauikit-texteditor/

Source0:       https://download.kde.org/stable/maui/mauikit-texteditor/%{version}/mauikit-texteditor-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Qml)

BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)

BuildRequires: cmake(MauiKit4)

%description
MauiKitTextEditor is a set of QtQuick components providing basic text editing
capabilities.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.

%prep
%autosetup -p1 -n mauikit-texteditor-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang mauikittexteditor

%files -f mauikittexteditor.lang
%license LICENSES/*
%{_kf6_libdir}/libMauiKitTextEditor4.so.4
%{_kf6_libdir}/libMauiKitTextEditor4.so.%{version}
%{_kf6_qmldir}/org/mauikit/texteditor/

%files devel
%{_kf6_libdir}/cmake/MauiKitTextEditor4/
%{_includedir}/MauiKit4/TextEditor/
%{_kf6_libdir}/libMauiKitTextEditor4.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue May 14 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
