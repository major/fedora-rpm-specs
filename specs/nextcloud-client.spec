%if 0%{?el8}
%undefine __cmake_in_source_build
%undefine _cmake_skip_rpath
%endif

Name:           nextcloud-client
Version:        3.15.3
Release:        %autorelease
Summary:        The Nextcloud Client

# -libs are LGPLv2+, rest GPLv2
License:        LGPL-2.1-or-later and GPL-2.0-only
Url:            https://nextcloud.com/install/#install-clients
Source0:        https://github.com/nextcloud/desktop/archive/v%{version}/desktop-%{version}.tar.gz
Source1:        com.nextcloud.desktopclient.nextcloud.metainfo.xml

%if 0%{?fedora} >= 39
ExcludeArch:    %{ix86}
%endif

%if 0%{?rhel}
BuildRequires:  rpmautospec-rpm-macros
BuildRequires:  policycoreutils
%endif

BuildRequires:  check
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  inotify-tools-devel
BuildRequires:  libcloudproviders-devel
BuildRequires:  libappstream-glib
BuildRequires:  neon-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  python3-sphinx
BuildRequires:  qtlockedfile-qt6-devel
BuildRequires:  qtkeychain-qt6-devel
BuildRequires:  qtsingleapplication-qt6-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-gui
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtscxml-devel
BuildRequires:  qt6-qtquickcontrols2-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  inkscape
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kbookmarks-devel

# Dolphin integration
%if 0%{?fedora} >= 24 || 0%{?rhel} > 7
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-karchive-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kguiaddons-devel
%endif
BuildRequires:  sqlite-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Provides: mirall = %{version}-%{release}
Obsoletes: mirall < 1.8.0

# Read https://bugzilla.redhat.com/show_bug.cgi?id=1651261
ExcludeArch: ppc64 ppc64le s390x

%description
Nextcloud-client enables you to connect to your private Nextcloud Server.
With it you can create folders in your home directory, and keep the contents
of those folders synced with your Nextcloud server. Simply copy a file into
the directory and the Nextcloud Client does the rest.


%package libs
Summary: Common files for nextcloud-client
License: LGPL-2.1-or-later
Provides: mirall-common = %{version}-%{release}
Obsoletes: mirall-common < 1.8.0
Requires: %{name}%{?_isa} = %{version}-%{release}

%description libs
Provides common files for nextcloud-client such as the
configuration file that determines the excluded files in a sync.


%package devel
Summary: Development files for nextcloud-client
License: LGPL-2.1-or-later
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
Provides: mirall-devel = %{version}-%{release}
Obsoletes: mirall-devel < 1.8.0

%description devel
Development headers for use of the nextcloud-client library

%package nautilus
Summary: nextcloud client nautilus extension
Supplements: (nextcloud-client and nautilus)
Requires: nautilus
Requires: nautilus-python
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: mirall-nautilus = %{version}-%{release}
Obsoletes: mirall-nautilus < 1.8.0

%description nautilus
The nextcloud desktop client nautilus extension.

%if 0%{?fedora}
# Only Fedora has Cinnamon, so there is no need for Nemo extension on EPEL
%package nemo
Summary:        Nemo overlay icons
Supplements:    (nextcloud-client and nemo)
Requires:       nemo
Requires:       nemo-python
Requires: %{name}%{?_isa} = %{version}-%{release}

%description nemo
This package provides overlay icons to visualize the sync state
in the nemo file manager.

# Only Fedora has Mate, so there is no need for Caja extension on EPEL
%package caja
Summary:        Caja overlay icons
Supplements:    (nextcloud-client and caja)
Requires:       caja
Requires:       python3-caja
Requires: %{name}%{?_isa} = %{version}-%{release}

%description caja
This package provides overlay icons to visualize the sync state
in the caja file manager.
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
%package dolphin
Summary:        Dolphin overlay icons
Supplements:    (nextcloud-client and dolphin)
Requires:       dolphin
Requires: %{name}%{?_isa} = %{version}-%{release}

%description dolphin
The nextcloud desktop client dolphin extension.
%endif

%prep
%setup -n desktop-%{version}

# change compiler flag
sed -i 's/-fPIE/-fPIC/g' src/gui/CMakeLists.txt
sed -i 's/-fPIE/-fPIC/g' src/cmd/CMakeLists.txt

%build
%cmake_kf6 \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" \
  -DNO_SHIBBOLETH=1 \
  -DBUILD_UPDATER=False

%cmake_build

%install
%cmake_install


%find_lang client --with-qt
mkdir -p %{buildroot}%{_datadir}/metainfo/
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.nextcloud.desktopclient.nextcloud.metainfo.xml


%if 0%{?rhel}
# Only Fedora has Cinnamon, so there is no need for Nemo extension on EPEL
rm -rf %{buildroot}%{_datadir}/nemo-python/
# Only Fedora has Mate, so there is no need for Caja extension on EPEL
rm -rf %{buildroot}%{_datadir}/caja-python/
%endif

%post
%if 0%{?rhel}
setsebool -P selinuxuser_execmod=on
%endif

%postun
%if 0%{?rhel}
setsebool -P selinuxuser_execmod=off
%endif

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.nextcloud.desktopclient.nextcloud.metainfo.xml

%ldconfig_scriptlets libs

%if 0%{?fedora} >= 24 || 0%{?rhel} > 7
%ldconfig_scriptlets dolphin
%endif

%files -f client.lang
%{_bindir}/nextcloud
%{_bindir}/nextcloudcmd
%{_datadir}/mime/packages/nextcloud.xml
%{_datadir}/applications/com.nextcloud.desktopclient.nextcloud.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/com.nextcloud.desktopclient.nextcloud.metainfo.xml
%{_datadir}/dbus-1/services/com.nextcloudgmbh.Nextcloud.service

%files libs
%{_libdir}/libnextcloudsync.so.0
%{_libdir}/libnextcloudsync.so.%{version}
%{_libdir}/libnextcloud_csync.so*
%doc README.md
%config %{_sysconfdir}/Nextcloud/sync-exclude.lst
%dir %{_sysconfdir}/Nextcloud

%files devel
%{_includedir}/nextcloudsync/
%{_libdir}/libnextcloudsync.so
%{_libdir}/nextcloudsync_vfs_suffix.so
%{_libdir}/nextcloudsync_vfs_xattr.so

%files nautilus
%{_datadir}/nautilus-python/extensions/*

%if 0%{?fedora}
# Only Fedora has Cinnamon, so there is no need for Nemo extension on EPEL
%files nemo
%{_datadir}/nemo-python/extensions/*

# Only Fedora has Mate, so there is no need for Caja extension on EPEL
%files caja
%{_datadir}/caja-python/extensions/*
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
%files dolphin
%{_libdir}/libnextclouddolphinpluginhelper.so
%{_kf6_plugindir}/overlayicon/nextclouddolphinoverlayplugin.so
%{_kf6_plugindir}/kfileitemaction/nextclouddolphinactionplugin.so
%endif

%changelog
%autochangelog
