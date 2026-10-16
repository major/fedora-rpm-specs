Name:           perl-SVK
Version:        2.2.3
Release:        48%{?dist}
Summary:        A Distributed Version Control System
# ARTISTIC:             Artistic-1.0-Perl text
# bin/svk:              GPL-2.0-only OR Artistic-1.0-Perl
# COPYING:              GPL-2.0 text
# lib/SVK/Accessor.pm:  GPL-2.0-only OR Artistic-1.0-Perl
## Not in any binary package
# inc/Module/Install/Metadata.pm:   GPL-1.0-or-later OR Artistic-1.0-Perl
## Not used and not in any binary package
# contrib/update-copyright.pl:      GPL-1.0-or-later OR Artistic-1.0-Perl
# utils/vc-svk.el:      GPL-2.0-or-later
License:        GPL-2.0-only
SourceLicense:  %{license} AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later
URL:            https://metacpan.org/release/SVK
Source0:        https://cpan.metacpan.org/modules/by-authors/id/C/CL/CLKAO/SVK-v%{version}.tar.gz
# Fix subversion version check, CPAN RT#125150
Patch0:         SVK-v2.2.3-Fix-SVN-Core-version-check.patch
# Do not try to install dependencies from CPAN at build time
Patch1:         SVK-v2.2.3-Disable-installing-dependencies-from-CPAN.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(SVN::Core) >= 1.3.0
BuildRequires:  perl(version) >= 0.77
# Run-time:
# No tests are performed
#BuildRequires:  perl(Algorithm::Annotate)
#BuildRequires:  perl(Algorithm::Diff) >= 1.19
#BuildRequires:  perl(App::CLI)
#BuildRequires:  perl(App::CLI::Command)
#BuildRequires:  perl(autouse)
#BuildRequires:  perl(base)
#BuildRequires:  perl(Carp)
#BuildRequires:  perl(Class::Accessor)
#BuildRequires:  perl(Class::Accessor::Fast)
#BuildRequires:  perl(Class::Autouse) >= 1.15
#BuildRequires:  perl(Class::Data::Inheritable)
#BuildRequires:  perl(Compress::Zlib)
#BuildRequires:  perl(Config)
#BuildRequires:  perl(constant)
#BuildRequires:  perl(Cwd)
#BuildRequires:  perl(Data::Dumper)
#BuildRequires:  perl(Data::Hierarchy) >= 0.30
## Date::Format only on Win32
#BuildRequires:  perl(Digest::MD5)
#BuildRequires:  perl(Encode)
#BuildRequires:  perl(Encode::TW)
#BuildRequires:  perl(Exporter)
#BuildRequires:  perl(ExtUtils::MakeMaker)
#BuildRequires:  perl(Fcntl)
#BuildRequires:  perl(File::Compare)
#BuildRequires:  perl(File::Copy)
#BuildRequires:  perl(File::Find)
#BuildRequires:  perl(File::Glob)
#BuildRequires:  perl(File::LibMagic) >= 0.84
#BuildRequires:  perl(File::MMagic)
#BuildRequires:  perl(File::Path)
#BuildRequires:  perl(File::Spec)
#BuildRequires:  perl(File::Temp)
#BuildRequires:  perl(File::Type)
#BuildRequires:  perl(FreezeThaw)
#BuildRequires:  perl(Getopt::Long)
#BuildRequires:  perl(IO::Digest)
#BuildRequires:  perl(List::MoreUtils)
#BuildRequires:  perl(List::Util)
#BuildRequires:  perl(LWP::UserAgent)
#BuildRequires:  perl(MIME::Base64)
#BuildRequires:  perl(Path::Class) >= 0.16
#BuildRequires:  perl(PerlIO)
#BuildRequires:  perl(PerlIO::eol) >= 0.13
#BuildRequires:  perl(PerlIO::gzip)
#BuildRequires:  perl(PerlIO::scalar)
#BuildRequires:  perl(PerlIO::via)
## PerlIO::via::Bzip2 not yet packaged
#BuildRequires:  perl(PerlIO::via::dynamic) >= 0.11
#BuildRequires:  perl(PerlIO::via::symlink) >= 0.02
#BuildRequires:  perl(POSIX)
#BuildRequires:  perl(Scalar::Util)
#BuildRequires:  perl(Socket)
#BuildRequires:  perl(Storable)
#BuildRequires:  perl(SVN::Client)
#BuildRequires:  perl(SVN::Core) >= 1.3.0
#BuildRequires:  perl(SVN::Delta)
## SVN::Dump not yet packages not needed only replacing packaged SVK
#BuildRequires:  perl(SVN::Fs)
## SVN::Mirror 0.71 retired
#BuildRequires:  perl(SVN::Ra)
#BuildRequires:  perl(SVN::Repos)
#BuildRequires:  perl(SVN::Simple::Edit) >= 0.27
#BuildRequires:  perl(Sys::Hostname)
#BuildRequires:  perl(Term::ReadKey)
#BuildRequires:  perl(Test::More)
#BuildRequires:  perl(Tie::Scalar)
#BuildRequires:  perl(Time::Local)
#BuildRequires:  perl(Time::Progress)
#BuildRequires:  perl(UNIVERSAL::require)
#BuildRequires:  perl(URI)
#BuildRequires:  perl(warnings)
#BuildRequires:  perl(YAML::Syck) >= 0.60
## Optional run-time:
#BuildRequires:  perl(Locale::Maketext::Lexicon) >= 0.62
#BuildRequires:  perl(Locale::Maketext::Simple) >= 0.16
#BuildRequires:  perl(Log::Log4perl)
# Tests:
# Not performed
Requires:   perl(Algorithm::Diff) >= 1.19
Requires:   perl(Class::Autouse) >= 1.15
Requires:   perl(Cwd)
Requires:   perl(ExtUtils::MakeMaker)
Requires:   perl(File::Find)
Recommends: perl(Locale::Maketext::Lexicon) >= 0.62
Recommends: perl(Locale::Maketext::Simple) >= 0.16
Recommends: perl(Log::Log4perl)
Requires:   perl(Path::Class) >= 0.16
Requires:   perl(PerlIO::gzip)
# PerlIO::via::Bzip2 not yet packaged
Requires:   perl(PerlIO::via::dynamic) >= 0.11
Requires:   perl(PerlIO::via::symlink) >= 0.02
Requires:   perl(SVN::Core) >= 1.3.0
# SVN::Dump not yet packages not needed only replacing packaged SVK
# SVN::Mirror 0.71 retired
Requires:   perl(SVN::Simple::Edit) >= 0.27
Requires:   perl(Term::ReadKey)
Requires:   perl(Tie::Scalar)
Requires:   perl(Time::Local)
Requires:   perl(Time::Progress)
Requires:   perl(URI)
Requires:   perl(YAML::Syck) >= 0.60
Provides:   perl(SVK::Version) = %{version}

# Remove uder-specified requires
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Algorithm::Diff|Class::Autouse|Path::Class|PerlIO::via::dynamic|PerlIO::via::symlink|SVN::Core|SVN::Simple::Edit|YAML::Syck)\\)$
# Remove under-specified provides
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(SVK\\)$

%description
SVK is a decentralized version control system written in Perl. It uses
the Subversion file system but provides additional features:

    * Offline operations like check-in, log, merge.
    * Distributed branches.
    * Lightweight checkout copy management (no .svn directories).
    * Advanced merge algorithms, like star-merge and cherry picking.

For more information about the SVK project, visit http://svk.elixus.org/.

%prep
%autosetup -p1 -n SVK-v%{version}
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# The tests are a bit hosed. Revisit at some point.
#make test
# Some tests fail: <https://rt.cpan.org/Public/Bug/Display.html?id=58633>
#chmod -R u+w t

%files
%license ARTISTIC COPYING
%doc CHANGES CHANGES-1.0 COMMITTERS README
%{perl_vendorlib}/SVK
%{perl_vendorlib}/SVK.pm
%{_mandir}/man1/svk.*
%{_mandir}/man3/SVK.*
%{_mandir}/man3/SVK::*
%{_bindir}/svk

%changelog
* Thu Oct 15 2026 Petr Pisar <ppisar@redhat.com> - 2.2.3-48
- Correct a license from "GPL-1.0-or-later OR Artistic-1.0-Perl" to
  "GPL-2.0-only"

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.3-43
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-36
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-33
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-30
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-27
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-24
- Perl 5.28 rebuild

* Fri Apr 20 2018 Petr Pisar <ppisar@redhat.com> - 2.2.3-23
- Fix subversion version check (CPAN RT#125150)
- Modernize spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-20
- Perl 5.26 rebuild

* Mon May 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-19
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-17
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-14
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 2.2.3-11
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 2.2.3-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  2 2011 Tom Callaway <spot@fedoraproject.org> - 2.2.3-6
- add missing Requires: perl(ExtUtils::MakeMaker) (bz 718870)

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.2.3-5
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.2.3-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.3-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jun 23 2010 Petr Pisar <ppisar@redhat.com> - 2.2.3-1
- 2.2.3 bump
- Remove SVN::Mirror dependency because perl-SVN-Mirror has been retired
- Fix spelling in description

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.1-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.2.1-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb  5 2009 Ian Burrell <ianburrell@gmail.com> - 2.2.1-2
- require Time::Progress

* Sat Jan 17 2009 Ian Burrell <ianburrell@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.2-3
- disable tests, they're a bit hosed

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.2-2
- rebuild for new perl

* Thu Aug 16 2007 Ian Burrell <ianburrell@gmail.com> - 2.0.2-1
- Update to 2.0.2
- Fix BuildRequires

* Mon Jun 18 2007 Ian Burrell <ianburrell@gmail.com> - 2.0.1-2
- Add Compress::Zlib to BuildRequires

* Sun Jun 17 2007 Ian Burrell <ianburrell@gmail.com> - 2.0.1-1
- Update to 2.0.1
- Filter optional File::LibMagic

* Tue May 29 2007 Ian Burrell <ianburrell@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Mon Sep 11 2006 Ian Burrell <ianburrell@gmail.com> - 1.08-5
- Rebuild for FC6

* Wed Aug  9 2006 Ian Burrell <ianburrell@gmail.com> - 1.08-4
- Add Term::ReadKey and SVN::Mirror requires

* Fri Jul  7 2006 Ian Burrell <ianburrell@gmail.com> - 1.08-2
- Remove contrib scripts
- Add filter provides to filter duplicate perl(SVK)

* Wed Jul  5 2006 Ian Burrell <ianburrell@gmail.com> - 1.08-1
- Update to 1.08
- Add build requires

* Tue Jul  4 2006 Ian Burrell <ianburrell@gmail.com> - 1.07-8
- Fix source URL

* Wed Jun 28 2006 Ian Burrell <ianburrell@gmail.com> - 1.07-7
- Cleanup duplicate requires

* Wed Jun 28 2006 Ian Burrell <ianburrell@gmail.com> - 1.07-6
- Add build requires

* Wed Jun 28 2006 Ian Burrell <ianburrell@gmail.com> - 1.07-5
- Add provides SVK::Version

* Wed Jun 28 2006 Ian Burrell <ianburrell@gmail.com> - 1.07-4
- Add option deps; remove autoinstall

* Thu Mar 30 2006 Ian Burrell <ianburrell@gmail.com> 1.07-1
- Specfile autogenerated by cpanspec 1.64.
