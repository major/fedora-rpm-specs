Summary: Matroska container manipulation utilities
Name: mkvtoolnix
Version: 73.0.0
Release: 2%{?dist}
License: GPLv2+
Source0: https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz
Source1: https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz.sig
Source2: https://mkvtoolnix.download/gpg-pub-moritzbunkus.txt
# fix compatibility with Ruby 3.2.0
Patch0: https://gitlab.com/mbunkus/mkvtoolnix/-/commit/ab6455f68c597ede3d6959597a38f2ecbc198011.patch
URL: https://mkvtoolnix.download/
BuildRequires: boost-devel
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: desktop-file-utils
BuildRequires: docbook-style-xsl
BuildRequires: fmt-devel >= 6.1.0
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gmp-devel
BuildRequires: gnupg2
BuildRequires: gtest-devel
BuildRequires: json-devel
BuildRequires: libappstream-glib
BuildRequires: libvorbis-devel
BuildRequires: po4a
BuildRequires: pkgconfig(dvdread)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(libcmark)
BuildRequires: pkgconfig(libebml) >= 1.4.4
BuildRequires: pkgconfig(libmatroska) >= 1.7.1
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(pugixml)
BuildRequires: pkgconfig(zlib)
BuildRequires: rubygem-drake
BuildRequires: rubygem-json
BuildRequires: utf8cpp-devel >= 3.2-2
BuildRequires: %{_bindir}/qmake6
BuildRequires: %{_bindir}/xsltproc
Requires: libebml%{_isa} >= 1.4.4
Requires: libmatroska%{_isa} >= 1.7.1
# bundles a modified avilib
Provides: bundled(avilib) = 0.6.10
# https://www.bunkus.org/videotools/librmff/index.html
Provides: bundled(librmff) = 0.6.0

%description
Mkvtoolnix is a set of utilities to mux and demux audio, video and subtitle
streams into and from Matroska containers.

%package gui
Summary: QT Graphical interface for Matroska container manipulation
Requires: %{name} = %{version}-%{release}
Requires: hicolor-icon-theme

%description gui
Mkvtoolnix is a set of utilities to mux and demux audio, video and subtitle
streams into and from Matroska containers.

This package contains the QT graphical interface for these utilities.

%prep
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q
%patch0 -p1
rm -rf lib/{fmt,libebml,libmatroska,nlohmann-json,pugixml,utf8-cpp}
rm -rf rake.d/vendor drake

%build
%configure \
  --disable-optimization \
  --disable-update-check \
  --with-boost-libdir=%{_libdir} \
  || cat config.log
drake %{?_smp_mflags} V=1

%install
drake DESTDIR=$RPM_BUILD_ROOT TOOLS=1 install
desktop-file-validate %{buildroot}%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.bunkus.mkvtoolnix-gui.appdata.xml

install -pm 755 src/tools/{base64tool,diracparser,ebml_validator,vc1parser} $RPM_BUILD_ROOT%{_bindir}

%find_lang %{name}
%find_lang mkvextract --with-man
%find_lang mkvmerge --with-man
%find_lang mkvpropedit --with-man
%find_lang mkvinfo --with-man
cat mkv{extract,info,merge,propedit}.lang >> mkvtoolnix.lang

%find_lang mkvtoolnix-gui --with-man

%check
drake tests:run_unit

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%{_bindir}/base64tool
%{_bindir}/diracparser
%{_bindir}/ebml_validator
%{_bindir}/mkvextract
%{_bindir}/mkvinfo
%{_bindir}/mkvmerge
%{_bindir}/mkvpropedit
%{_bindir}/vc1parser
%{_mandir}/man1/mkvextract.1*
%{_mandir}/man1/mkvinfo.1*
%{_mandir}/man1/mkvmerge.1*
%{_mandir}/man1/mkvpropedit.1*

%files gui -f mkvtoolnix-gui.lang
%{_bindir}/mkvtoolnix-gui
%{_mandir}/man1/mkvtoolnix-gui.1*
%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
%{_metainfodir}/org.bunkus.mkvtoolnix-gui.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/mime/packages/org.bunkus.mkvtoolnix-gui.xml
%{_datadir}/mkvtoolnix

%changelog
* Tue Jan 31 2023 Dominik Mierzejewski <dominik@greysector.net> - 73.0.0-2
- fix FTBFS with Ruby 3.2.0 (fixes rhbz#2161534)

* Tue Jan 03 2023 Dominik Mierzejewski <dominik@greysector.net> - 73.0.0-1
- update to 73.0.0 (#2157794)

* Wed Dec 07 2022 Dominik Mierzejewski <dominik@greysector.net> - 72.0.0-1
- update to 72.0.0 (#2142390)

* Thu Oct 13 2022 Dominik Mierzejewski <dominik@greysector.net> - 71.1.0-1
- update to 71.1.0 (#2118106)
- require libebml 1.4.4 and libmatroska 1.7.1

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 69.0.0-3
- Rebuilt for flac 1.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 69.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Dominik Mierzejewski <dominik@greysector.net> - 69.0.0-1
- update to 69.0.0 (#2105690)

* Mon May 23 2022 Dominik Mierzejewski <dominik@greysector.net> - 68.0.0-1
- update to 68.0.0 (#2089059)
- Qt6Svg is now required

* Wed May 04 2022 Dominik Mierzejewski <dominik@greysector.net> - 67.0.0-1
- update to 67.0.0 (#2073819)
- sounds were converted to webm/opus format, drop oxygen-sound theme requirement
- add missing build dependency on Qt6Multimedia

* Tue Mar 15 2022 Dominik Mierzejewski <dominik@greysector.net> - 66.0.0-1
- update to 66.0.0 (#2063542)
- drop obsolete patch

* Sun Mar 06 2022 Dominik Mierzejewski <rpm@greysector.net> - 65.0.0-2
- enable s390x builds (#2012824)

* Wed Feb 16 2022 Dominik Mierzejewski <rpm@greysector.net> - 65.0.0-1
- update to 65.0.0 (#2051181)

* Wed Feb 02 2022 Dominik Mierzejewski <rpm@greysector.net> - 64.0.0-1
- update to 64.0.0 (#2035773)
- drop obsolete patch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 63.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 14 2021 Dominik Mierzejewski <rpm@greysector.net> - 63.0.0-1
- update to 63.0.0 (#2023050)

* Mon Oct 11 2021 Dominik Mierzejewski <rpm@greysector.net> - 62.0.0-1
- update to 62.0.0 (#2012572)
- drop removed configure option
- skip s390x for qt6-qtbase issue (#2012824)

* Mon Sep 06 2021 Dominik Mierzejewski <rpm@greysector.net> - 61.0.0-1
- update to 61.0.0 (#1999174)
- drop obsolete patch

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 59.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Dominik Mierzejewski <rpm@greysector.net> - 59.0.0-2
- switch to Qt6
- work around qmake6 adding rpath

* Thu Jul 15 2021 Dominik Mierzejewski <rpm@greysector.net> - 59.0.0-1
- update to 59.0.0 (#1980989)
- adjust build dependencies to upstream changes

* Mon Jul 05 2021 Richard Shaw <hobbes1069@gmail.com> - 58.0.0-2
- Rebuild for new fmt version.

* Fri Jun 25 2021 Dominik Mierzejewski <rpm@greysector.net> - 58.0.0-1
- update to 58.0.0 (#1971313)

* Tue May 25 2021 Dominik Mierzejewski <rpm@greysector.net> - 57.0.0-1
- update to 57.0.0 (#1963333)
- build dependency clean-up

* Wed May 19 2021 Dominik Mierzejewski <rpm@greysector.net> - 56.1.0-1
- update to 56.1.0 (#1933359)
- requires libebml 1.4.2 and libmatroska 1.6.3
- BR fixed utf8cpp

* Mon Feb 01 2021 Dominik Mierzejewski <rpm@greysector.net> - 53.0.0-1
- update to 53.0.0 (#1912613)
- requires libebml 1.4.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 51.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 51.0.0-3
- Rebuilt for Boost 1.75

* Sat Oct 17 2020 Dominik Mierzejewski <rpm@greysector.net> - 51.0.0-2
- rebuild for libdvdread-6.1 ABI bump

* Mon Oct 05 2020 Dominik Mierzejewski <rpm@greysector.net> - 51.0.0-1
- update to 51.0.0 (#1876232)
- upstream switched to pcre2 for regex
- unbundle jpcre2

* Fri Aug 21 2020 Dominik Mierzejewski <rpm@greysector.net> - 49.0.0-1
- update to 49.0.0 (#1862797)
- requires libmatroska 1.6.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 48.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Dominik Mierzejewski <rpm@greysector.net> - 48.0.0-1
- update to 48.0.0 (#1842056)
- bump minimum libebml and libmatroska versions

* Sun Jun 21 2020 Dominik Mierzejewski <rpm@greysector.net> - 47.0.0-1
- update to 47.0.0 (#1842056)
- bump minimum fmt version
- enable DVD chapters support via libdvdread

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 46.0.0-2
- Rebuilt for Boost 1.73

* Sun May 03 2020 Dominik Mierzejewski <rpm@greysector.net> - 46.0.0-1
- update to 46.0.0 (#1830243)

* Wed Apr 22 2020 Dominik Mierzejewski <rpm@greysector.net> - 45.0.0-1
- update to 45.0.0 (#1820902)

* Fri Mar 13 2020 Dominik Mierzejewski <rpm@greysector.net> - 44.0.0-1
- update to 44.0.0 (#1787797)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 41.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 2019 Dominik Mierzejewski <rpm@greysector.net> - 41.0.0-1
- update to 41.0.0 (#1782273)

* Sat Nov 30 2019 Dominik Mierzejewski <rpm@greysector.net> - 40.0.0-1
- update to 40.0.0 (#1768672)
- move oxygen-sound-theme dependency to -gui subpackage (#1768209)

* Tue Oct 08 2019 Dominik Mierzejewski <rpm@greysector.net> - 38.0.0-1
- update to 38.0.0 (#1758875)
- use gpgverify macro

* Tue Sep 10 2019 Dominik Mierzejewski <rpm@greysector.net> - 37.0.0-1
- update to 37.0.0 (#1723039)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 34.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Dominik Mierzejewski <rpm@greysector.net> - 34.0.0-1
- update to 34.0.0 (#1688024)
- requires libebml 1.3.7 and libmatroska 1.5.0

* Mon Feb 11 2019 Dominik Mierzejewski <rpm@greysector.net> - 31.0.0-1
- update to 31.0.0 (#1674160)

* Wed Feb 06 2019 Dominik Mierzejewski <rpm@greysector.net> - 30.1.0-1
- update to 30.1.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 29.0.0-3
- Rebuilt for Boost 1.69

* Tue Dec 11 2018 Dominik Mierzejewski <rpm@greysector.net> - 29.0.0-2
- unbundle fmt (upstream switched from boost::format)

* Mon Dec 10 2018 Dominik Mierzejewski <rpm@greysector.net> - 29.0.0-1
- update to 29.0.0

* Tue Oct 30 2018 Dominik Mierzejewski <rpm@greysector.net> - 28.2.0-1
- update to 28.2.0
- fixes CVE-2018-4022 (#1644258)

* Mon Oct 08 2018 Dominik Mierzejewski <rpm@greysector.net> - 27.0.0-2
- add explicit BR on xsltproc
- fix keyring creation for sig verification with older gpg2 version

* Sat Oct 06 2018 Dominik Mierzejewski <rpm@greysector.net> - 27.0.0-1
- update to 27.0.0 (#1636462)

* Sun Jul 15 2018 Dominik Mierzejewski <rpm@greysector.net> - 25.0.0-1
- update to 25.0.0 (#1600752)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 24.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Dominik Mierzejewski <rpm@greysector.net> - 24.0.0-1
- update to 24.0.0 (#1589516)

* Wed May 23 2018 Dominik Mierzejewski <rpm@greysector.net> - 23.0.0-1
- update to 23.0.0 (#1574271)

* Fri Apr 06 2018 Dominik Mierzejewski <rpm@greysector.net> - 22.0.0-1
- update to 22.0.0 (#1562653)

* Wed Mar 07 2018 Dominik Mierzejewski <rpm@greysector.net> - 21.0.0-1
- update to 21.0.0 (#1548692)
- mkvinfo has no GUI again, moved back to main package
- drop obsolete scriptlets
- drop strict libebml/libmatroska deps, all Fedora releases have them
- add missing BR: gcc-c++

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 20.0.0-2
- Rebuilt for Boost 1.66

* Thu Jan 18 2018 Dominik Mierzejewski <rpm@greysector.net> - 20.0.0-1
- update to 20.0.0 (#1534796)
- fixes FTBFS with ruby 2.5 (#1532391)
- new dependency required to build GUIs: cmark

* Tue Dec 19 2017 Dominik Mierzejewski <rpm@greysector.net> - 19.0.0-1
- update to 19.0.0 (#1527485)
- disable built-in update check (#1515687)

* Mon Nov 20 2017 Dominik Mierzejewski <rpm@greysector.net> - 18.0.0-1
- update to 18.0.0 (#1514860)

* Tue Oct 24 2017 Dominik Mierzejewski <rpm@greysector.net> - 17.0.0-1
- update to 17.0.0 (#1504369)
- verify GPG signature of the source

* Sat Oct 07 2017 Dominik Mierzejewski <rpm@greysector.net> - 16.0.0-1
- update to 16.0.0 (#1497489)
- requires libmatroska >= 1.4.8

* Wed Aug 23 2017 Dominik Mierzejewski <rpm@greysector.net> - 15.0.0-1
- update to 15.0.0 (#1483229)
- requires libebml >= 1.3.5
- drop strict libmatroska requirement, all Fedora releases have 1.4.5+
- old ChangeLog was dropped

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Dominik Mierzejewski <rpm@greysector.net> - 14.0.0-1
- update to 14.0.0 (#1474050)

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 13.0.0-3
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 13.0.0-2
- Rebuilt for Boost 1.64

* Sun Jun 25 2017 Dominik Mierzejewski <rpm@greysector.net> - 13.0.0-1
- update to 13.0.0 (#1464751)

* Tue May 23 2017 Dominik Mierzejewski <rpm@greysector.net> - 12.0.0-1
- update to 12.0.0 (#1452950)
- unbundle sound files from oxygen sound theme
- add Provides: for bundled librmff

* Mon Apr 24 2017 Dominik Mierzejewski <rpm@greysector.net> - 11.0.0-1
- update to 11.0.0 (#1444579)
- drop obsolete patch (CXXFLAGS fix)
- new dependency introduced by upstream (Qt5Multimedia)
- rename desktop files to fix task switcher icons under Wayland

* Fri Mar 31 2017 Dominik Mierzejewski <rpm@greysector.net> - 10.0.0-1
- update to 10.0.0
- drop obsolete configure option
- fix system CXXFLAGS usage

* Tue Feb 21 2017 Dominik Mierzejewski <rpm@greysector.net> - 9.9.0-1
- update to 9.9.0 (#1424868)
- drop obsolete macros and Obsoletes:

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 9.8.0-2
- Rebuilt for Boost 1.63

* Mon Jan 23 2017 Dominik Mierzejewski <rpm@greysector.net> - 9.8.0-1
- update to 9.8.0 (#1415524)
- drop upstreamed patch (https://github.com/mbunkus/mkvtoolnix/issues/1858)

* Thu Jan 19 2017 Dominik Mierzejewski <rpm@greysector.net> - 9.7.1-1
- update to 9.7.1 (#1408814)
- add links explaining patches

* Mon Dec 05 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.6.0-1
- update to 9.6.0 (#1400209)

* Wed Oct 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.5.0-1
- update to 9.5.0 (#1385650)

* Wed Sep 28 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.4.2-1
- update to 9.4.2 (#1376266)

* Sun Aug 28 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.4.0-1
- update to 9.4.0 (#1370765)

* Fri Aug 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.3.1-1
- update to 9.3.1 (#1356324)
- drop upstreamed patch
- add requires on libmatroska 1.4.5+

* Wed Jun 01 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.2.0-1
- update to 9.2.0 (#1340601)
- relax precision in double precision arithmetic test on i686
  (upstream issue #1705)

* Sun May 22 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.1.0-2
- unbundle json
- clean up prep section

* Sat May 21 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.1.0-1.1
- rebuild for boost-1.60.0-5 (#1331983)

* Wed Apr 27 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.1.0-1
- update to 9.1.0 (#1329863)

* Tue Mar 29 2016 Dominik Mierzejewski <rpm@greysector.net> - 9.0.1-1
- update to 9.0.1 (#1321434)
- drop obsolete patch

* Mon Feb 22 2016 Dominik Mierzejewski <rpm@greysector.net> - 8.9.0-1
- update to 8.9.0
- autogenerate localized files list
- BR docbook-style-xsl and fix check for it

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jonathan Wakely <jwakely@redhat.com> - 8.8.0-2
- Rebuilt for Boost 1.60

* Tue Jan 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 8.8.0-1
- update to 8.8.0
- update Source and main URLs

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 8.7.0-2
- Rebuilt for Boost 1.60

* Tue Jan 05 2016 Dominik Mierzejewski <rpm@greysector.net> - 8.7.0-1
- update to 8.7.0

* Wed Dec 09 2015 Dominik Mierzejewski <rpm@greysector.net> - 8.6.1-1
- update to 8.6.1

* Thu Nov 26 2015 Dominik Mierzejewski <rpm@greysector.net> - 8.5.2-1
- update to 8.5.2

* Thu Oct 22 2015 Dominik Mierzejewski <rpm@greysector.net> - 8.5.1-1
- update to 8.5.1
- BR: libmatroska >= 1.4.4

* Mon Sep 21 2015 Dominik Mierzejewski <rpm@greysector.net> - 8.4.0-1
- update to 8.4.0
- drop obsolete patch
- add Provides: for bundled avilib
- wxGTK GUI is gone
- use license macro to tag the license text file

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 8.2.0-3
- Rebuilt for Boost 1.59

* Wed Aug 26 2015 Jonathan Wakely <jwakely@redhat.com> - 8.2.0-2
- Rebuilt for Boost 1.58 in F23

* Mon Aug 03 2015 Dominik Mierzejewski <rpm@greysector.net> - 8.2.0-1
- update to 8.2.0
- drop obsolete patch
- backport fix for compilation without curl (upstream issue 1359)
- include Spanish manpages

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 8.1.0-2
- rebuild for Boost 1.58

* Sun Jun 28 2015 Dominik Mierzejewski <rpm@greysector.net> - 8.1.0-1
- update to 8.1.0
- backport proper fix for issue 1284 from upstream
- fix -qt subpackage dependencies

* Fri Jun 26 2015 Dominik Mierzejewski <rpm@greysector.net> - 8.0.0-2
- fix tests which fail to compile with boost-1.56+

* Mon Jun 22 2015 Dominik Mierzejewski <rpm@greysector.net> - 8.0.0-1
- update to 8.0.0
- move find_lang call to install section
- disable tests which fail to compile (rhbz#1234405)
- build Qt5 GUI and reorganize subpackages
- switch Gtk GUI to GTK3
- unbundle drake

* Thu Jun 11 2015 Dominik Mierzejewski <rpm@greysector.net> - 7.9.0-1
- update to 7.9.0
- drop upstreamed patch for utf8cpp unbundling
- drop manual desktop file installation, upstream does it properly now

* Sat Apr 11 2015 Dominik Mierzejewski <rpm@greysector.net> - 7.8.0-2
- rebuilt for pugixml soname bump

* Mon Mar 30 2015 Dominik Mierzejewski <rpm@greysector.net> 7.8.0-1
- update to 7.8.0
- fix building tools
- unbundle utf8cpp

* Fri Mar 06 2015 Dominik Mierzejewski <rpm@greysector.net> 7.7.0-1
- update to 7.7.0
- include new manpages

* Mon Feb 09 2015 Dominik Mierzejewski <rpm@greysector.net> 7.6.0-1
- update to 7.6.0

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 7.5.0-3
- Rebuild for boost 1.57.0

* Thu Jan 15 2015 Dominik Mierzejewski <rpm@greysector.net> 7.5.0-2
- this actually build-requires libmatroska-1.4.2 (and libebml-1.3.1)
- remove bundled libebml and libmatroska so that they don't get used
  accidentally if available version is too low
- drop some old cruft from prep section

* Wed Jan 14 2015 Dominik Mierzejewski <rpm@greysector.net> 7.5.0-1
- update to 7.5.0

* Wed Dec 17 2014 Dominik Mierzejewski <rpm@greysector.net> 7.4.0-1
- update to 7.4.0
- drop obsolete patch (upstream bug #1090)
- shorten desktop and icon file installation commands

* Thu Dec 04 2014 Dominik Mierzejewski <rpm@greysector.net> 7.3.0-1
- update to 7.3.0
- enable unit tests
- use system boost code fragment and pugixml

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 7.2.0-2
- update icon/mime scriptlets

* Sun Sep 21 2014 Dominik Mierzejewski <rpm@greysector.net> 7.2.0-1
- update to 7.2.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Dominik Mierzejewski <rpm@greysector.net> 7.0.0-1
- update to 7.0.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 6.9.1-2
- Rebuild for boost 1.55.0

* Sun Apr 27 2014 Dominik Mierzejewski <rpm@greysector.net> 6.9.1-1
- update to 6.9.1

* Tue Mar 04 2014 Dominik Mierzejewski <rpm@greysector.net> 6.8.0-1
- update to 6.8.0
- fixes bug #1053883

* Sat Jan 18 2014 Dominik Mierzejewski <rpm@greysector.net> 6.7.0-1
- update to 6.7.0

* Fri Dec 27 2013 Dominik Mierzejewski <rpm@greysector.net> 6.6.0-1
- update to 6.6.0
- drop obsolete/redundant specfile parts
- remove executable bit from some sources
- drop version from libmatroska-devel BR
- disable curl support (used only for online update checks)

* Sun Oct 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 6.5.0-1
- Update to 6.5.0
- Fix duplicate localized man pages and add lang(de)

* Thu Oct 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 6.4.1-1
- Update to 6.4.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 6.3.0-2
- Rebuild for boost 1.54.0

* Sat Jul 13 2013 Nicolas Chauvet <kwizart@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Mon Apr 29 2013 Nicolas Chauvet <kwizart@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Fri Feb 22 2013 Nicolas Chauvet <kwizart@gmail.com> - 6.0.0-3
- Rebuilt for f19
- Fix bogus date

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 6.0.0-2
- Rebuild for Boost-1.53.0

* Tue Jan 22 2013 Nicolas Chauvet <kwizart@gmail.com> - 6.0.0-1
- Update to 6.0.0

* Mon Dec 10 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.9.0-1
- Update to 0.5.9

* Wed Sep 05 2012 Dominik Mierzejewski <rpm@greysector.net> 5.8.0-1
- update to 5.8.0

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 5.7.0-2
- Rebuild for new boost

* Sun Jul 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.7.0-1
- Update to 5.7.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.5.0-1
- Update to 5.5.0

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-3
- Rebuilt for c++ ABI breakage

* Tue Jan 17 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.2.1-2
- Add BR po4a

* Thu Jan 12 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.2.1-1
- Update to 5.2.1
- Add BR libcurl-devel

* Sun Nov 20 2011 Nicolas Chauvet <kwizart@gmail.com> - 5.0.1-1
- Update to 5.0.1

* Fri Sep 09 2011 Dan Horák <dan[at]danny.cz> - 4.9.1-3
- fix boost detection on other 64-bit arches (ax_boost_base.m4 too old)

* Sat Jul 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 4.9.1-2
- Rebuild for boost

* Thu Jul 14 2011 Nicolas Chauvet <kwizart@gmail.com> - 4.9.1-1
- Update to 4.9.1

* Tue Feb 15 2011 Nicolas Chauvet <kwizart@gmail.com> - 4.5.0-1
- Update to 4.5.0
- Backport Fix to build with boost::filesystem3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Dominik Mierzejewski <rpm@greysector.net> 4.4.0-1
- updated to 4.4.0
- build system switched to rake -> BR: ruby

* Sun Aug 01 2010 Dominik Mierzejewski <rpm@greysector.net> 4.2.0-1
- updated to 4.2.0 (many bugfixes, see upstream changelog:
  http://www.bunkus.org/cgi-bin/gitweb.cgi?p=mkvtoolnix.git;a=blob;f=ChangeLog)
- sorted BRs alphabetically
- use upstream .desktop files
- install 64x64 icons as well
- drop vendor from desktop filenames
- add Dutch manpages
- process mimeinfo file in scriptlets

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 4.0.0-2
- rebuilt against wxGTK-2.8.11-2

* Sat Jun 19 2010 Dominik Mierzejewski <rpm@greysector.net> 4.0.0-1
- updated to 4.0.0

* Sat May 29 2010 Dominik Mierzejewski <rpm@greysector.net> 3.4.0-1
- updated to 3.4.0
- drop unused %%{_datadir}/mkvtoolnix directory
- add build- and runtime requirements on newer libmatroska
- add runtime requirements on newer libebml due to ABI changes

* Sat Mar 27 2010 Dominik Mierzejewski <rpm@greysector.net> 3.3.0-1
- updated to 3.3.0

* Mon Feb 15 2010 Dominik Mierzejewski <rpm@greysector.net> 3.2.0-1
- updated to 3.2.0
- dropped versions from BRs, F-11 has same or newer
- added Chinese manpages

* Sat Jan 23 2010 Dominik Mierzejewski <rpm@greysector.net> 3.1.0-1
- updated to 3.1.0
  * BlueRay subtitles support
- added Japanese manpages

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.0-2
- Rebuild for Boost soname bump

* Sat Dec 26 2009 Dominik Mierzejewski <rpm@greysector.net> 3.0.0-1
- updated to 3.0.0
- dropped upstream'd patches

* Sun Dec 06 2009 Dominik Mierzejewski <rpm@greysector.net> 2.9.9-1
- updated to 2.9.9
  * new CLI tool: mkvpropedit
- fixed compilation of vc1parser

* Sun Sep 27 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 2.9.8-2
- Update desktop file according to F-12 FedoraStudio feature

* Wed Aug 26 2009 Dominik Mierzejewski <rpm@greysector.net> 2.9.8-1
- updated to 2.9.8
- improved summary and description for gui subpackage
- fixed installation of tools

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 06 2009 Dominik Mierzejewski <rpm@greysector.net> 2.6.0-1
- updated to 2.6.0
- dropped upstreamed patches

* Sun Mar 01 2009 Dominik Mierzejewski <rpm@greysector.net> 2.5.2-1
- updated to 2.5.2
- fix compilation
- include translated messages

* Fri Feb 27 2009 Dominik Mierzejewski <rpm@greysector.net> 2.5.1-1
- updated to 2.5.1
- dropped obsolete patches
- use new icon cache scriptlets
- add missing BR

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Dominik Mierzejewski <rpm@greysector.net> 2.4.2-1
- updated to 2.4.2
- dropped obsolete boost detection patch
- fixed segmentation fault in mmg (bug #477857)
- backported some minor fixes from current git
- fixed build on ppc64 again

* Wed Dec 17 2008 Benjamin Kosnik  <bkoz@redhat.com> 2.4.0-4
- Rebuild for boost-1.37.0.

* Mon Dec 01 2008 Dominik Mierzejewski <rpm@greysector.net> 2.4.0-3
- dropped obsolete mkvtoolnix-gcc43.patch

* Mon Dec 01 2008 Dominik Mierzejewski <rpm@greysector.net> 2.4.0-2
- fixed boost detection on ppc64 (and sparc64) (bug #473976)

* Sun Nov 30 2008 Dominik Mierzejewski <rpm@greysector.net> 2.4.0-1
- updated to 2.4.0
- rebased patch
- added new BRs
- added missing Requires: hicolor-icon-theme for hicolor icon dirs
- build and include more tools
- fixed rpmlint issues

* Sun Jun 01 2008 Dominik Mierzejewski <rpm@greysector.net> 2.2.0-1
- updated to 2.2.0
- dropped redundant BRs

* Fri Feb 15 2008 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-2
- fixed build with gcc-4.3

* Sun Aug 26 2007 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-1
- updated to 2.1.0
- updated license tag

* Sun Apr 15 2007 Dominik Mierzejewski <rpm@greysector.net> 2.0.2-1
- updated to 2.0.2

* Thu Feb 15 2007 Dominik Mierzejewski <rpm@greysector.net> 2.0.0-1
- updated to 2.0.0
- rebuilt against new flac

* Sat Dec 16 2006 Dominik Mierzejewski <rpm@greysector.net> 1.8.1-2
- rebuilt with new wxGTK

* Tue Dec 05 2006 Dominik Mierzejewski <rpm@greysector.net> 1.8.1-1
- updated to 1.8.1

* Sun Nov 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.8.0-3
- Update GTK icon cache in -gui's post(un)install phase, not main pkg's.
- Add menu entry for mkvinfo.

* Thu Nov 23 2006 Dominik Mierzejewski <rpm@greysector.net> 1.8.0-2
- moved mkvinfo and its manpage to -gui
- dropped --enable-debug from configure

* Sun Nov 19 2006 Dominik Mierzejewski <rpm@greysector.net> 1.8.0-1
- updated to 1.8.0
- prevent stripping binaries during make install
- removed sed from BRs
- made -gui Require: current version of the main package
- specfile cleanups

* Fri Jul 28 2006 Dominik Mierzejewski <rpm@greysector.net> 1.7.0-1
- updated to 1.7.0
- removed FCver dependent BRs

* Sun Apr 02 2006 Dominik Mierzejewski <rpm@greysector.net> 1.6.5-3
- added missing BRs
- enable all deps by default

* Sat Jan 07 2006 Dominik Mierzejewski <rpm@greysector.net> 1.6.5-2
- added desktop file and icon for GUI
- remove hardcoded -O3 from configure's CFLAGS

* Fri Jan 06 2006 Dominik Mierzejewski <rpm@greysector.net>
- dropped RH7.x support
- specfile cleanups

* Sun Dec 11 2005 Dominik Mierzejewski <rpm@greysector.net>
- updated to 1.6.5
- updated BuildRequires

* Thu Jul 07 2005 Dominik Mierzejewski <rpm@greysector.net>
- updated to 1.5.0

* Mon Apr 11 2005 Dominik Mierzejewski <rpm@greysector.net>
- fixed BRs for Fedoras

* Wed Jan 12 2005 Dominik Mierzejewski <rpm@greysector.net>
- fixed rebuilding under RH7.3

* Sat Jan 08 2005 Dominik Mierzejewski <rpm@greysector.net>
- updated to 1.0.1

* Sat Oct 16 2004 Dominik Mierzejewski <rpm@greysector.net>
- arranged sections in correct order
- split GUI into separate package
- added some bconds

* Sat Jan 03 2004 Ronald Bultje <rbultje@ronald.bitfreak.net
- set this thing up
