Name:		perl-Rose-DB-Object
Version:	0.820
Release:	10%{?dist}
Summary:	Extensible, high performance object-relational mapper (ORM)
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Rose-DB-Object
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Rose-DB-Object-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Bit::Vector)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Clone)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(overload)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Rose::DateTime::Util)
BuildRequires:	perl(Rose::DB)
BuildRequires:	perl(Rose::Object)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Memory::Cycle)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Time::Clock)
BuildRequires:	perl(warnings)

%global __requires_exclude ^perl\\(Rose::(DB|Object)::
%{?perl_default_filter}


%description
Rose::DB::Object is a base class for objects that encapsulate a single row
in a database table. Rose::DB::Object-derived objects are sometimes simply
called "Rose::DB::Object objects" in this documentation for the sake of
brevity, but be assured that derivation is the only reasonable way to use
this class.

%prep
%setup -q -n Rose-DB-Object-%{version}
find . -type f -executable -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
export AUTOMATED_TESTING=1
make test

%files
%doc Changes
%{perl_vendorlib}/Rose/DB/
%{_mandir}/man3/Rose::DB::Object*.3pm*

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.820-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.820-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.820-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.820-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.820-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.820-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.820-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.820-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 26 2021 Bill Pemberton <wfp5p@worldbroken.com> - 0.820-2
- update spec to remove filter_from_requires

* Sat Jun 26 2021 Bill Pemberton <wfp5p@worldbroken.com> - 0.820-1
- Update to 0.820 (#1976484)
- Added missing semicolon(!) in Rose::DB::Object::Metadata.

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.819-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.819-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.819-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.819-2
- Perl 5.32 rebuild

* Thu Jun 18 2020 Bill Pemberton <wfp5p@worldbroken.com> - 0.819-1
- update to 0.819

* Mon Jun  8 2020 Bill Pemberton <wfp5p@worldbroken.com> - 0.818-1
- update to 0.818

* Mon Apr  6 2020 Bill Pemberton <wfp5p@worldbroken.com> - 0.817-2
- add requires for more tests

* Mon Apr  6 2020 Bill Pemberton <wfp5p@worldbroken.com> - 0.817-1
- update to 0.817
- Updated to support DBD::Pg 3.8.0 and later

* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.815-17
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.815-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.815-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.815-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.815-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.815-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.815-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.815-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.815-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.815-8
- Rebuild due to bug in RPM (RHBZ #1468476)

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.815-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.815-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.815-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.815-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.815-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.815-2
- Perl 5.22 rebuild

* Tue Mar 24 2015 Bill Pemberton <wfp5p@worldbroken.com> - 0.815-1
- update to version 0.815
- updates more project URLs


* Wed Mar 18 2015 Bill Pemberton <wfp5p@worldbroken.com> - 0.814-1
- update to version 0.814
- updates project URLs

* Wed Nov 12 2014 Bill Pemberton <wfp5p@worldbroken.com> - 0.813-1
- Update to version 0.813
- This version has several bug and documentation fixes.

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.811-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.811-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Bill Pemberton <wfp5p@worldbroken.com> - 0.811-1
- update to version 0.811
- fixes a bug that prevented many-to-many map records from being saved
  to the database

* Mon Jan 20 2014 Bill Pemberton <wfp5p@worldbroken.com> - 0.810-1
- update to version 0.810

* Thu Dec  5 2013 Bill Pemberton <wfp5p@worldbroken.com> - 0.809-1
- update to version 0.808
- fixes precision and scale for auto-loaded numeric column metadata

* Mon Nov  4 2013 Bill Pemberton <wfp5p@worldbroken.com> - 0.808-1
- update to version 0.808
- fixes typos

* Tue Sep  3 2013 Bill Pemberton <wfp5p@worldbroken.com> - 0.807-1
- update to version 0.807
- Fixes inheritance of Rose::DB::Object::Cached's cached_objects_expire_in 
  attribute.

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.806-2
- Perl 5.18 rebuild

* Mon Jun 10 2013 Bill Pemberton <wfp5p@virginia.edu> - 0.806-1
- update to version 0.806
- fixes bug under perl 5.17

* Mon Mar 11 2013 Bill Pemberton <wfp5p@virginia.edu> - 0.805-1
- update to version 0.805

* Mon Feb  4 2013 Bill Pemberton <wfp5p@virginia.edu> - 0.804-1
- update to version 0.804

* Mon Jan  7 2013 Bill Pemberton <wfp5p@virginia.edu> - 0.803-1
- update to version 0.803

* Mon Nov 26 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.801-1
- update to version 0.801

* Mon Sep 10 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.800-1
- update to version 0.800

* Wed Sep  5 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.799-1
- update to version 0.799

* Mon Aug  6 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.798-4
- Update BuildRequires

* Mon Jul 16 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.798-3
- remove buildroot and clean
- remove defattr from files section
- add constant to BuildRequires

* Tue Jun 26 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.798-2
- Be more specific in files section

* Tue Jun 26 2012 Bill Pemberton <wfp5p@virginia.edu> - 0.798-1
- Initial version
