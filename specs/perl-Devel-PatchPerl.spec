Name:           perl-Devel-PatchPerl
Version:        2.08
Release:        13%{?dist}
Summary:        Patch perl source a la Devel::PPPort's buildperl.pl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-PatchPerl
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Devel-PatchPerl-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(File::pushd) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(lib)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More)
# Test::Pod not used
# Test::Pod::Coverage not used
Requires:       patch
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(File::pushd) >= 1.00

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::pushd\\)$

%description
Devel::PatchPerl is a modularization of the patching code contained in
Devel::PPPort's buildperl.pl.

%prep
%setup -q -n Devel-PatchPerl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-1
- 2.08 bump

* Mon Jan 04 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.06-1
- 2.06 bump

* Fri Nov 20 2020 Petr Pisar <ppisar@redhat.com> - 2.04-1
- 2.04 bump

* Mon Nov 09 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-1
- 2.02 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-2
- Perl 5.32 rebuild

* Fri Jun 05 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-1
- 2.00 bump

* Tue May 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-1
- 1.98 bump

* Mon May 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.94-1
- 1.94 bump

* Tue Apr 28 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.92-1
- 1.92 bump

* Thu Mar 12 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.90-1
- 1.90 bump

* Wed Mar 11 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.88-1
- 1.88 bump

* Wed Feb 05 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.86-1
- 1.86 bump

* Wed Jan 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.84-1
- 1.84 bump

* Wed Nov 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-1
- 1.80 bump

* Thu Nov 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-1
- 1.78 bump

* Mon Nov 11 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-1
- 1.76 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.64-1
- 1.64 bump

* Wed Jun 05 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.62-1
- 1.62 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-2
- Perl 5.30 rebuild

* Tue May 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-1
- 1.60 bump

* Mon Apr 29 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.58-1
- 1.58 bump

* Tue Feb 26 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-1
- 1.56 bump

* Mon Feb 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.54-1
- 1.54 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-2
- Perl 5.28 rebuild

* Sat Jun 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-1
- 1.52 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-2
- Perl 5.26 rebuild

* Mon Feb 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-1
- 1.48 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-1
- 1.46 bump

* Mon Aug 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-1
- 1.44 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-2
- Perl 5.24 rebuild

* Fri Apr 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-1
- 1.42 bump

* Tue Feb 02 2016 Petr Pisar <ppisar@redhat.com> - 1.40-1
- 1.40 bump

* Tue Jul 07 2015 Petr Šabata <contyk@redhat.com> - 1.38-1
- 1.38 bump, fixes for gcc5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-2
- Perl 5.22 rebuild

* Thu Jun 04 2015 Petr Šabata <contyk@redhat.com> - 1.34-1
- 1.34 bump

* Mon Jan 05 2015 Petr Šabata <contyk@redhat.com> - 1.30-1
- 1.30 bump

* Thu Nov 13 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-1
- 1.28 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 10 2013 Iain Arnell <iarnell@gmail.com> 1.00-1
- update to latest upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.84-2
- Perl 5.18 rebuild

* Fri Apr 19 2013 Iain Arnell <iarnell@gmail.com> 0.84-1
- update to latest upstream version
- drop IPC::Cmd dependency

* Tue Feb 19 2013 Iain Arnell <iarnell@gmail.com> 0.78-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 07 2012 Iain Arnell <iarnell@gmail.com> 0.76-1
- update to latest upstream version

* Fri Aug 03 2012 Iain Arnell <iarnell@gmail.com> 0.74-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.72-2
- Perl 5.16 rebuild

* Sat Jun 09 2012 Iain Arnell <iarnell@gmail.com> 0.72-1
- update to latest upstream version

* Fri May 18 2012 Iain Arnell <iarnell@gmail.com> 0.70-1
- update to latest upstream version

* Tue Apr 03 2012 Iain Arnell <iarnell@gmail.com> 0.68-1
- update to latest upstream version

* Thu Feb 09 2012 Iain Arnell <iarnell@gmail.com> 0.66-1
- update to latest upstream version

* Sun Feb 05 2012 Iain Arnell <iarnell@gmail.com> 0.64-1
- update to latest upstream version

* Fri Jan 06 2012 Iain Arnell <iarnell@gmail.com> 0.62-1
- update to latest upstream version

* Mon Oct 31 2011 Iain Arnell <iarnell@gmail.com> 0.60-2
- requires 'patch'

* Fri Oct 28 2011 Iain Arnell <iarnell@gmail.com> 0.60-1
- update to latest upstream version

* Sat Oct 22 2011 Iain Arnell <iarnell@gmail.com> 0.58-1
- update to latest upstream version

* Sat Sep 24 2011 Iain Arnell <iarnell@gmail.com> 0.52-1
- update to latest upstream version

* Sat Aug 13 2011 Iain Arnell <iarnell@gmail.com> 0.48-1
- update to latest upstream version

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.40-3
- Perl mass rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.40-2
- Perl mass rebuild

* Fri Jun 10 2011 Iain Arnell <iarnell@gmail.com> 0.40-1
- update to latest upstream version

* Fri May 27 2011 Iain Arnell <iarnell@gmail.com> 0.36-1
- update to latest upstream version

* Wed Apr 27 2011 Iain Arnell <iarnell@gmail.com> 0.30-1
- Specfile autogenerated by cpanspec 1.78.
