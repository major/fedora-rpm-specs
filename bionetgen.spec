%bcond_with mpich
%bcond_with mpi

%bcond_without bundled_sundials

Name:           bionetgen
Version:        2.8.4
Release:        3%{?dist}
Summary:        Software for rule-based modeling of biochemical systems
# Bionetgen binary file is compiled against bundled muparser (MIT) and sundials-2.6.0 (BSD) libraries
License:        GPLv3 and BSD and MIT
URL:            https://github.com/RuleWorld/bionetgen
Source0:        https://github.com/RuleWorld/bionetgen/archive/BioNetGen-%{version}/bionetgen-BioNetGen-%{version}.tar.gz

Patch0:         %{name}-fix_linker.patch
Patch1:         %{name}-fix_cmake_minimum.patch
Patch2:         bionetgen-cmake-c99.patch

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
%patch0 -p1 -b .backup
%patch1 -p1 -b .backup
%patch2 -p1 -b .c99
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

SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CFLAGS="$SETOPT_FLAGS"
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

SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CFLAGS="$SETOPT_FLAGS -I../src/util/mathutils -I../cvode-2.6.0/include -I../muparser_v2_2_4/include"
export CXXFLAGS="$SETOPT_FLAGS -I../src/util/mathutils -I../cvode-2.6.0/include -I../cvode-2.6.0/include/cvode -I../cvode-2.6.0/build/include  -I../cvode-2.6.0/src/cvode/fcmix -L../src/util/mathutils -I../muparser_v2_2_4/include -L../muparser_v2_2_4/lib -L../cvode-2.6.0/build/src/cvode/fcmix -L../cvode-2.6.0/build/src/sundials -L../cvode-2.6.0/build/src/cvode -L../cvode-2.6.0/build/src/nvec_ser"
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
* Sun Dec 11 2022 Florian Weimer <fweimer@redhat.com> - 2.8.4-3
- Port bundled CVODE CMake script to C99

* Fri Sep 09 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.8.4-2
- Switch to CMake method (rhbz#2124489)

* Mon Aug 08 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.8.4-1
- Release 2.8.4

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.8.2-2
- Perl 5.36 rebuild

* Sun May 15 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.8.2-1
- Release 2.8.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 02 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-1
- Release 2.7.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.0-2
- Perl 5.34 rebuild

* Thu Apr 29 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.6.0-1
- Release 2.6.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.5.2-1
- Release 2.5.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.1-2
- Perl 5.32 rebuild

* Fri Jun 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.5.1-1
- Release 2.5.1

* Fri Mar 20 2020 Petr Pisar <ppisar@redhat.com> - 2.5.0-7
- Specify dependencies for the tests

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-4
- Use devtoolset-8 on EPEL 7

* Mon Jul 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-3
- Rebuild for sundials

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.0-2
- Perl 5.30 rebuild

* Tue May 07 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-1
- Release 2.5.0

* Sat Apr 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-5
- Ready for MPI (disabled)
- Bundle Sundials

* Wed Feb 13 2019 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-4
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-2
- Filtering of SBMLMultiAux module

* Thu Nov 08 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-1
- Release 2.4.0
- Drop obsolete patch
- Rebuild on epel7 (rhbz#1647989)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.0-8
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-6
- Rebuild for sundials-3.0.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.0-3
- Perl 5.26 rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun May 07 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Wed Mar 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2.6-7
- Rebuild for sundials-2.7.0-10

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.6-5
- Rebuild for sundials-2.7.0-7

* Tue Oct 25 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.6-4
- Rebuild for sundials-2.7.0-6

* Sun Oct 16 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.6-3
- Rebuild for libsundials (#1384636)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.6-2
- Perl 5.24 rebuild

* Thu Feb 11 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 2.2.6-1
- Update to latest version
- Fix gcc6 compilation issue (#1306648)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.5-6
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.5-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.5-4
- Rebuilt for sundials 2.6.0.

* Thu Feb 26 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/GCC5 (#1195309)

* Sun Nov 30 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.5-2
- Drop dependency on compat f77, it is not needed.

* Fri Nov 21 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.5-1
- Initial packaging.
