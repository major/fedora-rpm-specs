%global module Ipopt

## Define libraries' destination
%global _incmpidir %{_includedir}/openmpi-%{_arch}
%global _libmpidir %{_libdir}/openmpi/lib
%global _binmpidir %{_libdir}/openmpi/bin
%global _incmpichdir %{_includedir}/mpich-%{_arch}
%global _libmpichdir %{_libdir}/mpich/lib
%global _binmpichdir %{_libdir}/mpich/bin

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%global with_openmpi 0
%else
%global with_openmpi 1
%endif
%else
%global with_openmpi 1
%endif
%global with_mpich 1
%global with_mpicheck 1
%global with_mpichcheck 1

%global with_asl 1
%global blaslib flexiblas

Name:  coin-or-%{module}
Summary: Interior Point OPTimizer
Version: 3.14.16
Release: %autorelease
License: EPL-2.0
URL:  https://coin-or.github.io/%{module}/
Source0: https://github.com/coin-or/Ipopt/archive/releases/%{version}/Ipopt-releases-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

BuildRequires: %{?dts}gcc, %{?dts}gcc-c++
BuildRequires: %{?dts}gcc-gfortran
BuildRequires: %{blaslib}-devel
BuildRequires: doxygen
BuildRequires: help2man
BuildRequires: make
BuildRequires: MUMPS-devel
BuildRequires: metis-devel
%if 0%{?with_asl}
BuildRequires: asl-devel
%endif
BuildRequires: openssh-clients
BuildRequires: pkgconfig
BuildRequires: hwloc-devel
BuildRequires: texlive-bibtex
BuildRequires: texlive-latex-bin-bin
BuildRequires: texlive-dvips
%if 0%{?fedora}
BuildRequires: tex(newunicodechar.sty)
%endif

Requires: %{name}-common = %{version}-%{release}

%description
Ipopt (Interior Point OPTimizer, pronounced eye-pea-Opt) is a software
package for large-scale nonlinear optimization. It is designed to find
(local) solutions of mathematical optimization problems of the form

   min     f(x)
x in R^n

s.t.       g_L <= g(x) <= g_U
           x_L <=  x   <= x_U

where f(x): R^n --> R is the objective function, and g(x): R^n --> R^m are
the constraint functions. The vectors g_L and g_U denote the lower and upper
bounds on the constraints, and the vectors x_L and x_U are the bounds on
the variables x. The functions f(x) and g(x) can be non-linear and non-convex,
but should be twice continuously differentiable. Note that equality
constraints can be formulated in the above formulation by setting the
corresponding components of g_L and g_U to the same value.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        common
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    common
This package contains the HTML documentation,
a PDF tutorial to use %{name} and related
license files.

########################################################
%if 0%{?with_openmpi}
%package openmpi
Summary: Interior Point OPTimizer compiled against openmpi
BuildRequires:  MUMPS-openmpi-devel
BuildRequires:  pkgconfig(ompi)
BuildRequires:  scalapack-openmpi-devel
BuildRequires:  ptscotch-openmpi-devel
Requires: %{name}-common = %{version}-%{release}
%description openmpi
%{name} libraries compiled against openmpi.

%package openmpi-devel
Summary: The %{name} headers and development-related files
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel
Shared links and header files for developing applications that
use %{name}-openmpi.
%endif
##########################################################
########################################################
%if 0%{?with_mpich}
%package mpich
Summary: Interior Point OPTimizer compiled against mpich
BuildRequires:  MUMPS-mpich-devel
BuildRequires:  mpich-devel
BuildRequires:  scalapack-mpich-devel
BuildRequires:  ptscotch-mpich-devel
Requires: %{name}-common = %{version}-%{release}
%description mpich
%{name} libraries compiled against MPICH.

%package mpich-devel
Summary: The %{name} headers and development-related files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel
Shared links and header files for developing applications that
use %{name}-mpich.
%endif
##########################################################

%prep
%setup -qc

pushd Ipopt-releases-%{version}

# Generate a doxygen tag file, disabled upstream in the 3.13.0 release
sed -i 's/#\(GENERATE_TAGFILE\)/\1/' doc/Doxyfile.in

# Fix the include file location
sed -i 's,\(@includedir@/coin\)-or,\1,' src/ipopt.pc.in
popd

%if 0%{?with_openmpi}
cp -a Ipopt-releases-%{version} %{module}-releases-openmpi
%endif
%if 0%{?with_mpich}
cp -a Ipopt-releases-%{version} %{module}-releases-mpich
%endif


%build

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-9/enable}
%endif

#######################################################
## Build serial version

cd Ipopt-releases-%{version}

export LIBLAPACK=-l%{blaslib}
export INCLAPACK=-I%{_includedir}/%{blaslib}

OPT_CFLAGS="%{build_ldflags}"
OPT_CXXFLAGS="%{build_cxxflags}"
CPPFLAGS="-I%{_includedir}/MUMPS"
CXXLIBS="-L%{_libdir} -ldmumps $LIBLAPACK -lmetis -ldl"
%configure CC=gcc CXX=g++ F77=gfortran CFLAGS="%{build_cflags} $INCLAPACK" CXXFLAGS="%{build_cxxflags} $INCLAPACK" \
           LDFLAGS="%{build_ldflags}" CXXLIBS="$CXXLIBS" \
 --with-mumps --with-mumps-cflags=-I%{_includedir}/MUMPS --with-mumps-lflags=-ldmumps \
 --with-lapack --with-lapack-lflags=$LIBLAPACK --enable-mpiinit \
%if 0%{?with_asl}
 --with-asl-cflags=-I%{_includedir}/asl --with-asl-lflags="-lasl" \
%endif
 --enable-shared --disable-java

pushd doc
sed -i '/LATEX_BATCHMOD/s/NO/YES/' Doxyfile
doxygen -u
popd

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build V=1 all doc
cd ..
#######################################################

#######################################################
## Build MPI version
%if 0%{?with_openmpi}

cd %{module}-releases-openmpi
%{_openmpi_load}
export LIBLAPACK=-l%{blaslib}
export INCLAPACK=-I%{_includedir}/%{blaslib}
CFLAGS="%{build_cxxflags} $INCLAPACK"
OPT_CFLAGS="%{build_cflags} $INCLAPACK"
LDFLAGS="%{build_ldflags}"
CXXFLAGS="%{build_cxxflags} $INCLAPACK"
OPT_CXXFLAGS="%{build_cxxflags} $INCLAPACK"
%if 0%{?rhel}
CPPFLAGS=" -pthread -I$MPI_INCLUDE"
CXXLIBS=" -L$MPI_LIB -lmpi_mpifh -lmpi -lscalapack -ldmumps -lmumps_common -lptscotcherr -lptscotch -lptesmumps -ldl"
%else
CPPFLAGS="$(pkg-config --cflags ompi-fort)"
CXXLIBS="$(pkg-config --libs ompi) $(pkg-config --libs ompi-fort) -lscalapack -ldmumps -lmumps_common -lptscotcherr -lptscotch -lptesmumps -ldl"
%endif
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
export F77=$MPI_BIN/mpif77

%configure --with-mumps-cflags=" -I$MPI_INCLUDE/MUMPS" \
 --with-mumps --with-mumps-lflags="-L$MPI_LIB -ldmumps -lmumps_common" --with-mumps-cflags="-I$MPI_INCLUDE/MUMPS" \
 --with-lapack --with-lapack-lflags=$LIBLAPACK --disable-java --enable-mpiinit \
%if 0%{?with_asl}
 --with-asl-cflags=-I%{_includedir}/asl --with-asl-lflags="-lasl" \
%endif
            MPICC=$MPI_BIN/mpicc \
            MPICXX=$MPI_BIN/mpic++ \
            MPIF77=$MPI_BIN/mpif77 \
            ADD_CFLAGS="-fopenmp" \
            ADD_FFLAGS="-fopenmp" \
            ADD_CXXFLAGS="-fopenmp" \
            CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" \
            LDFLAGS="$LDFLAGS" CXXLIBS="$CXXLIBS"

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
 sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
     -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
     -i libtool

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MPI_LIB
%make_build V=1 all
%{_openmpi_unload}
cd ..
%endif

#######################################################
## Build MPICH version
%if 0%{?with_mpich}

cd %{module}-releases-mpich
%{_mpich_load}
export LIBLAPACK=-l%{blaslib}
export INCLAPACK=-I%{_includedir}/%{blaslib}
CFLAGS="%{build_cflags} $INCLAPACK"
OPT_CFLAGS="%{build_cflags} $INCLAPACK"
LDFLAGS="%{build_ldflags}"
CXXFLAGS="%{build_cxxflags} $INCLAPACK"
OPT_CXXFLAGS="%{build_cxxflags} $INCLAPACK"
CPPFLAGS="$(pkg-config --cflags mpich)"
CXXLIBS="$(pkg-config --libs mpich) -lscalapack -ldmumps -lmumps_common -lptscotcherr -lptscotch -lptesmumps -ldl"
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
export F77=$MPI_BIN/mpif77

%configure --with-mumps-cflags=" -I$MPI_INCLUDE/MUMPS" \
 --with-mumps --with-mumps-lflags="-L$MPI_LIB -ldmumps -lmumps_common" --with-mumps-cflags="-I$MPI_INCLUDE/MUMPS" \
 --with-lapack --with-lapack-lflags=$LIBLAPACK --disable-java --enable-mpiinit \
%if 0%{?with_asl}
 --with-asl-cflags=-I%{_includedir}/asl --with-asl-lflags="-lasl" \
%endif
            MPICC=$MPI_BIN/mpicc \
            MPICXX=$MPI_BIN/mpic++ \
            MPIF77=$MPI_BIN/mpif77 \
            ADD_CFLAGS="-fopenmp" \
            ADD_FFLAGS="-fopenmp" \
            ADD_CXXFLAGS="-fopenmp" \
            CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" \
            LDFLAGS="$LDFLAGS" CXXLIBS="$CXXLIBS"

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
 sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
     -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
     -i libtool

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MPI_LIB
%make_build V=1 all
%{_mpich_unload}
cd ..
%endif

%install

#######################################################
## Install MPI version
%if 0%{?with_openmpi}
%{_openmpi_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT$MPI_BIN
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE
mkdir -p %{module}-releases-openmpi/headers

cd %{module}-releases-openmpi
 cp -p --no-dereference src/.libs/libipopt.so* \
       $RPM_BUILD_ROOT$MPI_LIB/
 cp -p --no-dereference contrib/sIPOPT/src/.libs/libsipopt.so* \
       $RPM_BUILD_ROOT$MPI_LIB/
%if 0%{?with_asl}
 cp -p --no-dereference src/Apps/AmplSolver/.libs/libipoptamplinterface.so* \
       $RPM_BUILD_ROOT$MPI_LIB/
 cp -p --no-dereference src/Apps/AmplSolver/.libs/ipopt \
       $RPM_BUILD_ROOT$MPI_BIN/
 cp -p --no-dereference contrib/sIPOPT/AmplSolver/ipopt_sens \
       $RPM_BUILD_ROOT$MPI_BIN/
%endif

 find -O3 src \( -name \*.h -o -name \*.hpp \) -exec cp -p {} headers \;
 cp -p contrib/sIPOPT/src/*.hpp src/Common/*.h headers
cd ..

##Copy MPI header files
install -p -m 644 %{module}-releases-openmpi/headers/* $RPM_BUILD_ROOT$MPI_INCLUDE
%{_openmpi_unload}
%endif

#######################################################
#######################################################
## Install MPICH version
%if 0%{?with_mpich}
%{_mpich_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT$MPI_BIN
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE
mkdir -p %{module}-releases-mpich/headers

cd %{module}-releases-mpich
 cp -p --no-dereference src/.libs/libipopt.so* \
       $RPM_BUILD_ROOT$MPI_LIB/
 cp -p --no-dereference contrib/sIPOPT/src/.libs/libsipopt.so* \
       $RPM_BUILD_ROOT$MPI_LIB/
%if 0%{?with_asl}
 cp -p --no-dereference src/Apps/AmplSolver/.libs/libipoptamplinterface.so* \
       $RPM_BUILD_ROOT$MPI_LIB/
 cp -p --no-dereference src/Apps/AmplSolver/.libs/ipopt \
       $RPM_BUILD_ROOT$MPI_BIN/
 cp -p --no-dereference contrib/sIPOPT/AmplSolver/ipopt_sens \
       $RPM_BUILD_ROOT$MPI_BIN/
%endif

 find -O3 src \( -name \*.h -o -name \*.hpp \) -exec cp -p {} headers \;
 cp -p contrib/sIPOPT/src/*.hpp src/Common/*.h headers
cd ..

##Copy MPI header files
install -p -m 644 %{module}-releases-mpich/headers/* $RPM_BUILD_ROOT$MPI_INCLUDE
%{_mpich_unload}
%endif

#######################################################

## Install serial version

mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/coin
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}

mkdir -p Ipopt-releases-%{version}/headers

cd Ipopt-releases-%{version}
 ##Copy libraries
 cp -p --no-dereference src/.libs/libipopt.so* \
       $RPM_BUILD_ROOT%{_libdir}/
 cp -p --no-dereference contrib/sIPOPT/src/.libs/libsipopt.so* \
       $RPM_BUILD_ROOT%{_libdir}/
 cp -p --no-dereference src/ipopt.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig
%if 0%{?with_asl}
 cp -p --no-dereference src/Apps/AmplSolver/.libs/libipoptamplinterface.so* \
       $RPM_BUILD_ROOT%{_libdir}/
 cp -p --no-dereference src/Apps/AmplSolver/ipoptamplinterface.pc \
       $RPM_BUILD_ROOT%{_libdir}/pkgconfig
 cp -p --no-dereference src/Apps/AmplSolver/.libs/ipopt \
       $RPM_BUILD_ROOT%{_bindir}/
 cp -p contrib/sIPOPT/AmplSolver/ipopt_sens \
       $RPM_BUILD_ROOT%{_bindir}/
%endif

 find -O3 src \( -name \*.h -o -name \*.hpp \) -exec cp -p {} headers \;
 cp -p contrib/sIPOPT/src/*.hpp src/Common/*.h headers
cd ..

# Make man pages
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
help2man -N $RPM_BUILD_ROOT%{_bindir}/ipopt > $RPM_BUILD_ROOT%{_mandir}/man1/ipopt.1
cat > $RPM_BUILD_ROOT%{_mandir}/man1/ipopt_sens.1 << EOF
.so man1/ipopt.1
EOF

##Copy header and documentation files
install -p -m 644 Ipopt-releases-%{version}/headers/* $RPM_BUILD_ROOT%{_includedir}/coin/

# Correct config.h due to manual install (#1295290)
pushd $RPM_BUILD_ROOT%{_includedir}/coin/
    rm config.h config_default.h
    # Use the generated config_ipopt.h
    sed -i 's/\(config_ipopt\)_default\(\.h\)/\1\2/' IpoptConfig.h
popd

cp -far Ipopt-releases-%{version}/doc/{html,*.tag} $RPM_BUILD_ROOT%{_docdir}/%{name}/

#######################################################
%check
cd Ipopt-releases-%{version}
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} make test
cd ..

%if 0%{?with_openmpi}
%if 0%{?with_mpicheck}
cd %{module}-releases-openmpi
%{_openmpi_load}
LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB make test
%{_openmpi_unload}
cd ..
%endif
%endif

%if 0%{?with_mpich}
%if 0%{?with_mpichcheck}
cd %{module}-releases-mpich
# Remove unknown -Lsystem/lib flag
for i in `find . -type f \( -name "Makefile" \)`; do
 sed -e 's|-Lsystem/lib||g' -i $i
done
#
%{_mpich_load}
MPICH_INTERFACE_HOSTNAME=localhost LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB make test
%{_mpich_unload}
cd ..
%endif
%endif

%files
%if 0%{?with_asl}
%{_bindir}/ipopt
%{_bindir}/ipopt_sens
%endif
%{_libdir}/libipopt.so.3
%{_libdir}/libipopt.so.%{version}
%{_libdir}/libsipopt.so.3
%{_libdir}/libsipopt.so.%{version}
%if 0%{?with_asl}
%{_libdir}/libipoptamplinterface.so.3
%{_libdir}/libipoptamplinterface.so.%{version}
%endif
%{_mandir}/man1/ipopt.1*
%{_mandir}/man1/ipopt_sens.1*

%files  devel
%{_includedir}/coin/*
%{_libdir}/libipopt.so
%{_libdir}/libsipopt.so
%{_libdir}/pkgconfig/ipopt.pc
%if 0%{?with_asl}
%{_libdir}/libipoptamplinterface.so
%{_libdir}/pkgconfig/ipoptamplinterface.pc
%endif

#######################################################
## Install MPI version
%if 0%{?with_openmpi}

%files openmpi
%if 0%{?with_asl}
%{_binmpidir}/ipopt
%{_binmpidir}/ipopt_sens
%endif
%{_libmpidir}/libipopt.so.3
%{_libmpidir}/libipopt.so.%{version}
%{_libmpidir}/libsipopt.so.3
%{_libmpidir}/libsipopt.so.%{version}
%if 0%{?with_asl}
%{_libmpidir}/libipoptamplinterface.so.3
%{_libmpidir}/libipoptamplinterface.so.%{version}
%endif

%files openmpi-devel
%{_libmpidir}/libipopt.so
%{_libmpidir}/libsipopt.so
%if 0%{?with_asl}
%{_libmpidir}/libipoptamplinterface.so
%endif
%{_incmpidir}/*

%endif
%if 0%{?with_mpich}

%files mpich
%if 0%{?with_asl}
%{_binmpichdir}/ipopt
%{_binmpichdir}/ipopt_sens
%endif
%{_libmpichdir}/libipopt.so.3
%{_libmpichdir}/libipopt.so.%{version}
%{_libmpichdir}/libsipopt.so.3
%{_libmpichdir}/libsipopt.so.%{version}
%if 0%{?with_asl}
%{_libmpichdir}/libipoptamplinterface.so.3
%{_libmpichdir}/libipoptamplinterface.so.%{version}
%endif

%files mpich-devel
%{_libmpichdir}/libipopt.so
%{_libmpichdir}/libsipopt.so
%if 0%{?with_asl}
%{_libmpichdir}/libipoptamplinterface.so
%endif
%{_incmpichdir}/*
%endif

%files common
%license Ipopt-releases-%{version}/LICENSE
%{_docdir}/%{name}/

%changelog
%autochangelog
