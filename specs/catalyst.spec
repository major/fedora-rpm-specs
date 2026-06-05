%bcond doc              1
%bcond fortran          1
%bcond mpich            1
%ifnarch %{ix86}
%bcond openmpi          1
%else
%bcond openmpi          0
%endif
%bcond python           1

%bcond bundle_conduit   1

Name:           catalyst
Version:        2.1.0
Release:        3%{?dist}
Summary:        API specification for simulations to analyze and visualize data in situ

%global         forgeurl https://gitlab.kitware.com/paraview/%{name}
%global         tag v%{version}
%forgemeta

# catalyst and conduit are licensed under the BSD 3-Clause license except:
# Apache-2.0
#   thirdparty/update-common.sh
# MIT
#   thirdparty/conduit/fmt
#   thirdparty/conduit/libyaml
#   thirdparty/conduit/yyjson
# MIT and JSON
#   thirdparty/conduit/rapidjson
# LicenseRef-Fedora-Public-Domain
#   thirdparty/conduit/libb64
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}
# Unbundling
Patch0:         catalyst-unbundle.patch
# Ignore global debug symbols in ABI tests
Patch1:         catalyst-test-abi_tests-ignore-debug-symbols.patch
# Limit maximum number of MPI ranks for tests
Patch2:         catalyst-test-mpi-high_num_ranks.patch
# Handle missing mpi4py for mpich tests on %%{ix86}
Patch3:         catalyst-test-mpi-mpi4py.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
%if %{with bundle_conduit}
BuildRequires:  fmt-devel
BuildRequires:  libb64-devel
BuildRequires:  libyaml-devel
BuildRequires:  rapidjson-devel
BuildRequires:  yyjson-devel
%endif

%if %{with fortran}
BuildRequires:  gcc-gfortran
%endif

%if %{with python} || %{with doc}
BuildRequires:  python3-devel
%endif
%if %{with python}
BuildRequires:  chrpath
BuildRequires:  python3dist(numpy)
%endif

%if %{with doc}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

%if %{with mpich}
BuildRequires:  mpich-devel
%if %{with python}
%ifnarch %{ix86}
BuildRequires:  python3-mpi4py-mpich
%endif
%endif
%endif
%if %{with openmpi}
BuildRequires:  openmpi-devel
%if %{with python}
BuildRequires:  python3-mpi4py-openmpi
%endif
%endif

%global mpi_list %{nil}
%if %{with mpich}
%global mpi_list %{?mpi_list} mpich
%endif
%if %{with openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${mpi:-serial}

# TODO - unbundle
%if %{with bundle_conduit}
Provides:       bundled(conduit)
%endif

%description
Catalyst is an API specification developed for simulations (and other
scientific data producers) to analyze and visualize data in situ.

Catalyst has been split out of ParaView. This package includes the definition
together with a lightweight implementation of this Catalyst API.

For details how to use Catalyst for in situ analysis and visualization in
simulations, see https://catalyst-in-situ.readthedocs.io/en/latest/index.html.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with python}
Requires:       python3-%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with python}
%package -n     python3-%{name}
Summary:        Python3 bindings for %{name}
%py_provides    python3-%{name}

%description -n python3-%{name}
The python3-%{name} package contains Python3 bindings for applications that use
%{name}.
%endif

%if %{with mpich}
%package        mpich
Summary:        MPICH MPI binaries for %{name}
%if %{with bundle_conduit}
Provides:       bundled(conduit)
%endif

%description    mpich
This package contains MPICH MPI binaries for %{name}.

%package        mpich-devel
Summary:        Development files for %{name}-mpich
Requires:       %{name}-mpich%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with python}
Requires:       python3-%{name}-mpich%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description    mpich-devel
The %{name}-mpich-devel package contains libraries and header files for developing
applications that use %{name}-mpich.

%if %{with python}
%package -n     python3-%{name}-mpich
Summary:        Python3 bindings for %{name}-mpich
Requires:       %{name}-mpich%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%py_provides    python3-%{name}-mpich

%description -n python3-%{name}-mpich
The python3-%{name}-mpich package contains Python3 bindings for applications that use
%{name}-mpich.
%endif
%endif

%if %{with openmpi}
%package        openmpi
Summary:        OpenMPI MPI binaries for %{name}
%if %{with bundle_conduit}
Provides:       bundled(conduit)
%endif

%description    openmpi
This package contains OpenMPI MPI binaries for %{name}.

%package        openmpi-devel
Summary:        Development files for %{name}-openmpi
Requires:       %{name}-openmpi%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with python}
Requires:       python3-%{name}-openmpi%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description    openmpi-devel
The %{name}-openmpi-devel package contains libraries and header files for developing
applications that use %{name}-openmpi.

%if %{with python}
%package -n     python3-%{name}-openmpi
Summary:        Python3 bindings for %{name}-openmpi
Requires:       %{name}-openmpi%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%py_provides    python3-%{name}-openmpi

%description -n python3-%{name}-openmpi
The python3-%{name}-openmpi package contains Python3 bindings for applications
that use %{name}-openmpi.
%endif
%endif

%if %{with doc}
%package        doc
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.
%endif

%prep
%forgeautosetup -p1
rm -rf thirdparty/conduit/{fmt,libb64,libyaml,rapidjson,yyjson}

%conf
%global catalyst_common_cmake_options                                           \\\
  -DCATALYST_BUILD_TESTING=ON                                                   \\\
  -DCATALYST_WITH_EXTERNAL_CONDUIT=%[%{with bundle_conduit}?"OFF":"ON"]         \\\
  -DCATALYST_WRAP_FORTRAN=%[%{with fortran}?"ON":"OFF"]                         \\\
  -DCATALYST_WRAP_PYTHON=%[%{with python}?"ON":"OFF"]

%global catalyst_mpi_cmake_options                                              \\\
  -DCMAKE_PREFIX_PATH:PATH=${MPI_HOME}                                          \\\
  -DCMAKE_INSTALL_PREFIX:PATH=${MPI_HOME}                                       \\\
  -DCMAKE_INSTALL_INCLUDEDIR:PATH=../../include/${MPI_COMPILER}                 \\\
  -DCMAKE_INSTALL_LIBDIR:PATH=lib                                               \\\
  -DCATALYST_USE_MPI=%["%{mpi_list}"?"ON":"OFF"]                                \\\
  %{catalyst_common_cmake_options}

# Serial
%cmake                                                                          \
  %{catalyst_common_cmake_options}

# MPI
for mpi in %{mpi_list}; do
  module load mpi/${mpi}-%{_arch}
  %cmake                                                                        \
    %{catalyst_mpi_cmake_options}
  module purge
done

%build
%cmake_build
for mpi in %{mpi_list}; do
  module load mpi/${mpi}-%{_arch}
  %cmake_build
  module purge
done

%if %{with doc}
cd docs
%make_build html
cd -
%endif

%install
%cmake_install
for mpi in %{mpi_list}; do
  module load mpi/${mpi}-%{_arch}
  %cmake_install
  module purge
done

# Fix RUNPATHs and Python MPI installation directories
chrpath -d %{buildroot}%{_bindir}/%{name}_replay
%if %{with python}
chrpath -d %{buildroot}%{python3_sitearch}/%{name}/%{name}_python.so
%endif
for mpi in %{mpi_list}; do
  module load mpi/${mpi}-%{_arch}
  chrpath -r ${MPI_LIB} \
    %{buildroot}${MPI_HOME}/bin/%{name}_replay
%if %{with python}
  mkdir -p %{buildroot}${MPI_PYTHON3_SITEARCH}
  cp -a %{buildroot}${MPI_LIB}/python%{python3_version}/site-packages/* \
    %{buildroot}${MPI_PYTHON3_SITEARCH}
  rm -rf %{buildroot}${MPI_LIB}/python%{python3_version}
  chrpath -r ${MPI_LIB} \
    %{buildroot}${MPI_PYTHON3_SITEARCH}/%{name}/%{name}_python.so
%endif
  module purge
done

%if %{with doc}
install -d %{buildroot}%{_docdir}/%{name}
cp -a docs/_build/html %{buildroot}%{_docdir}/%{name}
%endif

%check
%ctest
%if "%{mpi_list}" != ""
export CATALYST_TEST_MPI_HIGH_NUM_RANKS=${RPM_BUILD_NCPUS}
%if %{with fortran}
export CATALYST_TEST_MPI_HIGH_NUM_RANKS_FORTRAN=${CATALYST_TEST_MPI_HIGH_NUM_RANKS}
%endif
%if %{with python}
%ifnarch %{ix86}
export CATALYST_TEST_MPI_HIGH_NUM_RANKS_PYTHON=${CATALYST_TEST_MPI_HIGH_NUM_RANKS}
%else
# Force serial MPI python tests due to missing mpi4py on %%{ix86}
export CATALYST_TEST_MPI_HIGH_NUM_RANKS_PYTHON=1
%endif
%endif
%endif
%ifnarch s390x
mpi_fail=1
%endif
for mpi in %{mpi_list}; do
  module load mpi/${mpi}-%{_arch}
%ifarch s390x
# s390x has buggy MPICH [1,2]
# [1] https://github.com/icl-utk-edu/heffte/issues/59
# [2] https://github.com/HDFGroup/hdf5/issues/3730
  if [ "${mpi}" = "mpich" ]; then
    mpi_fail=0
  else
    mpi_fail=1
  fi
%endif
  %ctest || (exit ${mpi_fail})
  module purge
done

%files
%license License.txt
%license 3rdPartyLicenses.txt
%{_bindir}/%{name}_replay
%{_libdir}/lib%{name}.so.3*
%if %{with fortran}
%{_libdir}/lib%{name}_fortran.so
%endif
%{_libdir}/%{name}

%files          devel
%dir %{_libdir}/cmake/%{name}-2.1
%{_includedir}/%{name}-2.1
%{_libdir}/cmake/%{name}-2.1/%{name}-config-version.cmake
%{_libdir}/cmake/%{name}-2.1/%{name}-config.cmake
%{_libdir}/cmake/%{name}-2.1/%{name}-macros.cmake
%{_libdir}/cmake/%{name}-2.1/%{name}-targets-debug.cmake
%{_libdir}/cmake/%{name}-2.1/%{name}-targets.cmake
%{_libdir}/cmake/%{name}-2.1/%{name}_impl.c.in
%{_libdir}/cmake/%{name}-2.1/%{name}_impl.h.in
%{_libdir}/lib%{name}.so

%if %{with python}
%files -n       python3-%{name}
%{python3_sitearch}/%{name}
%if %{with bundle_conduit}
%{python3_sitearch}/%{name}_conduit
%endif
%endif

%if %{with mpich}
%files          mpich
%license License.txt
%license 3rdPartyLicenses.txt
%{_libdir}/mpich/bin/%{name}_replay
%{_libdir}/mpich/lib/lib%{name}.so.3*
%if %{with fortran}
%{_libdir}/mpich/lib/lib%{name}_fortran.so
%endif
%{_libdir}/mpich/lib/%{name}

%files          mpich-devel
%dir %{_libdir}/mpich/lib/cmake/%{name}-2.1
%{_includedir}/mpich-%{_arch}/%{name}-2.1
%{_libdir}/mpich/lib/cmake/%{name}-2.1/%{name}-config-version.cmake
%{_libdir}/mpich/lib/cmake/%{name}-2.1/%{name}-config.cmake
%{_libdir}/mpich/lib/cmake/%{name}-2.1/%{name}-macros.cmake
%{_libdir}/mpich/lib/cmake/%{name}-2.1/%{name}-targets-debug.cmake
%{_libdir}/mpich/lib/cmake/%{name}-2.1/%{name}-targets.cmake
%{_libdir}/mpich/lib/cmake/%{name}-2.1/%{name}_impl.c.in
%{_libdir}/mpich/lib/cmake/%{name}-2.1/%{name}_impl.h.in
%{_libdir}/mpich/lib/lib%{name}.so

%if %{with python}
%files -n       python3-%{name}-mpich
%{python3_sitearch}/mpich/%{name}
%if %{with bundle_conduit}
%{python3_sitearch}/mpich/%{name}_conduit
%endif
%endif
%endif

%if %{with openmpi}
%files          openmpi
%license License.txt
%license 3rdPartyLicenses.txt
%{_libdir}/openmpi/bin/%{name}_replay
%{_libdir}/openmpi/lib/lib%{name}.so.3*
%if %{with fortran}
%{_libdir}/openmpi/lib/lib%{name}_fortran.so
%endif
%{_libdir}/openmpi/lib/%{name}

%files          openmpi-devel
%dir %{_libdir}/openmpi/lib/cmake/%{name}-2.1
%{_includedir}/openmpi-%{_arch}/%{name}-2.1
%{_libdir}/openmpi/lib/cmake/%{name}-2.1/%{name}-config-version.cmake
%{_libdir}/openmpi/lib/cmake/%{name}-2.1/%{name}-config.cmake
%{_libdir}/openmpi/lib/cmake/%{name}-2.1/%{name}-macros.cmake
%{_libdir}/openmpi/lib/cmake/%{name}-2.1/%{name}-targets-debug.cmake
%{_libdir}/openmpi/lib/cmake/%{name}-2.1/%{name}-targets.cmake
%{_libdir}/openmpi/lib/cmake/%{name}-2.1/%{name}_impl.c.in
%{_libdir}/openmpi/lib/cmake/%{name}-2.1/%{name}_impl.h.in
%{_libdir}/openmpi/lib/lib%{name}.so

%if %{with python}
%files -n       python3-%{name}-openmpi
%{python3_sitearch}/openmpi/%{name}
%if %{with bundle_conduit}
%{python3_sitearch}/openmpi/%{name}_conduit
%endif
%endif
%endif

%if %{with doc}
%files          doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html
%endif

%changelog
* Wed Jun 03 2026 Python Maint <python-maint@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.15

* Mon May 25 2026 Matthew Krupcale  <mkrupcale@gmail.com> - 2.1.0-2
- Require python3-catalyst* for *-devel packages

* Sun May 24 2026 Matthew Krupcale  <mkrupcale@gmail.com> - 2.1.0-1
- Update to v2.1.0
- Add Fortran and Python bindings, MPI builds, testing, and documentation

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.15.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.14.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.13.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.12.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0-0.11.20201218git2fc94c5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.10.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.9.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.8.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.7.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.6.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.5.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.4.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.3.20201218git2fc94c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 20 2021 Orion Poplawski <orion@nwra.com> - 2.0-0.2.20201218git2fc94c5
- Add %%license, tweak description

* Mon Feb 1 2021 Orion Poplawski <orion@nwra.com> - 2.0-0.1.20201218git2fc94c5
- Initial package
