%global         uuid app.drey.Dialect
%global         forgeurl0 https://github.com/dialect-app/dialect
%global         forgeurl1 https://github.com/dialect-app/po
%global         adw_version 1.6.0

Name:           dialect
Version:        2.6.1
Release:        %autorelease
Summary:        A translation app for GNOME based on Google Translate

%global         tag0 %{version}
%global         tag1 %{version}
%forgemeta -a

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource0}
Source1:        %{forgesource1}

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gstreamer1-devel
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel >= %{adw_version}
BuildRequires:  libsecret-devel
BuildRequires:  libsoup3-devel
BuildRequires:  blueprint-compiler
BuildRequires:  python3-devel >= 3.10
BuildRequires:  python3-gobject-devel >= 3.51.0

Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugins-base
Requires:       gtk4
Requires:       libadwaita >= %{adw_version}
Requires:       libsecret
Requires:       libsoup3
Requires:       python3-gobject >= 3.51.0
Requires:       python3-dbus
Requires:       python3-gtts
Requires:       python3-beautifulsoup4
Requires:       libspelling
Requires:       gtksourceview5

%description
A translation app for GNOME based on Google Translate.

Features:
* Text translation up to 5000 chars
* Text to speech
* History
* Automatic language detection
* Clipboard buttons


%prep
%forgesetup -z 0
gzip -dc %{SOURCE1} | tar -xof -
rmdir po
mv po-%{tag1} po


%build
%meson
%meson_build


%install
%meson_install
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/

%find_lang %{name}
%find_lang %{name}-cldr-langs


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml


%files -f %{name}.lang -f %{name}-cldr-langs.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/%{uuid}.SearchProvider.service
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/gnome-shell/search-providers/%{uuid}.SearchProvider.ini
%{_datadir}/icons/hicolor/*/apps/%{uuid}*.svg
%{_metainfodir}/%{uuid}.metainfo.xml


%changelog
%autochangelog
