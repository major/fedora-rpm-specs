# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/K/KU/KURIHARA
%define FullName Text-QRCode

Name: perl-%{FullName}
Summary: Perl module to generate text base QR Code
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 0.05
Release: 11%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::Copy)
BuildRequires: perl(Module::Install::AutoInstall)
BuildRequires: perl(Module::Install::Can)
BuildRequires: perl(Module::Install::Compiler)
BuildRequires: perl(Module::Install::Metadata)
BuildRequires: perl(Module::Install::WriteAll)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(base)
BuildRequires: perl(inc::Module::Install)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: pkgconf-pkg-config
BuildRequires: pkgconfig(libqrencode)
BuildRequires: qrencode-devel >= 2.0.0

Requires: perl(XSLoader)

%description
This module allows you to generate QR Code using ' ' and '*'.

%prep
%setup -q -n %{FullName}-%{version}
rm -fr inc

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test VERBOSE=1

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%dir %{perl_vendorarch}/auto/Text
%dir %{perl_vendorarch}/auto/Text/QRCode
%{perl_vendorarch}/auto/Text/QRCode/QRCode.so
%dir %{perl_vendorarch}/Text
%{perl_vendorarch}/Text/QRCode.pm
%{_mandir}/man3/Text::QRCode.3pm.gz

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-9
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-5
- Perl 5.38 rebuild

* Wed Feb 08 2023 Johan Vromans <jvromans@squirrel.nl> - 0.05-4
- Incorporate reviewer feedback.

* Tue Feb 07 2023 Johan Vromans <jvromans@squirrel.nl> - 0.05-3
- Incorporate reviewer feedback.

* Fri Feb 03 2023 Johan Vromans <jvromans@squirrel.nl> - 0.05-2
- Incorporate reviewer feedback.

* Mon Dec 19 2022 Johan Vromans <jvromans@squirrel.nl> - 0.05-1
- Initial Fedora package.
