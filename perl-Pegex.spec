Name:           perl-Pegex
Version:        0.75
Release:        10%{?dist}
Summary:        Pegex Parser Generator
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pegex
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(XXX) >= 0.33
BuildRequires:  perl(YAML::PP) >= 0.018
BuildRequires:  perl(Safe)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(File::ShareDir::Install)
Requires:       perl(JSON::PP)
Requires:       perl(Scalar::Util)
Requires:       perl(XXX) >= 0.33
Requires:       perl(YAML::PP) >= 0.018

%description
Pegex is an Acmeist parser framework. It is a PEG parser grammar syntax,
combined with PCRE compatible regular expressions as the match tokens.
Pegex draws heavily from Perl 6 rules, but works equivalently in many
modern programming languages.

%prep
%setup -q -n Pegex-%{version}
## Remove bundled modules
#rm -r ./inc
#sed -i '79,$ d' Makefile.PL
sed -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING example META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-3
- Perl 5.32 rebuild

* Wed Mar 11 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.75-2
- Add BuildRequires perl(Safe)

* Mon Feb 17 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.75-1
- Update to 0.75

* Mon Jan 27 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.74-1
- Update to 0.74
- Change a lot of BuildRequires and Requires

* Mon Jan 06 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.72-1
- Update to 0.72

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-4
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Petr Pisar <ppisar@redhat.com> - 0.70-2
- Do not depend on bundled TestML
- Remove perl_bootstrap code because perl-TestML >= 0.54_05 does not require
  perl-Pegex

* Mon Nov 12 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.70-1
- Update to 0.70

* Fri Aug 31 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.65-1
- Update to 0.65
- Add dependency perl-JSON-PP

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-4
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.64-1
- Update to 0.64

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.63-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.63-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.63-1
- Update to 0.63

* Wed Sep 14 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.61-2
- remove tests that fails

* Thu Jun 16 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.61-1
- Update to 0.61

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-7
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-2
- Perl 5.22 rebuild

* Wed Feb 04 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.60-1
- Update to 0.60
- BuildRequires perl(File::ShareDir::Install) added

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-2
- Perl 5.20 rebuild

* Fri Aug 08 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.45-1
- Update to 0.45

* Thu Aug 07 2014 Petr Pisar <ppisar@redhat.com> - 0.44-2
- Finish bootstrap

* Thu Jul 31 2014 Petr Pisar <ppisar@redhat.com> - 0.44-1
- 0.44 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.21-2
- Perl 5.18 rebuild

* Mon Feb 18 2013 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.21-1
- Update to 0.21

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.11-6
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.11-2
- rebuild with new Perl version

* Wed Oct 27 2010 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.11-1
- remove unnecessary BuildRequires

* Sun Oct 03 2010 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.10-1
- BuildRequires perl(Test::Builder) added
- Specfile autogenerated by cpanspec 1.78.
