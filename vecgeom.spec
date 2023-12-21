%bcond_without check

%global forgeurl https://gitlab.cern.ch/VecGeom/VecGeom
Version:        1.2.7
%global tag v%{version}
%forgemeta

Name:           vecgeom
Release:        %autorelease
Summary:        A vectorized geometry library for particle-detector simulation
# the library is licensed under Apache-2.0, except
# base/robin_hood.h - robin-hood-hashing - MIT
# the following source code files from celeritas project - Apache-2.0 OR MIT:
# VecGeom/management/{ColorUtils.h,Environment.h,Logger.h,LoggerMessage.h,LoggerTypes.h}
# source/{ColorUtils.cpp,Environment.cpp,Logger.cpp,LoggerMessage.cpp,LoggerTypes.cpp}
License:        Apache-2.0 AND MIT AND (Apache-2.0 OR MIT)
URL:            %{forgeurl}
Source0:        %{forgesource}
# add soversion to the library
# modified from https://gitlab.cern.ch/VecGeom/VecGeom/-/merge_requests/889
Patch0:         vecgeom-add-soversion.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xerces-c)
BuildRequires:  cmake(veccore)

%description
VecGeom is a geometry modeller library with hit-detection features as needed by
particle detector simulation at the LHC and beyond. It was incubated by a
Geant-R&D initiative and the motivation to combine the code of Geant4 and
ROOT/TGeo into a single, better maintainable piece of software within the
EU-AIDA program. As such it is close in scope to TGeo and Geant4 geometry
modellers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DVECGEOM_GDML=ON \

%cmake_build

%install
%cmake_install

%if %{with check}
%check
# the tests all passed only on x86_64 architecture currently
%ifarch x86_64
%ctest
%endif
%endif

%files
%license LICENSE.txt APACHE-LICENSE-2.0.txt
%doc README.md
%{_libdir}/libvecgeom.so.1.2*
%{_libdir}/libvgdml.so.1.2*

%files devel
%{_includedir}/VecGeom/
%dir %{_libdir}/cmake/VecGeom
%{_libdir}/cmake/VecGeom/*.cmake
%{_libdir}/libvecgeom.so
%{_libdir}/libvgdml.so

%changelog
%autochangelog
