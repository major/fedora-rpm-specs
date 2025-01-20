# Recomend modules for RDF prefixes support
%bcond_without perl_URI_NamespaceMap_enables_rdf
# Perform optional tests
%bcond_without perl_URI_NamespaceMap_enables_optional_test

# Build cycle: perl-Attean → perl-URI-NamespaceMap
%if %{with perl_URI_NamespaceMap_enables_optional_test} && !%{defined perl_bootstrap}
%global optional_test 1
%else
%global optional_test 0
%endif

Name:           perl-URI-NamespaceMap
Version:        1.12
Release:        5%{?dist}
Summary:        Object-oriented collection of name spaces
# COPYRIGHT:    LicenseRef-Fedora-Public-Domain
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/URI-NamespaceMap
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/URI-NamespaceMap-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
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
%if %{optional_test}
# Optional tests:
BuildRequires:  perl(Attean) >= 0.025
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(RDF::Trine::NamespaceMap)
BuildRequires:  perl(Types::Attean) >= 0.024
%endif
# We need at least one of them, we choose XML::CommonNS
%if %{with perl_URI_NamespaceMap_enables_rdf}
Recommends:     perl(RDF::NS) >= 20130802
Recommends:     perl(RDF::NS::Curated)
Recommends:     perl(RDF::Prefixes)
%endif
Requires:       perl(URI) >= 1.52
Requires:       perl(XML::CommonNS)

# Hide private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CommonTest\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(CommonTest\\)
# Remove under-specified dependencies
%global __requires_exclude %{__requires_exclude}|^perl\\((Attean|Test::More|Types::Attean|URI)\\)$

%description
These Perl modules provide a database system for managing URI name spaces in
an object-oriented manner.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88
Requires:       perl(URI) >= 1.52
%if %{optional_test}
Requires:       perl(Attean) >= 0.025
Requires:       perl(RDF::Trine::NamespaceMap)
Requires:       perl(Types::Attean) >= 0.024
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n URI-NamespaceMap-%{version}
%if !%{optional_test}
for F in t/types-attean.t t/types-trine.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS README
%dir %{perl_vendorlib}/Types
%{perl_vendorlib}/Types/Namespace.pm
%dir %{perl_vendorlib}/URI
%{perl_vendorlib}/URI/Namespace.pm
%{perl_vendorlib}/URI/NamespaceMap
%{perl_vendorlib}/URI/NamespaceMap.pm
%{_mandir}/man3/Types::Namespace.*
%{_mandir}/man3/URI::Namespace.*
%{_mandir}/man3/URI::NamespaceMap.*
%{_mandir}/man3/URI::NamespaceMap::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Petr Pisar <ppisar@redhat.com> - 1.12-1
- 1.12 bump
- Package the tests

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
