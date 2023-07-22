Name:		perl-Crypt-Curve25519
Version:	0.07
Release:	4%{?dist}
Summary:	Generate shared secret using elliptic-curve Diffie-Hellman function
License:	(GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause
URL:		https://metacpan.org/release/Crypt-Curve25519
Source0:	https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-Curve25519-%{version}.tar.gz
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(Test::More) >= 0.88
# Runtime

%description
Curve25519 is a Diffie-Hellman function suitable for a wide variety of
applications.

Given a user's 32-byte secret key, Curve25519 computes the user's 32-byte
public key. Given the user's 32-byte secret key and another user's 32-byte
public key, Curve25519 computes a 32-byte secret shared by the two users. This
secret can then be used to authenticate and encrypt messages between the two
users.

%prep
%setup -q -n Crypt-Curve25519-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license curve25519-donna-license.md
%doc Changes README.md
%{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/Crypt::Curve25519.3*

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-3
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Paul Howarth <paul@city-fan.org> - 0.07-1
- Update to 0.07
  - Fix compilation issues with fmul name clash
- Use SPDX-format license tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-2
- Perl 5.36 rebuild

* Fri Mar  4 2022 Paul Howarth <paul@city-fan.org> - 0.06-1
- Initial RPM version
