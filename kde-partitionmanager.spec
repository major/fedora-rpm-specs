%global base_name partitionmanager

%global unstable 0
%global kf5min 5.91
%global qt5min 5.15.2
%global kf6min 5.240.0
%global qt6min 6.4.0
%global kpmcoremin 23.08

%if 0%{?fedora} >= 40
%global qt_maj_ver 6
%else
%global qt_maj_ver 5
%endif

Name:           kde-partitionmanager
Version:        23.08.2
Release:        %autorelease
Summary:        KDE Partition Manager

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND CC-BY-4.0 AND CC0-1.0 AND GFDL-1.2-or-later
URL:            http://www.kde.org/applications/system/kdepartitionmanager/
%if 0%{?unstable}
Source0:        http://download.kde.org/unstable/release-service/%{version}/src/partitionmanager-%{version}.tar.xz
%else
Source0:        http://download.kde.org/stable/release-service/%{version}/src/partitionmanager-%{version}.tar.xz
%endif

BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kpmcore-devel >= %{kpmcoremin}

%if %{qt_maj_ver} == 6
BuildRequires:  kf6-kcolorscheme-devel >= %{kf6min}
BuildRequires:  kf6-kconfig-devel >= %{kf6min}
BuildRequires:  kf6-kconfigwidgets-devel >= %{kf6min}
BuildRequires:  kf6-kcoreaddons-devel >= %{kf6min}
BuildRequires:  kf6-kcrash-devel >= %{kf6min}
BuildRequires:  kf6-kdbusaddons-devel >= %{kf6min}
BuildRequires:  kf6-kdoctools-devel >= %{kf6min}
BuildRequires:  kf6-ki18n-devel >= %{kf6min}
BuildRequires:  kf6-kiconthemes-devel >= %{kf6min}
BuildRequires:  kf6-kjobwidgets-devel >= %{kf6min}
BuildRequires:  kf6-kio-devel >= %{kf6min}
BuildRequires:  kf6-rpm-macros >= %{kf6min}
BuildRequires:  kf6-kxmlgui-devel >= %{kf6min}
BuildRequires:  kf6-kwidgetsaddons-devel >= %{kf6min}
BuildRequires:  qt6-qtbase-devel >= %{qt6min}
%else
BuildRequires:  kf5-kconfig-devel >= %{kf5min}
BuildRequires:  kf5-kconfigwidgets-devel >= %{kf5min}
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5min}
BuildRequires:  kf5-kcrash-devel >= %{kf5min}
BuildRequires:  kf5-kdbusaddons-devel >= %{kf5min}
BuildRequires:  kf5-kdoctools-devel >= %{kf5min}
BuildRequires:  kf5-ki18n-devel >= %{kf5min}
BuildRequires:  kf5-kiconthemes-devel >= %{kf5min}
BuildRequires:  kf5-kjobwidgets-devel >= %{kf5min}
BuildRequires:  kf5-kio-devel >= %{kf5min}
BuildRequires:  kf5-rpm-macros >= %{kf5min}
BuildRequires:  kf5-kxmlgui-devel >= %{kf5min}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5min}
BuildRequires:  qt5-qtbase-devel >= %{qt5min}
%endif

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(polkit-qt%{qt_maj_ver}-1)

Requires:       kf%{qt_maj_ver}-filesystem

%description
KDE Partition Manager is a utility program to help you manage the disk devices,
partitions and file systems on your computer. It allows you to easily create, 
copy, move, delete, resize without losing data, backup and restore partitions.

KDE Partition Manager supports a large number of file systems, 
including ext2/3/4, reiserfs, NTFS, FAT16/32, jfs, xfs and more.

Starting from version 1.9.50 KDE Partition Manager has become the GUI part of 
KPMcore (KDE PartitionManager core) which contain the libraries used to 
manipulate filesystems.


%prep
%autosetup -p1 -n partitionmanager-%{version}


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
%find_lang partitionmanager --with-kde --with-html

%check
# Validate .desktop file
%if %{qt_maj_ver} == 6
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*partitionmanager.desktop
%else
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/*partitionmanager.desktop
%endif

# Validate appdata file
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml


%files -f partitionmanager.lang
%license LICENSES/*
%if %{qt_maj_ver} == 6
%{_kf6_bindir}/partitionmanager
%{_kf6_datadir}/applications/*partitionmanager.desktop
%{_kf6_datadir}/kxmlgui5/partitionmanager/
%{_kf6_datadir}/solid/actions/open_in_partitionmanager.desktop
%{_kf6_datadir}/config.kcfg/partitionmanager.kcfg
%else
%{_kf5_bindir}/partitionmanager
%{_kf5_datadir}/applications/*partitionmanager.desktop
%{_kf5_datadir}/kxmlgui5/partitionmanager/
%{_kf5_datadir}/solid/actions/open_in_partitionmanager.desktop
%{_kf5_datadir}/config.kcfg/partitionmanager.kcfg
%endif
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/*partitionmanager.appdata.xml


%changelog
%autochangelog
