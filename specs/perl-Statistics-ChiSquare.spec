# Note: code is GPL-2.0-only OR Artistic-1.0-Perl, embedded data table is CC-BY-SA-3.0

Name:		perl-Statistics-ChiSquare
Version:	1.0000
Release:	12%{?dist}
Summary:	How well-distributed is your data?
License:	(GPL-2.0-only OR Artistic-1.0-Perl) AND CC-BY-SA-3.0
URL:		https://metacpan.org/release/Statistics-ChiSquare
Source0:	https://cpan.metacpan.org/modules/by-module/Statistics/Statistics-ChiSquare-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(warnings)
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Dependencies
# (none)

%description
Suppose you flip a coin 100 times, and it turns up heads 70 times. Is the coin
fair? Suppose you roll a die 100 times, and it shows 30 sixes. Is the die
loaded?

In statistics, the chi-square test calculates how well a series of numbers fits
a distribution. In this module, we only test for whether results fit an even
distribution. It doesn't simply say "yes" or "no". Instead, it gives you a
confidence interval, which sets upper and lower bounds on the likelihood that
the variation in your data is due to chance.

%prep
%setup -q -n Statistics-ChiSquare-%{version}

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
%license ARTISTIC.txt GPL2.txt
%doc CHANGELOG README
%{perl_vendorlib}/Statistics/
%{_mandir}/man3/Statistics::ChiSquare.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.0000-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Paul Howarth <paul@city-fan.org> - 1.0000-2
- Fix license tag to account for CC-BY-SA data table (#1967876)

* Fri Jun  4 2021 Paul Howarth <paul@city-fan.org> - 1.0000-1
- Initial RPM version
