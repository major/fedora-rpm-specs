# Perform optional tests
%bcond perl_IPC_Run_enables_optional_test %{undefined rhel}

Name:           perl-IPC-Run
Version:        20231003.0
Release:        7%{?dist}
Summary:        Perl module for interacting with child processes
# the rest:                     GPL+ or Artistic
# The Win32* modules are not part of the binary RPM package
# lib/IPC/Run/Win32Helper.pm:   GPLv2 or Artistic
# lib/IPC/Run/Win32Pump.pm:     GPLv2 or Artistic
# lib/IPC/Run/Win32IO.pm:       GPLv2 or Artistic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-Run
Source0:        https://cpan.metacpan.org/modules/by-module/IPC/IPC-Run-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# IO::Pty not needed strictly for build script
# Run-time:
# base not used on Linux
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pty) >= 1.08
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# Socket not used on Linux
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
# Text::ParseWords not used on Linux
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Win32::Process not used on Linux
# Win32API::File not used on Linux
# Tests:
# B not used on Linux
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Tty)
BuildRequires:  perl(Test::More) >= 0.47
%if %{with perl_IPC_Run_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Readonly)
%endif
# Runtime
Requires:       perl(Data::Dumper)
Requires:       perl(File::Basename)
Requires:       perl(IO::Pty) >= 1.08

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%prep
%setup -q -n IPC-Run-%{version}

# Remove Windows-only features that could add unnecessary dependencies
rm -f lib/IPC/Run/Win32*
sed -i -e '/^lib\/IPC\/Run\/Win32.*/d' MANIFEST
rm -f t/win32_*
sed -i -e '/^t\/win32_.*/d' MANIFEST

# Handle optional tests
%if !%{with perl_IPC_Run_enables_optional_test}
rm t/readonly.t
sed -i -e '/^t/readonly\.t/d' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changelog eg/ README.md
%{perl_vendorlib}/IPC/
%{_mandir}/man3/IPC::Run.3*
%{_mandir}/man3/IPC::Run::Debug.3*
%{_mandir}/man3/IPC::Run::IO.3*
%{_mandir}/man3/IPC::Run::Timer.3*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20231003.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri May 16 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 20231003.0-6
- Disable optional tests on RHEL

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20231003.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231003.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231003.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231003.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct  3 2023 Paul Howarth <paul@city-fan.org> - 20231003.0-1
- Update to 20231003.0 (rhbz#2241845)
  - On Windows, avoid hang under IPCRUNDEBUG (GH#157)
  - Refresh "cpanfile" from Makefile.PL, to allow use on Windows
  - Normalize shebangs to /usr/bin/perl (GH#163)
  - Fix or skip all tests recently seen to fail on Windows
  - Include t/result.t in releases
  - Make full_result() and result() Windows behavior match non-Windows (GH#168)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220807.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Michal Josef Špaček <mspacek@redhat.com> - 20220807.0-3
- Update license to SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220807.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug  7 2022 Paul Howarth <paul@city-fan.org> - 20220807.0-1
- Update to 20220807.0
  - If your applications rely on portability to Windows, see new documentation
    sections "argument-passing rules are program-specific" and "batch files"
    - This release fixes bugs in runs of Windows programs that use standard
      command line parsing rules
    - Runs of non-standard programs may require changes; notable non-standard
      programs include cmd.exe, cscript.exe, and Cygwin programs
  - Skip t/pty.t test on NetBSD too (GH#140)
  - Add strict/warnings
  - Follow Windows argument quoting rules (GH#142)
  - Allow win32_newlines.t to actually run (GH#146)
  - Make t/pty.t test pass on OpenBSD (GH#150)
  - Support Win32 commands having non-standard command line parsing rules
    (GH#148)
  - Support executing Win32 batch files
  - Add IPC::Run::Win32Process, for delivering non-standard command lines
  - Fix reporting of Win32::Process::Create() errors
  - On Windows, avoid hang when closing read end of pipe (GH#156)
  - Ignore known test failure on msys - t/windows_search_path.t (GH#155)
  - Avoid warning with IPCRUNDEBUG, in Windows spawned children
  - Use $^X, not 'perl', in tests
  - Thanks to the new active developer: Noah Misch!

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200505.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 20200505.0-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200505.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200505.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 20200505.0-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200505.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200505.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 20200505.0-2
- Perl 5.32 rebuild

* Wed May  6 2020 Paul Howarth <paul@city-fan.org> - 20200505.0-1
- Update to 20200505.0
  - Fix syntax errors in POD examples (GH#125)
  - Switch Readonly testing requirement to a recommends (GH#127)
  - Fix full_result to always return $? (GH#129)
  - kill_kill: Immediately KILL the child process as documented for Win32 (GH#136)
  - Switch to GitHub actions for CI testing
  - Re-structure shipped files into eg/
  - Move author tests into xt/ and test them separately

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180523.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180523.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 20180523.0-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180523.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180523.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 20180523.0-2
- Perl 5.28 rebuild

* Thu May 24 2018 Paul Howarth <paul@city-fan.org> - 20180523.0-1
- Update to 20180523.0
  - Fix using fd in child process when it happens to be the same number in the
    child as it was in the parent (GH#99)
- Switch upstream from search.cpan.org to metacpan.org

* Sat Mar 31 2018 Paul Howarth <paul@city-fan.org> - 0.99-1
- Update to 0.99
  - Fixes for Windows unit tests so they skip or pass
    - t/autoflush.t
    - t/readonly.t
    - t/run_stdin-callback-return-array.t

* Fri Mar 30 2018 Paul Howarth <paul@city-fan.org> - 0.98-1
- Update to 0.98
  - Switch to using $!{EINTR}
  - Honor umask for user/group permissions on a +rw file
  - Remove commented code from CPAN RT#50739
  - Fix _write on invalid objects (GH#63)
  - Make slave the controlling terminal so more programs can be called from
    IPC::Run reliably (GH#54)
  - Prevent Not a GLOB reference in close_terminal by untieing before close
    (GH#53)
  - Fix '&' closing the stdin of the right process (GH#46)
  - Do POSIX::_exit not ::exit (GH#41)
  - Ensure child Win32 processes have same priority as parent (GH#40)
  - Add unit test for passing use of Readonly.pm (GH#38)
  - Fix GLOB test in IPC::Run::IO->new (GH#39)
  - Fix for memory leak (GH#86, CPAN RT#57990)
  - MANIFEST was updated; new tests may start shipping now

* Tue Mar 27 2018 Paul Howarth <paul@city-fan.org> - 0.97-1
- Update to 0.97
  - Update meta and POD to point to GitHub issues not RT
  - Update README with pod changes
  - Fix variable name in synopsis (GH#47)
  - Fix t/run.t to work on "perl in space" (GH#100)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.96-2
- Perl 5.26 rebuild

* Sat May 13 2017 Paul Howarth <paul@city-fan.org> - 0.96-1
- Update to 0.96
  - Update bug tracker to https://github.com/toddr/IPC-Run/issues

* Tue Apr 25 2017 Paul Howarth <paul@city-fan.org> - 0.95-1
- Update to 0.95
  - Enable Travis-CI integration for IPC::Run
  - Use q{} and qq{} to fix problems with quotation in cmd.exe
  - Sync $VERSION across all files to address kwalitee
  - Stop side effect of altering flushing of STDOUT and STDERR (CPAN RT#109243)
  - CHILD_HANDLE should be closed with 'Close' to prevent a warning
  - Require Win32API::File on Windows
  - Better timer error message plus an additional unit test
  - Catching previously non-detected malformed time strings
  - Let Timer accept all allowable perl numbers
  - Allow the OS to choose the ephemeral port to use
  - Don't use version.pm to parse the perl version in Makefile.PL
  - perltidy
  - Do not import POSIX into local namespace (it's a memory hog)
  - Skip infinity test on perl below 5.8.9
  - Spelling fixes
  - Documentation fix: full_result returns $?, not $? >> 8
  - Fix check for reaped PID in reap_nb
  - Re-remove unnecessary use of UNIVERSAL
- Remove redundant Group: tag

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.94-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.94-2
- Perl 5.22 rebuild

* Mon Dec 15 2014 Paul Howarth <paul@city-fan.org> - 0.94-1
- Update to 0.94
  - Update License discrepancies (CPAN RT#100858)
  - Many typo corrections
  - Fix t/pty.t fails on Solaris 10 (CPAN RT#20105)
- Drop upstreamed patch for CPAN RT#20105
- Use %%license

* Thu Dec 11 2014 Petr Pisar <ppisar@redhat.com> - 0.93-1
- 0.93 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.92-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May  6 2014 Paul Howarth <paul@city-fan.org> - 0.92-5
- Address intermittent test failures (CPAN RT#20105, RH BZ#1094395)
- Add runtime dependency on Data::Dumper
- Add build dependency on IO::Tty for the test suite
- Make %%files list more explicit

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.92-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Petr Šabata <contyk@redhat.com> - 0.92-1
- 0.92 bump
- Modernize the spec
- Fix dependencies
- Enable the test suite
- Drop command macros

* Thu Sep 13 2012 Petr Pisar <ppisar@redhat.com> - 0.89-9
- IO::Pty is required when passing ">pty>" argument (bug #857030)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.89-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.89-5
- Perl mass rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.89-4
- Perl mass rebuild

* Thu Jun 23 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.89-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 08 2010 Iain Arnell <iarnell@epo.org> 0.89-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.84-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.84-2
- rebuild against perl 5.10.1

* Wed Sep 02 2009 Steven Pritchard <steve@kspei.com> 0.84-1
- Update to 0.84.
- Drop IPCRUNDEBUG from "make test" (bug fixed long ago).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Steven Pritchard <steve@kspei.com> 0.82-1
- Update to 0.82.
- Use fixperms macro instead of our own chmod incantation.
- Fix Source0 URL.
- BR Test::More.
- Include LICENSE, README, and abuse/ in docs.
- Cleanup to more closely resemble cpanspec output.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.80-5
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.80-4
- rebuild for new perl

* Tue Apr 17 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.80-3
- BuildRequire perl(ExtUtils::MakeMaker).

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.80-2
- Fix order of arguments to find(1).

* Thu May 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.80-1
- 0.80, fine tune build dependencies.

* Tue Jan 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.79-3
- Rebuild, cosmetic cleanups.

* Sun Apr 10 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.79-2
- Exclude Win32 specific modules.
- Include more docs.
- Skip tests if /dev/pts doesn't exist.

* Sat Apr  2 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.79-1
- 0.79.

* Sat Apr  2 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.78-2
- Sync with fedora-rpmdevtools' Perl spec template.
- Improve dependency filtering script.

* Sun Mar 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.78-0.fdr.1
- Update to 0.78.

* Sun Feb  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.77-0.fdr.4
- Reduce directory ownership bloat.

* Fri Nov 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.77-0.fdr.3
- BuildRequire perl-IO-Tty for better test coverage.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.77-0.fdr.2
- Fix typo in dependency filtering scriptlet.

* Sat Sep 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.77-0.fdr.1
- Update to 0.77.

* Fri Sep  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.75-0.fdr.3
- Avoid Win32-specific dependencies.
- Use PERL_INSTALL_ROOT.

* Sun Aug 31 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.75-0.fdr.2
- Install into vendor dirs.

* Thu Jun 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.75-0.fdr.1
- First build.
