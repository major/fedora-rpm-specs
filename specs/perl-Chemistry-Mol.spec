%bcond check 1

Name:           perl-Chemistry-Mol
Version:        0.40
Release:        %autorelease
Summary:        Molecule object toolkit
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Mol
Source0:        https://cpan.metacpan.org/authors/id/M/ME/MERKYS/Chemistry-Mol-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
%if %{with check}
BuildRequires:  perl(Clone)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Math::VectorReal)
BuildRequires:  perl(Set::Object)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Balanced)
%endif
BuildArch:      noarch

%description
This toolkit includes basic objects and methods to describe molecules. It
consists of several modules: Chemistry::Mol, Chemistry::Atom, Chemistry::Bond,
and Chemistry::File. These are the core modules of the PerlMol toolkit.

%prep
%autosetup -p1 -n Chemistry-Mol-%{version}

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
%{perl_vendorlib}/Chemistry/Atom.pm
%{perl_vendorlib}/Chemistry/Obj.pm
%{perl_vendorlib}/Chemistry/Bond.pm
%{perl_vendorlib}/Chemistry/File.pm
%{perl_vendorlib}/Chemistry/Tutorial.pod
%{perl_vendorlib}/Chemistry/Mol.pm
%{perl_vendorlib}/Chemistry/File/Dumper.pm
%{perl_vendorlib}/Chemistry/File/Formula.pm
%{_mandir}/man3/Chemistry::Mol.3pm.*
%{_mandir}/man3/Chemistry::Obj.3pm.*
%{_mandir}/man3/Chemistry::File::Dumper.3pm.*
%{_mandir}/man3/Chemistry::File.3pm.*
%{_mandir}/man3/Chemistry::Bond.3pm.*
%{_mandir}/man3/Chemistry::File::Formula.3pm.*
%{_mandir}/man3/Chemistry::Tutorial.3pm.*
%{_mandir}/man3/Chemistry::Atom.3pm.*

%changelog
%autochangelog
