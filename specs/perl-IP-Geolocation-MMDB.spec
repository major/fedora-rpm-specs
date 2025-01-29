Name:           perl-IP-Geolocation-MMDB
Version:        1.011
Release:        1%{?dist}
Summary:        Read MaxMind DB files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IP-Geolocation-MMDB
Source:         https://cpan.metacpan.org/authors/id/V/VO/VOEGELAS/IP-Geolocation-MMDB-%{version}.tar.gz
# Build:
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(Alien::libmaxminddb)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime:
BuildRequires:  perl(Math::BigInt) >= 1.999806
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
Suggests:       geolite2-asn
Suggests:       geolite2-city
Suggests:       geolite2-country

%{?perl_default_filter}

%description
A Perl module that reads MaxMind DB files and maps IP addresses to location
information such as country and city names.

%prep
%autosetup -n IP-Geolocation-MMDB-%{version}

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
%dir %{perl_vendorarch}/auto/IP
%dir %{perl_vendorarch}/auto/IP/Geolocation
%dir %{perl_vendorarch}/auto/IP/Geolocation/MMDB
%{perl_vendorarch}/auto/IP/Geolocation/MMDB/MMDB.so
%dir %{perl_vendorarch}/IP
%dir %{perl_vendorarch}/IP/Geolocation
%{perl_vendorarch}/IP/Geolocation/MMDB.pm
%dir %{perl_vendorarch}/IP/Geolocation/MMDB
%{perl_vendorarch}/IP/Geolocation/MMDB/Metadata.pm
%{_mandir}/man3/IP::Geolocation::MMDB.3*
%{_mandir}/man3/IP::Geolocation::MMDB::Metadata.3*

%changelog
* Sun Jan 26 2025 Andreas Vögele <andreas@andreasvoegele.com> - 1.011-1
- Update to 1.011

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.010-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-6
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.010-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-2
- Perl 5.38 rebuild

* Fri Jun 30 2023 Andreas Vögele <andreas@andreasvoegele.com> - 1.010-1
- Initial package
