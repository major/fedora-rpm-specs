# Recomend modules for RDF prefixes support
%bcond_without perl_URI_NamespaceMap_enables_rdf
# Perform optional tests
%bcond_without perl_URI_NamespaceMap_enables_optional_test

Name:           perl-URI-NamespaceMap
Version:        1.10
Release:        15%{?dist}
Summary:        Object-oriented collection of name spaces
# COPYRIGHT:    Public Domain
# other files:  GPL+ or Artistic
License:        (GPL+ or Artistic) or Public Domain
URL:            https://metacpan.org/release/URI-NamespaceMap
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/URI-NamespaceMap-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(IRI) >= 0.004
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Moo) >= 1.006000
BuildRequires:  perl(namespace::autoclean) >= 0.20
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library) >= 1.000000
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::URI) >= 0.004
BuildRequires:  perl(URI) >= 1.52
BuildRequires:  perl(warnings)
# Optional run-time:
# We need at least one of them
%if %{with perl_URI_NamespaceMap_enables_rdf}
BuildRequires:  perl(RDF::NS) >= 20130802
BuildRequires:  perl(RDF::NS::Curated)
BuildRequires:  perl(RDF::Prefixes)
%endif
BuildRequires:  perl(XML::CommonNS)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
# Build cycle: perl-Attean → perl-URI-NamespaceMap
%if %{with perl_URI_NamespaceMap_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(Attean) >= 0.025
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(RDF::Trine::NamespaceMap)
BuildRequires:  perl(Types::Attean)
%endif
# We need at least one of them, we choose XML::CommonNS
%if %{with perl_URI_NamespaceMap_enables_rdf}
Recommends:     perl(RDF::NS) >= 20130802
Recommends:     perl(RDF::NS::Curated)
Recommends:     perl(RDF::Prefixes)
%endif
Requires:       perl(XML::CommonNS)

%description
These Perl modules provide a database system for managing URI name spaces in
an object-oriented manner.

%prep
%setup -q -n URI-NamespaceMap-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-12
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-8
- Perl 5.34 re-rebuild of bootstrapped packages

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-4
- Perl 5.32 re-rebuild of bootstrapped packages

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-2
- Perl 5.30 rebuild

* Tue Apr 16 2019 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Petr Pisar <ppisar@redhat.com> - 1.06-1
- 1.06 bump

* Tue Jan 02 2018 Petr Pisar <ppisar@redhat.com> 1.04-1
- Specfile autogenerated by cpanspec 1.78.
