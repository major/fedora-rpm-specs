Name:           perl-Exporter-Tidy
Version:        0.08
Release:        26%{?dist}
Summary:        Another way of exporting symbols
# Generated with licenses.pl
License:        AAL or AFL or AGPLv3 or APSL 2.0 or ASL 2.0 or Artistic 2.0 or BSD or Boost or CATOSL or CDDL-1.0 or CNRI or CPAL or CeCILL or ECL 2.0 or EFL 2.0 or EPL-1.0 or EU Datagrid or EUPL 1.1 or Entessa or Fair or GPLv2 or GPLv3 or IBM or IPA or ISC or LGPLv2 or LGPLv3 or LPL or LPPL or MIT or MPLv1.1 or MPLv2.0 or MS-PL or MS-RL or MirOS or Motosoto or NCSA or NGPL or Naumen or Nokia or OFL or OSL 3.0 or PHP or PostgreSQL or Python or QPL or RPSL or SPL or Sleepycat or VSL or W3C or ZPLv2.0 or zlib
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
