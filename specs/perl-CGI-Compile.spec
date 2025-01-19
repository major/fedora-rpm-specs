# Perform optional tests
%bcond_without perl_CGI_Compile_enables_optional_test

Name:           perl-CGI-Compile
Summary:        Compile .cgi scripts to a code reference like ModPerl::Registry
Version:        0.27
Release:        2%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/CGI-Compile-%{version}.tar.gz 
URL:            https://metacpan.org/release/CGI-Compile
BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Sub::Name)
# Tests:
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
%if %{with perl_CGI_Compile_enables_optional_test}
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build-cycle: perl-Plack → perl-CGI-Compile → perl-Plack
BuildRequires:  perl(CGI::Emulate::PSGI)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Test)
%endif
BuildRequires:  perl(Sub::Identify)
# Test::Pod 1.41 not used
%endif

%{?perl_default_filter}

%description
CGI::Compile is an utility to compile CGI scripts into a code reference
that can run many times on its own namespace, as long as the script is
ready to run on a persistent environment.

%prep
%setup -q -n CGI-Compile-%{version}

sed -i 's/\r//' t/data_crlf.cgi t/end_crlf.cgi
sed -i -e '1s,#!.*perl,#!/usr/bin/perl,' t/*.t

%build
/usr/bin/perl Build.PL --installdirs vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING AUTOMATED_TESTING
./Build test


%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 15 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 0.27-1
- Update to 0.27

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.26-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 31 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.26-1
- Update to 0.26

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-8
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-7
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-4
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 09 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.25-1
- Update to 0.25

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-5
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-4
- Perl 5.32 rebuild

* Fri May 01 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-3
- Add test BR perl(Time::HiRes)

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 0.24-2
- Specify all dependencies

* Sun Feb 02 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.24-1
- Update to 0.24

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.23-2
- Update Source0 URL

* Sun Jan 19 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.23-1
- Update to 0.23
- Replace calls to %%{__perl} with /usr/bin/perl
- Remove no-longer-needed patch

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-12
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-8
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-3
- Perl 5.26 rebuild

* Mon May 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-2
- Fix building on Perl without '.' in @INC

* Mon Feb 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.22-1
- Update to 0.22

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-5
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Petr Pisar <ppisar@redhat.com> - 0.21-2
- Specify all dependencies
- Break build-cycle: perl-Plack → perl-CGI-Compile → perl-Plack

* Sat Jan 02 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.21-1
- Update to 0.21

* Sat Oct 31 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.20-1
- Update to 0.20

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.22 rebuild

* Sun Mar 08 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.19-1
- Update to 0.19

* Sun Nov 02 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.18-1
- Update to 0.18

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.17-1
- Update to 0.17

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.16-2
- Perl 5.18 rebuild

* Sun Mar 17 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.16-1
- Update to 0.16

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.15-4
- Perl 5.16 rebuild

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.15-3
- drop tests subpackage; move tests to main package documentation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.15-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.11-3
- Add BR: perl(CGI) (Fix FTBFS: BZ 660891).

* Tue Jun 22 2010 Petr Pisar <ppisar@redhat.com> - 0.11-2
- Rebuild against perl-5.12

* Sat Mar 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.11-1
- specfile by Fedora::App::MaintainerTools 0.006


