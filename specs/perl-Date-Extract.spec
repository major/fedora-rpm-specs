Name:           perl-Date-Extract
Version:        0.07
Release:        %autorelease
Summary:        Date::Extract Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-Extract
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Date-Extract-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(DateTime::Format::Natural) >= 0.60
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::MockTime::HiRes)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter


%description
Search a string for something that looks like a date string, and build a
DateTime object out of it.

%prep
%autosetup -n Date-Extract-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENCE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
