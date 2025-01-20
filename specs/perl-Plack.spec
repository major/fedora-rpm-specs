# Build with apache2 tests enabled
# - works in local mocks, but fails in Fedora's koji.
# - requires customized apache setup with apache >= 2.4.
# Default to not testing apache2.
%bcond_with apache

# Use Devel::StackTrace::WithLexicals for catching exceptions.
%bcond_without perl_Plack_enables_Devel_StackTrace_WithLexicals

# Build with FCGI support
%bcond_without perl_Plack_enables_fcgi

# Use XS HTTP parser. This can be disabled with PLACK_HTTP_PARSER_PP=1
# environment variable at run time.
%bcond_without perl_Plack_enables_HTTP_Parser_XS

# Build with mod_perl support for Apache HTTP server version 1.
# Abandoned/Unsupported in Fedora.
%bcond_with perl_Plack_enables_httpd1

# Build with mod_perl support for Apache HTTP server version 2.
# Abandoned/Unsupported in Fedora.
%bcond_without perl_Plack_enables_httpd2

# Recommends IPv6 support to HTTP::Server::PSGI embedded web server
%bcond_without perl_Plack_enables_ipv6

# Build with support for logging through Log::Log4perl
%bcond_without perl_Plack_enables_log4perl

# Test log middleware for Log::Log4perl and Log::Dispatch
%bcond_without perl_Plack_enables_log_test

# Suggest SSL support to HTTP::Server::PSGI embedded web server
%bcond_without perl_Plack_enables_ssl

Name:           perl-Plack
Version:        1.0051
Release:        5%{?dist}
Summary:        Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-%{version}.tar.gz
# Adapt tests to Fedora's httpd 2.4
Patch0:         Plack-1.0047-Update-Apache-2-handler-tests-to-httpd-2.4.patch
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.12.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
%if %{with perl_Plack_enables_httpd1}
BuildRequires:  perl(Apache::Constants)
BuildRequires:  perl(Apache::Request)
%endif
BuildRequires:  perl(Apache::LogFormat::Compiler) >= 0.33
%if %{with perl_Plack_enables_httpd2}
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::Log)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::Response)
BuildRequires:  perl(APR::Table)
%endif
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI::Compile) >= 0.03
BuildRequires:  perl(CGI::Emulate::PSGI) >= 0.10
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cookie::Baker) >= 0.07
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::StackTrace) >= 1.23
BuildRequires:  perl(Devel::StackTrace::AsHTML) >= 0.11
%if %{with perl_Plack_enables_Devel_StackTrace_WithLexicals}
BuildRequires:  perl(Devel::StackTrace::WithLexicals) >= 0.8
%endif
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
%if %{with perl_Plack_enables_fcgi}
# FCGI not used at tests
# FCGI::ProcManager not used at tests
%endif
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Filesys::Notify::Simple)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::MultiValue) >= 0.05
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Entity::Parser) >= 0.25
# HTTP::Headers version from HTTP::Message in META
BuildRequires:  perl(HTTP::Headers) >= 5.814
BuildRequires:  perl(HTTP::Headers::Fast) >= 0.18
%if %{with perl_Plack_enables_HTTP_Parser_XS}
BuildRequires:  perl(HTTP::Parser::XS)
%endif
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(HTTP::Tiny) >= 0.03
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
# IO::Socket::IP not used at tests
# IO::Socket::SSL not used at tests
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
%if %{with perl_Plack_enables_log_test} && %{with perl_Plack_enables_log4perl}
BuildRequires:  perl(Log::Log4perl)
%endif
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Refresh)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage) >= 1.36
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
%if %{with perl_Plack_enables_fcgi}
# Server::Starter not used at tests
%endif
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Stream::Buffered) >= 0.02
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::TCP) >= 2.15
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.59
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Form::UrlEncoded) >= 0.23

# tests
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Authen::Simple::Passwd)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::AsCGI) >= 1.2
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle::Util)
%if %{with perl_Plack_enables_fcgi}
BuildRequires:  perl(IO::Socket)
%endif
%if %{with perl_Plack_enables_log_test}
BuildRequires:  perl(Log::Dispatch) >= 2.25
BuildRequires:  perl(Log::Dispatch::Array) >= 1.001
%endif
BuildRequires:  perl(LWP::Protocol::http10)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Types)
# Test::Pod 1.41 not used
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
# FCGI::Client not used

%if %{with perl_Plack_enables_httpd2}
# For mod_perl.so
BuildRequires:  mod_perl >= 2

# For httpd tests
BuildRequires:  /usr/sbin/httpd
%endif

%if %{with perl_Plack_enables_fcgi}
# For lighttpd tests, not used, RELEASE_TESTING only
# /usr/sbin/lighttpd
# lighttpd-fastcgi
%endif

Requires:       perl(Apache::LogFormat::Compiler) >= 0.33
Requires:       perl(CGI::Compile) >= 0.03
Requires:       perl(CGI::Emulate::PSGI) >= 0.10
Requires:       perl(Cookie::Baker) >= 0.07
Requires:       perl(Devel::StackTrace) >= 1.23
Requires:       perl(Devel::StackTrace::AsHTML) >= 0.11
%if %{with perl_Plack_enables_Devel_StackTrace_WithLexicals}
Suggests:       perl(Devel::StackTrace::WithLexicals) >= 0.8
%endif
Requires:       perl(File::Basename)
Requires:       perl(Filesys::Notify::Simple)
Requires:       perl(Getopt::Long)
Requires:       perl(Hash::MultiValue) >= 0.05
Requires:       perl(HTTP::Entity::Parser) >= 0.17
# HTTP::Headers version from HTTP::Message in META
Requires:       perl(HTTP::Headers) >= 5.814
Requires:       perl(HTTP::Headers::Fast) >= 0.18
%if %{with perl_Plack_enables_HTTP_Parser_XS}
Recommends:     perl(HTTP::Parser::XS)
%endif
Requires:       perl(HTTP::Tiny) >= 0.03
%if %{with perl_Plack_enables_ssl}
Suggests:       perl(IO::Socket::SSL)
%endif
%if %{with perl_Plack_enables_ipv6}
Recommends:     perl(IO::Socket::IP)
%endif
Requires:       perl(lib)
Requires:       perl(Pod::Usage) >= 1.36
Requires:       perl(Stream::Buffered) >= 0.02
Requires:       perl(URI) >= 1.59
Requires:       perl(WWW::Form::UrlEncoded) >= 0.23

# Remove under-specified dependenics
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Apache::LogFormat::Compiler|CGI::Compile|CGI::Emulate::PSGI|Cookie::Baker|Devel::StackTrace|Devel::StackTrace::AsHTML|File::ShareDir|Hash::MultiValue|HTTP::Entity::Parser|HTTP::Headers|HTTP::Headers::Fast|HTTP::Tiny|Stream::Buffered|Test::More|Test::TCP|URI|WWW::Form::UrlEncoded)\\)$

%description
Plack is a set of tools for using the PSGI stack. It contains middleware
components, a reference server and utilities for Web application
frameworks. Plack is like Ruby's Rack or Python's Paste for WSGI.

%if %{with perl_Plack_enables_httpd1}
%package Handler-Apache1
Summary:    Plack handler for mod_perl in Apache HTTP server version 1
Requires:   perl-Plack = %{version}-%{release}

%description Handler-Apache1
%{summary}.
%endif

%if %{with perl_Plack_enables_httpd2}
%package Handler-Apache2
Summary:    Plack handler for mod_perl in Apache HTTP server version 2
Requires:   perl-Plack = %{version}-%{release}
Requires:   perl(URI) >= 1.59

%description Handler-Apache2
%{summary}.
%endif

%if %{with perl_Plack_enables_fcgi}
%package Handler-FCGI
Summary:    Plack handler for FastCGI
Requires:   perl-Plack = %{version}-%{release}
# FCGI handler needs FCGI::ProcManager by default
Requires:   perl(FCGI::ProcManager)
# Server::Starter is used only of Plack is executed from Server::Starter. No
# need for declaring the dependency.
Requires:   perl(URI) >= 1.59

%description Handler-FCGI
%{summary}.
%endif

%if %{with perl_Plack_enables_log4perl}
%package Middleware-Log4perl
Summary:    Plack middleware for logging through Log::Log4perl
Requires:   perl-Plack = %{version}-%{release}
Requires:   perl(Log::Log4perl)

%description Middleware-Log4perl
%{summary}.
%endif

%package Test
Summary:    Test-modules for perl-Plack
Requires:   perl-Plack = %{version}-%{release}
Requires:   perl(File::ShareDir) >= 1.00
Requires:   perl(Test::More) >= 0.88
Requires:   perl(Test::TCP) >= 2.15

%description Test
%{summary}.

%prep
%setup -q -n Plack-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} "$RPM_BUILD_ROOT"/*

%check
unset AUTHOR_TESTING PLACK_HTTP_PARSER_PP RELEASE_TESTING
export TEST_APACHE1=0%{?with_perl_Plack_enables_httpd1:1}
export TEST_APACHE2=0%{?with_perl_Plack_enables_httpd2:1}
%if ! %{with apache}
export TEST_APACHE1=0
export TEST_APACHE2=0
%endif
%{__make} test

%files
%doc Changes README
%{_bindir}/plackup
%{_mandir}/man1/plackup.*
%{perl_vendorlib}/Plack
%{perl_vendorlib}/Plack.pm
%{perl_vendorlib}/HTTP
# Abandoned/Unsupported in Fedora: Apache1
%exclude %{perl_vendorlib}/Plack/Handler/Apache1.pm
%exclude %{_mandir}/man3/Plack::Handler::Apache1.3pm*
# Packaged separately in perl-Plack-Handler-Apache2
%exclude %{perl_vendorlib}/Plack/Handler/Apache2*
%exclude %{_mandir}/man3/Plack::Handler::Apache2*
# Packaged separately in perl-Plack-Handler-FCGI
%exclude %{perl_vendorlib}/Plack/Handler/FCGI.pm
%exclude %{_mandir}/man3/Plack::Handler::FCGI.3pm*
# Packaged separatelt in perl-Plack-Middleware-Log4perl
%exclude %{perl_vendorlib}/Plack/Middleware/Log4perl.pm
%exclude %{_mandir}/man3/Plack::Middleware::Log4perl.3pm*
# Packaged separately in perl-Plack-Test
%exclude %{perl_vendorlib}/Plack/Test
%exclude %{perl_vendorlib}/Plack/Test.pm
%exclude %{perl_vendorlib}/auto/*
%exclude %{_mandir}/man3/Plack::Test*

%{_mandir}/man3/*

%if %{with perl_Plack_enables_httpd1}
%files Handler-Apache1
%{perl_vendorlib}/Plack/Handler/Apache1.pm
%{_mandir}/man3/Plack::Handler::Apache1.3pm*
%endif

%if %{with perl_Plack_enables_httpd2}
%files Handler-Apache2
%{perl_vendorlib}/Plack/Handler/Apache2*
%{_mandir}/man3/Plack::Handler::Apache2*
%endif

%if %{with perl_Plack_enables_fcgi}
%files Handler-FCGI
%{perl_vendorlib}/Plack/Handler/FCGI.pm
%{_mandir}/man3/Plack::Handler::FCGI.3pm*
%endif

%if %{with perl_Plack_enables_log4perl}
%files Middleware-Log4perl
%{perl_vendorlib}/Plack/Middleware/Log4perl.pm
%{_mandir}/man3/Plack::Middleware::Log4perl.3pm*
%endif

%files Test
%{_mandir}/man3/Plack::Test*
%dir %{perl_vendorlib}/Plack
%{perl_vendorlib}/Plack/Test
%{perl_vendorlib}/Plack/Test.pm
# Used by Plack/Test/Suite.pm
%{perl_vendorlib}/auto/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0051-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0051-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0051-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0051-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0051-1
- Update to 1.0051.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0050-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0050-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0050-2
- Convert license to SPDX.

* Mon Sep 12 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0050-1
- Upstream update.
- Modernize spec.
- Drop --skipdeps.
- Drop BR: /usr/bin/python.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0048-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.0048-7
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0048-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0048-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.0048-4
- Perl 5.34 rebuild

* Thu May 06 2021 Petr Pisar <ppisar@redhat.com>, Jitka Plesnikova <jplesnik@redhat.com> - 1.0048-3
- Specify all dependencies
- Move Apache httpd 2 mod_perl handler to perl-Plack-Handler-Apache2
- Move FCGI handler to perl-Plack-Handler-FCGI
- Move Log::Log4Perl middleware to perl-Plack-Middleware-Log4perl

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0048-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0048-1
- Update to 1.0048.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0047-9
- Perl 5.32 rebuild

* Wed Mar 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0047-8
- Add perl(DirHandle) needed for build

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0047-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0047-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0047-2
- Perl 5.28 rebuild

* Sun Feb 18 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0047-1
- Update to 1.0047.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0045-3
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0045-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0045-1
- Update to 1.0045.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0044-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.0044-2
- Perl 5.26 rebuild

* Fri Apr 28 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0044-1
- Update to 1.0044.

* Thu Feb 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0043-1
- Update to 1.0043.
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0042-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 01 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0042-1
- Update to 1.0042 (RHBZ#1382923).
- Spec cleanup.

* Sat Oct 08 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0039-2
- Preps for Plack-1.0042.

* Sat Jun 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0039-1
- Update to 1.0039.
- Cleanup BRs.

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0034-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0034-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0034-5
- Merge preps for pending upstream updates:
  - Preps for 1.0039:
    - BR: perl(HTTP::Headers::Fast) >= 0.18.
  - Preps for 1.0038:
    - BR: perl(HTTP::Headers::Fast) >= 0.20.
  - Preps for 1.0037:
    - BR: perl(HTTP::Headers::Fast) >= 0.18.
  - Preps for 1.0036:
    - BR: perl(Cookie::Baker), perl(HTTP::Headers::Fast).

* Fri Jan 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0034-4
- Modernize spec.
- Remove ref to %%{perl_vendorlib}/Plack/Server/Apache1.pm.
- Exclude stray %%{_mandir}/man3/Plack::Handler::Apache1.3pm* manpage.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0034-2
- Perl 5.22 rebuild

* Wed Feb 04 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0034-1
- Upstream update.

* Mon Oct 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0033-1
- Upstream update.

* Mon Oct 13 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0032-1
- Upstream update.

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0031-2
- Perl 5.20 rebuild

* Fri Aug 08 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0031-1
- Upstream update.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0030-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0030-3
- Move misplaced %%exclude-line from base-package to *-Test.

* Wed Jan 15 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0030-2
- Split out perl-Plack-Test to avoid dependency on Test::More (RHBZ #1052859).

* Mon Dec 30 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0030-1
- Upstream update.

* Wed Sep 18 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0029-1
- Upstream update.
- Update BRs.
- Modernize spec.

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.0022-3
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0022-1
- Upstream update.
- Add BR: perl(File::ShareDir::Install).
- Add BR: perl(Stream::Buffered).
- Remove perl-Plack-1.0004.patch (Not required anymore).
- Preps for Plack > 1.0022.

* Mon Feb 18 2013 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0004-3
- Fix changelog dates (Fedora_19_Mass_Rebuild FTBFS).
- Add perl-Plack-1.0004.patch.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0004-1
- Upstream update.

* Sun Sep 16 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0003-1
- Upstream update.

* Thu Aug 16 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0002-1
- Upstream update.

* Mon Jul 30 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 1.0001-1
- Upstream update.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9989-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 0.9989-2
- Perl 5.16 rebuild

* Wed Jun 27 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9989-1
- Upstream update.

* Mon May 21 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9988-1
- Upstream update.

* Mon Mar 19 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9986-1
- Upstream update.

* Wed Jan 18 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9985-3
- Activate optional BR: perl(Devel::StackTrace::WithLexicals).
- Activate optional BR: perl(LWP::Protocol::http10).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9985-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9985-1
- Upstream update.

* Fri Oct 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9984-2
- Add %%bcond_with apache to work around building failures in koji.

* Thu Oct 13 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9984-1
- Upstream update.

* Fri Aug 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9982-1
- Upstream update.

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.9980-2
- Perl mass rebuild

* Wed Jun 08 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9980-1
- Upstream update.

* Thu May 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9979-1
- Upstream update.
- Activate lighttpd and lighttpd-fcgi tests.

* Wed May 11 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9978-1
- Upstream update.

* Mon May 02 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9977-1
- Upstream update.

* Sun Apr 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9976-1
- Upstream update.

* Mon Mar 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9974-2
- Reflect HTTP-Server-Simple-PSGI having entered Fedora
  (Add BR: perl(HTTP::Server::Simple::PSGI)).

* Mon Mar 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9974-1
- Upstream update.

* Thu Mar 03 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9973-1
- Upstream update.
- Reflect upstream not shipping Plack/Handler/Net/FastCGI.pm anymore.
- Spec file cleanup.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9967-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9967-1
- Upstream update.

* Tue Jan 25 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9964-1
- Upstream update.

* Tue Jan 18 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9963-1
- Upstream update.
- Hack around incorrect hard-coded path to mod_perl.so.
- Activate Apache2 test.

* Mon Jan 03 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9960-1
- Upstream update.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9959-2
- Re-add %%{perl_vendorlib}/auto/*jpg (Used by Plack/Test).
- Add BR: perl(Authen::Simple::Passwd).
- Add BR: perl(CGI::Emulate::PSGI).

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9959-1
- Update to 0.9959.

* Tue Dec 21 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.9958-1
- Initial Fedora package.
