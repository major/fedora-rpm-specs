Name:           perl-MouseX-Types-Common
Version:        0.001000
Release:        3%{?dist}
Summary:        Set of commonly-used type constraints
License:        GPL+ or Artistic
URL:            http://metacpan.org/dist/MouseX-Types-Common/
Source0:        http://cpan.metacpan.org/authors/id/G/GF/GFUJI/MouseX-Types-Common-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__chmod}
BuildRequires:  %{__make}
BuildRequires:  %{__sed}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators

BuildRequires:  perl(:VERSION) >= 5.6.2
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Mouse) >= 0.42
BuildRequires:  perl(MouseX::Types) >= 0.01
BuildRequires:  perl(MouseX::Types::Mouse)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(Test::Exception)

BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A set of commonly-used type constraints that do not ship with Mouse
by default.

%prep
%setup -q -n MouseX-Types-Common-%{version}
# Remove bundled modules
rm -r inc
%{__sed} -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.001000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.001000-2
- Post-review fixes.

* Thu Jun 16 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.001000-1
- Initial Fedora package.
