%global debug_package %{nil}
%global _name   mate_menu

Name:           mate-menu
Version:        20.04.3
Release:        %autorelease
Summary:        Advanced Menu for the MATE Desktop
# mate_menu/keybinding.py use MIT license and the rest is under GPLv2+
# Automatically converted from old format: GPLv2+ and MIT - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-MIT
BuildArch:      noarch
Url:            https://github.com/ubuntu-mate/%{name}
# downloading the tarball
# spectool -g mate-menu.spec
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

Patch1:         mate-menu_adjust-package-manager.patch
Patch2:         mate-menu_default-applications.patch

BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils

Requires:       mate-menus
Requires:       mozo
Requires:       python3-configobj
Requires:       python3-gobject
Requires:       python3-pyxdg
Requires:       python3-xlib
Requires:       python3-setproctitle
Requires:       python3-unidecode
Requires:       beesu
Requires:       mate-panel


%description
An advanced menu for MATE. Supports filtering, favorites,
auto-session, and many other features.
This menu originated in the Linux Mint distribution and has
been ported to other distributions that ship the MATE Desktop
Environment.


%prep
%setup -q

%patch -P1 -p1 -b .adjust-package-manager
%patch -P2 -p1 -b .default-applications

# xdg-su isn't available in fedora
sed -i 's/xdg-su/beesu/g' %{_name}/execute.py

%build
%py3_build

%install
%py3_install

# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{python3} %{buildroot}%{_usr}/lib/%{name}/*.py

# avoid rpmlint invalid-lc-messages-dir and incorrect-locale-subdir errors
rm -rf %{buildroot}%{_datadir}/locale/ber
rm -rf %{buildroot}%{_datadir}/locale/es_419/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/es_419/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/nah/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/zh-Hans/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/zh-Hans/

%find_lang %{name}


%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_usr}/lib/%{name}/
%{python3_sitelib}/%{_name}/
%{python3_sitelib}/%{_name}-*-py3.*.egg-info/
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.mate.mate-menu*.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.MateMenuApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateMenuAppletFactory.service
%{_mandir}/man1/mate-menu.1.*


%changelog
%autochangelog
