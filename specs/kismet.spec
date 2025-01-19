%global _hardened_build 1
%global _version        2023-07-R1

## {Local macros...
%global cfgdir          %_sysconfdir/%name
%global _rpmversion     0.0.%(echo %_version | tr - .)
## ...local macros}

%{!?apply:%global  apply(p:n:b:) %patch%%{-n:%%{-n*}} %%{-p:-p%%{-p*}} %%{-b:-b%%{-b*}} \
%nil}

Summary:        WLAN detector, sniffer and IDS
Name:           kismet
Version:        %_rpmversion
Release:        8%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.kismetwireless.net/
Source0:        http://www.kismetwireless.net/code/%{name}-%_version.tar.xz

Patch0:         kismet-include.patch
Patch1:         kismet-install.patch
Patch2:         hak5-types.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel diffutils
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel libcap-devel libnl3-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  libmicrohttpd-devel protobuf-devel protobuf-c-devel
BuildRequires:  NetworkManager-libnm-devel libusb1-devel
BuildRequires:  sqlite-devel libwebsockets-devel
BuildRequires: make

%description
Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system. Kismet will work with any wireless card
which supports raw monitoring (rfmon) mode, and can sniff 802.11b,
802.11a, and 802.11g traffic.

Kismet identifies networks by passively collecting packets and detecting
standard named networks, detecting (and given time, decloaking) hidden
networks, and infering the presence of nonbeaconing networks via data
traffic.

%prep
%setup -qn %{name}-%{_version}

%patch -P 0 -p0
%patch -P 1 -p0
%patch -P 2 -p0

sed -i 's!\$(prefix)/lib/!%{_libdir}/!g' plugin-*/Makefile


# set our 'kismet' user, disable GPS and log into %%logdir by
# default
sed -i \
    -e '\!^ouifile=/etc/manuf!d' \
    -e '\!^ouifile=/usr/share/wireshark/wireshark/manuf!d' \
    conf/kismet.conf

sed -i s/@VERSION@/%{version}/g packaging/kismet.pc.in

%build

export ac_cv_lib_uClibcpp_main=no # we do not want to build against uClibc++, even when available
export LDFLAGS='-Wl,--as-needed'
%configure \
           --sysconfdir=%cfgdir \
           CXXFLAGS="$RPM_OPT_FLAGS -D__STDC_FORMAT_MACROS" \
           --disable-python-tools

%make_build


%install
BIN=$RPM_BUILD_ROOT/bin ETC=$RPM_BUILD_ROOT/etc %{__make} suidinstall DESTDIR=%{?buildroot} INSTALL="%{__install} -p"

%pre
getent group kismet >/dev/null || groupadd -f -r kismet

%files
%doc README*
%dir %attr(0755,root,root) %cfgdir
%config(noreplace) %cfgdir/*
%{_bindir}/kismet
%{_bindir}/kismet_cap_kismetdb
%{_bindir}/kismet_cap_pcapfile
%{_bindir}/kismet_discovery
%{_bindir}/kismet_server
%{_bindir}/kismetdb_clean
%{_bindir}/kismetdb_dump_devices
%{_bindir}/kismetdb_statistics
%{_bindir}/kismetdb_strip_packets
%{_bindir}/kismetdb_to_gpx
%{_bindir}/kismetdb_to_kml
%{_bindir}/kismetdb_to_pcap
%{_bindir}/kismetdb_to_wiglecsv
%attr(4755,root,root) %{_bindir}/kismet_cap_hak5_wifi_coconut
%attr(4755,root,root) %{_bindir}/kismet_cap_linux_bluetooth
%attr(4755,root,root) %{_bindir}/kismet_cap_linux_wifi
%attr(4755,root,root) %{_bindir}/kismet_cap_nrf_51822
%attr(4755,root,root) %{_bindir}/kismet_cap_nrf_52840
%attr(4755,root,root) %{_bindir}/kismet_cap_nrf_mousejack
%attr(4755,root,root) %{_bindir}/kismet_cap_nxp_kw41z
%attr(4755,root,root) %{_bindir}/kismet_cap_rz_killerbee
%attr(4755,root,root) %{_bindir}/kismet_cap_ti_cc_2531
%attr(4755,root,root) %{_bindir}/kismet_cap_ti_cc_2540
%{_datadir}/kismet
%{_libdir}/pkgconfig/kismet.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2023.07.R1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2023.07.R1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2023.07.R1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2023.07.R1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2023.07.R1-1
- 2023-07-R1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2022.08.R1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2022.08.R1-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2022.08.R1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 09 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2022.08.R1-1
- 2022-08-R1

* Fri Jul 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2022.02.R1-4
- Move to libusb1, drop pcre-devel BR.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2022.02.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2022.02.R1-2
- websockets rebuild

* Fri Feb 11 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2022.02.R1-1
- 2022-02-R1

* Thu Jan 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2022.01.R3-1
- 2022-01-R3

* Thu Jan 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2022.01.R2-1
- 2022-01-R2

* Wed Jan 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2022.01.R1-1
- 2022-01-R1

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 0.0.2021.08.R1-4
- Rebuilt for protobuf 3.19.0

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 0.0.2021.08.R1-3
- Rebuilt for protobuf 3.18.1

* Thu Aug 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2021.08.R1-2
- libwebsockets rebuild.

* Tue Aug 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2021.08.R1-1
- 2021-08-R1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2021.06.R1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2021.06.R1-1
- 2021-06-R1

* Tue May 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2021.05.R1-2
- Harden build, setguid.

* Thu May 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2021.05.R1-1
- 2021-05-R1

* Mon May 10 2021 Jonathan Wakely <jwakely@redhat.com> - 0.0.2020.12.R3-5
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 0.0.2020.12.R3-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.12.R3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 08:46:06 CET 2021 Adrian Reber <adrian@lisas.de> - 0.0.2020.12.R3-2
- Rebuilt for protobuf 3.14

* Mon Dec 07 2020 Gwyn Ciesla <gwync@protonmail.com>- 0.0.2020.12.R3-1
- 2020-12-R3

* Fri Dec 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2020.12.R1-1
- 2020-12-R1

* Fri Sep 25 2020 Adrian Reber <adrian@lisas.de> - 0.0.2020.09.R4-2
- Rebuilt(2) for protobuf 3.13

* Fri Sep 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2020.09.R4-1
- 2020-09-R4

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 0.0.2020.09.R3-2
- Rebuilt for protobuf 3.13

* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2020.09.R3-1
- 2020-09-R3

* Fri Sep 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2020.09.R2-1
- 2020-09-R2

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2020.09.R1-1
- 2020-09-R1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.04.R3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.04.R3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 0.0.2020.04.R3-2
- Rebuilt for protobuf 3.12

* Sun May 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2020.04.R3-1
- Latest upstream.

* Tue Apr 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2020.04.R2-1
- Latest upstream.

* Tue Apr 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2020.04.R1-1
- Latest upstream.

* Mon Mar 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2020.03.R1-1
- Latest upstream.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2019.12.R2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2019.12.R2-1
- Latest upstream.

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2019.12.R1-1
- Latest upstream.

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 0.0.2019.09.R1-2
- Rebuild for protobuf 3.11

* Tue Sep 03 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2019.09.R1-1
- Latest upstream.

* Thu Aug 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2019.08.R2-1
- latest upstream.

* Wed Jul 31 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2019.08.R1-1
- Latest upstream.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2019.07.R1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2019.07.R1-1
- Latet upstream.

* Thu May 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2019.05.R2-1
- Latest upstream.

* Thu May 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2019.05.R1-1
- Latest upstream.

* Mon Apr 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.0.2019.04.R1-1
- Latest upstream.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2016.07.R1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.0.2016.07.R1-8
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2016.07.R1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2016.07.R1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2016.07.R1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2016.07.R1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2016.07.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2016.07.R1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Jon Ciesla <limburgher@gmail.com> - 0.0.2016.07.R1-1
- Latest stable upstream.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2013.03.R1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2013.03.R1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.2013.03.R1-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2013.03.R1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2013.03.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2013.03.R1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Jon Ciesla <limburgher@gmail.com> - 0.0.2013.03.R1-1
- Latest stable upstream.
- Changed to libnl3

* Tue Mar 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.0.2011.03.R2-1607.20120307git6b8b77
- Revert pthread link flag change.

* Thu Mar 07 2013 Jon Ciesla <limburgher@gmail.com> - 0.0.2011.03.R2-1606.20120307git6b8b77
- Upgrade to latest git snapshot, BZ 917276.

* Fri Mar 01 2013 Jon Ciesla <limburgher@gmail.com> - 0.0.2011.03.R2-1605
- Spec cleanup.
- Switch from dietlibc to glibc.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2011.03.R2-1604
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2011.03.R2-1603
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.0.2011.03.R2-1602
- Rebuild against PCRE 8.30
- Fix %%files section for plugins

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2011.03.R2-1601
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 23 2011 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2011.03.R2-1600
- updated to 2011-03-R2

* Sat Apr  2 2011 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2011.03.R1-1600
- updated to 2011-03-R1 (#692715)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2010.07.R1-1501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2010.07.R1-1500
- updated to 2010-07-R1; rediffed patches

* Sun Feb 21 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2010.01.R1-1400
- added patch to honor listen configuration (#553275)

* Sat Jan 16 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2010.01.R1-1300
- updated to 2010-01-R1
- rediffed patches

* Sun Dec  6 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2009.11.R1-1300
- updated to 2009-11-R1

* Sun Aug  9 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- enhanced kismet_capture's pam configuration file

* Sun Aug  9 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2009.06.R1-1
- added Obsoletes: entry for old -extras subpackage

* Sun Aug  9 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2009.06.R1-0
- updated to 2009-06-R1
- reworked large parts of the package due to major upstream changes:
  * there is no separate user anymore but a kismet_capture consolehelper wrapper
  * a lot of the old filesystem layout has been changed/removed
  * removed -extras subpackage; added -plugins one

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2008.05.R1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.0.2008.05.R1-5
- Add patch to fix build against GCC 4.4 (#490811)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2008.05.R1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.2008.05.R1-3
- fix license tag

* Sat Jun 21 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2008.05.R1-2
- applied forgotten patch
- honor $NO_TMPWATCH instead of $NO_LOGROTATE in the tmpwatch script (#427262)

* Sat Jun 21 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2008.05.R1-1
- updated to 2008-05-R1
- removed some patches and added new ones

* Fri Jun 06 2008 Caolán McNamara <caolanm@redhat.com> - 0.0.2007.10.R1-4
- tweak configure to use -lMagickCore not -lMagick to rebuild for dependancies

* Fri Feb 22 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2007.10.R1-3
- fixed build with gcc43 (#434084, thx to Erik van Pienbroek)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Sat Nov 10 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2007.10.R1-2
- rebuilt for new libexpat

* Mon Oct  8 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2007.10.R1-1
- updated to 2007-10-R1
- dropped/rediffed patches
- added BR on dbus-devel

* Sun Feb  4 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2007.01.R1b-7
- further x86_64 fixes for printf() format-string modifiers

* Sat Feb  3 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2007.01.R1b-6
- updated to 2007-01-R1b
- removed most patches which were applied upstream; rediffed remaining
  ones
- added -setgroups patch
- added libpcap-devel BR; removed the glib-devel + bzip2-devel one
- build with '-Wl,--as-needed'

* Fri Sep 15 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2006.04.R1-4
- rebuilt

* Sun Jul  9 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2006.04.R1-3
- use new fedora-usermgmt code

* Sat Apr 29 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2006.04.R1-2
- fixed compilation problems on AMD64 introduced by my -alias patch
  (reported by Hans de Goede)
- fixed ssize_t vs. int problem on AMD64 (found and reported by Hans
  de Goede)
- initial import into Fedora Extra (review #165314)
- added 'freetype-devel' BR which is required for -devel branch

* Sat Apr 22 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2006.04.R1-1
- updated to 2006-04-R1
- fixed/improved some ./configure checks
- removed the starting 'A' from the summary
- added a bunch of patches fixing compiler warnings

* Fri Mar 17 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2005.08.R1-3
- fixed the usermgmt in the %%postun script: test for uninstallation
  and swap order of user- and groupdel operations
- moved logs to /var/log/kismet
- placed status information directly under /var/lib/kismet instead of
  /var/lib/kismet/.kismet
- added /etc/cron.dail/tmpwatch.kismet to cleanup the generated
  logfiles; used tmpwatch because kismet creates new, differently
  named logfiles.
- added -jobcontrol patch

* Thu Mar 16 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2005.08.R1-2
- set *USR and *GRP variables to avoid problems with certain 'install'
  versions

* Thu Aug 18 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2005.08.R1-1
- updated to 2005-08-R1 (SECURITY)
- do not use 'subst()' in %%prep anymore; the files *will* be touched
  so we do not need to care about the timestamp
- fixed copy&paste error in the gecos entry of the 'kismet' user

* Sun Aug  7 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2005.07.R1a-1
- updated to 2005-07-R1a

* Sat Jul  9 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.0.2005.06.R1-1
- Initial build.


## Local Variables:
## outline-regexp: "##\\s-*{.*\\.\\.\\."
## outline-heading-end-regexp: "##\\s-*\\.\\.\\..*}"
## End:
