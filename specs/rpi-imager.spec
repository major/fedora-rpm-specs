Name:           rpi-imager
Version:        2.0.6
Release:        %autorelease
Summary:        Graphical user-interface to write disk images and format SD cards
License:        Apache-2.0
URL:            https://github.com/raspberrypi/rpi-imager
Source0:        %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         https://gitlab.archlinux.org/archlinux/packaging/packages/rpi-imager/-/raw/main/remove-vendoring.patch

# https://github.com/raspberrypi/rpi-imager/blob/v1.9.0/src/CMakeLists.txt#L235
ExcludeArch:    s390x

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)

BuildRequires:  pkgconfig(liblzma)
BuildRequires:  libzstd-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  curl-devel
BuildRequires:  pkgconfig(gnutls)

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme
Requires:       dosfstools
Requires:       util-linux

# Needed if you want to be able to run rpi-imager as a regular user
Recommends:     udisks2

%description
Graphical user-interface to download and write Raspberry Pi disk images, or
write custom disk images and format SD cards.

%prep
%autosetup -p1

%build
pushd src
%cmake -GNinja \
    -DBUILD_SHARED_LIBS=OFF \
    -DENABLE_CHECK_VERSION=OFF \
    -DENABLE_TELEMETRY=OFF \
    -DGENERATE_TIMEZONES_FROM_IANA=OFF
%cmake_build
popd

%install
pushd src
%cmake_install
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license license.txt
%doc README.md
%{_bindir}/rpi-imager
%{_datadir}/applications/com.raspberrypi.rpi-imager.desktop
%{_datadir}/icons/hicolor/scalable/apps/rpi-imager.svg
%{_metainfodir}/com.raspberrypi.rpi-imager.metainfo.xml

%changelog
%autochangelog
