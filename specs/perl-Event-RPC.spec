Name:           perl-Event-RPC
Version:        1.10
Release:        22%{?dist}
Summary:        Event based transparent client/server RPC framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Event-RPC
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JRED/Event-RPC-%{version}.tar.gz
# Normalize documenation encoding
Patch0:         Event-RPC-1.08-Convert-to-UTF-8.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CBOR::XS)
BuildRequires:  perl(Event)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Glib)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(JSON::XS) >= 3
BuildRequires:  perl(Sereal) >= 3
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(utf8)
# Optional run-time:
BuildRequires:  perl(IO::Socket::SSL)
# Tests:
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests:
# Benchmark not used
# TODO:  Split dependencies on an event controller ||(AnyEvent Event Glib)
# Dependent on a format: ||(Sereal CBOR::XS JSON::XS Storable).
# The requires in lib/Event/RPC/Message.pm are void, CPAN RT#107405.
# Sereal is recommended, Storable is backward-compatible but insecure.
Requires:       %{name}-format = %{version}-%{release}
Recommends:     perl(Event::RPC::Message::Sereal)

# Filter documentation's dependencies
%{?perl_default_filter}

%description
Event::RPC supports you in developing Event based networking client/server
applications with transparent object/method access from the client to the
server. Network communication is optionally encrypted using IO::Socket::SSL.
Several event loop managers are supported due to an extensible API. Currently
Event, Glib, and AnyEvent are implemented. The latter lets you use nearly
every event loop implementation available for Perl.

%package Message-CBOR
Summary:        CBOR message format for Event::RPC
Requires:       perl(Event::RPC::Message::SerialiserBase)
Provides:       %{name}-format = %{version}-%{release}

%description Message-CBOR
This implements CBOR message format for Event::RPC Perl RPC framework.

%package Message-JSON
Summary:        JSON message format for Event::RPC
Requires:       perl(Event::RPC::Message::SerialiserBase)
Provides:       %{name}-format = %{version}-%{release}

%description Message-JSON
This implements JSON message format for Event::RPC Perl RPC framework.

%package Message-Sereal
Summary:        Sereal message format for Event::RPC
Requires:       perl(Event::RPC::Message)
Requires:       perl(Sereal) >= 3
Provides:       %{name}-format = %{version}-%{release}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Sereal\\)$

%description Message-Sereal
This implements Sereal message format for Event::RPC Perl RPC framework.

%package Message-Storable
Summary:        Storable message format for Event::RPC
Requires:       perl(Event::RPC::Message)
Provides:       %{name}-format = %{version}-%{release}

%description Message-Storable
This implements Storable message format for Event::RPC Perl RPC framework.

%prep
%setup -q -n Event-RPC-%{version}
%patch -P0 -p1
# Make it so that the .pl scripts in %%doc don't add bogus requirements
chmod -x examples/*.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%check
make test

%files
%doc Changes examples README
%{perl_vendorlib}/Event/
%exclude %{perl_vendorlib}/Event/RPC/Message/CBOR.pm
%exclude %{perl_vendorlib}/Event/RPC/Message/JSON.pm
%exclude %{perl_vendorlib}/Event/RPC/Message/Sereal.pm
%exclude %{perl_vendorlib}/Event/RPC/Message/Storable.pm
%{_mandir}/man3/*.3*
%exclude %{_mandir}/man3/Event::RPC::Message::CBOR.3*
%exclude %{_mandir}/man3/Event::RPC::Message::JSON.3*
%exclude %{_mandir}/man3/Event::RPC::Message::Sereal.3*
%exclude %{_mandir}/man3/Event::RPC::Message::Storable.3*

%files Message-CBOR
%{perl_vendorlib}/Event/RPC/Message/CBOR.pm
%{_mandir}/man3/Event::RPC::Message::CBOR.3*

%files Message-JSON
%{perl_vendorlib}/Event/RPC/Message/JSON.pm
%{_mandir}/man3/Event::RPC::Message::JSON.3*

%files Message-Sereal
%{perl_vendorlib}/Event/RPC/Message/Sereal.pm
%{_mandir}/man3/Event::RPC::Message::Sereal.3*

%files Message-Storable
%{perl_vendorlib}/Event/RPC/Message/Storable.pm
%{_mandir}/man3/Event::RPC::Message::Storable.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10-21
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-14
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-2
- Perl 5.28 rebuild

* Thu Jun 28 2018 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Tue Jun 26 2018 Petr Pisar <ppisar@redhat.com> - 1.09-1
- 1.09 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump

* Tue Sep 22 2015 Petr Pisar <ppisar@redhat.com> - 1.07-1
- 1.07 bump

* Mon Sep 21 2015 Petr Pisar <ppisar@redhat.com> - 1.06-1
- 1.06 bump

* Mon Sep 07 2015 Petr Pisar <ppisar@redhat.com> - 1.05-6
- Fix testing certificate (bug #1259404)
- Convert Changes into UTF-8
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 30 2014 Petr Pisar <ppisar@redhat.com> - 1.05-1
- 1.05 bump

* Mon Jan 27 2014 Petr Pisar <ppisar@redhat.com> - 1.04-1
- 1.04 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 1.03-2
- Perl 5.18 rebuild

* Mon Jun 17 2013 Petr Pisar <ppisar@redhat.com> - 1.03-1
- 1.03 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 1.01-12
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.01-10
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.01-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-6
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.01-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec  16 2008 kwizart < kwizart at gmail.com > - 1.01-1
- Update to 1.01

* Thu Jul  17 2008 kwizart < kwizart at gmail.com > - 1.00-1
- Update to 1.00

* Thu May  29 2008 kwizart < kwizart at gmail.com > - 0.90-3
- Fix directory ownership
- Remove unwanted provides Test_class
- Fix non-utf8 encoding

* Thu May  8 2008 kwizart < kwizart at gmail.com > - 0.90-2
- Fix encoding and permission for examples

* Wed Apr 30 2008 kwizart < kwizart at gmail.com > - 0.90-1
- Initial package for Fedora

