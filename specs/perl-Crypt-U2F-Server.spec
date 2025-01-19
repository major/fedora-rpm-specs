Name:           perl-Crypt-U2F-Server
Version:        0.47
Release:        2%{?dist}
Summary:        Low level wrapper around the U2F C library (server side)
License:        BSD-2-Clause AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/dist/Crypt-U2F-Server
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUIMARD/Crypt-U2F-Server-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libu2f-server-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.18.1
BuildRequires:  perl(Authen::U2F::Tester) >= 0.02
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)


%description
This is a very low level wrapper around the original C library. You
probably shouldn't use it, but use Crypt::U2F::Server::Simple instead!


%prep
%setup -q -n Crypt-U2F-Server-%{version}


%build
perl Makefile.PL \
  INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
%make_build test


%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/Crypt::U2F::Server*3pm*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Xavier Bachelot <xavier@bachelot.org> - 0.47-1
- Update to 0.47 (RHBZ#2261447, RHBZ#2280641, RHBZ#2292219, RHBZ#2302694)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-5
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 04 2023 Xavier Bachelot <xavier@bachelot.org> 0.45-2
- Clean up specfile

* Thu Feb 24 2022 Xavier Bachelot <xavier@bachelot.org> 0.45-1
- Update to 0.45

* Wed Nov 28 2018 Xavier Bachelot <xavier@bachelot.org> 0.43-1
- Initial package
