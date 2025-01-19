Name:           perl-Authen-U2F
Version:        0.003
Release:        8%{?dist}
Summary:        FIDO U2F library
# All but examples/demoserver/u2f-api.js is GPL-1.0-or-later OR Artistic-1.0-Perl
# examples/demoserver/u2f-api.js is BSD-3-Clause
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause
URL:            https://metacpan.org/dist/Authen-U2F
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBN/Authen-U2F-%{version}.tar.gz
# https://github.com/robn/Authen-U2F/issues/8
# https://developers.google.com/open-source/licenses/bsd
Source1:        bsd
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::OpenSSL::X509) >= 1.806
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(CryptX) >= 0.034
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON)
BuildRequires:  perl(Math::Random::Secure)
BuildRequires:  perl(MIME::Base64) >= 3.11
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Params)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(warnings)


%description
This module provides the tools you need to add support for U2F in your
application.


%prep
%setup -q -n Authen-U2F-%{version}
install -p -m 0644 %{SOURCE1} .

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*


%check
%make_build test


%files
%doc Changes README
%license LICENSE bsd
%{perl_vendorlib}/Authen/
%{_mandir}/man3/Authen::U2F.3pm*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Xavier Bachelot <xavier@bachelot.org> 0.003-4
- Add constraint to ExtUtils::MakeMaker
- Trim ugly HTML license file

* Wed Oct 04 2023 Xavier Bachelot <xavier@bachelot.org> 0.003-3
- Clean up specfile

* Wed Feb 23 2022 Xavier Bachelot <xavier@bachelot.org> 0.003-2
- Fix URL: and Source0:

* Wed Nov 28 2018 Xavier Bachelot <xavier@bachelot.org> 0.003-1
- Initial package
