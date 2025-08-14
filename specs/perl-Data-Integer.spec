Name:           perl-Data-Integer
Version:        0.007
Release:        %autorelease
Summary:        Details of the native integer data type
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Integer
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/Data-Integer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(integer)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(warnings)

%description
This module is about the native integer numerical data type. A native
integer is one of the types of datum that can appear in the numeric part
of a Perl scalar. This module supplies constants describing the native
integer type.

%prep
%autosetup -n Data-Integer-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README SECURITY.md
%{perl_vendorlib}/Data
%{_mandir}/man3/Data::Integer*

%changelog
%autochangelog
