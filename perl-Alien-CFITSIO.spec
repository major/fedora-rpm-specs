Name:           perl-Alien-CFITSIO
Version:        4.3.0.0
Release:        3%{?dist}
Summary:        Build and Install the CFITSIO library
License:        GPL-3.0-only
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Alien-CFITSIO/
Source0:        http://www.cpan.org/authors/id/D/DJ/DJERIUS/Alien-CFITSIO-v%{version}.tar.gz

%global debug_package %{nil}

BuildRequires:  cfitsio-devel >= 4.1.0
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Alien::Base)
BuildRequires:  perl(Alien::Build) >= 0.32
BuildRequires:  perl(Alien::Build::MM) >= 0.32
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien) >= 2.39
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Alien::Base)
Requires:       perl(base)
Requires:       perl(constant)
Requires:       perl(strict)
Requires:       perl(warnings)
# This RPM package ensures cfitsio is installed on the system
Requires:       pkgconfig(cfitsio) = %(type -p pkgconf >/dev/null && pkgconf --exists cfitsio && pkg-config --modversion cfitsio || echo 0)

%description
This module finds or builds the CFITSIO library. It supports at least
version CFITSIO 4.1.0.

%prep
%setup -q -n Alien-CFITSIO-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc alienfile Changes CONTRIBUTING.md dist.ini META.json perlcritic.rc perltidy.rc README tidyall.ini weaver.ini
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Orion Poplawski <orion@nwra.com> - 4.3.0.0-2
- Rebuild for cfitsio 4.3.1

* Sat Sep 02 2023 Orion Poplawski <orion@nwra.com> - 4.3.0.0-1
- Update to 4.3.0.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 4.1.0.5-2
- Rebuild for cfitsio 4.2

* Tue Aug 23 2022 Orion Poplawski <orion@nwra.com> 4.1.0.5-1
- Initial package
