Name:           perl-Authen-WebAuthn
Version:        0.001
Release:        5%{?dist}
Summary:        Library to add Web Authentication support to server applications
License:        GPL+ or Artistic
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
BuildRequires:  perl(Crypt::OpenSSL::X509)
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(Crypt::PK::RSA)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker) %{!?el7:>= 6.76}
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Mouse)
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
%{__perl} Makefile.PL INSTALLDIRS=vendor %{!?el7:NO_PACKLIST=1}
%make_build


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%if 0%{?el7}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%endif

%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license LICENSE
%doc README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
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
