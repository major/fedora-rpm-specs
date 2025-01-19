Name:           perl-Crypt-OpenSSL-X509
Version:        2.0.1
Release:        2%{?dist}
Summary:        Perl interface to OpenSSL for X509
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-X509
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASBN/Crypt-OpenSSL-X509-%{version}.tar.gz
# Respect distribution compiler flags
Patch0:         Crypt-OpenSSL-X509-1.914-Do-not-hard-code-CFLAGS.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Convert::ASN1) >= 0.33
BuildRequires:  perl(Crypt::OpenSSL::Guess)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  openssl
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
#BuildRequires:  perl(Test::CPAN::Meta::JSON)
#BuildRequires:  perl(Test::Kwalitee) >= 1.21

%description
Crypt::OpenSSL::X509 - Perl extension to OpenSSL's X509 API.

%prep
%setup -q -n Crypt-OpenSSL-X509-%{version}
%patch -P 0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes.md README TODO
%{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/Crypt::OpenSSL::X509.3pm*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 09 2024 Xavier Bachelot <xavier@bachelot.org> - 2.0.1-1
- Update to 2.0.1 (RHBZ#2303844)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Xavier Bachelot <xavier@bachelot.org> - 2.0.0-1
- Update to 2.0.0 (RHBZ#2295643)
- Clean up specfile

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.915-6
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.915-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.915-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.915-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.915-2
- Perl 5.38 rebuild

* Mon Jun 26 2023 Xavier Bachelot <xavier@bachelot.org> - 1.915-1
- Update to 1.915 (RHBZ#2215981)

* Mon Jun 05 2023 Xavier Bachelot <xavier@bachelot.org> - 1.914-1
- Update to 1.914 (RHBZ#2058821)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.912-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.912-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.912-2
- Perl 5.36 rebuild

* Mon Feb 14 2022 Xavier Bachelot <xavier@bachelot.org> - 1.912-1
- Update to 1.912 (RHBZ#2042270)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.910-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.910-2
- Rebuilt with OpenSSL 3.0.0

* Thu Sep 09 2021 Xavier Bachelot <xavier@bachelot.org> - 1.910-1
- Update to 1.910 (RHBZ#1988752)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.908-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.908-2
- Perl 5.34 rebuild

* Mon May 17 2021 Xavier Bachelot <xavier@bachelot.org> - 1.908-1
- Update to 1.908 (RHBZ#1960347)

* Mon May 03 2021 Xavier Bachelot <xavier@bachelot.org> - 1.907-1
- Update to 1.907 (RHBZ#1956101)

* Sun Apr 25 2021 Xavier Bachelot <xavier@bachelot.org> - 1.906-1
- Update to 1.906 (RHBZ#1953165)

* Wed Apr 21 2021 Xavier Bachelot <xavier@bachelot.org> - 1.905-1
- Update to 1.905 (RHBZ#1951911)

* Thu Apr 08 2021 Xavier Bachelot <xavier@bachelot.org> - 1.903-1
- Update to 1.903 (RHBZ#1947271)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.902-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Xavier Bachelot <xavier@bachelot.org> - 1.902-1
- Update to 1.902 (RHBZ#1895493)

* Sat Nov 07 2020 Xavier Bachelot <xavier@bachelot.org> - 1.901-1
- Update to 1.901
- Add BR: make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.813-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.813-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.813-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Wes Hardaker <wjhns174@hardakers.net> - 1.813-1
- upgrade to latest 1.813

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.812-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.812-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.812-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.812-1
- 1.812 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.808-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.808-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.808-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.808-1
- 1.808 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.807-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.807-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.807-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.807-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 27 2016 Petr Pisar <ppisar@redhat.com> - 1.807-2
- Adjust to OpenSSL 1.1.0 (bug #1383759)

* Wed Aug 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.807-1
- 1.807 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.806-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.806-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.806-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.806-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Petr Pisar <ppisar@redhat.com> - 1.806-1
- 1.806 bump

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.803-6
- Perl 5.22 rebuild

* Wed Feb 11 2015 Petr Pisar <ppisar@redhat.com> - 1.803-5
- Fix condition negation (bug #1190816)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.803-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.803-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.803-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 20 2013 Wes Hardaker <wjhns174@hardakers.net> - 1.803-1
- upgrade to latest 1.803

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.800.2-7
- Perl 5.18 rebuild
- Specify all dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.800.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.800.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.800.2-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.800.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.800.2-2
- Perl mass rebuild

* Wed May 11 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.800.2-1
- Another upstream minor release

* Thu May  5 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.800.1-2
- added new sources

* Thu May  5 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.800.1-1
- Update to the upstream 1.800.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.6-1
- Updated to the upstream: 1.6

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.4-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Sep  9 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.4-2
- removed broken tests that are probably related to patches applied to
  the main openssl base

* Thu Sep  9 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.4-1
- Update to the upstream

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.7-7
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.7-6
- rebuild against perl 5.10.1

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - 0.7-5
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.7-2
- rebuild with new openssl

* Mon Jul 21 2008 Wes Hardaker <wjhns174@hardakers.net> - 0.7-1
- Updated to upstream 0.7

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6-2
Rebuild for new perl

* Mon Feb 25 2008 Wes Hardaker <wjhns174@hardakers.net> - 0.6-1
- bump to upstream 0.6

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5-4
- Autorebuild for GCC 4.3

* Thu Dec  6 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.5-3
- Bump to force rebuild with new openssl lib version

* Fri Nov  9 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.5-2
- Update license tag to the proper new wording

* Fri Nov  9 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.5-1
- update to upstream 0.5 containing a MANIFEST fix
- Add Test::Pod and Module::Install to build requirements

* Mon May 14 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.4-3
- BuildRequire perl(Test::More) perl(Test::Pod)
- Fixed source code URL

* Tue May  8 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.4-2
- Add BuildRequire openssl-devel
- Don't manually require openssl
- Use vendorarch instead of vendorlib 

* Thu Apr 19 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.4-1
- Initial version
