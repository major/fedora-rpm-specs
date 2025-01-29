Summary: An ircII chat client
Name: epic
Version: 3.0
Release: 3%{?dist}
Epoch: 4
License: BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain
Source0: ftp://ftp.epicsol.org/pub/epic/EPIC4-PRODUCTION/epic4-%{version}.tar.xz
Source1: ftp://ftp.epicsol.org/pub/epic/EPIC4-PRODUCTION/epic4-help-current.tar.bz2
Source2: epic.wmconfig
Source3: ircII.servers
Source4: http://prdownloads.sourceforge.net/splitfire/sf-1.35.irc.gz
Source5: http://splitfire.sourceforge.net/schemes/sf-bitchx-scheme.irc.gz
Source6: http://splitfire.sourceforge.net/schemes/sf-eggsandham-scheme.irc.gz
Source7: http://splitfire.sourceforge.net/schemes/sf-light-scheme.irc.gz
Source8: http://splitfire.sourceforge.net/schemes/sf-perry-scheme.irc.gz
Patch0: epic-default.patch
Patch1: epic-fix-ftbfs.patch
URL: http://www.epicsol.org/
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: ncurses-devel
BuildRequires: make automake autoconf

%description
EPIC (Enhanced Programmable ircII Client) is an advanced ircII chat
client.  Chat clients connect to servers around the world, enabling
you to chat with other people.

%prep 
rm -rf $RPM_BUILD_DIR/ircii-EPIC%{prog_version}

%setup -q -n epic4-%{version} -a 1
%autopatch -p0

%build
export CFLAGS="$RPM_OPT_FLAGS -std=gnu17"
autoreconf -vi
%configure

rm -rf help/Makefile help/README_FIRST
find help -type d -name CVS | while read line; do rm -rf $line; done;

make

%install
rm -rf $RPM_BUILD_ROOT

# see INSTALL, -O2 is not usable for epic
export RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed s/-O2/-O/`

make install CFLAGS="$RPM_OPT_FLAGS" installhelp IP=$RPM_BUILD_ROOT prefix=%{_prefix} mandir=%{_mandir} 

rm $RPM_BUILD_ROOT/usr/bin/epic
ln -s epic-EPIC4-%{version} $RPM_BUILD_ROOT/usr/bin/epic 

for file in %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8}; do
	sNAME=`echo $file | sed -e 's/\.gz$//'`;
	bNAME=`basename $sNAME`;
	zcat $file | sed -e 's/^\(\^set HELP_PATH.*\)/#\1/' > $bNAME;
	install $bNAME $RPM_BUILD_ROOT/usr/share/epic/script/
done;

install %{SOURCE3} $RPM_BUILD_ROOT/usr/share/epic/

# remove the CVS dir in the doc dir
rm -rf doc/CVS

# wserv is just not very useful
rm -f $RPM_BUILD_ROOT/%{_libexecdir}/wserv

%files
%doc BUG_FORM INSTALL KNOWNBUGS README UPDATES
%doc doc/*
%license COPYRIGHT
%{_bindir}/*
%{_libexecdir}/*
%dir %{_datadir}/epic
%config(noreplace) %{_datadir}/epic/ircII.servers
%dir %attr(755,root,root) %{_datadir}/epic/script
%attr(644,root,root) %{_datadir}/epic/script/*
%{_mandir}/*/*
%dir %{_datadir}/epic/help
%{_datadir}/epic/help/*

%changelog
* Mon Jan 27 2025 Vitezslav Crhonek <vcrhonek@redhat.com> - 4:3.0-3
- Fix FTBFS

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4:3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 06 2024 Vitezslav Crhonek <vcrhonek@redhat.com> - 4:3.0-1
- Update to epic4-3.0
  Resolves: #2310116, #2300643

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 05 2024 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.10.11-1
- Update to epic4-2.10.11
  Resolves: #2272436

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 4:2.10.10-8
- SPDX migration
- Add %%license, add README to %%doc

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Peter Fordham <peter.fordham@gmail.com> - 4:2.10.10-6
- Port configure.in to C99, add autoreconf step to build and add a few missing includes.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4:2.10.10-3
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.10.10-1
- Update to epic4-2.10.10
  Resolves: #1943167

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.10.9-1
- Update to epic4-2.10.9
  Resolves: #1870717

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.10.8-2
- Remove changes made in epic4-2.10.8 that broke the package
  Resolves: #1836642

* Thu Feb 06 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.10.8-1
- Update to epic4-2.10.8
  Resolves: #1798155

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Vitezslav Crhonek <vcrhonek@redhat.com> - 4:2.10.7-1
- Update to epic4-2.10.7
  Resolves: #1694123

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 4:2.10.6-10
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Vitezslav Crhonek <vcrhonek@redhat.com> - 4:2.10.6-8
- Add BuildRequires gcc
- Remove Group and Buildroot tags

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 4:2.10.6-6
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4:2.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.10.6-1
- Update to epic4-2.10.6
  Resolves: #1303368

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.10.5-1
- Update to epic4-2.10.5

* Wed Feb 12 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.10.4-1
- Update to epic4-2.10.4

* Mon Feb 03 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.10.3-1
- Update to epic4-2.10.3
  Resolves: #1055262
- Fix wrong dates in %%changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 4:2.10.2-1
- Update to epic4-2.10.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr  1 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 4:2.10.1-1
- Update to epic4-2.10.1

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4:2.10-6
- rebuilt with new openssl

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 4:2.10-5
- Use bzipped upstream help tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 4:2.10-2
- rebuild with new openssl

* Tue Nov 25 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 4:2.10-1
- Update to upstream epic4-2.10

* Mon Feb 11 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 4:2.6-4
- Fix Buildroot

* Wed Dec  5 2007 Vitezslav Crhonek <vcrhonek@redhat.com> 4:2.6-3
- Rebuild

* Thu Aug 23 2007 Vitezslav Crhonek <vcrhonek@redhat.com> 4:2.6-2
- fix license
- rebuild

* Wed Jan 10 2007 Peter Vrabec <pvrabec@redhat.com> 4:2.6-1
- upgrade

* Mon Jul 31 2006 Peter Vrabec <pvrabec@redhat.com> 4:2.4-5
- upgrade to new bugfix release

* Mon Jul 31 2006 Peter Vrabec <pvrabec@redhat.com> 4:2.2-5
- add buildrequires ncurses-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4:2.2-4.1
- rebuild

* Wed May 17 2006 Karsten Hopp <karsten@redhat.de> 2.2-4
- add buildrequires openssl-devel

* Tue Feb 21 2006 Peter Vrabec <pvrabec@redhat.com> 4:2.2-3
- fix fuzz test fail (#181036)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4:2.2-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4:2.2-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Dec 06 2005 Jesse Keating <jkeating@redhat.com> 4:2.2-2
- Removed outdated patches
- Added libexec dir for files

* Tue Dec 06 2005 Jesse Keating <jkeating@redhat.com> 4:2.2-1
- rebuild

* Thu Mar 17 2005 Peter Vrabec <pvrabec@redhat.com> 4:1.0.1-20
- rebuild

* Tue Feb 08 2005 Peter Vrabec <pvrabec@redhat.com>
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Nov 11 2003 Jeremy Katz <katzj@redhat.com> 4:1.0.1-16
- add patch for buffer overflow (CAN-2003-0328) from 
  ftp://ftp.prbh.org/pub/epic/patches/alloca_underrun-patch-1

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeremy Katz <katzj@redhat.com> 4:1.0.1-14
- generated files to generate files.  fix gcc 3.3 build for real

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 4:1.0.1-13
- fix build with gcc 3.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 25 2002 Tim Powers <timp@redhat.com> 4:1.0.1-11
- fix references to %%install in the changelog so that it will build

* Sun Dec  1 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-10
- own %%{_datadir}/epic/help (#74031)

* Tue Oct 29 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-9
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.0.1-8
- automated rebuild

* Mon Jun  3 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-7
- include more of the docs
- patch the default global to enable 8-bit chars by default (#65033)

* Thu May 23 2002 Tim Powers <timp@redhat.com> 1.0.1-6
- automated rebuild

* Fri May 10 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-5
- rebuild in new environment

* Wed Feb 27 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-4
- rebuild
- desktop entries for console apps are silly, kill it

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 1.0.1-3 
- automated rebuild

* Wed Jan  2 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-2
- rebuild in new environment
- fix desktop file

* Tue Oct 30 2001 Crutcher Dunnavant <crutcher@redhat.com> 1.0.1-1
- iterate to newest version

* Thu Feb 15 2001 Tim Powers <timp@redhat.com>
- no longer conflicts with ircii

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jun 6 2000 Tim Powers <timp@redhat.com>
- fix man page location
- use %%configure and %%makeinstall
- use predefined RPM macros wherever possible
- use applnk instead of wmconfig
- include the stuff in %%{_libexecdir}

* Tue May 9 2000 Tim Powers <timp@redhat.com>
- built for 7.0

* Sun Jan  9 2000 Matt Wilson <msw@redhat.com>
- updated to epic4-2000
- updated to splitfire v1.30a

* Tue Nov 9 1999 Tim Powers <timp@redhat.com>
- updated to 4pre2.003 , two of the patches no longer needed, so they're
	dropped
- patched so that epic no longer looks for help files in /usr/lib/irc, instead
	looks in the correct place, /usr/share/epic/help
	
* Tue Jul 13 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Tue Apr 13 1999 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Oct 22 1998 <msw@redhat.com>
- Copy the splitfire script into the right directory
- Fixed diretory attributes.

* Wed Oct 21 1998 <msw@redhat.com>
- Rebuilt, moved help into main package.

* Tue Aug 18 1998 Manoj Kasichainula <manojk+rpm@io.com>
- Updated prog and help to 4pre2
- renamed to epic, since the web page doesn't call it ircii-epic.
- Use 'defattr' macro
- Changed server list, since current one seems out of date
- Other minor changes

* Sun May 17 1998 Manoj Kasichainula <manojk+rpm@io.com>
- Added help package (though a bit out of date)
- Uses bz2 file (needs bzip2 now)
- Minor spec file changes

* Sat May  9 1998 Anders Andersson <anders@sanyusan.se>
- Upgraded to pre1.200

* Tue Apr 28 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Upgraded to pre1.100
- Build for RH5
- Complex changes of %%install

* Sat Mar 28 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Upgraded to pre1.049

* Sat Mar 21 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Initial release (pre1.047)
- Small patch to disable loading local-script in global file
