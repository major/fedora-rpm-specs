%global repo dde-session-shell
%global dde_prefix deepin

Name:           %{dde_prefix}-session-shell
Version:        5.5.34
Release:        %autorelease
Summary:        Deepin Desktop Environment - session-shell module
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dtkcore-devel >= 5.5.23
BuildRequires:  qt5-linguist
BuildRequires:  dtkwidget-devel >= 5.1
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXi-devel
BuildRequires:  xcb-util-wm xcb-util-wm-devel
BuildRequires:  %{dde_prefix}-qt-dbus-factory-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  lightdm-qt5-devel
BuildRequires:  pam-devel
BuildRequires:  gtest-devel
BuildRequires:  openssl-devel
BuildRequires:  make
# provides needed directories
Requires:       dbus-common
Requires:       %{_bindir}/qdbus-qt5
# used by /etc/deepin/greeters.d/00-xrandr
Requires:       %{_bindir}/xrandr
# used by /etc/deepin/greeters.d/10-cursor-theme
Requires:       %{_bindir}/xrdb
Requires:       lightdm
Provides:       lightdm-deepin-greeter%{?_isa} = %{version}-%{release}
Provides:       lightdm-greeter = 1.2

%description
deepin-session-shell - Deepin desktop-environment - session-shell module.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i 's:/usr/lib:%{_libexecdir}:' scripts/lightdm-deepin-greeter
# We don't have common-auth on Fedora
sed -i 's/common-auth/password-auth/' src/libdde-auth/deepinauthframework.cpp


%build
export PATH=$PATH:%{_qt5_bindir}
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/cmake %{buildroot}%{_libdir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/dde-*.desktop

%files
%{_bindir}/dde-lock
%{_bindir}/lightdm-deepin-greeter
%attr(755,root,root) %{_bindir}/deepin-greeter
%{_sysconfdir}/deepin/
%{_sysconfdir}/lightdm/deepin/
%{_datadir}/dde-session-shell/
%{_datadir}/deepin-authentication/
%{_datadir}/applications/dde-lock.desktop
%{_datadir}/xgreeters/lightdm-deepin-greeter.desktop
%{_datadir}/dbus-1/services/com.deepin.dde.lockFront.service
%{_datadir}/dbus-1/services/com.deepin.dde.shutdownFront.service
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/dsg/

%files devel
%{_includedir}/%{repo}
%{_libdir}/cmake/DdeSessionShell/DdeSessionShellConfig.cmake

%changelog
%autochangelog
