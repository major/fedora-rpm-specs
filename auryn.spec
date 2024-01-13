# Upstream only provides static libraries
# https://github.com/fzenke/auryn/issues/4

# Switch them off if you want
# Best to start with the serial version
%bcond_without mpich
%bcond_without openmpi

%bcond_without doc
# Doxygen crashes on aarch64. Temporarily disabling dev docs
%bcond_with dev_doc

%bcond_without tests

Name:           auryn
Version:        0.8.2
Release:        %autorelease
Summary:        Plastic Recurrent Network Simulator

License:        GPLv3
URL:            http://www.fzenke.net/auryn/
Source0:        https://github.com/fzenke/%{name}/archive/v%{version}m/%{name}-%{version}.tar.gz

# Upstream added an m prefix to the directory structure for some reason
%global _version %{version}m

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Auryn is a source package used to create highly specialized and optimized code
to simulate recurrent spiking neural networks with spike timing dependent
plasticity (STDP)

Detailed documentation and a forum for support/discussion are available at
https://fzenke.net/auryn.

%if %{with doc}
%package        doc
Summary:        Documentation for %{name}
BuildRequires:  doxygen
BuildRequires:  /usr/bin/dot
BuildArch:      noarch


%description    doc
This package contains the doxygen generated documentation for %{name}
%endif


%if %{with mpich}
%package mpich
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  boost-mpich-devel
BuildRequires:  boost-mpich
BuildRequires:  rpm-mpi-hooks
Requires:       mpich

%description mpich
%{description}

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
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  boost-openmpi-devel
BuildRequires:  boost-openmpi
BuildRequires:  rpm-mpi-hooks
BuildRequires:  make
Requires:       openmpi

%description openmpi
%{description}

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
%autosetup -c -n %{name}-%{_version}

# Tweaks for all versions
pushd %{name}-%{_version}
    # Don't let it set its own optimisation flags
    sed -i '/SET(CMAKE_CXX_FLAGS/ d' CMakeLists.txt
    sed -i '/^BUILDDIR/ d' test/*.sh
    sed -i 's|^.BUILDDIR/test/||' test/*.sh

# Need to disable vector intrinsics on these architectures
%ifarch %{arm} s390x aarch64 %{power64}
    sed -i 's|^\(#define CODE_USE_SIMD_INSTRUCTIONS_EXPLICITLY\)|//\1|' src/auryn/auryn_definitions.h
%endif
popd

%if %{with mpich}
    cp -a %{name}-%{_version} %{name}-%{_version}-mpich
%endif
# mpich

%if %{with openmpi}
    cp -a %{name}-%{_version} %{name}-%{_version}-openmpi
%endif
# openmpi


%build
# https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_NO_INSTALL_PREFIX.html#variable:CMAKE_FIND_NO_INSTALL_PREFIX
%global do_cmake_config %{expand: \
echo
echo "*** BUILDING %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
%set_build_flags
pushd %{name}-%{_version}$MPI_COMPILE_TYPE  &&
    cmake . \\\
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
        -DLIB_SUFFIX=64 &&
%else
        -DLIB_SUFFIX="" &&
%endif
popd || exit -1;
}

%global do_make_build %{expand: \
    make %{?_smp_mflags} -C %{name}-%{_version}$MPI_COMPILE_TYPE || exit -1
}


%if %{with dev_doc}
# Does not permit non MPI versions
# Only build docs
pushd %{name}-%{_version}/doc
    doxygen Doxyfile
popd
%endif

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
    make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" CPPROG="cp -p" -C %{name}-%{_version}$MPI_COMPILE_TYPE || exit -1

    # Add suffix
    pushd $RPM_BUILD_ROOT/$MPI_BIN/
        mv -v aube{,$MPI_SUFFIX}
        mv -v aubs{,$MPI_SUFFIX}
    popd
}

# No serial version, skip

# Install MPICH version
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_install}

%{_mpich_unload}
%endif
# mpich

# Install OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_install}

%{_openmpi_unload}
%endif
# openmpi

%if %{with tests}
%check
%global do_tests %{expand:
echo
echo "*** TESTING %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
    pushd %{name}-%{_version}$MPI_COMPILE_TYPE/test
        ./run_unit_tests.sh || exit -1
    popd
}

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
%license %{name}-%{_version}/COPYING
%doc %{name}-%{_version}/AUTHORS
%doc %{name}-%{_version}/README.md
%doc %{name}-%{_version}/examples/
%if %{with dev_doc}
%doc %{name}-%{_version}/doc/html/
%endif
# dev_doc
%endif
# doc

%if %{with mpich}
%files mpich
%license %{name}-%{_version}/COPYING
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
%license %{name}-%{_version}/COPYING
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
