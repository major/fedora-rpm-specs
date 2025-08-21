Name:		perl-XML-Rules
Version:	1.16
Release:	38%{?dist}
Summary:	Parse XML and specify what and how to keep/process for individual tags
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/XML-Rules
Source0:	https://cpan.metacpan.org/modules/by-module/XML/XML-Rules-%{version}.tar.gz
Patch0:		XML-Rules-1.10-add-shebang.patch
BuildArch:	noarch

# build requirements
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build)
BuildRequires:	sed

# module requirements
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XML::Parser) >= 2.00
BuildRequires:	perl(XML::Parser::Expat) >= 2.00

# test requirements
BuildRequires:	perl(Encode)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(utf8)

# optional tests
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04

# dependencies
# (none)

%description
The XML::Rules module provides an API layer on top of XML::Parser.  It
allows you to specify rules that are subroutines to be run once a tag
is fully parsed and either process the data from the tag itself and
its children or specify what parts of the data and how to add to the
data structure being built for the parent tag.

%prep
%setup -q -n XML-Rules-%{version}

# fix end of line encoding
find . -type f -exec sed -i 's/\r//' {} \;

# the patch assumes the end of lines have already been fixed
%patch -P0 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README example
%license LICENSE
%{_bindir}/dtd2XMLRules.pl
%{_bindir}/xml2XMLRules.pl
%{perl_vendorlib}/XML/
%{_mandir}/man3/XML::Rules.3*

%changelog
* Tue Aug 19 2025 Paul Howarth <paul@city-fan.org> - 1.16-38
- Use author-independent source URL
- Specify all dependencies
- Fix permissions verbosely

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 1.16-35
- Convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-28
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-25
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-22
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-19
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-16
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-13
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-11
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Bill Pemberton <wfp5p@worldbroken.com> - 1.16-9
- modernize spec file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-7
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.16-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 25 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.16-1
- update to version 1.16

* Thu Dec 13 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.15-1
- update to version 1.15

* Mon Oct 22 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.14-1
- update to version 1.14

* Mon Oct 15 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.13-1
- update to version 1.13

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1.10-8
- Perl 5.16 rebuild

* Thu Feb 23 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.10-7
- use a patch to add shebangs to bin scripts

* Wed Feb 22 2012 Bill Pemberton <wfp5p@viridian.itc.Virginia.EDU> - 1.10-6
- Move end of line fix to prep stage

* Wed Feb 22 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.10-5
- add comments to clarify why the various BuildRequires are needed
- add BuildRequires for XML::Parser and XML::Parser::Expat.  The build
  script fails if these are not installed at build time.

* Thu Feb 16 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.10-4
- Add the shebang lines in setup instead of install
- Remove explicit requires for XML::Parser and XML::Parser::Expat

* Thu Feb 16 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.10-3
- move dtd2XMLRules.pl and xml2XMLRules.pl to _bindir
- drop version requirements for XML::Parser and XML::Parser::Expat

* Mon Mar 21 2011 Bill Pemberton <wfp5p@virginia.edu> - 1.10-2
- include sample programs bin/dtd2XMLRules.pl and bin/xml2XMLRules.pl
  in doc
- remove blank line after description
- don't assume man pages end in .gz

* Wed Mar  9 2011 Bill Pemberton <wfp5p@virginia.edu> - 1.10-1
- Initial spec

