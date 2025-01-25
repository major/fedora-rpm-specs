%bcond_with audacious
%bcond_without curl
%bcond_without ibm
%bcond_without imlib
%bcond_without lua_cairo
%bcond_without lua_imlib
%bcond_with moc
%bcond_without mpd
%bcond_without ncurses
%bcond_with nvidia
%bcond_without portmon
%bcond_without rss
%bcond_without weather
%bcond_without weather_xoap
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 8
%bcond_with wlan
%else
%bcond_without wlan
%endif
%bcond_without xdbe
%bcond_without xinerama

Name:           conky
Version:        1.22.0
Release:        1%{?dist}
Summary:        A system monitor for X

License:        GPL-3.0-or-later AND LGPL-2.1-or-later AND MIT-open-group AND BSD-3-Clause
URL:            https://github.com/brndnmtthws/conky
Source0:        https://github.com/brndnmtthws/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix build failure with gcc 15
Patch0:         conky-cstdint.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libXft-devel
BuildRequires:  libXt-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  lua-devel
%{?with_audacious:BuildRequires: audacious-devel < 3.5 dbus-glib-devel}
%{?with_curl:BuildRequires: curl-devel}
%{?with_imlib:BuildRequires: imlib2-devel}
%{?with_lua_cairo:BuildRequires: cairo-devel tolua++-devel}
%{?with_lua_imlib:BuildRequires: imlib2-devel tolua++-devel}
%{?with_ncurses:BuildRequires: ncurses-devel}
%{?with_nvidia:BuildRequires: libXNVCtrl-devel}
%{?with_rss:BuildRequires: curl-devel libxml2-devel}
%{?with_weather:BuildRequires: curl-devel}
%{?with_weather_xoap:BuildRequires: libxml2-devel}
%{?with_wlan:BuildRequires: wireless-tools-devel}
%{?with_xinerama:BuildRequires: libXinerama-devel}
BuildRequires:  pandoc
BuildRequires:  python3-pyyaml python3-jinja2
BuildRequires:  cmake git
BuildRequires:  desktop-file-utils

%description
A system monitor for X originally based on the torsmo code. but more kickass.
It just keeps on given'er. Yeah.

%prep
%setup -q
%autopatch -p1

# remove executable bits from files included in %{_docdir}
chmod a-x extras/convert.lua

for i in AUTHORS; do
    iconv -f iso8859-1 -t utf8 -o ${i}{_,} && touch -r ${i}{,_} && mv -f ${i}{_,}
done

%build
%cmake \
                            -DBUILD_DOCS=ON \
                            -DBUILD_BUILTIN_CONFIG=OFF \
                            -DBUILD_SHARED_LIBS:BOOL=OFF \
    %{?with_audacious:      -DBUILD_AUDACIOUS=ON} \
    %{?with_curl:           -DBUILD_CURL=ON} \
    %{!?with_ibm:           -DBUILD_IBM=OFF} \
    %{?with_imlib:          -DBUILD_IMLIB2=ON} \
    %{?with_lua_cairo:      -DBUILD_LUA_CAIRO=ON} \
    %{?with_lua_imlib:      -DBUILD_LUA_IMLIB2=ON} \
    %{!?with_moc:           -DBUILD_MOC=OFF} \
    %{!?with_mpd:           -DBUILD_MPD=OFF} \
    %{!?with_ncurses:       -DBUILD_NCURSES=OFF} \
    %{?with_nvidia:         -DBUILD_NVIDIA=ON} \
    %{!?with_portmon:       -DBUILD_PORT_MONITORS=OFF} \
    %{?with_rss:            -DBUILD_RSS=ON} \
    %{?with_weather:        -DBUILD_WEATHER_METAR=ON} \
    %{?with_weather_xoap:   -DBUILD_WEATHER_XOAP=ON} \
    %{?with_wlan:           -DBUILD_WLAN=ON} \
    %{?with_xdbe:           -DBUILD_XDBE=ON} \
    %{?!with_xinerama:      -DBUILD_XINERAMA=OFF} \
    ;

%cmake_build


%install
%cmake_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/conky
install -m644 -p data/conky.conf $RPM_BUILD_ROOT%{_sysconfdir}/conky
rm -rf $RPM_BUILD_ROOT%{_docdir}/conky-*
rm -f $RPM_BUILD_ROOT%{_libdir}/libtcp-portmon.a
rm -f $RPM_BUILD_ROOT/usr/lib/libconky_core.a


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/conky.desktop


%files
%doc AUTHORS COPYING README.md extras/*
%dir %{_sysconfdir}/conky
%config %{_sysconfdir}/conky/conky.conf
%{_bindir}/conky
%if %{with lua_cairo} || %{with lua_imlib}
%{_libdir}/conky
%endif
%{_datadir}/applications/conky.desktop
%{_datadir}/icons/hicolor/*/apps/conky*
%{_mandir}/man1/conky.1*


%changelog
* Thu Jan 23 2025 Miroslav Lichvar <mlichvar@redhat.com> - 1.22.0-1
- update to 1.22.0
- fix FTBFS with new gcc (#2339994)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 10 2024 Miroslav Lichvar <mlichvar@redhat.com> - 1.21.7-1
- update to 1.21.7

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 01 2024 Miroslav Lichvar <mlichvar@redhat.com> - 1.19.6-1
- update to 1.19.6

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 21 2023 Miroslav Lichvar <mlichvar@redhat.com> - 1.19.2-1
- update to 1.19.2

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 1.19.0-2
- Rebuild fo new imlib2

* Mon Apr 03 2023 Miroslav Lichvar <mlichvar@redhat.com> - 1.19.0-1
- update to 1.19.0

* Mon Mar 06 2023 Miroslav Lichvar <mlichvar@redhat.com> - 1.18.2-1
- update to 1.18.2

* Mon Feb 27 2023 Miroslav Lichvar <mlichvar@redhat.com> - 1.18.1-1
- update to 1.18.1

* Mon Feb 20 2023 Miroslav Lichvar <mlichvar@redhat.com> - 1.18.0-1
- update to 1.18.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Miroslav Lichvar <mlichvar@redhat.com> - 1.15.0-1
- update to 1.15.0

* Tue Sep 20 2022 Miroslav Lichvar <mlichvar@redhat.com> - 1.13.1-1
- update to 1.13.1
- enable ncurses support

* Thu Jul 28 2022 Jonathan Wright <jonathan@almalinux.org> - 1.12.2-5
- Initial build for EPEL8 and EPEL9
- Fixes rhbz#1765376

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 02 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.12.2-2
- Disable Wireless Extensions support (Fedora 36+)
  https://fedoraproject.org/wiki/Changes/RemoveWirelessExtensions

* Tue Sep 21 2021 Miroslav Lichvar <mlichvar@redhat.com> - 1.12.2-1
- update to 1.12.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 08 2021 Miroslav Lichvar <mlichvar@redhat.com> - 1.12.1-1
- update to 1.12.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Miroslav Lichvar <mlichvar@redhat.com> - 1.11.6-1
- update to 1.11.6
- convert to new cmake rpm macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Miroslav Lichvar <mlichvar@redhat.com> - 1.11.5-3
- enable cairo and imlib modules again (#1768166)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Miroslav Lichvar <mlichvar@redhat.com> - 1.11.5-1
- update to 1.11.5
- disable cairo and imlib modules to build without tolua++

* Tue Jul 30 2019 Miroslav Lichvar <mlichvar@redhat.com> - 1.11.4-1
- update to 1.11.4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Miroslav Lichvar <mlichvar@redhat.com> - 1.11.3-1
- update to 1.11.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Miroslav Lichvar <mlichvar@redhat.com> - 1.10.8-1
- update to 1.10.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Miroslav Lichvar <mlichvar@redhat.com> - 1.10.7-1
- update to 1.10.7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Miroslav Lichvar <mlichvar@redhat.com> - 1.10.6-1
- update to 1.10.6
- fix building with new gcc (#1423306)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 18 2016 Miroslav Lichvar <mlichvar@redhat.com> - 1.10.4-1
- update to 1.10.4

* Tue May 03 2016 Miroslav Lichvar <mlichvar@redhat.com> - 1.10.1-5.20160413git06f87b
- update to 1.10.1-20160413git06f87b
- enable port monitor (#1320739)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4.20160110gitb38ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Tim Niemueller <tim@niemueller.de> - 1.10.1-3.20160110gitb38ab1-3
- rebuild for updated tolua++

* Mon Jan 11 2016 Miroslav Lichvar <mlichvar@redhat.com> - 1.10.1-2.20160110gitb38ab1
- update to 1.10.1-20160110gitb38ab1

* Fri Dec 04 2015 Miroslav Lichvar <mlichvar@redhat.com> - 1.10.1-1.20151201git1abd25
- update to 1.10.1-20151201git1abd25
- enable double-buffering support (#1284232)

* Tue Nov 03 2015 Miroslav Lichvar <mlichvar@redhat.com> - 1.10.0-1.20150824git341495
- update to 1.10.0-20150824git341495
- don't package manual in html

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-14.20141003git30d09e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 16 2014 Miroslav Lichvar <mlichvar@redhat.com> - 1.9.0-13.20141003git30d09e
- update to 20141003git30d09e
- build with lua-5.2 for new tolua++

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-12.20140617gitab826d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Miroslav Lichvar <mlichvar@redhat.com> - 1.9.0-11.20140617gitab826d
- build with lua-5.1 (#1117120)

* Mon Jun 23 2014 Miroslav Lichvar <mlichvar@redhat.com> - 1.9.0-10.20140617gitab826d
- update to 20140617gitab826d

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-9.20131027git11a13d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Miroslav Lichvar <mlichvar@redhat.com> - 1.9.0-8.20131027git11a13d
- disable audacious support (#1090655)

* Tue Oct 29 2013 Miroslav Lichvar <mlichvar@redhat.com> - 1.9.0-7.20131027git11a13d
- update to 20131027git11a13d
- enable weather support (#1024089)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-6.20121101gitbfaa84
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 1.9.0-5.20121101gitbfaa84
- rebuild for lua 5.2

* Tue Apr 09 2013 Miroslav Lichvar <mlichvar@redhat.com> - 1.9.0-4.20121101gitbfaa84
- update to 20121101gitbfaa84
- remove obsolete macros

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Miroslav Lichvar <mlichvar@redhat.com> - 1.9.0-1
- update to 1.9.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 24 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.8.1-4
- Rebuild as needed for 1.8.1-3 and latest Audacious library deps.
- Fix rebuild failure on Rawhide (no <curl/types.h>).

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.8.1-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 06 2010 Miroslav Lichvar <mlichvar@redhat.com> - 1.8.1-1
- update to 1.8.1

* Wed Apr 21 2010 Miroslav Lichvar <mlichvar@redhat.com> - 1.8.0-4
- remove rpath

* Wed Apr 14 2010 Miroslav Lichvar <mlichvar@redhat.com> - 1.8.0-3
- enable imlib support (#581986)

* Thu Apr 01 2010 Miroslav Lichvar <mlichvar@redhat.com> - 1.8.0-2
- update to 1.8.0

* Mon Feb 15 2010 Miroslav Lichvar <mlichvar@redhat.com> - 1.7.2-2
- fix building with new audacious (#556317)

* Tue Aug 25 2009 Miroslav Lichvar <mlichvar@redhat.com> - 1.7.2-1
- Update to 1.7.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Miroslav Lichvar <mlichvar@redhat.com> - 1.7.1.1-2
- Rebuild for new audacious
- Buildrequire libxml2-devel

* Wed Jun 17 2009 Miroslav Lichvar <mlichvar@redhat.com> - 1.7.1.1-1
- Update to 1.7.1.1

* Mon May 11 2009 Miroslav Lichvar <mlichvar@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 26 2008 Miroslav Lichvar <mlichvar@redhat.com> - 1.6.1-1
- Update to 1.6.1
- Fix buffer overflow when reading interface addresses

* Tue Jul 22 2008 Miroslav Lichvar <mlichvar@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Fix freq_dyn on x86_64

* Tue Apr 01 2008 Miroslav Lichvar <mlichvar@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Sun Mar 23 2008 Miroslav Lichvar <mlichvar@redhat.com> - 1.5.0-1
- Update to 1.5.0
- Convert doc files to UTF-8

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.9-2
- Autorebuild for GCC 4.3

* Tue Nov 27 2007 Miroslav Lichvar <mlichvar@redhat.com> - 1.4.9-1
- Update to 1.4.9
- Enable support for Audacious 1.4.0

* Sun Oct 21 2007 Miroslav Lichvar <mlichvar@redhat.com> - 1.4.8-1
- Update to 1.4.8
- Enable mpd, rss and wireless support
- Update license tag

* Wed Apr 18 2007 Michael Rice <errr[AT]errr-online.com> - 1.4.5-4
- Rebuild to match audacious lib in fc6 bug: 236989

* Mon Apr 09 2007 Michael Rice <errr[AT]errr-online.com> - 1.4.5-3
- Rebuild for devel

* Thu Dec 14 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.5-2
- Ship NEWS
- Add patch for license of timed_thread and NEWS

* Tue Dec 12 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.5-1
- version bump
- change group
 
* Wed Dec 06 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.4-3
- rebuild for new audacious lib version

* Thu Nov 30 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.4-2
- Move nano and vim files into docs
- remove unneeded BR's

* Tue Nov 21 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.4-1
- Version bump
- Add vim and nano syntax files to package

* Thu Oct 05 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.3-1
- Version bump
- Remove Install file from docs

* Mon Oct 02 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.2-4
- moved to configure macro from ./configure
- clean up changelog and make more informative entrys
- Fixed sumary in spec file
- remove NEWS file since it was empty
- remove xmms support due to possible security issue
- remove bmp support due to possible security issue
- add missing BR for libXext-devel and remove unneeded libX11-devel  

* Thu Sep 28 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.2-3
- use the GPL as licence since the whole package is GPL

* Thu Sep 28 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.2-2
- remove unneeded deps

* Tue Sep 26 2006 Michael Rice <errr[AT]errr-online.com> - 1.4.2-1
- Initial RPM release
