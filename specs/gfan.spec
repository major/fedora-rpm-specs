Name:           gfan
Version:        0.7
Release:        %autorelease
Summary:        Software for Computing Gröbner Fans and Tropical Varieties
License:        GPL-2.0-or-later
URL:            https://math.au.dk/~jensen/software/gfan/gfan.html
Source:         https://math.au.dk/~jensen/software/%{name}/%{name}%{version}.tar.gz
# Sent upstream 2011 Apr 27.  Fix warnings that could indicate runtime
# problems.
Patch:          %{name}-warning.patch
# Build a shared library
Patch:          %{name}-shared.patch
# Adapt to the version of SoPlex packaged for Fedora
Patch:          %{name}-soplex.patch
# The C++20 standard is too new for Singular, leading to many build failures.
# Work around the only place in the code that needs C++20.
Patch:          %{name}-c++20.patch
# Fix Singular FTBFS due to missing gcd function for Rational
Patch:          %{name}-gcd.patch
# Fix Singular abort due to accessing an empty vector
Patch:          %{name}-multiplicities.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cddlib-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  glibc-langpack-en
BuildRequires:  gmp-devel
BuildRequires:  libsoplex-devel
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(ulem.sty)
BuildRequires:  TOPCOM

Requires:       libgfan%{_isa} = %{version}-%{release}

Recommends:     TOPCOM

%global _docdir_fmt %{name}

%description
The software computes all marked reduced Gröbner bases of an ideal.
Their union is a universal Gröbner basis. Gfan contains algorithms for
computing this complex for general ideals and specialized algorithms
for tropical curves, tropical hypersurfaces and tropical varieties of
prime ideals. In addition to the above core functions the package
contains many tools which are useful in the study of Gröbner bases,
initial ideals and tropical geometry. Among these are an interactive
traversal program for Gröbner fans and programs for graphical renderings.

%package        doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
Summary:        Gfan examples and documentation files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
Gfan examples and documentation files.

%package        -n libgfan
Summary:        Polyhedral computations related to polynomial rings

%description    -n libgfan
Gfanlib has two major features:
1) high-level exact polyhedral cone and polyhedral fan classes;
2) fast exact mixed volume computation for lattice polytopes with overflow
   checking.

In particular, gfanlib is missing the Gröbner basis part of gfan.

%package        -n libgfan-devel
Summary:        Development files for libgfan
Requires:       libgfan%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    -n libgfan-devel
The libgfan-devel package contains libraries and header files for
developing applications that use libgfan.

%prep
%autosetup -n %{name}%{version} -p1

%conf
# Point to where the TOPCOM binaries will be installed
sed -i.orig "s|^\(#define MINKOWSKIPROGRAM \).*|\1\"%{_bindir}/essai\"|" \
  src/minkowskisum.cpp
touch -r src/minkowskisum.cpp.orig src/minkowskisum.cpp
rm -f src/minkowskisum.cpp.orig

# No need to install a simple upstream Makefile to rsync homepage
# directory to upstream page.
rm -f homepage/Makefile

%build
# Enable use of SoPlex
sed -e 's|^\(SOPLEX_PATH = \).*|\1%{_prefix}|' \
    -e 's|^\(SOPLEX_LINKOPTIONS = \).*|\1%{build_ldflags} -lsoplex -lclusol -lmpfr -ltbb -lz-ng|' \
    -e 's|^\(SOPLEX_INCLUDEOPTIONS = \).*|\1|' \
    -i Makefile

%make_build CC=gcc CXX=g++ \
  OPTFLAGS='%{build_cxxflags} -DGMPRATIONAL -DNDEBUG -I%{_includedir}/cddlib' \
  PREFIX=%{_prefix} \
  soplex=true

# Build the manual
cd doc
latex manual.tex
bibtex manual
latex manual.tex
latex manual.tex
dvipdf manual.dvi manual.pdf
cd -

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p src/libgfan.so.0.0.0 %{buildroot}%{_libdir}
ln -s libgfan.so.0.0.0 %{buildroot}%{_libdir}/libgfan.so.0
ln -s libgfan.so.0 %{buildroot}%{_libdir}/libgfan.so

# Install the headers
mkdir -p %{buildroot}%{_includedir}/gfanlib
cp -p src/gfanlib*.h %{buildroot}%{_includedir}/gfanlib

# Fix the headers
for fil in %{buildroot}%{_includedir}/gfanlib/*.h; do
  sed -i.orig 's,#include "\(.*\)",#include <\1>,' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

# Install the binaries
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make install PREFIX=%{buildroot}%{_prefix}
cd %{buildroot}%{_bindir}
    ./%{name} installlinks
cd -


%check
# Some tests depend on US English collation order
export LC_ALL=en_US.UTF-8

# The xfig test output varies slightly by architecture, and is non-critical,
# so we skip that test.
rm -fr testsuite/0009RenderStairCase
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
./gfan _test


%files
%doc README
%license COPYING LICENSE
%{_bindir}/gfan*

%files doc
%doc doc/manual.pdf
%doc examples
%doc homepage

%files -n libgfan
%doc gfanlib/README.txt
%{_libdir}/libgfan.so.0*

%files -n libgfan-devel
%{_includedir}/gfanlib/
%{_libdir}/libgfan.so


%changelog
%autochangelog
