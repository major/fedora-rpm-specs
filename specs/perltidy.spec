Name:		perltidy
Version:	20250711
Release:	2%{?dist}
Summary:	Tool for indenting and re-formatting Perl scripts
License:	GPL-2.0-or-later
URL:		http://perltidy.sourceforge.net/
Source0:	https://cpan.metacpan.org/modules/by-module/Perl/Perl-Tidy-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Encode)
BuildRequires:	perl(English)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Pod::Html)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(utf8)
# Dependencies
Requires:	perl(File::Spec)
Requires:	perl(File::Temp)
Requires:	perl(HTML::Entities)
Requires:	perl(Pod::Html)
Provides:	perl-Perl-Tidy = %{version}-%{release}

%description
Perltidy is a Perl script that indents and re-formats Perl scripts to
make them easier to read. If you write Perl scripts, or spend much
time reading them, you will probably find it useful. The formatting
can be controlled with command line parameters. The default parameter
settings approximately follow the suggestions in the Perl Style Guide.
Perltidy can also output HTML of both POD and source code. Besides
re-formatting scripts, Perltidy can be a great help in tracking down
errors with missing or extra braces, parentheses, and square brackets
because it is very good at localizing errors.

%prep
%setup -q -n Perl-Tidy-%{version}

# Don't need Windows batch file
rm examples/pt.bat

# Quieten complaints about missing files
sed -i -e '/^examples\/pt\.bat/d' MANIFEST

# Remove unwanted exec permissions
find examples/ lib/ -type f -perm /a+x -exec chmod -c -x {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc BUGS.md CHANGES.md README.md docs/ examples/
%{_bindir}/perltidy
%{perl_vendorlib}/Perl/
%{_mandir}/man1/perltidy.1*
%{_mandir}/man3/Perl::Tidy.3*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20250711-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 14 2025 Paul Howarth <paul@city-fan.org> - 20250711-1
- Update to 20250711 (see CHANGES.md for details)

* Mon Jun 16 2025 Paul Howarth <paul@city-fan.org> - 20250616-1
- Update to 20250616 (see CHANGES.md for details)
- Use %%{make_build} and %%{make_install}

* Wed Mar 12 2025 Paul Howarth <paul@city-fan.org> - 20250311-1
- Update to 20250311 (see CHANGES.md for details) (rhbz#2351446)

* Thu Feb 13 2025 Paul Howarth <paul@city-fan.org> - 20250214-1
- Update to 20250214 (see CHANGES.md for details) (rhbz#2345575)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20250105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan  5 2025 Paul Howarth <paul@city-fan.org> - 20250105-1
- Update to 20250105 (see CHANGES.md for details) (rhbz#2335628)

* Tue Sep  3 2024 Paul Howarth <paul@city-fan.org> - 20240903-1
- Update to 20240903 (see CHANGES.md for details) (rhbz#2309446)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240511-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun May 12 2024 Paul Howarth <paul@city-fan.org> - 20240511-1
- Update to 20240511 (see CHANGES.md for details)

* Thu Feb  1 2024 Paul Howarth <paul@city-fan.org> - 20240202-1
- Update to 20240202 (see CHANGES.md for details) (rhbz#2262294)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230912-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230912-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 13 2023 Paul Howarth <paul@city-fan.org> - 20230912-1
- Update to 20230912 (rhbz#2238633)
  - Remove a syntax error check that could cause an incorrect error message
    when List::Gather::gather was used (GH#124)

* Sat Sep  9 2023 Paul Howarth <paul@city-fan.org> - 20230909-1
- Update to 20230909 (see CHANGES.md for details) (rhbz#2238025)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230701-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul  1 2023 Paul Howarth <paul@city-fan.org> - 20230701-1
- Update to 20230701 (see CHANGES.md for details) (rhbz#2219054)

* Thu Mar  9 2023 Paul Howarth <paul@city-fan.org> - 20230309-1
- Update to 20230309 (see CHANGES.md for details) (rhbz#2176557)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20221112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 11 2022 Paul Howarth <paul@city-fan.org> - 20221112-1
- Update to 20221112 (rhbz#2142076)
  - Fix undef warning in Perl before 5.12 (CPAN RT#145095)

* Thu Nov 10 2022 Paul Howarth <paul@city-fan.org> - 20221111-1
- Update to 20221111 (see CHANGES.md for details) (rhbz#2141765)
- Use SPDX-format license tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220613-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Paul Howarth <paul@city-fan.org> - 20220613-1
- Update to 20220613 (see CHANGES.md for details)

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 20220217-2
- Perl 5.36 rebuild

* Tue Feb 15 2022 Paul Howarth <paul@city-fan.org> - 20220217-1
- Update to 20220217 (see CHANGES.md for details)

* Tue Feb 15 2022 Paul Howarth <paul@city-fan.org> - 20220215-1
- Update to 20220215 (see CHANGES.md for details)
- Add workaround for bogus dependencies generated on EL-7

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 29 2021 Paul Howarth <paul@city-fan.org> - 20211029-1
- Update to 20211029 (see CHANGES.md for details)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210717-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Paul Howarth <paul@city-fan.org> - 20210717-1
- Update to 20210717 (see CHANGES.md for details)

* Thu Jun 24 2021 Paul Howarth <paul@city-fan.org> - 20210625-1
- Update to 20210625 (see CHANGES.md for details)

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 20210402-2
- Perl 5.34 rebuild

* Thu Apr  1 2021 Paul Howarth <paul@city-fan.org> - 20210402-1
- Update to 20210402 (see CHANGES.md for details)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Paul Howarth <paul@city-fan.org> - 20210111-1
- Update to 20210111 (see CHANGES.md for details)
- Use %%license unconditionally

* Mon Dec  7 2020 Paul Howarth <paul@city-fan.org> - 20201207-1
- Update to 20201207 (see CHANGES.md for details)

* Thu Dec  3 2020 Paul Howarth <paul@city-fan.org> - 20201202-1
- Update to 20201202 (see CHANGES.md for details)

* Tue Sep 29 2020 Paul Howarth <paul@city-fan.org> - 20201001-1
- Update to 20201001 (see CHANGES.md for details)

* Mon Sep  7 2020 Paul Howarth <paul@city-fan.org> - 20200907-1
- Update to 20200907 (see CHANGES.md for details)

* Sat Aug 22 2020 Paul Howarth <paul@city-fan.org> - 20200822-1
- Update to 20200822 (see CHANGES.md for details)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200619-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 20200619-2
- Perl 5.32 rebuild

* Sat Jun 20 2020 Paul Howarth <paul@city-fan.org> - 20200619-1
- Update to 20200619 (see CHANGES.md for details)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Paul Howarth <paul@city-fan.org> - 20200110-1
- Update to 20200110 (see CHANGES.md for details)

* Tue Dec  3 2019 Paul Howarth <paul@city-fan.org> - 20191203-1
- Update to 20191203 (see CHANGES.md for details)

* Sun Sep 15 2019 Paul Howarth <paul@city-fan.org> - 20190915-1
- Update to 20190915 (see CHANGES.md for details)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190601-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 20190601-2
- Perl 5.30 re-rebuild updated packages

* Mon Jun  3 2019 Paul Howarth <paul@city-fan.org> - 20190601-1
- Update to 20190601 (see CHANGES.md for details)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 20181120-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Paul Howarth <paul@city-fan.org> - 20181120-1
- Update to 20181120 (see CHANGES.md for details)
- Drop UTF-8 patch, no longer needed
- Text documentation converted to markdown upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180220-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 20180220-2
- Perl 5.28 rebuild

* Wed Feb 21 2018 Paul Howarth <paul@city-fan.org> - 20180220-1
- Update to 20180220
  - Fix index error causing perltidy to fail, resulting in empty files
    (CPAN RT#124469, CPAN RT#124494)

* Mon Feb 19 2018 Paul Howarth <paul@city-fan.org> - 20180219-1
- Update to 20180219 (see CHANGES for details)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan  1 2018 Paul Howarth <paul@city-fan.org> - 20180101-1
- Update to 20180101 (see CHANGES for details)

* Fri Dec 15 2017 Paul Howarth <paul@city-fan.org> - 20171214-1
- Update to 20171214 (see CHANGES for details)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170521-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 20170521-2
- Perl 5.26 rebuild

* Mon May 22 2017 Paul Howarth <paul@city-fan.org> - 20170521-1
- Update to 20170521
  - Includes fix for CVE-2016-10374: Uses current working directory without
    symlink-attack protection
  - See CHANGES for details of other bug fixes and enhancements
- Simplify find command using -delete

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160302-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 20160302-2
- Perl 5.24 rebuild

* Tue Mar  1 2016 Paul Howarth <paul@city-fan.org> - 20160302-1
- Update to 20160302
  - Corrected a minor problem in which an unwanted newline was placed before
    the closing brace of an anonymous sub with a signature, if it was in a
    list (CPAN RT#112534)
  - Corrected a minor problem in which occasional extra indentation was given
    to the closing brace of an anonymous sub in a list when the -lp parameter
    was set

* Mon Feb 29 2016 Paul Howarth <paul@city-fan.org> - 20160301-1
- Update to 20160301 (see CHANGES for details)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150815-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 15 2015 Paul Howarth <paul@city-fan.org> - 20150815-1
- Update to 20150815 (see CHANGES for details)
- Use %%license where possible

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140711-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 20140711-3
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 20140711-2
- Perl 5.20 rebuild

* Mon Jul 14 2014 Paul Howarth <paul@city-fan.org> - 20140711-1
- Update to 20140711 (see CHANGES for details)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140328-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Paul Howarth <paul@city-fan.org> - 20140328-1
- Update to 20140328
  - Fixed CPAN RT#94190 and debian Bug #742004: perltidy.LOG file left behind;
    the problem was caused by the memoization speedup patch in version
    20121207: an unwanted flag was being set, which caused a LOG to be written
    if perltidy was called multiple times
  - New default behavior for LOG files: if the source is from an array or
    string (through a call to the perltidy module) then a LOG output is only
    possible if a logfile stream is specified; this is to prevent unexpected
    perltidy.LOG files
  - Fixed debian Bug #740670, insecure temporary file usage; File::Temp is now
    used to get a temporary file (CVE-2014-2277)
  - Any -b (--backup-and-modify-in-place) flag is silently ignored when a
    source stream, destination stream, or standard output is used; this is
    because the -b flag may have been in a .perltidyrc file and warnings break
    Test::NoWarnings
- Drop upstreamed patch for CVE-2014-2277
- Classify buildreqs by usage

* Tue Mar 25 2014 Paul Howarth <paul@city-fan.org> - 20130922-2
- Cosmetic spec changes:
  - Use tabs
  - Comment patch applications
  - Don't use macros for commands
  - Use %%{buildroot} rather than $RPM_BUILD_ROOT
- Provide perl-Perl-Tidy for benefit of people looking for CPAN module
- Use a patch rather than scripted iconv run to fix character encoding
- BR: perl(Getopt::Long)
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Wed Mar 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 20130922-1
- Update to 20130922.
- Fix for CVE-2014-2277 from Debian (#1074721) + related man page fix.
- Fix bogus date in %%changelog.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121207-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 20121207-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 20121207-1
- Update to 20121207.

* Wed Aug 15 2012 Jitka Plesnikova <jplesnik@redhat.com> - 20120714-3
- Specify all dependencies.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120714-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Ville Skyttä <ville.skytta@iki.fi> - 20120714-1
- Update to 20120714.

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 20120701-2
- Perl 5.16 rebuild

* Sat Jul  7 2012 Ville Skyttä <ville.skytta@iki.fi> - 20120701-1
- Update to 20120701.

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 20120619-2
- Perl 5.16 rebuild

* Wed Jun 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 20120619-1
- Update to 20120619.
- Clean up specfile constructs no longer needed in Fedora or EL6+.

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 20101217-5
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101217-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 20101217-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101217-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 26 2010 Ville Skyttä <ville.skytta@iki.fi> - 20101217-1
- Update to 20101217.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 20090616-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 20090616-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090616-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Ville Skyttä <ville.skytta@iki.fi> - 20090616-1
- Update to 20090616.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071205-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20071205-3
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20071205-2
- rebuild for new perl

* Thu Dec  6 2007 Ville Skyttä <ville.skytta@iki.fi> - 20071205-1
- 20071205.
- Convert docs to UTF-8.

* Wed Aug  1 2007 Ville Skyttä <ville.skytta@iki.fi> - 20070801-1
- 20070801.

* Wed May  9 2007 Ville Skyttä <ville.skytta@iki.fi> - 20070508-1
- 20070508.

* Sat May  5 2007 Ville Skyttä <ville.skytta@iki.fi> - 20070504-1
- 20070504.

* Tue Apr 24 2007 Ville Skyttä <ville.skytta@iki.fi> - 20070424-1
- 20070424.

* Tue Apr 17 2007 Ville Skyttä <ville.skytta@iki.fi> - 20060719-3
- BuildRequire perl(ExtUtils::MakeMaker).

* Fri Sep 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 20060719-2
- Rebuild.

* Thu Jul 20 2006 Ville Skyttä <ville.skytta@iki.fi> - 20060719-1
- 20060719.
- Fix order of options to find(1) in %%install.

* Thu Jun 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 20060614-1
- 20060614, specfile cleanups, include examples in docs.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Dec 16 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:20031021-1
- Sync with fedora-rpmdevtools' Perl spec template to fix x86_64 build.
- Move version to the version field.

* Wed Oct 22 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.3.20031021
- Update to 20031021.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.3.20030726
- Install into vendor dirs.
- Spec cleanups.

* Tue Jul 29 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.2.20030726
- Update to 20030726.
- Use fedora-rpm-helper.

* Mon Jun 23 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.2.20021130
- Address issues in #194:
- Patch to get rid of a warning on startup.
- Do defattr before doc.

* Fri May 30 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20021130
- Fix release naming scheme (this is snapshot-only).

* Wed May  7 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.0.2.20021130
- Own dirs.
- Save .spec in UTF-8.

* Mon Apr 21 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.0.1.20021130
- First Fedora release, based on Simon Perreault's work.

* Mon Mar 10 2003 Simon Perreault <nomis80@nomis80.org> 20021130-2
- Changed architecture from i386 to noarch
- Added my name as packager
- Bumped up release number, which was forgotten by Anthony Rumble

* Sun Mar 09 2003 Anthony Rumble <anthony@linuxhelp.com.au>
- Tidied up RPM Source

* Sun Dec  1 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20021130

* Sat Nov  9 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20021106

* Mon Sep 23 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20020922

* Wed Aug 28 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20020826

* Tue May 7 2002 Simon Perreault <nomis80@linuxquebec.com>
- Require 5.6.1 because Tidy.pm is placed in a directory dependant on perl
  version.

* Sat Apr 27 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20020425.

* Wed Apr 17 2002 Simon Perreault <nomis80@linuxquebec.com>
- Generalized spec file. Added some documentation.

* Wed Apr 17 2002 Simon Perreault <nomis80@linuxquebec.com>
- Upgraded to version 20020416

* Mon Feb 25 2002 Simon Perreault <nomis80@linuxquebec.com>
- Spec file was created on release of 20020225
