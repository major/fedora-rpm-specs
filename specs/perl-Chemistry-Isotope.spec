%bcond check 1

Name:           perl-Chemistry-Isotope
Version:        0.11
Release:        %autorelease
Summary:        Table of the isotopes exact mass data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Isotope
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-Isotope-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
%if %{with check}
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
%endif
BuildArch:      noarch

%description
This module contains the exact mass data from the table of the isotopes. It has
an exportable function, isotope_mass, which returns the mass of an atom in mass
units given its mass number (A) and atomic number (Z); and a function
isotope_abundance which returns a table with the natural abundance of the
isotopes given an element symbol.

The table of the masses includes 2931 nuclides and is taken from
http://ie.lbl.gov/txt/awm95.txt (G. Audi and A.H. Wapstra, Nucl. Phys. A595,
409, 1995)

The table of natural abundances includes 288 nuclides and is taken from the
Commission on Atomic Weights and Isotopic Abundances report for the
International Union of Pure and Applied Chemistry in Isotopic Compositions of
the Elements 1989, Pure and Applied Chemistry, 1998, 70, 217.
http://www.iupac.org/publications/pac/1998/pdf/7001x0217.pdf

%prep
%autosetup -p1 -n Chemistry-Isotope-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} '%{buildroot}'/*

%if %{with check}
%check
make test
%endif

%files
%doc README
%dir %{perl_vendorlib}/Chemistry
%{perl_vendorlib}/Chemistry/Isotope.pm
%{_mandir}/man3/Chemistry::Isotope.3pm.*

%changelog
%autochangelog
