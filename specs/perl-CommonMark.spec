Name:           perl-CommonMark
Version:        0.310100
Release:        4%{?dist}
Summary:        Interface to the CommonMark C library
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CommonMark
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWELLNHOF/CommonMark-%{version}.tar.gz

# build requirements
BuildRequires:  cmark-devel >= 0.21.0
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Encode)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)

%description
This module is a wrapper around the official CommonMark C library libcmark.
It closely follows the original API.

%prep
%setup -q -n CommonMark-%{version}

%build
# -std=c17 is needed to fix build with GCC 15
# see https://github.com/Perl/perl5/issues/23192
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS -std=c17" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/CommonMark*
%{_mandir}/man3/*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.310100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.310100-3
- Perl 5.42 rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.310100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 18 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 0.310100-1
- Update to 0.310100

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.290000-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.290000-21
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.290000-17
- Perl 5.38 rebuild

* Mon Jan 30 2023 Jens Petersen <petersen@redhat.com> - 0.290000-16
- rebuild

* Fri Jan 27 2023 Jens Petersen <petersen@redhat.com> - 0.290000-15
- rebuild f38 against newer cmark

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.290000-12
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.290000-9
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.290000-6
- Perl 5.32 rebuild

* Tue Feb 04 2020 Petr Pisar <ppisar@redhat.com> - 0.290000-5
- Rebuild against cmark 0.29.0 (bug #1697593)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.290000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.290000-3
- Pass NO_PERLLOCAL to Makefile.PL
- Use %%{make_install} instead of make install (thanks to ppisar)

* Thu Aug 01 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.290000-2
- Take into account review comments (#1735562)

* Tue Jul 30 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.290000-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
