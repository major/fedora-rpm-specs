Name:           perl-MooseX-Role-WarnOnConflict
Version:        0.01
Release:        10%{?dist}
Summary:        Warn if classes override role methods without excluding them
License:        Artistic-2.0
URL:            http://cpan.metacpan.org/dist/MooseX-Role-WarnOnConflict/
Source0:        http://cpan.metacpan.org/authors/id/O/OV/OVID/MooseX-Role-WarnOnConflict-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__chmod}
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators

BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Meta::Role::Application::ToClass)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(warnings)


%description
When using Moose::Role, a class which provides a method a role provides
will silently override that method. This can cause strange, hard-to-debug
errors when the role's methods are not called. Simply use
MooseX::Role::WarnOnConflict instead of Moose::Role and overriding a role's
method becomes a composition-time warning. See the synopsis for a
resolution.

%prep
%setup -q -n MooseX-Role-WarnOnConflict-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.01-4
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.01-2
- Post-review fixes.

* Wed Jun 15 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.01-1
- Initial Fedora package.
