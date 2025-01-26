%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif
%bcond_without mpich

%global sover 4.13

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif

Name:       gmsh
Summary:    A three-dimensional finite element mesh generator
Version:    4.13.2
Release:    6%{?dist}
# MPI not available on i686
ExcludeArch: %{ix86}

# gmsh is GPL-2.0-or-later WITH Gmsh-exception, see LICENSE.txt
# contrib/{DiscreteIntegration, HighOrderMeshOptimizer, MeshOptimizer, onelab} are MIT, see respective README.txt
License:    GPL-2.0-or-later WITH Gmsh-exception AND MIT
URL:        http://geuz.org/gmsh/
# Download source from http://geuz.org/gmsh/src/%%{name}-%%{version}-source.tgz
# Delete contrib/blossom and contrib/mpeg_encode from source archive
Source0:    %{name}-%{version}-source-fedora.tar.xz
Source1:    %{name}.desktop

# Install onelab.py and gmsh.py into the python site-packages directory
Patch0:     gmsh_python.patch
# Adapt med.h include path
Patch1:     gmsh_med.patch
# Install Julia API to share/gmsh
Patch2:     gmsh_julia.patch
# Remove odd install of gmsh shared library
Patch3:     gmsh_install.patch
# Fix build error caused by include ordering
Patch4:     gmsh_build.patch
# Unbundle gl2ps
Patch5:     gmsh_unbundle_gl2ps.patch
# Header fix for GCC 13
Patch6:     gmsh-cstdint.patch
# Fix incompatible size_t* -> uint64_t* conversions
Patch7:     gmsh_uint64.patch

BuildRequires: alglib-devel
BuildRequires: ann-devel
%if %{with flexiblas}
BuildRequires:  flexiblas-devel
%else
BuildRequires:  blas-devel, lapack-devel
%endif
BuildRequires: eigen3-devel
BuildRequires: cgnslib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fltk-devel
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: gmm-devel
BuildRequires: gmp-devel
BuildRequires: hdf5-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: liblbfgs-devel
BuildRequires: libpng-devel
BuildRequires: make
BuildRequires: mathex-devel
BuildRequires: med-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: metis-devel
BuildRequires: netgen-mesher-devel-private
BuildRequires: opencascade-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: voro++-devel
BuildRequires: zlib-devel
BuildRequires: texinfo
# For transforming icon
BuildRequires: ImageMagick

Provides:      bundled(netgen-mesher) = svn469


Requires:       %{name}-common = %{version}-%{release}

%description
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor. Its design goal is to provide a fast, light and
user-friendly meshing tool with parametric input and advanced
visualization capabilities. Gmsh is built around four modules:
geometry, mesh, solver and post-processing. The specification of any
input to these modules is done either interactively using the
graphical user interface or in ASCII text files using Gmsh's own scripting
language.

%package common
Summary:        Common files for %{name}
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description common
Common files for %{name}.


%package libs
Summary:        Libraries provided by %{name}


%description libs
Libraries provided by %{name}. These libraries are not required for
the base %{name} package and are used for development only.


%package -n python3-%{name}
Summary:        Python3 API for %{name}
%{?python_provide:%python_provide python3-%{name}}
Obsoletes:      python3-%{name}-private

BuildArch:      noarch

Requires:       %{name}-libs = %{version}-%{release}

%description -n python3-%{name}
Python3 API for %{name}.


%package devel
Summary:        Development with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-devel-private

%description devel
Header files for development with %{name}.


%package doc
Summary:        Documentation, demos and tutorials for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation, demo projects and tutorials for %{name}.

###############################################################################

%if %{with openmpi}
%package        openmpi
Summary:        %{name} compiled against openmpi
BuildRequires:  openmpi-devel
BuildRequires:  netgen-mesher-openmpi-devel
BuildRequires:  hdf5-openmpi-devel
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description    openmpi
%{name} compiled against openmpi.


%package        openmpi-libs
Summary:        %{name} libraries compiled against openmpi

%description    openmpi-libs
%{name} libraries compiled against openmpi.


%package        openmpi-devel
Summary:        Development files for %{name} compiled against openmpi
# Require explicitly for dir ownership
Requires:       openmpi-devel
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-openmpi-devel-private

%description    openmpi-devel
Development files for %{name} compiled against openmpi.
%endif

###############################################################################

%if %{with mpich}
%package        mpich
Summary:        %{name} compiled against mpich
BuildRequires:  mpich-devel
BuildRequires:  netgen-mesher-mpich-devel
BuildRequires:  hdf5-mpich-devel
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-mpich-libs%{?_isa} = %{version}-%{release}

%description    mpich
%{name} compiled against mpich.


%package        mpich-libs
Summary:        %{name} libraries compiled against mpich

%description    mpich-libs
%{name} libraries compiled against mpich.


%package        mpich-devel
Summary:        Development files for %{name} compiled against mpich
# Require explicitly for dir ownership
Requires:       mpich-devel
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-mpich-devel-private

%description    mpich-devel
Development files for %{name} compiled against mpich.
%endif

###############################################################################

%prep
%autosetup -p1 -n %{name}-%{version}-source

# Copy these outside the contrib folder
cp contrib/Netgen/nglib_gmsh.h contrib/Netgen/nglib_gmsh.cpp src/mesh

# Bamg: part of freefem++, modified source code
# DiscreteIntegration: gmsh internal module
# HighOrderMeshOptimizer: gmsh internal module
# hxt: see contrib/hxt/CREDITS.txt
# kbipack: Source not available on the net anymore
# onelab: gmsh internal module
(
cd contrib;
ls -1 | \
    grep -v ^bamg$ | \
    grep -v ^DiscreteIntegration$ | \
    grep -v ^MeshOptimizer$ | \
    grep -v ^HighOrderMeshOptimizer$ | \
    grep -v ^QuadTri$ | \
    grep -v ^hxt$ | \
    grep -v ^kbipack$ | \
    grep -v ^onelab$ | \
xargs rm -rf
)


%build
# mpeg not in fedora due to patent issues
# blossoms is nonfree, see contrib/blossoms/README.txt

gmsh_cmake_args="\
    %{?with_flexiblas:-DBLA_VENDOR=FlexiBLAS} \
    -DENABLE_SYSTEM_CONTRIB=YES \
    -DENABLE_BUILD_LIB=YES \
    -DENABLE_BUILD_SHARED=YES \
    -DENABLE_BUILD_DYNAMIC=YES \
    -DENABLE_MPEG_ENCODE=NO \
    -DENABLE_METIS=YES \
    -DENABLE_BLOSSOM=NO \
    -DENABLE_CGNS=YES \
    -DENABLE_MED=YES \
    -DENABLE_EIGEN=YES \
    -DEIGEN_INC=%{_includedir}/eigen3 \
    -DENABLE_OCC=YES"

### serial version ###
%define _vpath_builddir %{_target_platform}
%cmake .. \
    -DENABLE_OPENMP=ON \
    $gmsh_cmake_args

%cmake_build

### openmpi version ###
%if %{with openmpi}
%{_openmpi_load}
export CXX=mpicxx
%define _vpath_builddir %{_target_platform}-openmpi
%cmake .. \
    -DENABLE_MPI=YES \
    -DCMAKE_INSTALL_BINDIR=$MPI_BIN \
    -DCMAKE_INSTALL_LIBDIR=$MPI_LIB \
    -DCMAKE_INSTALL_INCLUDEDIR=$MPI_INCLUDE \
    $gmsh_cmake_args

%cmake_build
%{_openmpi_unload}
%endif

### mpich version ###
%if %{with mpich}
%{_mpich_load}
export CXX=mpicxx
%define _vpath_builddir %{_target_platform}-mpich
%cmake .. \
    -DENABLE_MPI=YES \
    -DCMAKE_INSTALL_BINDIR=$MPI_BIN \
    -DCMAKE_INSTALL_LIBDIR=$MPI_LIB \
    -DCMAKE_INSTALL_INCLUDEDIR=$MPI_INCLUDE \
    $gmsh_cmake_args

%cmake_build
%{_mpich_unload}
%endif

# Built html documentation
make -C %{_target_platform} html

# Fix to create correct debuginfo
cp -a src/parser/Gmsh.* %{_target_platform}
%if %{with openmpi}
cp -a src/parser/Gmsh.* %{_target_platform}-openmpi
%endif
%if %{with mpich}
cp -a src/parser/Gmsh.* %{_target_platform}-mpich
%endif


%install
%if %{with openmpi}
%define _vpath_builddir %{_target_platform}-openmpi
%cmake_install
%endif
%if %{with mpich}
%define _vpath_builddir %{_target_platform}-mpich
%cmake_install
%endif
%define _vpath_builddir %{_target_platform}
%cmake_install

# Remove static libraries
find %{buildroot} -type f -name libgmsh.a -exec rm -f {} \;

# Install icon and .desktop file
convert -scale 128 utils/icons/gmsh.png icon_128x128.png
install -Dpm 0644 icon_128x128.png  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install License.txt via %%license
rm -f %{buildroot}%{_defaultdocdir}/%{name}/LICENSE.txt


%files common
%doc %{_defaultdocdir}/%{name}/CREDITS.txt
%doc %{_defaultdocdir}/%{name}/README.txt
%doc %{_defaultdocdir}/%{name}/CHANGELOG.txt
%license LICENSE.txt
%{_mandir}/man1/gmsh.1.gz
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{python3_sitelib}/onelab.py
%{python3_sitelib}/__pycache__/onelab.*

%files doc
%license LICENSE.txt
%doc %{_defaultdocdir}/%{name}/tutorials
%doc %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/%{name}.html
%doc %{_defaultdocdir}/%{name}/images/

%files
%{_bindir}/%{name}

%files devel
%{_includedir}/gmsh.h
%{_includedir}/gmshc.h
%{_includedir}/gmsh.h_cwrap
%{_includedir}/gmsh.f90
%{_libdir}/libgmsh.so

%files libs
%license LICENSE.txt
%{_libdir}/libgmsh.so.%{sover}*

%files -n python3-%{name}
%{python3_sitelib}/gmsh.py
%{python3_sitelib}/__pycache__/gmsh.*.pyc
%{python3_sitelib}/gmsh-%{version}*.dist-info/

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/%{name}

%files openmpi-devel
%{_includedir}/openmpi*/gmsh.h
%{_includedir}/openmpi*/gmshc.h
%{_includedir}/openmpi*/gmsh.h_cwrap
%{_includedir}/openmpi*/gmsh.f90
%{_libdir}/openmpi/lib/libgmsh.so

%files openmpi-libs
%license LICENSE.txt
%{_libdir}/openmpi/lib/libgmsh.so.%{sover}*
%endif

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/%{name}

%files mpich-devel
%{_includedir}/mpich*/gmsh.h
%{_includedir}/mpich*/gmshc.h
%{_includedir}/mpich*/gmsh.h_cwrap
%{_includedir}/mpich*/gmsh.f90
%{_libdir}/mpich/lib/libgmsh.so

%files mpich-libs
%license LICENSE.txt
%{_libdir}/mpich/lib/libgmsh.so.%{sover}*
%endif


%changelog
* Fri Jan 24 2025 Sandro Mani <manisandro@gmail.com> - 4.13.2-6
- Rebuild (cgnslib)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 4.13.2-4
- Rebuild for hdf5 1.14.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 4.13.2-2
- Rebuilt for Python 3.13

* Tue Jun 04 2024 Sandro Mani <manisandro@gmail.com> - 4.13.2-1
- Update to 4.13.2

* Sun Jun 02 2024 Richard Shaw <hobbes1069@gmail.com> - 4.13.1-2
- Rebuild for opencascade 7.8.1.

* Wed May 08 2024 Sandro Mani <manisandro@gmail.com> - 4.13.1-1
- Update to 4.13.1

* Tue Apr 09 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 4.13.0-3
- Ensure python3-gmsh depends on gmsh-libs
- Make the python3-gmsh subpackage noarch, since the bindings are pure Python

* Fri Mar 29 2024 Richard Shaw <hobbes1069@gmail.com> - 4.13.0-2
- Rebuild for OpenCascade 7.8.0.

* Tue Feb 27 2024 Sandro Mani <manisandro@gmail.com> - 4.13.0-1
- Update to 4.13.0

* Tue Jan 23 2024 Sandro Mani <manisandro@gmail.com> - 4.12.2-1
- Update to 4.12.2

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 14 2024 Sandro Mani <manisandro@gmail.com> - 4.12.1-1
- Update to 4.12.1

* Mon Jan 01 2024 Sandro Mani <manisandro@gmail.com> - 4.12.0-1
- Update to 4.12.0

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 4.11.1-7
- Rebuild for openmpi 5.0.0, drops i686 and C++ API

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Sandro Mani <manisandro@gmail.com> - 4.11.1-5
- Rebuild (cgnslib)

* Sat Jun 17 2023 Python Maint <python-maint@redhat.com> - 4.11.1-4
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Richard Shaw <hobbes1069@gmail.com> - 4.11.1-2
- Rebuild for opencascade.

* Wed Dec 21 2022 Sandro Mani <manisandro@gmail.com> - 4.11.1-1
- Update to 4.11.1

* Tue Nov 08 2022 Sandro Mani <manisandro@gmail.com> - 4.11.0-1
- Update to 4.11.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Sandro Mani <manisandro@gmail.com> - 4.10.5-1
- Update to 4.10.5

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 4.10.4-2
- Rebuilt for Python 3.11

* Sun Jun 19 2022 Sandro Mani <manisandro@gmail.com> - 4.10.4-1
- Update to 4.10.4

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.10.3-2
- Rebuilt for Python 3.11

* Mon May 30 2022 Sandro Mani <manisandro@gmail.com> - 4.10.3-1
- Update to 4.10.3

* Fri May 13 2022 Sandro Mani <manisandro@gmail.com> - 4.10.2-1
- Update to 4.10.2

* Mon May 09 2022 Sandro Mani <manisandro@gmail.com> - 4.10.1-2
- Fix removing bundled libraries

* Tue May 03 2022 Sandro Mani <manisandro@gmail.com> - 4.10.1-1
- Update to 4.10.1

* Tue Apr 26 2022 Sandro Mani <manisandro@gmail.com> - 4.10.0-1
- Update to 4.10.0

* Tue Mar 22 2022 Sandro Mani <manisandro@gmail.com> - 4.9.5-2
- Rebuild for cgnslib-4.3.0

* Mon Feb 21 2022 Richard Shaw <hobbes1069@gmail.com> - 4.9.5-1
- Update to 4.9.5.

* Fri Feb 04 2022 Sandro Mani <manisandro@gmail.com> - 4.9.4-1
- Update to 4.9.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Sandro Mani <manisandro@gmail.com> - 4.9.3-1
- Update to 4.9.3

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 4.9.2-1
- Update to 4.9.2.

* Sat Dec 18 2021 Richard Shaw <hobbes1069@gmail.com> - 4.9.1-1
- Update to 4.9.1.

* Fri Dec 03 2021 Richard Shaw <hobbes1069@gmail.com> - 4.9.0-1
- Update to 4.9.0.

* Wed Oct 27 2021 Sandro Mani <manisandro@gmail.com> - 4.8.4-6
- Rebuild (alglib)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 4.8.4-4
- Properly set BLA_VENDOR to FlexiBLAS for cmake >= 3.19

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.8.4-3
- Rebuilt for Python 3.10

* Thu Apr 29 2021 Sandro Mani <manisandro@gmail.com> - 4.8.4-2
- Rebuild (cgnslib)

* Thu Apr 29 2021 Sandro Mani <manisandro@gmail.com> - 4.8.4-1
- Update to 4.8.4

* Tue Apr 06 2021 Sandro Mani <manisandro@gmail.com> - 4.8.3-1
- Update to 4.8.3

* Mon Mar 29 2021 Sandro Mani <manisandro@gmail.com> - 4.8.2-1
- Update to 4.8.2

* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 4.8.1-1
- Update to 4.8.1

* Tue Mar 02 2021 Sandro Mani <manisandro@gmail.com> - 4.8.0-1
- Update to 4.8.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Richard Shaw <hobbes1069@gmail.com> - 4.7.1-1
- Update to 4.7.1.

* Sun Nov 08 2020 Richard Shaw <hobbes1069@gmail.com> - 4.7.0-1
- Update to 4.7.0.

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.6.0-5
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 21:40:30 GMT 2020 Sandro Mani <manisandro@gmail.com> - 4.6.0-4
- Rebuild (med)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 4.6.0-2
- Use __cmake_in_source_build

* Mon Jul 13 2020 Sandro Mani <manisandro@gmail.com> - 4.6.0-1
- Update to 4.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.5.6-4
- Rebuilt for Python 3.9

* Fri May 08 2020 Richard Shaw <hobbes1069@gmail.com> - 4.5.6-3
- Rebuild for unannounced soname bump in libcgns.

* Mon Apr 06 2020 Sandro Mani <manisandro@gmail.com> - 4.5.6-2
- Unbundle gl2ps (#1821461)

* Mon Mar 30 2020 Sandro Mani <manisandro@gmail.com> - 4.5.6-1
- Update to 4.5.6

* Sat Mar 21 2020 Sandro Mani <manisandro@gmail.com> - 4.5.5-1
- Update to 4.5.5

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 4.5.4-1
- Update to 4.5.4

* Sat Feb 22 2020 Sandro Mani <manisandro@gmail.com> - 4.5.3-1
- Update to 4.5.3

* Fri Feb 21 2020 Sandro Mani <manisandro@gmail.com> - 4.5.2-3
- Rebuild (cgnslib)

* Mon Feb 17 2020 Sandro Mani <manisandro@gmail.com> - 4.5.2-2
- Rebuild (cgnslib)

* Thu Jan 30 2020 Richard Shaw <hobbes1069@gmail.com> - 4.5.2-1
- Update to 4.5.2.
- Update install patch to correctly set RPATH for binaries and libraries.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 Sandro Mani <manisandro@gmail.com> - 4.5.1-1
- Update to 4.5.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.1-2
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Sandro Mani <manisandro@gmail.com> - 4.4.1-1
- Update to 4.4.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Sandro Mani <manisandro@gmail.com> - 4.4.0-1
- Update to 4.4.0

* Fri Apr 19 2019 Sandro Mani <manisandro@gmail.com> - 4.3.0-1
- Update to 4.3.0

* Thu Apr 04 2019 Sandro Mani <manisandro@gmail.com> - 4.2.3-1
- Update to 4.2.3

* Thu Mar 21 2019 Sandro Mani <manisandro@gmail.com> - 4.2.2-2
- Cleanup spec, drop references to non existing contrib modules
- Enable MeshOptimizer, QuadTri
- Clarify license

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for hdf5 1.10.5

* Wed Mar 13 2019 Sandro Mani <manisandro@gmail.com> - 4.2.2-1
- Update to 4.2.2

* Tue Mar 12 2019 Sandro Mani <manisandro@gmail.com> - 4.2.1-3
- Rebuild (cgnslib)

* Mon Mar 11 2019 Sandro Mani <manisandro@gmail.com> - 4.2.1-2
- Drop private API packages by upstream request
- Enable OpenMP in serial version
- Cleanup BuildRequires

* Thu Mar 07 2019 Sandro Mani <manisandro@gmail.com> - 4.2.1-1
- Update to 4.2.1

* Wed Mar 06 2019 Sandro Mani <manisandro@gmail.com> - 4.2.0-1
- Update to 4.2.0

* Sat Feb 23 2019 Sandro Mani <manisandro@gmail.com> - 4.1.5-2
- Rebuild (alglib)

* Fri Feb 15 2019 Sandro Mani <manisandro@gmail.com> - 4.1.5-1
- Update to 4.1.5

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 4.1.4-2
- Rebuild for openmpi 3.1.3

* Mon Feb 04 2019 Sandro Mani <manisandro@gmail.com> - 4.1.4-1
- Update to 4.1.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Sandro Mani <manisandro@gmail.com> - 4.1.3-1
- Update to 4.1.3

* Tue Jan 22 2019 Sandro Mani <manisandro@gmail.com> - 4.1.2-1
- Update to 4.1.2

* Sun Jan 20 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.1-1
- Update to 4.1.1.

* Mon Jan 14 2019 Sandro Mani <manisandro@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Mon Dec 10 2018 Sandro Mani <manisandro@gmail.com> - 4.0.7-1
- Update to 4.0.7

* Sun Nov 25 2018 Sandro Mani <manisandro@gmail.com> - 4.0.6-1
- Update to 4.0.6

* Fri Nov 16 2018 Sandro Mani <manisandro@gmail.com> - 4.0.5-1
- Update to 4.0.5

* Mon Oct 22 2018 Sandro Mani <manisandro@gmail.com> - 4.0.4-1
- Update to 4.0.4

* Thu Sep 27 2018 Sandro Mani <manisandro@gmail.com> - 4.0.2-1
- Update to 4.0.2

* Mon Sep 10 2018 Sandro Mani <manisandro@gmail.com> - 4.0.1-1
- Update to 4.0.1

* Thu Aug 23 2018 Sandro Mani <manisandro@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.6-10
- Rebuilt for Python 3.7

* Sun Jul 01 2018 Sandro Mani <manisandro@gmail.com> - 3.0.6-9
- Rebuild (alglib)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.6-8
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Sandro Mani <manisandro@gmail.com> - 3.0.6-7
- Rebuild (mmg3d)

* Sat Mar 10 2018 Sandro Mani <manisandro@gmail.com> - 3.0.6-6
- Rebuild (med)

* Wed Mar 07 2018 Sandro Mani <manisandro@gmail.com> - 3.0.6-5
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Sandro Mani <manisandro@gmail.com> - 3.0.6-3
- Rebuild (alglib)

* Tue Dec 12 2017 Sandro Mani <manisandro@gmail.com> - 3.0.6-2
- Enable python3 bindings

* Sun Nov 05 2017 Sandro Mani <manisandro@gmail.com> - 3.0.6-1
- Update to 3.0.6

* Thu Sep 07 2017 Sandro Mani <manisandro@gmail.com> - 3.0.5-1
- Update to 3.0.5

* Thu Aug 24 2017 Sandro Mani <manisandro@gmail.com> - 3.0.4-2
- Rebuild (alglib)

* Mon Jul 31 2017 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Sandro Mani <manisandro@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun May 14 2017 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Fri May 12 2017 Sandro Mani <manisandro@gmail.com> - 3.0.1-2
- Rebuild (alglib)

* Thu May 11 2017 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Thu May 11 2017 Richard Shaw <hobbes1069@gmail.com> - 2.16.0-3
- Rebuild for OCE 0.18.1 and updated netgen-mesher.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Sandro Mani <manisandro@gmail.com> - 2.16.0-1
- Update to 2.16.0

* Sun Dec 04 2016 Sandro Mani <manisandro@gmail.com> - 2.15.0-1
- Update to 2.15.0

* Sun Oct 30 2016 Sandro Mani <manisandro@gmail.com> - 2.14.1-1
- Update to 2.14.1

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.14.0-2
- Rebuild for openmpi 2.0

* Mon Oct 10 2016 Sandro Mani <manisandro@gmail.com> - 2.14.0-1
- Update to 2.14.0

* Thu Aug 18 2016 Sandro Mani <manisandro@gmail.com> - 2.13.2-1
- Update to 2.13.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 17 2016 Sandro Mani <manisandro@gmail.com> - 2.13.1-1
- Update to 2.13.1

* Tue Jul 12 2016 Sandro Mani <manisandro@gmail.com> - 2.13.0-1
- Update to 2.13.0

* Fri Jul 01 2016 Sandro Mani <manisandro@gmail.com> - 2.12.0-3
- Rebuild (cgnslib)

* Thu Apr  7 2016 Richard Shaw <hobbes109@gmail.com> - 2.12.0-2
- Rebuild for updated OCE.

* Sun Mar 06 2016 Sandro Mani <manisandro@gmail.com> - 2.12.0-1
- Update to 2.12.0

* Thu Feb 04 2016 Sandro Mani <manisandro@gmail.com> - 2.11.0-3
- Add gmsh_narrowing-conversion.patch

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 08 2015 Sandro Mani <manisandro@gmail.com> - 2.11.0-1
- Update to 2.11.0

* Wed Sep 16 2015 Orion Poplawski <orion@cora.nwra.com> - 2.10.1-4
- Rebuild for openmpi 1.10.0

* Sat Aug 22 2015 Sandro Mani <manisandro@gmail.com> - 2.10.1-3
- Rebuild (alglib)

* Thu Aug 13 2015 Sandro Mani <manisandro@gmail.com> - 2.10.1-2
- Rebuild for RPM MPI Requires Provides Change
- Fix build

* Sat Aug 08 2015 Sandro Mani <manisandro@gmail.com> - 2.10.1-1
- Update to 2.10.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May  3 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.9.3-2
- Rebuild for changed mpich

* Sat Apr 18 2015 Sandro Mani <manisandro@gmail.com> - 2.9.3-1
- Update to 2.9.3

* Tue Mar 31 2015 Sandro Mani <manisandro@gmail.com> - 2.9.2-1
- Update to 2.9.2

* Wed Mar 18 2015 Sandro Mani <manisandro@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Sat Mar 14 2015 Sandro Mani <manisandro@gmail.com> - 2.9.0-1
- Update to 2.9.0
- Use %%license
- Fix -Wl,--as-needed clearing default LDFLAGS

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.5-8
- rebuild (fltk)

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.8.5-7
- Rebuild for hdf5 1.8.14

* Sat Dec 13 2014 Sandro Mani <manisandro@gmail.com> - 2.8.5-6
- Rebuild (alglib)

* Tue Oct 07 2014 Sandro Mani <manisandro@gmail.com> - 2.8.5-5
- Rebuild (netgen-mesher)

* Sat Sep 06 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.5-4
- rebuild (gmm)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Sandro Mani <manisandro@gmail.com> - 2.8.5-2
- Rebuild (OCE)

* Wed Jul 23 2014 Sandro Mani <manisandro@gmail.com> - 2.8.5-1
- Update to 2.8.5
- Fix -doc requires
- Rebase patches

* Tue Jul 22 2014 Sandro Mani <manisandro@gmail.com> - 2.8.4-4
- Rename gmsh-demos to gmsh-doc
- Fix scriptlets for gmsh-common
- Install license file with *-libs subpackages

* Thu Jul 17 2014 Sandro Mani <manisandro@gmail.com> - 2.8.4-3
- Fix encoding of file tutorial/t12.geo
- Fix line endings of demos/component8.step
- Fix incorrect changelog
- Add -Wl,--as-needed
- Add BRs: cgnslib-devel med-devel
- Pass -DENABLE_CGNS=YES -DENABLE_MED=YES to cmake
- Install onelab.py in %%{python2_sitelib}
- Add missing Requires: gmsh-common

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 2.8.4-2
- Link executable against library
- Compile with mpi support

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 2.8.4-1
- Update to 2.8.3
- Update/add patches for unbundling libraries
- Spec cleanup, add missing scriptlets

* Mon Jan 23 2012 Alexey Vasyukov <vasyukov@gmail.com> - 2.5.0-6
- Add script to remove prohibited code completely from sources
- Do not set CMake flags because they are set in CMakeLists.txt by the script now

* Mon Nov 14 2011 Alexey Vasyukov <vasyukov@gmail.com> - 2.5.0-5
- Disable MPEG support because of patent issues
- Add patch to use system ANN instead of built-in one
- Add patch to use system GMM instead of built-in one
- Update CMake soname patch to avoid hardcoded numbers

* Sun Nov 13 2011 Alexey Vasyukov <vasyukov@gmail.com> - 2.5.0-4
- Add patch for API demo to make it usable

* Sun Nov 13 2011 Alexey Vasyukov <vasyukov@gmail.com> - 2.5.0-3
- Add desktop files

* Sat Nov 12 2011 Alexey Vasyukov <vasyukov@gmail.com> - 2.5.0-2
- Break into subpackages

* Thu Nov 10 2011 Alexey Vasyukov <vasyukov@gmail.com> - 2.5.0-1
- Initial build for Fedora
