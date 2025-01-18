%global __cmake_in_source_build 1
%define _hardened_build 1
Name: ettercap
Version: 0.8.3.1
Release: 16%{?dist}
Summary: Network traffic sniffer/analyser, NCURSES interface version
License: GPL-2.0-or-later
URL: http://ettercap.sourceforge.net
Source0: https://github.com/Ettercap/ettercap/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: ettercap.desktop
Source2: ettercap-README.fedora
# Permission from upstream to drop the silly modification restriction
Source3: ettercap_easter_egg_license.txt
Patch1: ettercap-0.8.1-radius-stack-overflow.patch
Patch2: harfbuzz.patch
Patch3: 2168090f5b023573ebea0f83574950401ed5d67b.patch
Patch4: 1170.patch
Patch5: 40534662043b7d831d1f6c70448afa9d374a9b63.patch

BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
BuildRequires: gtk3-devel
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: libtool
BuildRequires: bison
BuildRequires: flex
BuildRequires: cmake
BuildRequires: libcurl-devel
BuildRequires: groff-base
BuildRequires: libappstream-glib
#some requirements are available in fedora but not in stock epel
#build for epel requires libnet which is only available from rpmforge
%if 0%{?rhel}
BuildRequires: libnet
#epel 5
BuildRequires: libtool-ltdl-devel
BuildRequires: libpcap-devel
%endif
%if 0%{?fedora}
BuildRequires: libpcap-devel
BuildRequires: libnet-devel
BuildRequires: libtool-ltdl-devel
%endif
BuildRequires: make
Requires: polkit ethtool

%description
Ettercap is a suite for man in the middle attacks on LAN. It features
sniffing of live connections, content filtering on the fly and many other
interesting tricks. It supports active and passive dissection of many
protocols (even ciphered ones) and includes many feature for network and host
analysis. 


%prep
%setup -q

%patch -P 1 -p1
%patch -P 2 -p0
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1

%build
mkdir build
pushd build
%cmake ../ -DINSTALL_PREFIX=/usr -DMAN_INSTALLDIR=%{_mandir} -DINSTALL_LIBDIR=%{_libdir} -DENABLE_IPV6=yes -DENABLE_GEOIP=no -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES
make CFLAGS="$RPM_BUILD_FLAGS"

%install
mkdir -p  %{buildroot}%{_bindir}
pushd build
make install DESTDIR=%{buildroot}
make install man DESTDIR=%{buildroot}
#getting rid of libtool files potentially left behind when building plugins
rm -f %{buildroot}%{_libdir}/ettercap/*.la
mkdir -p %{buildroot}%{_docdir}
install -c -m 644 %{SOURCE2} %{buildroot}%{_docdir}
install -c -m 644 %{SOURCE3} %{buildroot}%{_docdir}
touch %{buildroot}%{_bindir}/ettercap

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 ../share/ettercap.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
rm -f ettercap*png

popd
install -c -m 644 desktop/ettercap.appdata.xml %{buildroot}%{_metainfodir}/ettercap.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS CHANGELOG THANKS TODO* README doc/
%{_bindir}/etter*
%config(noreplace) %{_sysconfdir}/ettercap/
%{_docdir}/ettercap-README.fedora
%{_docdir}/ettercap_easter_egg_license.txt
%{_mandir}/man5/etter*
%{_mandir}/man8/etter*
%{_datadir}/ettercap/
%{_libdir}/ettercap/
%{_libdir}/libettercap.so.0*
%{_libdir}/libettercap.so
%{_libdir}/libettercap-ui.so.0*
%{_libdir}/libettercap-ui.so
%{_datadir}/applications/ettercap.desktop
%{_datadir}/icons/hicolor/32x32/apps/ettercap.png
%{_datadir}/pixmaps/ettercap.svg
%{_datadir}/polkit-1/actions/org.pkexec.ettercap.policy
%{_metainfodir}/ettercap.appdata.xml
%{_metainfodir}/ettercap.metainfo.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.3.1-12
- Upstream patch for curl 8+

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.3.1-10
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.8.3.1-8
- Move to pcre2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.8.3.1-5
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.8.3.1-3
- Disable RPATH.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.8.3.1-1
- 0.8.3.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.8.3-1
- 0.8.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16.20170306git60aca9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-15.20170306git60aca9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-14.20170306git60aca9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-13.20170306git60aca9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12.20170306git60aca9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.2-11.20170306git60aca9
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10.20170306git60aca9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9.20170306git60aca9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.8.2-8.20170306git60aca9
- Patch for CVE-2017-8366

* Mon Mar 06 2017 Jon Ciesla <limburgher@gmail.com> - 0.8.2-7.20170306git60aca9
- Patch for CVE-2017-6430.

* Tue Feb 21 2017 Jon Ciesla <limburgher@gmail.com> - 0.8.2-6
- Use compat-openssl10-devel

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 08 2016 Jon Ciesla <limburgher@gmail.com> - 0.8.2-4
- Use smaller icon, BZ 1228834.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Jon Ciesla <limburgher@gmail.com> - 0.8.2-1
- Latest upstream.

* Tue Dec 16 2014 Jon Ciesla <limburgher@gmail.com> - 0.8.1-2
- Patches for multiple CVEs

* Mon Nov 03 2014 Jon Ciesla <limburgher@gmail.com> - 0.8.1-1
- 0.8.1.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 20 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.0-1
- 0.8.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.6-1
- Enable ipv6.
- 0.7.6, BZ 928245.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.5.3-2
- Drop desktop vendor tag.

* Fri Feb 01 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.5.3-1
- 0.7.5.3 final.

* Tue Jan 29 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.5.2-1
- 0.7.5.2 final.
- BR groff-base.

* Mon Jan 14 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.5.1-1
- 0.7.5.1, patch for CVE-2013-0722.
- Added libcurl-devel BR.

* Thu Oct 18 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.5-3
- 0.7.5 final.

* Tue Oct 16 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.5-2.1.20120906gitc796e5
- Fix DHCP spoofing in gtk interface, BZ 867075.

* Mon Sep 10 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.5-1.1.20120906gitc796e5
- Fixed Release tag and build flags, BZ 855504.

* Thu Sep 06 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.5-0.20120906gitc796e5
- Fixed Obsoletes, BZ 855067.

* Tue Sep 04 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.5-0.20120905gitc796e5
- Switch to git ettercap_rc branch for gtk crash, BZ 853791.
- Dropped UI and daemon patches.
- Merged subpackages, in part due to buildsystem change.
- Spec cleanup.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 12 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.4.1-3
- Add hardened build.

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.4.1-2
- libnet rebuild.

* Mon Mar 12 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.4.1-1
- New upstream.

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.7.4-4
- Rebuild against PCRE 8.30

* Mon Jan 30 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.4-3
- RPM_OPT_FLAGS fix, BZ 785562.

* Thu Jan 26 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.4-2
- Patch for CVE-2010-3843.

* Thu Jan 26 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.4-1
- New upstream. Now BRs bison, flex.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.3-39
- Rebuild for new libpng

* Wed Feb 09 2011 Tom Callaway <spot@fedoraproject.org> - 0.7.3-38
- fix licensing issue with easter egg and include documentation of permission
  from upstream

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Jon Ciesla <limb@jcomserv.net> - 0.7.3-36
- Patch to support passive DNS, BZ 646162.

* Fri Apr 23 2010 Jon Ciesla <limb@jcomserv.net> - 0.7.3-35
- Patch for 64bit crash by Timothy Redaelli, BZ 550237.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.7.3-34
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Jon Ciesla <limb@jcomserv.net> - 0.7.3-32
- Patch for selinux/fctnl issue, BZ 491612.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Jon Ciesla <limb@jcomserv.net> - 0.7.3-30
- Correction to -29.

* Wed Feb 04 2009 Jon Ciesla <limb@jcomserv.net> - 0.7.3-29
- Use more reasonably sized icon, BZ484030.

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 0.7.3-28
- rebuild with new openssl

* Thu Dec 04 2008 Caolán McNamara <caolanm@redhat.com> - 0.7.3-27
- rebuild for dependencies

* Mon Jun 16 2008 Jon Ciesla <limb@jcomserv.net> - 0.7.3-26
- Fix for mitm CPU util bug.

* Thu Jun 12 2008 Jon Ciesla <limb@jcomserv.net> - 0.7.3-25
- Corrected -24 patch.

* Thu Jun 12 2008 Jon Ciesla <limb@jcomserv.net> - 0.7.3-24
- Patch to fix daemon mode mitm behaviour BZ 450923.

* Tue Jun 10 2008 Jon Ciesla <limb@jcomserv.net> - 0.7.3-23
- Patch to fix ui in daemon mode BZ 450029.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 0.7.3-22
- GCC 4.3 rebuild.

* Wed Dec 05 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-21
- Rebuild due to openssl soname bump.
- Fixed desktop icon path.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-20
- License tag correction.
- Fixed open() in ec_log.c

* Wed Mar 28 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-19
- /usr/bin/ettercap ownership fix.

* Tue Mar 27 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-18
- Obsoletes fix.

* Mon Mar 26 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-17
- Provides/obsoletes fixes.

* Mon Mar 26 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-16
- Merged -plugins into common.
- Fixed UI patch from Till Maas.

* Sat Mar 24 2007 Manuel Wolfshant <wolfy@pcnet.ro> - 0.7.3-15
- Unified spec for epel / FC5 / FC6; build for epel is not possible until
 libnet is made available

* Fri Mar 23 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-14
- Alternatives fix by Manuel Wolfshant.
- Please run rpm -e ettercap ettercap-gtk --noscripts before upgrading.
- Bump to unified FC5 compat.

* Thu Mar 15 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-12
- Added ettercap-README.fedora
- Fixed Requires versioning.

* Thu Mar 15 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-11
- Fixed several typos, clarified a few minor things.

* Thu Mar 15 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-10
- Added doc and README.
- Replaced symlinks with alternatives solution.

* Thu Mar 15 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-9
- Removed libtool BR.
- Removed .la files.
- Moved plugins to subpackage.
- Re-added Provides to GTK package.

* Tue Mar 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-8
- Added libtool-ltdl-devel BR.
- Removed full path from desktop.
- Dropped provides from gtk package

* Tue Mar 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-7
- Fixed .desktop icon path
* Tue Mar 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-6
- Moved to consistent buildroot.
- Fixed BR, Rs.

* Tue Mar 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-5
- Removed dupes, moved symlinks for t and c to common only
- Moved desktop scriptlets to gtk package.
- Moved curses man page to curses package.

* Tue Mar 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-4
- Added Provides

* Tue Mar 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-3
- Updated BRs.
- Split out gtk and NCURSES versions from common package.
- Added UI patch from Till Maas, symlinks, .desktop, icon installation.

* Sat Mar 10 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-2
- Corrected Source URL.

* Sat Mar 10 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.3-1
- Initial packaging.
