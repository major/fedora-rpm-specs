Name:           perl-Business-ISMN
Version:        1.202
Release:        6%{?dist}
Summary:        Perl library for International Standard Music Numbers
License:        Artistic 2.0
URL:            https://metacpan.org/release/Business-ISMN
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISMN-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More) >= 1.00
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Tie::Cycle) >= 1.21
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Recommends:     perl(GD::Barcode::EAN13)

%description
%{summary}.

%prep
%setup -q -n Business-ISMN-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.pod
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.202-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.202-5
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.202-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.202-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.202-2
- Perl 5.34 rebuild

* Thu Mar 11 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.202-1
- 1.202 bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.201-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.201-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.201-6
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.201-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.201-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.201-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 20 2018 Colin B. Macdonald <cbm@m.fsf.org> - 1.201-1
- Version bump, #1640987

* Sun Jul 15 2018 Colin B. Macdonald <cbm@m.fsf.org> - 1.132-1
- Version bump, #1601159

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.131-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.131-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.131-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.131-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.131-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.131-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Colin B. Macdonald <cbm@m.fsf.org> - 1.131-1
- Version bump, #1401731

* Mon Dec 05 2016 Colin B. Macdonald <cbm@m.fsf.org> - 1.13-6
- Add BR on Test::Prereq, re-order BR list

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.13-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.13-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Colin B. Macdonald <cbm@m.fsf.org> 1.13-1
- Version bump, drop patch

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-5
- Perl 5.22 rebuild

* Fri Nov 21 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.11-4
- additional BuildRequires, minor edits.

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.11-3
- revision from other feedback on other packages.

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.11-2
- Replace nonsense autogenerated description.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 1.11-1
- Specfile autogenerated by cpanspec 1.78.
