%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

# Don't abort on compilation errors of the example python snippets
%global _python_bytecompile_errors_terminate_build 0

%if 0%{?el6}
	%ifarch ppc64
		%global build_mpich 0
	%else
		%global build_mpich 1
	%endif
%else
	%global build_mpich 1
%endif

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%global build_openmpi 0
%global build_mpich   0
%else
%global build_openmpi 1
%endif
%else
%global build_openmpi 1
%endif

Name:           netgen-mesher
# Also update version in netgen_fallback-version.patch!
Version:        6.2.2406
Release:        2%{?dist}
Summary:        Automatic mesh generation tool
ExcludeArch:    %{ix86}

License:        LGPL-2.0-only
URL:            https://github.com/NGSolve/netgen
Source0:        https://github.com/NGSolve/netgen/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        netgen-mesher.png
Source2:        netgen-mesher.desktop
# Source99:       https://raw.githubusercontent.com/NGSolve/pybind11/7ec2ddfc95f65d1e986d359466a6c254aa514ef3/tools/pybind11Tools.cmake
# Source100:      https://raw.githubusercontent.com/NGSolve/pybind11/7ec2ddfc95f65d1e986d359466a6c254aa514ef3/tools/FindPythonLibsNew.cmake

# Rename shared libaries (the original names are often way too generic), add library version
Patch1:         0002-Rename-libraries-add-library-versions.patch
# Make some includes relative (needed for when headers are in -private subpackage)
Patch2:         0004-Make-some-includes-relative.patch
# Rename binary in cmake so that exported modules work correctly
Patch3:         0010-rename-netgen-binary.patch
# Link against libjpeg
Patch4:         netgen_libjpeg.patch
# Fix fallback version
# See https://bugzilla.redhat.com/show_bug.cgi?id=1993574#c11
Patch5:         netgen_fallback-version.patch
# Fix Status typedef symbol collision by re-ordering includes
# /usr/include/mpich-x86_64/mpicxx.h:160:18: error: expected identifier before ‘int’
#   160 |     friend class Status;
Patch6:         netgen_include-order.patch
# Fix invalid egg-info version
Patch7:         netgen-mesher_egg-info-version.patch


BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  tk-devel
BuildRequires:  opencascade-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  metis-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libXmu-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  pybind11-devel
BuildRequires:  git

# Bundles a modified version of togl-2.1
Provides: bundled(tcl-togl) = 2.1


Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input from
constructive solid geometry (CSG) or boundary representation (BRep) from STL
file format. The connection to a geometry kernel allows the handling of IGES
and STEP files. NETGEN contains modules for mesh optimization and hierarchical
mesh refinement.

%package        common
Summary:        Common files for netgen
Requires:       hicolor-icon-theme
Requires:       tix
BuildArch:      noarch

%description    common
Common files for netgen.

%package        libs
Summary:        Netgen libraries

%description    libs
Netgen libraries.

%package        devel
Summary:        Development files for netgen
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for netgen.

%package        devel-private
Summary:        Private headers of netgen
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    devel-private
Private headers of netgen, needed to build certain netgen based software
packages.

%package -n     python3-%{name}
Summary:        Python3 interface for netgen
%{?python_provide:%python_provide python3-netgen}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python3 interface for netgen.

###############################################################################

%if %{build_openmpi}
%package        openmpi
Summary:        Netgen compiled against openmpi
BuildRequires:  environment-modules
BuildRequires:  openmpi-devel
BuildRequires:  python3-mpi4py-openmpi
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description    openmpi
Netgen compiled against openmpi.

%package        openmpi-libs
Summary:        Netgen libraries compiled against openmpi

%description    openmpi-libs
Netgen libraries compiled against openmpi.

%package        openmpi-devel
Summary:        Development files for Netgen compiled against openmpi
# Require explicitly for dir ownership
Requires:       openmpi-devel
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}

%description    openmpi-devel
Development files for Netgen compiled against openmpi.

%package -n     python3-%{name}-openmpi
Summary:        Python3 interface for netgen compiled against openmpi
%{?python_provide:%python_provide python3-netgen-openmpi}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-openmpi
Python3 interface for netgen compiled against openmpi.

%endif

###############################################################################

%if %{build_mpich}
%package        mpich
Summary:        Netgen compiled against mpich
BuildRequires:  environment-modules
BuildRequires:  mpich-devel
BuildRequires:  python3-mpi4py-mpich
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-mpich-libs%{?_isa} = %{version}-%{release}

%description    mpich
Netgen compiled against mpich.

%package        mpich-libs
Summary:        Netgen libraries compiled against mpich

%description    mpich-libs
Netgen libraries compiled against mpich.

%package        mpich-devel
Summary:        Development files for Netgen compiled against mpich
# Require explicitly for dir ownership
Requires:       mpich-devel
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}

%description    mpich-devel
Development files for Netgen compiled against mpich.

%package -n     python3-%{name}-mpich
Summary:        Python3 interface for netgen compiled against mpich
%{?python_provide:%python_provide python3-netgen-mpich}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-mpich
Python3 interface for netgen compiled against mpich.

%endif

###############################################################################

%prep
%autosetup -p1 -n netgen-%{version}

# Pull in minimal cmake files from NGSolv pybind11 project to make this one happy.
# install -pm 0744 %{SOURCE99} cmake/
# install -pm 0744 %{SOURCE100} cmake/cmake_modules/


%build
### serial version ###
%define _vpath_builddir %{_target_platform}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DNG_INSTALL_SUFFIX=netgen_mesher \
  -DUSE_NATIVE_ARCH=OFF \
  -DUSE_SUPERBUILD=OFF \
  -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/%{name} \
  -DNG_INSTALL_DIR_LIB=%{_libdir} \
  -DNG_INSTALL_DIR_CMAKE=%{_libdir}/cmake/%{name} \
  -DNG_INSTALL_DIR_PYTHON=%{python3_sitearch} \
  -DPREFER_SYSTEM_PYBIND11=ON \
  -DUSE_JPEG=1 -DUSE_OCC=1 \
  -DOpenGL_GL_PREFERENCE=GLVND
%cmake_build

### openmpi version ###
%if %{build_openmpi}
%define _vpath_builddir %{_target_platform}-openmpi
%{_openmpi_load}
export CXX=mpicxx
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DNG_INSTALL_SUFFIX=netgen_mesher \
  -DUSE_NATIVE_ARCH=OFF \
  -DUSE_SUPERBUILD=OFF \
  -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/openmpi/%{name} \
  -DNG_INSTALL_DIR_BIN=%{_libdir}/openmpi/bin/ \
  -DNG_INSTALL_DIR_LIB=%{_libdir}/openmpi/lib/ \
  -DNG_INSTALL_DIR_CMAKE=%{_libdir}/openmpi/lib/cmake/%{name} \
  -DNG_INSTALL_DIR_PYTHON=%{_libdir}/openmpi/python%{python3_version}/site-packages \
  -DPREFER_SYSTEM_PYBIND11=ON \
  -DUSE_JPEG=1 -DUSE_OCC=1 -DUSE_MPI=1
%cmake_build
%{_openmpi_unload}
%endif

### mpich version ###
%if %{build_mpich}
%define _vpath_builddir %{_target_platform}-mpich
%{_mpich_load}
export CXX=mpicxx
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DNG_INSTALL_SUFFIX=netgen_mesher \
  -DUSE_NATIVE_ARCH=OFF \
  -DUSE_SUPERBUILD=OFF \
  -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/mpich/%{name} \
  -DNG_INSTALL_DIR_BIN=%{_libdir}/mpich/bin/ \
  -DNG_INSTALL_DIR_LIB=%{_libdir}/mpich/lib/ \
  -DNG_INSTALL_DIR_CMAKE=%{_libdir}/mpich/lib/cmake/%{name} \
  -DNG_INSTALL_DIR_PYTHON=%{_libdir}/mpich/python%{python3_version}/site-packages \
  -DPREFER_SYSTEM_PYBIND11=ON \
  -DUSE_JPEG=1 -DUSE_OCC=1 -DUSE_MPI=1
%cmake_build
%{_mpich_unload}
%endif


%install
%define writepkgconfig() \
install -d -m 0755 %{buildroot}/$MPI_LIB/pkgconfig; \
cat > %{buildroot}/$MPI_LIB/pkgconfig/%{name}.pc << EOF\
prefix=%{_prefix}\
exec_prefix=${prefix}\
libdir=$MPI_LIB\
includedir=$MPI_INCLUDE/%{name}\
\
Name: %{name}\
Description:  %{summary}\
Version: %{version}\
Libs: -L\\\${libdir} -lnglib\
Libs.private: -lngcgs -lnggeom2d -lngmesh -lngocc -lngstl\
Cflags: -I\\\${includedir}\
EOF\
%{nil}

### openmpi version ###
%if %{build_openmpi}
%define _vpath_builddir %{_target_platform}-openmpi
%{_openmpi_load}
%cmake_install
%writepkgconfig
%{_openmpi_unload}
%endif

### mpich version ###
%if %{build_mpich}
%define _vpath_builddir %{_target_platform}-mpich
%{_mpich_load}
%cmake_install
%writepkgconfig
%{_mpich_unload}
%endif

### serial version ###
%define _vpath_builddir %{_target_platform}
%cmake_install
export MPI_LIB=%{_libdir}
export MPI_INCLUDE=%{_includedir}
%writepkgconfig

# Install icon and desktop file
install -Dpm 0644 %SOURCE1 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install --dir %{buildroot}/%{_datadir}/applications/ %SOURCE2

# Delete the doc folder, the files are in %%doc below
rm -rf %{buildroot}/%{_prefix}/doc

# Install private headers
(
cd libsrc
find \( -name *.hpp -or -name *.hxx -or -name *.h -or -name *.ixx -or -name *.jxx \) -exec install -Dpm 0644 {} %{buildroot}%{_includedir}/%{name}/private/{} \;
)

# Install the nglib.h header
install -Dpm 0644 nglib/nglib.h %{buildroot}%{_includedir}/%{name}/nglib.h

# R


%files common
%doc AUTHORS doc/ng4.pdf
%license LICENSE
%{_datadir}/netgen_mesher/
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/netgen-mesher

%files libs
%{_libdir}/libngcore.so.6.2
%{_libdir}/libnggui.so.6.2
%{_libdir}/libnglib.so.6.2

%files devel
%{_includedir}/%{name}
%exclude %{_includedir}/%{name}/private
%{_libdir}/libngcore.so
%{_libdir}/libnggui.so
%{_libdir}/libnglib.so
%{_libdir}/libngtogl.a
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*

%files devel-private
%{_includedir}/%{name}/private

%files -n python3-%{name}
%{python3_sitearch}/pyngcore/
%{python3_sitearch}/netgen_mesher/
%{python3_sitearch}/netgen_mesher-py3.egg-info

%if %{build_openmpi}
%files openmpi
%{_libdir}/openmpi/bin/netgen-mesher

%files openmpi-libs
%{_libdir}/openmpi/lib/libngcore.so.6.2
%{_libdir}/openmpi/lib/libnggui.so.6.2
%{_libdir}/openmpi/lib/libnglib.so.6.2

%files openmpi-devel
%{_includedir}/openmpi*/%{name}
%{_libdir}/openmpi/lib/libngcore.so
%{_libdir}/openmpi/lib/libnggui.so
%{_libdir}/openmpi/lib/libnglib.so
%{_libdir}/openmpi/lib/libngtogl.a
%{_libdir}/openmpi/lib/pkgconfig/%{name}.pc
%{_libdir}/openmpi/lib/cmake/%{name}/

%files -n python3-%{name}-openmpi
%{_libdir}/openmpi/python%{python3_version}/site-packages/pyngcore/
%{_libdir}/openmpi/python%{python3_version}/site-packages/netgen_mesher/
%{_libdir}/openmpi/python%{python3_version}/site-packages/netgen_mesher-py3.egg-info
%endif

%if %{build_mpich}
%files mpich
%{_libdir}/mpich/bin/netgen-mesher

%files mpich-libs
%{_libdir}/mpich/lib/libngcore.so.6.2
%{_libdir}/mpich/lib/libnggui.so.6.2
%{_libdir}/mpich/lib/libnglib.so.6.2

%files mpich-devel
%{_includedir}/mpich*/%{name}
%{_libdir}/mpich/lib/libngcore.so
%{_libdir}/mpich/lib/libnggui.so
%{_libdir}/mpich/lib/libnglib.so
%{_libdir}/mpich/lib/libngtogl.a
%{_libdir}/mpich/lib/pkgconfig/%{name}.pc
%{_libdir}/mpich/lib/cmake/%{name}/

%files -n python3-%{name}-mpich
%{_libdir}/mpich/python%{python3_version}/site-packages/pyngcore/
%{_libdir}/mpich/python%{python3_version}/site-packages/netgen_mesher/
%{_libdir}/mpich/python%{python3_version}/site-packages/netgen_mesher-py3.egg-info
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2406-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 03 2024 Sandro Mani <manisandro@gmail.com> - 6.2.2406-1
- Update to 6.2.2406

* Tue Sep 24 2024 Sandro Mani <manisandro@gmail.com> - 6.2.2405-1
- Update to 6.2.2405

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2404-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Sandro Mani <manisandro@gmail.com> - 6.2.2404-1
- Update to 6.2.2404

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 6.2.2403-3
- Rebuilt for Python 3.13

* Sat Jun 01 2024 Richard Shaw <hobbes1069@gmail.com> - 6.2.2403-2
- Rebuild for opencascade 7.8.1.

* Wed May 08 2024 Sandro Mani <manisandro@gmail.com> - 6.2.2403-1
- Update to 6.2.2403

* Sun Apr 14 2024 Sandro Mani <manisandro@gmail.com> - 6.2.2402-1
- Update to 6.2.2402

* Sat Mar 30 2024 Richard Shaw <hobbes1069@gmail.com> - 6.2.2202-11
- Rebuild for OpenCascade 7.8.0.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2202-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2202-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 6.2.2202-8
- Rebuild for openmpi 5.0.0, drops C++ API, i686 support

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2202-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 17 2023 Python Maint <python-maint@redhat.com> - 6.2.2202-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2202-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Richard Shaw <hobbes1069@gmail.com> - 6.2.2202-4
- Rebuild for opencascade.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2202-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.2.2202-2
- Rebuilt for Python 3.11

* Mon Mar 14 2022 Sandro Mani <manisandro@gmail.com> - 6.2.2202-1
- Update to 6.2.2202

* Sat Mar 05 2022 Sandro Mani <manisandro@gmail.com> - 6.2.2201-1
- Update to 6.2.2201

* Mon Jan 24 2022 Sandro Mani <manisandro@gmail.com> - 6.2.2105-3
- Fix packaging of python files

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2105-1
- Update to 6.2.2105

* Fri Sep 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2104-1
- Update to 6.2.2104

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2103-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 6.2.2103-2
- Rebuilt for Python 3.10

* Mon Jun 07 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2103-1
- Update to 6.2.2103

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.2.2102-2
- Rebuilt for Python 3.10

* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2102-1
- Update to 6.2.2102

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2101-1
- Update to 6.2.2101

* Thu Nov 26 2020 Richard Shaw <hobbes1069@gmail.com> - 6.2.2009-2
- Rebuild for OCC 7.5.0 side-tag.

* Thu Nov 12 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2009-1
- Update to 6.2.2009

* Sun Nov 08 2020 Richard Shaw <hobbes1069@gmail.com> - 6.2.2008-2
- Rebuild for OpenCASCADE 7.5.0.

* Thu Sep 17 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2008-1
- Update to 6.2.2008

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2007-1
- Update to 6.2.2007

* Fri Jun 19 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2006-1
- Update to 6.2.2006

* Sun Jun 14 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2005-1
- Update to 6.2.2005

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.2.2004-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2004-1
- Update to 6.2.2004

* Mon Feb 03 2020 Sandro Mani <manisandro@gmail.com> - 6.2.1910-1
- Update to 6.2.1910

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1810-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild


* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2.1810-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2.1810-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1810-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 6.2.1810-1
- Update to 6.2.1810

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 6.2-0.9.git94fd571
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-0.8.git94fd571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-0.7.git94fd571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.2-0.6.git94fd571
- Rebuilt for Python 3.7

* Wed May 02 2018 Sandro Mani <manisandro@gmail.com> - 6.2-0.5.git94fd571
- Rename netgen binary at CMake level to prevent breaking cmake config module (#1573330)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-0.4.git94fd571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-0.3.git94fd571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.git94fd571
- Install the nglib.h header

* Thu May 11 2017 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.1.git94fd571
- Update to 6.2.0 snapshot

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 5.3.1-12
- Rebuild for openmpi 2.0

* Thu Apr  7 2016 Richard Shaw <hobbes1069@gmail.com> - 5.3.1-11
- Rebuild for updated OCE.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 5.3.1-9
- Rebuild for openmpi 1.10.0

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.3.1-8
- Rebuild for MPI provides

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 5.3.1-7
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.3.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 12 2015 Sandro Mani <manisandro@gmail.com> - 5.3.1-4
- Rebuild (GCC5 ABI change)

* Sat Dec 13 2014 Sandro Mani <manisandro@gmail.com> - 5.3.1-3
- Fix library in -devel package

* Tue Oct 07 2014 Sandro Mani <manisandro@gmail.com> - 5.3.1-2
- Fix soname, use -release instead of -version-info

* Mon Oct 06 2014 Sandro Mani <manisandro@gmail.com> - 5.3.1-1
- Update to 5.3.1

* Mon Sep 01 2014 Sandro Mani <manisandro@gmail.com> - 5.3.0-1
- Update to 5.3.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Sandro Mani <manisandro@gmail.com> - 5.1-10
- Rebuild (OCE)

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 5.1-9
- Add missing mpich-devel BR

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 5.1-8
- Fix escaping of pkg-config variables

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 5.1-7
- Rename subpackage private -> devel-private

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 5.1-6
- Add netgen-5.1_relative-includes.patch

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 5.1-5
- Add subpackage for private headers
- Add patches from salome
- Make common package noarch
- Add missing %%{?_isa}

* Fri Jun 13 2014 Sandro Mani <manisandro@gmail.com> - 5.1-4
- Update netgen-5.1_build.patch
- Add netgen-5.1_msc-ver.patch

* Thu Jun 12 2014 Sandro Mani <manisandro@gmail.com> - 5.1-3
- Fix libgnlib soname

* Thu Jun 12 2014 Sandro Mani <manisandro@gmail.com> - 5.1-2
- Split off libraries in libs subpackages
- Rename shared libraries to less generic names

* Thu Jun 12 2014 Sandro Mani <manisandro@gmail.com> - 5.1-1
- Initial package
