Name:           hexglass
Version:        1.2.1
Release:        35%{?dist}
Summary:        Block falling puzzle game based on a hexagonal grid 
Summary(de):    Puzzlespiel mit fallenden Blöcken auf einem sechseckigen Raster

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://code.google.com/p/hexglass
Source0:        http://hexglass.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

# Let the application search for locale files in
# /usr/share/hexglass/translations/
Patch0:         %{name}-%{version}-locale-path.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt4-devel
BuildRequires: make

%description
HexGlass is a Tetris-like puzzle game. Ten different types of blocks 
continuously fall from above and you must arrange them to make horizontal 
rows of hexagonal bricks. Completing any row causes those hexagonal blocks 
to disappear and the rest above move downwards. The blocks above gradually 
fall faster and the game is over when the screen fills up and blocks can 
no longer fall from the top. 

%description -l de
HexGlass ist ein Tetris-ähnliches Puzzlespiel. Zehn verschiedene Blocktypen
fallen fortwährend nach unten und müssen so angeordnet werden, dass horizontale
Zeilen aus sechseckigen Elementen gebildet werden. Nach Vervollständigen einer
Zeile verschwinden die Blöcke, wodurch die übrigen nach unten verschoben
werden. Mit steigendem Schwierigkeitsgrad fallen die Blöcke schneller. 
Das Spiel ist vorbei, sobald das Spielfeld vollständig gefüllt ist und keine 
Blöcke mehr fallen können.

%prep
%setup -q
%patch -P0 -p1


%build
%{qmake_qt4} hexglass.pro
make %{?_smp_mflags}


%install
install -D hexglass %{buildroot}%{_bindir}/hexglass
install -d %{buildroot}%{_datadir}/%{name}/translations
install -m 644 -p translations/*.qm %{buildroot}%{_datadir}/%{name}/translations
install -D -m 644 -p resources/about_icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

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
<!-- Copyright 2014 Tim Waugh <twaugh@redhat.com> -->
<!--
BugReportURL: https://code.google.com/p/hexglass/issues/detail?id=1
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">hexglass.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Drop shapes to the bottom without leaving gaps</summary>
  <description>
    <p>
      In HexGlass the object is to rotate shaped pieces as the fall to the bottom
      so that they don't leave gaps.
      The pieces are made of small numbers of hexagons stuck together, and it is
      hard to work out the right way to rotate each piece as there are 6
      possible orientations.
    </p>
    <p>
      When a row is completed without any gaps, it is removed and all the
      hexagonal blocks above it move down one row.
      As the pieces fall faster, make sure not to let the screen fill up!
    </p>
  </description>
  <url type="homepage">http://code.google.com/p/hexglass</url>
  <screenshots>
    <screenshot type="default">http://hexglass.googlecode.com/svn/wiki/preview.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name} --with-qt

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}


%files -f %{name}.lang
%doc CHANGES COPYING README
%{_bindir}/hexglass
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-34
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Martin Gieseking <martin.gieseking@uos.de> - 1.2.1-19
- Added BR: gcc-c++ according to new packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.2.1-13
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.1-11
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.2.1-10
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 29 2011 Martin Gieseking <martin.gieseking@uos.de> 1.2.1-3
- added German summary and description

* Fri Jul 29 2011 Martin Gieseking <martin.gieseking@uos.de> 1.2.1-2
- added Group
- changed GenericName in .desktop file to "Block falling game"

* Tue Jul 26 2011 Martin Gieseking <martin.gieseking@uos.de> 1.2.1-1
- initial package

