Name:           perl-Crypt-JWT
Version:        0.036
Release:        1%{?dist}
Summary:        JSON Web Token (JWT, JWS, JWE) as defined by RFC7519, RFC7515, RFC7516
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Crypt-JWT
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/Crypt-JWT-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-libs
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::AuthEnc::GCM)
BuildRequires:  perl(Crypt::Digest)
BuildRequires:  perl(Crypt::KeyDerivation)
BuildRequires:  perl(Crypt::Mac::HMAC)
BuildRequires:  perl(Crypt::Misc)
BuildRequires:  perl(Crypt::Mode::ECB)
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(Crypt::PK::Ed25519)
BuildRequires:  perl(Crypt::PK::RSA)
BuildRequires:  perl(Crypt::PK::X25519)
BuildRequires:  perl(Crypt::PRNG)
BuildRequires:  perl(CryptX) >= 0.067
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker) %{!?el7:>= 6.76}
BuildRequires:  perl(JSON)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)


%description
Implements JSON Web Token (JWT) - https://tools.ietf.org/html/rfc7519. The
implementation covers not only JSON Web Signature (JWS) -
https://tools.ietf.org/html/rfc7515, but also JSON Web Encryption (JWE) -
https://tools.ietf.org/html/rfc7516.


%prep
%setup -q -n Crypt-JWT-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*


%check
%make_build test


%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::*.3pm*


%changelog
* Tue Jan 28 2025 Xavier Bachelot <xavier@bachelot.org> 0.036-1
- Update to 0.036 (RHBZ#2342507)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Xavier Bachelot <xavier@bachelot.org> 0.035-2
- Tweak for EL7

* Tue Nov 21 2023 Xavier Bachelot <xavier@bachelot.org> 0.035-1
- Update to 0.035

* Wed Sep 13 2023 Xavier Bachelot <xavier@bachelot.org> 0.034-1
- Initial specfile
