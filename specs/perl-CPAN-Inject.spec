Name:           perl-CPAN-Inject
Version:        1.14
Release:        38%{?dist}
Summary:        Base class for injecting distributions into CPAN sources
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Inject
Source0:        https://cpan.metacpan.org/authors/id/P/PS/PSHANGOV/CPAN-Inject-%{version}.tar.gz
# Work around CPAN bug mangling working directory, bug #1084093, CPAN RT#94963
Patch0:         CPAN-Inject-1.14-Restore-working-directory-after-loading-CPAN-configu.patch
# Expect en error if DNS does not work, bug #1138562, CPAN RT#98774
Patch1:         CPAN-Inject-1.14-Expect-unknown-exception-while-loading-CPAN-configur.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  sed
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install) >= 1.00
# Runtime
BuildRequires:  perl(CPAN) >= 1.36
BuildRequires:  perl(CPAN::Checksums) >= 1.05
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename) >= 2.6
BuildRequires:  perl(File::chmod) >= 0.30
BuildRequires:  perl(File::Copy) >= 2.02
BuildRequires:  perl(File::Path) >= 1.00
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat) >= 1.00
BuildRequires:  perl(Params::Util) >= 0.21
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Remove) >= 0.34
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Script) >= 1.02
Requires:       perl(CPAN) >= 1.36
Requires:       perl(CPAN::Checksums) >= 1.05
Requires:       perl(Cwd)
Requires:       perl(File::Basename) >= 2.6
Requires:       perl(File::chmod) >= 0.30
Requires:       perl(File::Copy) >= 2.02
Requires:       perl(File::Path) >= 1.00
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(File::stat) >= 1.00
Requires:       perl(File::chmod) >= 0.30
Requires:       perl(Params::Util) >= 0.21

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(CPAN::Checksums\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::(Basename|chmod|Copy|Path|Spec|stat|chmod)\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Params::Util\\)\s*$

%description
Following the release of CPAN::Mini, the CPAN::Mini::Inject module was
created to add additional distributions into a minicpan mirror.

%prep
%setup -q -n CPAN-Inject-%{version}
%patch -P0 -p1
%patch -P1 -p1

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
export HOME=$PWD/home
mkdir "$HOME"
make test </dev/null

%files
%doc Changes
%{perl_vendorlib}/*
%{_bindir}/cpaninject
%{_mandir}/man1/cpaninject.1.gz
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-31
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-28
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-25
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-22
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-19
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-16
- Perl 5.26 re-rebuild of bootstrapped packages

* Wed Jun 07 2017 Petr Pisar <ppisar@redhat.com> - 1.14-15
- Fix a changelog entry

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-14
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-9
- Perl 5.22 rebuild

* Thu Sep 11 2014 Petr Pisar <ppisar@redhat.com> - 1.14-8
- Expect an error if DNS does not work (bug #1138562)

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Petr Pisar <ppisar@redhat.com> - 1.14-5
- Run tests in a new home and noninteractively
- Work around CPAN bug mangling working directory (bug #1084093)

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 1.14-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-1
- 1.14 bump
- Modernize spec and drop command macros
- Remove bundled libraries. 
- Update dependencies.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.13-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.13-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Petr Sabata <psabata@redhat.com> - 1.13-1
- 1.13 version bump

* Mon Jan  3 2011 Petr Sabata <psabata@redhat.com> - 1.12-1
- 1.12 version bump

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-4
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-3
- Mass rebuild with perl-5.12.0

* Tue Dec 22 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.11-2
- switch off test which had problems with cpan in mock

* Wed Nov 18 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.11-1
- Specfile autogenerated by cpanspec 1.78.
