%global appname com.github.danrabbit.harvey

Name:           harvey
Summary:        The hero that Gotham needs right now
Version:        1.0.2
Release:        %autorelease
# The entire source is GPL-3.0-or-later:
#
#   The COPYING file is GPLv3, and while the phrase “or any later version” does
#   not appear, data/com.github.danrabbit.harvey.appdata.xml.in,
#   debian/copyright, and the SPDX headers of the Vala sources, src/*.vala,
#   indicate GPLv3+ is intended. For example, from the AppData file:
#
#     <project_license>GPL-3.0+</project_license>
#
# …except:
#   - data/Application.css is GPL-2.0-or-later
#   - data/com.github.danrabbit.harvey.appdata.xml.in is CC0-1.0, which is only
#   allowed for content
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC0-1.0

URL:            https://github.com/danrabbit/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)

Requires:       hicolor-icon-theme

Summary(fr):    Le héro dont Gotham a besoin dès à présent
Summary(es):    El héroe que Gotham estaba necesitando
Summary(en_AU): The hero that Gotham needs right now
Summary(en_CA): The hero that Gotham needs right now
Summary(en_GB): The hero that Gotham needs right now

%description
Calculate and visualize color contrast. Harvey checks a given set of colors for
WCAG contrast compliance.

%description -l fr
Calculez et visualisez les contrastes de couleur. Harvey vérifie qu’un jeu de
couleur est conforme aux recommandation de contraste WCAG.

%description -l es
Calcule y visualice el contraste de color, Harvey comprueba un conjunto
determinado de colores para el cumplimiento del contraste WCAG.

%description -l en_AU
Calculate and visualize colour contrast. Harvey checks a given set of colours
for WCAG contrast compliance.

%description -l en_CA
Calculate and visualize colour contrast. Harvey checks a given set of colours
for WCAG contrast compliance.

%description -l en_GB
Calculate and visualize colour contrast. Harvey checks a given set of colours
for WCAG contrast compliance.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml
# Matches what gnome-software and others use:
appstreamcli validate --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_metainfodir}/%{appname}.appdata.xml


%changelog
%autochangelog
