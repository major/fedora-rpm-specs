Name:           perl-Alien-libmaxminddb
Version:        2.001
Release:        2%{?dist}
Summary:        Find or download and install libmaxminddb
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-libmaxminddb
Source:         https://cpan.metacpan.org/authors/id/V/VO/VOEGELAS/Alien-libmaxminddb-%{version}.tar.gz
# Build:
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(utf8)
BuildRequires:  pkgconfig(libmaxminddb)
# Tests:
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl(Test::More)
Requires:       pkgconfig(libmaxminddb)

%global debug_package %{nil}

%{?perl_default_filter}

%description
MaxMind and DP-IP.com provide geolocation databases in the MaxMind DB file
format.  This Perl module finds or installs the C library libmaxminddb,
which can read MaxMind DB files.

%prep
%autosetup -n Alien-libmaxminddb-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor INSTALLVENDORLIB=%{perl_vendorarch} NO_PACKLIST=1 NO_PERLLOCAL=1
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
%dir %{perl_vendorarch}/auto/share
%dir %{perl_vendorarch}/auto/share/dist
%dir %{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb
%dir %{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb/_alien
%{perl_vendorarch}/auto/share/dist/Alien-libmaxminddb/_alien/alien.json
%{_mandir}/man3/Alien::libmaxminddb.3*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Mar 15 2025 Andreas Vögele <andreas@andreasvoegele.com> - 2.001-1
- Update to 2.001
- Alien::Build is no longer required

* Sun Mar 09 2025 Andreas Vögele <andreas@andreasvoegele.com> - 1.019-1
- Update to 1.019

* Fri Mar 07 2025 Andreas Vögele <andreas@andreasvoegele.com> - 1.018-1
- Update to 1.018

* Sun Jan 26 2025 Andreas Vögele <andreas@andreasvoegele.com> - 1.016-1
- Update to 1.016

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
