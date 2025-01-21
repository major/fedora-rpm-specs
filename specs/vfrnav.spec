Name:           vfrnav
Version:        20230429
Release:        17%{?dist}
Summary:        VFR/IFR Navigation

License:        GPL-2.0-or-later
URL:            https://gitlab.com/tsailer/vfrnav/
Source:         https://gitlab.com/tsailer/vfrnav/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch:          vfrnav-octave-colors.patch
Patch:          vfrnav-compile.patch

%bcond_without webservice
%bcond_with wetterdl
%bcond_with osmium

BuildRequires:  make
BuildRequires:  autoconf-archive
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gtkmm30-devel
BuildRequires:  libxml++-devel >= 2.14.0
BuildRequires:  sqlite-devel >= 3.0
BuildRequires:  gpsd-devel
BuildRequires:  libsqlite3x-devel
BuildRequires:  gdal-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  eigen3-devel
BuildRequires:  boost-devel
BuildRequires:  cairomm-devel
BuildRequires:  cairo-devel
BuildRequires:  zfstream-devel
BuildRequires:  gettext
%ifarch %java_arches
BuildRequires:  antlr-C++
%endif
%ifnarch s390 s390x
BuildRequires:  pilot-link-devel
%endif
BuildRequires:  gnome-bluetooth-libs-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  geoclue2-devel
BuildRequires:  gsl-devel
BuildRequires:  libftdi-devel
BuildRequires:  libftdi-c++-devel
BuildRequires:  libudev-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  evince-devel
BuildRequires:  libusb1-devel
BuildRequires:  libcurl-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  libsoup-devel
BuildRequires:  librsvg2-devel
BuildRequires:  podofo0.9-devel
BuildRequires:  systemd-devel
BuildRequires:  transfig
BuildRequires:  texlive
BuildRequires:  texlive-latex
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-epstopdf-bin
BuildRequires:  texlive-umlaute
BuildRequires:  texlive-babel-german
BuildRequires:  texlive-multirow
BuildRequires:  texlive-oberdiek
BuildRequires:  texlive-tools
BuildRequires:  poppler-utils
BuildRequires:  readline-devel
BuildRequires:  geos-devel
BuildRequires:  polyclipping-devel
BuildRequires:  libpqxx-devel
BuildRequires:  octave
BuildRequires:  octave-devel
BuildRequires:  inkscape
BuildRequires:  dia
BuildRequires:  selinux-policy-devel
BuildRequires:  qrencode-devel
BuildRequires:  libarchive-devel
BuildRequires:  yaml-cpp-devel
%if %{with osmium}
BuildRequires:  libosmium-devel
%endif
BuildRequires:  protozero-devel
BuildRequires:  utf8cpp-devel
BuildRequires:  expat-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  lz4-devel
Requires:       libreoffice-core
Requires:       libreoffice-calc
Requires:       texlive
Requires:       texlive-latex
Requires:       texlive-latex-bin-bin
Requires:       texlive-droid
Requires:       texlive-contour
Requires:       texlive-truncate
Requires:       texlive-changebar
Requires:       texlive-eurosym
Requires:       texlive-xstring
Requires:       texlive-hyphenat
Requires:       tex(t2aenc.def)
Requires:       texlive-lh
Requires:       texlive-xetex-def
Requires:       texlive-framed
Requires:       texlive-polyglossia
Requires:       texlive-multirow
Requires:       texlive-mdframed
%if 0%{?fedora} >= 25
Requires:       texlive-lualibs
Requires:       texlive-ctablestack
%endif

%if %{with webservice}
BuildRequires:  jsoncpp-devel
BuildRequires:  sqlite
%endif

# Auto BR:
# BuildRequires: atk-devel
# BuildRequires: bash
# BuildRequires: binutils
# BuildRequires: boost-devel
# BuildRequires: cairo-devel
# BuildRequires: cairomm-devel
# BuildRequires: coreutils
# BuildRequires: cpio
# BuildRequires: diffutils
# BuildRequires: elfutils
# BuildRequires: file
# BuildRequires: findutils
# BuildRequires: gawk
# BuildRequires: gcc-c++
# BuildRequires: gcc-gfortran
# BuildRequires: gcc
# BuildRequires: gdal-devel
# BuildRequires: gettext
# BuildRequires: glib2-devel
# BuildRequires: glibc-common
# BuildRequires: glibc-devel
# BuildRequires: glibc-headers
# BuildRequires: glibmm24-devel
# BuildRequires: gnome-bluetooth-devel
# BuildRequires: gnome-libs-devel
# BuildRequires: gnome-vfs2-devel
# BuildRequires: gpsd-devel
# BuildRequires: grep
# BuildRequires: gtk2-devel
# BuildRequires: gtkmm24-devel
# BuildRequires: gzip
# BuildRequires: kernel-headers
# BuildRequires: libart_lgpl-devel
# BuildRequires: libbonobo-devel
# BuildRequires: libbonoboui-devel
# BuildRequires: libbtctl-devel
# BuildRequires: libglademm24-devel
# BuildRequires: libgnomecanvas-devel
# BuildRequires: libgnome-devel
# BuildRequires: libgnomeui-devel
# BuildRequires: libsigc++20-devel
# BuildRequires: libsqlite3x-devel
# BuildRequires: libstdc++-devel
# BuildRequires: libxml2-devel
# BuildRequires: libxml++-devel
# BuildRequires: make
# BuildRequires: net-tools
# BuildRequires: pango-devel
# BuildRequires: pangomm-devel
# BuildRequires: pilot-link-devel
# BuildRequires: pkgconfig
# BuildRequires: popt-devel
# BuildRequires: sed
# BuildRequires: sqlite36-devel
# BuildRequires: tar
# BuildRequires: zfstream-devel
# BuildRequires: zlib-devel

%description
This is a navigation application for VFR and IFR flying.

%package utils
Summary:        VFR Navigation Utilities
Requires:       %{name} = %{version}
Requires:       php
Requires:       php-mbstring
Requires:       /usr/bin/convert

%description utils
This package contains utilities for database creation and manipulation
for the VFR navigation application.

%if %{with wetterdl}
%package wetterdl
Summary:        VFR Navigation Weather Downloader
Requires:       %{name} = %{version}

%description wetterdl
This package contains a downloader application for weather
pictures from flugwetter.de and other sources.
%endif

%package validatorservice
Summary:        VFR Navigation CFMU Validator Service
Requires:       %{name} = %{version}
Requires:       %{name}-selinux = %{version}
Requires:       xorg-x11-server-Xvfb

%description validatorservice
Opening the connection to the CFMU validator takes some time (in the order
of seconds to minutes). In order to amortize this time over multiple tasks,
this package contains a local socket validator server.

%package selinux
Summary:        VFR Navigation selinux module
Requires:       %{name} = %{version}
BuildArch:      noarch
Requires:       selinux-policy
Requires(post):         policycoreutils
Requires(postun):       policycoreutils

%description selinux
This package contains the selinux module required for vfrnav

%if %{with webservice}
%package webservice
Summary:        VFR Navigation CFMU Autorouter Webservice
Requires:       %{name} = %{version}
Requires:       %{name}-validatorservice = %{version}
Requires:       %{name}-selinux = %{version}
Requires:       httpd

%description webservice
This package contains a webservice for the CFMU Autorouter.
%endif

%prep
%autosetup -p1
autoreconf -fiv

%build
CXXFLAGS=`echo %optflags | sed -e 's/-O2//'`
export CXXFLAGS
CFLAGS=`echo %optflags | sed -e 's/-O2//'`
export CFLAGS
%configure
%make_build
# build selinux module
%make_build -C data/selinux -f %{_datadir}/selinux/devel/Makefile

%install
%make_install

for i in $RPM_BUILD_ROOT/%{_datadir}/applications/*.desktop; do
  grep -v '^\(\(X-\)\|\(Version\)\|\(Encoding\)\)' $i > $i.tmp
  sed -e s,Exec=/usr/bin/,Exec=, < $i.tmp > $i
  rm -f $i.tmp
done

for i in $RPM_BUILD_ROOT/%{_datadir}/applications/*.desktop; do
  desktop-file-validate $i
done

# convert icons to sane dimensions
install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps
install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps
convert -size 32x32 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/26x26/apps/vfrnav.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/vfrnav.png
convert -size 48x48 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/40x40/apps/vfrnav.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/vfrnav.png
convert -size 32x32 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/26x26/apps/wetterdl.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/wetterdl.png
convert -size 48x48 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/40x40/apps/wetterdl.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/wetterdl.png
rm -rf $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/26x26/
rm -rf $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/40x40/

install -d $RPM_BUILD_ROOT/%{_sysconfdir}/vfrnav

rm -f $RPM_BUILD_ROOT/%{_sbindir}/cfmuws
rm -f $RPM_BUILD_ROOT/lib/systemd/system/cfmuws.service
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cfmuws
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/vfrnav/cfmuwsusers.json

#rm -f $RPM_BUILD_ROOT/%{_bindir}/cfmusidstar

rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnav.so
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnav.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnav.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnavcarto.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnavcarto.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libvfrnavcarto.so


rm -f $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/web-extensions/libcfmuwebextension.a
rm -f $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/web-extensions/libcfmuwebextension.la

install -d $RPM_BUILD_ROOT/run/vfrnav/validator
install -d $RPM_BUILD_ROOT/var/lib/vfrnav

# selinux
install -p -m 644 -D data/selinux/vfrnav.pp $RPM_BUILD_ROOT%{_datadir}/selinux/packages/%{name}/%{name}.pp

%if %{with webservice}
install -d $RPM_BUILD_ROOT/%{_libdir}/vfrnav
echo "CREATE TABLE IF NOT EXISTS credentials (username TEXT UNIQUE NOT NULL, passwdclear TEXT, passwdmd5 TEXT, salt INTEGER);" | sqlite3 $RPM_BUILD_ROOT/%{_sysconfdir}/vfrnav/autoroute.db
install -d $RPM_BUILD_ROOT/run/vfrnav/autoroute
%else
rm -f $RPM_BUILD_ROOT/lib/systemd/system/cfmuautoroute.service
rm -f $RPM_BUILD_ROOT/lib/systemd/system/cfmuautoroute.socket
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cfmuautoroute
%endif

%if %{with wetterdl}
%else
rm -f $RPM_BUILD_ROOT/%{_bindir}/wetterdl.py
rm -f $RPM_BUILD_ROOT/%{_datadir}/applications/wetterdl.desktop
rm -f $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/wetterdl.png
rm -f $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/wetterdl.png
%endif

%pre validatorservice
getent group vfrnav &>/dev/null || groupadd -r vfrnav
getent passwd vfrnav &>/dev/null || \
useradd -g vfrnav -d /var/lib/vfrnav -M -r -s /sbin/nologin \
    -c "Special user account to be used by vfrnav cfmuautoroute/cfmuvalidate services" vfrnav

%post selinux
/usr/sbin/semodule -i %{_datadir}/selinux/packages/%{name}/%{name}.pp >/dev/null 2>&1 || :

%postun selinux
if [ $1 -eq 0 ] ; then
    /usr/sbin/semodule -r %{name} >/dev/null 2>&1 || :
fi

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog INSTALL NEWS README TODO doc/flightdeck.pdf
%{_datadir}/applications/vfrnav.desktop
%{_datadir}/applications/flightdeck.desktop
%{_datadir}/applications/vfrairporteditor.desktop
%{_datadir}/applications/vfrairspaceeditor.desktop
%{_datadir}/applications/vfrnavaideditor.desktop
%{_datadir}/applications/vfrtrackeditor.desktop
%{_datadir}/applications/vfrwaypointeditor.desktop
%{_datadir}/applications/acftperf.desktop
%{_datadir}/icons/hicolor/32x32/apps/vfrnav.png
%{_datadir}/icons/hicolor/48x48/apps/vfrnav.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/vfrnav.png
%{_datadir}/%{name}/bluetooth.png
%{_datadir}/%{name}/BlankMap-World_gray.svg
%{_datadir}/%{name}/dbeditor.ui
%{_datadir}/%{name}/navigate.ui
%{_datadir}/%{name}/routeedit.ui
%{_datadir}/%{name}/prefs.ui
%{_datadir}/%{name}/acftperformance.ui
%{_datadir}/%{name}/cfmuvalidate.ui
%{_libdir}/libreoffice/share/registry/vfrnav.xcd
%{_libdir}/libvfrnav.so.0
%{_libdir}/libvfrnav.so.0.0.0
%{_libdir}/libvfrnavcarto.so.0
%{_libdir}/libvfrnavcarto.so.0.0.0
%{_bindir}/vfrnav
%{_bindir}/vfrnavaideditor
%{_bindir}/vfrwaypointeditor
%{_bindir}/vfrairwayeditor
%{_bindir}/vfrairporteditor
%{_bindir}/vfrairspaceeditor
%{_bindir}/vfrtrackeditor
%{_bindir}/vfrnavdb2xml
%{_bindir}/vfrnavfplan
%{_bindir}/vfrnavxml2db
%{_bindir}/vfrpdfmanip
%{_bindir}/acftperf
%{_bindir}/flightdeck
%{_bindir}/cfmuvalidate
%{_bindir}/cfmuautoroute
%{_bindir}/checkfplan
%{_bindir}/vfrnavacftconv
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/cfmuvalidateserver
%{_libexecdir}/%{name}/web-extensions/libcfmuwebextension.so
%{_datadir}/%{name}/themes/gtk-3.0/flightdeck.css
%{_datadir}/%{name}/flightdeck.ui
%{_datadir}/%{name}/flightdeck/hbdhg.cfg
%{_datadir}/%{name}/flightdeck/hbpbx.cfg
%{_datadir}/%{name}/flightdeck/hbpho.cfg
%{_datadir}/%{name}/flightdeck/hbtda.cfg
%{_datadir}/%{name}/flightdeck/hbtdb.cfg
%{_datadir}/%{name}/flightdeck/hbtdc.cfg
%{_datadir}/%{name}/flightdeck/hbtdd.cfg
%{_datadir}/%{name}/flightdeck/sim.cfg
%{_datadir}/%{name}/aircraft/hbdhg.xml
%{_datadir}/%{name}/aircraft/hbpbx.xml
%{_datadir}/%{name}/aircraft/hbpho.xml
%{_datadir}/%{name}/aircraft/hbtda.xml
%{_datadir}/%{name}/aircraft/hbtdb.xml
%{_datadir}/%{name}/aircraft/hbtdc.xml
%{_datadir}/%{name}/aircraft/hbtdd.xml
%{_datadir}/%{name}/navlogtemplates/navlog.ods
%{_datadir}/%{name}/navlog.xml

%files utils
%{_bindir}/vfrdbdafif
%{_bindir}/vfrdbmapelementsdb
%{_bindir}/vfrdboptimizelabelplacement
%{_bindir}/vfrdbrebuildspatialindex
%{_bindir}/vfrdbsrtm30db
%{_bindir}/vfrdbsrtmwatermask
%{_bindir}/vfrgshhsimport
%{_bindir}/vfrdbsettopo30
%{_bindir}/vfrdbtopo30zerotiles
%{_bindir}/vfrdbtopo30bin
%{_bindir}/vfrdbupdategndelev
%{_bindir}/vfrdbcamelcase
%{_bindir}/vfrnavwmmconv
%{_bindir}/vfrnavwmmtest
%{_bindir}/vfrdbxplane
%{_bindir}/vfrdbcsv
%{_bindir}/vfrdbxplaneexport
%{_bindir}/flightdeckftdieeprog
%{_bindir}/vfrdbairwaydump
%{_bindir}/vfrdbeadimport
%{_bindir}/vfrdbaixmimport
%{_bindir}/vfrdbopenair
%{_bindir}/vfrdbfasimport
%{_bindir}/vfrradconvert
%{_bindir}/vfrdbukpostcodeimport
%{_bindir}/vfrnavfixdb
%{_bindir}/cfmusidstar
%{_bindir}/adrimport
%{_bindir}/adraupimport
%{_bindir}/adrquery
%{_bindir}/adrdbsync
%{_bindir}/aircraftopsperf
%{_bindir}/weatherfplan
%{_bindir}/vfrnavgrib2dump
%{_bindir}/vfrnavgrib2fcst
%{_bindir}/vfrdbbasulmimport
%{_bindir}/vfrnavmodes
%if %{with osmium}
%{_bindir}/osmbdry2shp
%{_bindir}/osm2odb
%{_bindir}/osm2sdb
%endif
%{_bindir}/odbquery
%{_bindir}/sdbquery
%{_bindir}/cartoquery

%if %{with wetterdl}
%files wetterdl
%{_bindir}/wetterdl.py
%{_datadir}/applications/wetterdl.desktop
%{_datadir}/icons/hicolor/32x32/apps/wetterdl.png
%{_datadir}/icons/hicolor/48x48/apps/wetterdl.png
%endif

%files validatorservice
/lib/systemd/system/cfmuvalidate.service
/lib/systemd/system/cfmuvalidate.socket
%config(noreplace) %{_sysconfdir}/sysconfig/cfmuvalidate
%dir %attr(0755,vfrnav,vfrnav) /run/vfrnav
%dir %attr(0750,vfrnav,vfrnav) /run/vfrnav/validator
%dir %attr(0750,vfrnav,vfrnav) /var/lib/vfrnav

%files selinux
%{_datadir}/selinux/packages/%{name}/vfrnav.pp

%if %{with webservice}
%files webservice
/lib/systemd/system/cfmuautoroute@.service
/lib/systemd/system/cfmuautoroute@.socket
%config(noreplace) %{_sysconfdir}/sysconfig/cfmuautoroute
%dir %{_sysconfdir}/vfrnav
%config(noreplace) %attr(0660,vfrnav,apache) %{_sysconfdir}/vfrnav/autoroute.db
%dir %attr(0750,vfrnav,apache) /run/vfrnav/autoroute
%endif

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20230429-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Thomas Sailer <fedora@tsailer.ch> - 20230429-16
- fixes for octave 9

* Mon Dec 23 2024 Björn Esser <besser82@fedoraproject.org> - 20230429-15
- Rebuild (libpqxx)

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 20230429-14
- Rebuild for octave 9.2

* Fri Nov 08 2024 Sandro Mani <manisandro@gmail.com> - 20230429-13
- Rebuild (gdal)

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 20230429-12
- Rebuild for yaml-cpp 0.8

* Tue Sep 10 2024 Sandro Mani <manisandro@gmail.com> - 20230429-11
- Rebuild (geos)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230429-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 06 2024 Sandro Mani <manisandro@gmail.com> - 20230429-9
- Rebuild (geos)

* Mon May 13 2024 Sandro Mani <manisandro@gmail.com> - 20230429-8
- Rebuild (gdal)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230429-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 20230429-6
- Rebuild (gdal)

* Sun Nov 12 2023 Sandro Mani <manisandro@gmail.com> - 20230429-5
- Rebuild (geos)

* Wed Aug 16 2023 Sandro Mani <manisandro@gmail.com> - 20230429-4
- Switch to BR podofo0.9-devel

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230429-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Sandro Mani <manisandro@gmail.com> - 20230429-2
- Rebuild (geos)

* Wed May 17 2023 Thomas Sailer <fedora@tsailer.ch> - 20230429-1
- update to 20230429

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 20201231-40
- Rebuild (gdal)

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 20201231-39
- Rebuild with octave 8.1.0

* Tue Jan 24 2023 Adam Williamson <awilliam@redhat.com> - 20201231-38
- rebuild for new libgps

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20201231-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Richard Shaw <hobbes1069@gmail.com> - 20201231-36
- Rebuild for yaml-cpp 0.7.0.

* Tue Nov 15 2022 Sandro Mani <manisandro@gmail.com> - 20201231-35
- Rebuild (geos)

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 20201231-34
- Rebuild (gdal)

* Tue Nov 08 2022 Richard Shaw <hobbes1069@gmail.com> - 20201231-33
- Rebuild for yaml-cpp 0.7.0.

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 20201231-32
- Restrict BR: antlr to %%java_arches

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 20201231-31
- Rebuild for gsl-2.7.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20201231-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Sandro Mani <manisandro@gmail.com> - 20201231-29
- Rebuild (geos)

* Tue Jun 07 2022 Sandro Mani <manisandro@gmail.com> - 20201231-28
- Rebuild (geos)

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 20201231-27
- Rebuild for octave 7.1

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 20201231-26
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Fri May 06 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 20201231-25
- Rebuild for new gpsd

* Tue May 03 2022 Sandro Mani <manisandro@gmail.com> - 20201231-24
- Rebuild (podofo)

* Fri Feb 18 2022 Thomas Sailer <fedora@tsailer.ch> - 20201231-23
- rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20201231-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Sandro Mani <manisandro@gmail.com> - 20201231-21
- Rebuild (geos)

* Mon Jan 10 2022 Björn Esser <besser82@fedoraproject.org> - 20201231-20
- Enable builds for ppc64le again

* Mon Jan 10 2022 Björn Esser <besser82@fedoraproject.org> - 20201231-19
- Rebuild (libpqxx)

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 20201231-18
- Rebuild (gdal)

* Sun Nov 07 2021 Sandro Mani <manisandro@gmail.com> - 20201231-17
- Rebuild (geos)

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 20201231-16
- Rebuild (jsoncpp)

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 20201231-15
- Rebuild (geos)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 20201231-14
- Rebuilt with OpenSSL 3.0.0

* Tue Sep 07 2021 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20201231-13
- rebuild

* Tue Aug 17 2021 Björn Esser <besser82@fedoraproject.org> - 20201231-12
- Rebuild (libpqxx)

* Thu Aug 12 2021 Björn Esser <besser82@fedoraproject.org> - 20201231-11
- Rebuild for octave 6.3.0, again

* Thu Aug 12 2021 Björn Esser <besser82@fedoraproject.org> - 20201231-10
- Add patch to fix invocation of inksacape v1.x
- Use macros for make

* Wed Aug 11 2021 Björn Esser <besser82@fedoraproject.org> - 20201231-9
- Rebuild (gpsd)

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 20201231-8
- Rebuild for octave 6.3.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201231-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 20201231-6
- Rebuild (gdal)

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 20201231-5
- Rebuild (geos)

* Wed Feb 03 2021 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20201231-3
- rebuild for libpqxx 7.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201231-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20201231-2
- rebuild for gpsd

* Mon Jan 11 2021 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20201231-1
- update to 20201231
- make osmium conditional and disable for now as libosmium-devel is broken with g++ 11

* Wed Nov 11 13:13:38 CET 2020 Sandro Mani <manisandro@gmail.com> - 20200429-4
- Rebuild (proj, gdal)

* Sun Aug 09 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20200429-3
- rebuild for libpqxx

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200429-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Björn Esser <besser82@fedoraproject.org> - 20200429-1
- update to 20200429

* Thu Jun 18 2020 Björn Esser <besser82@fedoraproject.org> - 20200427-4
- Rebuild (gpsd)

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 20200427-3
- Rebuild (jsoncpp)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 20200427-2
- Rebuild (gdal)

* Fri May 01 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20200427-1
- update to 20200427

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 20200202-2
- Rebuild (gdal)

* Wed Feb 5 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20200202-1
- update to 20200202

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190212-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 20190212-8
- Rebuild (jsoncpp)

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 20190212-7
- Rebuilt for GSL 2.6.

* Wed Aug 07 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20190212-6
- remove wetterdl subpackage due to python2 dependency

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190212-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 20190212-4
- Rebuild (jsoncpp)

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 20190212-3
- Rebuild (gpsd)

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 20190212-2
- Rebuild for octave 5.1

* Thu Feb 14 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20190212-1
- Compile fixes for rawhide

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180129-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180129-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Sandro Mani <manisandro@gmail.com> - 20180129-3
- Rebuild (podofo)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20180129-1
- update to 20180129
- drop openjpeg2 patch, as it was buggy and openjpeg2 support is now integrated

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20160429-13
- Remove obsolete scriptlets

* Wed Jan 17 2018 Sandro Mani <manisandro@gmail.com> - 20160429-12
- Switch to openjpeg2

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 20160429-11
- Rebuilt for jsoncpp.so.20

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 20160429-10
- Rebuilt for jsoncpp-1.8.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160429-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160429-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20160429-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Feb 02 2017 Sandro Mani <manisandro@gmail.com> - 20160429-6
- Rebuild (podofo)

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 20160429-5
- Rebuilt for Boost 1.63

* Thu Dec 29 2016 Rich Mattes <richmattes@gmail.com> - 20160429-4
- Rebuild for eigen3-3.3.1

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 20160429-3
- Rebuilt for libjsoncpp.so.11

* Sat Sep 24 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20160429-2
- rebuild for podofo

* Mon Sep 19 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20160429-1
- update to 20160429

* Wed May 18 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20160212-3
- rebuid for dependencies

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 20160212-2
- Rebuilt for libjsoncpp.so.1

* Mon Mar 21 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20160212-1
- update to 20160212

* Tue Feb 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20150429-3
- Drop geoclue-1 and gypsy support
- Use %%licence
- Minor spec cleanups

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 20150429-2
- Rebuild for gsl 2.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150429-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 27 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20130727-1
- convert webservice from websockets to php and long poll

* Sun Jul 14 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20130627-1
- add webservice

* Wed Jun 13 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.8-1
- update to 0.8: add flightdeck

* Wed Mar 25 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.3-1
- move to gypsy, add airways

* Sat Feb  2 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.1-2
- move utilities into their own subpackage

* Sat Aug 25 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.1-1
- initial spec file

