Name:           frobby
Summary:        Computations with monomial ideals
Version:        0.9.7
Release:        %autorelease

# GPL-2.0-or-later: the frobby code
# OFL-1.1-RFN: AMS fonts embedded in the PDF manual
# Knuth-CTAN: Computer Modern fonts embedded in the PDF manual
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN
URL:            https://github.com/Macaulay2/frobby
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Build a shared library instead of a static library
Patch:          %{name}-sharedlib.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gmp)
# docs
BuildRequires:  doxygen-latex

Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
Frobby is a software system and project for computations with monomial ideals.
Frobby is free software and it is intended as a vehicle for research on
monomial ideals, as well as a useful practical tool for investigating monomial
ideals.

The current functionality includes Hilbert series, maximal standard monomials,
combinatorial optimization on monomial ideals, primary decomposition,
irreducible decomposition, Alexander dual, associated primes, minimization and
intersection of monomial ideals as well as the computation of Frobenius
problems (using 4ti2) with very large numbers.  Frobby is also able to
translate between formats that can be used with several different computer
systems, such as Macaulay 2, Monos, 4ti2, CoCoA4 and Singular.  Thus Frobby
can be used with any of those systems.

%package -n libfrobby
License:        GPL-2.0-or-later
Summary:        Frobby internals as a library

%description -n libfrobby
This package contains the frobby internals as a library, often called
libfrobby.

%package -n libfrobby-devel
License:        GPL-2.0-or-later
Summary:        Developer files for libfrobby
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description -n libfrobby-devel
Header files and library links to develop applications that use the
Frobby internals as a library (libfrobby).

%prep
%autosetup -p1

%conf
%cmake -DBUILD_TESTING:BOOL=ON

%build
export STRIP=true
%cmake_build

# generate docs
cd doc
pdflatex manual.tex
pdflatex manual.tex
cd -

%install
%cmake_install

# We install these later
rm -fr %{buildroot}%{_prefix}/licenses %{buildroot}%{_defaultlicensedir}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir bin
ln -s ../%{_vpath_builddir}/frobby-tests bin/frobby
test/runTests

%files
%doc doc/manual.pdf
%{_bindir}/frobby

%files -n libfrobby
%license COPYING
%{_libdir}/libfrobby.so.0{,.*}

%files -n libfrobby-devel
%{_includedir}/frobby/
%{_libdir}/libfrobby.so

%changelog
%autochangelog
