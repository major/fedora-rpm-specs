Name:           pioneers
Version:        15.6
Release:        12%{?dist}
Summary:        Turnbased board strategy game (colonize an island)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pio.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pio/%{name}-%{version}.tar.gz
Patch0:         pioneers-15.6-sanitize.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libgnome-devel gtk2-devel gettext scrollkeeper intltool
BuildRequires:  itstool
BuildRequires:  perl(XML::Parser) desktop-file-utils
Requires:       hicolor-icon-theme
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
Pioneers is a computerized version of a well known strategy board game. The
goal of the game is to colonize an island. The players play the first
colonists hence the name pioneers.

Pioneers is a networkbased multiplayer game, this package contains the GUI
client as well as both a GUI and CLI version of the server for local games.


%package editor
Summary:        Pioneers Game Editor
Requires:       pioneers = %{version}-%{release}

%description editor
Pioneers is a computerized version of a well known strategy board game. The
goal of the game is to colonize an island. The players play the first
colinists hence the name pioneers.

The game editor allows maps and game descriptions to be created and
edited graphically.


%prep
%autosetup -p1

%build
# pioneers uses some GNU extensions
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

# Remove the too much like the original splashscreen
rm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}/splash.png

# Reinstall the .desktop files
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-editor.desktop \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-server-gtk.desktop

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
<!-- Copyright 2014 Eduardo Mayorga <e@mayorgalinux.com> -->
<!--
BugReportURL: https://sourceforge.net/p/pio/bugs/286/
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">pioneers.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Multiplayer board game inspired by The Settlers of Catan</summary>
  <description>
    <p>
      Pioneers is a free videogame implementation of the famous German game Settlers of Catan.
      The goal is to build towns, cities and roads on a board that is different every time, while accumulating various types of cards.
      It can be played online.
    </p>
  </description>
  <url type="homepage">http://pio.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://pio.sourceforge.net/screenshots0.11/client.png</screenshot>
  </screenshots>
</application>
EOF

%check
if grep Catan `find $RPM_BUILD_ROOT ! -path "$RPM_BUILD_ROOT/usr/src/debug*"`;
  then
  exit 1
fi



%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%postun
scrollkeeper-update -q || :


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README NEWS
%{_bindir}/%{name}
%{_bindir}/%{name}ai
%{_bindir}/%{name}-metaserver
%{_bindir}/%{name}-server-console
%{_bindir}/%{name}-server-gtk
%{_datadir}/games/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/help/C/%{name}
%{_mandir}/man6/%{name}*.6.gz
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-server-gtk.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-server.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-server.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-server.svg
%{_datadir}/icons/hicolor/scalable/actions/%{name}*.svg


%files editor
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{name}-editor.desktop
%{_datadir}/pixmaps/%{name}-editor.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-editor.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}-editor.svg

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 15.6-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Avram Lubkin <aviso@rockhopper.net> - 15.6-1
+- Updated to 15.6

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Than Ngo <than@redhat.com> - 15.5-3
- fix FTBFS against gcc10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 Avram Lubkin <aviso@rockhopper.net> - 15.5-1
+- Updated to 15.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 15.3-2
- Add an AppData file for the software center

* Mon Oct 27 2014 Paul W. Frields <stickster@gmail.com> - 15.3-1
- Update to upstream 15.3 (#1018594)
- Notes: http://sourceforge.net/p/pio/news/2014/10/pioneers-153-released/

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 14.1-4
- Removed --vendor from desktop-file-install for F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul  6 2012 Paul W. Frields <stickster@gmail.com> - 14.1-1
- New upstream version 14.1
- Details: http://sourceforge.net/mailarchive/message.php?msg_id=29324203
- Update sanitize patch, remove obsolete user name change patch

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.12.4-2
- Rebuild for new libpng

* Fri Jul 29 2011 Paul W. Frields <stickster@gmail.com> - 0.12.4-1
- Update to upstream 0.12.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug  5 2010 Paul W. Frields <stickster@gmail.com> - 0.12.3-2
- Fix callback for name changes (#594858)

* Mon Feb 15 2010 Paul W. Frields <stickster@gmail.com> - 0.12.3-1
- New upstream release 0.12.3
- Add patch for new default linker DSO behavior

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 0.12.2-2
- Fix patch fuzz build failure

* Fri May  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.12.2-1
- New upstream release 0.12.2

* Mon Apr 28 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.12.1-1
- New upstream release 0.12.1

* Wed Feb 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.11.3-4
- Fix building with latest glibc
- Rebuild for gcc-4.3

* Tue Dec 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.11.3-3
- Fix CVE-2007-6010 (potential server DOS)

* Thu Nov 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.11.3-2
- Also sanitize the .po files just to be sure
- Remove bogus pkgdatadir argument to make install
- Add %%check section
- Leave the icons in /usr/share/pixmaps so that the window icons work

* Tue Nov 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.11.3-1
- Initial Fedora Package
