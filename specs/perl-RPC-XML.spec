# Support for mod_perl
%bcond_without perl_RPC_XML_enables_mod_perl
# Run optional tests
%bcond_without perl_RPC_XML_enables_optional_test

%global cpan_name RPC-XML

Name:       perl-%{cpan_name}
Version:    0.82
Release:    14%{?dist}
Summary:    Set of classes for core data, message and XML handling
# LGPL version and Artistic variant are clarified in README.license.
# etc/make_method:      Artistic-2.0 OR LGPL-2.1-only
# etc/rpc-method.dtd:   Artistic-2.0 OR LGPL-2.1-only
# lib/Apache/RPC/Server.pm: Artistic-2.0 OR LGPL-2.1-only
# lib/Apache/RPC/Status.pm: Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML.pm:   Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Client.pm:    Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Parser.pm:    Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/ParserFactory.pm: Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Parser/XMLLibXML.pm:  Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Parser/XMLParser.pm:  Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Procedure.pm:     Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Server.pm:    Artistic-2.0 OR LGPL-2.1-only
License:    Artistic-2.0 OR LGPL-2.1-only
URL:        https://metacpan.org/release/%{cpan_name}
Source0:    https://cpan.metacpan.org/authors/id/R/RJ/RJRAY/%{cpan_name}-%{version}.tar.gz
Source1:    README.license
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.56
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time without Apache stuff:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Daemon) >= 6.12
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Load) >= 0.36
# Keep Net::Server::MultiType optional, HTTP::Daemon is preferred
BuildRequires:  perl(Scalar::Util) >= 1.55
BuildRequires:  perl(subs)
BuildRequires:  perl(URI)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::LibXML) >= 1.85
BuildRequires:  perl(XML::Parser) >= 2.46
%if %{with perl_RPC_XML_enables_mod_perl}
# Run-time for Apache stuff:
BuildRequires:  perl(Apache)
BuildRequires:  perl(Apache::Constants)
BuildRequires:  perl(Apache::File)
BuildRequires:  perl(CGI)
# Socket not used at tests
%endif
# Recommended run-time:
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(DateTime) >= 1.54
BuildRequires:  perl(DateTime::Format::ISO8601) >= 0.15
# Tests:
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP) >= 6.51
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 1.302183
%if %{with perl_RPC_XML_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Net::Server)
%endif
Recommends:     perl(Compress::Zlib)
Requires:       perl(HTTP::Daemon) >= 6.12
Requires:       perl(MIME::Base64)
Requires:       perl(Module::Load) >= 0.36
Requires:       perl(Scalar::Util) >= 1.55
Requires:       perl(XML::Parser) >= 2.46
Requires:       perl(DateTime) >= 1.54
Requires:       perl(DateTime::Format::ISO8601) >= 0.15
Requires:       perl(XML::LibXML) >= 1.85

%{?perl_default_filter}
# Remove underspecified symbols
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((LWP|Module::Load|Scalar::Util|Test::More|XML::LibXML|XML::Parser)\\)\\s*$
# Hide private modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(BadParserClass\\)

%description
The RPC::XML package is an implementation of XML-RPC. The module provides
classes for sample client and server implementations, a server designed as an
Apache location-handler, and a suite of data-manipulation classes that are
used by them.

%if %{with perl_RPC_XML_enables_mod_perl}
%package -n perl-Apache-RPC
Summary:    Companion packages for RPC::XML tuned for mod_perl environments

%description -n perl-Apache-RPC
This package contains Apache::RPC::Server and Apache::RPC::Status, useful for
running RPC::XML under mod_perl.
%endif

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       coreutils
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with perl_RPC_XML_enables_mod_perl}
Requires:       perl-Apache-RPC = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires:       perl-Test-Harness
Requires:       perl(LWP) >= 6.51
Requires:       perl(Module::Load) >= 0.36
Requires:       perl(Test::More) >= 1.302183
%if %{with perl_RPC_XML_enables_optional_test}
Requires:       perl(Net::Server)
%endif
Requires:       perl(Scalar::Util) >= 1.55
Requires:       perl(XML::LibXML) >= 1.85

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -qn %{cpan_name}-%{version}
cp -p %{SOURCE1} .
%if !%{with perl_RPC_XML_enables_mod_perl}
rm -rf lib/Apache
perl -i -ln -e 'print unless qr{^lib/Apache/}' MANIFEST
%endif
# Normalize shebangs
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
#!/bin/bash
set -e
# Tests, e.g. t/11_base64_fh.t write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license README.license
%doc ChangeLog* README etc/*.dtd ex/ methods/
%{_mandir}/man3/RPC::XML.*
%{_mandir}/man3/RPC::XML::*
%{_mandir}/man1/make_method.*
%{_bindir}/make_method
%dir %{perl_vendorlib}/RPC
%{perl_vendorlib}/RPC/XML
%{perl_vendorlib}/RPC/XML.pm

%if %{with perl_RPC_XML_enables_mod_perl}
%files -n perl-Apache-RPC
%license README.license
%doc README.apache2
%{_mandir}/man3/Apache::RPC::*
%dir %{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache/RPC
%endif

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 31 2024 Petr Pisar <ppisar@redhat.com> - 0.82-13
- Convert license tag to SPDX
- Properly declare an optional dependency on Compress::Zlib
- Package the tests

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Petr Pisar <ppisar@redhat.com> - 0.82-1
- 0.82 bump

* Wed Jan 06 2021 Petr Pisar <ppisar@redhat.com> - 0.81-1
- 0.81 bump
- perl-RPC-XML license corrected to
  "(Artistic 2.0 or Artistic or LGPLv2) and (Artistic 2.0 or LGPLv2)"

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-13
- Perl 5.30 rebuild

* Mon Mar 04 2019 Petr Pisar <ppisar@redhat.com> - 0.80-12
- Fix a flaw in IPv6-support.patch tests visible when localhost resolves to one
  address only (CPAN RT#120472)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-6
- Perl 5.26 rebuild

* Thu Mar 02 2017 Petr Pisar <ppisar@redhat.com> - 0.80-5
- Add IPv6 support needed for IPv6-capable HTTP::Daemon (CPAN RT#120472)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 20 2016 Petr Pisar <ppisar@redhat.com> - 0.80-3
- Correct perl_default_filter macro invocation without perl in SRPM build root

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-2
- Perl 5.24 rebuild

* Mon May 09 2016 Petr Pisar <ppisar@redhat.com> - 0.80-1
- 0.80 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.79-2
- Perl 5.22 rebuild

* Mon May 04 2015 Petr Pisar <ppisar@redhat.com> - 0.79-1
- 0.79 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Petr Pisar <ppisar@redhat.com> - 0.78-1
- 0.78 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 0.77-3
- Perl 5.18 rebuild
- Adjust tests for perl 5.18 (CPAN RT#86187)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 04 2012 Petr Pisar <ppisar@redhat.com> - 0.77-1
- 0.77 bump
- Specify all dependencies
- Modernize spec file
- Do not package tests

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.76-4
- Perl 5.16 rebuild

* Mon Jan 16 2012 Petr Pisar <ppisar@redhat.com> - 0.76-3
- Require MODULE_COMPAT because this is Perl package.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Petr Pisar <ppisar@redhat.com> - 0.76-1
- 0.76 bump

* Mon Apr 04 2011 Petr Pisar <ppisar@redhat.com> - 0.74-1
- 0.74 bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.69-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.69-2
- Mass rebuild with perl-5.12.0

* Tue Sep 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.69-1
- auto-update to 0.69 (by cpan-spec-update 0.01)
- added a new br on perl(File::Spec) (version 0.8)
- altered br on perl(LWP) (0 => 5.801)
- added a new br on perl(Scalar::Util) (version 1.19)
- altered br on perl(XML::Parser) (0 => 2.31)
- added a new br on perl(constant) (version 1.03)
- added a new req on perl(File::Spec) (version 0.8)
- added a new req on perl(LWP) (version 5.801)
- added a new req on perl(Scalar::Util) (version 1.19)
- added a new req on perl(XML::Parser) (version 2.31)
- added a new req on perl(constant) (version 1.03)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.64-1
- update to 0.64-1
- drop tests patch (fixed!)
- add BR on Net::Server

* Mon Sep 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.60-3
- bump

* Tue Aug 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.60-2
- quiesce offending test

* Sat Aug 23 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.60-1
- even more spec cleanups :-)
- update licensing

* Fri Jul 04 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.60-0.1
- update to 0.60
- spec file cleanups

* Sun Mar 16 2008 Nicholas Boyle <nsboyle@gmail.com> - 0.59-5
- Added BuildRequires for Test::More and XML::Parser

* Sun Mar 16 2008 Nicholas Boyle <nsboyle@gmail.com> - 0.59-4
- Created subpackage perl-Apache-RPC to allow RPC-XML to work without
  requiring mod_perl
- Manpages now installed as regular files, instead of docs
- Removed explicit perl_archlib and perl_vendorarch definitions

* Fri Mar 07 2008 Nicholas Boyle <nsboyle@gmail.com> - 0.59-3
- Added README.license to clarify licensing

* Sat Mar 01 2008 Nicholas Boyle <nsboyle@gmail.com> - 0.59-2
- Initial Fedora packaging

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.59-1
- Updated to release 0.59.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.58-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Sat Jan  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.57-1
- Initial package.
