%global tarball_version %%(echo %{version} | tr '~' '.')

Name:		geary
Version:	46.0
Release:	%autorelease
Summary:	A lightweight email program designed around conversations
# Geary is under LGPL-2.1-or-later.
# SQLite3-unicodesn code is in the Public Domain.
# libstemmer.vapi is covered by the BSD license.
# libunwind.vapi is covered by the MIT (aka Expat) license.
# Icons are under CC-BY-3.0, CC-BY-SA-3.0 or in the Public Domain (see
# COPYING.icons).
# As libstemmer.vapi and libunwind.vapi are built into the same binary with
# LGPLv2+ code, we end up with the more restrictive LGPLv2+ license covering
# the whole binary, so we don't need to specify BSD and MIT separately.
License:	LGPL-2.1-or-later AND CC-BY-3.0 AND CC-BY-SA-3.0 AND LicenseRef-Fedora-Public-Domain
URL:		https://wiki.gnome.org/Apps/Geary
Source0:	https://download.gnome.org/sources/geary/46/%{name}-%{tarball_version}.tar.xz

BuildRequires:	meson >= 0.49
BuildRequires:	vala >= 0.26.0
BuildRequires:	valadoc
# primary deps
BuildRequires:	pkgconfig(glib-2.0) >= 2.68
BuildRequires:	pkgconfig(gmime-3.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.24.24
BuildRequires:	pkgconfig(sqlite3) >= 3.12
BuildRequires:	pkgconfig(webkit2gtk-4.1)
# secondary deps
BuildRequires:	libstemmer-devel
BuildRequires:	pkgconfig(appstream-glib) >= 0.7.10
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(enchant-2) >= 2.1
BuildRequires:	pkgconfig(folks) >= 0.11
BuildRequires:	pkgconfig(gck-1)
BuildRequires:	pkgconfig(gcr-3) >= 3.10.1
BuildRequires:	pkgconfig(gdk-3.0) >= 3.24.24
BuildRequires:	pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:	pkgconfig(gio-2.0) >= 2.54
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gsound)
BuildRequires:	pkgconfig(gspell-1)
BuildRequires:	pkgconfig(gthread-2.0) >= 2.54
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(javascriptcoregtk-4.1)
BuildRequires:	pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:	pkgconfig(libhandy-1) >= 1.2.1
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(libsecret-1) >= 0.11
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libunwind) >= 1.1
BuildRequires:	pkgconfig(libunwind-generic) >= 1.1
BuildRequires:	pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:	pkgconfig(libytnef) >= 1.9.3
BuildRequires:	pkgconfig(webkit2gtk-web-extension-4.1)

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	python3
BuildRequires:	symlinks fakechroot
Requires:	hicolor-icon-theme
Recommends:	gnome-keyring

%description
Geary is a new email reader for GNOME designed to let you read your
email quickly and effortlessly. Its interface is based on
conversations, so you can easily read an entire discussion without
having to click from message to message. Geary is still in early
development and has limited features today, but we're planning to add
drag-and-drop attachments, lightning-fast searching, multiple account
support and much more. Eventually we'd like Geary to have an
extensible plugin architecture so that developers will be able to add
all kinds of nifty features in a modular way.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson -Dprofile=release
%meson_build

%install
%meson_install

desktop-file-validate \
  %{buildroot}%{_datadir}/applications/org.gnome.Geary.desktop \
  %{buildroot}%{_datadir}/applications/geary-autostart.desktop

pushd %{buildroot}
fakechroot -- symlinks -C -cvr %{_datadir}/help
popd

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license COPYING COPYING.icons
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/geary
%{_libdir}/geary
%{_datadir}/geary
%{_datadir}/applications/org.gnome.Geary.desktop
%{_datadir}/applications/geary-autostart.desktop
%{_metainfodir}/org.gnome.Geary.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Geary.service
%{_datadir}/glib-2.0/schemas/org.gnome.Geary.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Geary*
%{_datadir}/icons/hicolor/*/actions/*


%changelog
%autochangelog
