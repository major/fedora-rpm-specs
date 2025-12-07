%bcond check 1

Name:           perl-Chemistry-Canonicalize
Version:        0.11
Release:        %autorelease
Summary:        Number the atoms in a molecule in a unique way
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Canonicalize
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-Canonicalize-%{version}.tar.gz
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
This module provides functions for "canonicalizing" a molecular
structure; that is, to number the atoms in a unique way regardless of
the input order.

The canonicalization algorithm is based on: Weininger, et. al., J. Chem.
Inf. Comp. Sci. 29[2], 97-101 (1989)

This module is part of the PerlMol project.

%prep
%autosetup -p1 -n Chemistry-Canonicalize-%{version}
chmod -x README

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
%{perl_vendorlib}/Chemistry/Canonicalize.pm
%{_mandir}/man3/Chemistry::Canonicalize.3pm.*

%changelog
%autochangelog
