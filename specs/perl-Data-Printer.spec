Name:           perl-Data-Printer
Version:        1.002001
Release:        3%{?dist}
Summary:        Pretty printer for Perl data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Printer
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Printer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::Size)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::Util::FieldHash)
# Hash::Util::FieldHash::Compat not used
BuildRequires:  perl(if)
BuildRequires:  perl(mro)
# MRO::Compat not used
BuildRequires:  perl(Package::Stash) >= 0.3
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sort::Naturally)
BuildRequires:  perl(Term::ANSIColor) >= 3
BuildRequires:  perl(charnames)
BuildRequires:  perl(overload)
BuildRequires:  perl(version) >= 0.77
# Win32::Console::ANSI not used
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::HomeDir::Test)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Date::Handler::Delta)
BuildRequires:  perl(Date::Pcalc::Object)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Tiny)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(DateTime::Incomplete)
Requires:       perl(B)
Requires:       perl(B::Deparse)
Requires:       perl(File::HomeDir) >= 0.91
Requires:       perl(Hash::Util::FieldHash)
Requires:       perl(mro)
Requires:       perl(Package::Stash) >= 0.3
Requires:       perl(Term::ANSIColor) >= 3
Requires:       perl(version) >= 0.77

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\((File::HomeDir|Term::ANSIColor)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Package::Stash\\)$

%description
Data::Printer is a Perl module to pretty-print Perl data structures and
objects in full color. It is meant to display variables on screen, properly
formatted to be inspected by a human.

%prep
%setup -q -n Data-Printer-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.002001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.002001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 1.002001-1
- Update to 1.002001
- Migrate to SPDX license

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.001001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.001001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 31 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 1.001001-1
- Update to 1.001001

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.001000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.001000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 25 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 1.001000-1
- Update to 1.001000

* Mon Aug 01 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 1.000004-7
- Rework dependencies

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.000004-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.000004-2
- Perl 5.34 rebuild

* Sun Mar 07 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 1.000004-1
- Update to 1.000004

* Sun Feb 28 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 1.000001-1
- Update to 1.000001
- Replace calls to %%{__perl} with /usr/bin/perl
- Use %%{make_install} instead of "make pure_install
- Use %%{make_build} instead of "make"

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-2
- Perl 5.26 rebuild

* Wed Apr 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-1
- 0.39 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-2
- Perl 5.24 rebuild

* Mon Mar 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-1
- 0.38 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Petr Pisar <ppisar@redhat.com> - 0.36-1
- 0.36 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-3
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-2
- Perl 5.20 rebuild

* Tue Jul 22 2014 David Dick <ddick@cpan.org> - 0.35-1
- Initial release
