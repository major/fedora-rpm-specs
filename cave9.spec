%global fontname mutante
%global fontconf 64-%{name}-%{fontname}.conf

%global forgeurl https://github.com/bart9h/cave9
%global tag 0.4.1
%forgemeta

Name:           cave9
Version:        %{tag}
Release:        %autorelease
Summary:        3d game of cave exploration

License:        LGPL-3.0-only AND CC-BY-SA-2.5 AND CC-BY-SA-3.0 AND LicenseRef-Fedora-Public-Domain
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        http://cave9.googlecode.com/files/cave9_data-4.tgz
Source2:        cave9.desktop
Source4:        %{fontname}.metainfo.xml

BuildRequires:  gcc
BuildRequires:  SDL_image-devel, SDL_net-devel, SDL_ttf-devel, mesa-libGL-devel, desktop-file-utils, fontpackages-devel
BuildRequires: make
Requires:       cave9-%{fontname}-fonts


%description
Cave9 is a gravity cave-exploration game.

%package        %{fontname}-fonts

Summary:        Mutante font used by the HUD in cave9 game
BuildArch:      noarch
License:        CC-BY-SA-2.5
Requires:       fontpackages-filesystem
Source3:        %{name}-%{fontname}-fontconfig.conf

%description %{fontname}-fonts
Fantasy/display font used by the cave9 game, this font has only the basic
characters used in the Portuguese language was made as an experiment by the
designer Jonas Kühner (http://www.criatipos.com/) the font was altered by
the game developer to also include numbers.

%_font_pkg -n %{fontname} -f %{fontconf} %{fontname}.ttf
%doc data_README.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%prep
%setup -q -a1
sed -i src/GNUmakefile -e "s/-Wall -Werror -ggdb//"

%build
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/bin %{buildroot}/usr/share/cave9
install -m 755 -p cave9 $RPM_BUILD_ROOT/usr/bin
cp -p data/wall.jpg data/icon.png data/thrust.wav data/crash.wav data/hit.wav $RPM_BUILD_ROOT/usr/share/cave9

mkdir -p %{buildroot}/usr/share/pixmaps
cp -p data/icon.png $RPM_BUILD_ROOT/usr/share/pixmaps/cave9.png

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p data/*.ttf %{buildroot}%{_fontdir}/mutante.ttf

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

ln -s ../../..%{_fontdir}/mutante.ttf $RPM_BUILD_ROOT/usr/share/cave9/hud.ttf

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

%files
%doc AUTHORS.txt README.txt COPYING.txt data_README.txt
%{_bindir}/cave9
%{_datadir}/cave9
%{_datadir}/pixmaps/cave9.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/cave9.desktop

%changelog
%autochangelog
