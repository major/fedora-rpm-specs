%bcond check 1

Name:           perl-Chemistry-Bond-Find
Version:        0.23
Release:        %autorelease
Summary:        Detect bonds in a molecule from atomic 3D coords and assign formal bond orders
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Bond-Find
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-Bond-Find-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
%if %{with check}
BuildRequires:  perl(Chemistry::Mol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
%endif
BuildArch:      noarch

%description
This module provides functions for detecting the bonds in a molecule from its
3D coordinates by using simple cutoffs, and for guessing the formal bond
orders.

%prep
%autosetup -p1 -n Chemistry-Bond-Find-%{version}
chmod -x Changes Makefile.PL README t/*.t

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
%dir %{perl_vendorlib}/Chemistry/Bond
%{perl_vendorlib}/Chemistry/Bond/Find.pm
%{_mandir}/man3/Chemistry::Bond::Find.3pm.*

%changelog
%autochangelog
