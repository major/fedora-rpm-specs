Name:           perl-Object-Import
Version:        1.006
Release:        3%{?dist}
Summary:        Import methods of an object as functions to a package
License:        GPL-3.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Object-Import/
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/Object-Import-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make perl-interpreter perl-generators coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Math::BigInt) >= 1.59
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(warnings)

%description
This module lets you call methods of a certain object more easily by
exporting them as functions to a package. The exported functions are not
called as methods and do not receive an object argument, but instead the
object is fixed at the time you import them with this module.

%prep
%setup -q -n Object-Import-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README TODO
%license ARTISTIC GPL
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Chris Adams <linux@cmadams.net> 1.006-1
- new upstream release

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 1.005-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 1.005-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 1.005-1
- initial package
