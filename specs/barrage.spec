Name:           barrage
Version:        1.0.7
Release:        6%{?dist}
Summary:        Kill and destroy as many targets as possible within 3 minutes

License:        GPL-2.0-or-later
URL:            http://lgames.sourceforge.net/index.php?project=Barrage
Source0:        http://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:	%{name}.desktop
Patch0:         barrage-1.0.2-spelling.patch
Patch1:         barrage-1.0.5-hiscore.patch

Requires:       hicolor-icon-theme
BuildRequires:  gcc
BuildRequires:  SDL-devel SDL_mixer-devel desktop-file-utils
BuildRequires: make

%description
Barrage is a rather violent action game with the objective to kill
and destroy as many targets as possible within 3 minutes. The player
controls a gun that may either fire small or large grenades at
soldiers, jeeps and tanks. It is a very simple gameplay though it is
not that easy to get high scores.


%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0
# add Icon to desktop file
echo Icon=barrage >> barrage.desktop

%build
%configure
find . -type f -name 'Makefile' | xargs sed -i s/-Werror=format-security//g
%make_build %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# below the desktop file and icon stuff
desktop-file-install %{SOURCE2} \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
        $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

install -p -m 0644 %{SOURCE1} \
           $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

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
BugReportURL: https://sourceforge.net/p/lgames/support-requests/2/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">barrage.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A fast paced action game where you shoot down as many targets as possible</summary>
  <description>
    <p>
      Barrage is a fast paced shooter game where the objective is to destroy
      targets like soldiers, tanks and jeeps within 3 minutes.
    </p>
    <p>
      The player controls a gun that shoots small and large grenades at fast
      moving targets and you need to manage your aim, ammo and re-load times carefully.
    </p>
  </description>
  <url type="homepage">http://lgames.sourceforge.net/index.php?project=Barrage</url>
  <screenshots>
    <screenshot type="default">http://lgames.sourceforge.net/Barrage/ss1.jpg</screenshot>
    <screenshot>http://lgames.sourceforge.net/Barrage/ss0.jpg</screenshot>
    <screenshot>http://lgames.sourceforge.net/Barrage/ss2.jpg</screenshot>
  </screenshots>
</application>
EOF

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/barrage48.gif
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/barrage48.png

%files
%license COPYING
%doc AUTHORS BUGS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_var}/games/barrage.hscr


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.7-1
- 1.0.7

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.6-3
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.0.6-1
- 1.0.6

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.0.5-1
- 1.0.5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-13
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.0.4-7
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 17 2012 Jon Ciesla <limburgher@gmail.com> - 1.0.4-1
- New upstream.
- Menu overflow patch upstreamed.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Jon Ciesla <limb@jcomserv.net> - 1.0.3-1
- New upstream.
- Switched to Source desktop, generation isn't working.

* Fri Mar 19 2010 Jon Ciesla <limb@jcomserv.net> - 1.0.2-7
- Spelling fix.

* Fri Mar 19 2010 Jon Ciesla <limb@jcomserv.net> - 1.0.2-6
- Fix for crash due to overflow in menu.
- Fix for DSOLink error.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 31 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 1.0.2-3
- Fixed Source0 URL

* Sun Oct 26 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 1.0.2-2
- Add post and postun
- Add BUGS to doc
- Add desktop-file-install
- Change icon to 48x48
- Remove INSTALL from doc

* Sat Oct 25 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 1.0.2-1
- Initial SPEC file
