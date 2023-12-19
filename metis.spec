%undefine _ld_as_needed

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%global arch64 1
%else
%global arch64 0
%endif

Name:    metis
Version: 5.1.0.3
Release: %autorelease
Summary: Serial Graph Partitioning and Fill-reducing Matrix Ordering
License: Apache-2.0 AND LGPL-2.0-or-later
URL:     http://glaros.dtc.umn.edu/gkhome/views/%{name}
Source0: https://github.com/scivision/METIS/archive/refs/tags/v%{version}/METIS-%{version}.tar.gz

## This patch sets up libmetis soname of libmetis
Patch0:  %{name}-libmetis.patch

## This patch sets up shared GKlib library 
Patch1:  %{name}-shared-GKlib.patch

## This patch sets up GKREGEX, GKRAND, libsuffix options to the Makefiles 
Patch3:  %{name}-GKREGEX-GKRAND-LIBSUFFIX-fix.patch

## Rename library of 64 integer version
Patch4: %{name}_lib64.patch

Patch5: %{name}-pcre2.patch

BuildRequires: make
BuildRequires: cmake, gcc, gcc-c++
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires: pcre-devel
%else
BuildRequires: pcre2-devel
%endif
BuildRequires: help2man
BuildRequires: chrpath
#BuildRequires: GKlib-devel

%description
METIS is a set of serial programs for partitioning graphs, 
partitioning finite element meshes, and producing fill reducing 
orderings for sparse matrices. 
The algorithms implemented in METIS are based on the multilevel 
recursive-bisection, multilevel k-way, and multi-constraint 
partitioning schemes developed in our lab.
METIS is distributed with OpenMP support.

%package devel
Summary: METIS headers and development-related files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Header and library files of Metis.

%if 0%{?arch64}
%package -n metis64
Summary: Serial Graph Partitioning and Fill-reducing Matrix Ordering (64bit INTEGER)

%description -n metis64
METIS is a set of serial programs for partitioning graphs, 
partitioning finite element meshes, and producing fill reducing 
orderings for sparse matrices. 
The algorithms implemented in METIS are based on the multilevel 
recursive-bisection, multilevel k-way, and multi-constraint 
partitioning schemes developed in our lab.
METIS is distributed with OpenMP support.
This build has 64bit INTEGER support.

%package -n metis64-devel
Summary: METIS development libraries (64bit INTEGER)
Requires: metis64%{?_isa} = %{version}-%{release}

%description -n metis64-devel
Header and library files of Metis,
OpenMP version (64bit INTEGER).
%endif

%prep
%setup -qc 
 
pushd METIS-%{version}
rm -rf archive

%patch -P 0 -p0 -b .backup
%patch -P 1 -p0 -b .backup
%patch -P 3 -p0 -b .backup
%patch -P 5 -p0 -b .backup
popd

%if 0%{?arch64}
cp -a METIS-%{version} metis64
pushd metis64
%patch -P 4 -p0 -b .backup
popd
%endif

%build
%if 0%{?rhel} && 0%{?rhel} < 9
PCRE_LDFLAGS="-lpcreposix"
%else
PCRE_LDFLAGS="-lpcre2-posix"
%endif
%cmake -S METIS-%{version} -B METIS-%{version} \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DGKLIB_PATH=METIS-%{version}/src//GKlib \
 -DGKRAND:BOOL=ON \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES\
 -DSHARED:BOOL=TRUE \
 -DOPENMP:BOOL=ON \
 -DPCRE:BOOL=ON \
 -DCMAKE_C_FLAGS:STRING="%{optflags} -pthread" \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $PCRE_LDFLAGS" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $PCRE_LDFLAGS" \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}
%make_build -C METIS-%{version}

%if 0%{?arch64}
%if 0%{?rhel} && 0%{?rhel} < 9
PCRE_LDFLAGS="-lpcreposix"
%else
PCRE_LDFLAGS="-lpcre2-posix"
%endif
%cmake -S metis64 -B metis64 \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -Dintsize:STRING=64 -Drealsize:STRING=64 \
 -DGKLIB_PATH=METIS-%{version}/src/GKlib \
 -DGKRAND:BOOL=ON \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES\
 -DSHARED:BOOL=TRUE \
 -DOPENMP:BOOL=ON \
 -DPCRE:BOOL=ON \
 -DCMAKE_C_FLAGS:STRING="%{optflags} -pthread" \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $PCRE_LDFLAGS" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $PCRE_LDFLAGS" \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}
%make_build -C metis64
%endif

%install
pushd METIS-%{version}
%make_install

## Generate manpages from binaries
LD_PRELOAD=%{buildroot}%{_libdir}/lib%{name}.so.0 \
help2man --version-string="%{version}" -n "Partitions a graph into a specified number of parts." \
 -N --output="gpmetis.1" --no-discard-stderr --help-option="-help" %{buildroot}%{_bindir}/gpmetis

LD_PRELOAD=%{buildroot}%{_libdir}/lib%{name}.so.0 \
help2man --version-string="%{version}" \
 -n "Computes a fill-reducing ordering of the vertices of the graph using multilevel nested dissection." \
 -N --output="ndmetis.1" --no-discard-stderr --help-option="-help" %{buildroot}%{_bindir}/ndmetis

LD_PRELOAD=%{buildroot}%{_libdir}/lib%{name}.so.0 \
help2man --version-string="%{version}" -n "Partitions a mesh into a specified number of parts." \
 -N --output="mpmetis.1" --no-discard-stderr --help-option="-help" %{buildroot}%{_bindir}/mpmetis

LD_PRELOAD=%{buildroot}%{_libdir}/lib%{name}.so.0 \
help2man --version-string="%{version}" -n "Converts a mesh into a graph that is compatible with METIS." \
 -N --output="m2gmetis.1" --no-discard-stderr -h "-help" %{buildroot}%{_bindir}/m2gmetis

mkdir -p %{buildroot}%{_mandir}/man1
mv *.1 %{buildroot}%{_mandir}/man1
popd

# Save metis.h with IDXTYPEWIDTH = 32
mv %{buildroot}%{_includedir}/metis.h %{buildroot}%{_includedir}/metis32.h

%if 0%{?arch64}
pushd metis64
%make_install
# Save metis.h with IDXTYPEWIDTH = 64
mv %{buildroot}%{_includedir}/metis.h %{buildroot}%{_includedir}/metis64.h
popd
%endif

# Save metis.h with IDXTYPEWIDTH = 32
mv %{buildroot}%{_includedir}/metis32.h %{buildroot}%{_includedir}/metis.h

## Remove rpaths
chrpath -d %{buildroot}%{_bindir}/*

%check
cp -p %{buildroot}%{_bindir}/*metis METIS-%{version}/src/graphs/
cp -p %{buildroot}%{_bindir}/graphchk METIS-%{version}/src/graphs/
cd METIS-%{version}/src/graphs
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./ndmetis mdual.graph
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./mpmetis metis.mesh 2
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./gpmetis test.mgraph 4
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./gpmetis copter2.graph 4
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./graphchk 4elt.graph
cd ../../
%ctest -- --test-dir ./
cd ../
%if 0%{?arch64}
cp -p %{buildroot}%{_bindir}/*metis64 metis64/src/graphs/
cp -p %{buildroot}%{_bindir}/graphchk64 metis64/src/graphs/
cd metis64/src/graphs
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./ndmetis64 mdual.graph
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./mpmetis64 metis.mesh 2
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./gpmetis64 test.mgraph 4
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./gpmetis64 copter2.graph 4
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./graphchk64 4elt.graph
cd ../../
%ctest -- --test-dir ./
cd ../
%endif

%files
%doc METIS-%{version}/src/Changelog METIS-%{version}/src/manual/manual.pdf
%license METIS-%{version}/src/LICENSE.txt
%{_bindir}/cmpfillin
%{_bindir}/gpmetis
%{_bindir}/graphchk
%{_bindir}/m2gmetis
%{_bindir}/mpmetis
%{_bindir}/ndmetis
%{_mandir}/man1/*.1.gz
%{_libdir}/lib%{name}.so.0

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%if 0%{?arch64}
%files -n metis64
%doc metis64/src/Changelog metis64/src/manual/manual.pdf
%license metis64/src/LICENSE.txt
%{_bindir}/cmpfillin64
%{_bindir}/gpmetis64
%{_bindir}/graphchk64
%{_bindir}/m2gmetis64
%{_bindir}/mpmetis64
%{_bindir}/ndmetis64
%{_libdir}/lib%{name}64.so.0

%files -n metis64-devel
%{_includedir}/%{name}64.h
%{_libdir}/lib%{name}64.so
%endif

%changelog
%autochangelog
