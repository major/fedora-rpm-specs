%global quassel_data_dir    %{_var}/lib/quassel
%if 0%{?epel} != 0
# we don't have kf5-rpm-macros on EL10, so define the necessary dirs manually
%global _kf5_datadir %_datadir
%global _kf5_bindir %_prefix/bin
%endif

Name:    quassel
Summary: A modern distributed IRC system
Version: 0.14.0
Release: %autorelease

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License: GPL-2.0-only OR GPL-3.0-only
URL:     https://quassel-irc.org/
Source0: https://quassel-irc.org/pub/quassel-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules

%if 0%{?epel} == 0
BuildRequires: dbusmenu-qt5-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-rpm-macros
BuildRequires: phonon-qt5-devel
BuildRequires: qt5-qtwebkit-devel
%endif

BuildRequires: openssl-devel
BuildRequires: perl-generators
BuildRequires: qca-qt5-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: openldap-devel
BuildRequires: boost-devel

BuildRequires: systemd
BuildRequires: systemd-rpm-macros

BuildRequires: libappstream-glib

Requires: oxygen-icon-theme

Provides: %{name}-gui = %{version}-%{release}

Requires: %{name}-common = %{version}-%{release}

# Systemd service file and configuration script.
Source1: quasselcore.service
Source2: quassel.conf
Source3: quassel.sysusers

%description
Quassel IRC is a modern, distributed IRC client,
meaning that one (or multiple) client(s) can attach
to and detach from a central core --
much like the popular combination of screen and a
text-based IRC client such as WeeChat, but graphical

%package common
Summary: Quassel common/shared files
# not strictly required, but helps this get pulled out when
# someone removes %%name or %%name-client
Requires: %{name}-gui = %{version}-%{release}
# put here for convenience, instead of all subpkgs which
# provide %%{name}-gui
BuildArch: noarch
%description common
%{summary}.

%package core
Summary: Quassel core component

# Weak dependency on qt5 postgresql bindings.
# We use a weak dependency here so they can be uninstalled if necessary.
Recommends: qt5-qtbase-postgresql

%description core
The Quassel IRC Core maintains a connection with the
server, and allows for multiple clients to connect

%package client
Summary: Quassel client
Provides: %{name}-gui = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
%description client
Quassel client


%prep
%autosetup -p0 -n %{name}-%{version}

%build
%if 0%{?epel} == 0
%cmake_kf5 \
  -DWANT_MONO=1 -DUSE_QT5=1 -DWITH_KDE=1 -DHAVE_SSL=1 -DENABLE_SHARED=OFF
%else
# we don't have KDE/kf5 on EL10, so do a QT-only build instead
%cmake \
  -DWANT_MONO=1 -DUSE_QT5=1 -DHAVE_SSL=1 -DENABLE_SHARED=OFF
%endif

%cmake_build

%install
%cmake_install

# unpackaged files
rm -f %{buildroot}/%{_datadir}/pixmaps/quassel.png

# Install quassel.conf for systemd file
install -Dp -m 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}.conf

# Install systemd service file
install -Dp -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/quasselcore.service

# Install the systemd-sysusers config
install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

# Home directory for quassel user
install -d -m 0750 %{buildroot}/%{quassel_data_dir}

# Install AppStream metadata
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
install -p -m 0644 data/*.appdata.xml %{buildroot}%{_datadir}/metainfo/

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml


%post core
# Install quassel service.
%systemd_post quasselcore.service

%preun core
%systemd_preun quasselcore.service

%postun core
%systemd_postun_with_restart quasselcore.service

%files
%{_kf5_bindir}/quassel
%{_kf5_datadir}/applications/quassel.desktop
%{_datadir}/metainfo/quassel.appdata.xml

%files common
%doc README.md
%license COPYING gpl-2.0.txt gpl-3.0.txt
%if 0%{?epel} == 0
%{_kf5_datadir}/knotifications5/quassel.notifyrc
%endif
%{_kf5_datadir}/quassel/
%{_kf5_datadir}/icons/hicolor/*/*/*

%files core
%doc README.md
%license COPYING gpl-2.0.txt gpl-3.0.txt
%{_kf5_bindir}/quasselcore
%dir %attr(-,quassel,quassel) %{quassel_data_dir}
%{_unitdir}/quasselcore.service
%config(noreplace) %{_sysconfdir}/quassel.conf
%{_sysusersdir}/%{name}.conf

%files client
%{_kf5_bindir}/quasselclient
%{_kf5_datadir}/applications/quasselclient.desktop
%{_datadir}/metainfo/quasselclient.appdata.xml


%changelog
%autochangelog
