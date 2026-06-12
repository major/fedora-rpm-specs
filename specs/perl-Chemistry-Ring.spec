%bcond check 1
%define perl_bootstrap 1

Name:           perl-Chemistry-Ring
Version:        0.21
Release:        %autorelease
Summary:        Represent a ring as a substructure of a molecule
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Ring
Source0:        https://cpan.metacpan.org/authors/id/M/ME/MERKYS/Chemistry-Ring-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if %{with check}
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Chemistry::File::SMILES)
%endif
BuildRequires:  perl(Chemistry::Mol) >= 0.24
BuildRequires:  perl(Math::VectorReal)
BuildRequires:  perl(Statistics::Regression) >= 0.15
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
%endif
BuildArch:      noarch
Requires:       perl(Chemistry::Mol) >= 0.24
Requires:       perl(Statistics::Regression) >= 0.15
Requires:       perl(Exporter)

%description
This module provides some basic methods for representing a ring. A ring is a
subclass of molecule, because it has atoms and bonds. Besides that, it has some
useful geometric methods for finding the centroid and the ring plane, and
methods for aromaticity detection.

This module does not detect the rings by itself; for that, look at
Chemistry::Ring::Find.

This module is part of the PerlMol project.

%prep
%autosetup -p1 -n Chemistry-Ring-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} '%{buildroot}'/*

%if %{with check}
%check
make test
%endif

%files
%doc Changes README
%dir %{perl_vendorlib}/Chemistry
%dir %{perl_vendorlib}/Chemistry/Ring
%{perl_vendorlib}/Chemistry/Ring.pm
%{perl_vendorlib}/Chemistry/Ring/Find.pm
%{_mandir}/man3/Chemistry::Ring.3pm.*
%{_mandir}/man3/Chemistry::Ring::Find.3pm.*

%changelog
%autochangelog
