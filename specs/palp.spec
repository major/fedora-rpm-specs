Name:           palp
Version:        2.21
Release:        %autorelease
Summary:        A Package for Analyzing Lattice Polytopes
License:        GPL-3.0-or-later
URL:            http://hep.itp.tuwien.ac.at/~kreuzer/CY/CYpalp.html
VCS:            git:https://gitlab.com/stringstuwien/PALP.git
Source0:        http://hep.itp.tuwien.ac.at/~kreuzer/CY/palp/palp-%{version}.tar.gz
Source1:        https://export.arxiv.org/pdf/1205.4147

# Do not fork and execute a shell just to delete a file
Patch:          %{name}-unlink.patch
# Fedora changed the name of the latte-integrale "count" binary
Patch:          %{name}-latte.patch
# Fix a use-after-free
# https://gitlab.com/stringstuwien/PALP/-/merge_requests/8
Patch:          %{name}-use-after-free.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make

# Invokes awk, cat, and grep at runtime
Requires:       coreutils
Requires:       gawk
Requires:       grep

# Can invoke latte-integrale's count binary and Singular at runtime
Recommends:     latte-integrale
Recommends:     Singular

%global _docdir_fmt %{name}

%description
PALP contains routines for vertex and facet enumeration, computation of
incidences and symmetries, as well as completion of the set of lattice
points in the convex hull of a given set of points. In addition, there
are procedures specialized to reflexive polytopes such as the enumeration
of reflexive subpolytopes, and applications to toric geometry and string
theory, like the computation of Hodge data and fibration structures for
toric Calabi-Yau varieties.

%package doc
# GPL-3.0-or-later: the content of the documentation
# Knuth-CTAN: Computer Modern fonts embedded in the PDF documentation
# OFL-1.1-RFN: AMS fonts embedded in the PDF documentation
License:        GPL-3.0-or-later AND Knuth-CTAN AND OFL-1.1-RFN
Summary:        Documentation for palp

%description doc
Documentation for palp.

%prep
%autosetup -p1

%build
cp -p %{SOURCE1} 1205.4147v1.pdf

mkdir bin man
mv Global.h Global.h-template
for dim in 4 5 6 11; do
    echo Building PALP optimized for $dim dimensions
    sed "s/^#define[^a-zA-Z]*POLY_Dmax.*/#define POLY_Dmax $dim/" Global.h-template > Global.h
    %make_build
    for file in poly class cws nef mori; do
        mv ${file}.x bin/${file}-${dim}d.x
        help2man -N --version-string=%{version} -h -h bin/${file}-${dim}d.x \
            <<< e | sed '$d' | sed '$d' | sed '$d' > man/${file}-${dim}d.x.1
    done
    make cleanall
done
for file in poly class cws nef mori; do
    help2man -N --version-string=%{version} -h -h bin/${file}.x \
        <<< e | sed '$d' | sed '$d' | sed '$d' > man/${file}.x.1
done

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
pushd bin
    for exe in *.x; do
	install -m 755 $exe $RPM_BUILD_ROOT%{_bindir}/$exe
    done
popd
for file in poly class cws nef mori; do
    ln -sf ${file}-6d.x $RPM_BUILD_ROOT%{_bindir}/${file}.x
done
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%files doc
%doc 1205.4147v1.pdf

%changelog
%autochangelog
