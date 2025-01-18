Name:           centerim
Version:        4.22.10
Release:        47%{?dist}
Epoch:          1

Summary:        Text mode menu- and window-driven IM

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.centerim.org/
Source0:        http://www.centerim.org/download/releases/%{name}-%{version}.tar.gz
Source1:        http://www.centerim.org/images/b/b5/Centerim_b.svg
Source2:        centerim.desktop

Patch0:         centerim-4.22.6-url-escape-fedora.patch
Patch1:         centerim-gcc46.patch
# doubled slashes in paths cause debugedit to error with:
# canonicalization unexpectedly shrank by one character
# https://bugzilla.redhat.com/show_bug.cgi?id=304121
Patch2:         centerim-double-slash.patch
Patch3:         centerim-c99.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  curl-devel
BuildRequires:  ncurses-devel >= 4.2
BuildRequires:  gettext-devel
BuildRequires:  gpgme-devel
BuildRequires:  libjpeg-devel
BuildRequires:  desktop-file-utils
BuildRequires:  lzo-devel >= 2
BuildRequires:  nss-devel
BuildRequires:  nspr-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires: make

Requires:       xdg-utils

Provides:       centericq = 4.21.0
Obsoletes:      centericq <= 4.21.0

%description
CenterIM is a text mode menu- and window-driven IM interface that supports
the ICQ2000, Yahoo!, MSN, AIM TOC, IRC, Gadu-Gadu and Jabber protocols.
Internal RSS reader and a client for LiveJournal are provided.


%prep
%setup -q
%patch -P0 -p1 -b .url-escape-fedora
%patch -P1 -p1 -b .gcc46
%patch -P2 -p1 -b .dblslash
%patch -P3 -p1 -b .c99

iconv -f iso8859-1 -t utf8 ChangeLog >ChangeLog.utf8
touch -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
# The doubleslash path touches Makefile.am
autoreconf -vfi
autoconf
%configure \
        --with-ssl \
        --disable-rpath \
        --enable-locales-fix
%make_build


%check
make check


%install
%make_install
%find_lang %{name}

# Remove unnecessary stuff
rm %{buildroot}%{_bindir}/CenterIMLog2HTML.py
find %{buildroot} -type f -name "*.la" -delete

# Install Icon and Menu entry
install -d %{buildroot}%{_datadir}/icons
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}


%files -f %{name}.lang
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog FAQ NEWS README THANKS TODO
%{_bindir}/centerim
%{_bindir}/cimconv
%{_bindir}/cimformathistory
%{_bindir}/cimextracthistory.pl
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*.svg
%{_mandir}/man1/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1:4.22.10-46
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Florian Weimer <fweimer@redhat.com> - 1:4.22.10-42
- Update centerim-c99.patch with -Wreturn-mismatch fix (#2149217)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Florian Weimer <fweimer@redhat.com> - 1:4.22.10-39
- Improve compatibility with C99 compilers (#2149217)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:4.22.10-36
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 1:4.22.10-33
- Force C++14 as the code is not ready for C++17

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Lubomir Rintel <lkundrak@v3.sk> - 1:4.22.10-29
- Fix build
- Remove CenterIMLog2HTML.py

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:4.22.10-26
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1:4.22.10-21
- Rebuild for gpgme 1.18

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:4.22.10-18
- Build with OpenSSL now that NSS is retired

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:4.22.10-17
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1:4.22.10-14
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:4.22.10-12
- Perl 5.18 rebuild

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 4.22.10-11
- Patch to fix a problem tripping up debugedit

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1:4.22.10-10
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1:4.22.10-8
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1:4.22.10-7
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.10-5
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 01 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1:4.22.10-3
- fix ftbfs (rhbz#715642)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Lubomir Rintel <lkundrak@v3.sk> - 1:4.22.10-1
- New release, fixing CVE-2009-3720
- Drop upstreamed nss patch

* Thu Feb 18 2010 Lubomir Rintel <lkundrak@v3.sk> - 1:4.22.9-1
- Fix build
- New upstream release

* Mon Sep 07 2009 Lubomir Rintel <lkundrak@v3.sk> - 1:4.22.8-1
- New upstream release
- Our NSS patch integrated

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 Lubomir Rintel <lkundrak@v3.sk> - 1:4.22.7-1
- New upstream version
- Re-enable SSL, provided by NSS

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.22.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 09 2009 Lubomir Rintel <lkundrak@v3.sk> - 1:4.22.6-1
- New upstream release
- Disable openssl due to licensing trouble
- Fix dependencies

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1:4.22.6-0.2.20080705git
- Rebuild for Python 2.6

* Sat Jul 05 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.6-0.1.20080705git
- Update to mobshot to exclude files with problematic copyright

* Mon Apr 14 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.5-1
- 4.22.5 with fixes for various Yahoo protocol crashes

* Sun Mar 30 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.4-1
- 4.22.4 with Yahoo protocol fixes

* Tue Mar 25 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.3-2
- Escape URLs before opening with a browser (CVE-2008-1467) (#438871)
- Cherry-pick a couple of Yahoo IM fixes

* Tue Mar 11 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.3-1
- New upstream release

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:4.22.2-4
- Autorebuild for GCC 4.3

* Mon Jan 07 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.2-3
- Icon and menu entry

* Fri Dec 14 2007 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.2-2
- Replace centericq

* Sat Dec 08 2007 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.2-1
- New upstream release

* Wed Nov 28 2007 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.1.20071124-2
- Synchronized with GIT to fix the ICQ client side contacts problems (#402301)

* Thu Oct 25 2007 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.1.20071022-1
- New upstream tarball, functionally equivalent to previous revision of the pkg

* Tue Oct 23 2007 Lubomir Kundrak <lkundrak@redhat.com> - 1:4.22.1.20071003-4
- lkundrak's dumb, dumb, dumb and he .... up the versioning, bumping epoch
- Merging the upstream git snapshot:
- Our fixes upstreamed
- Fix for MSN NOT messages handling
- Fixed french translation

* Mon Oct 08 2007 Lubomir Kundrak <lkundrak@redhat.com> - 20071003-2
- Fixed BuildRoot
- Removed redundant BuildReq
- Rebased to more current upstream tarball

* Tue Oct 02 2007 Lubomir Kundrak <lkundrak@redhat.com> - 20070625-1
- fork centerim from centericq

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 4.21.0-14
- new license tag
- rebuild for ppc32 (devel)

* Thu Jul 19 2007 Lubomir Kundrak <lkundrak@redhat.com>
- fix CVE-2007-3713 multiple buffer overflows (#247979)

* Sun Jun 03 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- fix #242344

* Sun Apr 01 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.21.0-12
- fix #233808 (503 jabber disco)
- fix #233901 (no sound/no translation)

* Sat Feb 10 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.21.0-11
- fix CVE-2007-160 (#227791)

* Mon Jan 08 2007 Kevin Fenzi <kevin@tummy.com>
4.21.0-10
- Tweak to build on fc7 and rebuild for new curl

* Mon Nov 06 2006 Jindrich Novy <jnovy@redhat.com>
- rebuild because of the new curl

* Tue Sep 12 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.21.0-8
- FE6 rebuild

* Thu Mar 02 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.21.0-7
- fix #183623: ask before quit
- fix #183625, #183626: fixes lj hook

* Wed Mar 01 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.21.0-6
- improve utf8 support

* Tue Feb 14 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.21.0-5
- Rebuild for Fedora Extras 5

* Tue Jan 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.21.0-4
- Fix more security related stuff
- Fix libmsn

* Thu Nov 10 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.21.0-2
- rebuild

* Tue Sep 27 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.21.0-1
- version upgrade (#168425)

* Mon May 30 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.20.0-10
- cleanup the x86_64 build fixes...

* Sun May 29 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.20.0-9
- hopefully the last x86_64 build fixes...

* Sun May 29 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.20.0-8
- and again more size_t fixes in src

* Sun May 29 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.20.0-7
- even more size_t build fixes in kkstrtext

* Thu May 26 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.20.0-6
- renew -5 buildfix and drop ifarch
- add another x86_64 buildfix

* Thu May 26 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.20.0-5
- x86_64 buildfix

* Mon May 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.20.0-4
- enable jabber encryption support via gpgme
- fix build (#156202)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 4.20.0-3
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Feb 08 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.20.0-1
- version upgrade
- remove libicq2000 exclude (not needed anymore)
- fixed BuildRequires

* Tue Dec 21 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
4.13.0-1
- version upgrade
- exclude libicq2000 headers (may conflict with libicq2000-devel)
- drop GCC 3.4 patch (not needed anymore)

* Fri Nov 12 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 4.9.4-3
- Fix C++ code for FC3/GCC 3.4.

* Sun Jul 13 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de>
0:4.9.4-0.fdr.2
- Fixed issues mentioned in #446 by Michael Schwendt
* Thu Jul 03 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de>
0:4.9.4-0.fdr.1
- Initial RPM release.
