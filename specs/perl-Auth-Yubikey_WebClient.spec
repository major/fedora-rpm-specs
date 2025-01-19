Name:           perl-Auth-Yubikey_WebClient
Version:        4.02
Release:        2%{?dist}
Summary:        Authenticating the Yubikey against the Yubico Web API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://metacpan.org/dist/Auth-Yubikey_WebClient/
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASSYN/Auth-Yubikey_WebClient-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Digest::HMAC_SHA1) >= 1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(LWP::UserAgent) >= 1
BuildRequires:  perl(MIME::Base64) >= 1
BuildRequires:  perl(URI::Escape) >= 1
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Test::Pod) >=  1.22


%description
Authenticate against the Yubico server via the Web API in Perl.


%prep
# 4.0.2 tarball is malformed
#setup -q -n Auth-Yubikey_WebClient-%%{version}
%setup -q -n Auth-Yubikey_WebClient-master


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%{perl_vendorlib}/Auth
%{_mandir}/man3/Auth::Yubikey_WebClient.3pm*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 09 2024 Xavier Bachelot <xavier@bachelot.org> 4.02-1
- Update to 4.02

* Wed Nov 22 2023 Xavier Bachelot <xavier@bachelot.org> 4.01-1
- Initial package
