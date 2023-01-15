Name:           perl-HTTP-Easy
Version:        0.02
Release:        2%{?dist}
Summary:        HTTP helpers for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTTP-Easy
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONS/HTTP-Easy-%{version}.tar.gz

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
* Thu Aug  4 2022 Yanko Kaneti <yaneti@declera.com> - 0.02-2
- Address review issues (#2111647)

* Wed Jul 27 2022 Yanko Kaneti <yaneti@declera.com> - 0.02-1
- First attempt
