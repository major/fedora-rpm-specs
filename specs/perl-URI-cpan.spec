Name:		perl-URI-cpan
Version:	1.009
Release:	5%{?dist}
Summary:	URLs that refer to things on the CPAN
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/URI-cpan
Source0:	https://cpan.metacpan.org/modules/by-module/URI/URI-cpan-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.78
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(CPAN::DistnameInfo)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(URI::_generic)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(URI)
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Dependencies
# (none)

%description
This module is for handling URLs that refer to things on the CPAN.

%prep
%setup -q -n URI-cpan-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/URI/
%{_mandir}/man3/URI::cpan.3*
%{_mandir}/man3/URI::cpan::author.3*
%{_mandir}/man3/URI::cpan::dist.3*
%{_mandir}/man3/URI::cpan::distfile.3*
%{_mandir}/man3/URI::cpan::module.3*
%{_mandir}/man3/URI::cpan::package.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep  3 2023 Paul Howarth <paul@city-fan.org> - 1.009-1
- Update to 1.009
  - Updates to dist metadata only

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-2
- Perl 5.36 rebuild

* Tue Dec 21 2021 Paul Howarth <paul@city-fan.org> - 1.008-1
- Update to 1.008
  - Fix prereqs to rely on URI, not the unindexed URI::_generic

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.007-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.007-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.007-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Paul Howarth <paul@city-fan.org> - 1.007-4
- Modernize spec using %%{make_install}

* Tue Sep 15 2020 Paul Howarth <paul@city-fan.org> - 1.007-3
- perl(URI) is a test requirement, not a module requirement (#1876259)

* Sun Sep  6 2020 Paul Howarth <paul@city-fan.org> - 1.007-2
- Sanitize for Fedora

* Sun Sep  6 2020 Paul Howarth <paul@city-fan.org> - 1.007-1
- Initial RPM version
