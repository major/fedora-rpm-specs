Name:           perl-Encoding-FixLatin
Version:        1.04
Release:        2%{?dist}
Summary:        Takes mixed encoding input and produces UTF-8 output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Encoding-FixLatin
Source0:        https://www.cpan.org/modules/by-module/Encoding/Encoding-FixLatin-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More) >= 0.90
# test
# Circular dependency
#BuildRequires:  perl(Encoding::FixLatin::XS) >= 1.00
BuildRequires:  perl(Test::More)
# runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Recommends:     perl(Encoding::FixLatin::XS) >= 1.00

%description
Most encoding conversion tools take input in one encoding and produce
output in another encoding. This module takes input which may contain
characters in more than one encoding and makes a best effort to convert
them all to UTF-8 output.

%prep
%setup -q -n Encoding-FixLatin-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%dir %{perl_vendorlib}/Encoding/
%{perl_vendorlib}/Encoding/FixLatin.pm
%{_mandir}/man1/fix_latin.1*
%{_mandir}/man3/Encoding::FixLatin.3pm*
%{_bindir}/fix_latin


%changelog
* Wed Sep 09 2026 Xavier Bachelot <xavier@bachelot.org> 1.04-2
- Review fixes

* Tue May 26 2026 Xavier Bachelot <xavier@bachelot.org> 1.04-1
- Initial specfile
