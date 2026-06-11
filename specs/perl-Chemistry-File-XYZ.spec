Name:           perl-Chemistry-File-XYZ
Version:        0.11
Release:        %autorelease
Summary:        XYZ molecule format reader/writer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-File-XYZ
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-File-XYZ-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Chemistry::File)
BuildRequires:  perl(Chemistry::Mol)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(warnings)
BuildArch:      noarch

%description
This module reads XYZ files. It automatically registers the 'xyz' format
with Chemistry::Mol, so that XYZ files may be identified and read by
Chemistry::Mol->read().

%prep
%autosetup -p1 -n Chemistry-File-XYZ-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} '%{buildroot}'/*

%check
make test

%files
%doc README
%dir %{perl_vendorlib}/Chemistry
%dir %{perl_vendorlib}/Chemistry/File
%{perl_vendorlib}/Chemistry/File/XYZ.pm
%{_mandir}/man3/Chemistry::File::XYZ.3pm.*

%changelog
%autochangelog
