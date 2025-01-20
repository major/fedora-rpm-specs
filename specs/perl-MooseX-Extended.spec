Name:           perl-MooseX-Extended
Version:        0.35
Release:        5%{?dist}
Summary:        Extend Moose with safe defaults and useful features
License:        Artistic-2.0
URL:            https://metacpan.org/dist/MooseX-Extended/
Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/MooseX-Extended-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

BuildRequires:  perl(:VERSION) >= 5.20.0

BuildRequires:  perl(base)
BuildRequires:  perl(B::Hooks::AtRuntime) >= 8
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Data::Printer)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Future::AsyncAwait) >= 0.58
BuildRequires:  perl(Function::Parameters)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exception)
BuildRequires:  perl(Moose::Exception::Role::Class)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Role::WarnOnConflict)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(mro)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Syntax::Keyword::MultiSub) >= 0.02
BuildRequires:  perl(Syntax::Keyword::Try) >= 0.027
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Compile) >= 3.1.0
BuildRequires:  perl(Test::Compile::Internal)
BuildRequires:  perl(true) >= 1.0.2
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Params)
BuildRequires:  perl(Types::Common::Numeric)
BuildRequires:  perl(Types::Common::String)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Type::Tiny) >= 1.012004
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(warnings)

%description
This class attempts to create a safer version of Moose that defaults to
read-only attributes and is easier to read and write.

%prep
%setup -q -n MooseX-Extended-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} "$RPM_BUILD_ROOT"/*

%check
%{__make} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jun 26 2023 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.35-1
- Update to 0.35.

* Wed Nov 09 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.34-1
- Update to 0.34.

* Sun Aug 21 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.28-1
- Update to 0.28.

* Thu Jun 16 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.25-1
- Update to 0.25.
- Misc. spec file massaging.

* Thu Jun 16 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.24-1
- Initial Fedora package.
