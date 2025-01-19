Name:           perl-Authen-U2F-Tester
Version:        0.03
Release:        8%{?dist}
Summary:        FIDO/U2F Authentication Test Client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Authen-U2F-Tester
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/Authen-U2F-Tester-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.006
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Authen::U2F)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::Misc)
BuildRequires:  perl(Crypt::OpenSSL::X509)
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::AttributeShortcuts)
BuildRequires:  perl(MooseX::SingleArg)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(strictures) >= 2
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Carp)


%description
This module implements a FIDO/U2F tester that can be used for testing web
applications that support FIDO/U2F. Think of this module as a "virtual" U2F
security key.


%prep
%setup -q -n Authen-U2F-Tester-%{version}


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
%license LICENSE
%{perl_vendorlib}/Authen/
%{_mandir}/man3/Authen::U2F::Tester*3pm*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 25 2023 Xavier Bachelot <xavier@bachelot.org> 0.03-4
- Review fixes

* Wed Oct 04 2023 Xavier Bachelot <xavier@bachelot.org> 0.03-3
- Clean up specfile

* Thu Feb 24 2022 Xavier Bachelot <xavier@bachelot.org> 0.03-2
- Fix URL: and Source0:

* Wed Nov 28 2018 Xavier Bachelot <xavier@bachelot.org> 0.03-1
- Initial package
