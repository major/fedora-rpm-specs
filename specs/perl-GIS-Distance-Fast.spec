Name:           perl-GIS-Distance-Fast
Version:        0.16
Release:        8%{?dist}
Summary:        C implementation of GIS::Distance formulas
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GIS-Distance-Fast
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/GIS-Distance-Fast-%{version}.tar.gz
# Link to libm and fix linking by using EU::MM instead of buggy M::B::Tiny,
# <https://github.com/bluefeet/GIS-Distance-Fast/issues/1>
Patch0:         GIS-Distance-Fast-0.12-Build-using-ExtUtils-MakeMaker-and-link-to-math-libr.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.12
# Run-time:
BuildRequires:  perl(GIS::Distance::Formula) >= 0.17
BuildRequires:  perl(namespace::clean) >= 0.24
BuildRequires:  perl(parent)
BuildRequires:  perl(strictures) >= 2
# XSLoader || DynaLoader
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(GIS::Distance) >= 0.17
BuildRequires:  perl(Test2::V0) >= 0.000094
Requires:       perl(GIS::Distance::Formula) >= 0.17
Requires:       perl(namespace::clean) >= 0.24
# XSLoader || DynaLoader
Requires:       perl(XSLoader)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((GIS::Distance|GIS::Distance::Formula|namespace::clean|Test2::V0)\\)$

%description
This Perl module reimplements some, but not all, of the formulas that
come with GIS::Distance in the C programming language. C code is generally
much faster than the Perl equivalent.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(GIS::Distance) >= 0.17
Requires:       perl(Test2::V0) >= 0.000094

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n GIS-Distance-Fast-%{version}
# Normalize shenangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
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
%doc Changes README.md
%dir %{perl_vendorarch}/auto/GIS
%dir %{perl_vendorarch}/auto/GIS/Distance
%{perl_vendorarch}/auto/GIS/Distance/Fast
%dir %{perl_vendorarch}/GIS
%dir %{perl_vendorarch}/GIS/Distance
%{perl_vendorarch}/GIS/Distance/Fast
%{perl_vendorarch}/GIS/Distance/Fast.pm
%{_mandir}/man3/GIS::Distance::Fast.*
%{_mandir}/man3/GIS::Distance::Fast::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-6
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-2
- Perl 5.38 rebuild

* Thu Jun 08 2023 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Petr Pisar <ppisar@redhat.com> - 0.15-4
- Package the tests

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Perl 5.34 rebuild

* Mon Feb 01 2021 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-2
- Perl 5.30 rebuild

* Mon Mar 18 2019 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Thu Mar 14 2019 Petr Pisar <ppisar@redhat.com> - 0.12-1
- 0.12 bump

* Fri Mar 08 2019 Petr Pisar <ppisar@redhat.com> 0.10-1
- Specfile autogenerated by cpanspec 1.78.
