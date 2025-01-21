Name:           uqm
Version:        0.8.0
Release:        6%{?dist}
Summary:        The Ur-Quan Masters, a port of the classic game Star Control II

# Upstream claims everything to be under GPL-2.0-or-later.
# In reality, the source contains many files copied from other projects,
# with a variety of open source licenses.
License:        GPL-2.0-or-later AND GPL-2.0-only AND LGPL-2.1-or-later AND Zlib
URL:            http://sc2.sourceforge.net/
Source0:        http://download.sf.net/sc2/%{name}-%{version}-src.tgz
Source1:        %{name}.conf
Source2:        %{name}.sh
Source3:        %{name}.desktop
Source4:        %{name}-functions.sh
Source5:        %{name}.autodlrc
Patch0:         %{name}-optflags.patch

BuildRequires:  SDL-devel >= 1.2.8
BuildRequires:  SDL_image-devel >= 1.2.4
BuildRequires:  ImageMagick
BuildRequires:  libvorbis-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libGLU-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libpng-devel
BuildRequires:  gcc
Requires:       autodownloader
Provides:       uqm-content = %{version}-%{release}
Provides:       uqm-content-3domusic = %{version}-%{release}
Provides:       uqm-content-voice = %{version}-%{release}
Obsoletes:      uqm-content <= 0.6.0-2
Obsoletes:      uqm-content-3domusic <= 0.6.0-2
Obsoletes:      uqm-content-voice <= 0.6.0-2


%description
The Ur-Quan Masters is a port of the classic game Star Control II to
modern systems.  The program code that comprises The Ur-Quan Masters
was derived from code written by Toys for Bob, Inc. for the 3DO
version of Star Control II, with their permission and encouragement.


%prep
%setup -qn uqm-0.8.0
find -type d -name CVS -exec rm -rf {} ';'
%patch -P0 -p0

%build
echo INPUT_install_sharedir_VALUE=%{_datadir} > config.state
sed -i 's|@CONTENTDIR@|~/.uqm|g' src/config_unix.h.in
sh ./build.sh uqm < /dev/null
convert src/res/ur-quan-icon-std.ico uqm.png


%install

install -dm 755 $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}}
sed -e 's|/etc/|%{_sysconfdir}/|' %{SOURCE1} > \
  $RPM_BUILD_ROOT%{_sysconfdir}/uqm.conf
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/uqm.conf
sed -e 's|/usr/games/|%{_prefix}/games/|' %{SOURCE2} \
  > $RPM_BUILD_ROOT%{_bindir}/uqm
chmod 755 $RPM_BUILD_ROOT%{_bindir}/uqm

install -Dpm 755 uqm $RPM_BUILD_ROOT%{_prefix}/games/uqm

install -dm 755 \
  $RPM_BUILD_ROOT%{_datadir}/uqm/content/packages/addons
echo %{version} > $RPM_BUILD_ROOT%{_datadir}/uqm/content/version

desktop-file-install \
  --mode 644 \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
 %{SOURCE3}
install -Dpm 644 uqm-5.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/uqm.png

# needed "data" files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE4} %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}

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
<!-- Copyright 2014 Luya Tshimbalanga <luya@fedoraproject.org> -->
<!--
BugReportURL: https://bugs.uqm.stack.nl/show_bug.cgi?id=1199
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">uqm.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Classic space adventure game</summary>
  <description>
    <p>
    A port of classic game Star Control II that includes adventure and melee
    mode with enhancement for modern system.
    </p>
  </description>
  <url type="homepage">http://sc2.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://sc2.sourceforge.net/screenshots/meleestep.png</screenshot>
    <screenshot>http://sc2.sourceforge.net/screenshots/scale_triscan.png</screenshot>
    <screenshot>http://sc2.sourceforge.net/screenshots/slaveshield.png</screenshot>
  </screenshots>
</application>
EOF

%files
%license COPYING
%doc AUTHORS ChangeLog Contributing README
%doc WhatsNew doc/users/manual.txt
%config(noreplace) %{_sysconfdir}/uqm.conf
%{_bindir}/uqm
%{_prefix}/games/uqm
%{_datadir}/uqm/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/uqm.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Otto Liljalaakso <otto.liljalaakso@iki.fi> - 0.8.0-2
- License review, migrate to SPDX license ids

* Sat Jan 28 2023 Otto Liljalaakso <otto.liljalaakso@iki.fi> - 0.8.0-1
- Update to 0.8.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.0-16
- Updated upstream.

* Tue Jan 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.0-15
- Rename internal strings.h to fix FTBFS.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.7.0-9
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-5
- Drop desktop vendor tag.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Jon Ciesla <limb@jcomserv.net> - 0.7.0-2
- Corrected autodl file.

* Thu Nov 17 2011 Jon Ciesla <limb@jcomserv.net> - 0.7.0-1
- Updated to 0.7.0 release based on Solomon Peachy's changes from BZ 735956.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 28 2010 Jon Ciesla <limb@jcomserv.net> - 0.6.2-11
- Fix for autodl urls, BZ 494465.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.2-9
- Fix for content location (#505489)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.2-7
- forgot a few obsoletes/provides

* Thu Sep 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.2-6
- properly Provide/Obsolete dead uqm-content package

* Wed Sep 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.2-5
- drop /usr/share/games/uqm to /usr/share/uqm

* Wed Sep 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.2-4
- convert package to use autodownloader
- look for content in user homedir

* Sun Feb 17 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.2-3
- Rebuild for newer mikmod.

* Tue Aug 21 2007 Warren Togami <wtogami@redhat.com> - 0.6.2-2
- rebuild

* Thu Apr 19 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.2-1.1
- Rebuild for newer mikmod.

* Fri Jan 26 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.2-1
- Upstream 0.6.2.
- Require uqm-content >= 0.6, since 0.6.0 has not changed.

* Fri Dec 22 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.0-1
- Upstream 0.6.0
- Don't exclude 64-bit arches
- BR: mikmod-devel

* Sun Sep 03 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.5.0-1.1
- FC6 rebuild

* Mon Feb  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.0-1
- 0.5.0.

* Thu Jun  2 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.4.0-2
- Exclude 64-bit archs (#158705).

* Sun May 22 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.4.0-1
- 0.4.0, most patches applied upstream.
- Make install layout FHS compliant.
- Make compiled in default content dir point to the right place.

* Fri Mar 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3-4
- Fix FC4 build.

* Sat Dec 11 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.3-3
- Fix build on FC3.
- Improve comment in desktop entry file, add Finnish translation.

* Thu Jun 17 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.3-0.fdr.2
- Add upstream patch to fix all blue comms screen (bug 1751, upstream bug 363).

* Sat Sep  6 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.3-0.fdr.1
- Update to 0.3.
- Update description.
- Don't use libexecdir, it's not FHS compliant.

* Mon Jul  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.2-0.fdr.3
- Use desktop-file-utils.
- Spec cleanups.

* Sat Apr 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.2-0.fdr.2
- Add missing Epochs.
- Save .spec in UTF-8.

* Sun Mar 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.2-0.fdr.1
- First Fedora release.
- Update to 0.2.
- Separate content packages.
- Add patch for system default and per-user configurations.
- Move towards FHS compliant installation layout.
- Include icon for desktop entry.

* Sun Dec  1 2002 Ville Skyttä <ville.skytta at iki.fi> - 0.1-1cr
- Initial build.
