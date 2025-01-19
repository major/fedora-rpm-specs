# Perform optional tests
%bcond_without perl_Attean_enables_optional_test

Name:           perl-Attean
Version:        0.034
Release:        3%{?dist}
Summary:        Semantic web framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Attean
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/Attean-%{version}.tar.gz
# Do not use /usr/bin/env in shebangs,
# <https://github.com/kasei/attean/pull/117>, refused by the upstream
Patch0:         Attean-0.017-Canonize-shebangs.patch
# Disable changelog generator and other not helpful dependencies
Patch1:         Attean-0.034-Disable-unwanted-build-time-dependecies.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Algorithm::Combinatorics)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exporter::Tiny) >= 1
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Negotiate)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(I18N::LangTags)
BuildRequires:  perl(IRI) >= 0.005
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Math::Cartesian::Product) >= 1.008
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moo) >= 2.000002
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Log::Any)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(open)
BuildRequires:  perl(PerlIO::Layers)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Role::Tiny) >= 2.000003
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(sort)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Sub::Util) >= 1.4
BuildRequires:  perl(Test::Modern) >= 0.012
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::Roo::Role)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Type::Tiny::Role)
BuildRequires:  perl(Types::Common::String)
BuildRequires:  perl(Types::Namespace)
BuildRequires:  perl(Types::Path::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::URI)
BuildRequires:  perl(Types::UUID)
BuildRequires:  perl(URI::Escape) >= 1.36
BuildRequires:  perl(URI::file)
BuildRequires:  perl(URI::Namespace)
BuildRequires:  perl(URI::NamespaceMap) >= 0.12
BuildRequires:  perl(utf8)
BuildRequires:  perl(UUID::Tiny)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::Simple)
# Tests:
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Roo)
BuildRequires:  perl(Test::TypeTiny)
%if %{with perl_Attean_enables_optional_test}
# Optional tests:
BuildRequires:  perl(RDF::Trine)
%endif
Requires:       perl(Exporter::Tiny) >= 1
Requires:       perl(IRI) >= 0.005
Requires:       perl(Math::Cartesian::Product) >= 1.008
Requires:       perl(Moo) >= 2.000002
Requires:       perl(MooX::Log::Any)
Requires:       perl(Role::Tiny) >= 2.000003
Requires:       perl(sort)
Requires:       perl(Sub::Util) >= 1.4
Requires:       perl(URI::Escape) >= 1.36
Requires:       perl(URI::NamespaceMap) >= 0.12
# Provide collections of modules defined in one file.
# This is a public API, see Attean::API::Query POD.
# Search for "utility package" in the sources.
Provides:       perl(Attean::Algebra) = %{version}
Provides:       perl(Attean::API::Query) = %{version}
Provides:       perl(Attean::Expression) = %{version}
Provides:       perl(Attean::Plan) = %{version}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter::Tiny|IRI|Math::Cartesian::Product|Moo|Role::Tiny|Sub::Util|Test::Modern|Test::More|URI::Escape|URI::NamespaceMap)\\)

%description
Attean provides APIs for parsing, storing, querying, and serializing semantic
web (RDF and SPARQL) data.

%package -n perl-Test-Attean
Summary:        Modules for testing Attean semantic web framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Test::Modern) >= 0.012
# Renamed from perl-Attean-tests-0.030-6.
# No Obsoletes and Provides because perl-Attean-tests was reused for a different purpose.
# Users will get perl-Test-Attean installed by dependencies on Perl modules.

%description -n perl-Test-Attean
These are helper Perl modules for testing Attean, a semantic web framework.

%package tests
Summary:        Tests for %{name}
Requires:       perl-Test-Attean = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Attean::API::CostPlanner)
Requires:       perl(Attean::API::NaiveJoinPlanner)
Requires:       perl(Attean::API::NullaryQueryTree)
Requires:       perl(Attean::API::SimpleCostPlanner)
Requires:       perl(Attean::API::UnionScopeVariablesPlan)
Requires:       perl(Attean::Plan::Exists)
Requires:       perl(Attean::QueryPlanner)
Requires:       perl(AtteanX::API::JoinRotatingPlanner)
Requires:       perl(Moo)
%if %{with perl_Attean_enables_optional_test}
Requires:       perl(RDF::Trine)
%endif
Requires:       perl(Test::Attean::MutableETagCacheableQuadStore)
Requires:       perl(Test::Attean::MutableQuadStore)
Requires:       perl(Test::Attean::MutableTimeCacheableQuadStore)
Requires:       perl(Test::Attean::QuadStore)
Requires:       perl(Test::Attean::TripleStore)
Requires:       perl(Test::Modern) >= 0.012
Requires:       perl(Test::More) >= 0.88

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Attean-%{version}
# Remove bundled modules
rm -r inc/*
perl -i -lne 'print $_ unless m{^inc/}' MANIFEST
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
%doc Changes CONTRIBUTING README.md
%{_bindir}/attean_parse
%{_bindir}/attean_query
%{perl_vendorlib}/Attean*
%{perl_vendorlib}/Types
%{_mandir}/man3/Attean*
%{_mandir}/man3/Types::*

%files -n perl-Test-Attean
%{perl_vendorlib}/Test/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Petr Pisar <ppisar@redhat.com> - 0.034-1
- 0.034 bump

* Mon May 13 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-6
- Fix for change in import() behaviour for Perl > 5.39.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 03 2022 Petr Pisar <ppisar@redhat.com> - 0.033-1
- 0.033 bump

* Wed Aug 17 2022 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Fri Aug 05 2022 Petr Pisar <ppisar@redhat.com> - 0.031-1
- 0.031 bump
- Rename perl-Attean-tests to perl-Test-Attean and package upstream tests into
  perl-Attean-tests

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.030-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.030-5
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.030-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.030-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.030-2
- Perl 5.34 rebuild

* Mon Feb 08 2021 Petr Pisar <ppisar@redhat.com> - 0.030-1
- 0.030 bump

* Tue Feb 02 2021 Petr Pisar <ppisar@redhat.com> - 0.029-1
- 0.029 bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.028-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.028-1
- 0.028 bump

* Mon Nov 09 2020 Petr Pisar <ppisar@redhat.com> - 0.027-1
- 0.027 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-2
- Perl 5.32 rebuild

* Thu Feb 20 2020 Petr Pisar <ppisar@redhat.com> - 0.026-1
- 0.026 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Petr Pisar <ppisar@redhat.com> - 0.025-1
- 0.025 bump

* Mon Sep 23 2019 Petr Pisar <ppisar@redhat.com> - 0.024-1
- 0.024 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.023-2
- Perl 5.30 rebuild

* Thu May 02 2019 Petr Pisar <ppisar@redhat.com> - 0.023-1
- 0.023 bump

* Fri Mar 22 2019 Petr Pisar <ppisar@redhat.com> - 0.022-1
- 0.022 bump

* Mon Feb 18 2019 Petr Pisar <ppisar@redhat.com> - 0.021-1
- 0.021 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Petr Pisar <ppisar@redhat.com> - 0.020-1
- 0.020 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.019-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.019-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Petr Pisar <ppisar@redhat.com> - 0.019-1
- 0.019 bump

* Thu Jan 11 2018 Petr Pisar <ppisar@redhat.com> - 0.018-2
- Provide Perl module collections as an RPM symbol

* Mon Jan 08 2018 Petr Pisar <ppisar@redhat.com> 0.018-1
- Specfile autogenerated by cpanspec 1.78.
