# Run optional tests
%bcond_without perl_libwww_perl_enables_optional_test
# Perform tests that need the Internet
%bcond_with perl_libwww_perl_enables_internet_test

Name:           perl-libwww-perl
Version:        6.79
Release:        2%{?dist}
Summary:        A Perl interface to the World-Wide Web
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/libwww-perl
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/libwww-perl-%{version}.tar.gz
# Normalize shelbangs, not suitable for an upstream
Patch0:         libwww-perl-6.39-Normalize-shebangs-in-examples.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time:
# Authen::NTLM 1.02 not used at tests
BuildRequires:  perl(Carp)
# Data::Dump 1.13 not used at tests
# Data::Dump::Trace not used at tests
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode) >= 2.12
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
# Fcntl not used at tests
# File::Listing 6 not used at tests
# File::Spec not used at tests
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::HeadParser) => 3.71
BuildRequires:  perl(HTTP::Config)
BuildRequires:  perl(HTTP::Cookies) >= 6
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Headers::Util)
# HTTP::Negotiate 6 not used at tests
BuildRequires:  perl(HTTP::Request) >= 6.18
BuildRequires:  perl(HTTP::Request::Common) >= 6.18
BuildRequires:  perl(HTTP::Response) >= 6.18
BuildRequires:  perl(HTTP::Status) >= 6.18
# integer not used at tests
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(LWP::MediaTypes) >= 6
# Mail::Internet not needed
BuildRequires:  perl(MIME::Base64) >= 2.1
BuildRequires:  perl(Module::Load)
# Net::FTP 2.58 not used at tests
BuildRequires:  perl(Net::HTTP) >= 6.18
# Net::NNTP not used at tests
BuildRequires:  perl(parent) >= 0.217
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(URI::Escape)
# URI::Heuristic not used at tests
BuildRequires:  perl(WWW::RobotRules) >= 6
# Optional run-time:
# CPAN::Config not used at tests
# HTML::Parse not used at tests

# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::CookieJar::LWP)
BuildRequires:  perl(HTTP::Daemon) >= 6.01
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
%if %{with perl_libwww_perl_enables_internet_test}
BuildRequires:  perl(Test::RequiresInternet)
%endif
BuildRequires:  perl(utf8)
%if %{with perl_libwww_perl_enables_internet_test}
BuildRequires:  perl(Test::Needs)
%if %{with perl_libwww_perl_enables_optional_test}
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
BuildRequires:  perl(Test::LeakTrace)
%endif
%endif

Requires:       perl(Authen::NTLM) >= 1.02
Suggests:       perl(CPAN::Config)
Requires:       perl(Encode) >= 2.12
Requires:       perl(File::Spec)
Requires:       perl(File::Listing) >= 6
# Keep HTML::FormatPS optional
Suggests:       perl(HTML::FormatPS)
# Keep HTML::FormatText optional
Suggests:       perl(HTML::FormatText)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::HeadParser)
Suggests:       perl(HTML::Parse)
Requires:       perl(HTTP::Config)
Requires:       perl(HTTP::Cookies) >= 6
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Headers::Util)
Requires:       perl(HTTP::Negotiate) >= 6
Requires:       perl(HTTP::Request) >= 6.18
Requires:       perl(HTTP::Request::Common) >= 6.18
Requires:       perl(HTTP::Response) >= 6.18
Requires:       perl(HTTP::Status) >= 6.18
Requires:       perl(LWP::MediaTypes) >= 6
Suggests:       perl(LWP::Protocol::https) >= 6.02
Requires:       perl(MIME::Base64) >= 2.1
Requires:       perl(Net::FTP) >= 2.58
Requires:       perl(Net::HTTP) >= 6.18
Requires:       perl(URI) >= 1.10
Requires:       perl(URI::Escape)
Requires:       perl(WWW::RobotRules) >= 6
Provides:       perl(LWP::Debug::TraceHTTP::Socket) = %{version}
Provides:       perl(LWP::Protocol::http::Socket) = %{version}
Provides:       perl(LWP::Protocol::http::SocketMethods) = %{version}

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Authen::NTLM|Encode|File::Listing|HTTP::Cookies|HTTP::Daemon|HTTP::Date|HTTP::Negotiate|HTTP::Request|HTTP::Response|HTTP::Status|LWP::MediaTypes|MIME::Base64|Net::FTP|Net::HTTP|Test::More|URI|WWW::RobotRules)\\)$

%description
The libwww-perl collection is a set of Perl modules which provides a simple and
consistent application programming interface to the World-Wide Web.  The main
focus of the library is to provide classes and functions that allow you to
write WWW clients. The library also contain modules that are of more general
use and even classes that help you implement simple HTTP servers.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(HTTP::Cookies) >= 6
Requires:       perl(HTTP::CookieJar::LWP)
Requires:       perl(HTTP::Daemon) >= 6.01
Requires:       perl(HTTP::Request) >= 6.18
Requires:       perl(HTTP::Response) >= 6.18
Requires:       perl(Net::HTTP) >= 6.18
Requires:       perl(Test::More) >= 0.96
%if %{with perl_libwww_perl_enables_internet_test} && %{with perl_libwww_perl_enables_optional_test}
Requires:       perl(Test::LeakTrace)
%endif
Requires:       perl(URI) >= 1.10
Suggests:       perl(JSON::PP) => 2.27300

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n libwww-perl-%{version} 
%patch -P 0 -p1
%if !%{with perl_libwww_perl_enables_internet_test}
rm t/base/protocols/nntp.t t/leak/no_leak.t t/redirect.t
perl -i -ne 'print $_ unless m{^(?:t/base/protocols/nntp\.t|t/leak/no_leak\.t|t/redirect\.t)}' MANIFEST
%endif
# Help generators to recognize a Perl code
for F in $(find t -name '*.t') talk-to-ourself; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
# Install the aliases by default
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 --aliases < /dev/null
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t talk-to-ourself %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/local/http.t writes to CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset COVERAGE PERL_LWP_ENV_HTTP_TEST_SERVER_TIMEOUT PERL_LWP_ENV_HTTP_TEST_URL
prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset COVERAGE PERL_LWP_ENV_HTTP_TEST_SERVER_TIMEOUT PERL_LWP_ENV_HTTP_TEST_URL
make test

%files
%license LICENSE
%doc Changes examples README.SSL
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 03 2025 Michal Josef Špaček <mspacek@redhat.com> - 6.79-1
- 6.79 bump (rhbz#2375525)

* Tue Feb 25 2025 Michal Josef Špaček <mspacek@redhat.com> - 6.78-1
- 6.78 bump (rhbz#2346731)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 11 2024 Michal Josef Špaček <mspacek@redhat.com> - 6.77-1
- 6.77 bump

* Mon Jan 29 2024 Michal Josef Špaček <mspacek@redhat.com> - 6.76-1
- 6.76 bump

* Tue Jan 23 2024 Michal Josef Špaček <mspacek@redhat.com> - 6.74-1
- 6.74 bump

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Michal Josef Špaček <mspacek@redhat.com> - 6.73-1
- 6.73 bump

* Tue Jul 25 2023 Michal Josef Špaček <mspacek@redhat.com> - 6.72-1
- 6.72 bump

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 22 2023 Michal Josef Špaček <mspacek@redhat.com> - 6.71-1
- 6.71 bump

* Tue May 16 2023 Michal Josef Špaček <mspacek@redhat.com> - 6.70-1
- 6.70 bump
- Fix %patch macro

* Wed Mar 01 2023 Michal Josef Špaček <mspacek@redhat.com> - 6.68-1
- 6.68 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Michal Josef Špaček <mspacek@redhat.com> - 6.67-3
- Update license to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Michal Josef Špaček <mspacek@redhat.com> - 6.67-1
- 6.67 bump

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.66-2
- Perl 5.36 rebuild

* Thu May 19 2022 Michal Josef Špaček <mspacek@redhat.com> - 6.66-1
- 6.66 bump

* Tue May 10 2022 Michal Josef Špaček <mspacek@redhat.com> - 6.65-1
- 6.65 bump

* Wed Apr 27 2022 Michal Josef Špaček <mspacek@redhat.com> - 6.64-1
- 6.64 bump

* Tue Apr 26 2022 Michal Josef Špaček <mspacek@redhat.com> - 6.63-1
- 6.63 bump

* Tue Apr 05 2022 Michal Josef Špaček <mspacek@redhat.com> - 6.62-1
- 6.62 bump

* Tue Feb 08 2022 Michal Josef Špaček <mspacek@redhat.com> - 6.61-1
- 6.61 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Michal Josef Špaček <mspacek@redhat.com> - 6.60-1
- 6.60 bump

* Mon Nov 01 2021 Michal Josef Špaček <mspacek@redhat.com> - 6.58-1
- 6.58 bump

* Tue Sep 21 2021 Michal Josef Špaček <mspacek@redhat.com> - 6.57-1
- 6.57 bump

* Fri Aug 20 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.56-1
- 6.56 bump

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.55-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Michal Josef Špaček <mspacek@redhat.com> - 6.55-1
- 6.55 bump

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.54-2
- Perl 5.34 rebuild

* Thu May 06 2021 Michal Josef Špaček <mspacek@redhat.com> - 6.54-1
- 6.54 bump
- Unify build root to macro usage only

* Tue Mar 09 2021 Petr Pisar <ppisar@redhat.com> - 6.53-2
- Package talk-to-ourself script with the tests

* Mon Mar 08 2021 Petr Pisar <ppisar@redhat.com> - 6.53-1
- 6.53 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Petr Pisar <ppisar@redhat.com> - 6.52-1
- 6.52 bump

* Tue Jan 05 2021 Petr Pisar <ppisar@redhat.com> - 6.51-1
- 6.51 bump

* Thu Dec 17 2020 Petr Pisar <ppisar@redhat.com> - 6.50-1
- 6.50 bump

* Thu Sep 24 2020 Petr Pisar <ppisar@redhat.com> - 6.49-1
- 6.49 bump

* Mon Sep 21 2020 Petr Pisar <ppisar@redhat.com> - 6.48-1
- 6.48 bump

* Wed Aug 19 2020 Petr Pisar <ppisar@redhat.com> - 6.47-1
- 6.47 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.46-2
- Perl 5.32 re-rebuild updated packages

* Wed Jun 24 2020 Petr Pisar <ppisar@redhat.com> - 6.46-1
- 6.46 bump

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.45-2
- Perl 5.32 rebuild

* Tue Jun 09 2020 Petr Pisar <ppisar@redhat.com> - 6.45-1
- 6.45 bump

* Wed Apr 15 2020 Petr Pisar <ppisar@redhat.com> - 6.44-1
- 6.44 bump

* Fri Feb 14 2020 Petr Pisar <ppisar@redhat.com> - 6.43-3
- Do not perform tests that need the Internet by default

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Petr Pisar <ppisar@redhat.com> - 6.43-1
- 6.43 bump

* Thu Nov 21 2019 Petr Pisar <ppisar@redhat.com> - 6.42-1
- 6.42 bump

* Fri Nov 01 2019 Petr Pisar <ppisar@redhat.com> - 6.41-1
- 6.41 bump

* Fri Oct 25 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.40-1
- 6.40 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.39-2
- Perl 5.30 rebuild

* Tue May 07 2019 Petr Pisar <ppisar@redhat.com> - 6.39-1
- 6.39 bump

* Tue Mar 26 2019 Petr Pisar <ppisar@redhat.com> - 6.38-1
- 6.38 bump

* Thu Mar 07 2019 Petr Pisar <ppisar@redhat.com> - 6.37-1
- 6.37 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.36-1
- 6.36 bump

* Mon Jul 16 2018 Petr Pisar <ppisar@redhat.com> - 6.35-1
- 6.35 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.34-2
- Perl 5.28 rebuild

* Wed Jun 06 2018 Petr Pisar <ppisar@redhat.com> - 6.34-1
- 6.34 bump

* Tue Feb 27 2018 Petr Pisar <ppisar@redhat.com> - 6.33-1
- 6.33 bump

* Wed Feb 21 2018 Petr Pisar <ppisar@redhat.com> - 6.32-1
- 6.32 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Petr Pisar <ppisar@redhat.com> - 6.31-1
- 6.31 bump

* Mon Dec 11 2017 Petr Pisar <ppisar@redhat.com> - 6.30-1
- 6.30 bump

* Tue Nov 07 2017 Petr Pisar <ppisar@redhat.com> - 6.29-1
- 6.29 bump

* Fri Sep 22 2017 Petr Pisar <ppisar@redhat.com> - 6.27-2
- Provide hidden modules

* Fri Sep 22 2017 Petr Pisar <ppisar@redhat.com> - 6.27-1
- 6.27 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.26-2
- Perl 5.26 rebuild

* Thu Apr 13 2017 Petr Pisar <ppisar@redhat.com> - 6.26-1
- 6.26 bump

* Tue Apr 04 2017 Petr Pisar <ppisar@redhat.com> - 6.25-1
- 6.25 bump

* Wed Mar 15 2017 Petr Pisar <ppisar@redhat.com> - 6.24-1
- 6.24 bump

* Tue Mar 07 2017 Petr Pisar <ppisar@redhat.com> - 6.23-1
- 6.23 bump

* Thu Mar 02 2017 Petr Pisar <ppisar@redhat.com> - 6.22-1
- 6.22 bump

* Wed Feb 22 2017 Petr Pisar <ppisar@redhat.com> - 6.21-1
- 6.21 bump

* Thu Feb 16 2017 Petr Pisar <ppisar@redhat.com> - 6.19-2
- Accept proxy URLs with IPv6 host names (CPAN RT#94654)

* Wed Feb 15 2017 Petr Pisar <ppisar@redhat.com> - 6.19-1
- 6.19 bump

* Mon Feb 06 2017 Petr Pisar <ppisar@redhat.com> - 6.18-1
- 6.18 bump

* Wed Feb 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.17-1
- 6.17 bump

* Thu Jan 19 2017 Petr Pisar <ppisar@redhat.com> - 6.16-1
- 6.16 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.15-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Petr Pisar <ppisar@redhat.com> - 6.15-1
- 6.15 bump
- Add LWP::Protocol::https optional dependency on Suggests level

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.13-2
- Perl 5.22 rebuild

* Mon Feb 16 2015 Petr Pisar <ppisar@redhat.com> - 6.13-1
- 6.13 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.08-2
- Perl 5.20 rebuild

* Tue Jul 29 2014 Petr Pisar <ppisar@redhat.com> - 6.08-1
- 6.08 bump

* Mon Jul 07 2014 Petr Pisar <ppisar@redhat.com> - 6.07-1
- 6.07 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Petr Pisar <ppisar@redhat.com> - 6.06-1
- 6.06 bump
- Run tests against localhost (CPAN RT#94959)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 6.05-2
- Perl 5.18 rebuild

* Tue Mar 12 2013 Petr Pisar <ppisar@redhat.com> - 6.05-1
- 6.05 bump

* Fri Mar 08 2013 Petr Pisar <ppisar@redhat.com> - 6.04-5
- Honor time-out (bug #919448)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 6.04-2
- Perl 5.16 rebuild

* Mon Feb 20 2012 Petr Pisar <ppisar@redhat.com> - 6.04-1
- 6.04 bump

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Petr Pisar <ppisar@redhat.com> - 6.03-1
- 6.03 bump
- Remove RPM 4.8 dependecy filters

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 6.02-3
- RPM 4.9 dependency filtering added

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 6.02-2
- Perl mass rebuild

* Mon Mar 28 2011 Petr Pisar <ppisar@redhat.com> - 6.02-1
- 6.02 bump
- HTTPS support unbundled by upstream to break depency cycle in CPAN utilities.
  Install or depend on perl(LWP::Protocol::https) explicitly, if you need
  HTTPS support.

* Thu Mar 17 2011 Petr Pisar <ppisar@redhat.com> - 6.01-1
- 6.01 bump
- Remove BuildRoot stuff
- Remove unneeded hacks

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.837-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.837-2
- Add missing ':' to filter_from_requires perl(HTTP::GHTTP).
- filter_from_provides /perl(HTTP::Headers)$/d instead of /perl(HTTP::Headers)/d.

* Mon Sep 27 2010 Marcela Mašláňová <mmaslano@redhat.com> 5.837-1
- update

* Mon Jul 12 2010 Marcela Maslanova <mmaslano@redhat.com> - 5.836-1
- update

* Mon Jun 21 2010 Jesse Keating <jkeating@redhat.com> - 5.834-1
- Bump to match what was pushed to F13.

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 5.833-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 5.833-2
- rebuild against perl 5.10.1

* Fri Nov  6 2009 Marcela Mašláňová <mmaslano@redhat.com> 5.833-1
- update

* Thu Sep 17 2009 Warren Togami <cweyl@alumni.drew.edu> 5.831-1
- update to 5.831

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.825-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.825-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 5.825-1
- update to 5.825

* Thu Jan 22 2009 Marcela Mašláňová <mmaslano@redhat.com> 5.823-1
- update to 5.823

* Mon Oct 13 2008 Marcela Mašláňová <mmaslano@redhat.com> 5.817-1
- update to 5.817

* Tue Oct  7 2008 Marcela Mašláňová <mmaslano@redhat.com> 5.816-1
- update to 5.816
- fix #465855 - install --aliases by default
- use upstream patch for previous problem (see rt 38736)

* Thu Sep 18 2008 Marcela Maslanova <mmaslano@redhat.com> 5.814-2
- use untaint patch from Villa Skyte

* Thu Sep 18 2008 Marcela Maslanova <mmaslano@redhat.com> 5.814-1
- update to 5.814
- remove patch, now we have all upstream tests on

* Fri Mar  7 2008 Ville Skyttä <ville.skytta at iki.fi> - 5.808-7
- Use system /etc/mime.types instead of an outdated private copy.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.808-6
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.808-5
- rebuild for new perl

* Fri Oct 26 2007 Robin Norwood <rnorwood@redhat.com> - 5.808-4
- Fix various issues from package review:
- Fix tabs and spacing
- Remove unneeded BR: perl
- convert non-utf-8 files to utf-8
- Resolves: bz#226268

* Tue Aug 14 2007 Robin Norwood <rnorwood@redhat.com> - 5.808-3
- Make provides script filter out only the unversioned HTTP::Headers.

* Tue Aug 14 2007 Robin Norwood <rnorwood@redhat.com> - 5.808-2
- Disable some of the tests, with a long explanation.

* Mon Aug 13 2007 Robin Norwood <rnorwood@redhat.com> - 5.808-1
- Update to latest CPAN version
- Re-enable tests.  We'll see if they work now
- Move Requires filter into spec file
- Add Provides filter for unnecessary unversioned provides

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.805-1.1.1
- rebuild

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 5.805-1.1
- rebuild for new perl-5.8.8

* Mon Dec 19 2005 Jason Vas Dias<jvdias@redhat.com> - 5.805-1
- Upgrade to 5.805-1

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Sat Apr 02 2005 Warren Togami <wtogami@redhat.com> - 5.803-2
- skip make test (#150363)

* Sat Apr 02 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 5.803-1
- Update to 5.803.
- spec cleanup (#150363)

* Thu Nov 25 2004 Miloslav Trmac <mitr@redhat.com> - 5.79-6
- Convert man page to UTF-8

* Fri Aug 13 2004 Bill Nottingham <notting@redhat.com> 5.76-5
- fix %%defattr

* Mon Aug 09 2004 Alan Cox <alan@redhat.com> 5.76-4
- added missing BuildRequires on perl(HTML::Parser) [Steve Grubb]

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 16 2004 Warren Togami <wtogami@redhat.com> 5.76-2
- #12051 misc fixes from Ville Skyttä

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 5.76-1
- update to 5.76

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Tue Jul 16 2002 Chip Turner <cturner@redhat.com>
- added missing Requires on perl(HTML::Entities)

* Fri Mar 29 2002 Chip Turner <cturner@redhat.com>
- added Requires: for perl-URI and perl-Digest-MD5

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 7 2001 root <root@redhat.com>
- Spec file was autogenerated. 
