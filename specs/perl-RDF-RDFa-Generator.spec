Name:           perl-RDF-RDFa-Generator
Version:        0.204
Release:        4%{?dist}
Summary:        Generate data in RDFa
# COPYRIGHT:    LicenseRef-Fedora-Public-Domain
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/RDF-RDFa-Generator
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/RDF-RDFa-Generator-%{version}.tar.gz
# Adjust tests to perl-Test-Warnings ≥ 0.034, bug #2341034, proposed upstream,
# <https://github.com/perlrdf/p5-rdf-rdfa-generator/issues/7>,
# Copied from Debian <https://salsa.debian.org/perl-team/modules/packages/librdf-rdfa-generator-perl/-/raw/66f400fda5cc281ed7b8131fbd983a8eb30cc10d/debian/patches/done_testing-conflict.patch>
Patch0:         done_testing-conflict.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Icon::FamFamFam::Silk)
BuildRequires:  perl(RDF::NS::Curated) >= 0.006
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI::NamespaceMap) >= 1.05
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.60
# Tests:
BuildRequires:  perl(Attean) >= 0.019
BuildRequires:  perl(Attean::RDF)
# Additional prefixes are tested and they are provided by RDF::Prefixes that
# is an optional dependency of perl-URI-NamespaceMap
BuildRequires:  perl(RDF::Prefixes)
BuildRequires:  perl(Test::Modern)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Output)
Requires:       perl(XML::LibXML) >= 1.60

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Attean|Test::More|XML::LibXML)\\)$

%description
These Perl modules allow you to generate RDFa (Resource Description Framework
in Attributes) trees.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Attean) >= 0.019
Requires:       perl(RDF::Prefixes)
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n RDF-RDFa-Generator-%{version}
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
%doc Changes COPYRIGHT CREDITS examples README TODO
%dir %{perl_vendorlib}/RDF
%dir %{perl_vendorlib}/RDF/RDFa
%{perl_vendorlib}/RDF/RDFa/Generator.pm
%{perl_vendorlib}/RDF/RDFa/Generator
%{_mandir}/man3/RDF::RDFa::Generator.*
%{_mandir}/man3/RDF::RDFa::Generator::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Feb 07 2025 Petr Pisar <ppisar@redhat.com> - 0.204-4
- Adjust tests to perl-Test-Warnings ≥ 0.034 (bug #2341034)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.204-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.204-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 22 2024 Petr Pisar <ppisar@redhat.com> - 0.204-1
- 0.204 bump

* Thu Feb 22 2024 Petr Pisar <ppisar@redhat.com> - 0.202-1
- 0.202 bump
- Install the tests

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.200-14
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.200-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.200-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.200-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.200-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.200-2
- Perl 5.28 rebuild

* Mon Feb 12 2018 Petr Pisar <ppisar@redhat.com> - 0.200-1
- 0.200 bump

* Tue Feb 06 2018 Petr Pisar <ppisar@redhat.com> - 0.192-2
- Adapt tests to changes in Attean-0.019

* Tue Jan 02 2018 Petr Pisar <ppisar@redhat.com> - 0.192-1
- 0.192 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.103-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.103-2
- Perl 5.26 rebuild

* Fri Feb 10 2017 Petr Pisar <ppisar@redhat.com> 0.103-1
- Specfile autogenerated by cpanspec 1.78.
