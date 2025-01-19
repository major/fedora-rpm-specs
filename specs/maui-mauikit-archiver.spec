Name:          maui-mauikit-archiver
Version:       4.0.0
Release:       3%{?dist}
# Ignored the Mainpage.dox's LGPL-2.0-or-later as it's not used by us in any way
License:       LGPL-2.1-or-later AND BSD-2-Clause AND GPL-3.0-or-later
Summary:       Maui plugin for online archived/compressed files management
URL:           https://invent.kde.org/maui/mauikit-archiver/

Source0:       https://download.kde.org/stable/maui/mauikit-archiver/%{version}/mauikit-archiver-%{version}.tar.xz

# Added licenses that are missing from upstream,
# and removing unused license
# https://invent.kde.org/maui/mauikit-archiver/-/merge_requests/1
Patch0:        licenses.patch

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Network)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)

BuildRequires: cmake(MauiKit4)
BuildRequires: cmake(MauiKitFileBrowsing4)

%description
%{summary}.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.


%prep
%autosetup -p1 -n mauikit-archiver-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
# Workaround https://invent.kde.org/maui/index-fm/-/issues/76
# Thanks to Onuralp!
sed -e '/prefer/d' -i %{buildroot}%{_kf6_qmldir}/org/mauikit/archiver/qmldir

%files
%license LICENSES/*
%{_kf6_qmldir}/org/mauikit/archiver/
%{_kf6_libdir}/libMauiKitArchiver4.so.4
%{_kf6_libdir}/libMauiKitArchiver4.so.%{version}

%files devel
%{_kf6_libdir}/cmake/MauiKitArchiver4/
%{_includedir}/MauiKit4/Accounts/archiver_version.h
%{_kf6_libdir}/libMauiKitArchiver4.so
%{_includedir}/MauiKit4/Archiver/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 24 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-2
- Fix for https://invent.kde.org/maui/index-fm/-/issues/76 (Obtained from Arch)

* Tue May 14 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
