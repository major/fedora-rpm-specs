Name:           kio-snapshot
Version:        1.0.0
Release:        1%{?dist}
Summary:        Integration of Btrfs filesystem snapshots for KDE apps

License:        CC-BY-SA-4.0 AND CC0-1.0 AND LGPL-2.0-or-later
URL:            https://invent.kde.org/system/kio-snapshot
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Solid)

BuildRequires:  pkgconfig(libbtrfsutil)

%description
Btrfs Filesystem snapshot integration for KDE applications.

%prep
%autosetup -p1

%conf
%cmake_kf6

%build
%cmake_build


%install
%cmake_install

%check
# Verification fails:
# https://bugs.kde.org/show_bug.cgi?id=524510
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml ||:

%files
%license LICENSES/*
%doc README.md
%{_kf6_qtplugindir}/kf6/kfileitemaction/snapshotfileitemaction.so
%{_kf6_qtplugindir}/kf6/kio/kio_snapshot.so
%{_kf6_metainfodir}/org.kde.kio_snapshot.metainfo.xml

%changelog
* Thu Aug 20 2026 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- Initial Release
