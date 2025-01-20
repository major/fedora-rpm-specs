Name:           perl-Role-Hooks
Version:        0.008
Release:        8%{?dist}
Summary:        Role callbacks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Role-Hooks/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Role-Hooks-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1

BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)

BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Testsuite requirements
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)

# Optional testsuite requirements
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Package::Variant)
BuildRequires:  perl(Role::Basic)


# Not sure, if this dep should be mandatory
Recommends:	perl(Carp)

%description
This module allows a role to run a callback when it is applied to a class
or to another role.

%prep
%setup -q -n Role-Hooks-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} "$RPM_BUILD_ROOT"/*

%check
%{__make} test

%files
%license LICENSE COPYRIGHT
%doc Changes CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 21 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.008-2
- Reflect feedback from review.

* Sun Jul 10 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.008-1
- Update to 0.008.
- Drop BR: perl(Role::Tiny).

* Sun Jul 10 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.007-1
- Update to 0.007.

* Sun Jul 03 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.006-1
- Initial Fedora package.
