Name:           pingus
Version:        0.7.6
Release:        50%{?dist}
Summary:        Guide the penguins safely home before they drop of the cliff
License:        GPL-2.0-or-later
URL:            http://pingus.seul.org/
Source0:        http://pingus.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:        pingus.desktop
Source2:        pingus.png
Patch1:         pingus-0.7.6-gcc470-udl.patch
Patch2:         pingus-0.7.6-missing-header.patch
Patch3:         pingus-0.7.6-boost-169.patch
Patch4:         pingus-0.7.6-python3.patch
Patch5:         pingus-gcc13.patch
Patch6:         includes.patch
BuildRequires: make
BuildRequires:  SDL_mixer-devel SDL_image-devel boost-devel libpng-devel
BuildRequires:  physfs-devel python3-scons desktop-file-utils gcc-c++
Requires:       hicolor-icon-theme

%description
You take command in the game of a bunch of small penguins
and have to guide them around in levels. Since the penguins
walk on their own, the player can only influence them by giving them commands,
like build a bridge, dig a hole or redirect all penguins in the other
direction. The goal of each level is to reach the exit, for which multiple
combination of commands are necessary. The game is presented in a 2D site view.


%prep
%setup -q
%patch -P 1 -p0
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p0
%patch -P 5 -p1
%patch -P 6 -p0
iconv -f ISO8859-2 -t UTF8 AUTHORS > AUTHORS.tmp
mv AUTHORS.tmp AUTHORS


%build
scons CCFLAGS="$RPM_OPT_FLAGS -std=gnu++17" LINKFLAGS="$RPM_LD_FLAGS"


%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT
install -p -m 644 doc/man/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6/
rm -rf $RPM_BUILD_ROOT%{_mandir}/man1/

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

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
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
EmailAddress: grumbel@gmail.com
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">pingus.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Free version of Lemmings Puzzle Game</summary>
  <description>
    <p>
      Pingus is a Puzzle game where you need to save all your little penguins
      using the capabilities provided to you in the current level.
    </p>
    <p>
      The basic game idea is to be like Lemmings game.
      This versions has some other cool
      stuff like a world map and some very cool secret levels.
    </p>
  </description>
  <url type="homepage">http://pingus.seul.org/</url>
  <screenshots>
    <screenshot type="default">http://pingus.seul.org/images/screen_0.7.0-4.jpg</screenshot>
    <screenshot>http://pingus.seul.org/images/screen_0.7.0-3.jpg</screenshot>
  </screenshots>
  <launchable type="desktop-id">pingus.desktop</launchable>
</application>
EOF

%files
%license COPYING
%doc AUTHORS NEWS README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}.bin
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.7.6-46
- Update appdata

* Wed Nov 01 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.7.6-45
- Respect default linker flags

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.7.6-43
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.6-35
- Fix FTBFS.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.7.6-32
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.7.6-29
- Rebuilt for Boost 1.66

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.6-28
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.7.6-25
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 0.7.6-24
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jonathan Wakely <jwakely@redhat.com> - 0.7.6-21
- Rebuilt for Boost 1.63 and patched for GCC 7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.7.6-19
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.7.6-18
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-17
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.7.6-16
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.7.6-14
- Add an AppData file for the software center

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.7.6-13
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.7.6-10
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.7.6-8
- Rebuild for boost 1.54.0

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.6-7
- Drop desktop vendor tag.

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.7.6-6
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.7.6-5
- Rebuild for Boost-1.53.0

* Thu Jul 26 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.6-4
- Rebuild for boost 1.50.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for c++ ABI breakage

* Tue Jan 03 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.6-1
- New upstream.
- binsh patch upstreamed.
- Patch for gcc 4.7.0 user defined literal.

* Mon Nov 21 2011 Jon Ciesla <limb@jcomserv.net> - 0.7.4-4
- Rebuild for new Boost.

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 0.7.4-3
- Rebuild for libpng 1.5.

* Mon Oct 31 2011 Jon Ciesla <limb@jcomserv.net> - 0.7.4-2
- Patched Makefile to fix bogus dep.

* Thu Oct 20 2011 Jon Ciesla <limb@jcomserv.net> - 0.7.4-1
- New upstream.

* Thu Jul 21 2011 Jon Ciesla <limb@jcomserv.net> - 0.7.3-1
- New upstream, Boost rebuild.
- Dropped gcc44 patch, upstreamed.

* Fri Apr 08 2011 Jon Ciesla <limb@jcomserv.net> - 0.7.2-14
- Boost rebuild.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.7.2-12
- rebuild for new boost

* Thu Jul 29 2010 Bill Nottingham <notting@redhat.com> - 0.7.2-11
- Rebuild for boost-1.44, again

* Tue Jul 27 2010 Bill Nottingham <notting@redhat.com> - 0.7.2-10
- Rebuild for boost-1.44

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7.2-9
- Rebuild for Boost soname bump

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Hans de Goede <hdegoede@redhat.com> 0.7.2-7
- Update description for new trademark guidelines

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Rafał Psota <rafalzaq@gmail.com> - 0.7.2-5
- Fix compiling with gcc 4.4

* Wed Dec 17 2008 Benjamin Kosnik  <bkoz@redhat.com> - 0.7.2-4
- Rebuild for boost-1.37.0.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.2-3
- Autorebuild for GCC 4.3

* Wed Jan  9 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.2-2
- New upstream release 0.7.2
- Fix compiling with gcc 4.3

* Sun Sep 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.1-1
- New upstream release 0.7.1

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.0-1
- New upstream release 0.7.0 final
- This changes pingus from a ClanLib app into an SDL app
- Drop patch to switch pingus translations to gettext as it has been rejected
  by upstream, instead use pingus' own translation system  

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.0-0.5.20060721
- Update License tag for new Licensing Guidelines compliance

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.0-0.4.20060721
- FE6 Rebuild

* Sun Aug 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.0-0.3.20060721
- Rebuild for new ClanLib

* Sun Jul 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.0-0.2.20060721
- add missing BR: gettext

* Fri Jul 21 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.0-0.1.20060721
- initial Fedora Extras package
