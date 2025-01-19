Name:           perl-Authen-WebAuthn
Version:        0.005
Release:        2%{?dist}
Summary:        Library to add Web Authentication support to server applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Authen-WebAuthn
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBESSON/Authen-WebAuthn-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(CBOR::XS)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::OpenSSL::X509) >= 1.808
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(Crypt::PK::RSA)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Net::SSLeay) >= 1.88
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)


%description
This module lets you validate WebAuthn registration and authentication
responses.

Currently, it does not handle the generation of registration and
authentication requests.
The transmission of requests and responses from the application server to the
user's browser, and interaction with the WebAuthn browser API is also out of
scope and could be handled by a dedicated JS library.


%prep
%setup -q -n Authen-WebAuthn-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%license LICENSE
%doc README README.md
%{perl_vendorlib}/Authen
%{_mandir}/man3/Authen::WebAuthn.3*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 12 2024 Xavier Bachelot <xavier@bachelot.org> - 0.005-1
- Update to 0.005 (RHBZ#2332110)

* Mon Jul 29 2024 Xavier Bachelot <xavier@bachelot.org> - 0.004-1
- Update to 0.004 (RHBZ#2300031)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 04 2024 Xavier Bachelot <xavier@bachelot.org> - 0.003-1
- Update to 0.003 (RHBZ#2290374)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 22 2023 Xavier Bachelot <xavier@bachelot.org> - 0.002-1
- Update to 0.002
- Convert License to SPDX
- Cleanup specfile

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-3
- Perl 5.36 rebuild

* Sat Apr 30 2022 Xavier Bachelot <xavier@bachelot.org> 0.001-2
- Review fixes

* Mon Feb 14 2022 Xavier Bachelot <xavier@bachelot.org> 0.001-1
- Initial package
