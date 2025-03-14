%global forgeurl https://gitlab.com/CalcProgrammer1/%{upstream_package_name}
%global commit 28e97cf2d972d34ee8bf53116fe3fc8480221281
#%%global tag release_%%{version}
# Workaround for incorrect package suffix name with forge macros
# (.20231017gitrelease.0.9 for example)
#%%global distprefix %%{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global upstream_package_name OpenRGB

Name:           openrgb
Version:        0.9
%forgemeta
Release:        %autorelease
Summary:        Open source RGB lighting control

# Entire source code is GPL-2.0-only except some bundled libs:
#   * GPL-3.0-or-later:
#     - hueplusplus-1.0.0
#     - libcmmk
License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://openrgb.org
Source0:        %{forgesource}

# Attempt to support some Gigabyte boards (like x870e aorus pro ice)
# Not accepted upstream yet as there are a few things to sort out but this is
# usable as it is
Patch:          dd633e46370659e275fb7a0a16dcd1c3986d7b6e.patch

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
%forgeautosetup -p1

# Remove some bundled libs
pushd dependencies
rm -rf       \
  hidapi     \
  hidapi-win \
  libusb-*   \
  mbedtls-*  \
  %{nil}
popd


%build
%qmake_qt5 \
    .      \
    %{nil}
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}


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
