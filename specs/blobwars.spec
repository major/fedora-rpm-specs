%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           blobwars
Version:        2.00
Release:        17%{?dist}
Summary:        Mission and Objective based 2D Platform Game
# Code and gfx is all GPLv2+. Music is all CC-BY-SA. SFX are a mix, see readme
# Automatically converted from old format: GPLv2+ and CC-BY-SA and CC-BY and BSD and Public Domain - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Public-Domain
URL:            http://www.parallelrealities.co.uk/p/blob-wars-metal-blob-solid.html
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         blobwars-2.00-Werror.patch
Patch1:         blobwars-2.00-dont-override-strlcat.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ make
BuildRequires:  gettext
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  zlib-devel
Requires:       hicolor-icon-theme

%description
Blob Wars : Metal Blob Solid. This is Episode I of the Blob Wars Saga.
You must undertake the role of fearless Blob solider, Bob, as he infiltrates
various enemy installations and hideouts in an attempt to rescue as many
MIAs as possible.

%prep
%autosetup -p1

# fix permissions
chmod 0644 Makefile*

# SED-FIX-OPENSUSE -- Fix paths and libraries
sed -i -e 's|USEPAK ?= 0|USEPAK ?= 1|;
           s|$(PREFIX)/games|$(PREFIX)/bin|;
           s|$(PREFIX)/share/games|$(PREFIX)/share|;
           s| -Werror||;
           s|$(CXX) $(LIBS) $(GAMEOBJS) -o $(PROG)|$(CXX) $(GAMEOBJS) $(LIBS) -o $(PROG)|;
           s|$(CXX) $(LIBS) $(PAKOBJS) -o pak|$(CXX) $(PAKOBJS) $(LIBS) -o pak|;
           s|$(CXX) $(LIBS) $(MAPOBJS) -o mapeditor|$(CXX) $(MAPOBJS) $(LIBS) -o mapeditor|' Makefile

# SED-FIX-OPENSUSE -- Fix pak
sed -i -e 's|gzclose(pak)|gzclose((gzFile)pak)|;
           s|gzclose(fp)|gzclose((gzFile)fp)|' src/pak.cpp

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" RELEASE=1 DOCDIR=%{_pkgdocdir}/

%install
%make_install DOCDIR=%{_pkgdocdir}/
%find_lang %{name}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

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
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: hdegoede@redhat.com
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">blobwars.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Mission and Objective based 2D Platform Game</summary>
  <description>
    <p>
      Blob Wars: Metal Blob Solid is a 2D side scrolling platformer where you control
      Bob, (a blob secret agent) through 25 missions to rescue other blobs and stop
      the evil alien leader: Galdov.
    </p>
  </description>
  <url type="homepage">http://www.parallelrealities.co.uk/p/blob-wars-metal-blob-solid.html</url>
  <screenshots>
    <screenshot type="default">http://3.bp.blogspot.com/-VGOFb5wKQkE/T4RuJznkWkI/AAAAAAAAA10/u1pyXxBa1yw/s1600/03.jpg</screenshot>
    <screenshot>http://3.bp.blogspot.com/-oBB_IbOXWEI/T4RuI6G3Y5I/AAAAAAAAA1s/_Tb2v1YrINk/s1600/02.jpg</screenshot>
    <screenshot>http://3.bp.blogspot.com/-s0v-Lr5WBa0/T4RuH7DbgKI/AAAAAAAAA1k/58HXOP40NIk/s1600/01.jpg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files -f %{name}.lang
%{_pkgdocdir}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.00-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 28 2023 Hans de Goede <hdegoede@redhat.com> - 2.00-12
- Fix FTBFS (rhbz#2225725)
- Restore honering RPM_OPT_FLAGS, restore debuginfo pkgs
- Drop no longer used bitstream-vera-sans-fonts Requires
- Trim changelog

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
