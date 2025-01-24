# If we have a prerelease version we can define it here
%global prever beta1

Name:           openttd
Version:        15.0
Release:        %autorelease -p -e %{prever}
Summary:        Transport system simulation game

# bundled squirrel is under Zlib license
# bundled fmt is under MIT license
License:        GPL-2.0-only AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND Zlib
URL:            https://www.openttd.org
Source0:        https://cdn.openttd.org/openttd-releases/%{version}%{?prever:-%{prever}}/%{name}-%{version}%{?prever:-%{prever}}-source.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  grfcodec
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libpng-devel
BuildRequires:  lzo-devel
BuildRequires:  SDL2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

Requires:       hicolor-icon-theme
# src/3rdparty/squirrel is https://github.com/albertodemichelis/squirrel
# But modified for use of OpenTTD
Provides:       bundled(squirrel) = 2.2.5~openttd
# https://github.com/OpenTTD/OpenTTD/issues/11403
# src/3rdparty/fmt is https://github.com/fmtlib/fmt
Provides:       bundled(fmt) = 7.1.3

Recommends:     openttd-opengfx => 0.5.0
Recommends:     fluid-soundfont-gm

%description
OpenTTD is modeled after a popular transportation business simulation game
by Chris Sawyer and enhances the game experience dramatically. Many features
were inspired by TTDPatch while others are original.


%package docs
Summary:        Documentation for OpenTTD
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description docs
Development documentation for OpenTTD. Includes information on how to program
the AI.


%prep
%autosetup -p1 -n %{name}-%{version}%{?prever:-%{prever}}

sed -i "s|/usr/share|%{_datadir}|g" src/music/fluidsynth.cpp

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_BINDIR=bin \
    -DCMAKE_INSTALL_DATADIR=%{_datadir} \
    -DGLOBAL_DIR:PATH=%{_datadir}/%{name}

%cmake_build

%install
%cmake_install

# Remove the installed docs - we will install subset of those
rm -rf $RPM_BUILD_ROOT%{_docdir}

# install documentation
install -dpm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/docs/
cp -a docs/* $RPM_BUILD_ROOT%{_datadir}/%{name}/docs/
# this is installed into the proper path earlier
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/docs/%{name}.6


desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
        --add-category=StrategyGame \
        $RPM_BUILD_ROOT%{_datadir}/applications/openttd.desktop

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
<!-- Copyright 2014 Ankur Sinha <ankursinha@fedoraproject.org> -->
<!--
EmailAddress: alberth@openttd.org
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">openttd.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A highly detailed transport simulation game</summary>
  <description>
  <p>
      OpenTTD is a transport tycoon simulation game that enhances the
      original Transport Tycoon game developed by Chris Sawyer.
      The game includes road, air, train and naval transport with a large
      selection of industries and passenger services that need to be provided.
    </p>
  <p>
      The game can be played in both single and multiplayer modes where
      you compete with other transport companies to dominate the markets.
  </p>
  </description>
  <url type="homepage">https://www.openttd.org</url>
  <screenshots>
    <screenshot type="default">https://www.openttd.org/screenshots/1.4-02-opengfx-1920x1200.png</screenshot>
    <screenshot>https://www.openttd.org/screenshots/1.9-darkuk-3.png</screenshot>
  </screenshots>
  <updatecontact>info@openttd.org</updatecontact>
</application>
EOF

%files
%license COPYING.md
%doc changelog.md CONTRIBUTING.md CREDITS.md known-bugs.md README.md
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.32.xpm
%{_datadir}/pixmaps/%{name}.64.xpm
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%exclude %{_datadir}/%{name}/docs

%files docs
# These are really devel docs, but as we don't have -devel subpackage, we put it here
# Could be useful for people making graphics, AI scripts or translations
%{_datadir}/%{name}/docs/


%changelog
%autochangelog
