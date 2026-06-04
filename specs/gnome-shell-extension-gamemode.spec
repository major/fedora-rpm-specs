%define extension   gamemodeshellextension
%define uuid        %{extension}@trsnaqe.com

Name:           gnome-shell-extension-gamemode
Version:        20.0
Release:        %autorelease
Summary:        GameMode integration for GNOME Shell
License:        LGPL-2.1-only
URL:            https://github.com/trsnaqe/gamemode-shell-extension
Source0:        %{url}/archive/V%{version}/gamemode-extension-V%{version}.tar.gz
Source1:        lgpl-2.1.md

# https://github.com/Trsnaqe/gamemode-shell-extension/pull/22
Patch:          0001-Install-locale-files-with-meson.patch
# https://github.com/Trsnaqe/gamemode-shell-extension/pull/23
Patch:          0002-Compile-schemas-with-gnome.post_install.patch

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  glib2
Requires:       gnome-shell >= 45
Requires:       gamemode
Recommends:     gnome-extensions-app
BuildArch:      noarch

%description
GNOME Shell extension to integrate with GameMode. Can display
an icon when GameMode is active and also emit notifications
when the global GameMode status changes.

%prep
%autosetup -p1 -n gamemode-shell-extension-%{version}%{?prerelease:-%{prerelease}}
cp %{SOURCE1} .

%conf
%meson

%build
%meson_build

%install
%meson_install
%find_lang %{uuid}

%files -f %{uuid}.lang
%doc README.md
%license lgpl-2.1.md
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
