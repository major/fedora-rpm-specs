Name:           perl-BackPAN-Index
Version:        0.42
Release:        27%{?dist}
Summary:        Interface to the BackPAN index
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/BackPAN-Index
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/BackPAN-Index-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(App::Cache) >= 0.37
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(autodie)
BuildRequires:  perl(CLASS) >= 1.00
BuildRequires:  perl(CPAN::DistnameInfo) >= 0.09
BuildRequires:  perl(DBD::SQLite) >= 1.25
BuildRequires:  perl(DBIx::Class) >= 0.08109
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Module::Build) >= 0.37
BuildRequires:  perl(Mouse) >= 0.64
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Class) >= 0.17
BuildRequires:  perl(Test::Compile) >= 0.11
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(URI) >= 1.54
Requires:       perl(CLASS) >= 1.00
Requires:       perl(DBD::SQLite) >= 1.25
Requires:       perl(DBIx::Class) >= 0.08109
Requires:       perl(Path::Class) >= 0.17
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Parse::BACKPAN::Packages is deprecated in favor of BackPAN::Index
Obsoletes:      perl-Parse-BACKPAN-Packages <= 0.35

%{?perl_default_filter:
%filter_from_requires /perl(CLASS)$/d;/perl(Path::Class)$/d
%perl_default_filter
}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\((CLASS|Path::Class)$\\)

%description
This downloads, caches and parses the BackPAN index into a local database
for efficient querying.

%prep
%setup -q -n BackPAN-Index-%{version}

sed -i -e '1s~^#!.*perl~#!%{__perl}~' examples/backpan.pl

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
BACKPAN_INDEX_TEST_NO_INTERNET=1 ./Build test

%files
%doc CHANGES examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-26
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-23
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-20
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-17
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-14
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-6
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 0.42-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.40-6
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 0.40-5
- Round Module::Build version to 2 digits

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Iain Arnell <iarnell@gmail.com> 0.40-3
- update filtering for rpm 4.9

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.40-2
- Perl mass rebuild

* Sun Mar 20 2011 Iain Arnell <iarnell@gmail.com> 0.40-1
- update to latest upstream version
- run tests with BACKPAN_INDEX_TEST_NO_INTERNET
- patch TestUtils.pm to force BACKPAN_INDEX_TEST_NO_INTERNET

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Iain Arnell <iarnell@gmail.com> 0.39-2
- additional buildrequires for dual-lived modules
- filter underspecified requires

* Sun Dec 19 2010 Iain Arnell <iarnell@gmail.com> 0.39-1
- Specfile autogenerated by cpanspec 1.78.
- obsoletes perl-Parse-BACKPAN-Packages
