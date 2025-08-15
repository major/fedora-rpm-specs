%global forgeurl https://gitlab.com/megapixels-org/Megapixels
Version:        1.8.3
%global tag %{version}
%forgemeta

Name:           megapixels
Release:        %autorelease
Summary:        GTK4 camera application that knows how to deal with the media request api

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

# Only available on 64-bit architectures due to memory requirements
ExcludeArch:    %{ix86} armv7hl

# Patches
Patch0:         0001-fix-capture-callback-signature.patch

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zbar)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libjpeg)

BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  /usr/bin/xauth

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
# for postprocess.sh
Requires:       dcraw

%description
A GTK4 camera application that knows how to deal with the media request api.
It uses opengl to debayer the raw sensor data for the preview.

%prep
%forgeautosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/megapixels
%{_bindir}/megapixels-camera-test
%{_bindir}/megapixels-list-devices
%{_datadir}/applications/org.postmarketos.Megapixels.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.postmarketos.Megapixels.svg
%dir %{_datadir}/megapixels
%dir %{_datadir}/megapixels/config
%{_datadir}/megapixels/config/*.ini
%{_datadir}/megapixels/config/*.dcp
%{_datadir}/megapixels/postprocess.sh
%{_datadir}/metainfo/org.postmarketos.Megapixels.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.postmarketos.Megapixels.gschema.xml

%changelog
%autochangelog
