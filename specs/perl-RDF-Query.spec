Name:           perl-RDF-Query
Version:        2.919
Release:        3%{?dist}
Summary:        SPARQL 1.1 Query and Update implementation for RDF::Trine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RDF-Query
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/RDF-Query-%{version}.tar.gz
# Do not run author tests
Patch0:         RDF-Query-2.917-Disable-author-tests.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# None of the ./bin scripts is executed at tests
BuildRequires:  perl(base)
# Benchmark not used at tests
BuildRequires:  perl(Carp)
# CGI not used at tests
BuildRequires:  perl(constant)
# Cwd not used at tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(I18N::LangTags)
BuildRequires:  perl(JSON) >= 2
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Log4perl)
# LWP::MediaTypes not used at tests
# LWP::Simple not used at tests
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(overload)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(POSIX)
# RDF::Endpoint::Server does not exist
# <https://github.com/kasei/perlrdf/issues/139>
BuildRequires:  perl(RDF::Trine) >= 1.004
BuildRequires:  perl(RDF::Trine::Iterator)
BuildRequires:  perl(RDF::Trine::Namespace)
BuildRequires:  perl(RDF::Trine::Node::Blank)
BuildRequires:  perl(RDF::Trine::Node::Literal)
BuildRequires:  perl(RDF::Trine::Node::Resource)
BuildRequires:  perl(RDF::Trine::Node::Variable)
BuildRequires:  perl(RDF::Trine::Statement)
BuildRequires:  perl(RDF::Trine::Statement::Quad)
BuildRequires:  perl(RDF::Trine::VariableBindings)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(sort)
BuildRequires:  perl(Storable)
# Term::ReadKey not used at tests
# Term::ReadLine not used at tests
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI) >= 1.52
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
# Optional run-time:
BuildRequires:  perl(Geo::Distance) >= 0.09
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# Optional tests:
BuildRequires:  perl(Test::JSON) >= 0.03
Requires:       perl(CGI)
Requires:       perl(Exporter)
Recommends:     perl(Geo::Distance) >= 0.09
Requires:       perl(JSON) >= 2
Requires:       perl(URI) >= 1.52

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((JSON|Test::More|URI)\\)$
# Remove private dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((models\\.pl)\\)

%description
RDF::Query allows SPARQL and RDQL queries to be run against an RDF model,
returning rows of matching results.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::JSON) >= 0.03

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n RDF-Query-%{version}
%patch -P0 -p1
# Remove bundled modules, but keep the directory to prevent from runing author
# tests.
rm -rf inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Remove always skipped tests
for T in t/dataset-from-net.t t/hooks.t t/plan.t; do
    rm -- "$T"
    perl -i -ne 'print $_ unless m{\A'"$T"'\Z}' MANIFEST
done
# Remove executable bits from a documentation
find examples -type f -exec chmod -x {} +
# Fix shellbangs
for F in bin/rqsh examples/*.pl; do
    perl -i -MConfig -pe 's{\A#!/usr/bin/env\s+perl}{$Config{startperl}} if ($. == 1)' "$F"
done
# Help generators to recognize Perl scripts
for F in t/*.t t/streams.t.deprecated t/models.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a data t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset RDFQUERY_NETWORK_TESTS
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
unset RDFQUERY_NETWORK_TESTS
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc examples Changes.ttl README
%{_bindir}/rqsh
%dir %{perl_vendorlib}/RDF
%{perl_vendorlib}/RDF/Query
%{perl_vendorlib}/RDF/Query.pm
%{_mandir}/man1/rqsh.*
%{_mandir}/man3/RDF::Query.*
%{_mandir}/man3/RDF::Query::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.919-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.919-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Petr Pisar <ppisar@redhat.com> - 2.919-1
- 2.919 bump

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-20
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Petr Pisar <ppisar@redhat.com> - 2.918-18
- Remove a build-dependency on sed
- Package tests

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-16
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-13
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Petr Pisar <ppisar@redhat.com> - 2.918-11
- Modernize a spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.918-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.918-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Petr Pisar <ppisar@redhat.com> - 2.918-1
- 2.918 bump

* Thu Oct 27 2016 Petr Pisar <ppisar@redhat.com> 2.917-1
- Specfile autogenerated by cpanspec 1.78.
