Name:           perl-X-Tiny
Version:        0.22
Release:        5%{?dist}
Summary:        Base class for a bare-bones exception factory
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/X-Tiny
Source0:        https://www.cpan.org/authors/id/F/FE/FELIPE/X-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(overload)

# lib/X/Tiny/Base.pm has an override for debugger
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)$

%description
This stripped-down exception framework provides a baseline of functionality
for distributions that want to expose exception hierarchies with minimal
fuss. It's a pattern that I implemented in some other distributions I
created and didn't want to copy/paste around.

%prep
%setup -q -n X-Tiny-%{version}
# https://github.com/FGasper/p5-X-Tiny/pull/3
perl -pi -e '$_="" if(/Test::Simple/)' Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md
%license LICENSE
%dir %{perl_vendorlib}/X
%{perl_vendorlib}/X/Tiny*
%{_mandir}/man3/X::Tiny*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Apr 04 2025 Chris Adams <linux@cmadams.net> 0.22-4
- add missing Requires on perl(overload) (done with eval so missed by autodep)

* Thu Apr 03 2025 Chris Adams <linux@cmadams.net> 0.22-3
- update BuildRequires, filter with perl

* Wed Apr 02 2025 Chris Adams <linux@cmadams.net> 0.22-2
- filter 'perl(DB)' from provides (just an internal debugger override)
- tests don't actually use Test::Simple

* Tue Feb 18 2025 Chris Adams <linux@cmadams.net> 0.22-1
- initial package
