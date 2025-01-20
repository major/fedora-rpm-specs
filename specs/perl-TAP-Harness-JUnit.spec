Name:           perl-TAP-Harness-JUnit
Version:        0.42
Release:        30%{?dist}
Summary:        Generate JUnit compatible output from TAP results
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/TAP-Harness-JUnit
Source0:        https://cpan.metacpan.org/authors/id/J/JL/JLAVALLEE/TAP-Harness-JUnit-%{version}.tar.gz
Patch0:         perl-TAP-Harness-JUnit-0.32-ascii.patch

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
Requires:       perl(TAP::Harness) >= 3.05
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(TAP::Harness) >= 3.05
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(TAP::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Encode)

%{?perl_default_filter}

%description
The only difference between this module and TAP::Harness is that this adds
mandatory 'xmlfile' argument, that causes the output to be formatted into
XML in format similar to one that is produced by JUnit testing framework.


%prep
%setup -q -n TAP-Harness-JUnit-%{version}
%patch -P0 -p1 -b .ascii


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test || :


%files
%doc README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.42-29
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-22
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-19
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-2
- Perl 5.22 rebuild

* Sun Feb 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.42-1
- Update to 0.42

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.41-2
- Perl 5.18 rebuild

* Sun Feb 10 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.41-1
- Update to 0.41

* Sat Feb 02 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40-1
- Update to 0.40

* Sun Jan 27 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.39-1
- Update to 0.39

* Sun Nov 11 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.38-1
- Update to 0.38

* Sat Oct 06 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.37-1
- Update to 0.37
- Clean up spec file
- Add perl default filter

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.36-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.36-2
- Perl mass rebuild

* Wed Jun 15 2011 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.36-1
- Upstream bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.32-6
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.32-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.32-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.32-2
- Apply the ASCII patch, disable test

* Mon Jul 13 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.32-1
- New upstream release. Stupid, Lubomir, stupid.

* Mon Jul 13 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.31-1
- New upstream release

* Fri Apr 17 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.30-1
- New upstream release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 4 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.26-1
- New upstream release
- Re-enable regression tests

* Mon Nov 3 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.25-0.2
- Disable tests due to ambiguity in whitespace within rest results

* Mon Nov 3 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.25-0.1
- Ensure valid UTF-8 output
- Do not report failed plain and bad return value as two failures

* Fri Oct 31 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.24-1
- New upstream release

* Tue Aug 19 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.22-1
- New upstream release
- Enhanced documentation
- Fixed handling of tests with bad plan
- Ignore SKIP and TODO tests in JUnit

* Wed Aug 06 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.21-2
- Add BRs for enabled tests

* Wed Aug 06 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.21-1
- New usptream release

* Thu Jul 31 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.20-1
- New usptream release

* Wed Jul 30 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.01-2
- Allow test names to be specified without comments

* Mon Jul 28 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.01-1
- Specfile autogenerated by cpanspec 1.75.
- Fixed requires
