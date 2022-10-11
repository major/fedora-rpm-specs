%global newname gfeeds
%global uuid org.gabmus.%{newname}

Name: gnome-feeds
Version: 0.16.2
Release: %autorelease
Summary: RSS/Atom feed reader for GNOME
BuildArch: noarch

License: GPLv3+
URL: https://gabmus.gitlab.io/gnome-feeds
Source0: https://gitlab.com/gabmus/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: meson >= 0.50.0
BuildRequires: python3-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-3.0)

Requires: dbus-common
Requires: glib2
Requires: hicolor-icon-theme
Requires: libhandy1
Requires: python3-beautifulsoup4
Requires: python3-brotli
Requires: python3-feedparser
Requires: python3-html5lib
Requires: python3-listparser
Requires: python3-lxml
Requires: python3-pillow
Requires: python3-pygments
Requires: python3-pytz
Requires: python3-readability-lxml
Requires: python3-requests

%description
GNOME Feeds is a minimal RSS/Atom feed reader built with speed and simplicity
in mind.

It offers a simple user interface that only shows the latest news from your
subscriptions.

Articles are shown in a web view by default, with javascript disabled for a
faster and less intrusive user experience. There's also a reader mode
included, built from the one GNOME Web/Epiphany uses.

Feeds can be imported and exported via OPML.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{newname} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{newname}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{newname}
%{_datadir}/%{newname}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{newname}/


%changelog
%autochangelog
