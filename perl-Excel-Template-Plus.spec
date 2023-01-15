Name:           perl-Excel-Template-Plus
Version:        0.06
Release:        21%{?dist}
Summary:        Extension to the Excel::Template module
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Excel-Template-Plus
Source0:        https://cpan.metacpan.org/modules/by-module/Excel/Excel-Template-Plus-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Excel::Template)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Moose) >= 0.18
BuildRequires:  perl(MooseX::Param) >= 0.01
BuildRequires:  perl(Spreadsheet::ParseExcel)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception) >= 0.21
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
Requires:       perl(Moose) >= 0.18
Requires:       perl(MooseX::Param) >= 0.01

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Moose\\)$
%global __requires_exclude %__requires_exclude|^perl\\(MooseX::Param\\)$

%description
This module is an extension of the Excel::Template module, which allows
the user to use various "engines" from which you can create Excel files
through Excel::Template.
The idea is to use the existing (and very solid) excel file generation
code in Excel::Template, but to extend its more templatey bits with more
powerful options.
The only engine currently provided is the Template Toolkit engine, which
replaces Excel::Template's built in template features (the LOOP, and IF
constructs) with the full power of TT. This is similar to the module
Excel::Template::TT, but expands on that even further to try and create
a more extensive system.

%prep
%setup -q -n Excel-Template-Plus-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-20
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-17
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Sven Nierlein <sven.nierlein@consol.de> 0.06-1
- new upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Sven Nierlein <sven.nierlein@consol.de> 0.05-4
- updated build requires / requires

* Tue May 20 2014 Sven Nierlein <sven.nierlein@consol.de> 0.05-3
- added perl build requires / requires according to cpanspec
- added perl compat requires

* Sun Apr 06 2014 Sven Nierlein <sven.nierlein@consol.de> 0.05-2
- added perl build requires
- added Changes and README
- use DESTDIR as install target folder
- removed unnecessary build steps

* Sun Mar 23 2014 Sven Nierlein <sven.nierlein@consol.de> 0.05-1
- Specfile created
