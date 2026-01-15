Name:           viking

%global forgeurl https://github.com/viking-gps/viking
%global version0 1.11
%global tag0 viking-%version0
%forgemeta
Version:        %forgeversion
Release:        %autorelease
Summary:        GPS data editor and analyzer

License:        GPL-2.0-or-later
URL:            %forgeurl

Source0:        %forgesource

# Fails to build on s390x, not needed for multilib
ExcludeArch:    s390x %{ix86}

BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  expat-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gpsd-devel
BuildRequires:  gtk3-devel
BuildRequires:  libcurl-devel
BuildRequires:  gtk-doc
BuildRequires:  gnome-doc-utils
BuildRequires:  libexif-devel
BuildRequires:  bzip2-devel
BuildRequires:  file-devel
BuildRequires:  libgexiv2-devel
BuildRequires:  sqlite-devel
BuildRequires:  docbook-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  mapnik-devel
BuildRequires:  rarian-compat
BuildRequires:  geoclue2-devel
BuildRequires:  liboauth-devel
BuildRequires:  nettle-devel
BuildRequires:  libzip-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  json-glib-devel
BuildRequires:  yelp-tools
BuildRequires:  xxd
BuildRequires:  libnova-devel

Requires:       hicolor-icon-theme
Requires:       gpsbabel
Requires:       expect

%description
Viking is a free/open source program to manage GPS data. You can import, plot
and create tracks, routes and waypoints, show OSM, Bing Aerial and other maps,
geotag images, create routes using OSRM, see real-time GPS position, make maps
using Mapnik, control items, etc.

%prep
%forgeautosetup
NOCONFIGURE=1 ./autogen.sh
# Convert TODO to utf-8
mv TODO timestamp
iconv -f ISO-8859-1 -t UTF-8 -o TODO timestamp
touch -r timestamp TODO

%build
%configure
%make_build CFLAGS="${RPM_OPT_FLAGS} -fcommon"

%install
%make_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
desktop-file-install \
    --add-category="GTK;Network;" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-gnome

%check
make test

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog* NEWS README TODO
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
