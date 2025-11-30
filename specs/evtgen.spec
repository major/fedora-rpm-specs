%global real_version 3.00.00b1
%global tarball_version 0%{gsub %real_version b -beta}

Name:           evtgen
Version:        %real_version
Release:        %autorelease
Summary:        Event generator for particle physics

License:        GPL-3.0-or-later
URL:            https://evtgen.hepforge.org/
Source0:        EvtGen-%{tarball_version}.tar.gz
# ideally this should be downloaded from
#   https://evtgen.hepforge.org/downloads?f=EvtGen-%%{tarball_version}.tar.gz
# However, the url contains a query string which tricks fedpkg and pagure/distgit
# into thinking the file is not the source we want.
# 59dbf2f4f91dbd59072e3e2ef53ce60cdbc6a5021f0df3001c43d6350716167d  EvtGen-03.00.00-beta1.tar.gz

# disable rpath
# disable installation of static libraries
# link libEvtGenExternal against libEvtGen
Patch0:         evtgen-3.0.0b1.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  python3
BuildRequires:  pythia8-devel
BuildRequires:  HepMC3-devel
BuildRequires:  HepMC3-search-devel
BuildRequires:  doxygen

Requires:       %{name}-data = %{version}-%{release}

%description
EvtGen is a Monte Carlo event generator that simulates the decays
of heavy flavor particles, primarily B and D mesons. It contains
a range of decay models for intermediate and final states
containing scalar, vector and tensor mesons or resonances, as well
as leptons, photons and baryons. Decay amplitudes are used to
generate each branch of a given full decay tree, taking into
account angular and time-dependent correlations which allows for
the simulation of CP-violating processes.

%package devel
Summary:        Development files for evtgen
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-data = %{version}-%{release}

%description devel
This package contains the header files and libraries needed to
develop applications using evtgen.

%package data
Summary:        Data files for evtgen
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data
This package contains the data files needed by evtgen.

%package doc
Summary:        Documentation for evtgen
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
This package contains the documentation for evtgen.

%prep
%autosetup -n EvtGen/R%{gsub %tarball_version [.] -} -p1

%build
%cmake -DEVTGEN_PYTHIA=BOOL:ON \
       -DEVTGEN_HEPMC3=BOOL:ON \
       -DEVTGEN_BUILD_DOC=BOOL:ON \
       -DEVTGEN_BUILD_DOXYGEN=BOOL:ON
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/libEvtGen.so.*
%{_libdir}/libEvtGenExternal.so.*

%files devel
%{_libdir}/libEvtGen.so
%{_libdir}/libEvtGenExternal.so
%{_includedir}/EvtGen
%{_includedir}/EvtGenExternal
%{_includedir}/EvtGenBase
%{_includedir}/EvtGenModels
%{_datadir}/EvtGen/cmake

%files data
%{_datadir}/EvtGen
%exclude %{_datadir}/EvtGen/cmake

%files doc
%doc %{_docdir}/EvtGen

%changelog
%autochangelog
