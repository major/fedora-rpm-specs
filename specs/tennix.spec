Name:           tennix
Version:        1.3.4
Release:        5%{?dist}
Summary:        A simple tennis game

License:        GPL-2.0-or-later
URL:            http://icculus.org/tennix/
Source0:        https://repo.or.cz/tennix.git/snapshot/tennix-%{version}.tar.gz
Patch1:		tennix-1.0-tnxpath.patch

BuildRequires:  SDL2-devel SDL2_mixer-devel SDL2_image-devel SDL2_ttf-devel SDL2_gfx-devel SDL2_net-devel
BuildRequires:  desktop-file-utils gcc-c++ make


%description
Tennix! is a SDL port of a simple tennis game.
It features a two-player game mode and a single-player mode
against the computer.


%prep
%setup -qn tennix-tennix-1.3.4-9c8f18e

%patch -P 1 -p0

%build
./configure --prefix %{_prefix} --disable-python
CFLAGS="%{optflags}" make LIBS="-lm -lSDL2 -lSDL2_mixer -lSDL2_ttf -lSDL2_image -lSDL2_net"
make %{?_smp_mflags}

%install
PREFIX=%{_prefix} make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
                     data/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/scalable/apps/
cp $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/scalable/apps/%{name}.png


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
<!-- Copyright 2014 Your Name <email@address.com> -->
<!--
EmailAddress: m@thp.io
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">tennix.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Tennis simulator</summary>
  <description>
    <p>
      Tennix is a overhead view tennis simulator for one or two players.
      It features locations from all 4 Grand Slam tournaments in Australia,
      France, the USA and England.
    </p>
  </description>
  <url type="homepage">http://icculus.org/tennix/</url>
  <screenshots>
    <screenshot type="default">http://icculus.org/tennix/screenshots/2011/tennix-ingame-2011.png</screenshot>
  </screenshots>
</application>
EOF

%files
%license COPYING
%doc README HACKING TODO
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man6/%{name}.*
%attr(0664,root,games) /usr/share/tennix/tennix.tnx

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.3.4-1
- 1.3.4

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2.1-9.20190802gitfb013a1
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8.20190802gitfb013a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7.20190802gitfb013a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6.20190802gitfb013a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5.20190802gitfb013a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4.20190802gitfb013a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3.20190802gitfb013a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2.20190802gitfb013a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.1-13.201908102gitfb013a1
- Fix FTBFS.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12.20160127git37def4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11.20160127git37def4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10.20160127git37def4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9.20160127git37def4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1-8.20160127git37def4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-7.20160127git37def4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6.20160127git37def4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5.20160127git37def4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4.20160127git37def4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 03 2016 Jon Ciesla <limburgher@gmail.com> - 1.1-3.20160127git37def4
- Patch to char for arm.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2.20160127git37def4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Jon Ciesla <limburgher@gmail.com> - 1.1-1.20160127git37def4
- Post 1.1 snapshot for build issues, BZ 1295122.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.0-13
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.0-9
- Drop desktop vendor tag.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-5
- Correct makefile for 2.7.

* Fri Jul 30 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-4
- Fix python flag for 2.7.

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-2
- FTBFS fix, BZ 599940.

* Mon Nov 02 2009 Jon Ciesla <limb@jcomserv.net> - 1.0-1
- Update to 1.0, BZ 500068.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 27 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.6.1-4
- updated Summary
- fixed filename in SOURCE
- fixed paths in install section
- fixed icon caching after installing and uninstalling
- fixed timestamps preservation in prep section

* Sun Aug 24 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.6.1-3
- fixed .desktop file name in files section

* Mon May 12 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.6.1-2
- make install doesn't strip binaries
- make uses OPTFLAGS

* Wed May  7 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.6.1-1
- Initial release
