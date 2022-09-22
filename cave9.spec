%global fontname mutante
%global fontconf 64-%{name}-%{fontname}.conf

Name:           cave9
Version:        0.4
Release:        27%{?dist}
Summary:        3d game of cave exploration

License:        LGPLv3 and CC-BY-SA and Public Domain
URL:            http://code.google.com/p/cave9
Source0:        http://cave9.googlecode.com/files/cave9_src-%{version}.tgz
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
License:        CC-BY
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
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.4-12
- Add an AppData file for the software center

* Tue Nov 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4-11
- Add metainfo file to show mutante font in gnome-software
- Added fontname macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Richard Hughes <richard@hughsie.com> - 0.4-9
- Install the application icon in a standard location to fix display in
  gnome-software and Apper.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.4-6
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 04 2010 Victor Bogado da Silva Lins <victor@bogado.net> 0.4-1
- new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Victor Bogado <victor@bogado.net> 0.3-8
- removed the redundant ownership of the fontdir.
- lowered the priority
- Updated the font configuration to better match the suggested template.

* Tue Jun 23 2009 Victor Bogado <victor@bogado.net> 0.3-7
- following the tips from Nicolas Mailhot on bug#477371

* Mon Jun 22 2009 Victor Bogado <victor@bogado.net> 0.3-6
- adapted the font subpackge to the new template on Fedora 11

* Wed Jan 14 2009 Victor Bogado <victor@bogado.net> 0.3-5
- Added a fontconfig file.
- Renamed the font file subpackage to follow the font package naming convention.

* Tue Dec 30 2008 Victor Bogado <victor@bogado.net> 0.3-4
- Separate the font into a new package.

* Sun Nov 09 2008 Victor Bogado <victor@bogado.net> 0.3-3
- Use install -m 755 to ensure correct mode for binaries.
- Final dot missing on description.
- Missing "Public Domain" for nasa data files.

* Fri Nov 07 2008 Victor Bogado <victor@bogado.net> 0.3-2
- better description
- use of macros
- BuildRequires was missing 'desktop-file-utils'
- Flag to preserve timestamps on 'cp'

* Mon Sep 15 2008 Victor Bogado <victor@bogado.net> 0.3-1
- update version and data file.
- new data file is now compleatly free.

* Sat Apr 19 2008 Victor Bogado <victor@bogado.net> 0.2-2
- Use the compiler flags from fedora

* Wed Apr 16 2008 Victor Bogado <victor@bogado.net> 0.2-1
- initial spec
