Name:           gnome-shell-extension-kimpanel
Version:        90

%global uuid     kimpanel@kde.org
%global forgeurl https://github.com/wengxt/gnome-shell-extension-kimpanel
%global commit   8632e152fc2d331ebc9601d694256c0cf43b8712

%forgemeta

Release:        %autorelease
Summary:        KDE's kimpanel implementation for GNOME Shell

License:        GPL-2.0-or-later
URL:            %forgeurl
Source:         %forgesource

Patch0:         0001-Add-meson.build.patch
Patch1:         0002-Remove-hardcoded-settings-schema.patch

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  meson

Requires:       (gnome-shell >= 48 with gnome-shell < 50)
Requires:       fcitx5

%description
Input Method Panel using KDE's kimpanel protocol for GNOME Shell.

You can use gnome-tweaks (additional package) or run in terminal:

  $ gnome-extensions enable %uuid

%prep
%forgeautosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang gnome-shell-extensions-kimpanel

%files -f gnome-shell-extensions-kimpanel.lang
%license COPYING
%doc README
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/glib-2.0/schemas/*.gschema.xml


%changelog
%autochangelog
