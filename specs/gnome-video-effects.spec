Name:           gnome-video-effects
Version:        0.6.0
Release:        %autorelease
Summary:        Collection of GStreamer video effects

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://wiki.gnome.org/Projects/GnomeVideoEffects
Source0:        https://download.gnome.org/sources/%{name}/%{gnome_major_minor_version}/%{name}-%{version}.tar.xz
Buildarch:      noarch

BuildRequires:  gettext
BuildRequires:  meson

%if 0%{?fedora}
Requires:       frei0r-plugins
%endif

%description
A collection of GStreamer effects to be used in different GNOME Modules.


%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install


%files
%doc AUTHORS NEWS README
%license COPYING
%{_datadir}/pkgconfig/gnome-video-effects.pc
%{_datadir}/gnome-video-effects


%changelog
%autochangelog
