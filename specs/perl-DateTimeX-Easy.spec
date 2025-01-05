# Add a support for Date::Manip time objects
%bcond_without perl_DateTimeX_Easy_enables_Date_Manip
# Add a support for ICal time format
%bcond_without perl_DateTimeX_Easy_enables_ical

Name:       perl-DateTimeX-Easy
Version:    0.092
Release:    1%{?dist}
# lib/DateTimeX/Easy.pm:            GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:                          GPL-1.0-or-later OR Artistic-1.0-Perl
# README:                           GPL-1.0-or-later OR Artistic-1.0-Perl
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Parse a date/time string using the best method available
Source:     https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/DateTimeX-Easy-%{version}.tar.gz
Url:        https://metacpan.org/release/DateTimeX-Easy
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Flexible)
BuildRequires:  perl(DateTime::Format::Natural)
# 2.63 minimal version in META is superfluous
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Zone)
BuildRequires:  perl(vars)
# YAML not used, CPAN RT#144022
# Optional run-time:
# DateTime::Format::DateManip has been made optional due to instability
%if %{with perl_DateTimeX_Easy_enables_ical}
BuildRequires:  perl(DateTime::Format::ICal)
%endif
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
%if %{with perl_DateTimeX_Easy_enables_Date_Manip}
Suggests:       perl(DateTime::Format::DateManip)
%endif
%if %{with perl_DateTimeX_Easy_enables_ical}
Recommends:     perl(DateTime::Format::ICal)
%endif

# Do not export dependency on private module
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTimeX::Easy::DateParse\\)

%description
DateTimeX::Easy makes DateTime object creation quick and easy. It uses a
variety of DateTime::Format packages to do the bulk of the parsing, with
some custom tweaks to smooth out the rough edges (mainly concerning
timezone detection and selection).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n DateTimeX-Easy-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS README
%dir %{perl_vendorlib}/DateTimeX
%{perl_vendorlib}/DateTimeX/Easy
%{perl_vendorlib}/DateTimeX/Easy.pm
%{_mandir}/man3/DateTimeX::Easy.*
%{_mandir}/man3/DateTimeX::Easy::*.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 03 2025 Petr Pisar <ppisar@redhat.com> - 0.092-1
- 0.092 bump

* Tue Sep 24 2024 Petr Pisar <ppisar@redhat.com> - 0.091-7
- Adapt the tests and a documentation to changes in
  perl-DateTime-TimeZone-2.63 (bug #2314392)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.091-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.091-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.091-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.091-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.091-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 26 2022 Petr Pisar <ppisar@redhat.com> - 0.091-1
- 0.091 bump

* Mon Aug 15 2022 Petr Pisar <ppisar@redhat.com> - 0.090-1
- 0.090 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.089-32
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Petr Pisar <ppisar@redhat.com> - 0.089-29
- Adapt tests to DateTime-Format-Flexible-0.34 (bug #1982677)
- Package the tests

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.089-28
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.089-25
- Perl 5.32 rebuild

* Tue Jun 02 2020 Petr Pisar <ppisar@redhat.com> - 0.089-24
- Modernize a spec file

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.089-21
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.089-18
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.089-15
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.089-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.089-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.089-10
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.089-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.089-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.089-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.089-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.089-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.089-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.089-3
- Perl 5.16 rebuild

* Wed Jan 25 2012 Petr Pisar <ppisar@redhat.com> - 0.089-2
- Do not export dependency on private module DateTimeX::Easy::DateParse

* Tue Jan 24 2012 Petr Pisar <ppisar@redhat.com> - 0.089-1
- 0.089 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.088-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.088-6
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.088-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.088-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.088-3
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Dec 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.088-2
- Add missing changelog entry for 0.088-1.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.088-1
- Update to 0.88.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.087-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.087-4
- rebuild against perl 5.10.1

* Tue Aug 04 2009 Ralf Corsépius <corsepiu@fedoraproject.org> 0.087-3
- Fix mass rebuild breakdown: Add --skipdeps.
- Use Test::Most.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.087-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.087-1
- auto-update to 0.087 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.085-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 12 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.085-1
- update to 0.085
- touch up for review

* Sun Dec 07 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.084-0.1
- update to 0.084

* Sat Oct 11 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.082-1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.1)
