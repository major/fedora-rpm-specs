Name:           perl-DateTime-Format-Natural
Version:        1.19
Release:        2%{?dist}
Summary:        Create machine readable date/time with natural parsing logic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-Natural
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCHUBIGER/DateTime-Format-Natural-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::HiRes)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(Params::Validate) >= 1.15
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
# Tests only
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::MockTime::HiRes)
BuildRequires:  perl(Test::More)
Requires:       perl(Params::Validate) >= 1.15

%{?perl_default_filter}

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Params::Validate\\)$

%description
DateTime::Format::Natural takes a string with a human readable date/time
and creates a machine readable one by applying natural parsing logic.

%package Test
Summary:        Common test routines/data for perl-DateTime-Format-Natural
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Test
The DateTime::Format::Natural::Test class exports common test routines.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n DateTime-Format-Natural-%{version}
for f in Changes README; do
        iconv -f iso8859-1 -t utf-8 $f >$f.conf && mv $f.conf $f
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*.t
# Does not work for modules which are placed in %{perl_vendorlib}
rm %{buildroot}%{_libexecdir}/%{name}/t/00-load.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%doc Changes README
%dir %{perl_vendorlib}/DateTime
%dir %{perl_vendorlib}/DateTime/Format
%{perl_vendorlib}/DateTime/Format/Natural
%exclude %{perl_vendorlib}/DateTime/Format/Natural/Test.pm
%{perl_vendorlib}/DateTime/Format/Natural.pm
%{_bindir}/dateparse
%{_mandir}/man1/dateparse.*
%{_mandir}/man3/DateTime::Format::Natural.*
%{_mandir}/man3/DateTime::Format::Natural::*
%exclude %{_mandir}/man3/DateTime::Format::Natural::Test.*

%files Test
%{perl_vendorlib}/DateTime/Format/Natural/Test.pm
%{_mandir}/man3/DateTime::Format::Natural::Test.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-1
- 1.19 bump (rhbz#2335649)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-1
- 1.18 bump (rhbz#2242326)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 21 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-1
- 1.17 bump

* Wed Mar 22 2023 Petr Pisar <ppisar@redhat.com> - 1.16-2
- Run tests in parallel

* Sun Feb 05 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-1
- 1.16 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-1
- 1.15 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.13-2
- Perl 5.36 rebuild

* Mon Jan 24 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.13-1
- 1.13 bump
- Package tests

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-2
- Perl 5.34 rebuild

* Mon Mar 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-1
- 1.12 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-1
- 1.11 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-1
- 1.10 bump

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-2
- Perl 5.32 rebuild

* Mon May 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-1
- 1.09 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-1
- 1.08 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-2
- Perl 5.30 rebuild

* Mon Apr 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-1
- 1.07 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-1
- 1.06 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-2
- Perl 5.26 rebuild

* Mon Apr 24 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-1
- 1.05 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 26 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-1
- 1.04 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 03 2015 Petr Šabata <contyk@redhat.com> - 1.03-1
- 1.03 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-2
- Perl 5.22 rebuild

* Fri Nov 14 2014 Petr Šabata <contyk@redhat.com> - 1.02-1
- 1.02 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1.01-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 21 2012 Iain Arnell <iarnell@gmail.com> 1.01-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.00-2
- Perl 5.16 rebuild

* Sat Jun 09 2012 Iain Arnell <iarnell@gmail.com> 1.00-1
- update to latest upstream version

* Mon May 07 2012 Iain Arnell <iarnell@gmail.com> 0.99-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 06 2011 Iain Arnell <iarnell@gmail.com> 0.98-1
- update to latest upstream version

* Sat Aug 27 2011 Iain Arnell <iarnell@gmail.com> 0.97-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.96-2
- Perl mass rebuild

* Sun Jun 05 2011 Iain Arnell <iarnell@gmail.com> 0.96-1
- update to latest upstream version

* Wed May 18 2011 Iain Arnell <iarnell@gmail.com> 0.95-1
- update to latest upstream version

* Sun Apr 03 2011 Iain Arnell <iarnell@gmail.com> 0.94-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Iain Arnell <iarnell@gmail.com> 0.93-1
- update to latest upstream version

* Sat Jan 15 2011 Iain Arnell <iarnell@gmail.com> 0.92-1
- update to latest upstream version

* Sun Dec 12 2010 Iain Arnell <iarnell@gmail.com> 0.91-2
- split DateTime::Format::Natural::Test into separate sub-package to avoid
  runtime dependecy on Test::More

* Tue Nov 02 2010 Iain Arnell <iarnell@gmail.com> 0.91-1
- update to latest upstream version

* Thu Oct 07 2010 Iain Arnell <iarnell@gmail.com> 0.90-1
- regular update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Aug 06 2010 Iain Arnell <iarnell@gmail.com> 0.89-1
- update to latest upstream version

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 0.88-1
- update to latest upstream

* Sun May 30 2010 Iain Arnell <iarnell@gmail.com> 0.87-1
- update to latest upstream

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.86-2
- Mass rebuild with perl-5.12.0

* Wed Apr 21 2010 Iain Arnell <iarnell@gmail.com> 0.86-1
- update to latest upstream version

* Sun Mar 14 2010 Iain Arnell <iarnell@gmail.com> 0.85-1
- update to latest upstream version
- use perl_default_filter

* Thu Feb 25 2010 Iain Arnell <iarnell@gmail.com> 0.84-1
- update to latest upstream version

* Thu Jan 14 2010 Iain Arnell <iarnell@gmail.com> 0.83-1
- update to latest upstream version

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 0.82-1
- update to latest upstream version

* Wed Dec 09 2009 Iain Arnell <iarnell@gmail.com> 0.81-1
- update to latest upstream version

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.80-2
- rebuild against perl 5.10.1

* Fri Oct 30 2009 Iain Arnell <iarnell@gmail.com> 0.80-1
- update to latest upstream version

* Sun Sep 20 2009 Iain Arnell <iarnell@gmail.com> 0.79-1
- update to latest upstream version

* Sat Aug 29 2009 Iain Arnell <iarnell@gmail.com> 0.78-1
- update to latest upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Iain Arnell <iarnell@gmail.com> 0.77-1
- update to latest upstream version

* Sat Apr 11 2009 Iain Arnell <iarnell@gmail.com> 0.76-1
- update to latest upstream release

* Sat Feb 28 2009 Iain Arnell <iarnell@gmail.com> 0.75-1
- update to 0.75

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Iain Arnell <iarnell@gmail.com> 0.74-1
- update to 0.74

* Tue Nov 18 2008 Iain Arnell <iarnell@gmail.com> 0.73-1
- Specfile autogenerated by cpanspec 1.77.
