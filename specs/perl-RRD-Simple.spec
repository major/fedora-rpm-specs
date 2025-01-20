Name:		perl-RRD-Simple
Version:	1.44
Release:	51%{?dist}
Summary:	Simple interface to create and store data in RRD files
License:	Apache-2.0
URL:		https://metacpan.org/release/RRD-Simple
Source0:	https://cpan.metacpan.org/authors/id/N/NI/NICOLAW/RRD-Simple-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(Module::Build)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(RRDs)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More)
# Optional Tests
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
# Runtime
Requires:	perl(Data::Dumper)
Requires:	perl(File::Copy)
Requires:	perl(File::Temp)

# Optional test dependency that breaks tests
# https://rt.cpan.org/Public/Bug/Display.html?id=46193
BuildConflicts:	perl(Test::Deep)

# Move to unversioned documentation directories from F-20
# https://fedoraproject.org/wiki/Changes/UnversionedDocdirs
%global rrd_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

%description
RRD::Simple provides a simple interface to RRDTool's RRDs module. This module
does not currently offer the fetch method that is available in the RRDs
module. It does, however, create RRD files with a sensible set of default RRA
Round Robin Archive) definitions, and can dynamically add new data source
names to an existing RRD file.

This module is ideal for quick and simple storage of data within an RRD file
if you do not need to, nor want to, bother defining custom RRA definitions.

%prep
%setup -q -n RRD-Simple-%{version}

# Don't want provides/requires from documentation
%global docfilt perl -p -e 's|%{rrd_docdir}\\S+||'
# RRD::Simple version should be from distribution version, not svn revision
%global verfilt perl -p -e 's/(perl\\(RRD::Simple\\) =) \\d+/\\1 %{version}/'
# Apply provides/requires filters
%global provfilt /bin/sh -c "%{docfilt} | %{__perl_provides} | %{verfilt}"
%global __perl_provides %{provfilt}
%global reqfilt /bin/sh -c "%{docfilt} | %{__perl_requires}"
%global __perl_requires %{reqfilt}

%build
# Prevent call-home query/timeout; not strictly necessary
AUTOMATED_TESTING=1 perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
LC_ALL=C ./Build test

%files
%license LICENSE NOTICE
%doc Changes README examples/ t/
%dir %{perl_vendorlib}/RRD/
%dir %{perl_vendorlib}/RRD/Simple/
%{perl_vendorlib}/RRD/Simple.pm
%doc %{perl_vendorlib}/RRD/Simple/Examples.pod
%{_mandir}/man3/RRD::Simple.3*
%{_mandir}/man3/RRD::Simple::Examples.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-44
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-41
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-38
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-35
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Paul Howarth <paul@city-fan.org> - 1.44-33
- Drop redundant buildroot cleaning in %%install section
- Drop redundant explicit %%clean section

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-31
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-28
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Petr Pisar <ppisar@redhat.com> - 1.44-26
- Adjust RPM version detection to SRPM build root without perl

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-25
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Paul Howarth <paul@city-fan.org> - 1.44-23
- Use %%global rather than %%define

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-21
- Perl 5.22 rebuild

* Tue Apr 21 2015 Paul Howarth <paul@city-fan.org> - 1.44-20
- Classify buildreqs by usage
- Drop %%defattr, redundant since rpm 4.4
- Use %%license where possible

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-19
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Paul Howarth <paul@city-fan.org> - 1.44-16
- Handle filtering of provides from unversioned doc-dirs from F-20
- Don't need to remove empty directories from the buildroot

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 1.44-15
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 1.44-12
- Perl 5.16 rebuild

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> - 1.44-11
- Fix provides/requires filters to work with rpm 4.9+ too
- Add buildreqs for perl core modules, which may be dual-lived
- Nobody else likes macros for commands
- Don't package INSTALL file

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.44-10
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Paul Howarth <paul@city-fan.org> - 1.44-8
- Rebuild with rrdtool 1.4.4 in Rawhide (#631131)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.44-7
- Mass rebuild with perl-5.12.0

* Thu Mar 11 2010 Paul Howarth <paul@city-fan.org> - 1.44-6
- Drop POD patch, only needed with Test::Pod 1.40

* Wed Mar  3 2010 Paul Howarth <paul@city-fan.org> - 1.44-5
- Change buildreq perl(Test::Deep) to a build conflict until upstream fixes
  failing t/32exported_function_interface.t (#464964, CPAN RT#46193)
- Fix broken POD (CPAN RT#50868)
- Cosmetic clean-up of spec
- Mark RRD::Simple::Examples POD as %%doc
- Run test suite in "C" locale for spec compatibility with old distributions
- Simplify provides/requires filter
- Fix versioned provide for perl(RRD::Simple)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.44-4
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 03 2008 Chris Weyl <cweyl@alumni.drew.edu> - 1.44-1
- Update to 1.44

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.43-3
- Rebuild for new perl

* Fri Jan 11 2008 Ralf Corsépius <rc040203@freenet.de> - 1.43-2
- BR: perl(Test::More) (BZ 419631)
- BR: perl(Test::Pod), perl(Test::Pod::Coverage)

* Wed Mar 21 2007 Chris Weyl <cweyl@alumni.drew.edu> - 1.43-1
- Update to 1.43

* Tue Feb 13 2007 Chris Weyl <cweyl@alumni.drew.edu> - 1.41-1
- Update to 1.41
- Use Build.PL directly

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.40-2
- Bump for mass rebuild

* Fri Aug 25 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.40-1
- Update to 1.40
- Minor spec cleanups

* Tue Jun 27 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.39-1
- Bump release for extras build

* Tue Jun 27 2006 Chris Weyl <cweyl@alumni.drew.edu> - 1.39-0
- Initial spec file for F-E
