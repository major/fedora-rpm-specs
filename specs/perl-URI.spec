# Support isbn URN via Business::ISBN that needs gd library
%if 0%{?rhel}
%bcond_with perl_URI_enables_Business_ISBN
%bcond_with perl_URI_enables_Regexp_IPv6
%else
%bcond_without perl_URI_enables_Business_ISBN
%bcond_without perl_URI_enables_Regexp_IPv6
%endif

Name:           perl-URI
Version:        5.32
Release:        2%{?dist}
Summary:        A Perl module implementing URI parsing and manipulation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI
Source0:        https://cpan.metacpan.org/modules/by-module/URI/URI-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(integer)
BuildRequires:  perl(MIME::Base32)
BuildRequires:  perl(MIME::Base64) >= 2
BuildRequires:  perl(Net::Domain)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Warnings)
# Optional Tests
# Geo::Point not (yet) available in Fedora
#BuildRequires:  perl(Geo::Point)
# Dependencies
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(Encode)
Requires:       perl(MIME::Base64) >= 2
Requires:       perl(Net::Domain)
Requires:       perl(utf8)

# Optional Functionality
%if %{with perl_URI_enables_Business_ISBN}
# Business::ISBN pulls in gd and X libraries for barcode support, hence this soft dependency (#1380152)
# Business::ISBN → Test::Pod → Pod::Simple → HTML::Entities (HTML::Parser) → URI
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Business::ISBN) >= 3.005
%endif
Suggests:       perl(Business::ISBN) >= 3.005
%endif
%if %{with perl_URI_enables_Regexp_IPv6}
BuildRequires:  perl(Regexp::IPv6) >= 0.03
Suggests:       perl(Regexp::IPv6) >= 0.03
%endif

%description
This module implements the URI class. Objects of this class represent
"Uniform Resource Identifier references" as specified in RFC 2396 (and
updated by RFC 2732).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_URI_enables_Business_ISBN}
Requires:       perl(Business::ISBN) >= 3.005
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n URI-%{version}
chmod -c 644 uri-test

for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done


%build
perl Makefile.PL INSTALLDIRS=perl NO_PACKLIST=true NO_PERLLOCAL=true
%{make_build}

%install
%{make_install}

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{(urls.sto)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/storable.t
perl -i -pe 's{(urls.sto)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/storable-test.pl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%{_fixperms} -c %{buildroot}

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README uri-test
%{perl_privlib}/URI.pm
%{perl_privlib}/URI/
%{_mandir}/man3/URI.3*
%{_mandir}/man3/URI::Escape.3*
%{_mandir}/man3/URI::Heuristic.3*
%{_mandir}/man3/URI::QueryParam.3*
%{_mandir}/man3/URI::Split.3*
%{_mandir}/man3/URI::URL.3*
%{_mandir}/man3/URI::WithBase.3*
%{_mandir}/man3/URI::_punycode.3*
%{_mandir}/man3/URI::icap.3*
%{_mandir}/man3/URI::icaps.3*
%{_mandir}/man3/URI::data.3*
%{_mandir}/man3/URI::file.3*
%{_mandir}/man3/URI::geo.3*
%{_mandir}/man3/URI::ldap.3*
%{_mandir}/man3/URI::otpauth.3*
%{_mandir}/man3/URI::smb.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun May 11 2025 Paul Howarth <paul@city-fan.org> - 5.32-1
- 5.32 bump (rhbz#2365471)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov  6 2024 Paul Howarth <paul@city-fan.org> - 5.31-1
- 5.31 bump (rhbz#2324123)

* Wed Oct  9 2024 Paul Howarth <paul@city-fan.org> - 5.30-1
- 5.30 bump (rhbz#2317441)

* Fri Sep  6 2024 Paul Howarth <paul@city-fan.org> - 5.29-1
- 5.29 bump (rhbz#2310263)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 27 2024 Jitka Plesnikova <jplesnik@redhat.com> - 5.28-1
- 5.28 bump (rhbz#2271724)

* Fri Feb  9 2024 Paul Howarth <paul@city-fan.org> - 5.27-1
- 5.27 bump (rhbz#2263535)

* Sat Feb  3 2024 Paul Howarth <paul@city-fan.org> - 5.26-1
- 5.26 bump (rhbz#2262451)

* Sun Jan 28 2024 Paul Howarth <paul@city-fan.org> - 5.25-1
- 5.25 bump (rhbz#2260642)

* Fri Jan 26 2024 Jitka Plesnikova <jplesnik@redhat.com> - 5.24-1
- 5.24 bump (rhbz#2260409)

* Thu Jan 25 2024 Paul Howarth <paul@city-fan.org> - 5.22-1
- 5.22 bump (rhbz#2260363)

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 24 2023 Jitka Plesnikova <jplesnik@redhat.com> - 5.21-1
- 5.21 bump (rhbz#2233885)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May  1 2023 Paul Howarth <paul@city-fan.org> - 5.19-1
- 5.19 bump

* Sat Apr 29 2023 Paul Howarth <paul@city-fan.org> - 5.18-1
- 5.18 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov  3 2022 Paul Howarth <paul@city-fan.org> - 5.17-1
- 5.17 bump

* Wed Oct 12 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.16-1
- 5.16 bump

* Tue Oct 11 2022 Paul Howarth <paul@city-fan.org> - 5.15-1
- 5.15 bump

* Tue Oct 11 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.14-1
- 5.14 bump

* Fri Oct 07 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.13-1
- 5.13 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Paul Howarth <paul@city-fan.org> - 5.12-1
- 5.12 bump

* Tue Jul  5 2022 Paul Howarth <paul@city-fan.org> - 5.11-1
- 5.11 bump

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.10-3
- Perl 5.36 re-rebuild of bootstrapped packages

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.10-2
- Perl 5.36 rebuild

* Tue Oct 26 2021 Paul Howarth <paul@city-fan.org> - 5.10-1
- 5.10 bump

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.09-3
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.09-2
- Perl 5.34 rebuild

* Wed Mar 03 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.09-1
- 5.09 bump
- Package tests

* Sun Feb 28 2021 Paul Howarth <paul@city-fan.org> - 5.08-1
- 5.08 bump

* Sun Jan 31 2021 Paul Howarth <paul@city-fan.org> - 5.07-1
- 5.07 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.06-1
- 5.06 bump

* Wed Oct 21 2020 Paul Howarth <paul@city-fan.org> - 5.05-1
- 5.05 bump

* Tue Jul 28 2020 Petr Pisar <ppisar@redhat.com> - 1.76-9
- Modernize a spec file

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-8
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.76-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-1
- 1.76 bump

* Wed Jan 09 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-1
- 1.75 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.74-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.74-2
- Perl 5.28 rebuild

* Mon Apr 23 2018 Paul Howarth <paul@city-fan.org> - 1.74-1
- 1.74 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.73-1
- 1.73 bump

* Wed Jul 26 2017 Paul Howarth <paul@city-fan.org> - 1.72-1
- 1.72 bump

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-8
- Perl 5.26 re-rebuild of bootstrapped packages

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct  7 2016 Paul Howarth <paul@city-fan.org> - 1.71-5
- Soften Business::ISBN dependency from Requires: to Suggests: to avoid
  pulling in gd and X libraries (#1380152)

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Paul Howarth <paul@city-fan.org> - 1.71-1
- 1.71 bump

* Wed Oct 14 2015 Paul Howarth <paul@city-fan.org> - 1.69-2
- BR: perl(Test)

* Sat Jul 25 2015 Paul Howarth <paul@city-fan.org> - 1.69-1
- 1.69 bump

* Fri Jun 26 2015 Paul Howarth <paul@city-fan.org> - 1.68-1
- 1.68 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.67-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.67-2
- Perl 5.22 rebuild

* Wed Feb 25 2015 Paul Howarth <paul@city-fan.org> - 1.67-1
- 1.67 bump

* Fri Nov  7 2014 Paul Howarth <paul@city-fan.org> - 1.65-1
- 1.65 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.64-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.64-2
- Perl 5.20 rebuild

* Thu Jul 17 2014 Petr Šabata <contyk@redhat.com> - 1.64-1
- 1.64 bump

* Mon Jul 07 2014 Petr Pisar <ppisar@redhat.com> - 1.61-1
- 1.61 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-11
- Perl 5.18 re-rebuild of bootstrapped packages

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.60-9
- Perl 5.18 rebuild

* Wed Feb 27 2013 Paul Howarth <paul@city-fan.org> - 1.60-8
- Retain runtime dependency of perl(Business::ISBN) when bootstrapping; a
  better fix for the build dependency cycle was to drop LWP::Simple as a
  buildreq of perl-Business-ISBN (needed only for optional tests) when
  bootstrapping

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-6
- Update dependencies

* Tue Aug 28 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-5
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.60-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.60-2
- Perl 5.16 rebuild

* Mon Mar 26 2012 Paul Howarth <paul@city-fan.org> - 1.60-1
- Update to 1.60
  - Do not reverse the order of new parameters
  - Avoid test failure if the local hostname is 'foo' (CPAN RT#75519)
  - Work around a stupid join bug in 5.8.[12] (CPAN RT#59274)
  - Updated repository URL
- Don't need to remove empty directories from buildroot
- BR: perl(constant)

* Fri Jan 20 2012 Paul Howarth <paul@city-fan.org> - 1.59-3
- Break build dependency loop by only using perl(Business::ISBN) if we're not
  bootstrapping
- BR: perl(Carp) and perl(Exporter)
- Make %%files list more explicit
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Use %%{_fixperms} macro rather than our own chmod incantation
- Don't use macros for commands

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  2 2011 Tom Callaway <spot@fedoraproject.org> - 1.59-1
- update to 1.59

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.58-2
- Perl mass rebuild

* Wed Mar 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.58-1
- update to 1.58

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.56-1
- update

* Mon Oct 11 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.55-1
- update

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.54-2
- Mass rebuild with perl-5.12.0

* Mon Apr 19 2010 Petr Pisar <ppisar@redhat.com> - 1.54-1
- version bump
- Changes is in UTF-8 already
- rfc2396.txt removed by upstream

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.40-2
- rebuild against perl 5.10.1

* Tue Oct  6 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.40-1
- update to new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.37-1
- Upstream update.
- Add BR: perl(Test::More), perl(Business::ISBN).
- Remove requires-filter.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.35-8
- Rebuild for perl 5.10 (again)

* Wed Feb 13 2008 Robin Norwood <rnorwood@redhat.com> - 1.35-7
- rebuild again for new perl

* Wed Feb 13 2008 Robin Norwood <rnorwood@redhat.com> - 1.35-6
- Last update for package review

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.35-5
- rebuild for new perl

* Thu Oct 25 2007 Robin Norwood <rnorwood@redhat.com> - 1.35-4
- Fix various package review issues:
- Remove redundant BR: perl
- remove "|| :" from %%check
- move requires filter into spec file
- remove tabs and fix spacing

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.35-3.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Mon Jun 05 2006 Jason Vas Dias <jvdias@redhat.com> - 1.35-3
- fix License: tag

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 1.35-2.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Sat Apr 02 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.35-2
- Update to 1.35.
- Spec cleanup (#153205)

* Thu Sep 23 2004 Chip Turner <cturner@redhat.com> 1.30-3
- rebuild

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 1.30-2
- rebuild

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 1.30-1
- update to 1.30

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Tue Aug  6 2002 Chip Turner <cturner@localhost.localdomain>
- update to 1.21

* Tue Jun  4 2002 Chip Turner <cturner@redhat.com>
- properly claim directories owned by package so they are removed when package is removed

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 7 2001 root <root@redhat.com>
- Spec file was autogenerated. 
