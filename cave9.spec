%global forgeurl https://github.com/bart9h/cave9
%global fontname mutante
%global fontlicense CC-BY-2.5
%global fontfamily mutante
%global fontsummary Mutante font used by the HUD in cave9 game
%global fonts data/*.ttf


Name:           cave9
Version:        0.4.1
Release:        %autorelease
Summary:        3d game of cave exploration
%global tag %{version}
%forgemeta
License:        LGPL-3.0-only AND CC-BY-SA-3.0 AND LicenseRef-Fedora-Public-Domain
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        http://cave9.googlecode.com/files/cave9_data-4.tgz
Source2:        cave9.desktop
Source3:        64-%{name}-%{fontname}.conf
Source4:        %{fontname}.metainfo.xml

BuildRequires:  gcc
BuildRequires:  SDL_image-devel, SDL_net-devel, SDL_ttf-devel, mesa-libGL-devel, desktop-file-utils, fontpackages-devel
BuildRequires:  make
Requires:       fontpackages-filesystem
Requires:       cave9-%{fontname}-fonts

%description
Cave9 is a gravity cave-exploration game.


%global fontconf 64-%{name}-%{fontname}.conf
%global fontconfs %{SOURCE3} %{SOURCE4}
%global fontdescription %{expand:
Fantasy/display font used by the cave9 game, this font has only the
basic characters used in the Portuguese language was made as an
experiment by the designer Jonas Kühner (http://www.criatipos.com/) the
font was altered by the game developer to also include numbers.}
%fontmetapkg -n %{name}-%{fontname}-fonts


%prep
%setup -q -a1
sed -i src/GNUmakefile -e "s/-Wall -Werror -ggdb//"
mv data/hud.ttf data/mutante.ttf


%build
CFLAGS="%{optflags}" make %{?_smp_mflags}
%fontbuild


%install
mkdir -p %{buildroot}/usr/bin %{buildroot}/usr/share/cave9
install -m 755 -p cave9 $RPM_BUILD_ROOT/usr/bin
cp -p data/wall.jpg data/icon.png data/thrust.wav data/crash.wav data/hit.wav $RPM_BUILD_ROOT/usr/share/cave9

mkdir -p %{buildroot}/usr/share/pixmaps
cp -p data/icon.png $RPM_BUILD_ROOT/usr/share/pixmaps/cave9.png

%fontinstall
ln -s ../../..%{_datadir}/fonts/%{fontname}-fonts/mutante.ttf $RPM_BUILD_ROOT/usr/share/cave9/hud.ttf


# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://code.google.com/p/cave9/issues/detail?id=38
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">cave9.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A cave exploration game featuring unique controls based on gravity</summary>
  <description>
    <p>
      cave9 is 3D cave exploration game based on the SF-cave game.
      You control a jet that maneuvers through a series of caves and the objective
      of the game is to avoid colliding with the cave walls.
    </p>
  </description>
  <url type="homepage">http://code.google.com/p/cave9</url>
  <screenshots>
    <screenshot type="default">http://cave9.googlecode.com/files/cave9-small.jpg</screenshot>
  </screenshots>
</application>
EOF

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

mv data/README.txt data_README.txt
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  %{SOURCE2}


%check
%fontcheck


%files
%doc AUTHORS.txt README.txt
%license COPYING.txt data_README.txt
%{_bindir}/cave9
%{_datadir}/cave9
%{_datadir}/pixmaps/cave9.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/cave9.desktop


%files -n %{name}-%{fontname}-fonts -f %{fontfilelist}
%{_datadir}/appdata/%{fontname}.metainfo.xml
%license data_README.txt


%changelog
%autochangelog
