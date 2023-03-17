# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global uname OpenRGB

Name:           openrgb
Version:        0.8
Release:        %autorelease
Summary:        Open source RGB lighting control

# Entire source code is GPLv2 except some bundled libs:
#   * GPLv3+:   hueplusplus-1.0.0
#               libcmmk
License:        GPLv2 and GPLv3+
URL:            https://gitlab.com/CalcProgrammer1/OpenRGB
Source0:        %{url}/-/archive/release_%{version}/%{uname}-release_%{version}.tar.gz

# FTBFS with new GCC 13
# https://gitlab.com/CalcProgrammer1/OpenRGB/-/issues/3225
Patch0:         https://gitlab.com/CalcProgrammer1/OpenRGB/-/merge_requests/1743.patch#/Fix-building-with-GCC-13.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  mbedtls-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(libusb)

BuildRequires:  cmake
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5LinguistTools)

Requires:       %{name}-udev-rules = %{version}-%{release}
Requires:       hicolor-icon-theme

Provides:       bundled(hueplusplus) = 1.0.0
Provides:       bundled(libcmmk)

%description
Visit our website at https://openrgb.org!

One of the biggest complaints about RGB is the software ecosystem surrounding
it.  Every manufacturer has their own app, their own brand, their own style.
If you want to mix and match devices, you end up with a ton of conflicting,
functionally identical apps competing for your background resources.  On top
of that, these apps are proprietary and Windows-only.  Some even require
online accounts.  What if there was a way to control all of your RGB devices
from a single app, on both Windows and Linux, without any nonsense?  That is
what OpenRGB sets out to achieve.  One app to rule them all.

Features
  * Set colors and select effect modes for a wide variety of RGB hardware
  * Save and load profiles
  * Control lighting from third party software using the OpenRGB SDK
  * Command line interface
  * Connect multiple instances of OpenRGB to synchronize lighting across
    multiple PCs
  * Can operate standalone or in a client/headless server configuration
  * View device information
  * No official/manufacturer software required
  * Graphical view of device LEDs makes creating custom patterns easy


# Separate Udev rules package is useful for Flatpak package and others
%package        udev-rules
Summary:        Udev rules for %{name}
BuildArch:      noarch

Requires:       systemd-udev
Suggests:       %{name} = %{version}-%{release}

%description    udev-rules
Udev rules for %{name}.


%prep
%autosetup -n %{uname}-release_%{version} -p1

# Remove some bundled libs
pushd dependencies
rm -rf       \
  hidapi     \
  hidapi-win \
  libusb-*   \
  mbedtls-*  \
  %{nil}
popd

mkdir -p %{_target_platform}


%build
pushd %{_target_platform}
%qmake_qt5                        \
    PREFIX=%{buildroot}%{_prefix} \
    ..                            \
    %{nil}
popd
%make_build -C %{_target_platform}


%install
%make_install -C %{_target_platform}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


# Need to manually reload udev rules to get working app right after installing
# package
%post -n %{name}-udev-rules
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi


%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.metainfo.xml

%files udev-rules
%license LICENSE
%{_udevrulesdir}/60-%{name}.rules


%changelog
%autochangelog
