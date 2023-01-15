Name:           perl-PPI-PowerToys
Version:        0.14
Release:        37%{?dist}
Summary:        Handy collection of small PPI-based utilities
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/PPI-PowerToys
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/PPI-PowerToys-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install::DSL) >= 0.87
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(File::Find::Rule) >= 0.30
BuildRequires:  perl(File::Find::Rule::Perl) >= 0.03
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(PPI::Document) >= 1.201
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version) >= 0.74
BuildRequires:  perl(warnings)
# Tests only:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IPC::Run3) >= 0.034
BuildRequires:  perl(PPI)
BuildRequires:  perl(Probe::Perl) >= 0.01
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Script) >= 1.03

# Remove underspecified dependecies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(File::Find::Rule\\)$
%global __requires_exclude %__requires_exclude|perl\\(File::Find::Rule::Perl\\)$
%global __requires_exclude %__requires_exclude|perl\\(File::Spec\\)$
%global __requires_exclude %__requires_exclude|perl\\(Getopt::Long\\)$
%global __requires_exclude %__requires_exclude|perl\\(PPI::Document\\)$
%global __requires_exclude %__requires_exclude|perl\\(version\\)$

%description
The PPI PowerToys are a small collection of utilities for working with Perl
files, modules and distributions.

%prep
%setup -q -n PPI-PowerToys-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

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
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-36
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-33
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-30
- Perl 5.32 rebuild

* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-29
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-26
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-23
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-20
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Petr Pisar <ppisar@redhat.com> - 0.14-19
- Modernize spec file

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-18
- Perl 5.26 rebuild

* Thu May 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-17
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-15
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-12
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 0.14-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.14-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-3
- add new filter for rpm 4.9

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.14-2
- Perl mass rebuild

* Fri Jun 17 2011 Petr Pisar <ppisar@redhat.com> 0.14-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr
