Name:           perl-AnyEvent-XSPromises
Version:        0.006
Release:        2%{?dist}
Summary:        Another Promises library, this time implemented in XS for performance
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent-XSPromises
Source0:        http://www.cpan.org/modules/by-module/AnyEvent/AnyEvent-XSPromises-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(AnyEvent) >= 7
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More)


%description
This library provides a Promises interface, written in XS for performance,
conforming to the Promises/A+ specification.

%prep
%setup -q -n AnyEvent-XSPromises-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/AnyEvent/XSPromises/
%{perl_vendorarch}/AnyEvent/XSPromises*
%{_mandir}/man3/AnyEvent::XSPromises.3pm*

%changelog
* Tue Aug 05 2025 Xavier Bachelot <xavier@bachelot.org> 0.006-2
- Fixup according to review

* Fri Jul 25 2025 Xavier Bachelot <xavier@bachelot.org> 0.006-1
- Initial spec file
