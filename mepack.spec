%global major 1
%global minor 1
%global patch 1

Name:           mepack
Version:        %{major}.%{minor}.%{patch}
Release:        %autorelease
Summary:        A Fortran software library for solving dense Sylvester-like matrix equations

# libcscutils/    is LGPL-2.1-or-later
# lapack-missing/ is BSD-3-Clause
# everything else is GPL-3.0-or-later
License:        GPL-3.0-or-later and LGPL-2.1-or-later and BSD-3-Clause
URL:            https://www.mpi-magdeburg.mpg.de/projects/%{name}
Source0:        https://github.com/mpimd-csc/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make, cmake
BuildRequires:  gcc, gcc-fortran
BuildRequires:  flexiblas-devel
BuildRequires:  hdf5-devel
BuildRequires:  doxygen

%global _description %{expand:
MEPACK is a software library focused on solving dense Sylvester-like
matrix equations. The library is written in Fortran and provides
interfaces for C, MATLAB and GNU Octave. The development places great
emphasis on the fact that the algorithms can be adapted very well to
modern CPU architectures by current Fortran compilers. In addition, the
algorithms are accelerated through the use of directed acyclic graphs
using OpenMP to increase the utility of multicore architectures.
}

%description %_description

%if 0%{?__isa_bits} == 64
%package -n %{name}64
Summary:        A Fortran software library for solving dense Sylvester-like matrix equations

%description -n %{name}64 %_description
This build has 64-bit integer support.
%endif

%package devel
Summary:        Development headers and libraries for MEPACK
Requires:       gcc-gfortran%{_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?__isa_bits} == 64
Requires:       %{name}64%{?_isa} = %{version}-%{release}
%endif

%description devel %_description
This package contains the development headers and libraries.

%prep
%autosetup -p1
sed -i 's/GENERATE_HTML[ \t]*= YES/GENERATE_HTML = NO/g' doc/Doxyfile.in
sed -i 's/GENERATE_MAN [ \t]*= NO/GENERATE_MAN  = YES/g' doc/Doxyfile.in

%build
%cmake -B build \
    -DCMAKE_INSTALL_MODULEDIR=%{_fmoddir}/%{name} \
    -DINTEGER8=OFF \
    -DEXAMPLES=ON \
    -DDOC=ON
%make_build -C build
%make_build -C build doc
find build/doc -type f -size -50c -delete
%if 0%{?__isa_bits} == 64
%cmake -B build64 \
    -DCMAKE_INSTALL_MODULEDIR=%{_fmoddir}/%{name}64 \
    -DINTEGER8=ON \
    -DEXAMPLES=ON
%make_build -C build64
%endif

%install
%make_install -C build
install -d -m 0755 %{buildroot}%{_mandir}
cp -R build/doc/man/man3 %{buildroot}%{_mandir}
%if 0%{?__isa_bits} == 64
%make_install -C build64
%endif

%check
make -C build test
%if 0%{?__isa_bits} == 64
make -C build64 test
%endif

%files
%license LICENSE
%doc README.md CHANGELOG.md CITATION.cff
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.%{minor}.%{patch}

%if 0%{?__isa_bits} == 64
%files -n %{name}64
%license LICENSE
%doc README.md CHANGELOG.md CITATION.cff
%{_libdir}/lib%{name}64.so.%{major}
%{_libdir}/lib%{name}64.so.%{major}.%{minor}.%{patch}
%endif

%files devel
%{_mandir}/man3/*.3*
%{_includedir}/%{name}
%{_fmoddir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%if 0%{?__isa_bits} == 64
%{_includedir}/%{name}64
%{_fmoddir}/%{name}64
%{_libdir}/cmake/%{name}64
%{_libdir}/lib%{name}64.so
%{_libdir}/pkgconfig/%{name}64.pc
%endif

%changelog
%autochangelog
