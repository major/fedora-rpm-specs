%bcond check 1

Name:           perl-Chemistry-File-VRML
Version:        0.10
Release:        %autorelease
Summary:        Generate VRML models for molecules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-File-VRML
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-File-VRML-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
%if %{with check}
BuildRequires:  perl(Chemistry::File)
BuildRequires:  perl(Chemistry::Mol)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%endif
BuildArch:      noarch

%description
This module generates a VRML (Virtual Reality Modeling Language)
representation of a molecule, which can then be visualized with any VRML
viewer. This is a PerlMol file I/O plugin, and registers the 'vrml'
format with Chemistry::Mol. Note however that this file plugin is
write-only; there's no way of reading a VRML file back into a molecule.

This module is a modification of PDB2VRML by Horst Vollhardt, adapted to
the Chemistry::File interface.

%prep
%autosetup -p1 -n Chemistry-File-VRML-%{version}

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
%dir %{perl_vendorlib}/Chemistry/File
%{perl_vendorlib}/Chemistry/File/VRML.pm
%{_mandir}/man3/Chemistry::File::VRML.3pm.*

%changelog
%autochangelog
