# Use forge macros for pulling from GitHub
%global forgeurl https://github.com/fzenke/auryn

# Upstream only provides static libraries
# https://github.com/fzenke/auryn/issues/4

# Three flavors of the app are provided by default.
# Make sure at least one of below options is turned on or the build will
# fail (empty package).
%bcond serial 1
%bcond mpich 1
%bcond openmpi 1

%bcond tests 1

Name:           auryn
Version:        0.8.3
Release:        %autorelease
Summary:        Plastic Recurrent Network Simulator

%forgemeta

# SPDX
License:        GPL-3.0-only
URL:            http://www.fzenke.net/auryn/
Source0:        %forgesource
# Fix broken OpenMPI build.
# https://github.com/fzenke/auryn/issues/42
Patch:          remove_mpi_cxx_bindings.patch

# This used in various places and was needed before since
# upstream added an m suffix to the 0.8.2 release.
# I'll keep this for now for convenience, should we need it again.
%global _version %{version}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

%global _description %{expand:
Auryn is a source package used to create highly specialized and optimized code
to simulate recurrent spiking neural networks with spike timing dependent
plasticity (STDP).

Detailed documentation and a forum for support/discussion are available at
https://fzenke.net/auryn}

%description %_description


%if %{with serial}
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%endif


%if %{with doc}
%package        doc
Summary:        Examples for %{name}
BuildArch:      noarch

%description    doc
This package contains examples for %{name}
%endif


%if %{with mpich}
%package mpich
Summary:        %summary (MPICH)
BuildRequires:  mpich-devel
BuildRequires:  boost-mpich-devel
BuildRequires:  boost-mpich
BuildRequires:  rpm-mpi-hooks
Requires:       mpich

%description mpich
%_description


%package mpich-devel
Summary:        Development files for %{name}-mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Provides:       %{name}-mpich-static = %{version}-%{release}

%description mpich-devel
The %{name}-mpich-devel package contains libraries and header files for
developing applications that use %{name}-mpich.

%endif
# mpich


%if %{with openmpi}
%package openmpi
Summary:        %summary (OpenMPI)
BuildRequires:  openmpi-devel
BuildRequires:  boost-openmpi-devel
BuildRequires:  boost-openmpi
BuildRequires:  rpm-mpi-hooks
BuildRequires:  make
Requires:       openmpi

%description openmpi
%_description


%package openmpi-devel
Summary:        Development files for %{name}-openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Provides:       %{name}-openmpi-static = %{version}-%{release}

%description openmpi-devel
The %{name}-openmpi-devel package contains libraries and header files for
developing applications that use %{name}-openmpi.

%endif
# openmpi


%prep
%forgeautosetup -p1

# Tweaks for all versions
# Don't let it set its own optimisation flags
sed -i '/SET(CMAKE_CXX_FLAGS/ d' CMakeLists.txt
# Don't make MPI mandatory. It's not needed for the serial build.
sed -i 's/MPI REQUIRED/MPI/' CMakeLists.txt
# Modify test scripts for easier use in the sub builds
sed -i '/^BUILDDIR/ d' test/*.sh
sed -i 's|^.BUILDDIR/test/||' test/*.sh

# Need to disable vector intrinsics on these architectures
%ifarch %{arm} s390x aarch64 %{power64}
    sed -i 's|^\(#define CODE_USE_SIMD_INSTRUCTIONS_EXPLICITLY\)|//\1|' src/auryn/auryn_definitions.h
%endif

%if %{with serial}
    mkdir build-serial
%endif

%if %{with mpich}
    mkdir build-mpich
%endif

%if %{with openmpi}
    mkdir build-openmpi
%endif


%build
# https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_NO_INSTALL_PREFIX.html#variable:CMAKE_FIND_NO_INSTALL_PREFIX
%global do_cmake_config %{expand: \
echo
echo "*** BUILDING %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
%set_build_flags
pushd build$MPI_COMPILE_TYPE  &&
    cmake \\\
        -DCMAKE_FIND_NO_INSTALL_PREFIX:BOOL=TRUE \\\
        -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS -DBOOST_TIMER_ENABLE_DEPRECATED" \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_PREFIX:PATH="$MPI_HOME" \\\
        -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \\\
        -DLIB_INSTALL_DIR:PATH=%{_libdir} \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=ON \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 .. &&
%else
        -DLIB_SUFFIX="" .. &&
%endif
popd || exit -1;
}

%global do_make_build %{expand: \
    make %{?_smp_mflags} -C build$MPI_COMPILE_TYPE || exit -1
}

# Build serial version
%if %{with serial}
export MPI_COMPILE_TYPE="-serial"
export MPI_HOME=%{_prefix}
# Undefine AURYN_CODE_USE_MPI for serial build.
# See: https://www.fzenke.net/auryn/doku.php?id=manual:compileauryn
sed -i.mpi '/#define AURYN_CODE_USE_MPI/d' src/auryn/auryn_definitions.h
%{do_cmake_config}
%{do_make_build}
# Restore auryn_definitions.h
mv -v src/auryn/auryn_definitions.h.mpi src/auryn/auryn_definitions.h
# Fix install location for `libauryn.a`
sed -r -i 's|(\{CMAKE_INSTALL_PREFIX\}/lib)"|\164"|' \
    build$MPI_COMPILE_TYPE/src/cmake_install.cmake
%endif
# serial

# Build mpich version
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_cmake_config}
%{do_make_build}

%{_mpich_unload}
%endif
# mpich

# Build OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_cmake_config}
%{do_make_build}

%{_openmpi_unload}
%endif
# openmpi


%install
%global do_install %{expand:
echo
echo "*** INSTALLING %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
    make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" CPPROG="cp -p" -C build$MPI_COMPILE_TYPE || exit -1
}

%global do_rename %{expand:
echo
echo "*** RENAMING binaries for %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
    # Add suffix
    pushd $RPM_BUILD_ROOT/$MPI_BIN/
        mv -v aube{,$MPI_SUFFIX}
        mv -v aubs{,$MPI_SUFFIX}
    popd
}

# Install serial version
%if %{with serial}
export MPI_COMPILE_TYPE="-serial"
%{do_install}
%endif
# serial

# Install MPICH version
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_install}
%{do_rename}
%{_mpich_unload}
%endif
# mpich

# Install OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_install}
%{do_rename}
%{_openmpi_unload}
%endif
# openmpi

%if %{with tests}
%check
%global do_tests %{expand:
echo
echo "*** TESTING %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
    pushd build$MPI_COMPILE_TYPE/test
        ../../test/run_unit_tests.sh || exit -1
    popd
}

%if %{with serial}
export MPI_COMPILE_TYPE="-serial"
%{do_tests}
%endif
# tests

%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_tests}
%endif
# mpich

%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_tests}
%endif
# openmpi

%endif
# tests


%if %{with doc}
%files doc
%license COPYING
%doc README.* AUTHORS
%doc examples/
%endif
# doc

%if %{with serial}
%files
%license COPYING
%doc README.* AUTHORS
%{_bindir}/aube
%{_bindir}/aubs

%files devel
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/libauryn.a
%endif
# serial

%if %{with mpich}
%files mpich
%license COPYING
%doc README.* AUTHORS
%{_libdir}/mpich/bin/aube_mpich
%{_libdir}/mpich/bin/aubs_mpich

%files mpich-devel
%{_libdir}/mpich/include/%{name}
%{_libdir}/mpich/include/%{name}.h
%{_libdir}/mpich/lib/libauryn.a
%endif
# mpich

%if %{with openmpi}
%files openmpi
%license COPYING
%doc README.* AUTHORS
%{_libdir}/openmpi/bin/aube_openmpi
%{_libdir}/openmpi/bin/aubs_openmpi

%files openmpi-devel
%{_libdir}/openmpi/include/%{name}
%{_libdir}/openmpi/include/%{name}.h
%{_libdir}/openmpi/lib/libauryn.a
%endif
# openmpi


%changelog
%autochangelog
