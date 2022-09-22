Name:           perl-Authen-Krb5-Admin
Version:        0.17
Release:        33%{?dist}
Summary:        Perl extension for MIT Kerberos 5 admin interface
# admin.h - MIT
# ppport.h - GPL+ or Artisic (same as any version of Perl)
# everything else: BSD (two clause)
License:        MIT and BSD and (GPL+ or Artistic)
URL:            https://metacpan.org/release/Authen-Krb5-Admin
Source0:        https://cpan.metacpan.org/authors/id/S/SJ/SJQUINNEY/Authen-Krb5-Admin-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Authen::Krb5)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time - not used during build
#BuildRequires:  perl(AutoLoader)
#BuildRequires:  perl(Carp)
#BuildRequires:  perl(DynaLoader)
#BuildRequires:  perl(Exporter)
#BuildRequires:  perl(vars)
# Tests - tests are not executed
#BuildRequires:  perl(Socket)
#BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Authen::Krb5::Admin is an object-oriented interface to the Kerberos 5 admin
server. Currently only MIT KDCs are supported, but the author envisions
seamless integration with other KDCs.

%prep
%setup -q -n Authen-Krb5-Admin-%{version}

sed -i -e 's!$PREFIX/lib!$PREFIX/%{_lib}!' Makefile.PL

%build
# set some dummy values for the test to stop Makefile.PL from asking
# note: the values are never used
export PERL_KADM5_PRINCIPAL=dummy
export PERL_KADM5_TEST_NAME=dummy
export PERL_KADM5_TEST_NAME_2=dummy
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
# not possible due to required kerberos environment
#make test

%files
%doc README COPYING ChangeLog
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Authen
%{_mandir}/man3/*.3pm*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-32
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-29
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-26
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-23
- Perl 5.30 rebuild

* Mon Apr 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-22
- Specify all needed BRs

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-19
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-15
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 22 2016 Christian Krause <chkr@fedoraproject.org> - 0.17-13
- Rebuild against new krb5-1.15-beta1

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 20 2015 Petr Pisar <ppisar@redhat.com> - 0.17-10
- Rebuild against new krb5-1.14-beta1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-8
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 23 2013 Christian Krause <chkr@fedoraproject.org> - 0.17-4
- rebuild against new krb5-1.12

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.17-2
- Perl 5.18 rebuild

* Sun Feb 24 2013 Christian Krause <chkr@fedoraproject.org> - 0.17-1
- update to new upstream version
- minor cleanup

* Tue Feb 19 2013 Christian Krause <chkr@fedoraproject.org> - 0.16-1
- update to new upstream version
- minor cleanup

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.11-13
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Christian Krause <chkr@fedoraproject.org> - 0.11-9
- rebuild against new krb5-1.9

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-8
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-7
- Mass rebuild with perl-5.12.0

* Sat Mar 06 2010 Christian Krause <chkr@fedoraproject.org> - 0.11-6
- rebuild against new krb5-1.8

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.11-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Christian Krause <chkr@fedoraproject.org> - 0.11-3
- rebuild against new krb5-1.7

* Fri Mar 13 2009 Christian Krause <chkr@fedoraproject.org> - 0.11-2
- fixed build problem on x86_64 (libk5crypto not found)
- minor cleanup
- removed unnecessary build requirement

* Sat Mar 07 2009 Christian Krause <chkr@fedoraproject.org> - 0.11-1
- Initial spec file for Authen::Krb5::Admin
