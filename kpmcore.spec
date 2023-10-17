%global unstable 0
%global kf5min 5.92
%global qt5min 5.15.2
%global kf6min 5.240.0
%global qt6min 6.4.0
%global sover 12

%if 0%{?fedora} >= 40
%global qt_maj_ver 6
%else
%global qt_maj_ver 5
%endif

Name:           kpmcore
Version:        23.08.2
Release:        %autorelease
Summary:        Library for managing partitions by KDE programs
License:        GPL-3.0-or-later AND MIT AND CC-BY-4.0 AND CC0-1.0
URL:            https://github.com/KDE/kpmcore
%if 0%{?unstable}
Source0:        http://download.kde.org/unstable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%else
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif

BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext

%if %{qt_maj_ver} == 6
BuildRequires:  kf6-kcoreaddons-devel >= %{kf6min}
BuildRequires:  kf6-ki18n-devel >= %{kf6min}
BuildRequires:  kf6-kwidgetsaddons-devel >= %{kf6min}
BuildRequires:  qt6-qtbase-devel >= %{qt6min}
%else
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5min}
BuildRequires:  kf5-ki18n-devel >= %{kf5min}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5min}
BuildRequires:  qt5-qtbase-devel >= %{qt5min}
%endif
BuildRequires:  kf%{qt_maj_ver}-rpm-macros

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid) >= 2.33.2
BuildRequires:  pkgconfig(polkit-qt%{qt_maj_ver}-1)

Requires:       e2fsprogs
Requires:       kf%{qt_maj_ver}-filesystem

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
Requires:       qt%{qt_maj_ver}-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}


%prep
%autosetup -p1

%build
%if %{qt_maj_ver} == 6
%cmake_kf6 \
    -DQT_MAJOR_VERSION="6"
%else
%cmake_kf5 \
    -DQT_MAJOR_VERSION="5"
%endif
%cmake_build


%install
%cmake_install
%find_lang %{name}
%find_lang %{name}._policy_


%files -f %{name}.lang -f %{name}._policy_.lang
%license LICENSES/*
%doc README.md
%if %{qt_maj_ver} == 6
%{_kf6_libdir}/libkpmcore.so.%{sover}
%{_kf6_libdir}/libkpmcore.so.%{version}
%{_kf6_qtplugindir}/kpmcore
%else
%{_kf5_libdir}/libkpmcore.so.%{sover}
%{_kf5_libdir}/libkpmcore.so.%{version}
%{_kf5_qtplugindir}/kpmcore
%endif
%{_libexecdir}/kpmcore_externalcommand
%{_datadir}/dbus-1/system.d/org.kde.kpmcore.*.conf
%{_datadir}/dbus-1/system-services/org.kde.kpmcore.*.service
%{_datadir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy

%files devel
%{_includedir}/%{name}/
%if %{qt_maj_ver} == 6
%{_kf6_libdir}/cmake/KPMcore
%{_kf6_libdir}/libkpmcore.so
%else
%{_kf5_libdir}/cmake/KPMcore
%{_kf5_libdir}/libkpmcore.so
%endif


%changelog
%autochangelog
