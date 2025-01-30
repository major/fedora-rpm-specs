Name:           viking
Version:        1.10
Release:        %autorelease
Summary:        GPS data editor and analyzer

License:        GPL-2.0-or-later
URL:            https://viking.sourceforge.net/
Source0:        https://downloads.sourceforge.net/viking/viking-%{version}.tar.bz2
# SourceForge is not good for fetching individual files and patches. Resort to
# upstream's GitHub mirror.
Source1:        https://raw.githubusercontent.com/viking-gps/viking/refs/tags/viking-%{version}/autogen.sh
Patch:          https://github.com/viking-gps/viking/commit/443fe78cb097ae2196517fc726595b57cb9418c4.patch
# Make compatible with C23
# Backported from https://github.com/viking-gps/viking/pull/316
Patch:          0000-Declare-vik_aggregate_layer_new-parameter.patch
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

Requires:       hicolor-icon-theme
Requires:       gpsbabel
Requires:       expect

%description
Viking is a free/open source program to manage GPS data. You can import, plot
and create tracks, routes and waypoints, show OSM, Bing Aerial and other maps,
geotag images, create routes using OSRM, see real-time GPS position, make maps
using Mapnik, control items, etc.

%prep
%autosetup -p1
cp %{SOURCE1} . && chmod +x autogen.sh
NOCONFIGURE=1 ./autogen.sh
# Convert to utf-8
for file in ChangeLog NEWS TODO; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

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
