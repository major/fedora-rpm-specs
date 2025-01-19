Name:           perl-HTML-Gumbo
Version:        0.18
Release:        17%{?dist}
Summary:        HTML5 parser based on gumbo C library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Gumbo
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RUZ/HTML-Gumbo-%{version}.tar.gz

BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  gcc
BuildRequires:  perl-generators

BuildRequires:  perl(Alien::LibGumbo) >= 0.03
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)

BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  gumbo-parser-devel


%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as a
pure C99 library with no outside dependencies.

%prep
%setup -q -n HTML-Gumbo-%{version}

%build
%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir="$RPM_BUILD_ROOT" --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} "$RPM_BUILD_ROOT"/*

%check
./Build test

%files
%doc Changes
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/HTML*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-15
- Perl 5.40 rebuild

* Sun Mar 03 2024 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-14
- Rebuild against gumbo-parser-0.12.1.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-10
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-8
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-6
- Perl 5.36 rebuild

* Fri Apr 01 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-5
- Add R:perl(Test::More) (RHBZ#2070851).

* Sun Feb 27 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-4
- Add changes missed in previous iteration.

* Tue Feb 08 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-3
- Further misc. changes.

* Tue Jan 11 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-2
- Misc. changes.

* Fri Oct 22 2021 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-1
- Initial Fedora package.
