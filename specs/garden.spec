Name:           garden
Version:        1.0.9
Release:        23%{?dist}
Summary:        An innovative old-school 2D vertical shoot-em-up

License:        GPL-3.0-or-later
URL:            http://garden.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
#Patch0:         garden-dso.patch
#Patch1:         garden-printf-format.patch
Patch2:         garden-1.0.8-inline.patch

BuildRequires:  allegro-devel
BuildRequires:  desktop-file-utils
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires: make
Requires:       allegro

%description
Garden of colored lights is an old school 2D vertical shoot-em-up with some
innovative elements. Innovative graphics, soundtrack and game concept. The
game itself is very challenging and as you progress, you will understand that
you are dealing with a true piece of art...

%prep
%setup -q

# patch for DSO-linking
# https://sourceforge.net/tracker/?func=detail&aid=2982590&group_id=242667&atid=1121672
#%%patch0 -p1 -b .dso
#%%patch1 -p0 -b .format
%patch -P2 -p1

%build
autoreconf -if
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure 
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

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
BugReportURL: https://sourceforge.net/p/garden/feature-requests/4/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">garden.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Choose your equipment and fly your ship past the enemies</summary>
  <description>
    <p>
      In garden of coloured lights you must fly as far as you can while enemies
      attack.
      You choose how to equip the ship, depending on your strategy.
    </p>
    <p>
      The futuristic landscape scrolls upwards while strange plant-like enemies
      engage your ship in various ways.
      There are boss enemies to kill in each stage.
    </p>
  </description>
  <url type="homepage">http://garden.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://garden.sourceforge.net/drupal/sites/default/files/images/stage1_1.png</screenshot>
    <screenshot>http://garden.sourceforge.net/drupal/sites/default/files/images/stage1_2.png</screenshot>
    <screenshot>http://garden.sourceforge.net/drupal/sites/default/files/images/stage0_0.png</screenshot>
  </screenshots>
</application>
EOF

desktop-file-validate \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.9-18
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.0.9-11
- Fix FTBFS.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.9-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 11 2016 Jonathan Ciesla <limburgher@gmail.com> - 1.0.9-1
- 1.0.9, BZ 1306730.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Jonathan Ciesla <limburgher@gmail.com> - 1.0.8-14
- Patch out inlines to fix FTBFS.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.0.8-13
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Jonathan Ciesla <limburgher@gmail.com> - 1.0.8-10
- Support aarch64, BZ 925385.

* Mon Feb 10 2014 Jonathan Ciesla <limburgher@gmail.com> - 1.0.8-9
- Fix format-security FTBFS, BZ 1037077.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.8-4
- rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr  6 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.0.8-2
- added DSOlinking patch
- changed license from GPLv3 to GPLv3+
- added COPYING to %%doc

* Sat Mar 13 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.0.8-1
- initial package
