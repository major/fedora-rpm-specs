Name:           perl-forks
Version:        0.36
Release:        23%{?dist}
Summary:        A drop-in replacement for Perl threads using fork()
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic)
URL:            https://metacpan.org/release/forks
Source0:        https://cpan.metacpan.org/authors/id/R/RY/RYBSKEJ/forks-%{version}.tar.gz
# https://bugzilla.novell.com/show_bug.cgi?id=527537
# https://bugzillafiles.novell.org/attachment.cgi?id=313860
# http://rt.cpan.org/Public/Bug/Display.html?id=49878
Patch0:         perl-forks-assertion.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
# Devel::Required not useful
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.10
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
# Test::Builder used only with perl < 5.008001
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
Requires:       perl(IO::Socket) >= 1.18
Requires:       perl(List::MoreUtils) >= 0.15
Requires:       perl(Scalar::Util) >= 1.11
Requires:       perl(sigtrap)
Requires:       perl(Sys::SigAction) >= 0.11
Provides:       perl(forks::Devel::Symdump) = %{version}

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

%prep
%setup -q -n forks-%{version}
%patch0 -p1
find . -type f -exec chmod a-x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CREDITS README TODO
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*.3*

%changelog
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
