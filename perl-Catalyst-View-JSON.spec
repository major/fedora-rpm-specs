Name:           perl-Catalyst-View-JSON
Version:        0.37
Release:        12%{?dist}
Summary:        JSON view for your data
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Catalyst-View-JSON
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-View-JSON-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst::Exception)
BuildRequires:  perl(Catalyst::View)
BuildRequires:  perl(Encode)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003000
BuildRequires:  perl(MRO::Compat)
# Tests:
BuildRequires:  perl(Catalyst) >= 5.6
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(FindBin)
# HTTP::Request::AsCGI not needed with Catalyst >= 5.89
BuildRequires:  perl(lib)
# Plack::Test not used
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML)
Requires:       perl(JSON::MaybeXS) >= 1.003000

%description
Catalyst::View::JSON is a Catalyst View handler that returns stash data in
JSON format.

%prep
%setup -q -n Catalyst-View-JSON-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-8
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-5
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-2
- Perl 5.30 rebuild

* Wed May 22 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-1
- 0.37 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-2
- Perl 5.24 rebuild

* Wed Mar 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-1
- 0.36 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Petr Pisar <ppisar@redhat.com> - 0.35-1
- 0.35 bump
- License corrected from (GPL+ or Artistic 2.0) to (GPL+ or Artistic)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-13
- Perl 5.22 rebuild

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 0.30-10
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.30-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.30-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.30-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun  1 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.30-1
- update

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.26-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.26-2
- rebuild against perl 5.10.1

* Sun Sep 06 2009 Iain Arnell <iarnell@gmail.com> 0.26-1
- update to latest upstream release

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.25-1
- auto-update to 0.25 (by cpan-spec-update 0.01)
- added a new br on perl(MRO::Compat) (version 0)
- added a new br on perl(Test::More) (version 0)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 07 2008 Caolán McNamara <caolanm@redhat.com> 0.24-2
- rebuild for dependancies

* Thu Mar 27 2008 Simon Wilkinson <simon@sxw.org.uk> 0.24-1
- Specfile autogenerated by cpanspec 1.73.
