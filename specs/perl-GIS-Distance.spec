%if !%{defined perl_bootstrap}
# Run optional tests.
# Disabled because perl-Geo-Point was retired (bug #1748923).
# Build-cycle: perl-GIS-Distance → perl-Geo-Point → perl-Geo-Distance
%bcond_with perl_GIS_Distance_enables_optional_test
# Use optimized implementation in C
# Build-cycle: perl-GIS-Distance-XS → perl-GIS-Distance
%bcond_without perl_GIS_Distance_enables_xs
%endif

Name:           perl-GIS-Distance
Version:        0.20
Release:        6%{?dist}
Summary:        Calculate geographic distances
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GIS-Distance
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/GIS-Distance-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Measure::Length)
BuildRequires:  perl(Const::Fast) >= 0.014
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(namespace::clean) >= 0.24
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strictures) >= 2
%if %{with perl_GIS_Distance_enables_xs}
# Optional run-time:
BuildRequires:  perl(GIS::Distance::Fast) >= 0.13
%endif
# Tests:
BuildRequires:  perl(Test2::V0) >= 0.000094
%if %{with perl_GIS_Distance_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Geo::Point) >= 0.95
BuildRequires:  perl(Test2::Require::Module)
%endif
Requires:       perl(Const::Fast) >= 0.014
%if %{with perl_GIS_Distance_enables_xs}
Recommends:     perl(GIS::Distance::Fast) >= 0.13
%endif
Requires:       perl(namespace::clean) >= 0.24

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Const::Fast|Geo::Point|namespace::clean|Test2::V0)\\)$

%description
This Perl module calculates distances between geographic points on, at the
moment, planet Earth. Various "FORMULAS" are available that provide different
levels of accuracy versus speed.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test2::V0) >= 0.000094
%if %{with perl_GIS_Distance_enables_optional_test}
Requires:       perl(Geo::Point) >= 0.95
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n GIS-Distance-%{version}
%if !%{with perl_GIS_Distance_enables_optional_test}
rm t/geo_point.t
perl -i -ne 'print $_ unless m{^t/geo_point\.t}' MANIFEST
%endif
# Normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset GEO_DISTANCE_PP GIS_DISTANCE_PP
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset GEO_DISTANCE_PP GIS_DISTANCE_PP
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README.md
%dir %{perl_vendorlib}/GIS
%{perl_vendorlib}/GIS/Distance
%{perl_vendorlib}/GIS/Distance.pm
%{_mandir}/man3/GIS::Distance.*
%{_mandir}/man3/GIS::Distance::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 08 2023 Petr Pisar <ppisar@redhat.com> - 0.20-1
- 0.20 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-8
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-7
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Petr Pisar <ppisar@redhat.com> - 0.19-5
- Package the tests

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.34 rebuild

* Mon Feb 01 2021 Petr Pisar <ppisar@redhat.com> - 0.19-1
- 1.19 bump
- A license changed from "GPLv3+" to "GPL+ or Artistic"

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-8
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Petr Pisar <ppisar@redhat.com> - 0.18-5
- Disable optional tests because perl-Geo-Point will be retired (bug #1748923)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-2
- Perl 5.30 rebuild

* Mon May 13 2019 Petr Pisar <ppisar@redhat.com> - 0.18-1
- 0.18 bump
- License changed from "GPL+ or Artistic" to "GPLv3+"

* Mon Mar 18 2019 Petr Pisar <ppisar@redhat.com> - 0.17-2
- Finish bootstrapping perl-GIS-Distance-Fast-0.14

* Mon Mar 18 2019 Petr Pisar <ppisar@redhat.com> - 0.17-1
- 0.17 bump

* Wed Mar 13 2019 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Mon Mar 11 2019 Petr Pisar <ppisar@redhat.com> - 0.11-2
- Finish boostrapping with perl-GIS-Distance-XS

* Fri Mar 08 2019 Petr Pisar <ppisar@redhat.com> 0.11-1
- Specfile autogenerated by cpanspec 1.78.
