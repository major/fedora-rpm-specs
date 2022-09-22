# Workaround for GCC 10
# * https://gcc.gnu.org/gcc-10/porting_to.html#common
%define _legacy_common_support 1

Name:           dillo
Version:        3.0.5
Release:        16%{?dist}
Summary:        Very small and fast GUI web browser

License:        GPLv3+
URL:            https://www.dillo.org
Source0:        %{url}/download/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-openssl.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel >= 1.3.0
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libjpeg-devel = 6b
BuildRequires:  libpng-devel >= 1.2.0
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  zlib-devel

Requires:       wget%{?_isa}

# #676710 dillo requires iso8859 fonts
Requires:       xorg-x11-fonts-ISO8859-1-100dpi
Requires:       xorg-x11-fonts-ISO8859-1-75dpi

Provides:       webclient

%description
Dillo is a very small and fast web browser using GTK. Currently: no frames,
https, javascript.


%prep
%setup -q
%patch0 -p1 -b.dso
autoreconf -vif

%build
%configure --disable-dependency-tracking --enable-ipv6 --enable-ssl
%make_build


%install
%make_install
rm -f doc/Makefile*

%{__install} -d -m 0755 %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%{__install} -Dp -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# included with doc
rm -fr %{buildroot}%{_datadir}/doc/%{name}

# silence rpmlint and convert to utf8
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog
pushd doc
iconv -f iso8859-1 -t utf-8 Cache.txt > Cache.txt.conv && mv -f Cache.txt.conv Cache.txt
iconv -f iso8859-1 -t utf-8 Cookies.txt > Cookies.txt.conv && mv -f Cookies.txt.conv Cookies.txt
popd


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING
%doc AUTHORS README ChangeLog doc/
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/%{name}*
%{_bindir}/dpid
%{_bindir}/dpidc
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_libdir}/%{name}/
%{_mandir}/man1/*.1.*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 08 2022 Leigh Scott <leigh123linux@gmail.com> - 3.0.5-15
- Remove unused gtk+-devel, dillo was ported to FLTK2 in 2008

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.0.5-13
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jan 29 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.5-11
- build: remove manual LTO flags and fix epel7 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.5-8
- Fix/workaround FTBFS | RHBZ#1799282
- Packaging improvements

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Ranjan Maitra <aarem@fedoraproject.org>
- 3.0.5-2
- patched for dillo to use openssl 1.1 using patch provided  by Mattias Ellert <mattias.ellert AT physics DOT uu DOT se> 
- fixes BZ #1470354

* Fri Feb 17 2017 Ranjan Maitra <aarem@fedoraproject.org>
- 3.0.5-1
- version upgrade (BZ #1238891)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.0.4.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 3.0.4.1-2
- rebuild (fltk)

* Mon Dec 29 2014 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 3.0.4.1-1
- version upgrade (rhbz#1177439)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.4-1
- version upgrade (rhbz#1087222)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.0.3-2
- Perl 5.18 rebuild

* Thu May 30 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.3-1
- version upgrade

* Fri Feb 22 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.2-7
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.0.2-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.0.2-4
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.2-1
- version upgrade

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.0.1-2
- Rebuild for new libpng

* Sun Sep 25 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.1-1
- new upstream release

* Thu Sep 08 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.0-1
- upgrade to release

* Thu Sep 01 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.0-0.2.20110901
- current snapshot

* Thu Aug 04 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.0-0.1.20110804
- pull hg snapshot of dillo 3
- license change to GPLv3+
- build against latest fltk (rhbz#545273)
- fixes crash described in (rhbz#676710)

* Sun Feb 13 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.8.6-14
- require iso8859 fonts (#676710)
- clean up desktop files

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 15 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.8.6-13
- fix desktop entries (#487771)

* Sun Apr 11 2010 Bruno Wolff III <bruno@wolff.to> - 0.8.6-12
- Fix DSO linking bug 564723
- Cleanup i18n area before trying to mv source there

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.8.6-11
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 0.8.6-8
- rebuild with new openssl

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0.8.6-7
- Rebuilt for gcc43

* Thu Dec 06 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.8.6-6
- fix desktop file(s) #413111

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.8.6-5
 - Rebuild for deps

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.6-4
- new license tag
- rebuild for buildid

* Tue Sep 12 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.6-3
- FE6 rebuild

* Tue Jul 04 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.6-2
- fix some more aspects of #187691 (package now contains dillo and dillo-i18n)
- fix #197370

* Sun Jun 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.6-1
- version upgrade
- fix #187691

* Mon Apr 17 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.5-3
- enable some options

* Wed Apr 05 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.5-2
- add i18n patch (#147381)

* Sat Mar 04 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.5-1
- reenable build
- version upgrade
- add dist

* Thu Apr 07 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Feb  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.4-2
- Add icon, thanks to Robin Humble.

* Tue Jan 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.4-1
- Update to 0.8.4, fixes CAN-2005-0012 (#144953).

* Tue Sep  7 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.2-0.fdr.1
- Update to 0.8.2.
- Disable dependency tracking to speed up the build.

* Sun Jun 20 2004 Nils O. Selåsdal <NOS@Utel.no> - 0:0.8.1-0.fdr.1
- 0.8.1 release

* Mon Apr 19 2004 Nils O. Selåsdal <NOS@Utel.no> - 0:0.8.0-0.fdr.3
- Require wget for https support.

* Thu Feb 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.0-0.fdr.2
- Use "make install DESTDIR" instead of the %%makeinstall macro to avoid
  buildroot traces in installed files.
- Fix files list so that debuginfo files are not included in main package.
- Desktop entry improvements, split into external file.
- Include more docs.
- Convert spec file to UTF-8.

* Tue Feb 10 2004 Nils O. Selåsdal <NOS@Utel.no> - 0:0.8.0-0.fdr.1
- 0.8.0 release
- Add patch to silence debug messages

* Mon Aug 25 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.7.3-0.fdr.2
- Include ChangeLog in docs.
- Use X-Fedora , not X-Red-Hat-Extra.
- Add proper BuildRequires,remove Requires, since they're automatically
  picked up.
- use config(noreplace) for dillorc.
- add Provides webclient.

* Sat Aug 23 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.7.3-0.fdr.1
- Initial RPM release for fedora
