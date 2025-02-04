%if 0%{?fedora} >= 40
%ifarch %{ix86}
%global with_openmpi 0
%else
%global with_openmpi 1
%endif
%else
%global with_openmpi 1
%endif
%global with_mpich2 1
%global with_doc 1

%if 0%{?fedora}
%global with_octave 1
%global octpkg mathgl
%endif

%if 0%{?with_doc}
%global docs on
%else
%global docs off
%endif



Name:          mathgl
Version:       8.0.1
Release:       18%{?dist}
Summary:       Cross-platform library for making high-quality scientific graphics
Summary(de):   Plattformübergreifende Bibliothek für hochwertige wissenschaftliche Graphiken
Summary(ru):   Библиотека для осуществления высококачественной визуализации данных
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
Url:           http://mathgl.sourceforge.net
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

# Install binaries for generation examples of illustrations
Patch0:        mathgl-2.4.2-examples.patch

# Skip FLUID binary test
Patch1:        mathgl-2.4.1-fltk-skip-fluid.patch

# Mathgl's enable all tries to use hdf4 and 5 at the same time
Patch2:        mathgl-2.4.1-no_hdf4-and-hdf5-simultaneously.patch

# Let macros to decide how to install octave module
Patch3:        mathgl-nooctaveinstall.patch

# There is no easy way to disable ONLY octave. Have to cut it from CmakeList.txt
Patch4:        mathgl-2.4.1-nooctave.patch

# Add python3 support
Patch5:        mathgl-lang.patch

# Fix convertions
Patch6:        mathgl-2.4.1-gcc7.patch

# Disable uppdate-{destop,mine}-database during install process
Patch7:        mathgl-2.4.1-no_updatedb.patch

Patch8:        mathgl-freeglut.patch

# Disable rebuild of l10n files, rhbz #1808694
# .mo files built in compile time contain time stamp what make them different
# between different archs (or not if you are lucky. I'm not.)
Patch9: mathgl-2.4.2.1-norebuild_l10n.patch

# https://sourceforge.net/p/mathgl/bugs/48/
# Support for libharu 2.4
Patch10: mathgl-libharu2.4.patch

# Use flexiblas instead of gslcblas
Patch11:       mathgl-flexiblas.patch

Requires:      %{name}-common = %{version}-%{release}

# mandatory packages
BuildRequires: make
BuildRequires: gsl-devel libpng-devel flexiblas-devel
BuildRequires: desktop-file-utils
BuildRequires: cmake3
BuildRequires: perl(Storable)

# optional packages
BuildRequires: freeglut-devel hdf5-devel libjpeg-devel libtiff-devel
BuildRequires: fltk-devel
BuildRequires: qt5-qtbase-devel qt5-qtwebkit-devel
BuildRequires: wxGTK-devel giflib-devel libtool-ltdl-devel
BuildRequires: libharu-devel
BuildRequires: swig lua-devel
BuildRequires: libXmu-devel
BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}-numpy

%description
Mathgl is a cross-platform library for making high-quality scientific
graphics. It provides fast data plotting and handling of large data
arrays, as well as  window and console modes and for easy embedding
into other programs. Mathgl integrates into fltk, qt and
opengl applications

%description -l ru
Mathgl - это кроссплатформенная библиотека для подготовки высококачественных
научных иллюстраций. Библиотека обладает возможностью работы с большими
массивами данных, быстрой отрисовки, при этом работая как в консольном, так и
оконном режимах, легко интегрируясь в другие приложения. Mathgl может быть
использована в FLTK, Qt и OpenGL приложениях.

%package devel
Summary:       Libraries and header files for %{name} library
Summary(ru):   Библиотеки и файлы заголовков для %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      gsl-devel%{?_isa}
Requires:      zlib-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use serial version of %{name}.

%description devel -l ru
Пакет %{name}-devel содержит библиотеки и файлы заголовков, необходимые
для разработки приложений с использованием однопоточной версии %{name}.

%package fonts
Requires:      %{name}-common = %{version}-%{release}
Summary:       Compiled fonts for the %{name}

%description fonts
%{summary}.

%if 0%{?with_doc}
%package doc
Summary:       HTML documentation and tutorial for the %{name} applications
BuildArch:     noarch
BuildRequires: texi2html texinfo-tex

%description doc
This package contains the documentation in the HTML and PDF format of the %{name}
package.
%endif

%package -n udav
Summary:       Viewer and editor for mathgl graphs
Summary(ru):   Редактор и средство визуализации для MathGL
Requires:      %{name} = %{version}-%{release}

%description -n udav
UDAV is cross-platform program for interactive data array visualization
using the MathGL library. UDAV works as a front-end to the mathgl
scripting engine, allowing for the generation of a wide variety of
scientific graph styles.

%package mgllab
Summary:       Viewer and editor for mathgl graphs
Summary(ru):   Редактор и средство визуализации для MathGL
Requires:      %{name} = %{version}-%{release}
Provides:      mgllab = %{version}-%{release}

%description mgllab
mgllab is FLTK port of UDAV, cross-platform program for interactive
data array visualization using the MathGL library. Mgllab works as a
front-end to the mathgl scripting engine, allowing for the generation
of a wide variety of scientific graph styles.

%description mgllab -l ru
mgllab - это FLTK порт UDAV, кроссплатформенное приложение для
интерактивной визуализации массивов данных с применением библиотеки MathGL.
Mgllab, как GUI для MathGL, может быть использован для формирования
различного вида научных иллюстраций.

%package mglview
Summary:       Execute MathGL scripts and show in an window
Requires:      %{name}-fltk = %{version}-%{release}

%description mglview
mglview reads MGL scripts from scriptfile to produce plots of
specified functions or data. The program will create a GUI window
showing the script result.

%package -n python%{python3_pkgversion}-mathgl
%{?python_provide:%python_provide python%{python3_pkgversion}-mathgl}
Summary:       Python3 module for MathGL
Requires:      %{name} = %{version}-%{release}

%description -n python%{python3_pkgversion}-mathgl
%{Summary}.

%package lua
Summary:       Lua module for MathGL
Requires:      %{name} = %{version}-%{release}

%description lua
%{Summary}.

%if 0%{?with_octave}
%package -n octave-mathgl
Summary:       Octave module for MathGL
Requires:      %{name} = %{version}-%{release}
Requires:      octave >= 2.9.12
BuildRequires: octave-devel

%description -n octave-mathgl
%{summary}.
%endif

%package common
Summary:       Common files for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
Requires:      %{name}-fonts = %{version}-%{release}
%if 0%{?with_doc}
Requires(post): info
Requires(preun): info
%endif

%description common
%{summary}.

%package examples
Summary:       Example illustration generators for %{name}
Requires:      %{name} = %{version}-%{release}

%description examples
Binaries for generation examples of illustrations that could be 
prepared by %{name}.

%if 0%{?with_openmpi}
%package openmpi
Summary:       OpenMPI version of %{name} library
BuildRequires: openmpi-devel
BuildRequires: hdf5-openmpi-devel
Requires:      %{name}-common = %{version}-%{release}

%description openmpi
%{summary}.

%package openmpi-devel
Summary:       Devel files for OpenMPI version of %{name} library
Requires:      %{name}-openmpi%{_isa} = %{version}-%{release}
Requires:      gsl-devel%{?_isa}
Requires:      zlib-devel%{?_isa}

%description openmpi-devel
%{summary}.
%endif

%if 0%{?with_mpich2}
%package mpich
Summary:       MPICH version of %{name} library
BuildRequires: mpich-devel
BuildRequires: hdf5-mpich-devel
Requires:      %{name}-common = %{version}-%{release}
Provides:      %{name}-mpich2 = %{version}-%{release}
Obsoletes:     %{name}-mpich2 < 2.1.2-9

%description mpich
%{summary}.

%package mpich-devel
Summary:       Devel files for MPICH version of %{name} library
Requires:      %{name}-mpich%{_isa} = %{version}-%{release}
Provides:      %{name}-mpich2-devel = %{version}-%{release}
Obsoletes:     %{name}-mpich2-devel < 2.1.2-9
Requires:      gsl-devel%{?_isa}
Requires:      zlib-devel%{?_isa}

%description mpich-devel
%{summary}.
%endif

%package qt5
Summary:       Qt5 widgets of %{name} library
Requires:      %{name} = %{version}-%{release}
Obsoletes:     %{name}-qt < 2.4
Provides:      %{name}-qt = %{version}-%{release}
Obsoletes:     %{name}-qt4 < 8.0

%description qt5
%{summary}.

%package qt5-devel
Summary:       Devel files for qt5 widgets of %{name} library
Requires:      %{name}-devel = %{version}-%{release}
Requires:      %{name}-qt5 = %{version}-%{release}
Obsoletes:     %{name}-qt-devel < 2.4
Provides:      %{name}-qt-devel = %{version}-%{release}
Obsoletes:     %{name}-qt4-devel < 8.0
Requires:      qt5-qtbase-devel

%description qt5-devel
%{summary}.

%package fltk
Summary:       Fltk widgets of %{name} library
Requires:      %{name} = %{version}-%{release}
Requires:      fltk-fluid

%description fltk
%{summary}.

%package fltk-devel
Summary:       Devel files for fltk widgets of %{name} library
Requires:      %{name}-devel = %{version}-%{release}
Requires:      %{name}-fltk = %{version}-%{release}
Requires:      fltk-devel

%description fltk-devel
%{summary}.

%package wx
Summary:       wxWidgets widgets of %{name} library
Requires:      %{name} = %{version}-%{release}

%description wx
%{summary}.

%package wx-devel
Summary:       Devel files for wxWidgets widgets of %{name} library
Requires:      %{name}-devel = %{version}-%{release}
Requires:      %{name}-wx = %{version}-%{release}
Requires:      wxGTK-devel

%description wx-devel
%{summary}.

%prep
%setup -q

# get rid of 3d-paty getopt
rm -rf addons/getopt

# prep for both py2 and py3 build
#mkdir lang/python3
#touch lang/python3/CMakeLists.txt

#convert EOL encodings, maintaining timestames
for file in AUTHORS ChangeLog.txt README ; do
    sed 's/\r//' $file > $file.new && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%patch -P0 -p1 -b .examples
%patch -P1 -p1 -b .fluid
%patch -P2 -p1 -b .no-hdf4-and-hdf5-simultaneously
%patch -P5 -p1 -b .lang
%patch -P6 -p1 -b .gcc7
%patch -P7 -p1 -b .no_updatedb
%if 0%{?with_octave}
%patch -P3 -p1 -b .nooctaveinstall
%else
%patch -P4 -p1 -b .no_octave
%endif
%patch -P8 -p0 -b .freeglut
%patch -P9 -p1 -b .norebuild_l10n
%patch -P10 -p1 -b .libharu2.4
%patch -P11 -p1 -b .flexiblas

# Fix hardcoded Python version
#sed -i -e 's,3\.[0-9],%{python3_version},g' \
#       -e 's,cpython-3[0-9],cpython-%{python3_version_nodots},g' \
#          lang/python3/CMakeLists.txt

# Fix hardcoded paths
sed -i s,/usr/local/share/doc/mathgl/,%{_docdir}/%{name}/, udav/udav_wnd.h
sed -i s,/usr/local/share/udav/,%{_datadir}/udav/, udav/udav_wnd.cpp
sed -i s,/usr/local/share/mathgl/fonts/,%{_datadir}/%{name}/fonts/, udav/prop_dlg.cpp

# Fix octave module version wether we need it or not
sed -i -e "s,Version:.*,Version: %{version}," lang/DESCRIPTION

%if 0%{?fedora}
%global octave_tar_suffix %{octave_host}-%{octave_api}
%global mgl_octarch_dir %{_builddir}/%{buildsubdir}/build/
%global mgl_octarch_name %{octpkg}-%{version}-%{octave_tar_suffix}.tar.gz
%endif


%build

OMP_NUM_THREADS=1
export OMP_NUM_THREADS

%define building() \
BUILD_MPI="-Denable-mpi=on -Denable-all-docs=off" %buildcommon

%define building_serial() \
BUILD_MPI="-Denable-mpi=off \
           -Denable-all-docs=%{docs} \
           -Denable-all-widgets=on \
           -Denable-all-swig=on \
           -Denable-all-widgets=on \
           -Denable-hdf4=off \
           " %buildcommon

# Disable SMP build

%define buildcommon() \
%cmake \\\
    -DMathGL_INSTALL_CMAKE_DIR=%{_libdir}/cmake/mathgl \\\
    -DMathGL_INSTALL_LIB_DIR=%{_libdir} \\\
    -Denable-all=on \\\
    -Denable-qt5asqt=off \\\
    $BUILD_MPI \\\
    ..; \
%{cmake_build}

# serial
%global _vpath_builddir %{_target_platform}_serial
%building_serial

# MPI vars
export CC=mpicc
export CXX=mpicxx

%if 0%{?with_openmpi}
# OpenMPI
%{_openmpi_load}
%global _vpath_builddir %{_target_platform}_openmpi
%building
%{_openmpi_unload}
%endif

%if 0%{?with_mpich2}
# MPICH2
%{_mpich_load}
%global _vpath_builddir %{_target_platform}_mpich
%building
%{_mpich_unload}
%endif

%install

# MPI install libs only
%define installing() \
make install DESTDIR=%{buildroot}%{_libdir}/$MPI_COMPILER_NAME -C %{_target_platform}_$MPI_COMPILER_NAME INSTALL="install -p"; \
mkdir -p %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/lib/ \
mv %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/%{_libdir}/libmgl* %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/lib/; \
mkdir -p %{buildroot}%{_includedir}/$MPI_COMPILER/mgl2; \
mv %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/%{_includedir}/mgl2/* %{buildroot}%{_includedir}/$MPI_COMPILER/mgl2/; \
rm -f %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/lib/*.a; \
rm -r %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/usr

# Serial
%global _vpath_builddir %{_target_platform}_serial
%{cmake_install}
%if 0%{?with_octave}
rm -f %{buildroot}%{_datadir}/%{name}/mathgl.tar.gz
mkdir -p %{mgl_octarch_dir}
cp %{_target_platform}_serial/lang/%{octpkg}.tar.gz %{mgl_octarch_dir}/%{mgl_octarch_name}
%octave_pkg_install
rm -f %{mgl_octarch_dir}/%{mgl_octarch_name}/%{octpkg}.tar.gz
%endif

# part of serial build
%find_lang %{name}
%find_lang udav --with-qt

# No that modern cmake_install macros for mpi install.
%if 0%{?with_openmpi}
# OpenMPI
%{_openmpi_load}
%global _vpath_builddir %{_target_platform}_openmpi
MPI_COMPILER_NAME=openmpi %installing
%{_openmpi_unload}
%endif

%if 0%{?with_mpich2}
# MPICH
%{_mpich_load}
%global _vpath_builddir %{_target_platform}_mpich
MPI_COMPILER_NAME=mpich %installing
%{_mpich_unload}
%endif

#Remove symlink to .so file in python dir. Let python find libs normally
# not needed now?
#unlink %{buildroot}/%{python3_sitelib}/_mathgl.so

#Remove static libraries generated by cmake
rm %{buildroot}/%{_libdir}/*.a

# Remove the binary mgl.cgi. Im not convinced about it (eg mem leak in main), and that its really needed
# The same with man file for it
rm %{buildroot}/%{_prefix}/lib/cgi-bin/mgl.cgi
%if 0%{?with_doc}
rm %{buildroot}/%{_mandir}/man1/mgl.cgi.1*

# Prepare for documentation
if [ -d _tmp_docdir ]
then
rm -r _tmp_docdir
fi
mv %{buildroot}%{_docdir}/mathgl _tmp_docdir
%endif


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/udav.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mgllab.desktop


%ldconfig_scriptlets

%ldconfig_scriptlets qt5

%ldconfig_scriptlets fltk

%ldconfig_scriptlets wx

%if 0%{?with_octave}
%post -n octave-mathgl
%octave_cmd pkg rebuild

%preun -n octave-mathgl
%octave_pkg_preun

%postun -n octave-mathgl
%octave_cmd pkg rebuild
%endif

%files -f %{name}.lang
%doc AUTHORS ChangeLog.txt README COPYING  README_V2
%{_libdir}/libmgl.so.*
%{_bindir}/mglconv
%{_bindir}/mgltask
%exclude %{_bindir}/mgl_*example
%if 0%{?with_doc}
%{_mandir}/man1/mglconv.1.gz
%endif

%files devel
%{_libdir}/libmgl.so
%{_includedir}/mgl2/
%{_libdir}/cmake/mathgl/
%{_libdir}/cmake/mathgl2/

%files mgllab
%{_bindir}/mgllab
%{_datadir}/applications/mgllab.desktop

%files mglview
%{_bindir}/mglview
%if 0%{?with_doc}
%{_mandir}/man1/mglview.1.gz
%endif

%files qt5
%{_libdir}/libmgl-qt.so.*
%{_libdir}/libmgl-qt5.so.*
%{_libdir}/libmgl-wnd.so.*

%files qt5-devel
%{_libdir}/libmgl-qt.so
%{_libdir}/libmgl-qt5.so
%{_libdir}/libmgl-wnd.so

%files wx
%{_libdir}/libmgl-wx.so.*

%files wx-devel
%{_libdir}/libmgl-wx.so

%files fltk
%{_libdir}/libmgl-fltk.so.*
%{_libdir}/libmgl-glut.so.*

%files fltk-devel
%{_libdir}/libmgl-fltk.so
%{_libdir}/libmgl-glut.so

%files -n udav -f udav.lang
%{_bindir}/udav
%if 0%{?with_doc}
%{_mandir}/man1/udav.1.gz
%endif
%{_datadir}/applications/udav.desktop
%dir %{_datadir}/udav/

%files -n python%{python3_pkgversion}-mathgl
%{python3_sitelib}/*

%files lua
%{_libdir}/mgl-lua.so

%if 0%{?with_octave}
%files -n octave-mathgl
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/packinfo
%endif

%if 0%{?with_doc}
%files doc
%doc AUTHORS COPYING
%doc _tmp_docdir/*
%endif

%files fonts
%{_datadir}/%{name}/fonts/

%files common
%{_datadir}/pixmaps/*.png
%{_datadir}/mime/packages/mgl.xml
%if 0%{?with_doc}
%{_mandir}/man5/mgl.5.gz
%{_infodir}/%{name}*.gz
%endif

%files examples
%{_bindir}/mgl_*example

%if 0%{?with_openmpi}
%files openmpi
%doc COPYING
%{_libdir}/openmpi/lib/*.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/*.so
%{_includedir}/openmpi-%{_arch}/mgl2/
%endif

%if 0%{?with_mpich2}
%files mpich
%doc COPYING
%{_libdir}/mpich/lib/*.so.*

%files mpich-devel
%{_libdir}/mpich/lib/*.so
%{_includedir}/mpich-%{_arch}/mgl2/
%endif

%changelog
* Sun Feb 02 2025 Orion Poplawski <orion@nwra.com> - 8.0.1-18
- Rebuild with gsl 2.8

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 8.0.1-16
- Rebuild for octave 9.2

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 8.0.1-15
- Rebuild for hdf5 1.14.5

* Fri Aug  9 2024 Jerry James <loganjerry@gmail.com> - 8.0.1-14
- Link with flexiblas instead of gslcblas

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 8.0.1-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 8.0.1-11
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 8.0.1-10
- Fix -python subpackage build.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 8.0.1-7
- Rebuild for openmpi 5.0.0, drops i686 and C++ API
- Use newer patch syntax
- Cleanup old conditionals

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 8.0.1-5
- Rebuilt for Python 3.12

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 8.0.1-4
- Rebuild with octave 8.1.0

* Sun Mar 05 2023 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 8.0.1-3
- Fix -[wx,fltk,qt5]-devel dependencies.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 06 2022 Orion Poplawski <orion@nwra.com> - 8.0.1-1
- Update to 8.0.1
- Drop Qt4 support

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.4-18
- Rebuild for gsl-2.7.1

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 2.4.4-17
- Rebuild with wxWidgets 3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4.4-15
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 2.4.4-14
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 2.4.4-12
- Rebuild for hdf5 1.12.1

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 2.4.4-11
- Rebuild for hdf5 1.10.7/octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.4-9
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 30 2020 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.4.4-7
- Fix mpi build for that great cmake macro update.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@nwra.com> - 2.4.4-5
- Rebuild for hdf5 1.10.6

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.4-4
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.4.4-3
- Remove octave tar.gz from -fonts subpackage.
- Disable rebuild of l10n. Fix rhbz #1808694.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4.4-1
- 2.4.4, Rebuilt for new freeglut

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.2.1-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.2.1-11
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.4.2.1-10
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.2.1-9
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 2.4.2.1-7
- Rebuild for octave 5.1

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 2.4.2.1-6
- Remove hardcoded gzip suffix from GNU info pages

* Tue Mar 12 2019 Orion Poplawski <orion@nwra.com> - 2.4.2.1-5
- Rebuild for hdf5 1.10.5

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2.4.2.1-4
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Orion Poplawski <orion@cora.nwra.com> - 2.4.2.1-2
- Rebuild for octave 4.4

* Tue Nov 13 2018 Orion Poplawski <orion@cora.nwra.com> - 2.4.2.1-1
- Update to 2.4.2.1
- Rebuild for octave 4.4

* Tue Sep 18 2018 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.4.1-10
- Remove Python2 subpackage. Patch updated.

* Fri Jul 20 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.4.1-9
- Use proper %%python2_sitelib macro.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Scott Talbert <swt@techie.net> - 2.4.1-7
- Correct wx-devel dependency: wxGTK-devel -> wxGTK3-devel

* Wed Jul 04 2018 Marcel Plch <mplch@redhat.com> - 2.4.1-6
- Patch for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-5
- Rebuilt for Python 3.7

* Fri Feb 16 2018 D Haley <mycae gmx com> - 2.4.1-4
- Fix overflow in mgl_example (light)

* Tue Feb 13 2018 Sandro Mani <manisandro@gmail.com> - 2.4.1-3
- Rebuild (giflib)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.4.1-1
- Update to 2.4.1.
- Add python3 bindings.
- Refresh patches. Add new ones.
- Drop noqt4 patch. Make qt4 and qt5 widgets so, rename qt->qt4, add qt5 subpackage.
- Move lua bindings to lua subpackage.

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.3.5-9.1
- Python 2 binary package renamed to python2-mathgl
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.5-7.1
- rebuilt to fix FTBFS

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.5-5.1
- Rebuild for new Libharu.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.5.1-3
- Reenable octave bindings for f26 and above.

* Tue Jan 10 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.5.1-2
- Disable smp build.

* Mon Jan 09 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.5.1-1
- Update to new version.
- Update patches for new version.
- Drop X11 patch.

* Fri Jan 06 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.4-7
- Disable octave support for rawhide as octave-4.2 is not supported by swig for now.

* Thu Dec 08 2016 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.4-6
- Fix description tag for octave-mathgl.

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.4-5
- Rebuild for octave 4.2

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.4-4
- Rebuild for openmpi 2.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.4-2
- Rebuild for gsl 2.1

* Mon Feb 15 2016 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.4-1
- Drop patches: mathgl-2.3.3-includes.patch, mathgl-2.3.3-signed_char.patch,
  mathgl-2.3.3-gsl2.patch. Emplemented in upstream.
- Update *-examples.patch and *-x11.patch.
- Update to new 2.3.4.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.3-9
- All *-devel Requires should have _isa bits.

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.3-8
- Rebuild for hdf5 1.8.16

* Mon Jan 04 2016 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.3-7
- Split out python module and fonts.
- Make fonts subpackage arch depenedent, fix for RHBZ #1294072.
- Fix typos in name in changelog.

* Fri Dec 11 2015 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.3-6
- Unconditionalize libharu. It is in epel now.

* Wed Dec 09 2015 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.3-5
- Reenable octave module.
- Conditionalize doc and mpich subpackages.
- Conditionalize libharu and octave: only for Fedora.
- Move -qt, -wx and -fltk widgets into seperate subpackages.
- Update gsl patch: manage old version (in epel).

* Thu Nov 26 2015 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.3-4
- Fix building on arm (see mathgl-2.3.3-signed_char.patch).

* Tue Nov 24 2015 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.3-3
- Fix files section: cmake script and mime xml.

* Tue Nov 24 2015 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.3-2
- Add libtool-ltdl-devel to BR.

* Tue Nov 24 2015 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.3-1
- Update to new 2.3.3 version.
- Fix gsl-2 support.

* Wed Sep 16 2015 Orion Poplawski <orion@cora.nwra.com> - 2.3-11
- Rebuild for openmpi 1.10.0

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 2.3-10
- Rebuild for RPM MPI Requires Provides Change
- Fix FTBFS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 2.3-8
- Rebuild for hdf5 1.8.15

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 21 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 2.3-6
- Fix linking with libX11.

* Tue Mar 17 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 2.3-5
- Rebuild for new mpich.

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 2.3-4
- rebuild (fltk)

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.3-3
- Rebuild for hdf5 1.8.14

* Sat Oct 11 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.3-2
- Disable SMP build for serial (docs failed).

* Tue Oct 07 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.3-1
- Update for new 2.3 version.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 22 2014 Deji Akingunola <dakingun@gmail.com> - 2.2.1-4
- Rebuild for mpich-3.1

* Mon Feb 17 2014 Dan Horák <dan[at]danny.cz> - 2.2.1-3
- Conditionalize openmpi support, fixes build on s390(x)

* Fri Feb  7 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.2.1-2
- Workaround for race condition during package building.

* Tue Feb  4 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.2.1-1
- Update for new 2.2.1.

* Thu Jan 16 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.2-2
- Drop bogus ocatave support. For a time.

* Wed Dec 25 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 2.2-1
- Update to 2.2.
- Fix bogus dates.
- Fix issue with docdirs.

* Mon Aug 12 2013 Orion Poplawski <orion@cora.nwra.com> - 2.1.2-11
- Fix hdf BRs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Deji Akingunola <dakingun@gmail.com> - 2.1.2-9
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 2.1.2-8
- Rebuild for hdf5 1.8.11

* Tue Apr 23 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 2.1.2-7
- Modify patch to fix pics generation.

* Mon Apr 22 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 2.1.2-6
- Add patch to fix pics generation.

* Thu Apr 18 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 2.1.2-5
- Install binaries used for generation of examples of illustrations.

* Wed Apr 17 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 2.1.2-4
- Disable some .png generation for -doc.

* Mon Apr 15 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 2.1.2-3
- MPI suport for MathGL library: add -common subpackage.
- MPI enabled for MathGL library: add OpenMPI and MPICH2 support.
- Reformat spec for better reading (spaces vs tabs, aligning).

* Mon Apr 15 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 2.1.2-2
- Fix spec for better cmake use.
- Make vars in spec to be in one style.
- Add some Russian translation.
- .info is installed. Remove copying.
- Make udav sub-package to be with name "udav".
- Maintain traslation for udav.

* Sun Apr 14 2013 <mycae(a!)gmx.com> 2.1.2-1
- Update to upstream 2.1.2
- New upstream has entirely different build system

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.11.3-2
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 07 2012 <mycae(a!t)yahoo.com> - 1.11.3-1
- Update to 1.11.3

* Mon Dec 03 2012 Orion Poplawski <orion@cora.nwra.com> - 1.11.2-9
- Rebuild for hdf5 1.8.10

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 09 2011 <mycae(a!t)yahoo.com> - 1.11.2-6
- Fix build fail due to libpng no longer including zlib
- Remove no longer needed libtool hack

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.11.2-5
- Rebuild for new libpng

* Thu Jun 23 2011 <mycae(a!t)yahoo.com> - 1.11.2-4
- Recall why we needed hdf-devel. Its to keep configure happy.

* Thu Jun 23 2011 <mycae(a!t)yahoo.com> - 1.11.2-3
- Bump for build

* Thu Jun 23 2011 <mycae(a!t)yahoo.com> - 1.11.2-2
- Fix bug 678856, add hdf-static as buildrequire

* Wed Jun 01 2011 <mycae(a!t)yahoo.com> - 1.11.2-1
- Update to upstream 1.11.2

* Tue May 31 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.11.0.1-6
- Reflect fltk having changed its include directory (Fix FTBS).
- Fix German %%summary.

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 1.11.0.1-5
- Rebuild for hdf5 1.8.7 

* Sun Feb 27 2011 <mycae(a!t)yahoo.com> - 1.11.0.1-4
- Remove octave for Bug 679948, and dynamic patch non-functional due
  to swig covariant return type problems with octave_map

* Sat Feb 12 2011 <mycae(a!t)yahoo.com> - 1.11.0.1-3
- Request rebuild -- octave-config needs to emit correct api. 

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 27 2010 <mycae(a!t)yahoo.com> - 1.11.0.1-1
- Update to 1.11.0.1

* Sun Aug 08 2010 <mycae(a!t)yahoo.com> - 1.10.2.1-3
- Add gsl-devel to requires

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.10.2.1-2.1
- rebuilt against wxGTK-2.8.11-2

* Wed Apr 14 2010 <mycae(a!t)yahoo.com> - 1.10.2.1-1.1
- tag bump

* Wed Apr 14 2010 <mycae(a!t)yahoo.com> - 1.10.2.1-1
- Update to 1.10.2.1
- Fix linker error due to DSO change (Bug #564982)

* Sat Jan 02 2010 <mycae(a!t)yahoo.com> - 1.10-2
- Fix octave interface to load on startup
- Fix texinfo insatll

* Sat Jan 02 2010 <mycae(a!t)yahoo.com> - 1.10-1
- Update to 1.10

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9-8
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Sun Oct 25 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Sep 14 2009 <mycae(a!t)yahoo.com> 1.9-6
- Add COPYING to doc

* Sat Sep 12 2009 <mycae(a!t)yahoo.com> 1.9-5
- Removed the word "static" from devel description, as doesn't have static
- Fonts now owned at datadir/name level
- Added COPYRIGHT NEWS and TODO

* Sat Aug 15 2009 <mycae(a!t)yahoo.com> 1.9-4
- Fix octave installation method
- Remove wx lib, which doesn't have meaningful code.

* Sun Aug 02 2009  <mycae(a!t)yahoo.com> 1.9-3
- Fix texinfo install (mv to main & add pre/post)
- Remove chrpath, as we now autoreconf
- Add octave pkg rebuild commands

* Tue Jul 21 2009  <mycae(a!t)yahoo.com> 1.9-2 
- Fix rpath for build on x86_64. 
- remove unrecognized configure options: --enable-tiff, --disable-ltdl-install
- Switch to --enable-all --enable-octave
- Add hdf5 patch
- Add doc subpackage

* Thu Jul 09 2009 <mycae(a!t)yahoo.com> 1.9-1
- Update to 1.9
- Drop explicit Requires
- Perserve timestamps on EOL conversion
- Added patch to disable unused gsl cblas link

* Sat May 02 2009 <mycae(a!t)yahoo.com> 1.8.1-1
- Update to 1.8.1

* Wed Jan 28 2009 <mycae(a!t)yahoo.com> 1.8-3
- Ensure timestamps are preserved during make install
- Modify defattr
- Remove UDAV from package summary

* Mon Dec 29 2008 <mycae(a!t)yahoo.com> 1.8-2
- Remove redundant and erroneous licence field in devel section
- Fix files from mgl/*h to mgl/
- Removed Requires, per bugzilla recommendation.
- Disabled static library generation
- Removed libltdl from build 
- Added libtool-ltdl as BuildRequires

* Mon Dec 29 2008 <mycae(a!t)yahoo.com> 1.8-1
- Updated to version 1.8
- Added QT env. vars for fedora
- Cleaned up description
- Change licence field from GPL to GPLv2

* Wed Jun 4 2008 Nik <niktr@mail.ru> 
- disabled hdf5 support according to developer request

* Tue Jun 3 2008 Nik <niktr@mail.ru> 
- updated to version 1.7.1

* Mon Jun 2 2008 Nik <niktr@mail.ru> 
- updated to version 1.7

* Sat Apr 5 2008 Nik <niktr@mail.ru> 
- updated to version 1.6.2

* Thu Mar 13 2008 Nik <niktr@mail.ru>
- updated to version 1.6
- added fltk(-devel) to requres list

* Tue Mar 11 2008 Nik <niktr@mail.ru>
- tiff bug fixed
- enable-all option added

* Sat Mar 1 2008 Nik <niktr@mail.ru>
- spec cleanup
- --enable(jpeg, tiff, hdf5) features added
- enable-tiff leads to make error, submitted to author. Feature disabled.

* Fri Feb 29 2008 Nik <niktr@mail.ru>
- initial build of version 1.5
