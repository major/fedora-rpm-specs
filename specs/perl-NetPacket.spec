Name:           perl-NetPacket
Version:        1.8.0
Release:        1%{?dist}
Summary:        Assemble/disassemble network packets at the protocol level
# lib/NetPacket.pm:     Artistic-2.0
# lib/NetPacket/IPX.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/NetPacket/SLL.pm  Artistic-2.0
# lib/NetPacket/SLL2.pm:    Artistic-2.0
# lib/NetPacket/USBMon.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:      Artistic-2.0 text
## Not in any binary package
# repackage.sh:     GPL-2.0-or-later
## Stripped from the source archive
# CODE_OF_CONDUCT.md:   CC-BY ???
#                       "adapted from
#                       <https://www.contributor-covenant.org/version/2/0/code_of_conduct.html>"
#                       Probaly Hippocratic License 3.0
#                       <https://github.com/EthicalSource/contributor_covenant/blob/release/LICENSE.md>.
#                       FIXME: License clarification requested
#                       <https://github.com/EthicalSource/contributor_covenant/issues/1583>?
#                       XXX: Hippocratic License 3.0 disapproved by Fedora legal
#                       <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/717>.
#                       FIXME: No SPDX identifier for Hippocratic License 3.0
#                       <https://github.com/spdx/license-list-XML/issues/2931>
#                       FIXME: A copy of the license is missing
#                       <https://github.com/yanick/netpacket/issues/19>
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
SourceLicense:  %{license} AND GPL-2.0-or-later
URL:            https://metacpan.org/release/NetPacket
# Upstream URL <https://cpan.metacpan.org/authors/id/Y/YA/YANICK/NetPacket-%%{version}.tar.gz>
# Repackaged with "./repackage.sh %%{version}" because of CODE_OF_CONDUCT.md.
Source0:        NetPacket-%{version}_repackaged.tar.gz
Source1:        repackage.sh
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
# Net::Pcap and Net::PcapUtils are nowhere used.
BuildRequires:  perl(parent)
BuildRequires:  perl(Socket) >= 1.87
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test2::Bundle::More)
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful

%description
NetPacket provides a base class for a cluster of modules related to decoding
and encoding of network protocols. Each NetPacket descendant module knows how
to encode and decode packets for the network protocol it implements. Consult
the documentation for the module in question for protocol-specific
implementation.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n NetPacket-%{version}
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
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README SECURITY.md
%{perl_vendorlib}/NetPacket
%{perl_vendorlib}/NetPacket.pm
%{_mandir}/man3/NetPacket.*
%{_mandir}/man3/NetPacket::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Feb 05 2026 Petr Pisar <ppisar@redhat.com> - 1.8.0-1
- 1.8.0 bump
- Package the tests

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.2-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.2-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.2-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.2-5
- Perl 5.32 rebuild

* Fri Feb 28 2020 Petr Pisar <ppisar@redhat.com> - 1.7.2-4
- Build-requires blib for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Petr Pisar <ppisar@redhat.com> - 1.7.2-1
- 1.7.2 bump

* Mon Jun 10 2019 Petr Pisar <ppisar@redhat.com> - 1.7.1-1
- 1.7.1

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.0-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Petr Pisar <ppisar@redhat.com> - 1.7.0-1
- 1.7.0 bump
- License changed to (Artistic 2.0 and CC-BY)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-8
- Perl 5.26 rebuild

* Mon Mar 20 2017 Petr Pisar <ppisar@redhat.com> - 1.6.0-7
- Modernize spec file

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-2
- Perl 5.22 rebuild

* Sat Mar 14 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.0-1
- Update to 1.6.0

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.0-2
- Perl 5.20 rebuild

* Sun Jun 15 2014 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.5.0-1
- Update to 1.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 30 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.4-1
- Update to 1.4.4

* Tue Nov 26 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.3-1
- Update to 1.4.3

* Thu Sep 26 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.2-1
- Update to 1.4.2

* Fri Sep  6 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.1-1
- Update to 1.4.1

* Thu Aug 29 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.0-1
- Update to 1.4.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.3.3-3
- Perl 5.18 rebuild

* Thu May 16 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.3-2
- No longer disable the 000-report-versions.t test

* Thu May 16 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.3-1
- Update to 1.3.3.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.3.1-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.1-1
- Update to 1.3.1.

* Mon Nov 14 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.0-1
- Update to 1.3.0.
- Rebased patch0.

* Sat Jul 30 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.2.0-1
- Update to 1.2.0.

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1.1-2
- Perl mass rebuild

* Thu Feb 10 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.1.1-1
- Update to 1.1.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.1.0-1
- Update to 1.1.0.

* Fri Dec 24 2010 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0.1-1
- Update to 1.0.1.
- Disable test t/000-report-versions.t and downgrade build requirements
  (NetPacket-1.0.1-Build.PL-downgrade-modules-requirements.patch) in order
  to support EPEL >= 5 and Fedora >= 12.

* Mon Mar 29 2010 Jan Klepek 0.42.0-1
- Changed license to Artistic 2.0 and updated version

* Mon Mar 15 2010 Jan Klepek 0.41.1-1
- Specfile autogenerated by cpanspec 1.78.
