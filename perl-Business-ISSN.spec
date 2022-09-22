Name:           perl-Business-ISSN
Version:        1.005
Release:        3%{?dist}
Summary:        Perl library for International Standard Serial Numbers
License:        Artistic 2.0
URL:            https://metacpan.org/release/Business-ISSN
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISSN-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
%{summary}.

%prep
%setup -q -n Business-ISSN-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
# currently only a placeholder in examples/
%doc Changes README.pod
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-2
- Perl 5.36 rebuild

* Thu May 19 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-1
- 1.005 bump

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.004-5
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.004-2
- Perl 5.32 rebuild

* Fri Mar 20 2020 Colin B. Macdonald <cbm@m.fsf.org> - 1.004-1
- Version bump, #1815371

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-2
- Perl 5.28 rebuild

* Thu May 10 2018 Colin B. Macdonald <cbm@m.fsf.org> - 1.003-1
- Version bump, #1576611

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Colin B. Macdonald <cbm@m.fsf.org> - 1.002-1
- Version bump, #1401732, #1400099

* Mon Dec 05 2016 Colin B. Macdonald <cbm@m.fsf.org> - 1.001-5
- Add another BR for #1400099

* Mon Dec 05 2016 Colin B. Macdonald <cbm@m.fsf.org> - 1.001-4
- Add BR for #1400099

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.001-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Colin B. Macdonald <cbm@m.fsf.org> - 1.001-1
- Version bump, fix spec file formatting

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.91-5
- Perl 5.22 rebuild

* Fri Nov 21 2014 Colin B. Macdonald <cbm@m.fsf.org> - 0.91-4
- Use license macro, minor edits.

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> - 0.91-3
- revision from other feedback on other packages.

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> - 0.91-2
- Replace nonsense autogenerated description (just use summary).

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> - 0.91-1
- Specfile autogenerated by cpanspec 1.78.
