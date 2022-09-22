Name:           perl-Sub-HandlesVia
Version:        0.036
Release:        1%{?dist}

Summary:        Alternative handles_via implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Sub-HandlesVia
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Sub-HandlesVia-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0

BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Eval::TypeTiny)
BuildRequires:  perl(Exporter::Shiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util) >= 1.54
# N/A in Fedora: BuildRequires:  perl(MooseX::Extended)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Hooks) >= 0.008
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Type::Params) >= 1.004000
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Optional, for improved tests
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::ArrayRef)
BuildRequires:  perl(MooseX::InsideOut)
BuildRequires:  perl(MooX::TypeTiny)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Test::Moose)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
If you've used Moose's native attribute traits, or MooX::HandlesVia before,
you should have a fairly good idea what this does.

%prep
%setup -q -n Sub-HandlesVia-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%license LICENSE
%doc Changes CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Aug 26 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.036-1
- Update to 0.036.
- Spec cleanup.

* Mon Aug 22 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.035-1
- Update to 0.035.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.027-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.027-5
- Add BR: perl(Role::Hooks) for Sub-HandlesVia >= 0.32.

* Sun Jul 10 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.027-4
- Drop BR: perl(Scope::Guard) for Sub-HandlesVia >= 0.30.

* Sun Jul 10 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.027-3
- Drop BR: perl(Class::Tiny) for Sub-HandlesVia >= 0.29.

* Sun Jul 03 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.027-2
- Preps for 0.028.
- BR: perl(FindBin).
- BR: perl(:VERSION).

* Fri Jul 01 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.027-1
- Upstream update to 0.027.

* Thu Jun 16 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.025-1
- Upstream update to 0.025.

* Wed Jun 15 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.024-1
- Upstream update to 0.024.
- Add and comment out BR: perl(MooseX::Extended).

* Wed Jun 15 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.023-1
- Upstream update to 0.023.
- Add BR: perl(Scope::Guard).

* Tue Jun 14 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.022-1
- Upstream update to 0.022.

* Mon Jun 13 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.021-1
- Upstream update to 0.021.

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.016-2
- Perl 5.36 rebuild

* Fri Oct 22 2021 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.016-1
- Initial Fedora package.
