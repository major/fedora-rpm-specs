%global octavedir %{_datadir}/octave/site/m/Csdp

Name:           csdp
Version:        6.2.0
Release:        14%{?dist}
Summary:        C library for SemiDefinite Programming

License:        CPL-1.0
URL:            https://github.com/coin-or/Csdp/wiki
Source0:        http://www.coin-or.org/download/source/Csdp/Csdp-%{version}.tgz
# Written by Jerry James for Octave
Source1:        Csdp.INDEX
# Man pages written by Jerry James with text borrowed freely from the sources.
# These man pages therefore have the same copyright and license as the code.
Source2:        %{name}.1
Source3:        %{name}-theta.1
Source4:        %{name}-graphtoprob.1
Source5:        %{name}-complement.1
Source6:        %{name}-rand_graph.1
# Fix a missing printf prototype
Patch0:         %{name}-printf.patch

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
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       coin-or-Csdp-devel = %{version}-%{release}

%description devel
This package contains the header files necessary to develop programs
that use the CSDP library.

%package tools
Summary:        Command line tools for working with CSDP
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
Requires:       %{name}-tools = %{version}-%{release}, octave
BuildArch:      noarch

%description octave
This package contains an Octave interface to the C library for
SemiDefinite Programming.

%prep
%setup -q -n Csdp-%{version}
%patch0

%build
# We can't use the shipped build system.  First, a static library is built,
# but we want a shared library.  Second, parallel make is broken; there are no
# explicit dependencies between subdirectories.  Third, the CFLAGS need to be
# altered in various more-or-less drastic ways.  Fourth, the existing makefiles
# link all binaries with the entire set of libs, but not all binaries need all
# libs.  We build by hand to contain the pain.

# Choose the CFLAGS we want
CFLAGS="%{build_cflags} -I../include -I%{_includedir}/flexiblas -DNOSHORTS -DUSESIGTERM -DUSEGETTIME"
if [ %{__isa_bits} = "64" ]; then
  CFLAGS+=" -DBIT64"
fi
sed -i -e "s|^CFLAGS=.*|CFLAGS=${CFLAGS}|" \
       -e "s|^LIBS=.*|LIBS=%{build_ldflags} -L../lib -lsdp -lflexiblas -lm|" \
    solver/Makefile theta/Makefile

# Build the shared library
cd lib
gcc ${CFLAGS} -DUSEOPENMP -fopenmp -fPIC -shared -Wl,--soname=libsdp.so.6 *.c \
  -o libsdp.so.%{version} %{build_ldflags} -lgomp -lflexiblas -lm
ln -s libsdp.so.%{version} libsdp.so.6
ln -s libsdp.so.6 libsdp.so

# Build the solver
cd ../solver
%make_build CFLAGS="$CFLAGS" LIBS="%{build_ldflags} -L../lib -lsdp"

# Build theta, but don't necessarily link with everything
cd ../theta
gcc $CFLAGS -c complement.c
gcc $CFLAGS -o complement %{build_ldflags} complement.o
gcc $CFLAGS -c rand_graph.c
gcc $CFLAGS -o rand_graph %{build_ldflags} rand_graph.o
%make_build CFLAGS="$CFLAGS" LIBS="%{build_ldflags} -L../lib -lsdp"

%install
# Install the library
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp -pP lib/libsdp* $RPM_BUILD_ROOT%{_libdir}

# Install the binaries
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p solver/csdp $RPM_BUILD_ROOT%{_bindir}
cp -p theta/theta $RPM_BUILD_ROOT%{_bindir}/csdp-theta
cp -p theta/graphtoprob $RPM_BUILD_ROOT%{_bindir}/csdp-graphtoprob
cp -p theta/complement $RPM_BUILD_ROOT%{_bindir}/csdp-complement
cp -p theta/rand_graph $RPM_BUILD_ROOT%{_bindir}/csdp-rand_graph

# Install the header files
mkdir -p $RPM_BUILD_ROOT%{_includedir}/csdp
cp -p include/*.h $RPM_BUILD_ROOT%{_includedir}/csdp

# Install the Octave interface
mkdir -p $RPM_BUILD_ROOT%{octavedir}
cp -p matlab/*.m $RPM_BUILD_ROOT%{octavedir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{octavedir}/INDEX

# Install the man pages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
  $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc AUTHORS README doc/csdpuser.pdf
%license LICENSE
%{_libdir}/libsdp.so.*

%files devel
%doc doc/example.c
%{_libdir}/libsdp.so
%{_includedir}/%{name}

%files tools
%doc theta/README
%{_bindir}/*
%{_mandir}/man1/*

%files octave
%doc matlab/README
%{octavedir}

%changelog
* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 6.2.0-14
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Iñaki Úcar <iucar@fedoraproject.org> - 6.2.0-10
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 6.2.0-6
- Change the project URL to github
- Add more coin-or-Csdp-* provides

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 16 2017 Jerry James <loganjerry@gmail.com> - 6.2.0-2
- Build with openblas instead of atlas

* Sat Aug  5 2017 Jerry James <loganjerry@gmail.com> - 6.2.0-1
- New upstream version
- Provide coin-or-Csdp for parity with other coin-or packages
- Add -printf patch to fix build failure
- Switch from multithreaded atlas to single-threaded atlas

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 6.1.1-12
- Rebuild for octave 4.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 12 2015 Jerry James <loganjerry@gmail.com> - 6.1.1-9
- Link with RPM_LD_FLAGS
- Use license macro
- Minor spec file cleanups

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 21 2013 Jerry James <loganjerry@gmail.com> - 6.1.1-6
- Rebuild for atlas 3.10.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 6.1.1-2
- Rebuild for GCC 4.7

* Fri Mar 18 2011 Jerry James <loganjerry@gmail.com> - 6.1.1-1
- Initial RPM
