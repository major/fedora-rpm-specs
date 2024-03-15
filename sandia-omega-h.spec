%global forgeurl https://github.com/sandialabs/omega_h

%global soversion 9

# Build with MPI for parallelism
%bcond mpich 1
%bcond openmpi 1

# Build with OpenMP
# Disabled because tests take very long, some timeout, one fails
%bcond openmp 0

# Build examples
# Examples are arch specific. Installing them in %%doc causes rpmlint
# errors 'arch-dependent-file-in-usr-share' and 'binary-or-shlib-defines-rpath'.
%bcond examples 0

# Build and run tests
%bcond tests 1

# Use Omega_h_THROW
%bcond throw 0

Name:           sandia-omega-h
# Note: On GitHub there's also tag 10.1.0. But it predates 9.34.13.
Version:        9.34.13
Release:        %{autorelease}
Summary:        Reliable mesh adaptation
%global tag v%{version}
%forgemeta
# Various files carry their own license header
# src/Omega_h_any.hpp - BSL-1.0
# src/Omega_h_hilbert.hpp - LicenseRef-Fedora-Public-Domain
# src/Omega_h_rbtree.hpp - MIT
# src/r3d.hpp - LicenseRef-Fedora-Public-Domain
# tpl/pss/* - BSD-3-Clause
License:        BSD-2-Clause AND BSL-1.0 AND LicenseRef-Fedora-Public-Domain AND MIT AND BSD-3-Clause
URL:            https://sandialabs.github.io/repo/#/sandialabs/omega_h
Source:         %forgesource
# Make sure shared objects carry version info and are installed in the
# arch specific directory (%%{_libdir})
# Also make sure `-fopenmp` is passed to the linker as well
# Inspired by https://github.com/sandialabs/omega_h/issues/332#issuecomment-564100525
Patch:          build_flags_and_so_version.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Also exclude s390x since tests are failing on that arch
# https://bugzilla.redhat.com/show_bug.cgi?id=2269344
ExcludeArch:    %{ix86} s390x

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  Random123-devel
# For generating man pages
BuildRequires:  help2man

%global _description %{expand:
Omega_h is a C++14 library that implements tetrahedron and triangle
mesh adaptativity, with a focus on scalable HPC performance using
(optionally) MPI and OpenMP or CUDA. It is intended to provided
adaptive functionality to existing simulation codes. Mesh adaptivity
allows one to minimize both discretization error and number of degrees
of freedom live during the simulation, as well as enabling moving
object and evolving geometry simulations. Omega_h will do this for you
in a way that is fast, memory-efficient, and portable across many
different architectures.}

%description %_description

%global _summary %{summary}
%global _summary_devel %{summary} (devel package)


%package devel
Summary:        %{_summary_devel}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%global _description_devel %{expand:
Omega_h header files and libraries needed for programs that use the
omega_h library.}

%description devel %_description_devel


%if %{with examples}
%package doc
Summary:        Examples for %{name}
BuildRequires:  gmsh

%global _description_doc %{expand:
Examples for using the Omega_h library.}

%description doc %_description_doc
%endif


%if %{with mpich}

%package mpich
Summary:        %{_summary} (MPICH build)
BuildRequires:  mpich-devel

Requires:       mpich

%description mpich %_description


%package mpich-devel
Summary:        %{_summary_devel} (MPICH)
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:       mpich-devel

%description mpich-devel %_description_devel


%if %{with examples}
%package mpich-doc
Summary:        Examples for %{name}-mpich
BuildRequires:  gmsh-mpich

%description mpich-doc %_description_doc
%endif

%endif


%if %{with openmpi}

%package openmpi
Summary:        %{_summary} (OpenMPI build)
BuildRequires:  openmpi-devel

Requires:       openmpi

%description openmpi %_description


%package openmpi-devel
Summary:        %{_summary_devel} (OpenMPI)
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:       openmpi-devel

%description openmpi-devel %_description_devel


%if %{with examples}
%package openmpi-doc
Summary:        Examples for %{name}-openmpi
BuildRequires:  gmsh-openmpi

%description openmpi-doc %_description_doc
%endif

%endif


%prep
%forgeautosetup -p1

# Remove bundled Random123 and fix header file
rm -rvf tpl/random123
sed -i 's/random123/Random123/' src/Omega_h_random_inline.hpp

%if %{with mpich}
  mkdir build-mpich
%endif

%if %{with openmpi}
  mkdir build-openmpi
%endif


%build
# Shamelessly copied from `arbor`
#
# Best to use && so that if anything in the chain fails, the build also fails
# straight away
%global do_cmake_config %{expand: \
echo
echo "*** BUILDING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
echo "MPI_HOME: ${MPI_HOME}"
echo "MPI_INCLUDE: ${MPI_INCLUDE}"
echo "MPI_LIB: ${MPI_LIB}"
echo
pushd build$MPI_COMPILE_TYPE  &&
    cmake \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DINCLUDE_INSTALL_DIR:PATH=$MPI_INCLUDE \\\
        -DLIB_INSTALL_DIR:PATH=$MPI_LIB \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=OFF \\\
        -DCMAKE_BUILD_TYPE:STRING="Release" \\\
        -DLIB_SUFFIX="" \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
%if %{with openmp}
        -DOmega_h_USE_OpenMP:BOOL=ON \\\
%endif
%if %{with examples}
        -DOmega_h_EXAMPLES:BOOL=ON \\\
%endif
        -DOmega_h_USE_MPI:BOOL=ON \\\
        -DTPL_ENABLE_MPI:BOOL=ON \\\
%if %{with tests}
        -DBUILD_TESTING:BOOL=ON \\\
%endif
%if %{with throw}
        -DOmega_h_THROW:BOOL=ON \\\
%endif
        -B . -S .. &&
popd || exit -1;
}

%global do_make_build %{expand: \
    %make_build -C build$MPI_COMPILE_TYPE || exit -1
}

# Standard build without options
%cmake \
%if %{with openmp}
    -DOmega_h_USE_OpenMP:BOOL=ON \
%endif
%if %{with examples}
    -DOmega_h_EXAMPLES:BOOL=ON \
%endif
%if %{with tests}
        -DBUILD_TESTING:BOOL=ON \\\
%endif
%if %{with throw}
    -DOmega_h_THROW:BOOL=ON \
%endif
    -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build

# Build for MPICH
%if %{with mpich}
%{_mpich_load}
%set_build_flags
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
export MPI_COMPILE_TYPE="-mpich"
%{do_cmake_config}
%{do_make_build}
%{_mpich_unload}
%endif

# Build for OpenMPI
%if %{with openmpi}
%{_openmpi_load}
%set_build_flags
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
export MPI_COMPILE_TYPE="-openmpi"
%{do_cmake_config}
%{do_make_build}
%{_openmpi_unload}
%endif


%install
# Install everything
%global do_install %{expand: \
echo
echo "*** INSTALLING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
    %make_install -C build$MPI_COMPILE_TYPE || exit -1
    # Add required suffix to binaries
echo "*** Adding '${MPI_SUFFIX}' to binaries ***"
echo
    pushd $RPM_BUILD_ROOT/$MPI_BIN
        mv -v ascii_vtk2osh{,$MPI_SUFFIX}
        mv -v msh2osh{,$MPI_SUFFIX}
        mv -v osh2vtk{,$MPI_SUFFIX}
        mv -v osh_adapt{,$MPI_SUFFIX}
        mv -v osh_box{,$MPI_SUFFIX}
        mv -v osh_calc{,$MPI_SUFFIX}
        mv -v osh_eval_implied{,$MPI_SUFFIX}
        mv -v osh_filesystem{,$MPI_SUFFIX}
        mv -v osh_fix{,$MPI_SUFFIX}
        mv -v osh_part{,$MPI_SUFFIX}
        mv -v osh_reorder{,$MPI_SUFFIX}
        mv -v osh_scale{,$MPI_SUFFIX}
        mv -v oshdiff{,$MPI_SUFFIX}
        mv -v vtkdiff{,$MPI_SUFFIX}
    popd
}

# Install standard version
%cmake_install

# Generate man pages
mkdir man
mkdir -p %{buildroot}%{_mandir}/man1
export PATH="${PATH}:%{buildroot}%{_bindir}"
for BIN in $(find %{buildroot}%{_bindir} -type f -name osh_\* -printf '%%P ' -o -name \*diff -printf '%%P '); do
  if [ "${BIN}" = "osh_calc" ]; then continue; fi
  LD_LIBRARY_PATH="${LD_LIBRARY_PATH-}${LD_LIBRARY_PATH+:}%{buildroot}%{_libdir}" \
  help2man --section 1 --no-discard-stderr --no-info --name ${BIN}\
  --output man/${BIN}.1 ${BIN}
  install -m 0644 man/${BIN}.1 %{buildroot}%{_mandir}/man1
done

# Install MPICH version
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_install}
%{_mpich_unload}
%endif

# Install OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_install}
%{_openmpi_unload}
%endif


%if %{with tests}
%check

%global do_check %{expand: \
echo
echo "*** TESTING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
echo "*** MPI_LIB: ${MPI_LIB} ***"
echo
ctest \\\
    --test-dir build$MPI_COMPILE_TYPE \\\
    --output-on-failure --force-new-ctest-process \\\
    -j 2 --verbose --rerun-failed
}

%ctest --verbose --rerun-failed

%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_check}
%{_mpich_unload}
%endif

%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_check}
%{_openmpi_unload}
%endif

%endif


%files
%doc README.*
%license LICENSE
%{_bindir}/ascii_vtk2osh
%{_bindir}/msh2osh
%{_bindir}/osh2vtk
%{_bindir}/osh_adapt
%{_bindir}/osh_box
%{_bindir}/osh_calc
%{_bindir}/osh_eval_implied
%{_bindir}/osh_filesystem
%{_bindir}/osh_fix
%{_bindir}/osh_part
%{_bindir}/osh_reorder
%{_bindir}/osh_scale
%{_bindir}/oshdiff
%{_bindir}/vtkdiff
%{_libdir}/libomega_h.so.%{soversion}
%{_libdir}/libomega_h.so.%{version}
%{_mandir}/man1/*.1*


%files devel
%{_includedir}/Omega_h*
%{_includedir}/r3d.hpp
%{_libdir}/cmake/Omega_h
%{_libdir}/libomega_h.so


%if %{with examples}
%files doc
%doc redhat-linux-build/example
%license LICENSE
%endif


%if %{with mpich}

%files mpich
%doc README.*
%license LICENSE
%{_libdir}/mpich/bin/ascii_vtk2osh_mpich
%{_libdir}/mpich/bin/msh2osh_mpich
%{_libdir}/mpich/bin/osh2vtk_mpich
%{_libdir}/mpich/bin/osh_adapt_mpich
%{_libdir}/mpich/bin/osh_box_mpich
%{_libdir}/mpich/bin/osh_calc_mpich
%{_libdir}/mpich/bin/osh_eval_implied_mpich
%{_libdir}/mpich/bin/osh_filesystem_mpich
%{_libdir}/mpich/bin/osh_fix_mpich
%{_libdir}/mpich/bin/osh_part_mpich
%{_libdir}/mpich/bin/osh_reorder_mpich
%{_libdir}/mpich/bin/osh_scale_mpich
%{_libdir}/mpich/bin/oshdiff_mpich
%{_libdir}/mpich/bin/vtkdiff_mpich
%{_libdir}/mpich/lib/libomega_h.so.%{soversion}
%{_libdir}/mpich/lib/libomega_h.so.%{version}


%files mpich-devel
%{_libdir}/mpich/include/Omega_h*
%{_libdir}/mpich/include/r3d.hpp
%{_libdir}/mpich/lib/cmake/Omega_h
%{_libdir}/mpich/lib/libomega_h.so


%if %{with examples}
%files mpich-doc
%doc build-mpich/example
%license LICENSE
%endif

%endif


%if %{with openmpi}

%files openmpi
%doc README.*
%license LICENSE
%{_libdir}/openmpi/bin/ascii_vtk2osh_openmpi
%{_libdir}/openmpi/bin/msh2osh_openmpi
%{_libdir}/openmpi/bin/osh2vtk_openmpi
%{_libdir}/openmpi/bin/osh_adapt_openmpi
%{_libdir}/openmpi/bin/osh_box_openmpi
%{_libdir}/openmpi/bin/osh_calc_openmpi
%{_libdir}/openmpi/bin/osh_eval_implied_openmpi
%{_libdir}/openmpi/bin/osh_filesystem_openmpi
%{_libdir}/openmpi/bin/osh_fix_openmpi
%{_libdir}/openmpi/bin/osh_part_openmpi
%{_libdir}/openmpi/bin/osh_reorder_openmpi
%{_libdir}/openmpi/bin/osh_scale_openmpi
%{_libdir}/openmpi/bin/oshdiff_openmpi
%{_libdir}/openmpi/bin/vtkdiff_openmpi
%{_libdir}/openmpi/lib/libomega_h.so.%{soversion}
%{_libdir}/openmpi/lib/libomega_h.so.%{version}


%files openmpi-devel
%{_libdir}/openmpi/include/Omega_h*
%{_libdir}/openmpi/include/r3d.hpp
%{_libdir}/openmpi/lib/cmake/Omega_h
%{_libdir}/openmpi/lib/libomega_h.so


%if %{with examples}
%files openmpi-doc
%doc build-openmpi/example
%license LICENSE
%endif

%endif


%changelog
%autochangelog
