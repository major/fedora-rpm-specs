%global betaver beta3

Name:           celestia
Version:        1.6.2
Release:        0.9.%{betaver}%{?dist}
Summary:        OpenGL real-time visual space simulation
License:        GPLv2+ and CC-BY
# Previously, JPL images, Scott Hudson's asteroid models, and Shrox's Mars rover models were removed.
# This is no longer necessary as their licensing is now open.
# See README-LEGAL.JPL, README-LEGAL.ScottHudsonModels, and README-LEGAL.ShroxModels
Source0:        https://github.com/CelestiaProject/Celestia/archive/%{version}-%{betaver}.tar.gz
Source3:        celestia.desktop
Source4:        README-LEGAL.JPL
Source5:        README-LEGAL.ScottHudsonModels
Source6:        README-LEGAL.ShroxModels
URL:            https://celestia.space/
Patch0:         celestia-1.6.1-gcc47.patch
Patch2:         celestia-1.6.1-lua-5.2.patch
Patch5:         celestia-1.6.1-link-order.patch
Patch6:         celestia-1.6.2-beta3-lua-5.4.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  gtkglext-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  freeglut-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libGLU-devel
BuildRequires:  libXt-devel
BuildRequires:  libXmu-devel
BuildRequires:  lua-devel
BuildRequires:  gettext-devel
BuildRequires:  autoconf, automake, libtool
BuildRequires: make
Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun): GConf2

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Celestia is a real-time space simulation which lets you experience the
universe in three dimensions. Celestia does not confine you to the
surface of the Earth, it allows you to travel throughout the solar
system, to any of over 100,000 stars, or even beyond the galaxy.

Travel in Celestia is seamless; the exponential zoom feature lets
you explore space across a huge range of scales, from galaxy clusters
down to spacecraft only a few meters across. A 'point-and-goto'
interface makes it simple to navigate through the universe to the
object you want to visit.

%prep
%setup -q -n Celestia-%{version}-%{betaver}
# %%patch0 -p1 -b .gcc47
# %%patch2 -p1 -b .lua-52
# %%patch5 -p1 -b .link
%patch6 -p1 -b .lua54

cp %{SOURCE4} %{SOURCE5} %{SOURCE6} .

autoreconf -ifv .

%if 0
# Make sure we compile with the right CFLAGS/CXXFLAGS (from Hans de Goede).
sed -i 's/CFLAGS="\$CFLAGS \$CELESTIAFLAGS \$CELESTIA_CFLAGS"/CFLAGS="\$CFLAGS \$CELESTIAFLAGS"/' configure
sed -i 's/CXXFLAGS="\$CXXFLAGS \$CELESTIAFLAGS \$CELESTIA_CXXFLAGS"/CXXFLAGS="\$CXXFLAGS \$CELESTIAFLAGS"/' configure

# Avoid re-running the autotools
touch -r aclocal.m4 configure configure.in
%endif

# Fix permissions
chmod -x src/celengine/precession.cpp


%build
export GTK_LIBS="$( pkg-config --libs gtkglext-x11-1.0 libgnomeui-2.0 )"
%configure --with-gnome --with-lua
make %{?_smp_mflags}

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %make_install

install -p -m 644 -D src/celestia/kde/data/hi48-app-celestia.png \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/celestia.png
rm $RPM_BUILD_ROOT%{_datadir}/celestia/{controls.txt,COPYING}
ln -s %{_pkgdocdir}/controls.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/
ln -s %{_pkgdocdir}/COPYING $RPM_BUILD_ROOT%{_datadir}/%{name}/
#rm -r $RPM_BUILD_ROOT%%{_datadir}/celestia/manual

install -p -m 644 -D models/*.3ds $RPM_BUILD_ROOT%{_datadir}/%{name}/models/

rm $RPM_BUILD_ROOT%{_datadir}/applications/celestia.desktop

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications            \
  --add-category Application                               \
  --add-category Education                                 \
  %{SOURCE3}

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
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: claurel@gmail.com 
SentUpstream: 2013-09-30
-->
<application>
  <id type="desktop">celestia.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Celestia provides photo-realistic, real-time, three-dimensional viewing of
      the Solar System, the galaxy and the universe.
    </p>
    <p>
      It is an easy to use, freely-distributed, multi-platform, open source,
      software package which has become a valuable tool for astronomy education.
      Used in homes, schools, museums and planetariums around the world, it also
      is used as a visualization tool by space mission designers.
    </p>
  </description>
  <url type="homepage">http://www.shatters.net/celestia/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/celestia/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/celestia/b.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/celestia/c.png</screenshot>
  </screenshots>
  <updatecontact>claurel@gmail.com</updatecontact>
</application>
EOF

%find_lang %{name} --all-name

%pre
if [ "$1" -gt 1 ]; then
    GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` \
        gconftool-2 --makefile-uninstall-rule \
            %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :
    killall -HUP gconfd-2 &>/dev/null || :
fi

%post
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` \
    gconftool-2 --makefile-install-rule \
        %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :

%preun
if [ "$1" -eq "0" ] ; then
    GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` \
        gconftool-2 --makefile-uninstall-rule \
            %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :
    killall -HUP gconfd-2 &>/dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS ChangeLog README controls.txt coding-standards.html
%doc devguide.txt 
%license COPYING README-LEGAL.JPL README-LEGAL.ScottHudsonModels README-LEGAL.ShroxModels
%{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.9.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.8.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.7.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.6.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.5.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Tom Callaway <spot@fedoraproject.org> - 1.6.2-0.4.beta3
- Shrox's models are now CC-BY, switch to upstream tarball!

* Thu Aug 20 2020 Tom Callaway <spot@fedoraproject.org> - 1.6.2-0.3.beta3
- Successfully relicensed Scott Hudson's asteroid models to a FOSS & GPLv2+ compatible license
- generated new clean tarball

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-0.2.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Callaway <spot@fedoraproject.org> - 1.6.2-0.1.beta3
- update to 1.6.2-beta3
- fixes for lua 5.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 23 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.1-32
- Fix FTBFS, fix linkage order

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.6.1-29
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.1-20
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.6.1-19
- Add an AppData file for the software center

* Sun Nov 16 2014 Matias Kreder <mkreder@gmail.com> - 1.6.1-18
- Repackaged source with .tar.xz

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Richard Hughes <richard@hughsie.com> - 1.6.1-16
- Fix startup, thanks to a patch from Chris Rankin
- Resolves: #1045632

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.6.1-14
- FTBS, RHBZ#992048:
  - celestia-1.6.1-lua-5.2.patch: Add autoconf-2.67 generated snippets.
  Avoid running autotools (package config is incompatible to modern autotools).
  - Add celestia-1.6.1-gcc4.8.patch: Tweaks for building with gcc-4.8.x.
- Address docdir changes (RHBZ#993693).
- Fix permissons on source files.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 1.6.1-12
- rebuild for lua 5.2

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.1-11
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- fix desktop file to follow specification

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.6.1-9
- rebuild due to "jpeg8-ABI" feature drop

* Mon Jan 14 2013 Tom Callaway <spot@fedoraproject.org> - 1.6.1-8
- remove non-free (or unlicensed) files (bz 888210)

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.6.1-7
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Tom Callaway <spot@fedoraproject.org> - 1.6.1-5
- fix compile issues (gcc 4.7, zlib)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.6.1-2
- Rebuild for new libpng

* Mon Nov 14 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Hans de Goede <hdegoede@redhat.com> - 1.6.0-2
- Fix the license button in the about dialog not working

* Wed Dec  8 2010 Hans de Goede <hdegoede@redhat.com> - 1.6.0-1
- New upstream release 1.6.0 (#655565)
- Fix building with gcc-4.5 (#631077)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5.1-1
- New upstream release

* Sun Mar  1 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5.0-3
- Fix build with GCC 4.4

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Mar  1 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.5.0-1
- Upstream release 1.5.0 and dropping unnecessary patches
- celestia-1.5.0-gcc43.patch (#434441)
- Moving to education category (#220793)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.1-8
- Autorebuild for GCC 4.3

* Wed Nov 22 2006 Steven Pritchard <steve@kspei.com> 1.4.1-7
- Really fix the cmod models problem (#203525).  (Thanks to Hans de Goede.)
- Hopefully really handle the gconf schema properly.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 1.4.1-6
- Add --disable-schemas-install to configure.

* Tue Aug 22 2006 Steven Pritchard <steve@kspei.com> 1.4.1-5
- Turn on -fno-strict-aliasing to work around bug #203525.

* Mon Jul 31 2006 Steven Pritchard <steve@kspei.com> 1.4.1-4
- We modified configure.in, so now we need automake17 and gettext-devel.

* Mon Jul 31 2006 Nick Urbanik <nicku@nicku.org> 1.4.1-3
- Test errorMessage to see if it is null before copying it!
  This change suggested by Hank Ramsey and added to
  celestia-1.4.1-lua51-resume.patch
- Added developers documentation
- Incorporate patch suggested by Hank Ramsey to eliminate segfault
  when loading .celx files: celestia-1.4.1-lua51-resume.patch
- Update to add lua
- Incorporate
  http://www.archlinux.org/pipermail/tur-users/attachments/20060603/7dea8cd1/celestia-lua51.bin

* Fri May 19 2006 Steven Pritchard <steve@kspei.com> 1.4.1-2
- Include accidentally dropped 3ds models.

* Tue Mar 28 2006 Steven Pritchard <steve@kspei.com> 1.4.1-1
- Update to 1.4.1
- Use "pkg-config --libs gtkglext-x11-1.0 libgnomeui-2.0" instead of
  "pkg-config --libs gtk+-2.0"

* Fri Feb 10 2006 Steven Pritchard <steve@kspei.com> 1.4.0.20060210cvs-1
- Update to today's CVS snapshot

* Fri Feb 10 2006 Steven Pritchard <steve@kspei.com> 1.4.0-3
- Add celestia-1.4.0-compile.patch to fix a bug when compiling with g++ 4.1

* Thu Jan 05 2006 Steven Pritchard <steve@kspei.com> 1.4.0-2
- Add BR: libGLU-devel, libXt-devel, libXmu-devel
- Add -lpangox-1.0 to GTK_LIBS

* Mon Dec 26 2005 Steven Pritchard <steve@kspei.com> 1.4.0-1
- Update to 1.4.0
- Remove celestia-1.3.2-compile.patch (seems to be applied upstream)
- Use find_lang magic
- Remove duplicate desktop file
- Fix Help -> Controls

* Sat Dec 03 2005 Steven Pritchard <steve@kspei.com> 1.3.2-5
- BR libGL-devel instead of xorg-x11-Mesa-libGL

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.3.2-4
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-2
- Bump release to provide Extras upgrade path.

* Wed Nov 10 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.3.2-0.fdr.2
- Fixed FC3 compilation.

* Sat Aug 28 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.3.2-0.fdr.1
- Updated to 1.3.2.
- Switched to using GNOME frontend.
- Updated desktop file.
- Minor editing of description text.
- Converted spec file to UTF-8.

* Thu Nov 27 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.3.0-0.fdr.4
- Added build req gtkglarea (bug 740).

* Thu Nov 27 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.3.0-0.fdr.3
- Added Encoding=UTF-8 to desktop file (bug 740).
- Added work-around for linking problems on FC1 (bug 740).
- Updated {minor,numbered}moons.asc (bug 740).

* Wed Oct  8 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.3.0-0.fdr.2
- Replaced source tarball with proper release tarball.
- Added BuildRequires gnome-libs-devel for gnomeConf.sh.
- Build with freeglut instead of glut.

* Wed Sep 17 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.3.0-0.fdr.1
- Initial Fedora RPM release.

* Thu Apr 17 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.0.
- Added numberedmoons.ssc addon.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.

* Tue Jan 14 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.5.
- Included "Minor Moons of the Giant Planets" extra file.
- New icon from the KDE part of the source.

* Sat Sep 28 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.
- New style menu entry.

* Wed Jul  3 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt to remove the NVidia dependency (oops!).

* Wed May 15 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Sorry, I'm a maniac ;-)

* Tue May 14 2002 Julien MOUTTE <julien@moutte.net>
- Initial RPM release.
