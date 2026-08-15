# VCS   https://gitlab.xfce.org/apps/xfce4-panel-profiles

%global majorver 1.1
%global app_org_name org.xfce.PanelProfiles

Name:           xfce4-panel-profiles
Version:        1.1.1
Release:        %autorelease
Summary:        A simple application to manage Xfce panel layouts

License:        GPL-3.0-or-later
URL:            https://docs.xfce.org/apps/xfce4-panel-profiles/start
Source0:        https://archive.xfce.org/src/apps/%{name}/%{majorver}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(libxfce4util-1.0)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-psutil
BuildArch:      noarch
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       xfce4-panel


%description
A simple application to manage Xfce panel layouts

With the modular Xfce Panel, a multitude of panel layouts can be created. 
This tool makes it possible to backup, restore, import, and export these 
panel layouts.

%prep
%autosetup
# Remove shebangs from non-executable python library files
sed -i '1{\@^#!/usr/bin/env python3@d}' xfce4-panel-profiles/panelconfig.py xfce4-panel-profiles/xfce4-panel-profiles.py

%build
%meson
%meson_build

%install
%meson_install

# Rename non-standard hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}

# fix executable permissions on tarballs
chmod -x %{buildroot}%{_datadir}/%{name}/layouts/*

# get rid of INSTALL and extra license file
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
rm -f %{buildroot}%{_docdir}/%{name}/COPYING

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_org_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{app_org_name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS README.md
%{_mandir}/man1/%{name}*
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{app_org_name}.desktop
%{_datadir}/metainfo/%{app_org_name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{app_org_name}.*

%changelog
%autochangelog
