# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global grilo_version 0.3.15
%global goa_version 3.17.91

Name:		grilo-plugins
Version:	0.3.16
Release:	%autorelease
Summary:	Plugins for the Grilo framework

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://wiki.gnome.org/Projects/Grilo
Source0:	https://download.gnome.org/sources/grilo-plugins/%{release_version}/grilo-plugins-%{version}.tar.xz
Patch0:		disable-broken-plugins.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  git
BuildRequires:	avahi-gobject-devel
BuildRequires:	gettext
BuildRequires:	grilo-devel >= %{grilo_version}
BuildRequires:	glib2-devel
BuildRequires:	gom-devel
BuildRequires:	gnome-online-accounts-devel >= %{goa_version}
BuildRequires:	gperf
BuildRequires:	libgcrypt-devel
BuildRequires:	libxml2-devel
BuildRequires:	itstool
BuildRequires:	libarchive-devel
BuildRequires:	libmediaart-devel
BuildRequires:	libsoup3-devel
BuildRequires:	lua-devel
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:	rest-devel
BuildRequires:	sqlite-devel
BuildRequires:	totem-pl-parser-devel
BuildRequires:	json-glib-devel
%if ! 0%{?rhel}
BuildRequires:	libdmapsharing4-devel
BuildRequires:	pkgconfig(oauth)
%endif

%if ! 0%{?rhel}
Requires:	dleyna-server
%endif
Requires:	gnome-online-accounts%{_isa} >= %{goa_version}
Requires:	grilo%{_isa} >= %{grilo_version}

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Bookmarks
- Filesystem
- Flickr
- Freebox
- Gravatar
- iTunes Music Sharing
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Pocket
- Podcasts
- Radio France
- Shoutcast
- The Guardian Videos
- Tracker

%prep
%autosetup -p1 -S git

%build
%meson \
    -Denable-shoutcast=no \
    -Denable-bookmarks=yes \
%if 0%{?rhel}
    -Denable-dleyna=no \
    -Denable-dmap=no \
    -Denable-flickr=no \
%else
    -Denable-dleyna=yes \
    -Denable-dmap=yes \
    -Denable-flickr=yes \
%endif
    -Denable-filesystem=yes \
    -Denable-freebox=yes \
    -Denable-gravatar=yes \
    -Denable-lua-factory=yes \
    -Denable-metadata-store=yes \
%if 0%{?fedora}
    -Denable-podcasts=yes \
%endif
    -Denable-raitv=no \
    -Denable-tmdb=yes \
    -Denable-youtube=no \
    -Denable-tracker=no \
    -Denable-tracker3=yes

%meson_build

%install
%meson_install

%find_lang grilo-plugins --with-gnome

%files -f grilo-plugins.lang
%license COPYING
%doc AUTHORS NEWS README.md
%doc %{_datadir}/help/*/examples/example-tmdb.c
%{_datadir}/grilo-plugins/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/grilo-%{release_version}/*.so*

%changelog
%autochangelog
