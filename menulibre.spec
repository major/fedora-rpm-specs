%global forgeurl    https://github.com/bluesabre/menulibre

Name:           menulibre
Version:        2.3.1
Release:        %autorelease
Summary:        FreeDesktop.org compliant menu editor

%global tag     menulibre-%{version}
%forgemeta

License:        GPLv3
URL:            https://bluesabre.org/projects/menulibre/
Source0:        %{forgesource}
BuildArch:      noarch

Requires:       gnome-menus
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       xdg-utils

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib

BuildRequires:  gnome-menus
BuildRequires:  gtk3
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject
BuildRequires:  python3-psutil

%py_provides python3-%{name}
%py_provides python3-%{name}_lib


%description
MenuLibre is an advanced FreeDesktop.org compliant menu editor.

All fields specified in the FreeDesktop.org Desktop Entry and Menu
specifications are available to quickly update. Additionally, MenuLibre
provides an editor for the launcher actions used by applications such as Unity
and Plank.

Features:

- A beautiful interface powered by the latest version of GTK+.
- Create new launchers, or modify existing ones with complete control over
  common settings and access to advanced settings.
- Add, remove, and adjust desktop actions: powerful shortcuts available used by
  Unity, Xfce, and Pantheon.
- Easily rearrange menu items to suit your needs.


%prep
%forgeautosetup


%build
rm uninstall.py

%pyproject_wheel


%install
%pyproject_install

# Remove hashbang line from non-executable library files
for lib in %{buildroot}%{python3_sitelib}/%{name}{,_lib}/*.py; do
	sed '1{\@^#!/usr/bin/python3@d}' $lib > $lib.new &&
	touch -r $lib $lib.new &&
	mv $lib.new $lib
done

desktop-file-install									\
--remove-key="OnlyShowIn"								\
--delete-original										\
--dir=%{buildroot}%{_datadir}/applications				\
%{buildroot}/%{_datadir}/applications/%{name}.desktop

%pyproject_save_files %{name} %{name}_lib

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%py3_check_import menulibre menulibre_lib


%files -f %{name}.lang -f %{pyproject_files}
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-menu-validate
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-menu-validate.1.*


%changelog
%autochangelog
