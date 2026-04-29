Name:           perl-Getopt-Tabular
Version:        0.3
Release:        %autorelease
Summary:        Table-driven argument parsing for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Getopt-Tabular
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWARD/Getopt-Tabular-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%description
Getopt::Tabular is a Perl module for table-driven argument parsing,
vaguely inspired by John Ousterhout's Tk_ParseArgv.  All you really need
to do to use the package is set up a table describing all your command-line
options, and call &GetOptions.

%prep
%setup -q -n Getopt-Tabular-%{version}
sed -i 's#/usr/local/bin/perl5#%{__perl}#' demo
chmod a-x demo

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes demo README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
