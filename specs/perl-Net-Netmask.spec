Name:           perl-Net-Netmask
Version:        2.0002
Release:        7%{?dist}
Summary:        Perl module for manipulating and looking up IP network blocks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Netmask
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMASLAK/Net-Netmask-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt) >= 1.999811
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(vars)
# Tests only
# Benchmark not used when runnig the tests through make check or prove
# Test::More 0.96 not used
# Test::Perl::Critic not used
# Test::Pod 1.41 not used
BuildRequires:  perl(Test::UseAllModules) >= 0.17
# Test::Version not used
BuildRequires:  perl(Test2::V0) >= 0.000111
BuildRequires:  perl(utf8)
# Optional tests
# Test::Vars not used
Requires:       perl(Math::BigInt) >= 1.999811

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Math::BigInt\\)$

%description
Net::Netmask parses and understands IPv4 and IPv6 CIDR blocks (see
<https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing> for more
information on CIDR blocks). There are also functions to insert a network
block into a table and then later look up network blocks by an IP address
using that table.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Net-Netmask-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/release*
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/author*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING RELEASE_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.0002-1
- 2.0002 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.0001-6
- Perl 5.36 rebuild

* Tue Apr 05 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.0001-5
- Updated dependencies

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.0001-2
- Perl 5.34 rebuild

* Tue Mar 30 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.0001-1
- 2.0001 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9104-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9104-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.9104-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9104-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9104-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.9104-4
- Perl 5.30 rebuild

* Fri Mar 01 2019 Petr Pisar <ppisar@redhat.com> - 1.9104-3
- Modernize spec file

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9104-1
- 1.9104 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9103-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9103-2
- Perl 5.28 rebuild

* Tue Jun 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9103-1
- 1.9103 bump

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9101-1
- 1.9101 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9022-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9022-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9022-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.9022-2
- Perl 5.22 rebuild

* Thu May 21 2015 Petr Šabata <contyk@redhat.com> - 1.9022-1
- 1.9022 bump
- Modernized the SPEC
- Corrected the dep list
- License changed to `Perl'
- Changed the bogus date in changelog according to our git log

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.9015-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9015-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9015-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.9015-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9015-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9015-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.9015-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9015-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.9015-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9015-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.9015-7
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.9015-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.9015-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 30 2008 Paul Howarth <paul@city-fan.org> - 1.9015-2
- Add perl(:MODULE_COMPAT...) dependency (#449362)
- Remove redundant buildreq perl
- Fix "make check" syntax
- Fix argument order for find with -depth

* Thu Sep 27 2007 Warren Togami <wtogami@redhat.com> - 1.9015-1
- 1.9015, update license tag

* Thu Sep 14 2006 Warren Togami <wtogami@redhat.com> - 1.9012-3
- rebuild for FC6

* Fri May 20 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.9012-2
- 1.9012, use canonical CPAN URL in Source0.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.9011-2
- rebuilt

* Sun Aug 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.9011-1
- Update to 1.9011.
- Bring up to date with current fedora.us Perl spec template.

* Sun Feb  8 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.9007-0.fdr.2
- Reduce directory ownership bloat.
- Run tests in the %%check section.

* Sat Feb 07 2004 Warren Togami <warren@togami.com> - 0:1.9007-0.fdr.1
- upgrade to 1.9007

* Thu Nov 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.9004-0.fdr.2
- Specfile rewrite.

* Fri Sep 19 2003 Warren Togami <warren@togami.com> - 1.9004-0.fdr.1
- Specfile autogenerated.
