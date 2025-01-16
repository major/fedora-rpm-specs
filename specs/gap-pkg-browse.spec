# Automated testing is difficult, since we really want to visually inspect
# the results of the tests.  I have not been able to find a useful automated
# test for this package, so the maintainer should always run this before
# pushing a new version:
#
# gap -l '%%{gap_archdir};' <<< 'Test("tst/test.tst");'
#
# That test is more useful if the altasrep package is also installed.

%global pkgname browse
%global upname Browse

# When bootstrapping a new architecture, there is no gap-pkg-atlasrep or
# gap-pkg-ctbllib package yet.  Those packages are needed only for testing this
# one, but require this package to function at all.  Therefore, do the
# following:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-atlasrep in bootstrap mode.
# 3. Build gap-pkg-tomlib.
# 4. Build gap-pkg-ctbllib in bootstrap mode.
# 5. Build gap-pkg-atlasrep in non-bootstrap mode.
# 6. Build this package in non-bootstrap mode.
# 7. Build gap-pkg-ctbllib in non-bootstrap mode.
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        1.8.21
Release:        %autorelease
Summary:        GAP browser for 2-dimensional arrays of data

License:        GPL-3.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.math.rwth-aachen.de/~Browse/
Source:         %{url}/%{upname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  netpbm-progs
BuildRequires:  pkgconfig(ncurses)

%if %{without bootstrap}
BuildRequires:  gap-pkg-atlasrep-doc
BuildRequires:  gap-pkg-ctbllib-doc
BuildRequires:  gap-pkg-tomlib
%endif

Requires:       gap-core%{?_isa}

Recommends:     gap-pkg-atlasrep
Recommends:     gap-pkg-io%{?_isa}
Recommends:     gap-pkg-tomlib

# Don't Provide the ncurses glue
%global __provides_exclude_from ncurses\\.so

%description
The motivation for this package was to develop functions for an
interactive display of two-dimensional arrays of data, for example
character tables.  They should be displayed with labeled rows and
columns, the display should allow some markup for fonts or colors, it
should be possible to search for entries, to sort rows or columns, to
hide and unhide information, to bind commands to keys, and so on.

To achieve this our package now provides three levels of functionality,
where in particular the first level may also be used for completely
other types of applications:
- A low level interface to ncurses: This may be interesting for all
  kinds of applications which want to display text with some markup and
  colors, maybe in several windows, using the available capabilities of
  a terminal.
- A medium level interface to a generic function NCurses.BrowseGeneric:
  We introduce a new operation Browse which is meant as an interactive
  version of Display for GAP objects.  Then we provide a generic
  function for browsing two-dimensional arrays of data, handles labels
  for rows and columns, searching, sorting, binding keys to actions,
  etc.  This is for users who want to implement new methods for browsing
  two-dimensional data.
- Applications of these interfaces: We provide some applications of the
  ncurses interface and of the function NCurses.BrowseGeneric.  These
  may be interesting for end users, and also as examples for programmers
  of further applications.  This includes a method for browsing
  character tables, several games, and an interface for demos.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Gap browser documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-io-doc

%if %{without bootstrap}
Requires:       gap-pkg-atlasrep-doc
Requires:       gap-pkg-ctbllib-doc
%endif

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%conf
# Give an executable script a shebang
sed -i '1i#!/bin/sh' bibl/getnewestbibfile

%build
# This is NOT an autoconf-generated configure script
./configure %{gap_archdir}
%make_build

# Link to main GAP documentation
mkdir ../pkg
ln -s ../%{upname} ../pkg
gap -l "$PWD/..;" makedocrel.g
rm -fr ../pkg

# Fix links
sed -i "s,$PWD/\.\./pkg,..,g" doc/*.html

%install
rm tst/*~
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{upname}/doc
cp -a app bibl bin lib tst version *.g %{buildroot}%{gap_archdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%files
%doc CHANGES README
%license doc/GPL
%dir %{gap_archdir}/pkg/%{upname}/
%{gap_archdir}/pkg/%{upname}/*.g
%{gap_archdir}/pkg/%{upname}/app/
%{gap_archdir}/pkg/%{upname}/bibl/
%{gap_archdir}/pkg/%{upname}/bin/
%{gap_archdir}/pkg/%{upname}/lib/
%{gap_archdir}/pkg/%{upname}/tst/
%{gap_archdir}/pkg/%{upname}/version

%files doc
%docdir %{gap_archdir}/pkg/%{upname}/doc/
%{gap_archdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
