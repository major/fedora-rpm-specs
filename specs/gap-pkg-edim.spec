%global pkgname edim
%global upname  EDIM

Name:           gap-pkg-%{pkgname}
Version:        1.3.8
Release:        %autorelease
Summary:        Elementary divisors of integer matrices

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/EDIM/
VCS:            git:https://github.com/frankluebeck/EDIM.git
Source:         %{url}%{upname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
The main purpose of the EDIM package is to publish an implementation of
an algorithm (found by the package author) for computing prime parts of
the elementary divisors of integer matrices (i.e., the diagonal entries
of the Smith normal form).

The programs are developed and already successfully used for large
matrices (up to rank >12000) with moderate entries and many non-trivial
elementary divisors which are products of some small primes. But they
should be useful for other types of matrices as well.

Among the other functions of the package are:
- an inversion algorithm for large rational matrices (using a p-adic
  method)
- a program for finding the largest elementary divisor of an integral
  matrix (particularly interesting when this is much smaller than the
  determinant) and
- implementations of some normal form algorithms described by Havas,
  Majewski, Matthews, Sterling (using LLL- or modular techniques).

%package doc
# The content is GPL-2.0-or-later.
# doc/mathml.css is MPL-1.1.
# The remaining licenses cover the various fonts embedded in PDFs:
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND MPL-1.1 AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        EDIM documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%conf
# Fix encodings
for fil in doc/edim.bib doc/edim.bbl; do
  iconv -f iso8859-1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%build
# This is NOT an autoconf-generated script.  Do not use %%configure.
./configure %{gap_archdir}
%make_build

# Link to main GAP documentation
sed -i.orig '/IsBound/ipathtoroot := "%{gap_libdir}";' makedocrel.g
mkdir ../pkg
ln -s ../%{upname}-%{version} ../pkg
gap -l "$PWD/..;" makedocrel.g
rm -fr ../pkg
mv makedocrel.g.orig makedocrel.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{upname}/doc
cp -a *.g bin lib tst VERSION %{buildroot}%{gap_archdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
gap -l '%{buildroot}%{gap_archdir};' tst/testinstall.g

%files
%doc CHANGES README TODO
%license GPL
%dir %{gap_archdir}/pkg/%{upname}/
%{gap_archdir}/pkg/%{upname}/*.g
%{gap_archdir}/pkg/%{upname}/bin/
%{gap_archdir}/pkg/%{upname}/lib/
%{gap_archdir}/pkg/%{upname}/tst/
%{gap_archdir}/pkg/%{upname}/VERSION

%files doc
%docdir %{gap_archdir}/pkg/%{upname}/doc/
%{gap_archdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
