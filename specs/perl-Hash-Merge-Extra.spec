Name:           perl-Hash-Merge-Extra
Version:        0.06
Release:        1%{?dist}
Summary:        Collection of extra behaviors for Hash::Merge
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Hash-Merge-Extra
Source0:        http://www.cpan.org/modules/by-module/Hash/Hash-Merge-Extra-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)

%description
Collection of extra behaviors for Hash::Merge.

%prep
%setup -q -n Hash-Merge-Extra-%{version}

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
%{perl_vendorlib}/Hash/
%{_mandir}/man3/Hash::Merge::Extra.3pm*


%changelog
* Tue Oct 06 2026 Xavier Bachelot <xavier@bachelot.org> 0.06-1
- Initial specfile
