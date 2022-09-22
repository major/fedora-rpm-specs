%global unstable 0
%global kf5min 5.90
%global qtmin 5.15.0
%global kpmcoremin 22.03

Name:           kde-partitionmanager
Version:        22.08.1
Release:        %autorelease
Summary:        KDE Partition Manager

License:        GPLv3+
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
BuildRequires:  kpmcore-devel >= %{kpmcoremin}
BuildRequires:  qt5-qtbase-devel >= %{qtmin}

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(polkit-qt5-1)

Requires:       kf5-filesystem

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

# Small fix for the desktop file
# Upstream has already fixed it in master branch
sed -i s/SingleMainWindow=True/SingleMainWindow=true/g ./src/org.kde.partitionmanager.desktop


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
%find_lang partitionmanager --with-kde --with-html

%check
# Validate .desktop file
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/*partitionmanager.desktop

# Validate appdata file
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml


%files -f partitionmanager.lang
%license LICENSES/*
%{_kf5_bindir}/partitionmanager
%{_kf5_datadir}/applications/*partitionmanager.desktop
%{_kf5_datadir}/kxmlgui5/partitionmanager/
%{_kf5_datadir}/solid/actions/open_in_partitionmanager.desktop
%{_kf5_datadir}/config.kcfg/partitionmanager.kcfg
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/*partitionmanager.appdata.xml


%changelog
%autochangelog
