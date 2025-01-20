%bcond_with mpich
%bcond_with mpi

%bcond_without bundled_sundials

Name:           bionetgen
Version:        2.9.0
Release:        %autorelease
Summary:        Software for rule-based modeling of biochemical systems
# Bionetgen binary file is compiled against bundled muparser (MIT) and sundials-2.6.0 (BSD) libraries
License:        GPL-3.0-only AND BSD-3-Clause AND MIT
URL:            https://github.com/RuleWorld/bionetgen
Source0:        https://github.com/RuleWorld/bionetgen/archive/BioNetGen-%{version}/bionetgen-BioNetGen-%{version}.tar.gz

Patch0:         %{name}-fix_linker.patch
Patch1:         %{name}-fix_cmake_minimum.patch
Patch2:         %{name}-cmake-c99.patch

%if 0%{without bundled_sundials}
BuildRequires:  sundials-devel
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Win32)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       bionetgen-perl = %{version}-%{release}

# BioNetGen does not namespace its perl modules
%global __provides_exclude perl\\(.*BNG.*|Cache|CartesianProduct|Compartment.*|Component.*|Console|EnergyPattern|Expression|Function|HNauty|Map|ModelWrapper|Molecule*|Observable|Param*|PatternGraph|Population*|RateLaw|RefineRule|Rxn*|SBMLMultiAux|Species*|Visualization*|XML::*|XMLReader\\)
%global __requires_exclude perl\\(.*BNG.*|Cache|CartesianProduct|Compartment.*|Component.*|Console|EnergyPattern|Expression|Function|HNauty|Map|ModelWrapper|Molecule*|Observable|Param*|PatternGraph|Population*|RateLaw|RefineRule|Rxn*|SBMLMultiAux|Species*|Visualization*|XML::*|XMLReader\\)

%description
BioNetGen is software for the specification and simulation of
rule-based models of biochemical systems, including signal
transduction, metabolic, and genetic regulatory networks. The
BioNetGen language has recently been extended to include explicit
representation of compartments. A review of methods for rule-based
modeling is available in Science Signaling (Sci. STKE, 18 July 2006,
Issue 344, p. re6).

BioNetGen is presently a mixture of Perl and C++. Network generation
is currently implemented in Perl, the network simulator is C++, and a
new language parser is being developed with ANTLR.

#########
%if 0%{with mpi}
%package openmpi
Summary:    Software for rule-based modeling of biochemical systems (OpenMPI)
BuildRequires:  muParser-devel
%if 0%{without bundled_sundials}
BuildRequires:  sundials-openmpi-devel >= 3.2.1
%endif
BuildRequires:  openmpi-devel
Requires:       bionetgen-perl = %{version}-%{release}

%description openmpi
BioNetGen is software for the specification and simulation of
rule-based models of biochemical systems, including signal
transduction, metabolic, and genetic regulatory networks. The
BioNetGen language has recently been extended to include explicit
representation of compartments. A review of methods for rule-based
modeling is available in Science Signaling (Sci. STKE, 18 July 2006,
Issue 344, p. re6).

BioNetGen is presently a mixture of Perl and C++. Network generation
is currently implemented in Perl, the network simulator is C++, and a
new language parser is being developed with ANTLR.

%package openmpi-devel
Summary:    Software for rule-based modeling of biochemical systems (OpenMPI)

%description openmpi-devel
Software for rule-based modeling of biochemical systems (developer files).
%endif
######

#########
%if 0%{with mpich}
%package mpich
Summary: Software for rule-based modeling of biochemical systems (MPICH)
BuildRequires:  muParser-devel
%if 0%{without bundled_sundials}
BuildRequires:  sundials-mpich-devel >= 3.2.1
%endif
BuildRequires:  mpich-devel
Requires:       bionetgen-perl = %{version}-%{release}

%description mpich
BioNetGen is software for the specification and simulation of
rule-based models of biochemical systems, including signal
transduction, metabolic, and genetic regulatory networks. The
BioNetGen language has recently been extended to include explicit
representation of compartments. A review of methods for rule-based
modeling is available in Science Signaling (Sci. STKE, 18 July 2006,
Issue 344, p. re6).

BioNetGen is presently a mixture of Perl and C++. Network generation
is currently implemented in Perl, the network simulator is C++, and a
new language parser is being developed with ANTLR.

%package mpich-devel
Summary: Software for rule-based modeling of biochemical systems (MPICH)

%description mpich-devel
Software for rule-based modeling of biochemical systems (developer files).
%endif
######

%package perl
Summary:        Perl scripts and Models used by bionetgen
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Math::Trig)
BuildRequires:  make
Requires:       bionetgen = %{version}-%{release}
Requires:       perl(Math::Trig)
Provides:       bundled(XML-TreePP) = 0.41
%description perl
%{summary}.

%prep
%setup -qc

pushd bionetgen-BioNetGen-%{version}

%if 0%{with bundled_sundials}
rm -f bng2/libsource/{gsl-1.9.tar.gz,Mathutils.tar.gz,muparser_v2_2_4.zip}
tar -xvf bng2/libsource/cvode-2.6.0.tar.gz -C bng2/Network3
tar -xvf bng2/libsource/muparser_v2_2_4.tar.gz -C bng2/Network3
%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .backup
%patch -P 2 -p1 -b .c99
rm -f bng2/libsource/*
%endif
popd

%if 0%{with mpi}
cp -a bionetgen-BioNetGen-%{version} openmpi
%endif
%if 0%{with mpich}
cp -a bionetgen-BioNetGen-%{version} mpich
%endif

%build
CFLAGS="$CFLAGS -Wno-unused-variable -Wno-unused-but-set-variable -std=gnu17"
CXXFLAGS="$CXXFLAGS -Wno-deprecated-declarations"

pushd bionetgen-BioNetGen-%{version}/bng2/Network3

# Compile muparser static library
cd muparser_v2_2_4
%configure --enable-shared=no --enable-static=yes --enable-samples=no
%make_build
cd ../

# Compile mathutils static library
make -j1 -C src/util/mathutils

# Build sundials static libraries
%if %{with bundled_sundials}

export CFLAGS="${CFLAGS//-Werror=format-security/-Wno-error=format-security}"
mkdir -p cvode-2.6.0/build
%define _vpath_builddir cvode-2.6.0/build
%cmake -S cvode-2.6.0 -B cvode-2.6.0/build -DCMAKE_MODULE_LINKER_FLAGS:STRING="%{__global_ldflags}" \
 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DEXAMPLES_ENABLE=OFF -DEXAMPLES_INSTALL=OFF \
 -DBUILD_SHARED_LIBS:BOOL=OFF -DBUILD_STATIC_LIBS:BOOL=ON \
 -DMPI_ENABLE:BOOL=OFF \
 -DFCMIX_ENABLE:BOOL=ON
%cmake_build
%endif

export CFLAGS="$CFLAGS -I../src/util/mathutils -I../cvode-2.6.0/include -I../muparser_v2_2_4/include"
export CXXFLAGS="${CXXFLAGS//-Werror=format-security/-Wno-error=format-security} -I../src/util/mathutils -I../cvode-2.6.0/include -I../cvode-2.6.0/include/cvode -I../cvode-2.6.0/build/include  -I../cvode-2.6.0/src/cvode/fcmix -L../src/util/mathutils -I../muparser_v2_2_4/include -L../muparser_v2_2_4/lib -L../cvode-2.6.0/build/src/cvode/fcmix -L../cvode-2.6.0/build/src/sundials -L../cvode-2.6.0/build/src/cvode -L../cvode-2.6.0/build/src/nvec_ser"
mkdir -p build
%define _vpath_builddir build
%cmake  -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DBUILD_SHARED_LIBS:BOOL=OFF -DBUILD_STATIC_LIBS:BOOL=ON
%cmake_build
popd

%if 0%{with mpi}
pushd openmpi/bng2/Network3

%{_openmpi_load}
%{_openmpi_unload}

popd
%endif

%if 0%{with mpich}
pushd mpich/bng2/Network3

%{_mpich_load}
%{_mpich_unload}

popd
%endif


%install
pushd bionetgen-BioNetGen-%{version}/bng2/Network3/build
mkdir -vp %{buildroot}%{_bindir}
install -pm 755 run_network %{buildroot}%{_bindir}/
popd

mkdir -vp %{buildroot}%{perl_vendorlib}/BioNetGen
cp -r bionetgen-BioNetGen-%{version}/bng2/Perl2 %{buildroot}%{perl_vendorlib}/BioNetGen/
cp -r bionetgen-BioNetGen-%{version}/bng2/BNG2.pl %{buildroot}%{perl_vendorlib}/BioNetGen/
cp -a bionetgen-BioNetGen-%{version}/bng2/Models2 %{buildroot}%{perl_vendorlib}/BioNetGen/
rm -f %{buildroot}%{perl_vendorlib}/BioNetGen/Models2/bin/run_network_%{_arch}-linux
rm -f %{buildroot}%{perl_vendorlib}/BioNetGen/Models2/run_network

%if 0%{with mpi}
%{_openmpi_load}
%{_openmpi_unload}
%endif

%if 0%{with mpich}
%{_mpich_load}
%{_mpich_unload}
%endif

%check
pushd bionetgen-BioNetGen-%{version}/bng2/Models2
%ifarch %{arm}
install -pm 755 ../Network3/build/run_network -D ./bin/run_network_armv7l-linux
install -pm 755 ../Network3/build/run_network -D ../bin/run_network_armv7l-linux
%else
install -pm 755 ../Network3/build/run_network -D ./bin/run_network_%{_target_cpu}-linux
install -pm 755 ../Network3/build/run_network -D ../bin/run_network_%{_target_cpu}-linux
%endif
echo "Running some tests ..."
../BNG2.pl CaOscillate_Func.bngl CaOscillate_Sat.bngl catalysis.bngl egfr_net.bngl egfr_net_red.bngl egfr_path.bngl energy_example1.bngl fceri_ji.bngl test_continue.bngl
echo "Tests finished."

%files
%license bionetgen-BioNetGen-%{version}/LICENSE
%doc bionetgen-BioNetGen-%{version}/README.md bionetgen-BioNetGen-%{version}/bng2/CREDITS.txt
%doc bionetgen-BioNetGen-%{version}/bng2/CHANGES.txt bionetgen-BioNetGen-%{version}/bng2/VERSION
%{_bindir}/run_network

%files perl
%{perl_vendorlib}/BioNetGen/

%if 0%{with mpi}
%files openmpi
%license bionetgen-BioNetGen-%{version}/LICENSE
%doc bionetgen-BioNetGen-%{version}/README.md bionetgen-BioNetGen-%{version}/bng2/CREDITS.txt
%doc bionetgen-BioNetGen-%{version}/bng2/CHANGES.txt bionetgen-BioNetGen-%{version}/bng2/VERSION
%{_libdir}/openmpi/bin/run_network
%endif

%if 0%{with mpich}
%files mpich
%license bionetgen-BioNetGen-%{version}/LICENSE
%doc bionetgen-BioNetGen-%{version}/README.md bionetgen-BioNetGen-%{version}/bng2/CREDITS.txt
%doc bionetgen-BioNetGen-%{version}/bng2/CHANGES.txt bionetgen-BioNetGen-%{version}/bng2/VERSION
%{_libdir}/mpich/bin/run_network
%endif

%changelog
%autochangelog
