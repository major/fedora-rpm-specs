Name:		fbg2
Version:	0.4
Release:	35%{?dist}
Summary:	A falling block stacking game
# Code is GPLv2+, music and graphics are CC-BY-SA
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:		http://sourceforge.net/projects/fbg/
# Cannot use this source as is. Need to remove
# fbg2-0.4/Data/Music/FallingBlockGameSndTrk.ogg
# because it is a sound trademark associated with a popular
# falling blocks game.
# rm -rf fbg2-0.4/Data/Music/FallingBlockGameSndTrk.ogg
# Source0:	http://downloads.sourceforge.net/project/fbg/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-clean.tar.gz
# http://www.jamendo.com/en/track/165311/russian
Source1:	RudySeb_-_russian.ogg
Source2:	README.music
# 64 x 64 public domain image for logo
Source3:	fbg2.png
Patch0:		fbg2-0.4-desktop-fix.patch
BuildRequires:  gcc
BuildRequires:	radius-engine-devel >= 0.7, desktop-file-utils, zip
BuildRequires: make
# rhbz#949506, also see rhbz#949167
%if 0%{?fedora} >= 19
Obsoletes:	fbg < 0.9.1-13
Provides:	fbg = 0.9.1-13
%endif

%description
Falling Block Game is a free, open source block stacking game. The object of 
the game is to move and rotate pieces in order to fill in complete rows. The 
more rows you clear at once, the more points you score! 

%prep
%setup -q
%patch -P0 -p1 -b .fix
cp %{SOURCE1} Data/Music/FallingBlockGameSndTrk.ogg
cp %{SOURCE2} .
mv fbg2.png fbg2-small.png
cp %{SOURCE3} .

chmod -x License.txt ChangeLog *.c

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

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
BugReportURL: https://sourceforge.net/p/fbg/feature-requests/12/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">fbg2.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>move the falling blocks to create lines</summary>
  <description>
    <p>
      The Falling Block Game is a game where groups of blocks of certain
      predefined shapes fall from the top of the screen, and the player
      has to rotate and move them to create lines of blocks that then
      disappear when a line is complete.
    </p>
  </description>
  <url type="homepage">http://sourceforge.net/projects/fbg/</url>
  <screenshots>
    <screenshot type="default">http://fbg.sourceforge.net/releases/images/fbg2-v0.4-released/fbgscore2.jpg</screenshot>
  </screenshots>
</application>
EOF

desktop-file-validate %{buildroot}%{_datadir}/applications/fbg2.desktop

%files
%doc License.txt ChangeLog README.music
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4-34
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.4-13
- Add an AppData file for the software center

* Fri Oct 31 2014 Tom Callaway <spot@fedoraproject.org> - 0.4-12
- add 64x64 png icon (bz1157527)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 0.4-8
- rebuild for lua 5.2

* Mon Apr  8 2013 Hans de Goede <hdegoede@redhat.com> - 0.4-7
- Add Obsoletes and Provides fbg (rhbz#949506)

* Tue Apr  2 2013 Tom Callaway <spot@fedoraproject.org> - 0.4-6
- remove sound trademark music

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 4 2012 Tom Callaway <spot@fedoraproject.org> - 0.4-4
- rebuild for new radius-engine

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec  9 2011 Tom Callaway <spot@fedoraproject.org> - 0.4-1
- update to 0.4

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3-3
- Rebuild for new libpng

* Mon Feb 21 2011 Tom Callaway <spot@fedoraproject.org> 0.3-2
- add zip to BuildRequires

* Tue Jan  4 2011 Tom Callaway <spot@fedoraproject.org> 0.3-1
- initial package
