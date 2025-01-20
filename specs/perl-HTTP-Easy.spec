Name:           perl-HTTP-Easy
Version:        0.04
Release:        6%{?dist}
Summary:        HTTP helpers for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/Mons/HTTP-Easy
Source0:        https://github.com/Mons/HTTP-Easy/archive/refs/tags/%{version}/HTTP-Easy-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(:VERSION) >= 5.8.8
# tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib::abs)
BuildRequires:  perl(URI)


%description
Set of useful helpers for HTTP work with Perl.

%prep
%setup -q -n HTTP-Easy-%{version}

%build
unset AUTHOR
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Yanko Kaneti <yaneti@declera.com> - 0.04-1
- Update to 0.04 from Mons' github and change upstream url

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug  4 2022 Yanko Kaneti <yaneti@declera.com> - 0.02-2
- Address review issues (#2111647)

* Wed Jul 27 2022 Yanko Kaneti <yaneti@declera.com> - 0.02-1
- First attempt
