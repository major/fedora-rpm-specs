%global gap_pkgname radiroot
%global giturl      https://github.com/gap-packages/radiroot

Name:           gap-pkg-%{gap_pkgname}
Version:        2.9
Release:        %autorelease
Summary:        Compute radicals for roots of solvable rational polynomials

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/radiroot/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
# Fix out of order lines in an example
Patch:          %{name}-example.patch

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): htm lib tst
BuildOption(check): tst/testall.g

BuildRequires:  GAPDoc-doc
BuildRequires:  gap(alnuth) >= 3.0
BuildRequires:  gap-devel >= 4.7
BuildRequires:  tth

Requires:       gap(alnuth) >= 3.0
Requires:       gap-core >= 4.7

Recommends:     texlive-latex
Recommends:     texlive-xdvi

Provides:       gap(RadiRoot) = %{version}-%{release}
Provides:       gap(radiroot) = %{version}-%{release}

%description
This package can compute and display an expression by radicals for the roots
of a solvable, rational polynomial.  Related to this it is possible to create
the Galois group and the splitting field of a rational polynomial.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        Radiroot documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -p0 -n %{gap_upname}-%{version}

%conf
# Fix link to main GAP bibliography file
sed -i 's,/doc/manual,&bib.xml,' doc/manual.tex

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/pkg/GAPDoc ../gapdoc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc} ../gapdoc

%files
%doc CHANGES README
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/htm/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
