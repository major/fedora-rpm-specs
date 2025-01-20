Name:           perl-HTTP-Tiny-Paranoid
Version:        0.07
Release:        6%{?dist}
Summary:        Safer HTTP::Tiny
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTTP-Tiny-Paranoid
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBN/HTTP-Tiny-Paranoid-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make perl-interpreter perl-generators coreutils
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTTP::Tiny) >= 0.070
BuildRequires:  perl(Net::DNS::Paranoid)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
This module is a subclass of HTTP::Tiny that performs exactly one
additional function: before connecting, it passes the hostname to
Net::DNS::Paranoid. If the hostname is rejected, then the request is
aborted before a connect is even attempted.

%prep
%setup -q -n HTTP-Tiny-Paranoid-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
# no tests so do a manual load check
#make test
perl -I./lib -MHTTP::Tiny::Paranoid -e '1;'

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/HTTP
%{_mandir}/man3/HTTP::Tiny::*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.07-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.07-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.07-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.07-1
- initial package
