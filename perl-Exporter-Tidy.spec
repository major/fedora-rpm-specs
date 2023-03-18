Name:           perl-Exporter-Tidy
Version:        0.08
Release:        27%{?dist}
Summary:        Another way of exporting symbols
# Generated with licenses.pl
License:        0BSD or AAL or AFL-3.0 or AGPL-3.0-only or APSL-2.0 or Apache-1.1 or Apache-2.0 or Artistic-2.0 or BSD-1-Clause or BSD-2-Clause or BSD-3-Clause or BSD-3-Clause-LBNL or BSL-1.0 or CATOSL-1.1 or CDDL-1.0 or CNRI-Python or CPAL-1.0 or CPL-1.0 or CUA-OPL-1.0 or ECL-1.0 or ECL-2.0 or EFL-2.0 or EPL-1.0 or EPL-2.0 or EUDatagrid or EUPL-1.1 or EUPL-1.2 or Entessa or Fair or GPL-1.0-only or GPL-2.0-only or GPL-3.0-only or HPND or IPL-1.0 or ISC or Jam or LGPL-2.0-only or LGPL-2.1-only or LGPL-3.0-only or LPL-1.02 or MIT or MIT-0 or MPL-1.0 or MPL-1.1 or MPL-2.0 or MS-PL or MS-RL or MirOS or Motosoto or NCSA or NGPL or NTP or Naumen or Nokia or OLDAP-2.8 or OSL-1.0 or OSL-2.1 or OSL-3.0 or PHP-3.01 or PostgreSQL or QPL-1.0 or RPSL-1.0 or SISSL or SPL-1.0 or Sleepycat or UPL-1.0 or Unicode-DFS-2016 or Unlicense or VSL-1.0 or W3C or ZPL-2.0 or ZPL-2.1 or Zlib
URL:            https://metacpan.org/release/Exporter-Tidy
Source0:        https://cpan.metacpan.org/authors/id/J/JU/JUERD/Exporter-Tidy-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
# Tests only
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
Requires:       perl(Carp)

%description
This module serves as an easy, clean alternative to Exporter. Unlike
Exporter, it is not subclassed, but it simply exports a custom import()
into your namespace.

%prep
%setup -q -n Exporter-Tidy-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-25
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-23
- Replace EPL by EPL-1.0

* Wed Jan 05 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-22
- Replace CDDL by correct CDDL-1.0

* Mon Jan 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-21
- Use make_* macros

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-19
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-2
- Perl 5.22 rebuild

* Tue Jan 06 2015 Petr Šabata <contyk@redhat.com> - 0.08-1
- 0.08 bump

* Mon Jan 05 2015 Petr Šabata <contyk@redhat.com> - 0.07-1
- Initial packaging
