# Supported rpmbuild options:
#
# --with live-test/--without live-test
#   include/exclude LIVE_TEST testsuite
#   Default: --without (Requires networking, doesn't work in mock)
%bcond_with     live_test

Name:           perl-Web-Scraper
Version:        0.38
Release:        32%{?dist}
Summary:        Web Scraping Toolkit using HTML and CSS Selectors or XPath expressions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Web-Scraper
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Web-Scraper-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Selector::XPath) >= 0.03
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTML::TreeBuilder) >= 3.23
BuildRequires:  perl(HTML::TreeBuilder::XPath) >= 0.08
BuildRequires:  perl(HTML::TreeBuilder::LibXML) >= 0.13
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP) >= 5.827
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::XPathEngine) >= 0.08
BuildRequires:  perl(YAML)
BuildRequires:  perl(strict)

# Required by the testsuite
BuildRequires:  /usr/bin/ps


# rpm's deptracker misses these:
Requires:  perl(LWP::UserAgent)

%{?perl_default_filter}

%description
Web::Scraper is a web scraper toolkit, inspired by Ruby's equivalent
Scrapi. It provides a DSL-ish interface for traversing HTML documents and
returning a neatly arranged Perl data structure.

%prep
%setup -q -n Web-Scraper-%{version}

# Package does not depend on ExtUtils::MakeMaker
sed -i '/ExtUtils::MakeMaker/d' META.*

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

# Web-Scraper >= 0.38 misses to install bin/scaper
# Install it manually
install -m 755 -d ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 bin/scraper ${RPM_BUILD_ROOT}%{_bindir}

%{_fixperms} $RPM_BUILD_ROOT/*

%check
LEAK_TEST=1 %{?with_live_test:LIVE_TEST=1} ./Build test

%files
%doc Changes README
%{_bindir}/scraper
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-26
- Spec file cosmetics.

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-25
- Convert licence to SPDX.
- Update sources to sha512.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-23
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-20
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-14
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Petr Pisar <ppisar@redhat.com> - 0.38-4
- Correct dependency on ps tool

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-2
- Perl 5.22 rebuild

* Thu Oct 23 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-1
- Upstream update.
- Fix bogus %%changelog entry.
- Reflect upstream having changed to Build.PL.
- Work-around to upstream having missed to install bin/scrapper.

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.37-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.37-1
- Upstream update.

* Tue Aug 07 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.36-2
- R: perl(LWP::UserAgent).
- Make live tests working (Add Web-Scraper-0.36-testsuite-hacks.patch).
- BR: /bin/ps.

* Tue Jul 10 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.36-1.20120710.0
- Merge in Xavier's spec.

* Sat Jan 21 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.36-1.20120121.0
- More deps.
- Add %%{?perl_default_filter}.

* Mon Dec 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.36-1
- Upstream update.
- Add --with/without live-test (disabled by default).

* Wed Mar 30 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.34-1
- Upstream update.
- Spec cleanup.

* Tue Dec 21 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.32-1
- Initial Fedora package.
