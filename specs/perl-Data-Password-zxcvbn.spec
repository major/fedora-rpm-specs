Name:           perl-Data-Password-zxcvbn
Version:        1.1.2
Release:        5%{?dist}
Summary:        Dropbox's password estimation logic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Data-Password-zxcvbn
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAKKAR/Data-Password-zxcvbn-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::AllUtils) >= 0.14
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moose)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(warnings)


%description
This is a Perl port of Dropbox's password strength estimation
library, zxcvbn.


%prep
%setup -q -n Data-Password-zxcvbn-%{version}


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
%doc Changes README.md scripts
%{_bindir}/zxcvbn-password-strength
%{_mandir}/man1/zxcvbn-password-strength.1*
%{_mandir}/man3/Data::Password::zxcvbn*3pm*
%{perl_vendorlib}/Data/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 13 2023 Xavier Bachelot <xavier@bachelot.org> 1.1.2-1
- Initial specfile
