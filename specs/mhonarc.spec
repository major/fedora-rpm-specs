Name:           mhonarc
Version:        2.6.24
Release:        15%{?dist}
Summary:        Perl mail-to-HTML converter

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/MHonArc
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDIDRY/MHonArc-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(Time::Local)
Provides:       MHonArc = %{version}-%{release}

# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(.*\.pl\\)

%description
MHonArc is a Perl mail-to-HTML converter. MHonArc provides HTML mail
archiving with index, mail thread linking, etc; plus other
capabilities including support for MIME and powerful user
customization features.


%prep
%setup -q -n MHonArc-%{version}


%build
# Nothing to build


%install
%{__perl} install.me -batch -libpath %{buildroot}%{_datadir}/MHonArc \
  -nodoc -manpath %{buildroot}%{_mandir} -binpath %{buildroot}%{_bindir}
# Aww, remainders of buildroot and /usr/local, weed 'em out.
%{__perl} -pi -e \
  "s|%{buildroot}\b||g ; s|/usr/local/bin/perl\b|%{__perl}|g" \
  %{buildroot}%{_bindir}/* examples/mha*


%files
%license COPYING
%doc ACKNOWLG BUGS CHANGES RELNOTES TODO
%doc doc examples extras logo
%{_bindir}/mh*
%{_datadir}/MHonArc
%{_mandir}/man1/mh*.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.24-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.24-7
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.24-4
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Xavier Bachelot <xavier@bachelot.org> - 2.6.24-2
- Better URL: and Source0:

* Tue Dec 01 2020 Xavier Bachelot <xavier@bachelot.org> - 2.6.24-1
- Update to 2.6.24 (RHBZ#1901625)
- Specfile cleanup

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.19-19
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.19-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.19-13
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.19-12
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.6.19-9
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.19-8
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug  3 2016 José Matos <jamatos@fedoraproject.org> - 2.6.19-6
- Fix bug #1298904

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.19-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 01 2015 Petr Šabata <contyk@redhat.com> - 2.6.19-3
- Amend the latest dep list fix, adding dependencies from the FILELIST, too

* Thu Aug 27 2015 Petr Šabata <contyk@redhat.com> - 2.6.19-2
- Prevent FTBFS by correcting the build time dependency list

* Tue Jul 21 2015 José Matos <jamatos@fedoraproject.org> - 2.6.19-1
- Update to 2.6.19

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.18-16
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.18-15
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 José Matos <jamatos@fedoraproject.org> - 2.6.18-13
- add patch (based on debian patch) that:
-   removes some deprecation warning (bz 901351)
-   adds some Microsoft Office 2007 mime types
-   adds some hardening

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.6.18-11
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.6.18-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 2.6.18-6
- RPM 4.9 dependency filtering added

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.18-5
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.18-4
- Perl 5.14 mass rebuild

* Tue Mar 15 2011 José Matos <jamatos@fedoraproject.org> - 2.6.18-3
- Fix requires filter.

* Sat Mar 12 2011 José Matos <jamatos@fedoraproject.org> - 2.6.18-2
- Take back the unwanted dependencies filter with new clothes.

* Sat Mar 12 2011 José Matos <jamatos@fedoraproject.org> - 2.6.18-1
- Thanks to Jeff Schroeder for the ideas to fix the spec file (bz 664730)
- New upstream release
- Fixes CVE-2010-1677 and CVE-2010-4524 (bz 664730)
- Use %%{version} in Source
- Simplify the filter usage for perl requirements

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 09 2009 Aurelien Bompard <abompard@fedoraproject.org> 2.6.16-6
- filter out unwanted Requires (provided by MHonArc itself)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.6.16-4
- fix license tag

* Sat Nov 18 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.6.16-3
- rebuild, perl-Unicode-Map8 now builds on x86_64

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.6.16-2
- rebuild

* Thu Jun 15 2006 Aurelien Bompard <gauret[AT]free.fr> 2.6.16-1
- version 2.6.16

* Thu Feb 23 2006 Aurelien Bompard <gauret[AT]free.fr> 2.6.15-4
- excludearch x86_64

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 2.6.15-3
- rebuild for FC5

* Wed Jul 27 2005 Aurelien Bompard <gauret[AT]free.fr> 2.6.15-2
- rebuild

* Wed Jul 27 2005 Aurelien Bompard <gauret[AT]free.fr> 2.6.15-1
- version 2.6.15

* Sat Jul 23 2005 Aurelien Bompard <gauret[AT]free.fr> 2.6.14-1
- version 2.6.14

* Sat Jun 11 2005 Aurelien Bompard <gauret[AT]free.fr> 2.6.12-1
- version 2.6.12

* Mon May 23 2005 Aurelien Bompard <gauret[AT]free.fr> 2.6.11-1%{?dist}
- version 2.6.11
- use dist tag

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon May 17 2004 Aurelien Bompard <gauret[AT]free.fr> 0:2.6.10-0.fdr.1
- version 2.6.10 (bugfix for old perl)

* Sat May 08 2004 Aurelien Bompard <gauret[AT]free.fr> 0:2.6.9-0.fdr.1
- version 2.6.9

* Sat Dec  6 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.8-0.fdr.2
- Fix $RPM_BUILD_ROOT replacing (bug 39).

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.8-0.fdr.1
- Update to 2.6.8.

* Fri Aug  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.7-0.fdr.1
- Update to 2.6.7.

* Wed Jul 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.6-0.fdr.1
- Update to 2.6.6.

* Sun Jul  6 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.4-0.fdr.1
- Update to 2.6.4.

* Wed May  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.3-0.fdr.2
- %%{buildroot} -> $RPM_BUILD_ROOT.
- s/MHonArc/mhonarc/

* Tue Apr  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.3-0.fdr.1
- Update to 2.6.3.
- Save .spec in UTF-8.

* Fri Mar 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.2-0.fdr.1
- Update to 2.6.2, and to current Fedora guidelines.

* Sun Mar  2 2003 Ville Skyttä <ville.skytta at iki.fi> - 2.6.1-1.fedora.1
- First Fedora release, based on work of Mandrake folks.
- Moved stuff from %%{_libdir} to %%{_datadir}.

* Mon Feb 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.6.1-1mdk
- 2.6.1

* Mon Feb 10 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.6.0-1mdk
- 2.6.0

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.5.14-2mdk
- rebuild

* Sun Jan 26 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.5.14-1mdk
- security release
- misc spec file fixes

* Tue Oct 22 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.5.13-1mdk
- 2.5.13

* Tue Jul 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.5.10-1mdk
- 2.5.10

* Mon Jul 22 2002  Lenny Cartier <lenny@mandrakesoft.com> 2.5.9-1mdk
- 2.5.9

* Fri Jul 12 2002 Pixel <pixel@mandrakesoft.com> 2.5.7-2mdk
- remove "AutoReqProv: no" (it doesn't change anything)
- rebuild for new perl 5.8.0

* Mon Jun 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.5.7-1mdk
- 2.5.7

* Tue Jun 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.5.6-1mdk
- 2.5.6

* Tue May 28 2002 Christian Belisle <cbelisle@mandrakesoft.com> 2.5.5-1mdk
- 2.5.5
- quiet the %%setup

* Tue Apr 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.5.3-1mdk
- 2.5.3

* Wed Jun 20 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.4.9-1mdk
- License
- updated to 2.4.9

* Sat Apr 14 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.4.8-1mdk
- Build a 2.4.8.

* Tue Jan 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.4.7-2mdk
- clean spec

* Fri Nov 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.4.7-1mdk
- shamelessly ripped from RedHat contribs.

* Fri Feb 18 2000 Yuri Detzel <yad@mail.ru>
- Updated to version 2.4.5
- Fixed rewriting and deleting files in lib directory
  during building of RPM package
- Updated to new url of MHonArc home page

* Wed Aug 18 1999 Chuck Mead <csm@lunar-penguin.com>
- Updated to version 2.4.3

* Sat Jun 26 1999 Jeff Breidenbach <jeff@alum.mit.edu>
- Updated to version 2.4.0

* Wed Nov 18 1998 Jeff Breidenbach <jeff@alum.mit.edu>
- Added utilities to RPM (mha-dbedit, mha-dbrecover)

* Wed Nov 11 1998 Jeff Breidenbach <jeff@alum.mit.edu>
- Removed "BuildRoot:" to fix path problem.

* Mon Nov 9 1998 Jeff Breidenbach <jeff@alum.mit.edu>
- updated to version 2.3.3
- updated Perl requirement to perl 5.
- Removed RPM patch; used install.me command line options instead

* Tue Oct 27 1998 Jeff Breidenbach <jeff@alum.mit.edu>
- updated to version 2.3.1

* Wed Apr 1 1998 Stig HackVän <stig@hackvan.com>
- removed bogus "%%dep" macro from %%install script
- removed bogus %%doc tags from the /usr/{bin,lib} files
- moved to noarch architecture

* Wed Mar 3 1998 Jeff Breidenbach <jeff@jab.org>
- built new version under RedHat Hurricane w/ glibc

* Wed Nov 19 1997 Greg Boehnlein <damin@nacs.net>
- rebuilt under RedHat Mustang w/ glibc

* Sat Nov 08 1997 Andrew Pimlott <pimlott@math.harvard.edu>
- started from a contrib'ed RPM for version 1.2.3.  There was no
  identification of the original packager.
- lots of clean-up
- BuiltRoot'ed
