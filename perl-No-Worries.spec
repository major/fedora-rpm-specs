%global cpan_name No-Worries

Name:           perl-%{cpan_name}
Version:        1.7
Release:        6%{?dist}
Summary:        Perl coding without worries
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LC/LCONS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI::Escape)
# and for better testing...
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%description
This module and its sub-modules ease coding by providing consistent convenient
functions to perform frequently used programming tasks.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
rm -fr $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.7-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Lionel Cons <lionel.cons@cern.ch> - 1.7-1
- Updated to 1.7 (rhbz #2014403)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-2
- Perl 5.30 rebuild

* Wed Apr 03 2019 Lionel Cons <lionel.cons@cern.ch> 1.6-1
- Upgrade to 1.6 upstream version, rhbz #1695472.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.5-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 01 2017 Lionel Cons <lionel.cons@cern.ch> 1.5-1
- Upgrade to 1.5 upstream version, rhbz #1477136.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.4-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Lionel Cons <lionel.cons@cern.ch> 1.4-1
- Upgrade to 1.4 upstream version, rhbz #1397222.

* Wed Oct 05 2016 Lionel Cons <lionel.cons@cern.ch> 1.3-1
- Upgrade to 1.3 upstream version, rhbz #1381896.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 03 2015 Lionel Cons <lionel.cons@cern.ch> 1.2-6
- Spec file cleanup.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Massimo Paladin <massimo.paladin@gmail.com> 1.2-1
- Updating to upstream 1.2, rhbz #1086545.

* Fri Jan 31 2014 Massimo Paladin <massimo.paladin@gmail.com> 1.1-1
- Updating to upstream 1.1, rhbz #1054233.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Pisar <ppisar@redhat.com> - 1.0-2
- Perl 5.18 rebuild

* Wed May 22 2013 Massimo Paladin <massimo.paladin@gmail.com> 1.0-1
- Updating to upstream 1.0, rhbz #965606.

* Wed Feb 27 2013 Massimo Paladin <massimo.paladin@gmail.com> 0.9-1
- Updating to upstream 0.9, rhbz #916064.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Massimo Paladin <massimo.paladin@gmail.com> 0.8-1
- Updating to upstream 0.8 rhbz#895876.

* Wed Nov 14 2012 Massimo Paladin <massimo.paladin@gmail.com> 0.7-1
- Updating to latest upstream version.

* Thu Oct 04 2012 Massimo Paladin <massimo.paladin@gmail.com> 0.6-1
- Updating to latest upstream version.

* Wed Aug 01 2012 Massimo Paladin <massimo.paladin@gmail.com> 0.5-1
- Updating to latest upstream version.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 0.4-2
- Perl 5.16 rebuild

* Wed Jul 04 2012 Massimo Paladin <massimo.paladin@gmail.com> 0.4-1
- Updating to latest upstream version.

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 0.3-3
- Perl 5.16 rebuild

* Mon Jun 11 2012 Massimo Paladin <massimo.paladin@gmail.com> 0.3-2
- Cleaning the spec file.

* Wed May 30 2012 Lionel Cons <lionel.cons@cern.ch> 0.3-1
- Specfile autogenerated by cpanspec 1.78.
- Specfile cleanup.
