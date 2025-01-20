Name:           perl-JSON-Path
Version:        1.0.6
Release:        3%{?dist}
Summary:        Search nested hashref/arrayref structures using JSONPath

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/JSON-Path
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POPEFELIX/JSON-Path-%{version}.tar.gz

BuildArch:      noarch

# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter >= 1:5.16.0
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Assert)
BuildRequires:  perl(Exporter::Shiny)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LV)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test2::V0)

# Those are only needed when building for RHEL, on Fedora they come in as
# dependencies of the above
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires:  perl(CPAN)
%endif


%description
This module implements JSONPath, an XPath-like language for searching JSON-
like structures.


%prep
%setup -q -n JSON-Path-%{version}


%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} %{buildroot}/*


%check
%{make_build} test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/JSON*
%{_mandir}/man3/JSON*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 27 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 1.0.6-1
- Update to 1.0.06
- Use correct license in license tag

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 17 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 1.0.4-1
- Update to 1.0.4
- Update dependencies
- Migrate to SPDX license

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 25 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 1.0.3-1
- Update to 1.0.3

* Sun Sep 11 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 1.0.2-1
- Update to 1.0.2

* Sun Sep 04 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 1.0.1-1
- Update to 1.0.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.510-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.510-2
- Perl 5.36 rebuild

* Mon Apr 04 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 0.510-1
- Update to 0.51

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.431-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.431-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.431-2
- Perl 5.34 rebuild

* Sun Jan 31 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.431-1
- Update to 0.431
- Replace calls to %%{__perl} with /usr/bin/perl
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make
- Pass NO_PERLLOCAL to Makefile.PL
- Add %%license tag

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.420-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.420-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.420-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.420-2
- Perl 5.28 rebuild

* Sun May 06 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.420-1
- Update to 0.420

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.411-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.411-1
- Update to 0.411

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.205-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.205-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.205-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.205-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.205-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.205-4
- Pass NO_PACKLIST to Makefile.PL
- Remove %%defattr macro
- Tighten file listing

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.205-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.205-2
- Perl 5.22 rebuild

* Sun Sep 07 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.205-1
- Update to 0.205

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.101-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.101-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 0.101-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Mathieu Bridon <bochecha@fedoraproject.org> 0.101-1
- Specfile autogenerated by cpanspec 1.78. (with a couple of tweaks)
