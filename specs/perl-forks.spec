Name:           perl-forks
Version:        0.36
Release:        33%{?dist}
Summary:        A drop-in replacement for Perl threads using fork()
# ppport.h:     GPL-1.0-or-later OR Artistic-1.0-Perl
# README:       GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/forks/Devel/Symdump.pm:   GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/forks/shared.pm:          GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/forks/signals.pm:         GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/forks.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/threads/shared/array.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/threads/shared/handle.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/threads/shared/hash.pm:   GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/threads/shared/scalar.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/forks
Source0:        https://cpan.metacpan.org/authors/id/R/RY/RYBSKEJ/forks-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
# Devel::Required not useful
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Any)
BuildRequires:  perl(ExtUtils::MM_Unix)
# Filter::Util::Call used only with perl < 5.008
BuildRequires:  perl(Storable) >= 2.05
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.3.0
BuildRequires:  perl(Acme::Damn)
BuildRequires:  perl(Attribute::Handlers)
# attributes not used with our perl
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket) >= 1.18
BuildRequires:  perl(List::MoreUtils) >= 0.15
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util) >= 1.11
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sys::SigAction) >= 0.11
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
# Test::Builder used only with perl < 5.008001
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
Requires:       perl(IO::Socket) >= 1.18
Requires:       perl(List::MoreUtils) >= 0.15
Requires:       perl(Scalar::Util) >= 1.11
Requires:       perl(sigtrap)
Requires:       perl(Sys::SigAction) >= 0.11
Provides:       perl(forks::Devel::Symdump) = %{version}
Provides:       perl(forks::signals) = %{version}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((IO::Socket|List::MoreUtils|Scalar::Util|Sys::SigAction)\\)$

%description
The forks.pm module is a drop-in replacement for threads.pm.  It has the
same syntax as the threads.pm module (it even takes over its name space) but
has some significant differences:

- you do _not_ need a special (threaded) version of Perl
- it is _much_ more economic with memory usage on OS's that support COW
- it is more efficient in the start-up of threads
- it is slightly less efficient in the stopping of threads
- it is less efficient in inter-thread communication

If for nothing else, it allows you to use the Perl threading model in
non-threaded Perl builds and in older versions of Perl (5.6.0 and
higher are supported).

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(if)
Requires:       perl(lib)
Requires:       perl(List::MoreUtils) >= 0.15
Requires:       perl(Sys::SigAction) >= 0.11
Requires:       perl(Thread::Queue)
Requires:       perl(threads)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n forks-%{version}
# Remove always skipped tests
rm t/forks99.t
perl -i -ne 'print $_ unless m{^t/forks99\.t}' MANIFEST
# Correct permissions
find . -type f -exec chmod a-x {} +
# Correct shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
unset FORKS_SIMULATE_USEITHREADS PERL_MM_USE_DEFAULT 
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find "$RPM_BUILD_ROOT" -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} "$RPM_BUILD_ROOT"/*
# Install tests
mkdir -p "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cp -a t "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cat > "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL_CORE PERL5_ITHREADS_STACK_SIZE THREADS_DAEMON_MODEL \
    THREADS_IP_MASK THREADS_NATIVE_EMULATION THREADS_NICE \
    THREADS_NO_PRELOAD_SHARED THREADS_SIGCHLD_IGNORE THREADS_SOCKET_UNIX
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test

%check
unset PERL_CORE PERL5_ITHREADS_STACK_SIZE THREADS_DAEMON_MODEL \
    THREADS_IP_MASK THREADS_NATIVE_EMULATION THREADS_NICE \
    THREADS_NO_PRELOAD_SHARED THREADS_SIGCHLD_IGNORE THREADS_SOCKET_UNIX
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes CREDITS README TODO
%{perl_vendorarch}/auto/forks
%{perl_vendorarch}/forks
%{perl_vendorarch}/forks.pm
%dir %{perl_vendorarch}/threads
%{perl_vendorarch}/threads/shared
%{_mandir}/man3/forks.*
%{_mandir}/man3/forks::*
%{_mandir}/man3/threads::shared::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Petr Pisar <ppisar@redhat.com> - 0.36-32
- Depend on perl(lib) for the tests

* Thu Aug 08 2024 Petr Pisar <ppisar@redhat.com> - 0.36-31
- Correct a license tag to "GPL-1.0-or-later OR Artistic-1.0-Perl"
- Package the tests
- Stop applying a patch for replacing signal handlers unneeded since Perl
  5.14 (CPAN RT#49878)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-29
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-25
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-22
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-19
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 29 2016 Petr Pisar <ppisar@redhat.com> - 0.36-4
- Modernize spec file

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-1
- 0.36 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-14
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-13
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 0.34-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.34-6
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.34-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.34-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Jun 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.34-1
- update because https://rt.cpan.org/Public/Bug/Display.html?id=56263

* Sun May 02 2010 Bernard Johnson <bjohnson@symetrix.com> - 0.33-5
- always apply assertion patch

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.33-4
- Mass rebuild with perl-5.12.0

* Sun Jan 31 2010 Bernard Johnson <bjohnson@symetrix.com> - 0.33-3
- fix permissions in build to squelch rpmlint complaints
- add version to provides

* Tue Jan 19 2010 Bernard Johnson <bjohnson@symetrix.com> - 0.33-2
- fix BR
- add patch from novell site to fix assertion in fedora < 13
- change references of forks::Devel::Symdump to Devel::Symdump

* Fri Jun 05 2009 Bernard Johnson <bjohnson@symetrix.com> - 0.33-1
- initial release
