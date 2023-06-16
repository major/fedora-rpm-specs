Name:           perl-Alien-libmaxminddb
Version:        1.012
Release:        1%{?dist}
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
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*

%changelog
* Mon May 22 2023 Andreas Vögele <andreas@andreasvoegele.com> - 1.012-1
- Initial package
