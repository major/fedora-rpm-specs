Name:			perl-Spreadsheet-WriteExcel
Version:		2.40
Release:		33%{?dist}
Summary:		Write formatted text and numbers to a cross-platform Excel binary file
License:		GPL-1.0-or-later OR Artistic-1.0-Perl
URL:			https://metacpan.org/release/Spreadsheet-WriteExcel
Source0:		https://cpan.metacpan.org/modules/by-module/Spreadsheet/Spreadsheet-WriteExcel-%{version}.tar.gz
Patch0:			Spreadsheet-WriteExcel-2.40-utf8.patch
BuildArch:		noarch
# Build
BuildRequires:		coreutils
BuildRequires:		findutils
BuildRequires:		make
BuildRequires:		perl-generators
BuildRequires:		perl-interpreter
BuildRequires:		perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:		perl(autouse)
BuildRequires:		perl(Carp)
BuildRequires:		perl(Date::Calc)
BuildRequires:		perl(Date::Manip)
BuildRequires:		perl(Digest::MD4)
BuildRequires:		perl(Encode)
BuildRequires:		perl(Exporter)
BuildRequires:		perl(File::Temp)
BuildRequires:		perl(FileHandle)
BuildRequires:		perl(Getopt::Long)
BuildRequires:		perl(integer)
BuildRequires:		perl(OLE::Storage_Lite) >= 0.19
BuildRequires:		perl(Parse::RecDescent)
BuildRequires:		perl(Pod::Usage)
BuildRequires:		perl(POSIX)
BuildRequires:		perl(strict)
BuildRequires:		perl(Time::Local)
BuildRequires:		perl(vars)
# Test Suite
BuildRequires:		perl(Test::More)
# Dependencies
Requires:		perl(Date::Calc)
Requires:		perl(Date::Manip)
Requires:		perl(Digest::MD4)
Requires:		perl(Encode)
Requires:		perl(File::Temp)
Requires:		perl(OLE::Storage_Lite) >= 0.19
Requires:		perl(Parse::RecDescent)

%{?perl_default_filter:
%filter_requires_in %{perl_vendorlib}/Spreadsheet/WriteExcel/Examples.pm
%perl_default_filter
}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}Spreadsheet/WriteExcel/Examples\\.pm$

%description
The Spreadsheet::WriteExcel module can be used to create a cross-
platform Excel binary file. Multiple worksheets can be added to a
workbook and formatting can be applied to cells. Text, numbers,
formulas, hyperlinks and images can be written to the cells.

The Excel file produced by this module is compatible with 97,
2000, 2002 and 2003. Generated files are also compatible with the
spreadsheet applications Gnumeric and OpenOffice.org.

This module cannot be used to read an Excel file. See
Spreadsheet::ParseExcel or look at the main documentation for some
suggestions. This module cannot be used to write to an existing
Excel file.

%prep
%setup -q -n Spreadsheet-WriteExcel-%{version} 

# Fix encoding of Changes file
%patch -P0

# Fix line endings
perl -pi -e 's/\r\n/\n/g' examples/*.txt

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README docs/ examples/
%{_bindir}/chartex
%{perl_vendorlib}/Spreadsheet/
%{_mandir}/man1/chartex.1*
%{_mandir}/man3/Spreadsheet::WriteExcel.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::BIFFwriter.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Big.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Chart.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Chart::Area.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Chart::Bar.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Chart::Column.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Chart::External.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Chart::Line.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Chart::Pie.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Chart::Scatter.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Chart::Stock.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Examples.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Format.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Formula.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::OLEwriter.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Properties.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Utility.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Workbook.3*
%{_mandir}/man3/Spreadsheet::WriteExcel::Worksheet.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug  6 2024 Miroslav Suchý <msuchy@redhat.com> - 2.40-32
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-25
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-22
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-19
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  8 2019 Paul Howarth <paul@city-fan.org> - 2.40-17
- Spec tidy-up
  - Use author-independent source URL
  - Classify buildreqs by usage
  - Convert Changes file to UTF-8
  - Fix permissions verbosely
  - Don't need to remove empty directories from the buildroot
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-15
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-12
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar  5 2014 Tom Callaway <spot@fedoraproject.org> - 2.40-1
- 2.40

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 2.37-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.37-10
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Iain Arnell <iarnell@gmail.com> 2.37-8
- add __requires_exclude_from for rpm 4.9

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.37-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.37-5
- used new filtering according to guidelines to resolve useless requirement

* Fri Jan 28 2011 Oliver Falk <oliver@linux-kernel.at> - 2.37-4
- Rebuild

* Thu Jan 27 2011 Oliver Falk <oliver@linux-kernel.at> - 2.37-3
- Rebuild with new perl-5.12.3

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.37-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jul 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.37-1
- update to 2.37

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.36-2
- Mass rebuild with perl-5.12.0

* Wed Jan 27 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.36-1
- update to 2.36

* Fri Jan  8 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.34-1
- update to 2.34

* Mon Dec  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.30-1
- update to 2.30

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.25-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.25-1
- update to 2.25

* Fri Feb 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 2.21-3
- remove new provides/requires rpm is finding on f11 (RHBZ#473874, also
  visible at http://tinyurl.com/cp75ml koji build log for 2.21-2/f11)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.21-1
- update to 2.21

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.20-2
- rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.20-1
- 2.20

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.18-1
- 2.18
- license tag fix

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.17-2
- bump for fc6

* Fri Jul  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.17-1
- bump to 2.17

* Fri Mar 31 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.16-1
- bump to 2.16

* Tue Jan 10 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.15-1
- bump to 2.15

* Wed May 11 2005 Oliver Falk <oliver@linux-kernel.at>		- 2.14-1
- Update
- Add a complete URL for Source0
- Beautifying (fix identations and make it look more like the
  spectemplate-perl.spec)

* Tue May 10 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.13-3
- more spec cleanups

* Sun Apr 24 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.13-2
- spec cleanups

* Thu Apr 21 2005 Oliver Falk <oliver@linux-kernel.at> 2.13-1
- Update

* Thu Apr 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.12-3
- rework spec to match template
- set to noarch

* Thu Apr 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.12-2
- Add MODULE_COMPAT requires line

* Fri Apr 1 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.12-1
- initial package
