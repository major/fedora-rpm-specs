# Upstream made a number of performance improvements after the last release
# was tagged in 2017.
%global commit  0dcf187a159c365b6d4e4e0ed5849f7b706da408
%global date    20181018
%global forgeurl https://github.com/coin-or/Csdp

%global octavedir %{_datadir}/octave/site/m/Csdp

Name:           csdp
Version:        6.2.0
Summary:        C library for SemiDefinite Programming

%forgemeta

# The content is EPL-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
License:        EPL-2.0 AND Knuth-CTAN
Release:        %autorelease
URL:            %{forgeurl}/wiki
VCS:            git:%{forgeurl}.git
Source0:        %{forgesource}
# Written by Jerry James for Octave
Source1:        Csdp.INDEX
# Man pages written by Jerry James with text borrowed freely from the sources.
# These man pages therefore have the same copyright and license as the code.
Source2:        %{name}.1
Source3:        %{name}-theta.1
Source4:        %{name}-graphtoprob.1
Source5:        %{name}-complement.1
Source6:        %{name}-rand_graph.1

# Convert from K&R C to ANSI C to fix problems with GCC 15
Patch:          %{name}-ansi-c.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)

Provides:       coin-or-Csdp = %{version}-%{release}

%description
CSDP is a library of routines that implements a predictor corrector
variant of the semidefinite programming algorithm of Helmberg, Rendl,
Vanderbei, and Wolkowicz.  The main advantages of this code are that it
is written to be used as a callable subroutine, it is written in C for
efficiency, the code runs in parallel on shared memory multiprocessor
systems, and it makes effective use of sparsity in the constraint
matrices.

%package devel
Summary:        Header files for CSDP
License:        EPL-2.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       coin-or-Csdp-devel = %{version}-%{release}

%description devel
This package contains the header files necessary to develop programs
that use the CSDP library.

%package tools
Summary:        Command line tools for working with CSDP
License:        EPL-2.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       coin-or-Csdp-tools = %{version}-%{release}

%description tools
This package contains command-line wrappers around the CSDP library,
including a solver, a program for computing the Lovasz Theta number of a
graph, and some graph manipulation programs.

Note that "csdp-" has been prefixed to some of the binary names, due to
the generic nature of the names.

%package octave
Summary:        Octave interface to CSDP
License:        EPL-2.0
Requires:       %{name}-tools = %{version}-%{release}, octave
BuildArch:      noarch

%description octave
This package contains an Octave interface to the C library for
SemiDefinite Programming.

%prep
%forgeautosetup -p1

%build
# We can't use the shipped build system.  First, a static library is built,
# but we want a shared library.  Second, parallel make is broken; there are no
# explicit dependencies between subdirectories.  Third, the CFLAGS need to be
# altered in various more-or-less drastic ways.  Fourth, the existing makefiles
# link all binaries with the entire set of libs, but not all binaries need all
# libs.  We build by hand to contain the pain.

# Choose the CFLAGS we want
CFLAGS='%{build_cflags} -I../include -I%{_includedir}/flexiblas -DNOSHORTS -DUSESIGTERM -DUSEGETTIME -DBIT64 -DHIDDENSTRLEN -DCSDP_NEED_BLAS'
LIBS='%{build_ldflags} -L../lib -lsdp'
sed -i -e "s|^CFLAGS=.*|CFLAGS=${CFLAGS}|" \
       -e "s|^LIBS=.*|LIBS=${LIBS} -lflexiblas -lm|" \
    solver/Makefile theta/Makefile

# Build the shared library
cd lib
gcc ${CFLAGS} -DUSEOPENMP -fopenmp -fPIC -shared -Wl,--soname=libsdp.so.6 *.c \
  -o libsdp.so.%{version} %{build_ldflags} -lgomp -lflexiblas -lm
ln -s libsdp.so.%{version} libsdp.so.6
ln -s libsdp.so.6 libsdp.so

# Build the solver
cd ../solver
%make_build CFLAGS="$CFLAGS" LIBS="$LIBS"

# Build theta, but don't necessarily link with everything
cd ../theta
gcc $CFLAGS -c complement.c
gcc $CFLAGS -o complement %{build_ldflags} complement.o
gcc $CFLAGS -c rand_graph.c
gcc $CFLAGS -o rand_graph %{build_ldflags} rand_graph.o
%make_build CFLAGS="$CFLAGS" LIBS="$LIBS"

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -pP lib/libsdp* %{buildroot}%{_libdir}

# Install the binaries
mkdir -p %{buildroot}%{_bindir}
cp -p solver/csdp %{buildroot}%{_bindir}
cp -p theta/theta %{buildroot}%{_bindir}/csdp-theta
cp -p theta/graphtoprob %{buildroot}%{_bindir}/csdp-graphtoprob
cp -p theta/complement %{buildroot}%{_bindir}/csdp-complement
cp -p theta/rand_graph %{buildroot}%{_bindir}/csdp-rand_graph

# Install the header files
mkdir -p %{buildroot}%{_includedir}/csdp
cp -p include/*.h %{buildroot}%{_includedir}/csdp

# Install the Octave interface
mkdir -p %{buildroot}%{octavedir}
cp -p matlab/*.m %{buildroot}%{octavedir}
cp -p %{SOURCE1} %{buildroot}%{octavedir}/INDEX

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
  %{buildroot}%{_mandir}/man1

%files
%doc AUTHORS README.md doc/csdpuser.pdf
%license LICENSE
%{_libdir}/libsdp.so.6*

%files devel
%doc doc/example.c
%{_libdir}/libsdp.so
%{_includedir}/%{name}

%files tools
%doc theta/README
%{_bindir}/csdp*
%{_mandir}/man1/csdp*

%files octave
%doc matlab/README
%{octavedir}

%changelog
%autochangelog
