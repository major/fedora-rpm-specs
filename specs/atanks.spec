Name:           atanks
Version:        6.6
Release:        7%{?dist}
Summary:        Remake of a classic DOS game "Scorched Earth"

License:        GPL-2.0-or-later
URL:            http://atanks.sourceforge.net/
Source0:        http://download.sourceforge.net/atanks/atanks-%{version}.tar.gz

# atanks upstream adds "-march=native -O2" to CXXFLAGS which may affect Fedora
# optimization flags. Also not every platform has -march=native option.
Patch0:         atanks-remove-cxxflags-mangling.patch


BuildRequires:  allegro-devel, desktop-file-utils, gcc-c++
BuildRequires: make
Requires:	hicolor-icon-theme

%description
Atomic Tanks is a game in which you control an overly-powerful
tank and attempt to blow up other highly powerful tanks. Players
get to select a number of weapons and defensive items and then
attack each other in a turn-based manner. The last tank standing
is the winner.


%prep
%setup -q
%patch -P0 -p1

%build
PREFIX=%{_prefix} CXXFLAGS="%{optflags}" LDFLAGS="$RPM_LD_FLAGS" make %{?_smp_mflags} DEBUG=NO

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 0755 \
    $RPM_BUILD_ROOT%{_datadir}/games/atanks \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps \
    $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m 0644 *.txt $RPM_BUILD_ROOT%{_datadir}/games/atanks/
install -p -m 0644 unicode.dat $RPM_BUILD_ROOT%{_datadir}/games/atanks/
install -p -m 0755 atanks $RPM_BUILD_ROOT%{_bindir}/atanks
install -p -m 0644 atanks.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 atanks.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

cp -pr button exporter misc missile sound stock tank tankgun text title $RPM_BUILD_ROOT%{_datadir}/games/atanks/ 
desktop-file-install \
    --mode 0644 \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
    --add-category StrategyGame \
    atanks.desktop

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
<!-- HOUSEKEEPING FOR RICHARD, REMOVE THIS COMMENT WHEN THIS GOES UPSTREAM
BugReportURL: jessefrgsmith@yahoo.ca
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">atanks.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Turn-based artillery strategy game</summary>
  <description>
    <p>
      Atomic Tanks is a turn based artillery strategy game where opponents
      take turns to bombard each other with a wide array of different weapons.
      To make things more interesting, Atomic Tanks also features desctructable
      landscapes, teleporting, parachutes and different weather conditions.
    </p>
  </description>
  <url type="homepage">http://atanks.sourceforge.net/index.html</url>
  <screenshots>
    <screenshot type="default">http://atanks.sourceforge.net/Screenshots/scrnshot29.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files
%license COPYING
%doc Changelog README TODO
%dir %{_datadir}/games/atanks
%{_datadir}/games/atanks/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%{_bindir}/atanks


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 6.6-2
- migrated to SPDX license

* Thu Jan 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 6.6-1
- 6.6

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.5-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Jonathan Ciesla <limburgher@gmail.com> - 6.5-1
- 6.5

* Wed Apr 27 2016 Jonathan Ciesla <limburgher@gmail.com> - 6.4-3
- Drop atanks.sh, not longer needed, and spec cleanup.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Jonathan Ciesla <limburgher@gmail.com> - 6.4-1
- Latest upstream.

* Wed Dec 02 2015 Jonathan Ciesla <limburgher@gmail.com> - 6.3-4
- BR fix, BZ 1230470.

* Thu Sep 24 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 6.3-3
- removed upstream mangling of CXXFLAGS to build on secondary archs - rhbz#1251422

* Wed Aug 12 2015 Ville Skyttä <ville.skytta@iki.fi> - 6.3-2
- Build with $RPM_OPT/LD_FLAGS again, mark COPYING as %%license

* Tue Aug 04 2015 Jonathan Ciesla <limburgher@gmail.com> - 6.3-1
- 6.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr 06 2015 Jonathan Ciesla <limburgher@gmail.com> - 6.2-1
- 6.2
- Fixed atanks.sh --nothread flag.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 6.1-2
- Add an AppData file for the software center

* Fri Dec 19 2014 Jonathan Ciesla <limburgher@gmail.com> - 6.1-1
- 6.1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Jonathan Ciesla <limburgher@gmail.com> - 6.0-1
- 6.0

* Mon Mar 31 2014 Jonathan Ciesla <limburgher@gmail.com> - 5.9-1
- 5.9

* Mon Jan 27 2014 Jonathan Ciesla <limburgher@gmail.com> - 5.8-1
- 5.8, fixes for some gcc-specific crashes.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Jonathan Ciesla <limburgher@gmail.com> - 5.7-1
- New upstream, fix for Options crash.

* Thu Oct 04 2012 Jonathan Ciesla <limburgher@gmail.com> - 5.6-1
- Minor upstream bugfix.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Jonathan Ciesla <limburgher@gmail.com> - 5.5-1
- Minor upstream bugfix.

* Mon Apr 23 2012 Jonathan Ciesla <limburgher@gmail.com> - 5.4-2
- Fix OPTFLAGS, BZ 815393.

* Tue Apr 10 2012 Jonathan Ciesla <limburgher@gmail.com> - 5.4-1
- New upstream.
- pthread patch upstreamed.

* Mon Mar 12 2012 Jonathan Ciesla <limburgher@gmail.com> - 5.3-1
- New upstream.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-3
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Jon Ciesla <limb@jcomserv.net> - 5.2-1
- New upstream.

* Thu Jul 14 2011 Nikola Pajkovsky <npajkovs@redhat.com> - 5.1-1
- new upstream version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 4.7-2
- Rebuilt for gcc bug 634757

* Mon Sep 13 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 4.7-1
- bump up to 4.7

* Wed Feb 17 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 4.3-3
- Resolves: #564768 - FTBFS atanks-4.3-2.fc13: ImplicitDSOLinking

* Fri Jan 22 2010 Jon Ciesla <limb@jcomserv.net> - 4.3-2
- Update icon cache.

* Fri Jan 15 2010 Jon Ciesla <limb@jcomserv.net> - 4.3-1
- New upstream.

* Wed Jan 13 2010 Jon Ciesla <limb@jcomserv.net> - 4.2-1
- New upstream.
- Dropped nothreads patch, upstreamed.

* Fri Nov 06 2009 Jon Ciesla <limb@jcomserv.net> - 4.1-3
- Fix crash on SMP systems.

* Wed Nov 04 2009 Jon Ciesla <limb@jcomserv.net> - 4.1-2
- Add unicode.dat, datafiles.

* Thu Oct 29 2009 Nikola Pajkovsky <npajkovs@redhat.com> 4.1-1
- Upstream 4.1

* Thu Sep 17 2009 Jon Ciesla <limb@jcomserv.net> - 3.9-1
- Upstream 3.9

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 3.7-1
- Upstream 3.7

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 3.2-1
- Upstream 3.2
- Use upstream atanks.png

* Sat Apr 12 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.9-1
- Upstream 2.9

* Sun Dec 23 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.7-1
- Upstream 2.7

* Fri Aug 17 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.5-1
- Upstream 2.5
- Appease license naming gods

* Mon Jul 02 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4-1
- Importing into Fedora CVS and building.

* Fri Jun 29 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4-0.1
- Initial packaging for Fedora.
