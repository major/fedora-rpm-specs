Name:           perl-Alien-LibGumbo
Version:        0.05
Release:        12%{?dist}
Summary:        Gumbo parser library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-LibGumbo
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RUZ/Alien-LibGumbo-%{version}.tar.gz

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 0:5.010

BuildRequires:  perl(Alien::Base) >= 0.005
BuildRequires:  perl(Alien::Base::ModuleBuild)
BuildRequires:  perl(File::ShareDir) >= 1.03
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Path::Class) >= 0.013

BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  gumbo-parser-devel


# Pull in %%{_libdir}/libgumbo.so.?
Requires:       gumbo-parser%{?_isa}

# This is an architecture-dependent package because it stores data about
# architecture-specific library, but it has no XS code, hence no debuginfo.
%global debug_package %%{nil}


%description
This distribution installs libgumbo:https://github.com/google/gumbo-parser
on your system for use by perl modules like HTML::Gumbo.

%prep
%setup -q -n Alien-LibGumbo-%{version}
# Remove bundled gumbo tarball
rm -f gumbo-0.10.1.tar.gz
sed -i -e '/gumbo-0.10.1.tar.*/d' MANIFEST

%build
%{__perl} Build.PL --installdirs=vendor --install_path lib=%{perl_vendorarch}
./Build

%install

./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test

%files
%doc Changes
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-10
- Rebuild against gumbo-parser-0.12.1.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-5
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-3
- Perl 5.36 rebuild

* Mon Jan 10 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-2
- Various changes.

* Fri Oct 22 2021 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-1
- Initial Fedora package.
