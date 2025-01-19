Name:          maui-mauikit-accounts
Version:       4.0.0
Release:       2%{?dist}
License:       BSD-2-Clause AND LGPL-2.1-or-later AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later
Summary:       MauiKit utilities to handle User Accounts
URL:           https://invent.kde.org/maui/mauikit-accounts

Source0:       https://download.kde.org/stable/maui/mauikit-accounts/%{version}/mauikit-accounts-4.0.0.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Network)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)

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
%autosetup -p1 -n mauikit-accounts-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang mauikitaccounts

%files -f mauikitaccounts.lang
%license LICENSES/*
%{_kf6_libdir}/libMauiKitAccounts4.so.4
%{_kf6_libdir}/libMauiKitAccounts4.so.%{version}
%{_kf6_qmldir}/org/mauikit/accounts/

%files devel
%{_kf6_libdir}/libMauiKitAccounts4.so
%{_kf6_libdir}/cmake/MauiKitAccounts4/
%{_includedir}/MauiKit4/Accounts/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue May 14 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
