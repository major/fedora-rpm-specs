Name:           bout++
Version:        5.2.0
Release:        %autorelease
Summary:        Library for the BOUndary Turbulence simulation framework

# BOUT++ itself is LGPL, but we are linking with GPLed code, so the distributed library is GPL
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://boutproject.github.io/
Source0:        https://github.com/boutproject/BOUT-dev/releases/download/v%{version}/BOUT++-v%{version}.tar.gz

Patch:          https://github.com/boutproject/BOUT-dev/pull/3188.patch
# https://github.com/boutproject/BOUT-dev/commit/7d8418e
Patch:          bout++-expose-std-erase.patch
Patch:          bout++-fmt12-runtime.patch
# https://github.com/boutproject/BOUT-dev/commit/27d5c932b6cc
Patch:          bout++-fake-mesh-accumulate.patch

Patch:          test-timeout.patch
# Allow installing the docs from top-level build directory
Patch:          https://github.com/boutproject/BOUT-dev/pull/3111.patch

Patch:          bout++-no-make-bash.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%bcond_without flexiblas
%bcond_without manual
%bcond_without test
%bcond_without sundials
%bcond_without petsc
%bcond_with 3dmetrics

# Enable both mpi every where
%bcond_without mpich
%bcond_without openmpi

# Use system mpark
%bcond_without system_mpark

#
#           DEPENDENCIES
#

BuildRequires:  m4
BuildRequires:  zlib-devel
BuildRequires:  cmake
BuildRequires:  gettext-devel
BuildRequires:  environment-modules
BuildRequires:  netcdf-devel
BuildRequires:  netcdf-cxx%{?fedora:4}-devel
BuildRequires:  hdf5-devel
BuildRequires:  fftw-devel
BuildRequires:  fmt-devel
BuildRequires:  chrpath
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-cython
BuildRequires:  python%{python3_pkgversion}-netcdf4
BuildRequires:  python%{python3_pkgversion}-scipy
BuildRequires:  python%{python3_pkgversion}-boututils
BuildRequires:  python%{python3_pkgversion}-boutdata
BuildRequires:  python%{python3_pkgversion}-zoidberg
BuildRequires:  python%{python3_pkgversion}-tables
%if %{with flexiblas}
BuildRequires:  flexiblas-devel
%else
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
%endif
BuildRequires:  gcc-c++
%if %{with system_mpark}
BuildRequires:  mpark-variant-devel
%endif
# cxx generation
BuildRequires:  python%{python3_pkgversion}-jinja2
# Documentation
%if %{with manual}
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
%endif
%if %{with petsc} && %{with mpich}
BuildRequires: petsc-mpich-devel
BuildRequires: hdf5-mpich-devel
%endif
%if %{with petsc} && %{with openmpi}
BuildRequires: petsc-openmpi-devel
BuildRequires: hdf5-openmpi-devel
%endif
%if %{with sundials} && %{with mpich}
BuildRequires: sundials-mpich-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1839131
BuildRequires: sundials-devel
%endif
%if %{with sundials} && %{with openmpi}
BuildRequires: sundials-openmpi-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1839131
BuildRequires: sundials-devel
%endif

#
#           DESCRIPTIONS
#


%if %{with mpich}
BuildRequires:  mpich-devel
%global mpi_list mpich
%endif
%if %{with openmpi}
BuildRequires:  openmpi-devel
%global mpi_list openmpi %{?mpi_list}
%endif

%description
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.



%if %{with mpich}
%package mpich
Summary: BOUT++ mpich libraries
Requires: %{name}-common = %{version}-%{release}
# Use bundled version, to reproduce upstream results
Provides: bundled(libpvode)
Recommends: environment-modules
Recommends: python%{python3_pkgversion}-boututils
Recommends: python%{python3_pkgversion}-boutdata
Recommends: python%{python3_pkgversion}-xbout

%package mpich-devel
Summary: BOUT++ mpich libraries
Requires:  %{name}-mpich = %{version}-%{release}
Recommends:  gcc-c++
Recommends:  mpich-devel
Recommends:  zlib-devel
Recommends:  gettext-devel
Recommends:  netcdf-devel
Recommends:  netcdf-cxx%{?fedora:4}-devel
Recommends:  hdf5-devel
Recommends:  fftw-devel
%if %{with flexiblas}
Recommends:  flexiblas-devel
%else
Recommends:  blas-devel
Recommends:  lapack-devel
%endif
%if %{with system_mpark}
Recommends:  mpark-variant-devel
%endif
%if %{with petsc}
Recommends:  petsc-mpich-devel
Recommends:  hdf5-mpich-devel
%endif
%if %{with sundials}
Recommends:  sundials-mpich-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1839131
Recommends:  sundials-devel
%endif


%description mpich-devel
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This BOUT++ library is build for mpich.

%description mpich
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This BOUT++ library is build for mpich.

%package -n python%{python3_pkgversion}-%{name}-mpich
Summary:  BOUT++ mpich library for python%{python3_pkgversion}
Requires: %{name}-mpich
Requires: python%{python3_pkgversion}-%{name}
BuildRequires: python%{python3_pkgversion}-devel
Requires: mpich
Requires: python%{python3_pkgversion}-mpich
Requires: python%{python3_pkgversion}-numpy
Requires: python%{python3_pkgversion}-boututils
Requires: python%{python3_pkgversion}-boutdata
Recommends: python%{python3_pkgversion}-xbout

%py_provides python%{python3_pkgversion}-%{name}-mpich
%description  -n python%{python3_pkgversion}-%{name}-mpich
This is the BOUT++ library python%{python3_pkgversion} with mpich.

%endif




%if %{with openmpi}
%package openmpi
Summary: BOUT++ openmpi libraries
# Use bundled version, to reproduce upstream results
Provides: bundled(libpvode)
Requires: %{name}-common = %{version}-%{release}
Recommends: environment-modules
Recommends: python%{python3_pkgversion}-boututils
Recommends: python%{python3_pkgversion}-boutdata
Recommends: python%{python3_pkgversion}-xbout

%package openmpi-devel
Summary: BOUT++ openmpi libraries
Requires: %{name}-openmpi = %{version}-%{release}
Recommends:  gcc-c++
Recommends:  openmpi-devel
Recommends:  zlib-devel
Recommends:  gettext-devel
Recommends:  netcdf-devel
Recommends:  netcdf-cxx%{?fedora:4}-devel
Recommends:  hdf5-devel
Recommends:  fftw-devel
%if %{with flexiblas}
Recommends:  flexiblas-devel
%else
Recommends:  blas-devel
Recommends:  lapack-devel
%endif
%if %{with system_mpark}
Recommends:  mpark-variant-devel
%endif
%if %{with petsc}
Recommends:  petsc-openmpi-devel
Recommends:  hdf5-openmpi-devel
%endif
%if %{with sundials}
Recommends:  sundials-openmpi-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1839131
Recommends:  sundials-devel
%endif



%description openmpi-devel
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This BOUT++ library is build for openmpi and provides the required
header files.

%description openmpi
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This BOUT++ library is build for openmpi.

%package -n python%{python3_pkgversion}-%{name}-openmpi
Summary:  BOUT++ openmpi library for python%{python3_pkgversion}
Requires: %{name}-openmpi
Requires: python%{python3_pkgversion}-%{name}
BuildRequires: python%{python3_pkgversion}-devel
Requires: openmpi
Requires: python%{python3_pkgversion}-openmpi
Requires: python%{python3_pkgversion}-numpy
Requires: python%{python3_pkgversion}-boututils
Requires: python%{python3_pkgversion}-boutdata
Recommends: python%{python3_pkgversion}-xbout

%py_provides python%{python3_pkgversion}-%{name}-openmpi

%description  -n python%{python3_pkgversion}-%{name}-openmpi
This is the BOUT++ library python%{python3_pkgversion} with openmpi.

%endif


%package common
Summary: Common files for BOUT++
%description common
MPI-independent files for BOUT++, namely localisation files.

%package -n python%{python3_pkgversion}-%{name}
Summary: BOUT++ python library
Requires:   python%{python3_pkgversion}-netcdf4
Requires:   python%{python3_pkgversion}-numpy
Recommends: python%{python3_pkgversion}-scipy
Recommends: python%{python3_pkgversion}-matplotlib
Recommends: python%{python3_pkgversion}-boututils
Recommends: python%{python3_pkgversion}-boutdata

BuildArch: noarch
%py_provides python%{python3_pkgversion}-%{name}

%description -n python%{python3_pkgversion}-%{name}
Python%{python3_pkgversion} library for pre and post processing of BOUT++ data




%if %{with manual}
%package -n %{name}-doc
Summary: BOUT++ Documentation
BuildArch: noarch

%description -n %{name}-doc
BOUT++ is a framework for writing fluid and plasma simulations in
curvilinear geometry. It is intended to be quite modular, with a
variety of numerical methods and time-integration solvers available.
BOUT++ is primarily designed and tested with reduced plasma fluid
models in mind, but it can evolve any number of equations, with
equations appearing in a readable form.

This package contains the documentation.
%endif

#
#           PREP
#

%prep
%autosetup -n BOUT++-v%{version} -p1

# Switch to standard theme
# sphinx_book_theme is not packaged
sed -e 's/html_theme = "sphinx_book_theme"/html_theme = "sphinxdoc"/' -i manual/sphinx/conf.py

%if %{with system_mpark}
# use mpark provided by fedora
rm -rf externalpackages/mpark.variant/
mkdir -p externalpackages/mpark.variant/include/
%endif

rm -rf tools/pylib/boutdata
rm -rf tools/pylib/boututils

# Remove shebang
for f in $(find -L tools/pylib/ -type f | grep -v _boutcore_build )
do
    sed -i '/^#!\//d' $f
done

sed -e '32,35d' -i tests/integrated/test-petsc_laplace_MAST-grid/runtest
sed -e 's/build_and_log, //' -e 's/, build_and_log//' -e '/ import build_and_log$/d' -e 's/^\(.*\)build_and_log(.*/\1pass/' -i $(find tests -name runtest -type f)

# Increase timeout for copr / s390x
sed -e 's/ 3s / 30s /' -i tests/integrated/test-coordinates-initialization/runtest


# $MPI_SUFFIX will be evaluated in the loops below, set by mpi modules
%global _vpath_builddir %{_target_platform}${MPI_SUFFIX:-_serial}


#
#           BUILD
#

%build

for mpi in %{mpi_list}
do
  if [ $mpi = mpich ] ; then
      %_mpich_load
  elif [ $mpi = openmpi ] ; then
      %_openmpi_load
  else
      echo "unknown mpi" &> /dev/stderr
      exit 1
  fi

  %cmake \
      -DCMAKE_INSTALL_PREFIX:PATH=${MPI_HOME} \
      -DCMAKE_INSTALL_LIBDIR:PATH=lib \
      -DCMAKE_INSTALL_INCLUDEDIR:PATH=${MPI_INCLUDE}/bout++/ \
      -DCMAKE_INSTALL_PYTHON_SITEARCH:PATH=${MPI_PYTHON3_SITEARCH} \
      -DCMAKE_INSTALL_DATAROOTDIR:PATH=%{_datadir} \
      -DBOUT_ENABLE_MPI:BOOL=ON \
      -DBOUT_USE_FFTW=ON \
      -DBOUT_USE_NETCDF=ON \
      -DBOUT_USE_SCOREP=OFF \
      -DBOUT_USE_SYSTEM_MPARK_VARIANT=ON \
      -DBOUT_USE_LAPACK=ON \
      -DBOUT_USE_NLS=ON \
      -DBOUT_USE_SYSTEM_FMT=ON \
      -DBOUT_USE_UUID_SYSTEM_GENERATOR=ON \
      -DBOUT_TEST_TIMEOUT=1800 \
%if %{with 3dmetrics}
      -DBOUT_ENABLE_METRIC_3D=ON \
%endif
%if %{with manual}
      -DBOUT_BUILD_DOCS=ON \
%endif
%if %{with petsc}
      -DBOUT_USE_PETSC=ON \
%endif
%if %{with sundials}
      -DBOUT_USE_SUNDIALS=ON \
%endif

      %cmake_build

%if %{with test}
      %cmake_build -t build-check
%endif

  if [ $mpi = mpich ] ; then
      %_mpich_unload
  elif [ $mpi = openmpi ] ; then
      %_openmpi_unload
  fi
done

# Build the documentaion
%if %{with manual}
pushd manual
# By default they are preferring the sphinx-build-3 which seems to be broken
make sphinx-build=sphinx-build
popd
%endif

#
#           INSTALL
#

%install

for mpi in %{mpi_list}
do
  if [ $mpi = mpich ] ; then
      %_mpich_load
  else
      %_openmpi_load
  fi
  %cmake_install

  for f in $(find ${RPM_BUILD_ROOT}/${MPI_LIB} ${RPM_BUILD_ROOT}/${MPI_PYTHON3_SITEARCH} | grep -E '/libbout|/libpvode|/libpvpre') ; do
    chrpath -r $MPI_LIB $f
  done

  rm -rf  ${RPM_BUILD_ROOT}/usr/share/bout++

  mkdir -p ${RPM_BUILD_ROOT}/usr/share/modulefiles/bout++
  cat > ${RPM_BUILD_ROOT}/usr/share/modulefiles/bout++/$MPI_COMPILER <<EOF
#%Module 1.0
#
#  BOUT++ module for use with 'environment-modules' package
#  Created by bout-add-mod-path v0.9
# Only allow one bout++ module to be loaded at a time
conflict bout++
# Require mpi
prereq mpi/$MPI_COMPILER

setenv    BOUT_TOP   $MPI_INCLUDE/bout++/
EOF

  if [ $mpi = mpich ] ; then
      %_mpich_unload
  else
      %_openmpi_unload
  fi
done

# Install the documentation
%if %{with manual}
pushd manual/html
# Copy all non-hidden files/folders
find ./ -type f -not -path '*/.*' -not -path '.*/' -exec install -D "{}" "%{buildroot}%{_docdir}/bout++/{}" \;
popd
%endif


%find_lang libbout

#
#           CHECK
#

%check

# Ignore errors on some architectures
# s390x: https://bugzilla.redhat.com/show_bug.cgi?id=1998838
# s390x: https://bugzilla.redhat.com/show_bug.cgi?id=2259532
# All architectures: https://github.com/boutproject/BOUT-dev/issues/3041

%if %{with test}
for mpi in %{mpi_list}
do
    fail=1
    if [ $mpi = mpich ] ; then
        %_mpich_load
	%ifarch s390x
	fail=0
        # The following tests appear to completely hang with no timeout
        exclude_arch="-E test-invertable-operator|test-laplacexy-fv|test-laplacexy-short|test-laplacexz|test-petsc-laplace|test-multigrid-laplace"
	%endif
    else
        %_openmpi_load
    fi

    export OMPI_MCA_rmaps_base_oversubscribe=yes
    export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
    # Allow OpenMPI to run as root inside mock/container builds
    export OMPI_ALLOW_RUN_AS_ROOT=1
    export OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1
    # Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1997717
    export HDF5_USE_FILE_LOCKING=FALSE

    SEGFAULT_SIGNALS="segv" %ctest -R serial_tests || $(exit $fail)
    SEGFAULT_SIGNALS="segv" %ctest -R "MMS-" || $(exit $fail)
    SEGFAULT_SIGNALS="segv" %ctest -R "test-" $exclude_arch || $(exit $fail)

    if [ $mpi = mpich ] ; then
        %_mpich_unload
    else
        %_openmpi_unload
    fi
done
%endif

#
#           FILES SECTION
#

%if %{with mpich}
%files mpich
%{_libdir}/mpich/lib/libbout++.so.5.2.0
%{_libdir}/mpich/lib/*.so.1.0.0
%{_libdir}/mpich/bin/*
%doc README.md
%doc CITATION.bib
%doc CITATION.cff
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%license LICENSE.GPL
/usr/share/modulefiles/bout++/mpich-*

%files mpich-devel
%{_includedir}/mpich-%{_arch}/bout++
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/cmake/*

%files -n python%{python3_pkgversion}-%{name}-mpich
%{python3_sitearch}/mpich/*
%endif


%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/lib/libbout++.so.5.2.0
%{_libdir}/openmpi/lib/*.so.1.0.0
%{_libdir}/openmpi/bin/*
%doc README.md
%doc CITATION.bib
%doc CITATION.cff
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%license LICENSE.GPL
/usr/share/modulefiles/bout++/openmpi-*

%files openmpi-devel
%{_includedir}/openmpi-%{_arch}/bout++
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/cmake/*

%files -n python%{python3_pkgversion}-%{name}-openmpi
%{python3_sitearch}/openmpi/*
%endif

%files common -f libbout.lang
%dir /usr/share/modulefiles/bout++/

%files -n python%{python3_pkgversion}-%{name}
%doc README.md
%doc CITATION.bib
%doc CITATION.cff
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%license LICENSE.GPL


%if %{with manual}
%files -n %{name}-doc
%doc  %{_docdir}/bout++/
%endif

#
#           CHANGELOG
#

%changelog
%autochangelog
