%global unstable 0
%global kf5min 5.90
%global qtmin 5.15.0
%global sover 12

Name:           kpmcore
Version:        22.12.1
Release:        2%{?dist}
Summary:        Library for managing partitions by KDE programs
License:        GPLv3+
URL:            https://github.com/KDE/kpmcore
%if 0%{?unstable}
Source0:        http://download.kde.org/unstable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%else
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif

BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5min}
BuildRequires:  kf5-ki18n-devel >= %{kf5min}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5min}
BuildRequires:  qt5-qtbase-devel >= %{qtmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid) >= 2.33.2
BuildRequires:  pkgconfig(polkit-qt5-1)

Requires:       e2fsprogs
Requires:       kf5-filesystem

Recommends:     dosfstools
Recommends:     exfatprogs
Recommends:     f2fs-tools
Recommends:     fatresize
Recommends:     hfsutils
Recommends:     hfsplus-tools
Recommends:     jfsutils
Recommends:     nilfs-utils
Recommends:     ocfs2-tools
Recommends:     udftools

%description
KPMcore contains common code for managing partitions by KDE Partition Manager 
and other KDE projects


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}


%prep
%autosetup -p1

%build
%cmake_kf5
%cmake_build


%install
%cmake_install
%find_lang %{name}
%find_lang %{name}._policy_


%files -f %{name}.lang -f %{name}._policy_.lang
%license LICENSES/*
%doc README.md
%{_kf5_libdir}/libkpmcore.so.%{sover}
%{_kf5_libdir}/libkpmcore.so.%{version}
%{_kf5_qtplugindir}/kpmcore
%{_libexecdir}/kpmcore_externalcommand
%{_datadir}/dbus-1/system.d/org.kde.kpmcore.*.conf
%{_datadir}/dbus-1/system-services/org.kde.kpmcore.*.service
%{_datadir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy

%files devel
%{_includedir}/%{name}/
%{_kf5_libdir}/cmake/KPMcore
%{_kf5_libdir}/libkpmcore.so


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

%autochangelog
