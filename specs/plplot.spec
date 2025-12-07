%{!?octave_api:%global octave_api %(octave-config -p API_VERSION || echo 0)}
# Set to bcond_with or use --without doc to disable doc build
%bcond_without doc
# Set to bcond_with or use --without octave to disable octave support
%if 0%{?el8}%{?el9}
# EL8 has too old of a swig - https://bugzilla.redhat.com/show_bug.cgi?id=1753475
# EL9 has too old of a swig, and we can't make use of the swig:4.1 module
%bcond_with octave
%else
%bcond_without octave
%endif

# conditionalize Ada support
%ifnarch %{GNAT_arches}
%bcond_with ada
%else
%bcond_without ada
%endif

# conditionalize Ocaml support
# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
%ifarch %{ix86} sparc64 s390 s390x
%bcond_with ocaml
%else
%bcond_without ocaml
%endif

# Let's drop itcl for EPEL8
%if 0%{?rhel} >= 8
%bcond_with itcl
%else
%bcond_without itcl
%endif

#RHEL8 does not have X on s390x
%ifarch s390x
%if 0%{?el8}
%bcond_with check
%else
%bcond_without check
%endif
%else
%bcond_without check
%endif

%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif

# No more Java on i686
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

%global commit 48a56ee63d25d24eeb44f392025953a6e9cc6b3f

Name:           plplot
Version:        5.15.0
Release:        %autorelease
Summary:        Library of functions for making scientific plots

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://plplot.sourceforge.net/
Source0:        https://downloads.sourceforge.net/plplot/%{name}-%{version}.tar.gz
#Source0:        https://sourceforge.net/code-snapshots/git/p/pl/plplot/plplot.git/plplot-plplot-%{commit}.zip
Source1:        xorg.conf
# Drop -mieee-fp
Patch0:         plplot-ieee.patch
# Fix build with Qt 5.15
# commit 2aa2e1bdae9f75dbf74dc970e80834081fb3d0de
Patch1:         plplot-qt-5.15.patch
Patch2:         plplot-multiarch.patch
# Upstream patch to fix in-tree ocaml rpath - plplot-5.15.0-37-g6b215267e
Patch3:         plplot-ocaml-rpath.patch
# Python 3.13 support
Patch4:         plplot-python3.13.patch
# Fix example for numpy 2.X
# https://bugzilla.redhat.com/show_bug.cgi?id=2336933
# https://sourceforge.net/p/plplot/plplot/merge-requests/7/
Patch5:         plplot-numpy.patch
# Fix test for signal()
# https://sourceforge.net/p/plplot/plplot/merge-requests/8/
Patch6:         plplot-signal.patch
# Don't use -custom with ocamlc
Patch7:         plplot-ocaml.patch
# Fix safe-string new default in OCaml 4.06.
Patch9:         plplot-5.12.0-safe-string.patch
Patch10:        plplot-pyqt5-sip-path.patch
Patch11:        plplot-sip-build-support.patch
Patch12:        plplot-cmake-c99.patch
# Update OCaml link invocations for OCaml 5.0.0
Patch13:        plplot-ocaml-link.patch
# Fix for SWIG 4.3.0
Patch14:        plplot-5.15.0-swig-4.3.patch
# Fix for SWIG 4.4.0
# https://sourceforge.net/p/plplot/support-requests/56/
Patch15:        https://sourceforge.net/p/plplot/support-requests/_discuss/thread/bd326c8bff/fec5/attachment/plplot-5.15.0-swig-4.4.patch


BuildRequires:  cmake >= 3.13.2
# Building with Ninja generator fails in the java add_custom_command
%global _cmake_generator "Unix Makefiles"
BuildRequires:  make
BuildRequires:  libtool-ltdl-devel
BuildRequires:  gcc-gfortran
%if %{with ada}
BuildRequires:  gcc-gnat
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel
BuildRequires:  lapack-devel
%endif
%endif
BuildRequires:  swig
%if %{with octave}
BuildRequires:  octave-devel
%global build_octave -DTRY_OCTAVE4=ON
%else
Obsoletes:      %{name}-octave < %{version}-%{release}
%global build_octave -DENABLE_octave:BOOL=OFF
%endif
%if %{with java}
BuildRequires:  java-devel
# Work around https://bugzilla.redhat.com/show_bug.cgi?id=2225018
%if 0%{?el9}
BuildRequires:  tzdata-java
%endif
%else
Obsoletes:      %{name}-java < %{version}-%{release}
Obsoletes:      %{name}-java-devel < %{version}-%{release}
%endif
BuildRequires:  freetype-devel, qhull-devel , ncurses-devel
BuildRequires:  gd-devel
BuildRequires:  tcl-devel < 1:9
BuildRequires:  tk-devel < 1:9
%if %{with itcl}
BuildRequires:  itcl-devel, itk-devel
BuildRequires:  iwidgets
%endif
BuildRequires:  python3-devel, python3-numpy
BuildRequires:  perl(XML::DOM), lasi-devel, wxGTK-devel
BuildRequires:  gnu-free-mono-fonts
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
%if %{with doc}
BuildRequires:  docbook2X
BuildRequires:  doxygen
BuildRequires:  texlive-xmltex
BuildRequires:  tex(ulem.sty)
# RHEL8 does not ship xmlto-tex
%if 0%{?fedora}
BuildRequires:  xmlto-tex
%else
BuildRequires:  xmlto
%endif
%endif
%if %{with ocaml}
BuildRequires:  ocaml
# ocaml cairo support disabled upstream
# BuildRequires:  ocaml-cairo-devel
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
%if ! ( 0%{?rhel} >= 8 )
BuildRequires:  ocaml-lablgtk-devel
%endif
BuildRequires:  ocaml-ocamldoc
%endif
BuildRequires:  libharu-devel
BuildRequires:  lua-devel
BuildRequires:  cmake(qt5gui)
BuildRequires:  cmake(qt5printsupport)
BuildRequires:  cmake(Qt5Svg)
#For pyqt5
BuildRequires:  python3dist(pyqt-builder)
BuildRequires:  python3dist(sip) >= 5
BuildRequires:  python3-qt5-devel
BuildRequires:  shapelib-devel
# For %check
%if %{with check}
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  mesa-dri-drivers
%endif
BuildRequires:  chrpath
Requires:       gnu-free-mono-fonts
Requires:       gnu-free-sans-fonts
Requires:       gnu-free-serif-fonts
Requires:       python3-numpy


%description
PLplot is a library of functions that are useful for making scientific
plots.

PLplot can be used from within compiled languages such as C, C++,
FORTRAN and Java, and interactively from interpreted languages such as
Octave, Python, Perl and Tcl.

The PLplot library can be used to create standard x-y plots, semilog
plots, log-log plots, contour plots, 3D surface plots, mesh plots, bar
charts and pie charts. Multiple graphs (of the same or different sizes)
may be placed on a single page with multiple lines in each graph.

A variety of output file devices such as Postscript, png, jpeg, LaTeX
and others, as well as interactive devices such as xwin, tk, xterm and
Tektronics devices are supported. New devices can be easily added by
writing a small number of device dependent routines.

There are almost 2000 characters in the extended character set. This
includes four different fonts, the Greek alphabet and a host of
mathematical, musical, and other symbols. Some devices supports its own
way of dealing with text, such as the Postscript and LaTeX drivers, or
the png and jpeg drivers that uses the Freetype library.


%package        libs
Summary:        Libraries for PLplot
Requires:       %{name}-data = %{version}-%{release}
Obsoletes:      %{name}-perl < 5.14.0-8

%description    libs
%{summary}.


%package        data
Summary:        Data files for PLplot
BuildArch:      noarch

%description    data
%{summary}.


%package        devel
Summary:        Development headers and libraries for PLplot
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.


%package        doc
Summary:        Documentation for PLplot
# Conditional OCaml support prevents this
#BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
%{summary}.


%if %{with ada}
%package        ada
Summary:        Functions for scientific plotting with Ada
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    ada
%{summary}.

%package        ada-devel
Summary:        Development files for using PLplot Ada bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-ada%{?_isa} = %{version}-%{release}
Requires:       gcc-gnat

%description    ada-devel
%{summary}.
%endif


%package        fortran-devel
Summary:        Development files for using PLplot Fortran bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%if 0%{?fedora}
Requires:       gcc-gfortran%{_isa}
%else
Requires:       gcc-gfortran
%endif

%description    fortran-devel
%{summary}.


%if %{with java}
%package        java
Summary:        Functions for scientific plotting with Java
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       java-headless

%description    java
%{summary}.

%package        java-devel
Summary:        Development files for using PLplot GNOME
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-java%{?_isa} = %{version}-%{release}

%description    java-devel
%{summary}.
%endif


%package        lua
Summary:        Functions for scientific plotting with Lua
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       lua

%description    lua
%{summary}.


%if %{with ocaml}
%package        -n ocaml-plplot
Summary:        Functions for scientific plotting with OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       plplot-ocaml = %{version}-%{release}
Obsoletes:      plplot-ocaml < 5.9.10-3

%description    -n ocaml-plplot
%{summary}.


%package        -n ocaml-plplot-devel
Summary:        Development files for PLplot OCaml
Requires:       ocaml-plplot%{?_isa} = %{version}-%{release}
Provides:       plplot-ocaml-devel = %{version}-%{release}
Obsoletes:      plplot-ocaml-devel < 5.9.10-3

%description    -n ocaml-plplot-devel
%{summary}.
%endif


%if %{with octave}
%package        octave
Summary:        Functions for scientific plotting with Octave
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       octave(api) = %{octave_api}

%description    octave
%{summary}.
%endif


%package        pyqt
Summary:        Functions for scientific plotting with PyQt
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    pyqt
%{summary}.


%package        qt
Summary:        Functions for scientific plotting with Qt
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    qt
%{summary}.

%package        qt-devel
Summary:        Development files for using PLplot with Qt
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-qt%{?_isa} = %{version}-%{release}
Requires:       cmake(qt5gui)
Requires:       cmake(qt5printsupport)
Requires:       cmake(Qt5Svg)

%description    qt-devel
%{summary}.


%package        tk
Summary:        Functions for scientific plotting with Tk
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tk
%{summary}.

%package        tk-devel
Summary:        Development files for using PLplot with Tk
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-tk%{?_isa} = %{version}-%{release}
Requires:       tk-devel%{?_isa}

# Do not check any tk examples requires
%global __requires_exclude_from ^%{_datadir}/plplot%{version}/examples/tk/tk.*$

%description    tk-devel
%{summary}.


%package        wxGTK
Summary:        Functions for scientific plotting with wxGTK
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    wxGTK
%{summary}.

%package        wxGTK-devel
Summary:        Development files for using PLplot with wxGTK
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-wxGTK%{?_isa} = %{version}-%{release}
Requires:       wxGTK-devel%{?_isa}

%description    wxGTK-devel
%{summary}.


%prep
%setup -q
%patch -P0 -p1 -b .ieee
%patch -P1 -p1 -b .qt5
%patch -P2 -p1 -b .multiarch
%patch -P3 -p1 -b .ocaml-rpath
%patch -P4 -p1 -b .python3.13
%patch -P5 -p1 -b .numpy
%patch -P6 -p1 -b .signal
%patch -P7 -p1 -b .ocaml
%patch -P9 -p1 -b .safestring
%patch -P10 -p1 -b .sip-path
%patch -P11 -p1 -b .sip-build
%patch -P12 -p1
%patch -P13 -p1 -b .ocamlmklib
%patch -P14 -p1
%patch -P15 -p1
# Use cmake FindLua
rm cmake/modules/FindLua.cmake


%build
%if 0%{?fedora}
export LDFLAGS='%{build_ldflags} -Wl,--no-warn-execstack'
%endif
export PATH="%{_qt5_bindir}:$PATH"
# Needed for octave output to not have control characters
unset TERM
printenv
# We assume that tk version is the same as tcl, cannot check without DISPLAY
tkver=$(echo 'puts [info patchlevel]; exit' | tclsh)
%if %{with itcl}
# Hacks to determine versions without DISPLAY
itclver=$(echo %{_libdir}/libitcl*.so | sed -e 's/.*itcl\([0-9.]*\)\.so/\1/')
itkver=$(echo %{_libdir}/libitk*.so | sed -e 's/.*itk\([0-9.]*\)\.so/\1/')
iwidgetsver=$(echo %{_datadir}/tcl*/iwidgets* | sed -e 's/.*iwidgets//')
%endif
%cmake \
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
        -DFORTRAN_MOD_DIR:PATH=%{_fmoddir} \
        -DUSE_RPATH:BOOL=OFF \
        -DENABLE_ada:BOOL=ON \
        %{?with_flexiblas:-DBLA_VENDOR=FlexiBLAS} \
        -DENABLE_d:BOOL=ON \
%if %{with itcl}
        -DENABLE_itcl:BOOL=ON \
        -DENABLE_itk:BOOL=ON \
        -DPLPLOT_ITCL_VERSION=$itclver \
        -DPLPLOT_ITK_VERSION=$itkver \
        -DIWIDGETS_VERSIONS_LIST:STRING="$iwidgetsver;$itkver;$itclver" \
        -DUSE_INCRTCL_VERSION_4:BOOL=ON \
%endif
        -DENABLE_lua:BOOL=ON \
        -DENABLE_ocaml:BOOL=ON \
        -DOCAML_INSTALL_DIR:PATH=`ocamlc -where` \
        %{build_octave} \
        -DENABLE_tk:BOOL=ON \
        -DJAVAWRAPPER_DIR:PATH="%{_libdir}/plplot%{version}" \
        -DNON_TRANSITIVE:BOOL=ON \
        -DPL_FREETYPE_FONT_PATH:PATH="/usr/share/fonts/gnu-free" \
        -DPLD_aqt:BOOL=ON \
        -DPLD_ntk:BOOL=ON \
        -DPLD_pstex:BOOL=ON \
        -DPLD_svg:BOOL=ON \
        -DPLD_wxwidgets:BOOL=ON \
        -DPLPLOT_TK_VERSION=$tkver \
        -DPLPLOT_USE_QT5=ON \
%if %{with doc}
        -DXML_DECL:FILEPATH=/usr/share/sgml/xml.dcl \
        -DBUILD_DOC:BOOL=ON \
        -DBUILD_DOX_DOC:BOOL=ON \
%else
        -DPREBUILT_DOC:BOOL=ON \
%endif
        -DBUILD_TEST:BOOL=ON

%cmake_build


%install
%cmake_install

# Fix up tclIndex files so they are the same on all builds
#for file in $RPM_BUILD_ROOT%{_datadir}/plplot%{version}/examples/*/tclIndex
#do
   #grep '^[# ]' ${file} > tclIndex.hd
   #grep -v '^[# ]' ${file} | sort > tclIndex
   #cat tclIndex.hd tclIndex > ${file}
#done

#Don't pull in script interpreters for example binaries
find $RPM_BUILD_ROOT%{_datadir}/plplot%{version}/examples -type f | xargs chmod -x


%if %{with check}
%check
cp %SOURCE1 .
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
else
   Xorg=/usr/libexec/Xorg.bin
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -nolisten tcp -nolisten unix -logfile ./xorg.log -config ./xorg.conf -configdir . :99 &
export DISPLAY=:99
# Help bytecode-only arches find the OCaml stublib
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/bindings/ocaml:$RPM_BUILD_ROOT%{_libdir}
# Exclude ocaml from ppc/ppc64/ppc64le, arm
%ifarch ppc ppc64 ppc64le
%ctest --exclude-regex 'ocaml|octave'
%else
%ifarch %{arm} aarch64
%ctest --exclude-regex 'java|ocaml|octave'
%else
%ifarch s390x
# Most tests are segfaulting on s390x for some reason in F32+
%ctest || :
%else
# Octave tests are failing, ignore for now
%ctest --exclude-regex 'octave'
# Keep tabs on them though
%ctest --tests-regex 'octave' || :
%endif
%endif
%endif
%endif


%files
%{_bindir}/pltek
%{_bindir}/pstex2eps
%{python3_sitearch}/_plplotc.so
%{python3_sitearch}/plplot.py*
%{python3_sitearch}/plplotc.py*
%{python3_sitearch}/Plframe.py*
%{python3_sitearch}/TclSup.py*
%{python3_sitearch}/__pycache__/plplot.*
%{python3_sitearch}/__pycache__/plplotc.*
%{python3_sitearch}/__pycache__/Plframe.*
%{python3_sitearch}/__pycache__/TclSup.*
%{_infodir}/plplotdoc.info*
%{_mandir}/man1/pltek.1.gz
%{_mandir}/man1/pstex2eps.1.gz
%doc %dir %{_datadir}/plplot%{version}/examples
%doc %{_datadir}/plplot%{version}/examples/plplot-test.sh
%doc %{_datadir}/plplot%{version}/examples/plplot-test-interactive.sh
%doc %{_datadir}/plplot%{version}/examples/python/
%doc %{_datadir}/plplot%{version}/examples/test_python.sh
%doc %{_datadir}/plplot%{version}/examples/Chloe.pgm
%doc %{_datadir}/plplot%{version}/examples/README.Chloe

%files libs
%doc COPYING.LIB Copyright
%{_libdir}/libcsirocsa.so.0*
%{_libdir}/libcsironn.so.0*
%{_libdir}/libplplotcxx.so.15*
%{_libdir}/libplplot.so.17*
%{_libdir}/libplplotfortran.so.0*
%{_libdir}/libqsastime.so.0*
%dir %{_libdir}/plplot%{version}
%dir %{_libdir}/plplot%{version}/drivers
%{_libdir}/plplot%{version}/drivers/cairo.so
%{_libdir}/plplot%{version}/drivers/cairo.driver_info
%{_libdir}/plplot%{version}/drivers/mem.so
%{_libdir}/plplot%{version}/drivers/mem.driver_info
%{_libdir}/plplot%{version}/drivers/ntk.so
%{_libdir}/plplot%{version}/drivers/ntk.driver_info
%{_libdir}/plplot%{version}/drivers/null.so
%{_libdir}/plplot%{version}/drivers/null.driver_info
%{_libdir}/plplot%{version}/drivers/pdf.so
%{_libdir}/plplot%{version}/drivers/pdf.driver_info
%{_libdir}/plplot%{version}/drivers/ps.so
%{_libdir}/plplot%{version}/drivers/ps.driver_info
%{_libdir}/plplot%{version}/drivers/pstex.so
%{_libdir}/plplot%{version}/drivers/pstex.driver_info
%{_libdir}/plplot%{version}/drivers/psttf.so
%{_libdir}/plplot%{version}/drivers/psttf.driver_info
%{_libdir}/plplot%{version}/drivers/svg.so
%{_libdir}/plplot%{version}/drivers/svg.driver_info
%{_libdir}/plplot%{version}/drivers/xfig.so
%{_libdir}/plplot%{version}/drivers/xfig.driver_info
%{_libdir}/plplot%{version}/drivers/xwin.so
%{_libdir}/plplot%{version}/drivers/xwin.driver_info

%files data
%dir %{_datadir}/plplot%{version}
%{_datadir}/plplot%{version}/*.fnt
%{_datadir}/plplot%{version}/*.pal
%{_datadir}/plplot%{version}/*.sh*
%{_datadir}/plplot%{version}/ss/

%files devel
%{_includedir}/plplot/
%exclude %{_includedir}/plplot/pltcl.h
%exclude %{_includedir}/plplot/pltk.h
%exclude %{_includedir}/plplot/qt.h
%exclude %{_includedir}/plplot/wx*
%{_libdir}/cmake/plplot/
%{_libdir}/libcsirocsa.so
%{_libdir}/libcsironn.so
%{_libdir}/libplplotcxx.so
%{_libdir}/libplplot.so
%{_libdir}/libqsastime.so
%{_libdir}/pkgconfig/plplot.pc
%{_libdir}/pkgconfig/plplot-c++.pc
%doc %{_datadir}/plplot%{version}/examples/CMakeLists.txt
%doc %{_datadir}/plplot%{version}/examples/CTest*
%doc %dir %{_datadir}/plplot%{version}/examples/cmake
%doc %dir %{_datadir}/plplot%{version}/examples/cmake/modules
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/language_support.cmake
%if %{with ada}
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/language_support/
%endif
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/pkg-config.cmake
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/plplot_configure.cmake
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/plplot_functions.cmake
%doc %{_datadir}/plplot%{version}/examples/c/
%doc %{_datadir}/plplot%{version}/examples/c++/
%doc %{_datadir}/plplot%{version}/examples/Makefile
%doc %{_datadir}/plplot%{version}/examples/plplot_test/
%doc %{_datadir}/plplot%{version}/examples/test_c.sh
%doc %{_datadir}/plplot%{version}/examples/test_c_interactive.sh
%doc %{_datadir}/plplot%{version}/examples/test_cxx.sh
%doc %{_datadir}/plplot%{version}/examples/test_diff.sh

%{_mandir}/man3/pl*.3*

%files doc
%{_docdir}/%{name}/

%if %{with ada}
%files ada
%{_libdir}/libplplotada.so.4*

%files ada-devel
#Until we find an owner for %{_libdir}/ada/adalib/
%{_libdir}/ada/
#%{_libdir}/ada/adalib/plplotadad/
%{_libdir}/libplplotada.so
%{_libdir}/pkgconfig/plplot-ada.pc
#Until we find an owner for %{_datadir}/ada/adainclude/
%{_datadir}/ada/
#%{_datadir}/ada/adainclude/plplotadad/
%doc %{_datadir}/plplot%{version}/examples/ada/
%doc %{_datadir}/plplot%{version}/examples/test_ada.sh
%endif

%files fortran-devel
%{_fmoddir}/plfortrandemolib.mod
%{_fmoddir}/plplot.mod
%{_fmoddir}/plplot_double.mod
%{_fmoddir}/plplot_graphics.mod
%{_fmoddir}/plplot_private_exposed.mod
%{_fmoddir}/plplot_private_utilities.mod
%{_fmoddir}/plplot_single.mod
%{_fmoddir}/plplot_types.mod
%{_libdir}/libplplotfortran.so
%{_libdir}/libplfortrandemolib.a
%{_libdir}/pkgconfig/plplot-fortran.pc
%doc %{_datadir}/plplot%{version}/examples/fortran/
%doc %{_datadir}/plplot%{version}/examples/test_fortran.sh

%if %{with java}
%files java
%{_libdir}/plplot%{version}/libplplotjavac_wrap.so
%{_datadir}/java/plplot.jar

%files java-devel
%doc %{_datadir}/plplot%{version}/examples/java/
%doc %{_datadir}/plplot%{version}/examples/test_java.sh
%endif

%files lua
%{_libdir}/lua/plplot/
%doc %{_datadir}/plplot%{version}/examples/lua/
%doc %{_datadir}/plplot%{version}/examples/test_lua.sh

%if %{with ocaml}
%files -n ocaml-plplot
# %%dir %%{_libdir}/ocaml/plcairo/
# %%{_libdir}/ocaml/plcairo/META
# %%{_libdir}/ocaml/plcairo/*.cma
# %%{_libdir}/ocaml/plcairo/*.cmi
%dir %{_libdir}/ocaml/plplot/
%{_libdir}/ocaml/plplot/META
%{_libdir}/ocaml/plplot/*.cma
%{_libdir}/ocaml/plplot/*.cmi
%{_libdir}/ocaml/stublibs/*

%files -n ocaml-plplot-devel
%{_libdir}/pkgconfig/plplot-ocaml.pc
# %%{_libdir}/ocaml/plcairo/*.a
# %%{_libdir}/ocaml/plcairo/*.cmxa
# %%{_libdir}/ocaml/plcairo/plcairo.mli
%{_libdir}/ocaml/plplot/*.a
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/plplot/*.cmx*
%endif
%{_libdir}/ocaml/plplot/plplot.mli
%doc %{_datadir}/plplot%{version}/examples/ocaml/
%doc %{_datadir}/plplot%{version}/examples/test_ocaml.sh
%endif

%if %{with octave}
%files octave
%{_datadir}/plplot_octave/
%{_datadir}/octave/site/m/PLplot/
%{_libdir}/octave/site/oct/*/plplot_octave.oct
%doc %{_datadir}/plplot%{version}/examples/octave/
%doc %{_datadir}/plplot%{version}/examples/test_octave.sh
%doc %{_datadir}/plplot%{version}/examples/test_octave_interactive.sh
%endif

%files pyqt
%{python3_sitearch}/plplot_pyqt5.so

%files qt
%{_libdir}/libplplotqt.so.2*
%{_libdir}/plplot%{version}/drivers/qt.so
%{_libdir}/plplot%{version}/drivers/qt.driver_info

%files qt-devel
%{_includedir}/plplot/qt.h
%{_libdir}/libplplotqt.so
%{_libdir}/pkgconfig/plplot-qt.pc
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/ndp_UseQt4.cmake

%files tk
%{_bindir}/plserver
%{_bindir}/pltcl
%{_libdir}/libplplottcltk.so.14*
%{_libdir}/libplplottcltk_Main.so.1*
%{_libdir}/libtclmatrix.so.10*
%{_libdir}/plplot%{version}/drivers/tk.so
%{_libdir}/plplot%{version}/drivers/tk.driver_info
%{_libdir}/plplot%{version}/drivers/tkwin.so
%{_libdir}/plplot%{version}/drivers/tkwin.driver_info
%{python3_sitearch}/_Pltk_init.so
%{python3_sitearch}/Pltk_init.py
%{python3_sitearch}/__pycache__/Pltk_init.*

%{_datadir}/plplot%{version}/pkgIndex.tcl
%doc %{_datadir}/plplot%{version}/examples/test_tcl.sh
%doc %{_datadir}/plplot%{version}/examples/tcl/
%doc %{_datadir}/plplot%{version}/examples/tk/
%{_datadir}/plplot%{version}/tcl/
%{_mandir}/man1/plserver.1.gz
%{_mandir}/man1/pltcl.1.gz

%files tk-devel
%{_includedir}/plplot/pltcl.h
%{_includedir}/plplot/pltk.h
%{_libdir}/libplplottcltk.so
%{_libdir}/libplplottcltk_Main.so
%{_libdir}/libtclmatrix.so
%{_libdir}/pkgconfig/plplot-tcl.pc
%{_libdir}/pkgconfig/plplot-tcl_Main.pc

%files wxGTK
%{_bindir}/wxPLViewer
%{_libdir}/libplplotwxwidgets.so.1*
%{_libdir}/plplot%{version}/drivers/wxwidgets.so
%{_libdir}/plplot%{version}/drivers/wxwidgets.driver_info

%files wxGTK-devel
%{_includedir}/plplot/wx*
%{_libdir}/libplplotwxwidgets.so
%{_libdir}/pkgconfig/plplot-wxwidgets.pc


%changelog
%autochangelog
