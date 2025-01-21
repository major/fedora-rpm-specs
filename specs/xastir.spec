Summary: Amateur Station Tracking and Reporting system for amateur radio
Name:    xastir
Epoch:   1
Version: 2.2.0
Release: 7%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: https://github.com/Xastir/Xastir/archive/Release-%{version}.tar.gz
Source1: %{name}.desktop
Source2: %{name}.png
Source3: %{name}.svg
Source4: org.xastir.Xastir.metainfo.xml
URL:     http://www.xastir.org
Requires: wget
Requires: hicolor-icon-theme
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: wget, libXt-devel, GraphicsMagick-devel
%if 0%{?fedora} >= 24
BuildRequires: motif-devel
%else
BuildRequires: lesstif-devel
%endif
BuildRequires: dos2unix, libax25-devel, curl-devel, proj-devel, libXpm-devel
BuildRequires: python3-devel, gpsman, gdal-devel, libdb-devel
BuildRequires: desktop-file-utils, xfontsel, hdf5-devel
BuildRequires: autoconf, automake, shapelib-devel

%description
Xastir is a graphical application that interfaces HAM radio
and internet access to realtime mapping software.

Install XASTIR if you are interested in APRS(tm) and HAM radio
software.

%prep
%setup -q -n Xastir-Release-%{version}
touch -r configure.ac aclocal.m4 Makefile.in config.h.in

%build
./bootstrap.sh
%configure --with-geotiff=/usr/include/libgeotiff
make %{?_smp_mflags}
for f in README ChangeLog ; do
    mv $f $f.iso88591
    iconv -o $f -f iso88591 -t utf8 $f.iso88591
    touch -r $f.iso88591 $f
    rm -f $f.iso88591
done
dos2unix -k scripts/toporama250k.pl

%install
rm -rf %{buildroot}
make install DESTDIR="%{buildroot}" INSTALL="install -p"
#fix wrong doc-path instalation in make install target
#or else we'll get unpacked files
rm -rf %{buildroot}/usr/share/doc
#remove gpx2shape because of unsupported dependency Geo::Shapelib
rm %{buildroot}/usr/share/xastir/scripts/gpx2shape
#strip exec bit from .pm files
find %{buildroot} -type f -name '*.pm' -exec chmod -x {} 2>/dev/null ';'
install -D -p -m644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -p -m644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -D -p -m644 %{SOURCE4} %{buildroot}%{_metainfodir}/org.xastir.Xastir.metainfo.xml

%files
%{_bindir}/xastir
%{_bindir}/xastir_udp_client
%{_bindir}/callpass
%{_bindir}/testdbfawk
%{_mandir}/man1/xastir*.*
%{_mandir}/man1/callpass.*
%{_mandir}/man1/testdbfawk.*
%{_datadir}/xastir
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/org.xastir.Xastir.metainfo.xml
%doc AUTHORS ChangeLog COPYING DEBUG_LEVELS FAQ LICENSE
%doc README
%doc README.MAPS UPGRADE

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 1:2.2.0-6
- Rebuild for hdf5 1.14.5

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1:2.2.0-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Sandro Mani <manisandro@gmail.com> - 1:2.2.0-2
- Rebuild (shapelib)

* Wed Nov 01 2023 Lucian Langa <lucilanga@7pot.org> - 1:2.2.0-1
- drop pcre
- re-add shapelib depdency - interal shapelib dropped upstream
- drop all patches - fixed upstream
- upgrade to latest upstream

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Daniel Rusek <mail@asciiwolf.com> - 1:2.1.4-16
- Added AppStream metadata, better icon
  Resolves: rhbz#2218927

* Tue Apr 25 2023 DJ Delorie <dj@redhat.com> - 1:2.1.4-15
- Fix C99 compatibility issue

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Petr Viktorin <pviktori@redhat.com> - 2.1.4-9
- Switch BuildRequires to python3

* Mon Sep 21 2020 Jeff Law <law@redhat.com> - 2.1.4-8
- Depend on libdb-devel rather than db4-devel

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 2.1.4-7
- BuildRequire xfontsel not xorg-x11-apps

* Thu Mar 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2.1.4-6
- Fix epoch, can't be decremented

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 0:2.1.4-5
- Rebuild (gdal)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 1:2.1.0-2
- Rebuild for hdf5 1.10.5

* Wed Mar 13 2019 Lucian Langa <lucilanga@gnome.eu.org> - 1:2.1.0-1
- update to latest upstream release
- explicitly pass python3 shebang to tigerpoly script (#1676226)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:2.0.8-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1:2.0.8-4
- rebuild to fix latest broken deps II

* Wed Mar 01 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1:2.0.8-3
- rebuild to fix latest broken deps

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 03 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1:2.0.8-1
- cleanup specfile
- update to latest upstream

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Richard Shaw <hobbes1069@gmail.com> - 1:2.0.6-5
- Rebuild for updated libax25.

* Thu Oct 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2.0.6-4
- Build against motif on fedora >= 24.

* Tue Jul 28 2015 Lucian Langa <lucilanga@gnome.eu.org> - 1:2.0.6-3
- rebuild for newer gdal

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Lucian Langa <lucilanga@gnome.eu.org> - 1:2.0.6-1
- update to latest upstream

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Lucian Langa <cooly@gnome.eu.org> - 1:2.0.4-6
- prefer graphicsmagick (#919713, #1036204)

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 1:2.0.4-5
- Rebuild for gdal 1.10.0

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1:2.0.4-4
- Perl 5.18 rebuild

* Thu Aug 01 2013 Lucian Langa <cooly@gnome.eu.org> - 1:2.0.4-3
- drop shapelib dependency

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1:2.0.4-2
- Perl 5.18 rebuild

* Wed Mar 27 2013 Lucian Langa <cooly@gnome.eu.org> - 1:2.0.4-1
- fix bogus changelog dates
- drop all previous patches  - fixed upstream
- new upstream release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 04 2012 Lucian Langa <cooly@gnome.eu.org> - 1:2.0.0-5
- rebuilt against newer IM

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1:2.0.0-4
- Rebuild against PCRE 8.30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 1:2.0.0-3
- Rebuild for hdf5 1.8.7

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 31 2010 Lucian Langa <cooly@gnome.eu.org> - 1:2.0.0-1
- add patch to fix mapdir handling
- new upstream release

* Wed Sep 29 2010 jkeating - 1:1.9.8-5
- Rebuilt for gcc bug 634757

* Thu Sep 16 2010 Lucian Langa <cooly@gnome.eu.org> - 1:1.9.8-4
- rebuilt with newer IM

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 1:1.9.8-3
- recompiling .py files against Python 2.7 (rhbz#623418)

* Wed Apr 14 2010 Lucian Langa <cooly@gnome.eu.org> - 1:1.9.8-2
- update BR to include hdf5 (GDAL)

* Wed Apr 14 2010 Lucian Langa <cooly@gnome.eu.org> - 1:1.9.8-1
- add patch1 to correctly pick gdal flags
- update patch0
- update to latest upstream (1.9.8)

* Wed Mar 10 2010 Lucian Langa <cooly@gnome.eu.org> - 1:1.9.6-3
- rebuild with newer shapelib and IM

* Sun Oct 25 2009 Lucian Langa <cooly@gnome.eu.org> - 1:1.9.6-2
- fix desktop file (#530841)

* Tue Oct 13 2009 Lucian Langa <cooly@gnome.eu.org> - 1:1.9.6-1
- drop patch1 fixed upstream
- new upstream release

* Mon Aug 10 2009 Lucian Langa <cooly@gnome.eu.org> - 1:1.9.4-10
- update BR as xfontsel is in xorg-x11-apps package

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Lucian Langa <cooly@gnome.eu.org> - 1:1.9.4-8
- rebuilt against newer IM

* Tue Mar 10 2009 Lucian Langa <cooly@gnome.eu.org> - 1:1.9.4-7
- downgrade to the latest stable
- add patch for english units

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.5-2
- patch for new IM

* Sun Dec 21 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.5-1
- cleanup desktop file
- drop engunits patch (fixed upstream)
- upgrade to devel version (FTBS with previous version)

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.9.4-6
- Rebuild for Python 2.6

* Tue Oct 07 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.4-5
- upstream patch, fix for #435762

* Sun Oct 05 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.4-4
- misc cleanups

* Sat Oct 04 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.4-3
- fix for RH #435762

* Mon Sep 08 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.4-2
- update Build requires

* Sun Sep 07 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.4-1
- new upstream 1.9.4
- drop wget and IM patch (fixed upstream)

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9.2-10
- fix license tag
- fix spec up so it doesn't confuse license checking script

* Thu Aug 28 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.2-9
- drop uneeded and potential risky files

* Tue Jul 08 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.2-8
- Rebuild against newer db4 headers

* Fri Jun 06 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.2-7
- Rebuild against gpsman, festival, Berkley DB, gdal

* Sun May 18 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.2-6
- Patch for newer wget

* Mon May  5 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.2-5
- Update to newer ImageMagick

* Sat Mar  8 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.2-4
- Install correct xastir icon
- Misc cleanups
- Rebuild with wget support

* Sun Mar  2 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.2-3
- Added desktop and icon file

* Sat Feb 23 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.2-2
- Moved scripts from libdir to datadir

* Fri Feb 22 2008 Lucian Langa <cooly@gnome.eu.org> - 1.9.2-1
- Updated to Fedora Packaging specifications

* Thu Jul 03 2003 Alan Crosswell <n2ygk@weca.org>
- 1.2.1 my patches now integrated into the main trunk.

* Sat Jun 21 2003 Alan Crosswell <n2ygk@weca.org>
- added xastir-maps.patch

* Mon Jun 16 2003 Alan Crosswell <n2ygk@weca.org>
- 1.2.0

* Fri Jun 06 2003 Alan Crosswell <n2ygk@weca.org>
- June 5 snapshot

* Thu May 15 2003 Alan Crosswell <n2ygk@weca.org>
- start with chuck's spec file for 1.1.4

