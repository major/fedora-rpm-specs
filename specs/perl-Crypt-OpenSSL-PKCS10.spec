Name:           perl-Crypt-OpenSSL-PKCS10
Version:        0.34
Release:        1%{?dist}
Summary:        Perl interface to OpenSSL for PKCS10
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-PKCS10
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-OpenSSL-PKCS10-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
# It's required for successful Crypt::OpenSSL::Guess process.
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::OpenSSL::Guess) >= 0.11
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Crypt::OpenSSL::RSA)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(Test::Lib)
BuildRequires:  perl(Test::More)

# Remove private test modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Crypt::OpenSSL::PKCS10|Test::Crypt::OpenSSL::PKCS10::Util\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Test::Crypt::OpenSSL::PKCS10|Test::Crypt::OpenSSL::PKCS10::Util\\)$

%description
Crypt::OpenSSL::PKCS10 Perl module provides the ability to create PKCS10
certificate requests using RSA key pairs.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       openssl
Requires:       perl(Crypt::OpenSSL::RSA)
Requires:       perl-Test-Harness

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Crypt-OpenSSL-PKCS10-%{version}
# Help file to recognize the Perl scripts and normalize shebangs
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
# Remove release/author tests
rm %{buildroot}/%{_libexecdir}/%{name}/t/author*
rm %{buildroot}/%{_libexecdir}/%{name}/t/release*
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt*
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/Crypt::OpenSSL::PKCS10*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon Jan 27 2025 Michal Josef Špaček <mspacek@redhat.com> - 0.34-1
- 0.34 bump (rhbz#2342050)

* Fri Jan 24 2025 Michal Josef Špaček <mspacek@redhat.com> - 0.31-1
- 0.31 bump (rhbz#2339426)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-2
- Perl 5.40 rebuild

* Mon Jun 10 2024 Michal Josef Špaček <mspacek@redhat.com> - 0.26-1
- 0.26 bump (rhbz#2291091)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-1
- 0.25 bump (rhbz#2231739)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 19 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-1
- 0.20 bump (rhbz#2223434)
- Update license to SPDX format

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-6
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.36 rebuild

* Tue Mar 29 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.19-2
- Fix detection of openssl library (bug #2069748)

* Tue Mar 29 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.19-1
- 0.19 bump

* Tue Mar 22 2022 Adam Williamson <awilliam@redhat.com> - 0.18-2
- Rebuild with no changes to fix update mess on F36

* Wed Mar 16 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.18-1
- 0.18 bump
- Package tests

* Fri Mar 11 2022 Petr Pisar <ppisar@redhat.com> - 0.16-20
- Adapt to OpenSSL 3 (bug #2005973)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.16-18
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-16
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-13
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump (bug #1383760)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Wes Hardaker <wjhns174@hardakers.net> - 0.15-1
- 0.15 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-5
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 20 2013 Wes Hardaker <wjhns174@hardakers.net> - 0.12-1
- 0.12 release for bug fixes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.09-2
- Perl 5.18 rebuild
- Prevent test from crashing (CPAN RT#87049)

* Tue Mar  5 2013 Wes Hardaker <wjhns174@hardakers.net> - 0.09-1
- updated to 0.9

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.06-20
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-18
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-16
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-15
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.06-14
- rebuild against perl 5.10.1

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - 0.06-13
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.06-10
- rebuild with new openssl

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.06-9
Rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.06-8
- Autorebuild for GCC 4.3

* Thu Dec  6 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.06-7
- Bump to force rebuild with new openssl lib version

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.06-6
- Rebuild for selinux ppc32 issue.

* Fri Jun  1 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.06-5
- really remove the README file this time

* Thu May 31 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.06-4
- added a build requirement for Crypt::OpenSSL::RSA
- fix hard-coded include/library paths in the Makefile.PL
- unmodified template README removed from install
- Reverse terms in license to match perl rpm exactly

* Mon May 14 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.06-3
- BuildRequire perl(Test::More) perl(ExtUtils::MakeMaker)
- Fixed source code URL

* Tue May  8 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.06-2
- Add BuildRequire openssl-devel
- Don't manually require openssl
- Use vendorarch instead of vendorlib 

* Thu Apr 19 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.06-1
- Initial version
