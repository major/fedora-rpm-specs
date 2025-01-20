Name:           perl-HTTP-OAI
Version:        4.13
Release:        6%{?dist}
Summary:        API for OAI-PMH
License:        BSD-3-Clause
URL:            https://metacpan.org/release/HTTP-OAI
Source0:        https://cpan.metacpan.org/authors/id/H/HO/HOCHSTEN/HTTP-OAI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
# CGI not used, bin/oai_static_gateway.pl is never executed
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode) >= 2.12
BuildRequires:  perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(LWP::MemberMixin)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(overload)
# Pod::Usage not uset at tests
BuildRequires:  perl(POSIX)
# Term::ReadKey not used at tests
# Term::ReadLine not used at tests
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::LibXML) >= 1.60
BuildRequires:  perl(XML::LibXML::SAX)
BuildRequires:  perl(XML::LibXML::SAX::Builder)
BuildRequires:  perl(XML::LibXML::SAX::Parser)
BuildRequires:  perl(XML::LibXML::XPathContext)
BuildRequires:  perl(XML::NamespaceSupport)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base) >= 1.04
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::SAX::Writer)
# Tests:
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.99
Requires:       perl(Encode) >= 2.12
Requires:       perl(Term::ReadLine)
Requires:       perl(Term::ReadKey)
Requires:       perl(XML::LibXML) >= 1.60
Requires:       perl(XML::SAX::Base) >= 1.04

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Encode|Test::More|XML::LibXML|XML::SAX::Base)\\)$
# Hide prive modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(XML::SAX::Debug\\)

%description
These are Perl modules and tools implementing Open Archives Initiative
Protocol for Metadata Harvesting (OAI-PMH).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.99
Requires:       perl(XML::LibXML) >= 1.60
Requires:       perl(XML::SAX)
Requires:       perl(XML::SAX::Base) >= 1.04
Requires:       perl(XML::SAX::ParserFactory)
Requires:       perl(XML::SAX::Writer)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n HTTP-OAI-%{version}
# Remove always skipped author tests
rm t/author-pod-syntax.t
perl -i -ne 'print $_ unless m{^t/author-pod-syntax.t}' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a examples t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset HTTP_OAI_AGENT HTTP_OAI_NETTESTS HTTP_OAI_SAX_TRACE HTTP_OAI_TRACE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc bin/oai_static_gateway.pl Changes README
%{_bindir}/oai_browser.pl
%{_bindir}/oai_pmh.pl
%dir %{perl_vendorlib}/HTTP
%{perl_vendorlib}/HTTP/OAI
%{perl_vendorlib}/HTTP/OAI.pm
%{_mandir}/man1/oai_browser.pl.*
%{_mandir}/man1/oai_pmh.pl.*
%{_mandir}/man3/HTTP::OAI.*
%{_mandir}/man3/HTTP::OAI::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 06 2023 Petr Pisar <ppisar@redhat.com> - 4.13-1
- 4.13 bump

* Fri Jun 02 2023 Petr Pisar <ppisar@redhat.com> - 4.12-1
- 4.12 bump
- Package the tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.10-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.10-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.10-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.10-1
- 4.10 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.08-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.08-1
- 4.08 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.07-2
- Perl 5.28 rebuild

* Mon Jun 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.07-1
- 4.07 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-1
- 4.06 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-1
- 4.05 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-2
- Perl 5.26 rebuild

* Wed Feb 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-1
- 4.04 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.03-4
- Perl 5.24 rebuild

* Fri Feb 05 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.03-3
- Add BR: perl(Test) (Fix F23FTBFS).
- Modernize spec.
- Add %%license.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 4.03-1
- New upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.27-8
- Perl 5.22 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 3.27-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 3.27-1
- tidying of spec file
- new upstream release 3.27
* Thu Apr 28 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 3.24-1
- Specfile autogenerated by cpanspec 1.78.
