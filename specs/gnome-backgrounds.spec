%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-backgrounds
Version:        48.2.1
Release:        %autorelease
Summary:        Desktop backgrounds packaged with the GNOME desktop

License:        CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/gnome-backgrounds
Source0:        https://download.gnome.org/sources/%{name}/48/%{name}-%{tarball_version}.tar.xz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  meson

# svg and jxl pixbuf loaders
Requires: (librsvg2 if gdk-pixbuf2)
Requires: (jxl-pixbuf-loader if gdk-pixbuf2)

Provides:   gnome-backgrounds-extras = %{version}-%{release}
Obsoletes:  gnome-backgrounds-extras < %{version}-%{release}

%description
The gnome-backgrounds package contains the default
desktop background, known as the Adwaita background,
for the GNOME Desktop version

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/images

# all translations are merged back into xml by intltool
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/gnome-background-properties/adwaita.xml
%{_datadir}/gnome-background-properties/blobs.xml
%{_datadir}/gnome-background-properties/drool.xml
%{_datadir}/gnome-background-properties/pills.xml
%{_datadir}/backgrounds/gnome/adwaita-d.jpg
%{_datadir}/backgrounds/gnome/adwaita-l.jpg
%{_datadir}/backgrounds/gnome/blobs-d.svg
%{_datadir}/backgrounds/gnome/blobs-l.svg
%{_datadir}/backgrounds/gnome/drool-d.svg
%{_datadir}/backgrounds/gnome/drool-l.svg
%{_datadir}/backgrounds/gnome/pills-d.jxl
%{_datadir}/backgrounds/gnome/pills-l.jxl
%{_datadir}/gnome-background-properties/amber.xml
%{_datadir}/gnome-background-properties/fold.xml
%{_datadir}/gnome-background-properties/geometrics.xml
%{_datadir}/gnome-background-properties/glass-chip.xml
%{_datadir}/gnome-background-properties/lcd.xml
%{_datadir}/gnome-background-properties/lcd-rainbow.xml
%{_datadir}/gnome-background-properties/map.xml
%{_datadir}/gnome-background-properties/mollnar.xml
%{_datadir}/gnome-background-properties/morphogenesis.xml
%{_datadir}/gnome-background-properties/neogeo.xml
%{_datadir}/gnome-background-properties/pixels.xml
%{_datadir}/gnome-background-properties/pride.xml
%{_datadir}/gnome-background-properties/progress.xml
%{_datadir}/gnome-background-properties/ring.xml
%{_datadir}/gnome-background-properties/sheet.xml
%{_datadir}/gnome-background-properties/swoosh.xml
%{_datadir}/gnome-background-properties/symbolic.xml
%{_datadir}/gnome-background-properties/symbolic-soup.xml
%{_datadir}/gnome-background-properties/tarka.xml
%{_datadir}/gnome-background-properties/vnc.xml
%{_datadir}/backgrounds/gnome/amber-d.jxl
%{_datadir}/backgrounds/gnome/amber-l.jxl
%{_datadir}/backgrounds/gnome/fold-d.jxl
%{_datadir}/backgrounds/gnome/fold-l.jxl
%{_datadir}/backgrounds/gnome/geometrics-d.jxl
%{_datadir}/backgrounds/gnome/geometrics-l.jxl
%{_datadir}/backgrounds/gnome/glass-chip-d.jxl
%{_datadir}/backgrounds/gnome/glass-chip-l.jxl
%{_datadir}/backgrounds/gnome/lcd-d.jxl
%{_datadir}/backgrounds/gnome/lcd-l.jxl
%{_datadir}/backgrounds/gnome/lcd-rainbow-d.jxl
%{_datadir}/backgrounds/gnome/lcd-rainbow-l.jxl
%{_datadir}/backgrounds/gnome/map-d.svg
%{_datadir}/backgrounds/gnome/map-l.svg
%{_datadir}/backgrounds/gnome/mollnar-d.svg
%{_datadir}/backgrounds/gnome/mollnar-l.svg
%{_datadir}/backgrounds/gnome/morphogenesis-d.svg
%{_datadir}/backgrounds/gnome/morphogenesis-l.svg
%{_datadir}/backgrounds/gnome/neogeo-d.jxl
%{_datadir}/backgrounds/gnome/neogeo-l.jxl
%{_datadir}/backgrounds/gnome/pixels-d.jxl
%{_datadir}/backgrounds/gnome/pixels-l.jxl
%{_datadir}/backgrounds/gnome/pride-d.jxl
%{_datadir}/backgrounds/gnome/pride-l.jxl
%{_datadir}/backgrounds/gnome/progress-d.jxl
%{_datadir}/backgrounds/gnome/progress-l.jxl
%{_datadir}/backgrounds/gnome/ring-d.jxl
%{_datadir}/backgrounds/gnome/ring-l.jxl
%{_datadir}/backgrounds/gnome/sheet-d.jxl
%{_datadir}/backgrounds/gnome/sheet-l.jxl
%{_datadir}/backgrounds/gnome/swoosh-d.jxl
%{_datadir}/backgrounds/gnome/swoosh-l.jxl
%{_datadir}/backgrounds/gnome/symbolic-d.png
%{_datadir}/backgrounds/gnome/symbolic-l.png
%{_datadir}/backgrounds/gnome/symbolic-soup-d.jxl
%{_datadir}/backgrounds/gnome/symbolic-soup-l.jxl
%{_datadir}/backgrounds/gnome/tarka-d.jxl
%{_datadir}/backgrounds/gnome/tarka-l.jxl
%{_datadir}/backgrounds/gnome/vnc-d.png
%{_datadir}/backgrounds/gnome/vnc-l.png

%changelog
%autochangelog