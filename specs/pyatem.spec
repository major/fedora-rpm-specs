Name: pyatem
Summary: Library and control application for Blackmagic Design ATEM video switchers

# Per the LICENSE file:
# - GTK app is GPL-3.0-only;
# - Python library is LGPL-3.0-only and contains some Public Domain code.
# udev rules are unclear, arguably they are part of the lib and hence LGPL.
# There are also some icons with GPL-3.0-or-later comments in their SVG markup.
License: GPL-3.0-only AND GPL-3.0-or-later AND LGPL-3.0-only AND LicenseRef-Fedora-Public-Domain

Version: 0.13.0
Release: 2%{?dist}

URL: https://openswitcher.org
Source0: https://git.sr.ht/~martijnbraam/%{name}/archive/%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: scdoc

BuildRequires: glib2-devel
BuildRequires: python3-devel
BuildRequires: pkgconfig(libhandy-1)

BuildRequires: systemd-rpm-macros

%description
Library implementing the ATEM video switcher protocol and a GTK3 application.

# -- Python lib

%package -n python3-%{name}
Summary: Python library for controlling Blackmagic Design ATEM video mixers
License: LGPL-3.0-only AND LicenseRef-Fedora-Public-Domain

Requires: python3dist(pyusb)
Requires: python3dist(requests)

Recommends: %{name}-udev

%description -n python3-%{name}
PyATEM is a Python library implementing the ATEM video switcher protocol.

# -- udev rules

%package udev
Summary: Unprivileged device access rules for %{name}
License: LGPL-3.0-only

Requires: python3-%{name} = %{version}-%{release}
Requires: systemd-udev

BuildArch: noarch

%description udev
This package contains udev rules which allow %{name} to access relevant devices
when ran by an unprivileged user.

# -- GTK GUI

%package -n openswitcher
Summary: Control application for Blackmagic Design ATEM video switchers
License: GPL-3.0-only AND GPL-3.0-or-later

Requires: python3-%{name} = %{version}-%{release}

Requires: glib2
Requires: hicolor-icon-theme
Requires: python3-gobject
Recommends: python3dist(paho-mqtt)
Recommends: %{name}-udev

BuildArch: noarch

%description -n openswitcher
Open Switcher is a control application for the Blackmagic Design ATEM video
switchers. These are normally controlled with the propriatary Windows or OS X
application over a network connection. Open Switcher is a re-implementation
that aims to be as close to the supported features of ATEM Software Control
as possible. Getting to 100% compatabilty would be quite hard since it exposes
quite a lot of extra functionalities for specific models of mixers which would
be technically difficult to implement or hard to do due to lack of access
to the more expensive hardware.

# -- subpackages end

%prep
%autosetup


%generate_buildrequires
%pyproject_buildrequires


%conf
%meson


%build
%pyproject_wheel
%meson_build


%install
%pyproject_install
%pyproject_save_files %{name}

%meson_install
%find_lang openswitcher

install -m 755 -d %{buildroot}%{_udevrulesdir}
install -m 644 ./100-blackmagicdesign.rules %{buildroot}%{_udevrulesdir}


%check
for PROGRAM in Setup Switcher; do
	desktop-file-validate "%{buildroot}%{_datadir}/applications/nl.brixit.${PROGRAM}.desktop"
	appstream-util validate-relax --nonet "%{buildroot}%{_metainfodir}/nl.brixit.${PROGRAM}.appdata.xml"
done


%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE-lgpl3.txt

%files udev
%{_udevrulesdir}/100-blackmagicdesign.rules

%files -n openswitcher -f openswitcher.lang
%license LICENSE-gpl3.txt
%{_bindir}/atemswitch
%{_bindir}/bmd-setup
%{_bindir}/openswitcher-proxy
%{_bindir}/switcher-control
%{_datadir}/applications/nl.brixit.Setup.desktop
%{_datadir}/applications/nl.brixit.Switcher.desktop
%{_datadir}/glib-2.0/schemas/nl.brixit.Switcher.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/nl.brixit.Setup.svg
%{_datadir}/icons/hicolor/scalable/apps/nl.brixit.Switcher.svg
%{_datadir}/switcher/
%{_mandir}/man1/atemswitch.1*
%{_mandir}/man1/bmd-setup.1*
%{_mandir}/man1/openswitcher-proxy.1*
%{_mandir}/man1/switcher-control.1*
%{_metainfodir}/nl.brixit.Setup.appdata.xml
%{_metainfodir}/nl.brixit.Switcher.appdata.xml


%changelog
* Wed Sep 09 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.13.0-2
- Add icon licenses to License tag
- Add missing Requires

* Sat May 09 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.13.0-1
- Initial packaging
