%global commit 9bb2daf1c83f5932b145a6135f3a48f969639ef3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           espresso
Version:        4.2.2
Release:        10%{?dist}
Summary:        Extensible Simulation Package for Research on Soft matter
# segfault on s390x: https://github.com/espressomd/espresso/issues/3753
# segfault on armv7hl: https://src.fedoraproject.org/rpms/espresso/pull-request/4
ExcludeArch:    s390x i686 armv7hl

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://espressomd.org
Source0:        https://github.com/%{name}md/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# fix for NumPy 2 support
# https://github.com/espressomd/espresso/pull/4992
Patch0:         %{name}-numpy.patch
# fix for CMake 3.30 support
# https://github.com/espressomd/espresso/pull/4992
Patch1:         %{name}-cmake.patch
# improve build reproducibility (diffoscope)
# https://github.com/espressomd/espresso/commit/2111342
Patch2:         %{name}-cython.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake3 >= 3.16
BuildRequires:  /usr/bin/cython
%global cython /usr/bin/cython
BuildRequires:  fftw-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-scipy
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  boost-devel
BuildRequires:  hdf5-devel
BuildRequires:  gsl-devel
BuildRequires:  boost-devel
BuildRequires:  mpich-devel
BuildRequires:  boost-mpich-devel
BuildRequires:  hdf5-mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  boost-openmpi-devel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  python%{python3_pkgversion}-h5py

Requires:       python%{python3_pkgversion}-numpy
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      %{name}-devel < %{version}-%{release}

%description
ESPResSo can perform Molecular Dynamics simulations of bead-spring models
in various ensembles ((N,V,E), (N,V,T), and (N,p,T)).
ESPResSo contains a number of advanced algorithms, e.g.
    * DPD thermostat (for hydrodynamics)
    * P3M, MMM1D, ELC for electrostatic interactions
    * Lattice-Boltzmann for hydrodynamics

%package common
Summary:        Common files for %{name} packages
BuildArch:      noarch
Requires:       %{name}-common = %{version}-%{release}
%description common
ESPResSo can perform Molecular Dynamics simulations of bead-spring models
in various ensembles ((N,V,E), (N,V,T), and (N,p,T)).
ESPResSo contains a number of advanced algorithms, e.g.
    * DPD thermostat (for hydrodynamics)
    * P3M, MMM1D, ELC for electrostatic interactions
    * Lattice-Boltzmann for hydrodynamics
This package contains the license file and data files shared between the
sub-packages of %{name}.

%package -n python%{python3_pkgversion}-%{name}-openmpi
Requires:       %{name}-common = %{version}-%{release}
Requires:       python%{python3_pkgversion}-h5py
Suggests:       python%{python3_pkgversion}-MDAnalysis
Summary:        Extensible Simulation Package for Research on Soft matter
Provides:       %{name}-openmpi = %{version}-%{release}
Obsoletes:      %{name}-openmpi < 3.3.0-12
%description -n python%{python3_pkgversion}-%{name}-openmpi
ESPResSo can perform Molecular Dynamics simulations of bead-spring models
in various ensembles ((N,V,E), (N,V,T), and (N,p,T)).
ESPResSo contains a number of advanced algorithms, e.g.
    * DPD thermostat (for hydrodynamics)
    * P3M, MMM1D, ELC for electrostatic interactions
    * Lattice-Boltzmann for hydrodynamics

This package contains %{name} compiled against Open MPI.


%package -n python%{python3_pkgversion}-%{name}-mpich
Requires:       %{name}-common = %{version}-%{release}
Requires:       python%{python3_pkgversion}-h5py
Suggests:       python%{python3_pkgversion}-MDAnalysis
Summary:        Extensible Simulation Package for Research on Soft matter
Provides:       %{name}-mpich2 = %{version}-%{release}
Obsoletes:      %{name}-mpich2 < 3.1.1-3
Provides:       %{name}-mpich = %{version}-%{release}
Obsoletes:      %{name}-mpich < 3.3.0-12
%description -n python%{python3_pkgversion}-%{name}-mpich
ESPResSo can perform Molecular Dynamics simulations of bead-spring models
in various ensembles ((N,V,E), (N,V,T), and (N,p,T)).
ESPResSo contains a number of advanced algorithms, e.g.
    * DPD thermostat (for hydrodynamics)
    * P3M, MMM1D, ELC for electrostatic interactions
    * Lattice-Boltzmann for hydrodynamics

This package contains %{name} compiled against MPICH2.


%prep
%setup -q -n %{name}
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

%build
%global defopts \\\
 -DWITH_PYTHON=ON \\\
 -DWITH_TESTS=ON \\\
 -DCMAKE_SKIP_RPATH=ON \\\
 -DINSTALL_PYPRESSO=OFF \\\
 -DCTEST_ARGS=%{?_smp_mflags} \\\
 -DTEST_TIMEOUT=480 \\\
 -DWITH_CUDA=OFF \\\
 -DWITH_HDF5=OFF \\\
 -DWITH_GSL=ON \\\
 -DPYTHON_INSTDIR=${MPI_PYTHON3_SITEARCH} \\\
 -DPYTHON_EXECUTABLE=%{__python3} \\\
 -DCYTHON_EXECUTABLE=%{cython}
%global _vpath_builddir ${mpi:-serial}

# https://github.com/espressomd/espresso/issues/3396
%global _lto_cflags %{nil}

for mpi in mpich openmpi ; do
   module load mpi/${mpi}-%{_arch}
   old_LDFLAGS="${LDFLAGS}"
   export LDFLAGS="${LDFLAGS} -Wl,-rpath,${MPI_PYTHON3_SITEARCH}/%{name}md"
   %{cmake3} %{defopts}
   export LD_LIBRARY_PATH=$PWD/${mpi:-serial}/src/config
   %cmake3_build
   export LDFLAGS="${old_LDFLAGS}"
   module unload mpi/${mpi}-%{_arch}
done

%install
for mpi in mpich openmpi ; do
   module load mpi/${mpi}-%{_arch}
   %cmake3_install
   module unload mpi/${mpi}-%{_arch}
done

%check
export CTEST_OUTPUT_ON_FAILURE=1
for mpi in mpich openmpi ; do
   module load mpi/${mpi}-%{_arch}
   export LD_LIBRARY_PATH=${MPI_LIB}:%{buildroot}${MPI_PYTHON3_SITEARCH}/%{name}md
   %cmake3_build --target check_unit_tests
   %cmake3_build --target check_python_skip_long
   module unload mpi/${mpi}-%{_arch}
done

%files common
%doc AUTHORS Readme.md NEWS ChangeLog
%license COPYING

%files -n python%{python3_pkgversion}-%{name}-openmpi
%{python3_sitearch}/openmpi/%{name}md/

%files -n python%{python3_pkgversion}-%{name}-mpich
%{python3_sitearch}/mpich/%{name}md/

%changelog
* Sun Feb 02 2025 Orion Poplawski <orion@nwra.com> - 4.2.2-10
- Rebuild with gsl 2.8

* Thu Jan 23 2025 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/ReproduciblePackageBuilds

* Thu Jan 23 2025 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.2-8
- Rebuilt for NumPy 2.2 and CMake 3.31

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 4.2.2-6
- Rebuild for hdf5 1.14.5

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2.2-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.2.2-3
- Rebuilt for Python 3.13

* Wed Jun 05 2024 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.2-2
- Disable statistical tests (sensitive to Fedora mass rebuilds)
- Re-enable OpenMPI testsuite

* Wed May 22 2024 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.2-1
- Version bump to v4.2.2

* Tue Feb 27 2024 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.1-11
- Fix several occurrences of undefined behavior
- Build and test with all available cores

* Tue Jan 23 2024 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.1-10
- Skip unit test with numerical instabilities

* Mon Jan 22 2024 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.1-9
- Remove support for hdf5

* Mon Jan 22 2024 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.1-8
- Fix for API change in unittest from Python 3.12

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 4.2.1-6
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 4.2.1-4
- Rebuilt for Python 3.12

* Wed Apr 26 2023 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.1-3
- Fix LB inertialess tracers bug, fix compiler warnings

* Tue Apr 18 2023 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.1-2
- Fix for API change in setuptools 67.3.0

* Mon Apr 17 2023 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.1-1
- Version bump to v4.2.1

* Sat Apr 01 2023 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.0-8
- Skip fragile ICC python interface test

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 4.2.0-7
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.0-5
- Fix Python errors from numpy 1.24

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.0-4
- Rebuild for gsl-2.7.1

* Tue Aug 02 2022 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.0-3
- Disable OpenMPI tests

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.2.0-1
- Version bump to v4.2.0

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.1.4-13
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 4.1.4-12
- Rebuilt for Boost 1.78

* Wed Jan 26 2022 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.1.4-11
- Rebuild with CMake fixes and without distutils

* Thu Jan 20 2022 Jean-Noël Grad <jgrad@icp.uni-stuttgart.de> - 4.1.4-10
- Rebuild for GCC 12.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 4.1.4-8
- Rebuild for hdf5 1.12.1

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 4.1.4-7
- Rebuild for hdf5 1.10.7

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 4.1.4-6
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.1.4-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 4.1.4-2
- Rebuilt for Boost 1.75

* Tue Oct 20 2020 Christoph Junghans <junghans@votca.org> - 4.1.4-1
- Version bump to v4.1.4 (bug #1889614)

* Mon Oct 19 2020 Jeff Law <law@redhat.com> - 4.1.3-4
- Fix missing #includes from gcc-10

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Christoph Junghans <junghans@votca.org> - 4.1.3-1
- version bump to v4.1.3 (bug #1855054)

* Fri Jul 03 2020 Christoph Junghans <junghans@votca.org> - 4.1.2-5
- Rebuild for hdf5 1.10.6

* Thu Jun 11 2020 Christoph Junghans <junghans@votca.org> - 4.1.2-4
- fix build with boost-1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.2-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Christoph Junghans <junghans@votca.org> - 4.1.2-1
- Version bump to v4.1.2 (bug #1783470)
- Drop 3312.patch got merge upstream

* Fri Nov 15 2019 Christoph Junghans <junghans@votca.org> - 4.1.1-2
- Remove rpath

* Wed Nov 13 2019 Christoph Junghans <junghans@votca.org> - 4.1.1-1
- Version bump to v4.1.1

* Tue Oct 01 2019 Christoph Junghans <junghans@votca.org> - 4.1.0-1
- Version bump to v4.1.0 (bug #1757509)
- updated 2946.patch to 3228.diff
- major spec clean up

* Wed Sep 11 2019 Christoph Junghans <junghans@votca.org> - 4.0.2-8
- MDAnalysis is optional

* Tue Sep 03 2019 Christoph Junghans <junghans@votca.org> - 4.0.2-7
- fix deps, h5py is needed at cmake time

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.2-6
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Christoph Junghans <junghans@votca.org> - 4.0.2-3
- add missing soversion to libH5mdCore

* Tue Jun 25 2019 Christoph Junghans <junghans@votca.org> - 4.0.2-2
- enable hdf5 support

* Wed Apr 24 2019 Christoph Junghans <junghans@votca.org> - 4.0.2-1
- Version bump to 4.0.2

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 4.0.1-3
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
- Rebuilt to change main python from 3.4 to 3.6 (on epel7)

* Fri Jan 25 2019 Christoph Junghans <junghans@votca.org> - 4.0.1-1
- version bump to 4.0.1

* Fri Sep 07 2018 Christoph Junghans <junghans@votca.org> - 4.0.0-1
- version bump to 4.0.0 (bug #1625379)
- move to python3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.12.20180203gitf74064d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0-0.11.20180203gitf74064d
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Feb 04 2018 Christoph Junghans <junghans@votca.org> - 4.0-0.10.20170220git7a9ac74
- added 1830.patch to fix install (missing libEspressoConfig)

* Sat Feb 03 2018 Christoph Junghans <junghans@votca.org> - 4.0-0.9.20170220git7a9ac74
- Bump to version 4.0 git version f74064d
- Drop 1056.patch, got merged upstream

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.8.20170228git8a021f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.7.20170228git8a021f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0-0.6.20170228git8a021f5
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0-0.5.20170228git8a021f5
- Rebuilt for Boost 1.64

* Sun Mar 12 2017 Peter Robinson <pbrobinson@fedoraproject.org> 4.0-0.4.20170228git8a021f5
- Drop ExcludeArch as boost-mpi is now built on ppc64le

* Sun Mar 05 2017 Christoph Junghans <junghans@votca.org> - 4.0-0.3.20170228git8a021f5
- Dropped 1042.patch, merged upstream
- Add 1056.patch to fix install

* Sat Feb 25 2017 Christoph Junghans <junghans@votca.org> - 4.0-0.2.20170220git7a9ac74
- ExcludeArch: ppc64le due to missing boost-mpi

* Thu Feb 16 2017 Christoph Junghans <junghans@votca.org> - 4.0-0.1.20170220git7a9ac74
- Bump to version 4.0 git version
- Drop cypthon patch, incl. upstream
- Add 1042.patch from upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-10
- Rebuild for openmpi 2.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-8
- Rebuild for openmpi 1.10.0

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.0-7
- Rebuild for MPI provides

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 3.3.0-6
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.3.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 12 2015 Thomas Spura <tomspur@fedoraproject.org> - 3.3.0-3
- Rebuild for changed mpich libraries
- Added patch for building with cython-0.22
- Remove group tag

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Thomas Spura <tomspur@fedoraproject.org> - 3.3.0-1
- update to 3.3.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Thomas Spura <tomspur@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun May 25 2014 Thomas Spura <tomspur@fedoraproject.org> - 3.2.0-2
- run autoreconf in %%build to support aarch64

* Sat May 24 2014 Thomas Spura <tomspur@fedoraproject.org> - 3.2.0-1
- update to 3.2.0

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sat Feb 22 2014 Deji Akingunola <dakingun@gmail.com> - 3.1.1-5
- Rebuild for mpich-3.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Deji Akingunola <dakingun@gmail.com> - 3.1.1-3
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 14 2012 Thomas Spura <tomspur@fedoraproject.org> - 3.1.1-1
- rebuild for newer mpich2
- update to new version
- disable tk per upstream request
- drop patch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.0.2-2
- add missing BR autoconf/automake
- use _isa where possible
- use general tclsh shebang
- build --with-tk

* Thu Oct  6 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.0.2-1
- update to new version
- introduce configure_mpi

* Sun Sep 25 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.0.1-3
- use correct MPI_SUFFIX
- don't install library as upstream doesn't support it anymore

* Sun Sep 25 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.0.1-2
- correctly install into _libdir/openmpi and not _libdir/name-openmpi

* Fri Sep 16 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.0.1-1
- initial packaging
