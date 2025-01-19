Name:           perl-Alien-libmaxminddb
Version:        1.015
Release:        3%{?dist}
Summary:        Find or download and install libmaxminddb
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-libmaxminddb
Source:         https://cpan.metacpan.org/authors/id/V/VO/VOEGELAS/Alien-libmaxminddb-%{version}.tar.gz
# Build:
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(Alien::Build)
BuildRequires:  perl(Alien::Build::MM)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime:
BuildRequires:  perl(parent)
BuildRequires:  perl(utf8)
BuildRequires:  pkgconfig(libmaxminddb)
# Tests:
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test::More)
Requires:       pkgconfig(libmaxminddb)
Suggests:       perl(IP::Geolocation::MMDB)

%global debug_package %{nil}

%{?perl_default_filter}

%description
MaxMind and DP-IP.com provide geolocation databases in the MaxMind DB file
format.  This Perl module finds or downloads and installs the C library
libmaxminddb, which can read MaxMind DB files.

%prep
%autosetup -n Alien-libmaxminddb-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%dir %{perl_vendorarch}/Alien
%{perl_vendorarch}/Alien/libmaxminddb.pm
%dir %{perl_vendorarch}/Alien/libmaxminddb
%dir %{perl_vendorarch}/Alien/libmaxminddb/Install
%{perl_vendorarch}/Alien/libmaxminddb/Install/Files.pm
%dir %{perl_vendorarch}/auto/Alien
%dir %{perl_vendorarch}/auto/Alien/libmaxminddb
%{perl_vendorarch}/auto/Alien/libmaxminddb/libmaxminddb.txt
%dir %{perl_vendorarch}/auto/share
%dir %{perl_vendorarch}/auto/share/dist
%dir %{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb
%dir %{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb/_alien
%{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb/_alien/alien.json
%{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb/_alien/alienfile
%{_mandir}/man3/Alien::libmaxminddb.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Andreas Vögele <andreas@andreasvoegele.com> - 1.015-1
- Update to 1.015

* Sat Jan 27 2024 Andreas Vögele <andreas@andreasvoegele.com> - 1.014-1
- Update to 1.014

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 23 2023 Andreas Vögele <andreas@andreasvoegele.com> - 1.013-1
- Update to 1.013

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Andreas Vögele <andreas@andreasvoegele.com> - 1.012-2
- List files explicitly

* Mon May 22 2023 Andreas Vögele <andreas@andreasvoegele.com> - 1.012-1
- Initial package
