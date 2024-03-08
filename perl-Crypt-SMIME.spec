Name:           perl-Crypt-SMIME
Version:        0.29
Release:        1%{?dist}
Summary:        S/MIME message signing, verification, encryption and decryption
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-SMIME
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-SMIME-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  openssl
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Taint::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Taint)
BuildRequires:  perl(Test::More)

#Add a test sub package.
%{?perl_default_subpackage_tests}


%description
This module provides a class for handling S/MIME messages. It can sign,
verify, encrypt and decrypt messages. It requires libcrypto
(http://www.openssl.org) to work.


%prep
%setup -q -n Crypt-SMIME-%{version}
# As part of the rpm process we generate some files which
# then cause t/manifest.t to fail.
printf '\\.list$\n^\\.package_note\n' >> MANIFEST.SKIP


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/SMIME*3pm*


%changelog
* Wed Feb 06 2024 Xavier Bachelot <xavier@bachelot.org> - 0.29-1
- Update to 0.29 (RHBZ #2264507)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-8
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-5
- Perl 5.36 rebuild

* Tue Mar 22 2022 Adam Williamson <awilliam@redhat.com> - 0.28-4
- Rebuild with no changes to fix update mess on F36

* Fri Mar 18 2022 Petr Pisar <ppisar@redhat.com> - 0.28-3
- Ignore .package_note file by MANIFEST tests (bug #2059502)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Xavier Bachelot <xavier@bachelot.org> - 0.28-1
- Update to 0.28 (fixes #2007251)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.27-5
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 24 2020 Petr Pisar <ppisar@redhat.com> - 0.27-1
- 0.27 bump (bug #1875827)

* Fri Aug 21 2020 Steve Traylen <steve.traylen@cern.ch> - 0.26-1
- 0.26 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.28 rebuild

* Mon Mar 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-1
- 0.25 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-1
- 0.23 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-1
- 0.19 bump

* Fri Oct 14 2016 Petr Pisar <ppisar@redhat.com> - 0.18-1
- 0.18 bump

* Wed Jun 22 2016 Steve Traylen <steve.traylen@cern.ch> - 0.17-1
- 0.17 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 3 2015 Steve Traylen <steve.traylen@cern.ch> - 0.16-1
- 0.16 bump

* Mon Aug 31 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-1
- 0.15 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-10
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-9
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.10-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.10-2
- Perl 5.16 rebuild
- Specify all dependencies

* Tue Feb 14 2012 Steve Traylen <steve.traylen@cern.ch> 0.10-1
- Update to 0.10

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-6
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Iain Arnell <iarnell@gmail.com> 0.09-5
- doesn't require perl(Test::Exception) or perl(Test::More)

* Tue Jun 22 2010 Petr Pisar <ppisar@redhat.com> 0.09-4
- Rebuild against perl-5.12

* Tue May 4 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-3
- First release on Fedora/EPEL.

* Mon May 3 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-2
- Additon of openssl-devel build requires.

* Mon Apr 26 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
- Install with DESTDIR
- Create -test subpackage if macro is define.
- Remove SMIME.mlpod from docs.
