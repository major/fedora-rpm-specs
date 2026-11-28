%global commit bfce851d4da5a01f24189ba79eac9385b7ce8533
# git log -1 --pretty=format:%ct
%global timestamp 1699609231
%global nanopb_commit 13666952914f3cf43a70c6b9738a7dc0dd06a6dc

%global srcname qFlipper
%global forgeurl https://github.com/flipperdevices/%{srcname}
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           qflipper
Version:        1.3.3
Release:        %autorelease
Summary:        Desktop application for updating Flipper Zero firmware via PC

# qFlipper proper is GPLv3, the bundled nanopb library is zlib
License:        GPL-3.0-or-later AND Zlib
URL:            https://update.flipperzero.one
Source0:        %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz
Source1:        https://github.com/nanopb/nanopb/archive/%{nanopb_commit}/nanopb-%{nanopb_commit}.tar.gz
Source2:        one.flipperzero.qflipper.metainfo.xml

# qFlipper fails to build on i686
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros

BuildRequires:  libusb1-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  zlib-devel

Requires:       %{name}-udev = %{version}-%{release}

# nanopb needs to be compiled in, and needs to match the one used in the
# firmware on the device side
Provides:       bundled(nanopb) = 0.4.5

%description
Graphical desktop application for updating Flipper Zero firmware via PC.

Features:
* Update Flipper's firmware and supplemental data with a press of one button
* Repair a broken fimware installation
* Stream Flipper's display and control it remotely
* Install firmware from a .dfu file
* Backup and restore settings, progress and pairing data
* Automatic self-update feature
* Command line interface

# These would ideally go into hwdb but that's complicated
# https://github.com/systemd/systemd/pull/24869
%package     udev
Summary:     Udev integration for Flipper Zero
Requires:    systemd-udev

%description udev
This package contains udev integration rules for Flipper Zero.

%prep
%autosetup -n %{srcname}-%{version} -b 1

# Use the correct nanopb snapshot
rmdir 3rdparty/nanopb
ln -s ../../nanopb-%{nanopb_commit} 3rdparty/nanopb

# Set the version
sed -i qflipper_common.pri \
    -e 's/$$GIT_VERSION/%{version}/' \
    -e 's/$$GIT_COMMIT/%{shortcommit}/' \
    -e 's/$$GIT_TIMESTAMP/%{timestamp}/'

# Fix the plugins library path
sed -e 's:/lib/:/%{_lib}/:' \
    -i backend/applicationbackend.cpp plugins/flipperproto0/flipperproto0.pro

%build
%qmake_qt5 \
  PREFIX=%{buildroot}%{_prefix} \
  CONFIG+=qtquickcompiler \
  DEFINES+=DISABLE_APPLICATION_UPDATES

%make_build

%install
%make_install

# Install the appdata file
install -Dpm0644 -t %{buildroot}%{_metainfodir} %SOURCE2

%check
# Validate desktop files
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{srcname}.desktop

%files
%license LICENSE 3rdparty/nanopb/LICENSE.txt
%doc README.md screenshot.png
%{_bindir}/*
%{_libdir}/%{srcname}
%{_datadir}/applications/%{srcname}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{srcname}.png
%{_metainfodir}/one.flipperzero.qflipper.metainfo.xml

%files udev
%license LICENSE
%{_udevrulesdir}/42-flipperzero.rules

%changelog
%autochangelog
