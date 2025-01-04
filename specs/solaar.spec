%bcond check 1

Name:           solaar
Version:        1.1.14
Release:        %autorelease
Summary:        Device manager for a wide range of Logitech devices
URL:            https://github.com/pwr/Solaar
Source:         %{url}/archive/%{version}/Solaar-%{version}.tar.gz

# Fedora-specific patches
Patch:          solaar-udev-wayland.patch
Patch:          solaar-autostart.patch

BuildArch:      noarch
License:        GPL-2.0-or-later

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
%if %{with check}
BuildRequires:  gtk3
BuildRequires:  python3-dbus
BuildRequires:  python3-evdev
BuildRequires:  python3-hid-parser
BuildRequires:  python3-psutil
BuildRequires:  python3-gobject-base
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-pyudev
BuildRequires:  python3-pyyaml
BuildRequires:  python3-typing-extensions
%endif

Requires:       hicolor-icon-theme
Requires:       solaar-udev
Recommends:     (gnome-shell-extension-appindicator if gnome-shell)
Recommends:     gtk3
Recommends:     libappindicator-gtk3
Recommends:     python3-gobject-base
Recommends:     python3-hid-parser

%description
Solaar is a device manager for Logitech's Unifying Receiver peripherals. It is
able to pair/unpair devices to the receiver and, for most devices, read battery
status.

gtk3 is recommended.  Without it, you can run solaar commands to view the
configuration of the devices and pair/unpair peripherals but you cannot use the
graphical interface.


%package doc
Summary:        Developer documentation for Solaar
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
This package provides documentation for Solaar, a device manager for
Logitech's Unifying Receiver peripherals.


%package udev
Summary:        Udev rules for Logitech receivers
BuildArch:      noarch

%description udev
This package contains udev rules which grant users permission to access various
connected Logitech wireless receivers.  This includes Unifying receivers,
various types of Nano receivers and some other types which can be used by
Solaar.


%prep
%autosetup -p1 -n Solaar-%{version}
rm docs/.gitignore
rm -rv lib/hid_parser


%build
%py3_build
tools/po-compile.sh


%install
%py3_install

install -pm755 tools/hidconsole %{buildroot}%{_bindir}

# Remove pointless shebangs
sed -i -e '1d' %{buildroot}/%{python3_sitelib}/solaar/{gtk,tasks}.py

# Fix shebang line
sed -i -e '1s,^#!.*$,#!/usr/bin/python3,' %{buildroot}/%{_bindir}/hidconsole

desktop-file-validate %{buildroot}/%{_datadir}/applications/solaar.desktop

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/solaar.desktop

%find_lang %{name}

%check
%pytest

%posttrans udev
# This is needed to apply permissions to existing devices when the package is
# installed.
# Skip triggering udevd when it is note accessible, e.g. containers or
# rpm-ostree-based systems.
if [ -S /run/udev/control ]; then
    /usr/bin/udevadm trigger --subsystem-match=hidraw --action=add
fi

%files -f %{name}.lang
%license LICENSE.txt
%doc CHANGELOG.md COPYRIGHT Release_Notes.md share/README
%{_bindir}/solaar
%{_bindir}/hidconsole
%{python3_sitelib}/hidapi
%{python3_sitelib}/keysyms
%{python3_sitelib}/logitech_receiver
%{python3_sitelib}/solaar
%{python3_sitelib}/solaar-%{version}*-py%{python3_version}.egg-info
%{_datadir}/applications/solaar.desktop
%{_datadir}/icons/hicolor/32x32/apps/solaar-light_*.png
%{_datadir}/icons/hicolor/scalable/apps/solaar.svg
%{_datadir}/icons/hicolor/scalable/apps/solaar-attention.svg
%{_datadir}/icons/hicolor/scalable/apps/solaar-init.svg
%{_datadir}/icons/hicolor/scalable/apps/solaar-symbolic.svg
%{_metainfodir}/io.github.pwr_solaar.solaar.metainfo.xml
%config(noreplace) %{_sysconfdir}/xdg/autostart/solaar.desktop


%files doc
%doc docs/*


%files udev
%license LICENSE.txt
%{_udevrulesdir}/42-logitech-unify-permissions.rules


%changelog
%autochangelog
