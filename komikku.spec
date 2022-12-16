%global appname Komikku
%global uuid    info.febvre.%{appname}
%global gtk4_version        4.8.1
%global libadwaita_version  1.2

Name:           komikku
Version:        1.6.0
Release:        %autorelease
Summary:        A manga reader for GNOME
BuildArch:      noarch

License:        GPLv3+
URL:            https://gitlab.com/valos/Komikku
Source0:        %{url}/-/archive/v%{version}/%{appname}-v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.59.0
BuildRequires:  python3-devel >= 3.8

BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}

Requires:       hicolor-icon-theme
Requires:       gtk4 >= %{gtk4_version}
Requires:       libadwaita >= %{libadwaita_version}
Requires:       libnotify
Requires:       python3-beautifulsoup4
Requires:       python3-brotli
Requires:       python3-cloudscraper
Requires:       python3-dateparser >= 1.1.4
Requires:       python3-emoji
Requires:       python3-gobject
Requires:       python3-keyring >= 21.6.0
Requires:       python3-lxml
Requires:       python3-natsort
# The conflict between python-magic and python-file-magic should be brought to
# FESCO.
Requires:       python3dist(file-magic)
Requires:       python3-pillow
Requires:       python3-pure-protobuf
Requires:       python3-rarfile
Requires:       python3-unidecode

%description
Komikku is a manga reader for GNOME. It focuses on providing a clean, intuitive
and adaptive interface.

Keys features

* Online reading from dozens of servers
* Offline reading of downloaded comics
* Categories to organize your library
* RTL, LTR, Vertical and Webtoon reading modes
* Several types of navigation:
  * Keyboard arrow keys
  * Right and left navigation layout via mouse click or tapping
    (touchpad/touch screen)
  * Mouse wheel
  * 2-fingers swipe gesture (touchpad)
  * Swipe gesture (touch screen)
* Automatic update of comics
* Automatic download of new chapters
* Reading history
* Light and dark themes

%prep
%autosetup -n %{appname}-v%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
%autochangelog
