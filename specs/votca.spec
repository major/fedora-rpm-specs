Name:           votca
Version:        2024.2
%global         uversion %{version}
%global         sover 2024
Release:        4%{?dist}
Summary:        Versatile Object-oriented Toolkit for Coarse-graining Applications
License:        Apache-2.0
URL:            http://www.votca.org
Source0:        https://github.com/votca/votca/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global with_xtp 1

%global with_gmx 1
# no gromacs package on s390x
# same for espressomd
%ifarch s390x
%global with_gmx 0
%endif

BuildRequires:  gcc-c++
BuildRequires:  fdupes
BuildRequires:  cmake3
BuildRequires:  expat-devel
BuildRequires:  fftw-devel
BuildRequires:  eigen3-devel
BuildRequires:  boost-devel
%if %{with_gmx}
BuildRequires:  gromacs-devel
%endif
BuildRequires:  perl-generators
BuildRequires:  hdf5-devel
BuildRequires:  python3
%if %{with_xtp}
BuildRequires:  python3-lxml
BuildRequires:  python3-h5py
BuildRequires:  libxc-devel
BuildRequires:  libecpint-devel
BuildRequires:  libint2-devel
%endif

# mpi packages only used for testing
%if %{with_gmx}
BuildRequires:  gromacs-openmpi
# only needed to run gromacs
BuildRequires:  openmpi-devel
BuildRequires:  python3-espresso-openmpi
%else
%global _openmpi_load %{nil}
%global _openmpi_unload %{nil}
%endif

#used for testing only
%if %{with_gmx}
BuildRequires:  gromacs
%endif
BuildRequires:  lammps
BuildRequires:  python3-cma
BuildRequires:  python3-pytest
BuildRequires:  gnuplot
BuildRequires:  psmisc

Requires:   %{name}-common = %{version}-%{release}
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
%if %{with_xtp}
Requires:   %{name}-common-xtp = %{version}-%{release}
%endif
Obsoletes:      votca-tools <= 2022~rc1
Provides:       votca-tools = %version-%release
Obsoletes:      votca-csg <= 2022~rc1
Provides:       votca-csg = %version-%release
Obsoletes:      votca-xtp <= 2022~rc1
Provides:       votca-xtp = %version-%release

%global votca_desc \
VOTCA is a software package which focuses on the analysis of molecular \
dynamics data, the development of systematic coarse-graining techniques as \
well as methods used for simulating microscopic charge (and exciton) transport \
in disordered semiconductors.

%description
%{votca_desc}

%package devel
Summary:        Development headers and libraries for votca
Requires:       pkgconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# votca header include these headers
Requires:       boost-devel
Requires:       expat-devel
Requires:       fftw3-devel
Requires:       libxc-devel
Requires:       libint2-devel
Requires:       libecpint-devel
Requires:       hdf5-devel
Obsoletes:      votca-csg-devel <= 2022~rc1
Provides:       votca-csg-devel = %version-%release
Obsoletes:      votca-tools-devel <= 2022~rc1
Provides:       votca-tools-devel = %version-%release
Obsoletes:      votca-xtp-devel <= 2022~rc1
Provides:       votca-xtp-devel = %version-%release

%description devel
%{votca_desc}

This package contains development headers and libraries for the VOTCA
package.

%package libs
Summary:    Libraries for VOTCA coarse-graining engine
Obsoletes:  votca-csg-libs <= 2022~rc1
Provides:   votca-csg-libs = %version-%release
Obsoletes:  votca-xtp-libs <= 2022~rc1
Provides:   votca-xtp-libs = %version-%release

%description libs
%{votca_desc}

This package contains libraries for the VOTCA package.

%package common
Summary:    Architecture independent data files for VOTCA
BuildArch:  noarch
Obsoletes:  votca-csg-common <= 2022~rc1
Provides:   votca-csg-common = %version-%release

%description common
%{votca_desc}

This package contains architecture independent data files for the VOTCA
package.

%package csg-tutorials
Summary:    Architecture independent csg tutorial files for VOTCA
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description csg-tutorials
%{votca_desc}

This package contains architecture independent csg tutorial files
for the VOTCA package.

# split off as some arch do not have xtp parts
%if %{with_xtp}
%package xtp-tutorials
Summary:    Architecture independent xtp tutorial files for VOTCA
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description xtp-tutorials
%{votca_desc}

This package contains architecture independent xtp tutorial files
for the VOTCA package.

%package common-xtp
Summary:    Architecture independent data files for xtp parts of VOTCA
BuildArch:  noarch
Obsoletes:  votca-xtp-common <= 2022~rc1
Provides:   votca-xtp-common = %version-%release

%description common-xtp
%{votca_desc}

This package contains architecture independent data files for the xtp
parts of the VOTCA package.
%endif

%package bash
Summary:    Bash completion for VOTCA
Requires:   %{name} = %{version}-%{release}
Requires:   bash-completion
BuildArch:  noarch
Obsoletes:  votca-csg-bash <= 2022~rc1
Provides:   votca-csg-bash = %version-%release

%description bash
%{votca_desc}

This package contains bash completion support for the VOTCA package.

%prep
%autosetup -p1 -n %{name}-%{uversion}

# we don't have an espressopp package in Fedora yet
rm -rf csg-tutorials/spce/ibi_espressopp

%build
# load openmpi, so that cmake can find mdrun_openmpi for testing only
%_openmpi_load
# not a 100% sure why this is needed, but otherwise espressomd cannot be found
export PYTHONPATH="${MPI_PYTHON3_SITEARCH}${PYTHONPATH:+:}${PYTHONPATH}"

%{cmake} -DCMAKE_BUILD_TYPE=Release -DINSTALL_RC_FILES=OFF -DENABLE_TESTING=ON -DBUILD_CSGAPPS=ON \
 -DBUILD_XTP=%{with_xtp} \
  -DENABLE_REGRESSION_TESTING=ON -DHDF5_C_COMPILER_EXECUTABLE=/usr/bin/h5cc -DINJECT_MARCH_NATIVE=OFF
%cmake_build
%_openmpi_unload

%install
%cmake_install
# Install bash completion file
%__install -D -m0644 %{__cmake_builddir}/csg/scripts/csg-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/votca

%fdupes %{buildroot}%{_prefix}

%check
%_openmpi_load
export PYTHONPATH="${MPI_PYTHON3_SITEARCH}${PYTHONPATH:+:}${PYTHONPATH}"
%ctest
%_openmpi_unload

%files
%{_bindir}/{votca,csg,xtp}_*
%{_mandir}/man1/{votca,csg,xtp}_*.1*
%{_mandir}/man7/votca-*.7*

%files common
%doc CHANGELOG.rst NOTICE.rst README.rst
%license LICENSE
%{_datadir}/votca/
%exclude %{_datadir}/votca/*-tutorials/
%exclude %{_datadir}/votca/xtp/

%files csg-tutorials
%{_datadir}/votca/csg-tutorials/

%if %{with_xtp}
%files xtp-tutorials
%{_datadir}/votca/xtp-tutorials/

%files common-xtp
%license LICENSE
%{_datadir}/votca/xtp/
%endif

%files libs
%license LICENSE
%{_libdir}/libvotca_*.so.%{sover}

%files devel
%{_includedir}/votca/
%{_libdir}/libvotca_*.so
%{_libdir}/cmake/VOTCA_*

%files bash
%{_datadir}/bash-completion/completions/votca

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 2024.2-3
- Rebuild for hdf5 1.14.5

* Sat Oct 12 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2024.2-2
- Rebuild against libxc 7.0.0 in rawhide.

* Sun Sep 29 2024 Christoph Junghans <junghans@votca.org> - 2024.2-1
- Version bump to v2024.2 (bug #2315578)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2024.1-2
- convert license to SPDX

* Sat Jul 20 2024 Christoph Junghans <junghans@votca.org> - 2024.1-1
- Version bump to v2024.1 (bug #2298540)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 01 2024 Christoph Junghans <junghans@votca.org> - 2024-2
- Rebuilt to gromacs-2024

* Wed Jan 24 2024 Christoph Junghans <junghans@votca.org> - 2024-1
- Version bump to v2024 (bug#2260025)

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 2023-2
- Rebuilt for Boost 1.83

* Thu Nov 16 2023 Christoph Junghans <junghans@votca.org> - 2023-1
- Version bump to v2023

* Sun Nov 12 2023 Christoph Junghans <junghans@votca.org> - 2023~rc2-2
- Rebuild for gromacs-2023

* Wed Jul 26 2023 Christoph Junghans <junghans@votca.org> - 2023~rc2-1
- Version bump to v2023-rc.2

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023~rc1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2023~rc1-2
- Rebuilt for Boost 1.81

* Fri Feb 03 2023 Christoph Junghans <junghans@votca.org> - 2023-1
- Version bump to v2023-rc.1 (bug #2166654)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Christoph Junghans <junghans@votca.org> - 2022.1-1
- Version bump to v2022.1

* Tue Nov 29 2022 Christoph Junghans <junghans@votca.org> - 2022-11
- Rebuild for libxc again

* Thu Oct 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2022-10
- Rebuild for new libxc

* Mon Oct 24 2022 Christoph Junghans <junghans@votca.org> - 2022-9
- Rebuild for libxc-6.0.0

* Mon Aug 08 2022 Christoph Junghans <junghans@votca.org> - 2022-8
- Fix build wtih espresso-4.2.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2022-6
- Rebuilt for Boost 1.78

* Wed Apr 27 2022 Christoph Junghans <junghans@votca.org> - 2022-5
- Rebuild for gromacs-2022.1

* Sat Feb 05 2022 Christoph Junghans <junghans@votca.org> - 2022-4
- Rebuild for gromacs-2021

* Tue Feb 01 2022 Christoph Junghans <junghans@votca.org> - 2022-3
- Remove espressopp tutorial and hence py2 dep

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Christoph Junghans <junghans@votca.org> - 2022-1
- Version bump to v2020 (bug #2041116)

* Wed Dec 29 2021 Christoph Junghans <junghans@votca.org> - 2022~rc2-2
- Incorporated changes from package review (bug #2032487#c7)

* Thu Dec 23 2021 Christoph Junghans <junghans@votca.org> - 2022~rc2-1
- initial import (bug #2032487)

