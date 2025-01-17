# Disable package note flags, since root saves the compiler/linker flags
# used during the build
%undefine _package_note_flags

%global root7 1
%global dataframe 1
%global roofit 1
%global tmvasofieparser 1
%global distrdf %{dataframe}

%global bundlejson 0

%if %{?fedora}%{!?fedora:0}
%ifarch %{ix86} %{arm}
%global pandas 0
%else
%global pandas 1
%endif
%else
%global pandas 0
%endif

%if %{?rhel}%{!?rhel:0} == 10
# R not yet available in EPEL 10
%global rrr 0
%else
%global rrr 1
%endif

%if %{?fedora}%{!?fedora:0} >= 40
%global roofitmp 1
%else
%global roofitmp 0
%endif

# Do not generate autoprovides for Python modules
%global __provides_exclude_from ^%{python3_sitearch}/lib.*\\.so$

Name:		root
Version:	6.34.02
%global libversion %(cut -d. -f 1-2 <<< %{version})
Release:	3%{?dist}
Summary:	Numerical data analysis framework

License:	LGPL-2.1-or-later
URL:		https://root.cern/
#		The upstream source is modified to exclude proprietary fonts
#		See Source8 for how to create Source0
Source0:	%{name}-%{version}.tar.xz
#		Input data for the tests
Source1:	%{name}-testfiles.tar.xz
#		Script to generate above source
Source2:	%{name}-testfiles.sh
#		Desktop file and icon
Source3:	%{name}.desktop
Source4:	%{name}.png
#		MIME type file and icon
Source5:	%{name}.xml
Source6:	application-x-root.png
#		Instructions for setting up a python virtual environment
#		for running the JupyROOT notebook on EPEL
Source7:	JupyROOT-on-EPEL
#		Script to generate Source0
Source8:	%{name}-get-src.sh
#		Clad is a source-transformation automatic differentiation (AD)
#		library for C++, implemented as a plugin for the Clang compiler
Source9:	https://github.com/vgvassilev/clad/archive/v1.7/clad-1.7.tar.gz
#		Use system fonts
Patch0:		%{name}-fontconfig.patch
#		Reduce memory usage during linking on ARM and x86 by generating
#		smaller debuginfo for the llvm libraries
#		Fedora builders run out of memory with the default setting
Patch1:		%{name}-memory-arm-x86.patch
#		Don't install minicern static library
Patch2:		%{name}-dont-install-minicern.patch
#		Do not export Python modules in CMake config
Patch3:		%{name}-no-export-python-modules.patch
#		Run some test on 32 bit that upstream has disabled
Patch4:		%{name}-32bit-tests.patch
#		Fix compilation of TMVA SOFIE parser on s390x
#		https://github.com/root-project/root/pull/17307
Patch5:		%{name}-Fix-compilation-on-s390x.patch
#		Make -DCLAD_SOURCE_DIR option work
#		https://github.com/root-project/root/pull/17308
Patch6:		%{name}-Make-DCLAD_SOURCE_DIR-option-work.patch
#		Fix segmentation fault during testing on ix86
#		https://github.com/root-project/root/pull/17314
Patch7:		%{name}-tmva-sofie-Fix-Tile-operator.patch
#		Adjust test/stressGraphics.ref
#		https://github.com/root-project/root/pull/17398
Patch8:		%{name}-Adjust-test-stressGraphics.ref.patch

BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	make
#		root on Linux requires cmake 3.16
#		but 3.19 is needed for flexiblas support
BuildRequires:	cmake >= 3.19
BuildRequires:	libX11-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXft-devel
BuildRequires:	libXext-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fcgi-devel
BuildRequires:	ftgl-devel
BuildRequires:	gl2ps-devel
BuildRequires:	glew-devel
BuildRequires:	pcre2-devel
BuildRequires:	zlib-devel
BuildRequires:	xz-devel
BuildRequires:	lz4-devel
BuildRequires:	xxhash-devel
BuildRequires:	libzstd-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	ncurses-devel
BuildRequires:	libxml2-devel
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	unuran-devel
BuildRequires:	mariadb-connector-c-devel
BuildRequires:	sqlite-devel
BuildRequires:	unixODBC-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	libpq-devel
BuildRequires:	python%{python3_pkgversion}-devel >= 3.7
BuildRequires:	python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-numpy
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtwebengine-devel
%endif
%ifarch %{qt6_qtwebengine_arches}
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtwebengine-devel
%endif
BuildRequires:	openssl-devel
%if %{?fedora}%{!?fedora:0} >= 41
#		Needed by civetweb.c in root-net-http
BuildRequires:	openssl-devel-engine
%endif
BuildRequires:	libtool-ltdl-devel
BuildRequires:	desktop-file-utils
BuildRequires:	dcap-devel
BuildRequires:	xrootd-client-devel >= 1:5.0.0
BuildRequires:	cfitsio-devel
#		Davix version >= 0.6.4, but not between 0.6.8 and 0.7.0
BuildRequires:	davix-devel >= 0.7.1
%if %{rrr}
BuildRequires:	R-Rcpp-devel
BuildRequires:	R-RInside-devel
%endif
BuildRequires:	readline-devel
BuildRequires:	tbb-devel >= 2020
BuildRequires:	libuuid-devel
BuildRequires:	graphviz-devel
BuildRequires:	expat-devel
BuildRequires:	pythia8-devel >= 8.1.80
BuildRequires:	flexiblas-devel
%if ! %{bundlejson}
BuildRequires:	json-devel >= 3.9
%endif
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 9
#		Disable uring in EPEL 8 (liburing is available,
#		but uring not supported by the RHEL 8 kernel)
#		Supported by the RHEL kernel since RHEL 9.3
BuildRequires:	liburing-devel
%endif
%if %{tmvasofieparser}
BuildRequires:	protobuf-devel >= 3.0
%endif
%ifnarch %{ix86} %{arm}
BuildRequires:	libarrow-devel
%endif
%if %{roofit}
%if %{roofitmp}
#		Required for roofit-multiprocess
#		Requires new zeromq with zmq_ppoll
BuildRequires:	zeromq-devel >= 4.3.5
BuildRequires:	cppzmq-devel
%endif
%endif
%if %{pandas}
BuildRequires:	python%{python3_pkgversion}-pandas
%endif
BuildRequires:	python%{python3_pkgversion}-rcssmin
BuildRequires:	uglify-js3
BuildRequires:	perl-generators
BuildRequires:	gtest-devel
BuildRequires:	gmock-devel
#		Fonts
BuildRequires:	font(freesans)
BuildRequires:	font(freeserif)
BuildRequires:	font(freemono)
BuildRequires:	font(standardsymbolsps)
BuildRequires:	font(d050000l)
BuildRequires:	font(z003)
BuildRequires:	font(droidsansfallback)
#		With gdb installed test failures will show backtraces
BuildRequires:	gdb
#		Defines _jsdir
BuildRequires:	web-assets-devel
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-multiproc%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	emacs-%{name} < 5.34.28
Obsoletes:	emacs-%{name}-el < 5.34.28

%description
The ROOT system provides a set of object oriented frameworks with all
the functionality needed to handle and analyze large amounts of data
in a very efficient way. Having the data defined as a set of objects,
specialized storage methods are used to get direct access to the
separate attributes of the selected objects, without having to touch
the bulk of the data. Included are histogramming methods in an
arbitrary number of dimensions, curve fitting, function evaluation,
minimization, graphics and visualization classes to allow the easy
setup of an analysis system that can query and process the data
interactively or in batch mode, as well as a general parallel
processing framework, PROOF, that can considerably speed up an
analysis.

Thanks to the built-in C++ interpreter cling, the command, the
scripting and the programming language are all C++. The interpreter
allows for fast prototyping of the macros since it removes the, time
consuming, compile/link cycle. It also provides a good environment to
learn C++. If more performance is needed the interactively developed
macros can be compiled using a C++ compiler via a machine independent
transparent compiler interface called ACliC.

The system has been designed in such a way that it can query its
databases in parallel on clusters of workstations or many-core
machines. ROOT is an open system that can be dynamically extended by
linking external libraries. This makes ROOT a premier platform on
which to build data acquisition, simulation and data analysis systems.

%package icons
Summary:	ROOT icon collection
BuildArch:	noarch
Requires:	%{name}-core = %{version}-%{release}

%description icons
This package contains icons used by the ROOT GUI.

%package fonts
Summary:	ROOT font collection
BuildArch:	noarch
#		STIX version 0.9 only
License:	OFL-1.1
Requires:	%{name}-core = %{version}-%{release}

%description fonts
This package contains fonts used by ROOT that are not available in Fedora.
In particular it contains STIX version 0.9 that is used by TMathText.

%package tutorial
Summary:	ROOT tutorial scripts and test suite
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description tutorial
This package contains the tutorial scripts and test suite for ROOT.

%package core
Summary:	ROOT core libraries
License:	LGPL-2.1-or-later AND LGPL-2.0-or-later AND ISC AND MIT AND NCSA
Requires:	%{name}-fonts = %{version}-%{release}
Requires:	%{name}-icons = %{version}-%{release}
#		Dynamic dependencies
Requires:	%{name}-cling%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-asimage%{?_isa} = %{version}-%{release}
#		Packages providing the libraries listed by "root-config --libs"
#		(Only root-physics and root-multiproc are not dragged in by
#		recursively resolving the dependency on root-graf-asimage
#		above, so it is not that much of a bloat...)
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-postscript%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-multiproc%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-physics%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
%if %{dataframe}
Requires:	%{name}-tree-dataframe%{?_isa} = %{version}-%{release}
%endif
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}
Requires:	%{name}-vecops%{?_isa} = %{version}-%{release}
#		To resolve dependency in installed ROOTConfig.cmake
%if %{bundlejson}
Provides:	bundled(json-devel) = 3.10.5
%else
Requires:	json-devel >= 3.9
%endif
#		Fonts
Requires:	xorg-x11-fonts-ISO8859-1-75dpi
Requires:	font(freesans)
Requires:	font(freeserif)
Requires:	font(freemono)
Requires:	font(standardsymbolsps)
Requires:	font(d050000l)
Requires:	font(z003)
Requires:	font(droidsansfallback)
Obsoletes:	%{name}-ruby < 6.00.00
Obsoletes:	%{name}-vdt < 6.10.00
Obsoletes:	%{name}-proof-pq2 < 6.16.00
Obsoletes:	%{name}-rootd < 6.16.00
Obsoletes:	%{name}-geocad < 6.18.00
Obsoletes:	%{name}-graf-qt < 6.18.00
Obsoletes:	%{name}-gui-qt < 6.18.00
Obsoletes:	%{name}-gui-qtgsi < 6.18.00
Obsoletes:	%{name}-io-hdfs < 6.18.00
Obsoletes:	%{name}-io-rfio < 6.18.00
Obsoletes:	%{name}-net-bonjour < 6.18.00
Obsoletes:	%{name}-net-globus < 6.18.00
Obsoletes:	%{name}-net-ldap < 6.18.00
Obsoletes:	%{name}-net-krb5 < 6.18.00
Obsoletes:	%{name}-table < 6.18.00
Obsoletes:	%{name}-memstat < 6.26.00
Obsoletes:	%{name}-montecarlo-vmc < 6.26.00
Obsoletes:	%{name}-doc < 6.26.00
Obsoletes:	%{name}-io-gfal < 6.30.00
Obsoletes:	%{name}-roofit-common < 6.30.00

%description core
This package contains the core libraries used by ROOT: libCore, libNew,
libRint and libThread.

%package multiproc
Summary:	Multi-processor support for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description multiproc
This package provides ROOT's multi-processor support library: libMultiProc.

%package cling
Summary:	Cling C++ interpreter
License:	(NCSA OR LGPL-2.1-only) AND (Apache-2.0 WITH LLVM-exception OR NCSA) AND BSD-2-Clause AND BSD-3-Clause AND MIT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
#		Root's cling interpreter uses a particular git commit of
#		llvm and clang with application specific changes. It does
#		not work with the system libraries. The bundled llvm and
#		clang are compiled using -fvisibility=hidden, and are not
#		visible outside of the libCling module.
Provides:	bundled(clang-libs)
Provides:	bundled(llvm-libs)
Requires:	gcc-c++
Requires:	redhat-rpm-config
Obsoletes:	%{name}-cint7 < 5.26.00c
Obsoletes:	%{name}-cint < 6.00.00
Obsoletes:	%{name}-cintex < 6.00.00
Obsoletes:	%{name}-reflex < 6.00.00

%description cling
Cling is an interactive C++ interpreter, built on top of Clang and
LLVM compiler infrastructure.

%package testsupport
Summary:	Unit test support library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description testsupport
This package contains the unit test support library for ROOT.

%package tpython
Summary:	ROOT's TPython interface
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-%{name}%{?_isa} = %{version}-%{release}
#		Package split (tpython from Python bindings)
Obsoletes:	python%{python3_pkgversion}-%{name} < 6.22.00

%description tpython
This package contains ROOT's TPython interface. It makes it possible
to call Python from ROOT.

%package -n python%{python3_pkgversion}-%{name}
Summary:	Python extension for ROOT
%py_provides	python%{python3_pkgversion}-%{name}
Provides:	%{name}-python%{python3_pkgversion} = %{version}-%{release}
Obsoletes:	%{name}-python%{python3_pkgversion} < 6.08.00
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split (tpython from Python bindings)
Obsoletes:	python%{python3_pkgversion}-%{name} < 6.22.00
#		JsMVA python module is now a submodule of ROOT python module
Provides:	python%{python3_pkgversion}-jsmva = %{version}-%{release}
Obsoletes:	python%{python3_pkgversion}-jsmva < 6.32.00

%description -n python%{python3_pkgversion}-%{name}
This package contains the Python extension for ROOT. It makes it
possible to use ROOT classes in Python.

%package -n python%{python3_pkgversion}-jupyroot
Summary:	ROOT Jupyter kernel
BuildArch:	noarch
%py_provides	python%{python3_pkgversion}-jupyroot
Requires:	python%{python3_pkgversion}-%{name} = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
#		notebook package was merged with JupyROOT package
Provides:	%{name}-notebook = %{version}-%{release}
Obsoletes:	%{name}-notebook < 6.32.00
Requires:	js-jsroot >= 7.8
%if %{?fedora}%{!?fedora:0}
#		jupyter-notebook not available in RHEL/EPEL
#		some functionality missing
Requires:	jupyter-notebook
#		python-metakernel not available in RHEL/EPEL
#		some functionality missing
Requires:	python%{python3_pkgversion}-ipython
Requires:	python%{python3_pkgversion}-metakernel
Requires:	python-jupyter-filesystem
%endif

%description -n python%{python3_pkgversion}-jupyroot
The Jupyter kernel for the ROOT notebook.

%if %{distrdf}
%package -n python%{python3_pkgversion}-distrdf
Summary:	Distributed RDataFrame
BuildArch:	noarch
%py_provides	python%{python3_pkgversion}-distrdf
Requires:	python%{python3_pkgversion}-%{name} = %{version}-%{release}
Requires:	%{name}-tree-dataframe = %{version}-%{release}

%description -n python%{python3_pkgversion}-distrdf
A layer on top of RDataFrame to enable distributed computations. It is
a port of the previously known PyRDF python package.
%endif

%if %{rrr}
%package r
Summary:	R interface for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	R-Rcpp-devel
Requires:	R-RInside-devel

%description r
ROOT R is an interface in ROOT to call R functions using an R C++
interface. This interface opens the possibility in ROOT to use the
very large set of mathematical and statistical tools provided by R.
With ROOT R you can perform a conversion from ROOT's C++ objects to
R's objects, transform the returned R objects into ROOT's C++ objects,
then the R functionality can be used directly for statistical studies
in ROOT.

%package r-tools
Summary:	R Tools
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-r%{?_isa} = %{version}-%{release}

%description r-tools
This package contains a minimizer module for ROOT that uses the ROOT
R interface.
%endif

%package genetic
Summary:	Genetic algorithms for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva%{?_isa} = %{version}-%{release}

%description genetic
This package contains a genetic minimizer module for ROOT.

%package geom
Summary:	Geometry library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
#		Package split (geom-builder and geom-painter from geom)
Obsoletes:	%{name}-geom < 6.28.00

%description geom
This package contains a library for defining geometries in ROOT.

%package geom-builder
Summary:	Geometry builder library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
#		Package split (geom-builder and geom-painter from geom)
Obsoletes:	%{name}-geom < 6.28.00

%description geom-builder
This package contains a library for building geometries in ROOT.

%package geom-painter
Summary:	Geometry painter library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split (geom-builder and geom-painter from geom)
Obsoletes:	%{name}-geom < 6.28.00

%description geom-painter
This package contains a library for drawing geometries in ROOT.

%package gdml
Summary:	GDML import/export for ROOT geometries
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xml%{?_isa} = %{version}-%{release}

%description gdml
This package contains an import/export module for ROOT geometries.

%package graf
Summary:	2D graphics library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description graf
This package contains the 2-dimensional graphics library for ROOT.

%package graf-asimage
Summary:	AfterImage graphics renderer for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-postscript%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description graf-asimage
This package contains the AfterImage renderer for ROOT, which allows
you to store output graphics in many formats, including JPEG, PNG and
TIFF.

%package graf-fitsio
Summary:	ROOT interface for the Flexible Image Transport System (FITS)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description graf-fitsio
This package contains a library for using the Flexible Image Transport
System (FITS) data format in root.

%package graf-gpad
Summary:	Canvas and pad library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
#		Dynamic dependency
Requires:	%{name}-graf-postscript%{?_isa} = %{version}-%{release}

%description graf-gpad
This package contains a library for canvas and pad manipulations.

%package graf-gviz
Summary:	Graphviz 2D library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}

%description graf-gviz
This package contains the 2-dimensional graphviz library for ROOT.

%package graf-postscript
Summary:	Postscript/PDF renderer library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}

%description graf-postscript
This package contains a library for ROOT, which allows rendering
postscript and PDF output.

%package graf-x11
Summary:	X window system renderer for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}

%description graf-x11
This package contains the X11 renderer for ROOT, which allows using an
X display for showing graphics.

%package graf3d
Summary:	Basic 3D shapes library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description graf3d
This library contains the basic 3D shapes and classes for ROOT. For
a more full-blown geometry library, see the root-geom package.

%package graf3d-csg
Summary:	Constructive solid geometry
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description graf3d-csg
This library is used to generate composite shapes.

%package graf3d-eve
Summary:	Event display library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-gl%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-montecarlo-eg%{?_isa} = %{version}-%{release}
Requires:	%{name}-physics%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description graf3d-eve
This package contains a library for defining event displays in ROOT.

%package graf3d-gl
Summary:	GL renderer for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-asimage%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-csg%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description graf3d-gl
This package contains the GL renderer for ROOT. This library provides
3D rendering of volumes and shapes defined in ROOT, as well as 3D
rendering of histograms, and similar. Included is also a high quality
3D viewer for ROOT defined geometries.

%package graf3d-gviz3d
Summary:	Graphviz 3D library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-gl%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}

%description graf3d-gviz3d
This package contains the 3-dimensional graphviz library for ROOT.

%package graf3d-x3d
Summary:	X 3D renderer for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}

%description graf3d-x3d
This package contains the X 3D renderer for ROOT. This library provides
3D rendering of volumes and shapes defined in ROOT. Included is also
a low quality 3D viewer for ROOT defined geometries.

%package gui
Summary:	GUI library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
#		Dynamic dependencies
Requires:	%{name}-graf-x11%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
#		Package split (gui-html from gui)
Obsoletes:	%{name}-gui < 6.14.00

%description gui
This package contains a library for defining graphical user interfaces.

%package gui-html
Summary:	HTML GUI library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
#		Package split (gui-html from gui)
Obsoletes:	%{name}-gui < 6.14.00

%description gui-html
This package contains a library for defining HTML graphical user interfaces.

%package gui-fitpanel
Summary:	GUI element for fits in ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description gui-fitpanel
This package contains a library to show a pop-up dialog when fitting
various kinds of data.

%package gui-ged
Summary:	GUI element for editing various ROOT objects
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Dynamic dependency
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description gui-ged
This package contains a library to show a pop-up window for editing
various ROOT objects.

%package gui-builder
Summary:	GUI editor library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
#		Package renamed
Provides:	%{name}-guibuilder = %{version}-%{release}
Provides:	%{name}-guibuilder%{?_isa} = %{version}-%{release}
Obsoletes:	%{name}-guibuilder < 6.14.00

%description gui-builder
This package contains a library for editing graphical user interfaces
in ROOT.

%package gui-recorder
Summary:	Interface for recording and replaying events in ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description gui-recorder
This library provides interface for recording and replaying events in ROOT.
Recorded events are:
 - Commands typed by user in command line ('new TCanvas')
 - GUI events (mouse movement, button clicks, ...)
All the recorded events from one session are stored in one TFile
and can be replayed again anytime.

%package hbook
Summary:	Hbook library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description hbook
This package contains the Hbook library for ROOT, allowing you to
access legacy Hbook files (NTuples and Histograms from PAW).

%package hist
Summary:	Histogram library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
#		Dynamic dependency
Requires:	%{name}-hist-painter%{?_isa} = %{version}-%{release}

%description hist
This package contains a library for histogramming in ROOT.

%package hist-painter
Summary:	Histogram painter plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description hist-painter
This package contains a painter of histograms for ROOT.

%package spectrum
Summary:	Spectra analysis library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}

%description spectrum
This package contains the Spectrum library for ROOT.

%package spectrum-painter
Summary:	Spectrum painter plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}

%description spectrum-painter
This package contains a painter of spectra for ROOT.

%package html
Summary:	HTML documentation generator for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	graphviz

%description html
This package contains classes to automatically extract documentation
from marked up sources.

%package io
Summary:	Input/output of ROOT objects
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 9
Requires:	liburing-devel
%endif

%description io
This package provides I/O routines for ROOT objects.

%package io-dcache
Summary:	dCache input/output library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description io-dcache
This package contains the dCache extension for ROOT.

%package io-sql
Summary:	SQL input/output library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description io-sql
This package contains the SQL extension for ROOT, that allows
transparent access to files data via an SQL database, using ROOT's
TFile interface.

%package io-xml
Summary:	XML reader library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
#		Package split (io-xmlparser from io-xml)
Obsoletes:	%{name}-io-xml < 6.14.00

%description io-xml
This package contains the XML reader library for ROOT.

%package io-xmlparser
Summary:	XML parser library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
#		Package split (io-xmlparser from io-xml)
Obsoletes:	%{name}-io-xml < 6.14.00

%description io-xmlparser
This package contains the XML parser library for ROOT.

%package foam
Summary:	A Compact Version of the Cellular Event Generator
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description foam
The general-purpose self-adapting Monte Carlo (MC) event
generator/simulator mFOAM (standing for mini-FOAM) is a new compact
version of the FOAM program, with a slightly limited functionality
with respect to its parent version. On the other hand, mFOAM is
easier to use for the average user.

%package fftw
Summary:	FFTW library for ROOT
License:	GPL-2.0-or-later
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description fftw
This package contains the Fast Fourier Transform extension for ROOT.
It uses the very fast fftw (version 3) library.

%package fumili
Summary:	Fumili library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description fumili
This package contains the fumili library for ROOT. This provides an
alternative fitting algorithm for ROOT.

%package genvector
Summary:	Generalized vector library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description genvector
This package contains the Genvector library for ROOT. This provides
a generalized vector library.

%package mathcore
Summary:	Core mathematics library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
#		Dynamic dependencies
Requires:	%{name}-mathmore%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit2%{?_isa} = %{version}-%{release}

%description mathcore
This package contains the MathCore library for ROOT.

%package mathmore
Summary:	GSL interface library for ROOT
License:	GPL-2.0-or-later
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description mathmore
This package contains the MathMore library for ROOT. This provides
a partial GNU Scientific Library interface for ROOT.
While the rest of root is licensed under LGPLv2+ this optional library
is licensed under GPLv2+ due to its use of GSL.

%package matrix
Summary:	Matrix library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description matrix
This package contains the Matrix library for ROOT.

%package minuit
Summary:	Minuit library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description minuit
This package contains the MINUIT library for ROOT. This provides a
fitting algorithm for ROOT.

%package minuit2
Summary:	Minuit version 2 library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description minuit2
This package contains the MINUIT version 2 library for ROOT. This
provides an fitting algorithm for ROOT.

%package mlp
Summary:	Multi-layer perceptron extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description mlp
This package contains the mlp library for ROOT. This library provides
a multi-layer perceptron neural network package for ROOT.

%package physics
Summary:	Physics library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description physics
This package contains the physics library for ROOT.

%package quadp
Summary:	QuadP library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description quadp
This package contains the QuadP library for ROOT. This provides the a
framework in which to do Quadratic Programming. The quadratic
programming problem involves minimization of a quadratic function
subject to linear constraints.

%package smatrix
Summary:	Sparse matrix library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description smatrix
This package contains the Smatrix library for ROOT.

%package splot
Summary:	Splot library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description splot
A common method used in High Energy Physics to perform measurements
is the maximum Likelihood method, exploiting discriminating variables
to disentangle signal from background. The crucial point for such an
analysis to be reliable is to use an exhaustive list of sources of
events combined with an accurate description of all the Probability
Density Functions (PDF).

To assess the validity of the fit, a convincing quality check is to
explore further the data sample by examining the distributions of
control variables. A control variable can be obtained for instance by
removing one of the discriminating variables before performing again
the maximum Likelihood fit: this removed variable is a control
variable. The expected distribution of this control variable, for
signal, is to be compared to the one extracted, for signal, from the
data sample. In order to be able to do so, one must be able to unfold
from the distribution of the whole data sample.

The SPlot method allows to reconstruct the distributions for the
control variable, independently for each of the various sources of
events, without making use of any a priori knowledge on this
variable. The aim is thus to use the knowledge available for the
discriminating variables to infer the behavior of the individual
sources of events with respect to the control variable.

SPlot is optimal if the control variable is uncorrelated with the
discriminating variables.

%package unuran
Summary:	Random number generator library
License:	GPL-2.0-or-later
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description unuran
Contains universal (also called automatic or black-box) algorithms
that can generate random numbers from large classes of continuous or
discrete distributions, and also from practically all standard
distributions.

To generate random numbers the user must supply some information
about the desired distribution, especially a C-function that computes
the density and - depending on the chosen methods - some additional
information (like the borders of the domain, the mode, the derivative
of the density ...). After a user has given this information an
init-program computes all tables and constants necessary for the
random variate generation. The sample program can then generate
variates from the desired distribution.

%package vecops
Summary:	Vector operation extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
#		Library split (tree-dataframe and vecops from tree-player)
Obsoletes:	%{name}-tree-player < 6.14.00

%description vecops
This package contains a vector operation extension for ROOT.

%package montecarlo-eg
Summary:	Event generator library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description montecarlo-eg
This package contains an event generator library for ROOT.

%package montecarlo-pythia8
Summary:	Pythia version 8 plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-montecarlo-eg%{?_isa} = %{version}-%{release}

%description montecarlo-pythia8
This package contains the Pythia version 8 plug-in for ROOT. This
package provides the ROOT user with transparent interface to the Pythia
(version 8) event generators for hadronic interactions. If the term
"hadronic" does not ring any bells, this package is not for you.

%package net
Summary:	Net library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description net
This package contains the ROOT networking library.

%package net-rpdutils
Summary:	Authentication utilities used by xproofd
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description net-rpdutils
This package contains authentication utilities used by xproofd.

%package net-auth
Summary:	Authentication extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description net-auth
This package contains the basic authentication algorithms used by ROOT.

%package net-davix
Summary:	Davix extension for ROOT
Requires:	davix-libs%{?_isa} >= 0.6.4
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description net-davix
This package contains the davix extension for ROOT, that provides
access to http based storage such as webdav and S3.

%package net-http
Summary:	HTTP server extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	js-jsroot >= 7.8
#		Library split (net-httpsniff from net-http)
Obsoletes:	%{name}-net-http < 6.14.00

%description net-http
This package contains the HTTP server extension for ROOT. It provides
an http interface to arbitrary ROOT applications.

%package net-httpsniff
Summary:	HTTP sniffer extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xml%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Library split (net-httpsniff from net-http)
Obsoletes:	%{name}-net-http < 6.14.00

%description net-httpsniff
This package contains the HTTP sniffer extension for ROOT.

%package netx
Summary:	NetX extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description netx
This package contains the NetX extension for ROOT, i.e. a client for
the xrootd server. Only the new (NetXNG) version is provided.

%package proof
Summary:	PROOF extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Obsoletes:	%{name}-clarens < 5.34.01
Obsoletes:	%{name}-peac < 5.34.01
#		Package split (proof-player from proof)
Obsoletes:	%{name}-proof < 6.14.00
Obsoletes:	%{name}-proofd < 6.16.00
Obsoletes:	%{name}-xproof < 6.22.08-2

%description proof
This package contains the proof extension for ROOT. This provides a
client to use in a PROOF environment.

%package proof-bench
Summary:	PROOF benchmarking
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-proof%{?_isa} = %{version}-%{release}
Requires:	%{name}-proof-player%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description proof-bench
This package contains the steering class for PROOF benchmarks.

%package proof-player
Summary:	PROOF player extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-proof%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}
#		Package split (proof-player from proof)
Obsoletes:	%{name}-proof < 6.14.00

%description proof-player
This package contains the proof player extension for ROOT.

%package proof-sessionviewer
Summary:	GUI to browse an interactive PROOF session
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-proof%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description proof-sessionviewer
This package contains a library for browsing an interactive PROOF
session in ROOT.

%if %{roofit}
%package roofit
Summary:	ROOT extension for modeling expected distributions - toolkit
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-batchcompute%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split / Library split (from roofit)
Obsoletes:	%{name}-roofit < 6.20.00

%description roofit
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains the RooFit toolkit classes.

%package roofit-core
Summary:	ROOT extension for modeling expected distributions - core
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-foam%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit2%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-batchcompute%{?_isa} = %{version}-%{release}
%if %{roofitmp}
Requires:	%{name}-roofit-multiprocess%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-zmq%{?_isa} = %{version}-%{release}
%endif
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split / Library split (from roofit)
Obsoletes:	%{name}-roofit < 6.20.00
#		Dataframe helpers are now part of core
Obsoletes:	%{name}-roofit-dataframe-helpers < 6.34.00

%description roofit-core
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains the core RooFit classes.

%package roofit-more
Summary:	ROOT extension for modeling expected distributions - more
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathmore%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
#		Package split / Library split (from roofit)
Obsoletes:	%{name}-roofit < 6.20.00

%description roofit-more
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains RooFit classes that use the mathmore library.

%package roofit-batchcompute
Summary:	Optimized computation functions for PDFs
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description roofit-batchcompute
While fitting, a significant amount of time and processing power is
spent on computing the probability function for every event and PDF
involved in the fitting model. To speed up this process, roofit can
use the computation functions provided in this library. The functions
provided here process whole data arrays (batches) instead of a single
event at a time, as in the legacy evaluate() function in roofit. In
addition, the code is written in a manner that allows for compiler
optimizations, notably auto-vectorization. This library is compiled
multiple times for different vector instuction set architectures and
the optimal code is executed during runtime, as a result of an
automatic hardware detection mechanism that this library contains.

%package roofit-hs3
Summary:	RooFit HS3
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist-factory%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-jsoninterface%{?_isa} = %{version}-%{release}

%description roofit-hs3
When using RooFit, statistical models can be conveniently handled and
stored as a RooWorkspace. However, for the sake of interoperability
with other statistical frameworks, and also ease of manipulation, it
may be useful to store statistical models in text form. This library
sets out to achieve exactly that, exporting to and importing from JSON
and YML.

%package roofit-jsoninterface
Summary:	JSON interface to RooFit
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description roofit-jsoninterface
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains the JSON interface to RooFit.

%if %{roofitmp}
%package roofit-multiprocess
Summary:	Multi-process support for RooFit
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-zmq%{?_isa} = %{version}-%{release}

%description roofit-multiprocess
This package contains a library providing classes that implements
mult-process support for RooFit.

%package roofit-zmq
Summary:	ZeroMQ interface library for RooFit
License:	BSD-2-Clause

%description roofit-zmq
This package contains a helper library used by RooFit::MultiProcess to
interface to the ZeroMQ library.
%endif

%package roostats
Summary:	Statistical tools built on top of RooFit
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split / Library split (from roofit)
Obsoletes:	%{name}-roofit < 6.20.00

%description roostats
RooStats is a package containing statistical tools built on top of
RooFit.

%package hist-factory
Summary:	RooFit PDFs from ROOT histograms
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xmlparser%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-jsoninterface%{?_isa} = %{version}-%{release}
Requires:	%{name}-roostats%{?_isa} = %{version}-%{release}

%description hist-factory
Create RooFit probability density functions from ROOT histograms.

%package xroofit
Summary:	Extra tools for RooFit projects
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-fitpanel%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist-factory%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-hs3%{?_isa} = %{version}-%{release}
Requires:	%{name}-roostats%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description xroofit
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains extra tools for RooFit projects.
%endif

%package sql-mysql
Summary:	MySQL client plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description sql-mysql
This package contains the MySQL plugin for ROOT. This plugin
provides a thin client (interface) to MySQL servers. Using this
client, one can obtain information from a MySQL database into the
ROOT environment.

%package sql-odbc
Summary:	ODBC plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description sql-odbc
This package contains the ODBC (Open DataBase Connectivity) plugin
for ROOT, that allows transparent access to any kind of database that
supports the ODBC protocol.

%package sql-sqlite
Summary:	Sqlite client plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description sql-sqlite
This package contains the sqlite plugin for ROOT. This plugin
provides a thin client (interface) to sqlite servers. Using this
client, one can obtain information from a sqlite database into the
ROOT environment.

%package sql-pgsql
Summary:	PostgreSQL client plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description sql-pgsql
This package contains the PostGreSQL plugin for ROOT. This plugin
provides a thin client (interface) to PostGreSQL servers. Using this
client, one can obtain information from a PostGreSQL database into the
ROOT environment.

%package tmva
Summary:	Toolkit for multivariate data analysis
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xml%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit%{?_isa} = %{version}-%{release}
Requires:	%{name}-mlp%{?_isa} = %{version}-%{release}
Requires:	%{name}-multiproc%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}
#		Library split (tmva-utils from tmva)
Obsoletes:	%{name}-tmva < 6.28.08

%description tmva
The Toolkit for Multivariate Analysis (TMVA) provides a
ROOT-integrated environment for the parallel processing and
evaluation of MVA techniques to discriminate signal from background
samples. It presently includes (ranked by complexity):

  * Rectangular cut optimization
  * Correlated likelihood estimator (PDE approach)
  * Multi-dimensional likelihood estimator (PDE - range-search approach)
  * Fisher (and Mahalanobis) discriminant
  * H-Matrix (chi-squared) estimator
  * Artificial Neural Network (two different implementations)
  * Boosted Decision Trees

The TMVA package includes an implementation for each of these
discrimination techniques, their training and testing (performance
evaluation). In addition all these methods can be tested in parallel,
and hence their performance on a particular data set may easily be
compared.

%if %{dataframe}
%package tmva-utils
Summary:	Toolkit for multivariate data analysis (dataframe utilities)
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
#		Library split (tmva-utils from tmva)
Obsoletes:	%{name}-tmva < 6.28.08

%description tmva-utils
TMVA utilities using dataframe.
%endif

%package tmva-python
Summary:	Toolkit for multivariate data analysis (Python)
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva-sofie%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-numpy

%description tmva-python
Python integration with TMVA.

%if %{rrr}
%package tmva-r
Summary:	Toolkit for multivariate data analysis (R)
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-r%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva%{?_isa} = %{version}-%{release}

%description tmva-r
R integration with TMVA.
%endif

%package tmva-sofie
Summary:	ROOT/TMVA SOFIE (System for Optimized Fast Inference code Emit)
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description tmva-sofie
ROOT/TMVA SOFIE (System for Optimized Fast Inference code Emit)
generates C++ functions easily invokable for the fast inference of
trained neural network models. It takes ONNX model files as inputs and
produces C++ header files that can be included and utilized in a
"plug-and-go" style.

%if %{tmvasofieparser}
%package tmva-sofie-parser
Summary:	ROOT/TMVA SOFIE Parsers
License:	BSD-3-Clause AND MIT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva-sofie%{?_isa} = %{version}-%{release}

%description tmva-sofie-parser
Parsers for ROOT/TMVA SOFIE
%endif

%package tmva-gui
Summary:	Toolkit for multivariate data analysis GUI
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xml%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-viewer%{?_isa} = %{version}-%{release}

%description tmva-gui
GUI for the Toolkit for Multivariate Analysis (TMVA)

%package tree
Summary:	Tree library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description tree
This package contains the Tree library for ROOT.

%if %{dataframe}
%package tree-dataframe
Summary:	A high level interface to ROOT trees
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
%if %{root7}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}
%endif
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}
Requires:	%{name}-vecops%{?_isa} = %{version}-%{release}
#		Library split (tree-dataframe and vecops from tree-player)
Obsoletes:	%{name}-tree-player < 6.14.00

%description tree-dataframe
This package contains a high level interface to ROOT trees.
%endif

%package tree-player
Summary:	Library to loop over a ROOT tree
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-multiproc%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Library split (tree-dataframe and vecops from tree-player)
Obsoletes:	%{name}-tree-player < 6.14.00

%description tree-player
This package contains a plugin to loop over a ROOT tree.

%package tree-viewer
Summary:	GUI to browse a ROOT tree
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description tree-viewer
This package contains a plugin for browsing a ROOT tree in ROOT.

%package tree-webviewer
Summary:	ROOT tree web viewer library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description tree-webviewer
This package contains a plugin for browsing a ROOT tree in a web GUI.

%package unfold
Summary:	Distribution unfolding
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xmlparser%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description unfold
An algorithm to unfold distributions from detector to truth level.

%package cli
Summary:	ROOT command line utilities
BuildArch:	noarch
Requires:	python%{python3_pkgversion}-%{name} = %{version}-%{release}

%description cli
The ROOT command line utilities is a set of scripts for common tasks
written in python.

%package gui-webdisplay
Summary:	Web display for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}

%description gui-webdisplay
This package contains a web display extension for ROOT.

%ifarch %{qt5_qtwebengine_arches}
%package gui-qt5webdisplay
Summary:	Qt5 Web display
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}

%description gui-qt5webdisplay
This package contains a Qt5 web display extension for ROOT.
%endif

%ifarch %{qt6_qtwebengine_arches}
%package gui-qt6webdisplay
Summary:	Qt6 Web display
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}

%description gui-qt6webdisplay
This package contains a Qt6 web display extension for ROOT.
%endif

%package gui-webgui6
Summary:	Web based GUI for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}

%description gui-webgui6
This package provides a Web based GUI for ROOT.

%package gui-browsable
Summary:	ROOT GUI browsable providers
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split (gui-browsable-v7 from gui-browsable)
Obsoletes:	%{name}-gui-browsable < 6.32.06

%description gui-browsable
This package contains ROOT GUI browsable providers.

%package gui-browserv7
Summary:	ROOT file browser and browser widgets
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom-webviewer%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-browsable%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webgui6%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-webviewer%{?_isa} = %{version}-%{release}
#		Package split (gui-browserv7-v7 from gui-browserv7)
Obsoletes:	%{name}-gui-browserv7 < 6.32.06

%description gui-browserv7
This package contains the ROOT file browser (RBrowser) and browser widgets.

%package geom-webviewer
Summary:	Geometry web viewer library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom-painter%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-csg%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description geom-webviewer
This package contains a library for viewing geometries in a web GUI.

%if %{root7}
%package graf-gpadv7
Summary:	Canvas and pad library for ROOT (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description graf-gpadv7
This package contains a library for canvas and pad manipulations.

%package graf-primitives
Summary:	Graphics primitives (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}

%description graf-primitives
This package contains graphics primitives for ROOT 7

%package graf3d-eve7
Summary:	Event display library for ROOT (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom-webviewer%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-csg%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-montecarlo-eg%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}
Requires:	%{name}-physics%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description graf3d-eve7
This package contains a library for defining event displays in ROOT 7.

%package gui-browsable-v7
Summary:	Additional ROOT GUI browsable providers (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-browsable%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist-draw%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}
#		Package split (gui-browsable-v7 from gui-browsable)
Obsoletes:	%{name}-gui-browsable < 6.32.06

%description gui-browsable-v7
This package contains additional ROOT GUI browsable providers for ROOT 7.

%package gui-browserv7-v7
Summary:	Additional ROOT browser widgets (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-browsable%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-browserv7%{?_isa} = %{version}-%{release}
#		Package split (gui-browserv7-v7 from gui-browserv7)
Obsoletes:	%{name}-gui-browserv7 < 6.32.06

%description gui-browserv7-v7
This package contains additional ROOT browser widgets for ROOT 7.

%package gui-canvaspainter
Summary:	Canvas painter (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description gui-canvaspainter
This package contains a canvas painter extension for ROOT 7

%package gui-fitpanelv7
Summary:	GUI element for fits in ROOT (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description gui-fitpanelv7
This package contains a library to show a pop-up dialog when fitting
various kinds of data.

%package histv7
Summary:	Histogram library for ROOT (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description histv7
This package contains a library for histogramming in ROOT 7.

%package hist-draw
Summary:	Histogram drawing (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}

%description hist-draw
This package contains an histogram drawing extension for ROOT 7.

%package tree-ntuple
Summary:	Ntuple (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description tree-ntuple
This package contains an ntuple extension for ROOT 7.

%package tree-ntuple-utils
Summary:	Ntuple utility library (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}

%description tree-ntuple-utils
This package contains utility functions for ntuples.
%endif

%prep
%setup -q -a 1 -a 9

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1

# Remove bundled sources in order to be sure they are not used
#  * afterimage
rm -rf graf2d/asimage/src/libAfterImage/{libjpeg,libpng,libungif,zlib}
sed '/zlib\/zlib.h/d' -i graf2d/asimage/src/libAfterImage/.depend
#  * ftgl
rm -rf graf3d/ftgl/src graf3d/ftgl/inc
#  * freetype
rm -rf graf2d/freetype/src
#  * glew, lz4, nlohmann, pcre, xxhash, zlib, zstd
rm -rf builtins/glew
rm -rf builtins/lz4
%if ! %{bundlejson}
rm -rf builtins/nlohmann
%endif
rm -rf builtins/pcre
rm -rf builtins/xxhash
rm -rf builtins/zlib
rm -rf builtins/zstd
#  * lzma
rm core/lzma/src/*.tar.gz
#  * gl2ps
rm graf3d/gl/src/gl2ps.cxx graf3d/gl/src/gl2ps/gl2ps.h
#  * unuran
rm math/unuran/src/*.tar.gz
#  * xrootd-private-devel headers
rm -rf proof/xrdinc/*
#  * x11 extension headers
rm -rf graf2d/x11/inc/X11
#  * jsroot
rm -rf js/[^f]* js/files/draw.htm js/files/online.htm

# Remove pre-minified script and style files
rm etc/notebook/JsMVA/js/*.min.js
rm etc/notebook/JsMVA/css/*.min.css

# Additional documentation
install -p -m 644 %{SOURCE7} bindings/jupyroot

%build
%if %{?fedora}%{!?fedora:0} == 40 || %{?rhel}%{!?rhel:0} == 10
# This package triggers a fault in LLVM when LTO is enabled.  Until LLVM
# is analyzed and fixed, disable LTO
%define _lto_cflags %{nil}
%endif

unset QTDIR
unset QTLIB
unset QTINC

# Minify script and style files
for s in etc/notebook/JsMVA/js/*.js ; do
    uglifyjs-3 ${s} -c -m -o ${s%.js}.min.js
done
for s in etc/notebook/JsMVA/css/*.css ; do
    python3 -m rcssmin < ${s} > ${s%.css}.min.css
done

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}/%{name} \
       -DCMAKE_INSTALL_PYTHONDIR:PATH=%{python3_sitearch} \
       -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_datadir}/%{name} \
       -DCMAKE_INSTALL_DOCDIR:PATH=%{_pkgdocdir} \
       -DPython3_EXECUTABLE:PATH=%{__python3} \
       -Dgnuinstall:BOOL=ON \
       -Dbuiltin_cfitsio:BOOL=OFF \
       -Dbuiltin_clang:BOOL=ON \
       -Dbuiltin_cling:BOOL=ON \
       -Dbuiltin_cppzmq:BOOL=OFF \
       -Dbuiltin_davix:BOOL=OFF \
       -Dbuiltin_fftw3:BOOL=OFF \
       -Dbuiltin_freetype:BOOL=OFF \
       -Dbuiltin_ftgl:BOOL=OFF \
       -Dbuiltin_gl2ps:BOOL=OFF \
       -Dbuiltin_glew:BOOL=OFF \
       -Dbuiltin_gsl:BOOL=OFF \
       -Dbuiltin_gtest:BOOL=OFF \
       -Dbuiltin_llvm:BOOL=ON \
       -Dbuiltin_lz4:BOOL=OFF \
       -Dbuiltin_lzma:BOOL=OFF \
%if %{bundlejson}
       -Dbuiltin_nlohmannjson:BOOL=ON \
%else
       -Dbuiltin_nlohmannjson:BOOL=OFF \
%endif
       -Dbuiltin_openssl:BOOL=OFF \
       -Dbuiltin_openui5:BOOL=ON \
       -Dbuiltin_pcre:BOOL=OFF \
       -Dbuiltin_tbb:BOOL=OFF \
       -Dbuiltin_unuran:BOOL=OFF \
       -Dbuiltin_vc:BOOL=OFF \
       -Dbuiltin_vdt:BOOL=OFF \
       -Dbuiltin_veccore:BOOL=OFF \
       -Dbuiltin_xrootd:BOOL=OFF \
       -Dbuiltin_xxhash:BOOL=OFF \
       -Dbuiltin_zeromq:BOOL=OFF \
       -Dbuiltin_zlib:BOOL=OFF \
       -Dbuiltin_zstd:BOOL=OFF \
%ifnarch %{ix86} %{arm}
       -Darrow:BOOL=ON \
%else
       -Darrow:BOOL=OFF \
%endif
       -Dasimage:BOOL=ON \
       -Dccache:BOOL=OFF \
       -Ddistcc:BOOL=OFF \
       -Dcefweb:BOOL=OFF \
       -Dclad:BOOL=ON \
       -DCLAD_SOURCE_DIR:PATH=${PWD}/clad-1.7 \
       -Dcocoa:BOOL=OFF \
       -Dcuda:BOOL=OFF \
       -Ddaos:BOOL=OFF \
%if %{dataframe}
       -Ddataframe:BOOL=ON \
%else
       -Ddataframe:BOOL=OFF \
%endif
       -Ddavix:BOOL=ON \
       -Ddcache:BOOL=ON \
       -Ddev:BOOL=OFF \
       -Dfcgi:BOOL=ON \
       -Dfftw3:BOOL=ON \
       -DFIREFOX_EXECUTABLE:PATH=/usr/bin/firefox \
       -Dfitsio:BOOL=ON \
       -Dfortran:BOOL=ON \
       -Dgdml:BOOL=ON \
       -Dgeom:BOOL=ON \
       -Dgeombuilder:BOOL=ON \
       -Dgviz:BOOL=ON \
       -Dhtml:BOOL=ON \
       -Dhttp:BOOL=ON \
       -Dimt:BOOL=ON \
       -Dlibcxx:BOOL=OFF \
       -Dmathmore:BOOL=ON \
       -Dmemory_termination:BOOL=OFF \
       -Dminuit2_mpi:BOOL=OFF \
       -Dminuit2_omp:BOOL=OFF \
       -Dmpi:BOOL=OFF \
       -Dmysql:BOOL=ON \
       -Dodbc:BOOL=ON \
       -Dopengl:BOOL=ON \
       -Dpgsql:BOOL=ON \
       -Dproof:BOOL=ON \
       -Dpyroot:BOOL=ON \
       -Dpythia8:BOOL=ON \
%ifarch %{qt5_qtwebengine_arches}
       -Dqt5web:BOOL=ON \
%else
       -Dqt5web:BOOL=OFF \
%endif
%ifarch %{qt6_qtwebengine_arches}
       -Dqt6web:BOOL=ON \
%else
       -Dqt6web:BOOL=OFF \
%endif
%if %{rrr}
       -Dr:BOOL=ON \
%else
       -Dr:BOOL=OFF \
%endif
%if %{roofit}
       -Droofit:BOOL=ON \
%if %{roofitmp}
       -Droofit_multiprocess:BOOL=ON \
%else
       -Droofit_multiprocess:BOOL=OFF \
%endif
%else
       -Droofit:BOOL=OFF \
       -Droofit_multiprocess:BOOL=OFF \
%endif
       -Droofit_hs3_ryml:BOOL=OFF \
%if %{root7}
       -Droot7:BOOL=ON \
%else
       -Droot7:BOOL=OFF \
%endif
       -Drpath:BOOL=OFF \
       -Druby:BOOL=OFF \
       -Druntime_cxxmodules:BOOL=OFF \
       -Dshadowpw:BOOL=ON \
       -Dshared:BOOL=ON \
       -Dsoversion:BOOL=ON \
       -Dspectrum:BOOL=ON \
       -Dsqlite:BOOL=ON \
       -Dssl:BOOL=ON \
       -Dtmva:BOOL=ON \
       -Dtmva-cpu:BOOL=ON \
       -Dtmva-cudnn:BOOL=OFF \
       -Dtmva-gpu:BOOL=OFF \
       -Dtmva-pymva:BOOL=ON \
%if %{rrr}
       -Dtmva-rmva:BOOL=ON \
%else
       -Dtmva-rmva:BOOL=OFF \
%endif
%if %{tmvasofieparser}
       -Dtmva-sofie:BOOL=ON \
%else
       -Dtmva-sofie:BOOL=OFF \
%endif
       -Dtpython:BOOL=ON \
       -Dunfold:BOOL=ON \
       -Dunuran:BOOL=ON \
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 9
       -During:BOOL=ON \
%else
       -During:BOOL=OFF \
%endif
       -Dvc:BOOL=OFF \
       -Dvdt:BOOL=OFF \
       -Dveccore:BOOL=OFF \
       -Dvecgeom:BOOL=OFF \
       -Dwebgui:BOOL=ON \
       -Dx11:BOOL=ON \
       -Dxml:BOOL=ON \
       -Dxrootd:BOOL=ON \
       -Dfail-on-missing:BOOL=ON \
       -Dtesting:BOOL=ON \
       -Dtestsupport:BOOL=ON \
       -Dtest_distrdf_pyspark:BOOL=OFF \
       -Dtest_distrdf_dask:BOOL=OFF \
       -Dclingtest:BOOL=OFF \
       -Dcoverage:BOOL=OFF \
       -Droottest:BOOL=OFF \
       -Drootbench:BOOL=OFF \
       -Dasan:BOOL=OFF
%cmake_build

%install
%cmake_install

# Let rpm redo the python byte compilation
find %{buildroot}%{python3_sitearch} -depth -type d -name __pycache__ -exec rm -r {} ';'

# Install desktop entry and icon
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
install -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

# Install mime type and icon
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes
install -p -m 644 %{SOURCE5} %{buildroot}%{_datadir}/mime/packages
install -p -m 644 %{SOURCE6} \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes

# Move python cli helper to its own directory
mkdir -p %{buildroot}%{_datadir}/%{name}/cli
mv %{buildroot}%{python3_sitearch}/cmdLineUtils.py \
   %{buildroot}%{_datadir}/%{name}/cli
sed -e '/^\#!/d' -i %{buildroot}%{_datadir}/%{name}/cli/cmdLineUtils.py

# Install GDB pretty printers to auto load safe path
mkdir -p %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}/%{name}
mv %{buildroot}%{_libdir}/%{name}/*-gdb.py \
   %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}/%{name}

# Fix python extension suffix
mv %{buildroot}%{python3_sitearch}/libROOTPythonizations.so \
   %{buildroot}%{python3_sitearch}/libROOTPythonizations%{python3_ext_suffix}

# Move noarch python modules to sitelib
if [ "%{python3_sitelib}" != "%{python3_sitearch}" ] ; then
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{python3_sitearch}/JupyROOT %{buildroot}%{python3_sitelib}
%if %{distrdf}
mv %{buildroot}%{python3_sitearch}/DistRDF %{buildroot}%{python3_sitelib}
%endif
fi

# Create .dist-info files so that rpm auto-generates provides
mkdir %{buildroot}%{python3_sitearch}/ROOT-%{version}.dist-info
echo 'Name: ROOT' > \
    %{buildroot}%{python3_sitearch}/ROOT-%{version}.dist-info/METADATA
echo 'Version: %{version}' >> \
    %{buildroot}%{python3_sitearch}/ROOT-%{version}.dist-info/METADATA
mkdir %{buildroot}%{python3_sitelib}/JupyROOT-%{version}.dist-info
echo 'Name: JupyROOT' > \
    %{buildroot}%{python3_sitelib}/JupyROOT-%{version}.dist-info/METADATA
echo 'Version: %{version}' >> \
    %{buildroot}%{python3_sitelib}/JupyROOT-%{version}.dist-info/METADATA
%if %{distrdf}
mkdir %{buildroot}%{python3_sitelib}/DistRDF-%{version}.dist-info
echo 'Name: DistRDF' > \
    %{buildroot}%{python3_sitelib}/DistRDF-%{version}.dist-info/METADATA
echo 'Version: %{version}' >> \
    %{buildroot}%{python3_sitelib}/DistRDF-%{version}.dist-info/METADATA
%endif

# Put jupyter stuff in the right places
mkdir -p %{buildroot}%{_datadir}/jupyter/kernels

cp -pr %{buildroot}%{_datadir}/%{name}/notebook/kernels/root \
   %{buildroot}%{_datadir}/jupyter/kernels/python%{python3_pkgversion}-jupyroot
sed -e 's/ROOT C++/& (Python 3)/' \
    -e 's!python[0-9]*\.[0-9]*!%{__python3}!' \
    -i %{buildroot}%{_datadir}/jupyter/kernels/python%{python3_pkgversion}-jupyroot/kernel.json
sed -e '/^\#!/d' \
    -i %{buildroot}%{python3_sitelib}/JupyROOT/kernel/rootkernel.py

rm -rf %{buildroot}%{_datadir}/%{name}/notebook/custom
rm -rf %{buildroot}%{_datadir}/%{name}/notebook/html
rm -rf %{buildroot}%{_datadir}/%{name}/notebook/kernels
rm     %{buildroot}%{_datadir}/%{name}/notebook/jupyter_notebook_config.py

# Replace the rootnb.exe wrapper with a simpler one
cat > %{buildroot}%{_bindir}/rootnb.exe << EOF
#! /bin/sh
if [ -z "\$(type jupyter 2>/dev/null)" ] ; then
   echo jupyter not found in path. Exiting.
   exit 1
fi
if [ -z "\$(type jupyter-notebook 2>/dev/null)" ] ; then
   echo jupyter-notebook not found in path. Exiting.
   exit 1
fi
jupyter notebook "\$@"
EOF

# Avoid /usr/bin/env shebangs (and adapt cli to cmdLineUtils location)
sed -e 's!/usr/bin/env bash!/bin/bash!' -i %{buildroot}%{_bindir}/root-config
sed -e 's!/usr/bin/env /usr/bin/python.*!%{__python3}!' \
    -e '/import sys/d' \
    -e '/import cmdLineUtils/iimport sys' \
    -e '/import cmdLineUtils/isys.path.insert(0, "%{_datadir}/%{name}/cli")' \
    -i %{buildroot}%{_bindir}/rootbrowse \
       %{buildroot}%{_bindir}/rootcp \
       %{buildroot}%{_bindir}/rooteventselector \
       %{buildroot}%{_bindir}/rootls \
       %{buildroot}%{_bindir}/rootmkdir \
       %{buildroot}%{_bindir}/rootmv \
       %{buildroot}%{_bindir}/rootprint \
       %{buildroot}%{_bindir}/rootrm \
       %{buildroot}%{_bindir}/rootslimtree
sed -e 's!/usr/bin/env /usr/bin/python.*!%{__python3}!' \
    -i %{buildroot}%{_bindir}/rootdrawtree
sed -e 's!/usr/bin/env python!%{__python3}!' \
    -i %{buildroot}%{_datadir}/%{name}/dictpch/makepch.py \
       %{buildroot}%{_pkgdocdir}/tutorials/histfactory/makeQuickModel.py \
       %{buildroot}%{_pkgdocdir}/tutorials/tmva/keras/ApplicationClassificationKeras.py \
       %{buildroot}%{_pkgdocdir}/tutorials/tmva/keras/ApplicationRegressionKeras.py \
       %{buildroot}%{_pkgdocdir}/tutorials/tmva/keras/ClassificationKeras.py \
       %{buildroot}%{_pkgdocdir}/tutorials/tmva/keras/GenerateModel.py \
       %{buildroot}%{_pkgdocdir}/tutorials/tmva/keras/MulticlassKeras.py \
       %{buildroot}%{_pkgdocdir}/tutorials/tmva/keras/RegressionKeras.py
sed -e 's!/usr/bin/python!%{__python3}!' \
    -i %{buildroot}%{_datadir}/%{name}/pdg_table_update.py

# Remove some junk
rm %{buildroot}%{_datadir}/%{name}/proof/*.sample
rm -rf %{buildroot}%{_datadir}/%{name}/proof/utils
rm %{buildroot}%{_datadir}/%{name}/root.desktop
rm %{buildroot}%{_bindir}/setxrd*
rm %{buildroot}%{_bindir}/thisroot*
rm %{buildroot}%{_pkgdocdir}/INSTALL
rm %{buildroot}%{_pkgdocdir}/README.CXXMODULES.md

# Only used on Windows
rm %{buildroot}%{_datadir}/%{name}/macros/fileopen.C

# Remove plugin definitions for non-built and obsolete plugins
pushd %{buildroot}%{_datadir}/%{name}/plugins
%if ! %{rrr}
rm ROOT@@Math@@Minimizer/P090_RMinimizer.C
%endif
rm TGLManager/P020_TGWin32GLManager.C
rm TGLManager/P030_TGOSXGLManager.C
rm TProofMgr/P010_TXProofMgr.C
rm TProofServ/P010_TXProofServ.C
rm TSlave/P010_TXSlave.C
rm TSQLServer/P040_TOracleServer.C
rm TVirtualGeoConverter/P010_TGeoVGConverter.C
rm TVirtualGLImp/P020_TGWin32GL.C
rm TVirtualX/P030_TGWin32.C
rm TVirtualX/P050_TGQuartz.C
rmdir TProofMgr
rmdir TProofServ
rmdir TSlave
rmdir TVirtualGeoConverter
popd

# Replace bundled jsroot with symlinks to system version
for x in build img mathjax modules scripts files/draw.htm files/online.htm ; do
    ln -nrs %{buildroot}%{_jsdir}/jsroot/$x \
	    %{buildroot}%{_datadir}/%{name}/js/$x
done

# Create ldconfig configuration
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/%{name} > \
     %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# Make ROOTConfig-targets.cmake not error on missing files to work better with
# subpackages
sed -e 's/FATAL_ERROR \(.*imported\)/WARNING \1/' \
    -e '/Possible reasons include/i\
but this file does not exist.\
If this target is used you need to install the package that provides this\
file using \\"dnf install\\".\
If this target is not used this warning can be ignored.")' \
    -e '/Possible reasons include/,/)/d' \
    -i %{buildroot}%{_datadir}/%{name}/cmake/ROOTConfig-targets.cmake

# Create includelist files ...
for f in `find %{_vpath_builddir} -name cmake_install.cmake -a '!' -path '*/llvm-project/*'` ; do
    l=`sed 's!%{_vpath_builddir}/\(.*\)/cmake_install.cmake!includelist-\1!' <<< $f`
    l=`tr / - <<< $l`
    tmpdir=`mktemp -d`
    DESTDIR=$tmpdir cmake -DCMAKE_INSTALL_COMPONENT=headers -P $f > /dev/null
    ( cd $tmpdir ; find . -type f) | sort | sed 's!^\.!!' > $l
    rm -rf $tmpdir
done

# ... and merge some of them
cat includelist-core-{[^mw],m[^au]}* > includelist-core
cat includelist-graf2d-x11ttf >> includelist-graf2d-x11
cat includelist-graf3d-rglew >> includelist-graf3d-gl

# Do python byte compilation (for non-standard paths)
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/cli
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}/%{name}

%check
pushd %{_vpath_builddir}
pushd test
ln -s ../../files files
popd
pushd runtutorials
ln -s ../../files files
for x in df014_CsvDataSource_MuRun2010B_cpp.csv \
	 df014_CsvDataSource_MuRun2010B_py.csv \
	 df015_CsvDataSource_MuRun2010B.csv ; do
    ln -sf ../../files/tutorials/df014_CsvDataSource_MuRun2010B.csv $x
done
popd
pushd tmva/tmva/test
ln -s ../../../../files files
popd
pushd tmva/tmva/test/DNN
ln -s ../../../../../files files
popd
pushd tmva/tmva/test/envelope
ln -s ../../../../../files files
popd

# Exclude some tests that can not be run
#
# - test-stressIOPlugins-*
#   requires network access (by design since they test the remote file IO)
#
# - tutorial-dataframe-df101_h1Analysis
# - tutorial-tree-run_h1analysis
# - tutorial-multicore-imt001_parBranchProcessing
# - tutorial-multicore-mp103_processSelector
# - tutorial-multicore-mp104_processH1
# - tutorial-multicore-mp105_processEntryList
#   requires network access: http://root.cern.ch/files/h1/
#
# - tutorial-multicore-imt101_parTreeProcessing
#   requires input data: http://root.cern.ch/files/tp_process_imt.root (707 MB)
#
# - tutorial-dataframe-df###_SQlite*
#   reads sqlite data over network:
#   http://root.cern.ch/files/root_download_stats.sqlite
#
# - tutorial-dataframe-df033_Describe-py
# - tutorial-dataframe-df102_NanoAODDimuonAnalysis(-py)?
#   reads input data over network:
#   root://eospublic.cern.ch//eos/opendata/cms/derived-data/
#   AOD2NanoAODOutreachTool/Run2012BC_DoubleMuParked_Muons.root
#
# - gtest-tree-treeplayer-treeprocessormt-remotefiles
# - tutorial-dataframe-df103_NanoAODHiggsAnalysis(-py)?
#   reads input data over network:
#   root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/
#
# - tutorial-dataframe-df104_HiggsToTwoPhotons-py
# - tutorial-dataframe-df105_WBosonAnalysis-py
# - tutorial-dataframe-df106_HiggsToFourLeptons(-py)
# - tutorial-dataframe-df107_SingleTopAnalysis-py
# - tutorial-rcanvas-df104-py
# - tutorial-rcanvas-df105-py
#   reads input data over network:
#   root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/
#
# - tutorial-v7-ntuple-ntpl003_lhcbOpenData
#   reads input data over network
#   http://root.cern.ch/files/LHCb/lhcb_B2HHH_MagnetUp.root (425 MB)
#
# - tutorial-v7-ntuple-ntpl004_dimuon
#   reads input data over network
#   http://root.cern.ch/files/NanoAOD_DoubleMuon_CMS2011OpenData.root (1.5 GB)
#
# - tutorial-v7-ntuple-ntpl008_import
#   reads input data over network
#   http://root.cern.ch/files/HiggsTauTauReduced/GluGluToHToTauTau.root (20 MB)
#
# - tutorial-v7-ntuple-ntpl011_global_temperatures
#   reads input data over network
#   http://root.cern.ch/files/tutorials/GlobalLandTemperaturesByCity.csv
#
# - gtest-net-davix-RRawFileDavix
#   reads input file over network
#   http://root.cern.ch/files/davix.test
#
# - gtest-net-netxng-RRawFileNetXNG
#   reads input file over network
#   root://eospublic.cern.ch/eos/root-eos/xrootd.test
#
# - gtest-net-netxng-TNetXNGFileTest
#   reads input file over network
#   root://eospublic.cern.ch/eos/root-eos/h1/dstarmb.root
#
# - gtest-tmva-tmva-rreader
# - gtest-tmva-tmva-rstandardscaler
# - tutorial-tmva-tmva003_RReader
# - tutorial-tmva-tmva004_RStandardScaler
#   reads input data over network
#   http://root.cern.ch/files/tmva_class_example.root
#
# - tutorial-tmva-tmva103_Application
#   reads input data over network
#   http://root.cern/files/tmva101.root
#
# - tutorial-tmva-RBatchGenerator_NumPy-py
#   reads input data over network
#   http://root.cern/files/Higgs_data.root
#
# - test-import-numba
# - tutorial-pyroot-pyroot004_NumbaDeclare-py
# - pyunittests-pyroot-numbadeclare
#   these tests require the numba python module which is not available
#
# - test-webgui-ping
#   error: Cannot display window in native
excluded="\
test-stressIOPlugins|\
tutorial-dataframe-df101_h1Analysis|\
tutorial-tree-run_h1analysis|\
tutorial-multicore-imt001_parBranchProcessing|\
tutorial-multicore-mp103_processSelector|\
tutorial-multicore-mp104_processH1|\
tutorial-multicore-mp105_processEntryList|\
tutorial-multicore-imt101_parTreeProcessing|\
tutorial-dataframe-df..._SQlite|\
tutorial-dataframe-df033_Describe-py|\
tutorial-dataframe-df102_NanoAODDimuonAnalysis|\
gtest-tree-treeplayer-treeprocessormt-remotefiles|\
tutorial-dataframe-df103_NanoAODHiggsAnalysis|\
tutorial-dataframe-df104_HiggsToTwoPhotons-py|\
tutorial-dataframe-df105_WBosonAnalysis-py|\
tutorial-dataframe-df106_HiggsToFourLeptons|\
tutorial-dataframe-df107_SingleTopAnalysis-py|\
tutorial-rcanvas-df104-py|\
tutorial-rcanvas-df105-py|\
tutorial-v7-ntuple-ntpl003_lhcbOpenData|\
tutorial-v7-ntuple-ntpl004_dimuon|\
tutorial-v7-ntuple-ntpl008_import|\
tutorial-v7-ntuple-ntpl011_global_temperatures|\
gtest-net-davix-RRawFileDavix|\
gtest-net-netxng-RRawFileNetXNG|\
gtest-net-netxng-TNetXNGFileTest|\
gtest-tmva-tmva-rreader|\
gtest-tmva-tmva-rstandardscaler|\
tutorial-tmva-tmva003_RReader|\
tutorial-tmva-tmva004_RStandardScaler|\
tutorial-tmva-tmva103_Application|\
tutorial-tmva-RBatchGenerator_NumPy-py|\
test-import-numba|\
tutorial-pyroot-pyroot004_NumbaDeclare-py|\
pyunittests-pyroot-numbadeclare|\
test-webgui-ping"

# gtest-roofit-roofit-vectorisedPDFs-testLandau:
# Expected equality of these values:
#   nFarOff
#     Which is: 1
#   0u
#     Which is: 0
#
# test-stressgraphics-firefox-skip3d:
# requires firefox...
#
# gtest-tree-treeplayer-treetreeplayertestUnit:
# segmentation fault
#
# tutorial-webcanv-fonts_ttf.cxx:
# Requires web graphics
#
# tutorial-roofit-rf617_simulation_based_inference_multidimensional-py:
# from sklearn.neural_network import MLPClassifier
#
# tutorial-roofit-rf618_mixture_models-py:
# import xgboost as xgb
excluded="${excluded}|\
gtest-roofit-roofit-vectorisedPDFs-testLandau|\
test-stressgraphics-firefox-skip3d|\
gtest-tree-treeplayer-treetreeplayertestUnit|\
tutorial-webcanv-fonts_ttf.cxx|\
tutorial-roofit-rf617_simulation_based_inference_multidimensional-py|\
tutorial-roofit-rf618_mixture_models-py"

# Test using tensorflow and torch
# Disabled for Python >= 3.12, but must be excluded for Python < 3.12
excluded="${excluded}|\
pyunittests-bindings-pyroot-pythonizations-batchgen|\
test-import-tensorflow|\
test-import-torch"

%if ! %{pandas}
# - test-import-pandas
# - tutorial-dataframe-df026_AsNumpyArrays-py
# - tutorial-dataframe-df035_RDFFromPandas-py
# - tutorial-roofit-rf409_NumPyPandasToRooFit-py
#   Requires the pandas python module not (yet) available in RHEL/EPEL 9
excluded="${excluded}|\
test-import-pandas|\
tutorial-dataframe-df026_AsNumpyArrays-py|\
tutorial-dataframe-df035_RDFFromPandas-py|\
tutorial-roofit-rf409_NumPyPandasToRooFit-py"
%endif

%ifarch %{ix86}
# - gtest-tree-dataframe-dataframe-concurrency
#   "There's already an active task arena."
excluded="${excluded}|\
gtest-tree-dataframe-dataframe-concurrency"
%endif

%ifarch aarch64
# - tutorial-tmva-RBatchGenerator_filters_vectors-py
#   Randomly segfaults
#   *** Break *** segmentation violation
excluded="${excluded}|\
tutorial-tmva-RBatchGenerator_filters_vectors-py"
%endif

%ifarch %{power64}
# - tutorial-roostats-IntervalExamples-py
#   *** Break *** segmentation violation
excluded="${excluded}|\
gtest-tree-ntuple-v7-ntuple-evolution|\
tutorial-roostats-IntervalExamples-py"
%endif

%ifarch s390x
# - gtest-roofit-roofitcore-testNaNPacker
# - gtest-roofit-roofitcore-testLikelihoodGradientJob
#   Uses "Packed NaN" feature, not implemented for big endian.
excluded="${excluded}|\
gtest-roofit-roofitcore-testNaNPacker|\
gtest-roofit-roofitcore-testLikelihoodGradientJob"

# - gtest-core-dictgen-dictgen-base
# - gtest-tmva-sofie-TestCustomModelsFromONNX
# - gtest-tree-dataframe-dataframe-unified-constructor
#
# - gtest-tree-dataframe-datasource-ntuple
# - gtest-tree-ntuple-v7-ntuple-basics
# - gtest-tree-ntuple-v7-ntuple-bulk
# - gtest-tree-ntuple-v7-ntuple-cast
# - gtest-tree-ntuple-v7-ntuple-compat
# - gtest-tree-ntuple-v7-ntuple-extended
# - gtest-tree-ntuple-v7-ntuple-friends
# - gtest-tree-ntuple-v7-ntuple-index
# - gtest-tree-ntuple-v7-ntuple-merger
# - gtest-tree-ntuple-v7-ntuple-model
# - gtest-tree-ntuple-v7-ntuple-modelext
# - gtest-tree-ntuple-v7-ntuple-multi-column
# - gtest-tree-ntuple-v7-ntuple-packing
# - gtest-tree-ntuple-v7-ntuple-parallel-writer
# - gtest-tree-ntuple-v7-ntuple-project
# - gtest-tree-ntuple-v7-ntuple-processor
# - gtest-tree-ntuple-v7-ntuple-show
# - gtest-tree-ntuple-v7-ntuple-storage
# - gtest-tree-ntuple-v7-ntuple-storage-daos
# - gtest-tree-ntuple-v7-ntuple-types
# - gtest-tree-ntuple-v7-ntuple-view
# - gtest-tree-ntuple-v7-rfield-class
# - gtest-tree-ntuple-v7-rfield-streamer
# - gtest-tree-ntuple-v7-rfield-variant
# - gtest-tree-ntuple-v7-rfield-vector
# - gtest-tree-ntupleutil-v7-ntuple-importer
# - gtest-tree-ntupleutil-v7-ntuple-inspector
#   https://github.com/root-project/root/issues/12426
#
# - pyunittests-bindings-experimental-distrdf-backend-distrdf-unit-backend-graph-caching
# - pyunittests-bindings-pyroot-pythonizations-pyroot-pyz-rtensor
# - pyunittests-bindings-pyroot-pythonizations-pyroot-pyz-stl-vector
# - tutorial-dataframe-df006_ranges-py
# - tutorial-fit-combinedFit-py
# - tutorial-fit-NumericalMinimization-py
# - tutorial-math-exampleFunction-py
# - tutorial-pyroot-hsum-py
# - tutorial-rcanvas-rbox-py
#   https://github.com/root-project/root/issues/12429
#
# - tutorial-tree-drawsparse
#   https://github.com/root-project/root/issues/12431
#
# - test-stresshistofit
# - test-stresshistofit-interpreted
# - test-stresshistogram
# - test-stresshistogram-interpreted
excluded="${excluded}|\
gtest-core-dictgen-dictgen-base|\
gtest-tmva-sofie-TestCustomModelsFromONNX|\
gtest-tree-dataframe-dataframe-unified-constructor|\
gtest-tree-dataframe-datasource-ntuple|\
gtest-tree-ntuple-v7-ntuple-basics|\
gtest-tree-ntuple-v7-ntuple-bulk|\
gtest-tree-ntuple-v7-ntuple-cast|\
gtest-tree-ntuple-v7-ntuple-compat|\
gtest-tree-ntuple-v7-ntuple-extended|\
gtest-tree-ntuple-v7-ntuple-friends|\
gtest-tree-ntuple-v7-ntuple-index|\
gtest-tree-ntuple-v7-ntuple-merger|\
gtest-tree-ntuple-v7-ntuple-model\$\$|\
gtest-tree-ntuple-v7-ntuple-modelext|\
gtest-tree-ntuple-v7-ntuple-multi-column|\
gtest-tree-ntuple-v7-ntuple-packing|\
gtest-tree-ntuple-v7-ntuple-parallel-writer|\
gtest-tree-ntuple-v7-ntuple-project|\
gtest-tree-ntuple-v7-ntuple-processor|\
gtest-tree-ntuple-v7-ntuple-show|\
gtest-tree-ntuple-v7-ntuple-storage\$\$|\
gtest-tree-ntuple-v7-ntuple-storage-daos|\
gtest-tree-ntuple-v7-ntuple-types|\
gtest-tree-ntuple-v7-ntuple-view|\
gtest-tree-ntuple-v7-rfield-class|\
gtest-tree-ntuple-v7-rfield-streamer|\
gtest-tree-ntuple-v7-rfield-variant|\
gtest-tree-ntuple-v7-rfield-vector|\
gtest-tree-ntupleutil-v7-ntuple-importer|\
gtest-tree-ntupleutil-v7-ntuple-inspector|\
pyunittests-bindings-experimental-distrdf-backend-distrdf-unit-backend-graph-caching|\
pyunittests-bindings-pyroot-pythonizations-pyroot-pyz-rtensor|\
pyunittests-bindings-pyroot-pythonizations-pyroot-pyz-stl-vector|\
tutorial-dataframe-df006_ranges-py|\
tutorial-fit-combinedFit-py|\
tutorial-fit-NumericalMinimization-py|\
tutorial-math-exampleFunction-py|\
tutorial-pyroot-hsum-py|\
tutorial-rcanvas-rbox-py|\
tutorial-tree-drawsparse|\
test-stresshistofit\$\$|\
test-stresshistofit-interpreted|\
test-stresshistogram\$\$|\
test-stresshistogram-interpreted"
%endif

%if %{?fedora}%{!?fedora:0} >= 40 || %{?rhel}%{!?rhel:0} >= 10
# Fails with gcc 14 on aarch64, ppc64le and s390x (on EPEL 10 also x86_64)
# https://github.com/root-project/root/issues/14446
# - gtest-math-matrix-testMatrixTSparse
excluded="${excluded}|\
gtest-math-matrix-testMatrixTSparse"
%endif

# Filter out parts of tests that require remote network access
# RNTuple.StdAtomic fails on ix86 (different alignment 64 bit (non)atomic)
# TClingDataMemberInfo.Offset fails on s390x
# https://github.com/root-project/root/issues/14512
GTEST_FILTER=-\
%ifarch %{ix86}
RNTuple.StdAtomic:\
%endif
%ifarch s390x
TClingDataMemberInfo.Offset:\
%endif
RCsvDS.Remote:\
RNTuple.OpenHTTP:\
RRawFile.Remote:\
RSqliteDS.Davix:\
TChainParsing.DoubleSlash:\
TChainParsing.RemoteGlob:\
TFile.ReadWithoutGlobalRegistrationNet:\
TFile.ReadWithoutGlobalRegistrationWeb \
%if ! %{pandas}
ROOTTEST_IGNORE_PANDAS_PY3=1 \
%endif
ROOTTEST_IGNORE_NUMBA_PY3=1 \
ROOTTEST_IGNORE_JUPYTER_PY3=1 \
make test ARGS="%{?_smp_mflags} --output-on-failure -E \"${excluded}\""

popd

%pretrans net-http -p <lua>
path = "%{_datadir}/%{name}/js"
st = posix.stat(path)
if st and st.type == "link" then
    os.remove(path)
end

%post net-http
# Replace bundled jsroot with symlinks to system version
for x in build img mathjax modules scripts files/draw.htm files/online.htm ; do
    ln -fnrs %{_jsdir}/jsroot/$x %{_datadir}/%{name}/js/$x
done

%pre -n python%{python3_pkgversion}-%{name}
if [ -r /var/lib/alternatives/libPyROOT.so ] ; then
    for alt in `grep python3.*/.*.so /var/lib/alternatives/libPyROOT.so` ; do
	%{_sbindir}/update-alternatives --remove libPyROOT.so $alt
    done
fi

%post -n python%{python3_pkgversion}-jupyroot
mkdir -p /etc/jupyter
if [ -e /etc/jupyter/jupyter_notebook_config.py ] ; then
    sed '/Extra static paths for JupyROOT - start/','/Extra static paths for JupyROOT - end/'d -i /etc/jupyter/jupyter_notebook_config.py
fi
cat << EOF >> /etc/jupyter/jupyter_notebook_config.py
# Extra static paths for JupyROOT - start - do not remove this line
c.NotebookApp.extra_static_paths.append('%{_jsdir}/jsroot')
# Extra static paths for JupyROOT - end - do not remove this line
EOF
if [ -e /etc/jupyter/jupyter_server_config.py ] ; then
    sed '/Extra static paths for JupyROOT - start/','/Extra static paths for JupyROOT - end/'d -i /etc/jupyter/jupyter_server_config.py
fi
cat << EOF >> /etc/jupyter/jupyter_server_config.py
# Extra static paths for JupyROOT - start - do not remove this line
c.ServerApp.extra_static_paths.append('%{_jsdir}/jsroot')
# Extra static paths for JupyROOT - end - do not remove this line
EOF

%postun -n python%{python3_pkgversion}-jupyroot
if [ $1 -eq 0 ] ; then
    if [ -e /etc/jupyter/jupyter_notebook_config.py ] ; then
	sed '/Extra static paths for JupyROOT - start/','/Extra static paths for JupyROOT - end/'d -i /etc/jupyter/jupyter_notebook_config.py
	if [ ! -s /etc/jupyter/jupyter_notebook_config.py ] ; then
	    rm /etc/jupyter/jupyter_notebook_config.py
	    rmdir /etc/jupyter 2>/dev/null || :
	fi
    fi
    if [ -e /etc/jupyter/jupyter_server_config.py ] ; then
	sed '/Extra static paths for JupyROOT - start/','/Extra static paths for JupyROOT - end/'d -i /etc/jupyter/jupyter_server_config.py
	if [ ! -s /etc/jupyter/jupyter_server_config.py ] ; then
	    rm /etc/jupyter/jupyter_server_config.py
	    rmdir /etc/jupyter 2>/dev/null || :
	fi
    fi
fi

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%files
%{_bindir}/hadd
%{_bindir}/root
%{_bindir}/root.exe
%{_bindir}/rootn.exe
%{_bindir}/rootreadspeed
%{_bindir}/roots
%{_bindir}/roots.exe
%{_bindir}/rootssh
%{_mandir}/man1/hadd.1*
%{_mandir}/man1/root.1*
%{_mandir}/man1/root.exe.1*
%{_mandir}/man1/rootn.exe.1*
%{_mandir}/man1/roots.exe.1*
%{_datadir}/applications/root.desktop
%{_datadir}/icons/hicolor/48x48/apps/root.png
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-root.png
%{_datadir}/mime/packages/root.xml

%files icons
%{_datadir}/%{name}/icons

%files fonts
%{_datadir}/%{name}/fonts

%files tutorial
%doc %{_pkgdocdir}/tutorials

%files core -f includelist-core
%{_bindir}/rmkdepend
%{_bindir}/root-config
%{_mandir}/man1/rmkdepend.1*
%{_mandir}/man1/root-config.1*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libCore.*
%{_libdir}/%{name}/libImt.*
%{_libdir}/%{name}/libNew.*
%{_libdir}/%{name}/libRint.*
%{_libdir}/%{name}/libThread.*
%{_libdir}/%{name}/lib*Dict.*
%dir %{_datadir}/gdb/auto-load%{_libdir}/%{name}
%{_datadir}/gdb/auto-load%{_libdir}/%{name}/libCore.*
%dir %{_datadir}/gdb/auto-load%{_libdir}/%{name}/__pycache__
%{_datadir}/gdb/auto-load%{_libdir}/%{name}/__pycache__/libCore.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/allDict.cxx.pch
%{_datadir}/%{name}/class.rules
%{_datadir}/%{name}/gdb-backtrace.sh
%{_datadir}/%{name}/gitinfo.txt
%{_datadir}/%{name}/helgrind-root.supp
%{_datadir}/%{name}/lsan-root.supp
%{_datadir}/%{name}/Makefile.arch
%{_datadir}/%{name}/root.mimes
%{_datadir}/%{name}/system.rootauthrc
%{_datadir}/%{name}/system.rootdaemonrc
%{_datadir}/%{name}/system.rootrc
%{_datadir}/%{name}/valgrind-root.supp
%{_datadir}/%{name}/valgrind-root-python.supp
%{_mandir}/man1/system.rootdaemonrc.1*
%dir %{_datadir}/%{name}/cmake
%{_datadir}/%{name}/cmake/*.cmake
%dir %{_datadir}/%{name}/cmake/modules
%{_datadir}/%{name}/cmake/modules/*.cmake
%dir %{_datadir}/%{name}/macros
%{_datadir}/%{name}/macros/Dialogs.C
%dir %{_datadir}/%{name}/plugins
%dir %{_datadir}/%{name}/plugins/*
%dir %{_includedir}/%{name}
%if %{bundlejson}
%dir %{_includedir}/%{name}/nlohmann
%{_includedir}/%{name}/nlohmann/json.hpp
%endif
%{_includedir}/%{name}/RConfigOptions.h
%{_includedir}/%{name}/RConfigure.h
%{_includedir}/%{name}/ROOT.modulemap
%{_includedir}/%{name}/compiledata.h
%dir %{_includedir}/%{name}/Math
%dir %{_includedir}/%{name}/ROOT
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%dir %{_pkgdocdir}
# CREDITS and LICENSE are used at runtime by the .credits and .license commands
# They therefore should not be marked doc.
%{_pkgdocdir}/CREDITS
%{_pkgdocdir}/LICENSE
%doc %{_pkgdocdir}/DEVELOPMENT.md
%doc %{_pkgdocdir}/ReleaseNotes
%license LICENSE LGPL2_1.txt

%files multiproc -f includelist-core-multiproc
%{_libdir}/%{name}/libMultiProc.*

%files cling
%{_bindir}/genreflex
%{_bindir}/rootcint
%{_bindir}/rootcling
%{_mandir}/man1/rootcling.1*
%{_libdir}/%{name}/libCling.*
%{_datadir}/%{name}/cling
%{_datadir}/%{name}/dictpch
%doc interpreter/cling/CREDITS.txt
%doc interpreter/cling/README.md
%license interpreter/cling/LICENSE.TXT

%files testsupport
%{_includedir}/%{name}/ROOT/TestSupport.hxx
%{_libdir}/%{name}/TestSupport
%doc core/testsupport/README.md

%files tpython -f includelist-bindings-tpython
%{_libdir}/%{name}/libROOTTPython.*
%{_libdir}/%{name}/libROOTTPython_rdict.pcm

%files -n python%{python3_pkgversion}-%{name} -f includelist-bindings-pyroot
%{python3_sitearch}/cppyy
%{python3_sitearch}/cppyy_backend
%{python3_sitearch}/ROOT
%{python3_sitearch}/ROOT-*.dist-info
%{python3_sitearch}/libcppyy.so
%{python3_sitearch}/libcppyy_backend.so
%{python3_sitearch}/libROOTPythonizations%{python3_ext_suffix}
%{_libdir}/%{name}/libcppyy.*
%{_libdir}/%{name}/libcppyy_backend.*
%dir %{_includedir}/%{name}/CPyCppyy

%files -n python%{python3_pkgversion}-jupyroot
%{python3_sitelib}/JupyROOT
%{python3_sitelib}/JupyROOT-*.dist-info
%{_datadir}/jupyter/kernels/python%{python3_pkgversion}-jupyroot
%{_bindir}/rootnb.exe
%{_datadir}/%{name}/notebook
%doc bindings/jupyroot/README.md
%doc bindings/jupyroot/JupyROOT-on-EPEL

%if %{distrdf}
%files -n python%{python3_pkgversion}-distrdf
%{python3_sitelib}/DistRDF
%{python3_sitelib}/DistRDF-*.dist-info
%endif

%if %{rrr}
%files r -f includelist-bindings-r
%{_libdir}/%{name}/libRInterface.*
%{_libdir}/%{name}/libRInterface_rdict.pcm
%doc bindings/r/doc/users-guide/*.md

%files r-tools -f includelist-math-rtools
%{_libdir}/%{name}/libRtools.*
%{_libdir}/%{name}/libRtools_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P090_RMinimizer.C
%endif

%files genetic -f includelist-math-genetic
%{_libdir}/%{name}/libGenetic.*
%{_libdir}/%{name}/libGenetic_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P080_GeneticMinimizer.C

%files geom -f includelist-geom-geom
%{_libdir}/%{name}/libGeom.*
%{_libdir}/%{name}/libGeom_rdict.pcm
%{_datadir}/%{name}/RadioNuclides.txt

%files geom-builder -f includelist-geom-geombuilder
%{_libdir}/%{name}/libGeomBuilder.*
%{_libdir}/%{name}/libGeomBuilder_rdict.pcm
%{_datadir}/%{name}/plugins/TGeoManagerEditor/P010_TGeoManagerEditor.C

%files geom-painter -f includelist-geom-geompainter
%{_libdir}/%{name}/libGeomPainter.*
%{_libdir}/%{name}/libGeomPainter_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualGeoPainter/P010_TGeoPainter.C

%files gdml -f includelist-geom-gdml
%{_libdir}/%{name}/libGdml.*
%{_libdir}/%{name}/libGdml_rdict.pcm

%files graf -f includelist-graf2d-graf
%{_libdir}/%{name}/libGraf.*
%{_libdir}/%{name}/libGraf_rdict.pcm
%{_datadir}/%{name}/plugins/TMinuitGraph/P010_TGraph.C

%files graf-asimage -f includelist-graf2d-asimage
%{_libdir}/%{name}/libASImage.*
%{_libdir}/%{name}/libASImage_rdict.pcm
%{_libdir}/%{name}/libASImageGui.*
%{_libdir}/%{name}/libASImageGui_rdict.pcm
%{_datadir}/%{name}/plugins/TImage/P010_TASImage.C
%{_datadir}/%{name}/plugins/TImagePlugin/P010_TASPluginGS.C
%{_datadir}/%{name}/plugins/TPaletteEditor/P010_TASPaletteEditor.C

%files graf-fitsio -f includelist-graf2d-fitsio
%{_libdir}/%{name}/libFITSIO.*
%{_libdir}/%{name}/libFITSIO_rdict.pcm

%files graf-gpad -f includelist-graf2d-gpad
%{_libdir}/%{name}/libGpad.*
%{_libdir}/%{name}/libGpad_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualPad/P010_TPad.C

%files graf-gviz -f includelist-graf2d-gviz
%{_libdir}/%{name}/libGviz.*
%{_libdir}/%{name}/libGviz_rdict.pcm

%files graf-postscript -f includelist-graf2d-postscript
%{_libdir}/%{name}/libPostscript.*
%{_libdir}/%{name}/libPostscript_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualPS/P010_TPostScript.C
%{_datadir}/%{name}/plugins/TVirtualPS/P020_TSVG.C
%{_datadir}/%{name}/plugins/TVirtualPS/P030_TPDF.C
%{_datadir}/%{name}/plugins/TVirtualPS/P040_TImageDump.C
%{_datadir}/%{name}/plugins/TVirtualPS/P050_TTeXDump.C

%files graf-x11 -f includelist-graf2d-x11
%{_libdir}/%{name}/libGX11.*
%{_libdir}/%{name}/libGX11_rdict.pcm
%{_libdir}/%{name}/libGX11TTF.*
%{_libdir}/%{name}/libGX11TTF_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualX/P010_TGX11.C
%{_datadir}/%{name}/plugins/TVirtualX/P020_TGX11TTF.C

%files graf3d -f includelist-graf3d-g3d
%{_libdir}/%{name}/libGraf3d.*
%{_libdir}/%{name}/libGraf3d_rdict.pcm
%{_datadir}/%{name}/plugins/TView/P010_TView3D.C

%files graf3d-csg -f includelist-graf3d-csg
%{_libdir}/%{name}/libRCsg.*
%{_libdir}/%{name}/libRCsg_rdict.pcm

%files graf3d-eve -f includelist-graf3d-eve
%{_libdir}/%{name}/libEve.*
%{_libdir}/%{name}/libEve_rdict.pcm

%files graf3d-gl -f includelist-graf3d-gl
%{_libdir}/%{name}/libRGL.*
%{_libdir}/%{name}/libRGL_rdict.pcm
%{_datadir}/%{name}/plugins/TGLHistPainter/P010_TGLHistPainter.C
%{_datadir}/%{name}/plugins/TGLManager/P010_TX11GLManager.C
%{_datadir}/%{name}/plugins/TVirtualGLImp/P010_TX11GL.C
%{_datadir}/%{name}/plugins/TVirtualPadPainter/P010_TGLPadPainter.C
%{_datadir}/%{name}/plugins/TVirtualViewer3D/P020_TGLSAViewer.C
%{_datadir}/%{name}/plugins/TVirtualViewer3D/P030_TGLViewer.C

%files graf3d-gviz3d -f includelist-graf3d-gviz3d
%{_libdir}/%{name}/libGviz3d.*
%{_libdir}/%{name}/libGviz3d_rdict.pcm

%files graf3d-x3d -f includelist-graf3d-x3d
%{_libdir}/%{name}/libX3d.*
%{_libdir}/%{name}/libX3d_rdict.pcm
%{_datadir}/%{name}/plugins/TViewerX3D/P010_TViewerX3D.C
%{_datadir}/%{name}/plugins/TVirtualViewer3D/P010_TVirtualViewerX3D.C

%files gui -f includelist-gui-gui
%{_libdir}/%{name}/libGui.*
%{_libdir}/%{name}/libGui_rdict.pcm
%{_datadir}/%{name}/plugins/TBrowserImp/P010_TRootBrowser.C
%{_datadir}/%{name}/plugins/TBrowserImp/P020_TRootBrowserLite.C
%{_datadir}/%{name}/plugins/TGPasswdDialog/P010_TGPasswdDialog.C
%{_datadir}/%{name}/plugins/TGuiFactory/P010_TRootGuiFactory.C

%files gui-html -f includelist-gui-guihtml
%{_libdir}/%{name}/libGuiHtml.*
%{_libdir}/%{name}/libGuiHtml_rdict.pcm

%files gui-fitpanel -f includelist-gui-fitpanel
%{_libdir}/%{name}/libFitPanel.*
%{_libdir}/%{name}/libFitPanel_rdict.pcm
%{_datadir}/%{name}/plugins/TFitEditor/P010_TFitEditor.C

%files gui-ged -f includelist-gui-ged
%{_libdir}/%{name}/libGed.*
%{_libdir}/%{name}/libGed_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualPadEditor/P010_TGedEditor.C

%files gui-builder -f includelist-gui-guibuilder
%{_libdir}/%{name}/libGuiBld.*
%{_libdir}/%{name}/libGuiBld_rdict.pcm
%{_datadir}/%{name}/plugins/TGuiBuilder/P010_TRootGuiBuilder.C
%{_datadir}/%{name}/plugins/TVirtualDragManager/P010_TGuiBldDragManager.C

%files gui-recorder -f includelist-gui-recorder
%{_libdir}/%{name}/libRecorder.*
%{_libdir}/%{name}/libRecorder_rdict.pcm

%files hbook -f includelist-hist-hbook
%{_bindir}/g2root
%{_bindir}/h2root
%{_mandir}/man1/g2root.1*
%{_mandir}/man1/h2root.1*
%{_libdir}/%{name}/libHbook.*
%{_libdir}/%{name}/libHbook_rdict.pcm

%files hist -f includelist-hist-hist
%{_libdir}/%{name}/libHist.*
%{_libdir}/%{name}/libHist_rdict.pcm
%dir %{_includedir}/%{name}/v5

%files hist-painter -f includelist-hist-histpainter
%{_libdir}/%{name}/libHistPainter.*
%{_libdir}/%{name}/libHistPainter_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualHistPainter/P010_THistPainter.C
%{_datadir}/%{name}/plugins/TVirtualGraphPainter/P010_TGraphPainter.C

%files spectrum -f includelist-hist-spectrum
%{_libdir}/%{name}/libSpectrum.*
%{_libdir}/%{name}/libSpectrum_rdict.pcm

%files spectrum-painter -f includelist-hist-spectrumpainter
%{_libdir}/%{name}/libSpectrumPainter.*
%{_libdir}/%{name}/libSpectrumPainter_rdict.pcm

%files html -f includelist-html
%{_libdir}/%{name}/libHtml.*
%{_libdir}/%{name}/libHtml_rdict.pcm
%{_datadir}/%{name}/html

%files io -f includelist-io-io
%{_libdir}/%{name}/libRIO.*
%{_datadir}/%{name}/plugins/TArchiveFile/P010_TZIPFile.C
%{_datadir}/%{name}/plugins/TVirtualStreamerInfo/P010_TStreamerInfo.C

%files io-dcache -f includelist-io-dcache
%{_libdir}/%{name}/libDCache.*
%{_libdir}/%{name}/libDCache_rdict.pcm
%{_datadir}/%{name}/plugins/TFile/P040_TDCacheFile.C
%{_datadir}/%{name}/plugins/TSystem/P020_TDCacheSystem.C

%files io-sql -f includelist-io-sql
%{_libdir}/%{name}/libSQLIO.*
%{_libdir}/%{name}/libSQLIO_rdict.pcm
%{_datadir}/%{name}/plugins/TFile/P090_TSQLFile.C

%files io-xml -f includelist-io-xml
%{_libdir}/%{name}/libXMLIO.*
%{_libdir}/%{name}/libXMLIO_rdict.pcm
%{_datadir}/%{name}/plugins/TFile/P080_TXMLFile.C

%files io-xmlparser -f includelist-io-xmlparser
%{_libdir}/%{name}/libXMLParser.*
%{_libdir}/%{name}/libXMLParser_rdict.pcm

%files foam -f includelist-math-foam
%{_libdir}/%{name}/libFoam.*
%{_libdir}/%{name}/libFoam_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@DistSampler/P020_TFoamSampler.C

%files fftw -f includelist-math-fftw
%{_libdir}/%{name}/libFFTW.*
%{_libdir}/%{name}/libFFTW_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualFFT/P010_TFFTComplex.C
%{_datadir}/%{name}/plugins/TVirtualFFT/P020_TFFTComplexReal.C
%{_datadir}/%{name}/plugins/TVirtualFFT/P030_TFFTRealComplex.C
%{_datadir}/%{name}/plugins/TVirtualFFT/P040_TFFTReal.C

%files fumili -f includelist-math-fumili
%{_libdir}/%{name}/libFumili.*
%{_libdir}/%{name}/libFumili_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P070_TFumiliMinimizer.C
%{_datadir}/%{name}/plugins/TVirtualFitter/P020_TFumili.C

%files genvector -f includelist-math-genvector
%{_libdir}/%{name}/libGenVector.*
%{_libdir}/%{name}/libGenVector_rdict.pcm
%{_libdir}/%{name}/libGenVector32.rootmap
%{_libdir}/%{name}/libGenVector_G__GenVector32_rdict.pcm
%dir %{_includedir}/%{name}/Math/GenVector

%files mathcore -f includelist-math-mathcore
%{_libdir}/%{name}/libMathCore.*
%{_libdir}/%{name}/libMathCore_rdict.pcm
%dir %{_includedir}/%{name}/Fit

%files mathmore -f includelist-math-mathmore
%{_libdir}/%{name}/libMathMore.*
%{_libdir}/%{name}/libMathMore_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P010_Brent.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P020_Bisection.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P030_FalsePos.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P040_Newton.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P050_Secant.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P060_Steffenson.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P030_GSLMinimizer.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P040_GSLNLSMinimizer.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P050_GSLSimAnMinimizer.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@VirtualIntegrator/P010_GSLIntegrator.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@VirtualIntegrator/P020_GSLMCIntegrator.C

%files matrix -f includelist-math-matrix
%{_libdir}/%{name}/libMatrix.*
%{_libdir}/%{name}/libMatrix_rdict.pcm

%files minuit -f includelist-math-minuit
%{_libdir}/%{name}/libMinuit.*
%{_libdir}/%{name}/libMinuit_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P020_TMinuitMinimizer.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P060_TLinearMinimizer.C
%{_datadir}/%{name}/plugins/TVirtualFitter/P010_TFitter.C

%files minuit2 -f includelist-math-minuit2
%{_libdir}/%{name}/libMinuit2.*
%{_libdir}/%{name}/libMinuit2_rdict.pcm
%dir %{_includedir}/%{name}/Minuit2
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P010_Minuit2Minimizer.C
%{_datadir}/%{name}/plugins/TVirtualFitter/P030_TFitterMinuit.C
%{_datadir}/%{name}/plugins/TVirtualFitter/P040_TFitterFumili.C

%files mlp -f includelist-math-mlp
%{_libdir}/%{name}/libMLP.*
%{_libdir}/%{name}/libMLP_rdict.pcm

%files physics -f includelist-math-physics
%{_libdir}/%{name}/libPhysics.*
%{_libdir}/%{name}/libPhysics_rdict.pcm

%files quadp -f includelist-math-quadp
%{_libdir}/%{name}/libQuadp.*
%{_libdir}/%{name}/libQuadp_rdict.pcm

%files smatrix -f includelist-math-smatrix
%{_libdir}/%{name}/libSmatrix.*
%{_libdir}/%{name}/libSmatrix_rdict.pcm
%{_libdir}/%{name}/libSmatrix32.rootmap
%{_libdir}/%{name}/libSmatrix_G__Smatrix32_rdict.pcm

%files splot -f includelist-math-splot
%{_libdir}/%{name}/libSPlot.*
%{_libdir}/%{name}/libSPlot_rdict.pcm

%files unuran -f includelist-math-unuran
%{_libdir}/%{name}/libUnuran.*
%{_libdir}/%{name}/libUnuran_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@DistSampler/P010_TUnuranSampler.C

%files vecops -f includelist-math-vecops
%{_libdir}/%{name}/libROOTVecOps.*
%{_libdir}/%{name}/libROOTVecOps_rdict.pcm

%files montecarlo-eg -f includelist-montecarlo-eg
%{_libdir}/%{name}/libEG.*
%{_libdir}/%{name}/libEG_rdict.pcm
%{_datadir}/%{name}/pdg_table.txt
%{_datadir}/%{name}/pdg_table_update.py
%doc %{_pkgdocdir}/cfortran.doc

%files montecarlo-pythia8 -f includelist-montecarlo-pythia8
%{_libdir}/%{name}/libEGPythia8.*
%{_libdir}/%{name}/libEGPythia8_rdict.pcm

%files net -f includelist-net-net
%{_libdir}/%{name}/libNet.*
%{_libdir}/%{name}/libNet_rdict.pcm
%{_datadir}/%{name}/plugins/TApplication/P010_TApplicationRemote.C
%{_datadir}/%{name}/plugins/TApplication/P020_TApplicationServer.C
%{_datadir}/%{name}/plugins/TFile/P010_TWebFile.C
%{_datadir}/%{name}/plugins/TFile/P120_TNetFile.C
%{_datadir}/%{name}/plugins/TFile/P150_TS3WebFile.C
%{_datadir}/%{name}/plugins/TFileStager/P020_TNetFileStager.C
%{_datadir}/%{name}/plugins/TSystem/P050_TWebSystem.C
%{_datadir}/%{name}/plugins/TSystem/P070_TNetSystem.C
%{_datadir}/%{name}/plugins/TVirtualMonitoringWriter/P020_TSQLMonitoringWriter.C

%files net-rpdutils
%{_libdir}/%{name}/libSrvAuth.*

%files net-auth -f includelist-net-auth
%{_libdir}/%{name}/libRootAuth.*
%{_libdir}/%{name}/libRootAuth_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualAuth/P010_TRootAuth.C
%doc %{_pkgdocdir}/README.AUTH

%files net-davix -f includelist-net-davix
%{_libdir}/%{name}/libRDAVIX.*
%{_libdir}/%{name}/libRDAVIX_rdict.pcm
%{_datadir}/%{name}/plugins/TFile/P130_TDavixFile.C
%{_datadir}/%{name}/plugins/TSystem/P045_TDavixSystem.C
%{_datadir}/%{name}/plugins/ROOT@@Internal@@RRawFile/P010_RRawFileDavix.C

%files net-http -f includelist-net-http
%{_libdir}/%{name}/libRHTTP.*
%{_libdir}/%{name}/libRHTTP_rdict.pcm
%dir %{_datadir}/%{name}/js
%dir %{_datadir}/%{name}/js/files
%{_datadir}/%{name}/js/files/canv_batch.htm
%{_datadir}/%{name}/js/files/geom_batch.htm
%{_datadir}/%{name}/js/files/web.config
%{_datadir}/%{name}/js/files/wslist.htm
%ghost %{_datadir}/%{name}/js/build
%ghost %{_datadir}/%{name}/js/img
%ghost %{_datadir}/%{name}/js/mathjax
%ghost %{_datadir}/%{name}/js/modules
%ghost %{_datadir}/%{name}/js/scripts
%ghost %{_datadir}/%{name}/js/files/draw.htm
%ghost %{_datadir}/%{name}/js/files/online.htm
%doc net/http/README.txt net/http/civetweb/*.md

%files net-httpsniff -f includelist-net-httpsniff
%{_libdir}/%{name}/libRHTTPSniff.*
%{_libdir}/%{name}/libRHTTPSniff_rdict.pcm

%files netx -f includelist-net-netxng
%{_libdir}/%{name}/libNetxNG.*
%{_libdir}/%{name}/libNetxNG_rdict.pcm
%{_datadir}/%{name}/plugins/TFile/P100_TXNetFile.C
%{_datadir}/%{name}/plugins/TFileStager/P010_TXNetFileStager.C
%{_datadir}/%{name}/plugins/TSystem/P040_TXNetSystem.C
%{_datadir}/%{name}/plugins/ROOT@@Internal@@RRawFile/P020_RRawFileNetXNG.C

%files proof -f includelist-proof-proof
%{_bindir}/proofserv
%{_bindir}/proofserv.exe
%{_mandir}/man1/proofserv.1*
%{_libdir}/%{name}/libProof.*
%{_libdir}/%{name}/libProof_rdict.pcm
%{_datadir}/%{name}/plugins/TChain/P010_TProofChain.C
%{_datadir}/%{name}/plugins/TDataSetManager/P010_TDataSetManagerFile.C
%{_datadir}/%{name}/plugins/TProof/P010_TProofCondor.C
%{_datadir}/%{name}/plugins/TProof/P020_TProofSuperMaster.C
%{_datadir}/%{name}/plugins/TProof/P030_TProofLite.C
%{_datadir}/%{name}/plugins/TProof/P040_TProof.C

%files proof-bench -f includelist-proof-proofbench
%{_libdir}/%{name}/libProofBench.*
%{_libdir}/%{name}/libProofBench_rdict.pcm
%{_datadir}/%{name}/proof

%files proof-player -f includelist-proof-proofplayer
%{_libdir}/%{name}/libProofDraw.*
%{_libdir}/%{name}/libProofDraw_rdict.pcm
%{_libdir}/%{name}/libProofPlayer.*
%{_libdir}/%{name}/libProofPlayer_rdict.pcm
%{_datadir}/%{name}/plugins/TProofMonSender/P020_TProofMonSenderSQL.C
%{_datadir}/%{name}/plugins/TVirtualProofPlayer/P010_TProofPlayer.C
%{_datadir}/%{name}/plugins/TVirtualProofPlayer/P020_TProofPlayerRemote.C
%{_datadir}/%{name}/plugins/TVirtualProofPlayer/P030_TProofPlayerLocal.C
%{_datadir}/%{name}/plugins/TVirtualProofPlayer/P040_TProofPlayerSlave.C
%{_datadir}/%{name}/plugins/TVirtualProofPlayer/P050_TProofPlayerSuperMaster.C
%{_datadir}/%{name}/plugins/TVirtualProofPlayer/P060_TProofPlayerLite.C

%files proof-sessionviewer -f includelist-gui-sessionviewer
%{_libdir}/%{name}/libSessionViewer.*
%{_libdir}/%{name}/libSessionViewer_rdict.pcm
%{_datadir}/%{name}/plugins/TProofProgressDialog/P010_TProofProgressDialog.C
%{_datadir}/%{name}/plugins/TProofProgressLog/P010_TProofProgressLog.C
%{_datadir}/%{name}/plugins/TSessionViewer/P010_TSessionViewer.C

%if %{roofit}
%files roofit -f includelist-roofit-roofit
%{_libdir}/%{name}/libRooFit.*
%{_libdir}/%{name}/libRooFit_rdict.pcm

%files roofit-core -f includelist-roofit-roofitcore
%{_libdir}/%{name}/libRooFitCore.*
%{_libdir}/%{name}/libRooFitCore_rdict.pcm
%dir %{_includedir}/%{name}/RooFit
%dir %{_includedir}/%{name}/RooFit/Detail
%dir %{_includedir}/%{name}/RooFit/TestStatistics
%dir %{_includedir}/%{name}/RooFitLegacy
%{_datadir}/gdb/auto-load%{_libdir}/%{name}/libRooFitCore.*
%{_datadir}/gdb/auto-load%{_libdir}/%{name}/__pycache__/libRooFitCore.*

%files roofit-more -f includelist-roofit-roofitmore
%{_libdir}/%{name}/libRooFitMore.*
%{_libdir}/%{name}/libRooFitMore_rdict.pcm

%files roofit-batchcompute
%{_libdir}/%{name}/libRooBatchCompute.*
%{_libdir}/%{name}/libRooBatchCompute_*

%files roofit-hs3 -f includelist-roofit-hs3
%{_libdir}/%{name}/libRooFitHS3.*
%{_libdir}/%{name}/libRooFitHS3_rdict.pcm
%dir %{_includedir}/%{name}/RooFitHS3
%{_datadir}/%{name}/RooFitHS3_wsexportkeys.json
%{_datadir}/%{name}/RooFitHS3_wsfactoryexpressions.json

%files roofit-jsoninterface -f includelist-roofit-jsoninterface
%{_libdir}/%{name}/libRooFitJSONInterface.*
%{_libdir}/%{name}/libRooFitJSONInterface_rdict.pcm
%dir %{_includedir}/%{name}/RooFit

%if %{roofitmp}
%files roofit-multiprocess -f includelist-roofit-multiprocess
%{_libdir}/%{name}/libRooFitMultiProcess.*
%dir %{_includedir}/%{name}/RooFit
%dir %{_includedir}/%{name}/RooFit/MultiProcess

%files roofit-zmq
%{_libdir}/%{name}/libRooFitZMQ.*
%endif

%files roostats -f includelist-roofit-roostats
%{_libdir}/%{name}/libRooStats.*
%{_libdir}/%{name}/libRooStats_rdict.pcm
%dir %{_includedir}/%{name}/RooStats

%files hist-factory -f includelist-roofit-histfactory
%{_bindir}/hist2workspace
%{_bindir}/prepareHistFactory
%{_mandir}/man1/hist2workspace.1*
%{_mandir}/man1/prepareHistFactory.1*
%{_libdir}/%{name}/libHistFactory.*
%{_libdir}/%{name}/libHistFactory_rdict.pcm
%{_datadir}/%{name}/HistFactorySchema.dtd
%dir %{_includedir}/%{name}/RooStats/HistFactory
%dir %{_includedir}/%{name}/RooStats/HistFactory/Detail
%doc roofit/histfactory/doc/README

%files xroofit -f includelist-roofit-xroofit
%{_libdir}/%{name}/libRooFitXRooFit.*
%{_libdir}/%{name}/libRooFitXRooFit_rdict.pcm
%dir %{_includedir}/%{name}/RooFit/xRooFit
%endif

%files sql-mysql -f includelist-sql-mysql
%{_libdir}/%{name}/libRMySQL.*
%{_libdir}/%{name}/libRMySQL_rdict.pcm
%{_datadir}/%{name}/plugins/TSQLServer/P010_TMySQLServer.C

%files sql-odbc -f includelist-sql-odbc
%{_libdir}/%{name}/libRODBC.*
%{_libdir}/%{name}/libRODBC_rdict.pcm
%{_datadir}/%{name}/plugins/TSQLServer/P050_TODBCServer.C

%files sql-sqlite -f includelist-sql-sqlite
%{_libdir}/%{name}/libRSQLite.*
%{_libdir}/%{name}/libRSQLite_rdict.pcm
%{_datadir}/%{name}/plugins/TSQLServer/P060_TSQLiteServer.C

%files sql-pgsql -f includelist-sql-pgsql
%{_libdir}/%{name}/libPgSQL.*
%{_libdir}/%{name}/libPgSQL_rdict.pcm
%{_datadir}/%{name}/plugins/TSQLServer/P020_TPgSQLServer.C

%files tmva -f includelist-tmva-tmva
%{_libdir}/%{name}/libTMVA.*
%{_libdir}/%{name}/libTMVA_rdict.pcm
%dir %{_includedir}/%{name}/TMVA
%dir %{_includedir}/%{name}/TMVA/DNN
%dir %{_includedir}/%{name}/TMVA/DNN/Architectures
%dir %{_includedir}/%{name}/TMVA/DNN/Architectures/Cpu
%dir %{_includedir}/%{name}/TMVA/DNN/Architectures/Reference
%dir %{_includedir}/%{name}/TMVA/DNN/CNN
%dir %{_includedir}/%{name}/TMVA/DNN/RNN
%license tmva/doc/LICENSE
%exclude %{_includedir}/%{name}/TMVA/RBDT.hxx
%exclude %{_includedir}/%{name}/TMVA/RInferenceUtils.hxx
%exclude %{_includedir}/%{name}/TMVA/RReader.hxx
%exclude %{_includedir}/%{name}/TMVA/RSofieReader.hxx
%exclude %{_includedir}/%{name}/TMVA/RStandardScaler.hxx
%exclude %{_includedir}/%{name}/TMVA/RTensorUtils.hxx
%exclude %{_includedir}/%{name}/TMVA/BatchGenerator/RBatchGenerator.hxx
%exclude %{_includedir}/%{name}/TMVA/BatchGenerator/RBatchLoader.hxx
%exclude %{_includedir}/%{name}/TMVA/BatchGenerator/RChunkLoader.hxx

%if %{dataframe}
%files tmva-utils
%{_libdir}/%{name}/libTMVAUtils.*
%{_libdir}/%{name}/libTMVAUtils_rdict.pcm
%dir %{_includedir}/%{name}/TMVA
%{_includedir}/%{name}/TMVA/RBDT.hxx
%{_includedir}/%{name}/TMVA/RInferenceUtils.hxx
%{_includedir}/%{name}/TMVA/RReader.hxx
%{_includedir}/%{name}/TMVA/RSofieReader.hxx
%{_includedir}/%{name}/TMVA/RStandardScaler.hxx
%{_includedir}/%{name}/TMVA/RTensorUtils.hxx
%dir %{_includedir}/%{name}/TMVA/BatchGenerator
%{_includedir}/%{name}/TMVA/BatchGenerator/RBatchGenerator.hxx
%{_includedir}/%{name}/TMVA/BatchGenerator/RBatchLoader.hxx
%{_includedir}/%{name}/TMVA/BatchGenerator/RChunkLoader.hxx
%endif

%files tmva-python -f includelist-tmva-pymva
%{_libdir}/%{name}/libPyMVA.*
%{_libdir}/%{name}/libPyMVA_rdict.pcm

%if %{rrr}
%files tmva-r -f includelist-tmva-rmva
%{_libdir}/%{name}/libRMVA.*
%{_libdir}/%{name}/libRMVA_rdict.pcm
%endif

%files tmva-sofie -f includelist-tmva-sofie
%{_libdir}/%{name}/libROOTTMVASofie.*
%{_libdir}/%{name}/libROOTTMVASofie_rdict.pcm
%doc tmva/sofie/README.md

%if %{tmvasofieparser}
%files tmva-sofie-parser -f includelist-tmva-sofie_parsers
%{_libdir}/%{name}/libROOTTMVASofieParser.*
%{_libdir}/%{name}/libROOTTMVASofieParser_rdict.pcm
%endif

%files tmva-gui -f includelist-tmva-tmvagui
%{_libdir}/%{name}/libTMVAGui.*
%{_libdir}/%{name}/libTMVAGui_rdict.pcm

%files tree -f includelist-tree-tree
%{_libdir}/%{name}/libTree.*
%{_libdir}/%{name}/libTree_rdict.pcm
%doc %{_pkgdocdir}/README.SELECTOR

%if %{dataframe}
%files tree-dataframe -f includelist-tree-dataframe
%{_libdir}/%{name}/libROOTDataFrame.*
%{_libdir}/%{name}/libROOTDataFrame_rdict.pcm
%endif

%files tree-player -f includelist-tree-treeplayer
%{_libdir}/%{name}/libTreePlayer.*
%{_libdir}/%{name}/libTreePlayer_rdict.pcm
%{_datadir}/%{name}/plugins/TFileDrawMap/P010_TFileDrawMap.C
%{_datadir}/%{name}/plugins/TVirtualTreePlayer/P010_TTreePlayer.C

%files tree-viewer -f includelist-tree-treeviewer
%{_libdir}/%{name}/libTreeViewer.*
%{_libdir}/%{name}/libTreeViewer_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualTreeViewer/P010_TTreeViewer.C

%files tree-webviewer -f includelist-tree-webviewer
%{_libdir}/%{name}/libROOTTreeViewer.*
%{_libdir}/%{name}/libROOTTreeViewer_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualTreeViewer/P020_RTreeViewer.C

%files unfold -f includelist-hist-unfold
%{_libdir}/%{name}/libUnfold.*
%{_libdir}/%{name}/libUnfold_rdict.pcm

%files cli
%{_bindir}/rootbrowse
%{_bindir}/rootcp
%{_bindir}/rootdrawtree
%{_bindir}/rooteventselector
%{_bindir}/rootls
%{_bindir}/rootmkdir
%{_bindir}/rootmv
%{_bindir}/rootprint
%{_bindir}/rootrm
%{_bindir}/rootslimtree
%{_datadir}/%{name}/cli

%files gui-webdisplay -f includelist-gui-webdisplay
%{_libdir}/%{name}/libROOTWebDisplay.*
%{_libdir}/%{name}/libROOTWebDisplay_rdict.pcm
%{_datadir}/%{name}/runfirefox.sh
%{_datadir}/%{name}/ui5

%ifarch %{qt5_qtwebengine_arches}
%files gui-qt5webdisplay
%{_libdir}/%{name}/libROOTQt5WebDisplay.*
%endif

%ifarch %{qt6_qtwebengine_arches}
%files gui-qt6webdisplay
%{_libdir}/%{name}/libROOTQt6WebDisplay.*
%endif

%files gui-webgui6 -f includelist-gui-webgui6
%{_libdir}/%{name}/libWebGui6.*
%{_libdir}/%{name}/libWebGui6_rdict.pcm
%{_datadir}/%{name}/plugins/TCanvasImp/P010_TWebCanvas.C
%{_datadir}/%{name}/plugins/TControlBarImp/P010_TWebControlBar.C

%files gui-browsable -f includelist-gui-browsable
%{_libdir}/%{name}/libROOTBrowsable.*
%{_libdir}/%{name}/libROOTBrowsable_rdict.pcm
%{_libdir}/%{name}/libROOTBranchBrowseProvider.*
%{_libdir}/%{name}/libROOTGeoBrowseProvider.*
%{_libdir}/%{name}/libROOTLeafDraw6Provider.*
%{_libdir}/%{name}/libROOTObjectDraw6Provider.*

%files gui-browserv7 -f includelist-gui-browserv7
%{_libdir}/%{name}/libROOTBrowserv7.*
%{_libdir}/%{name}/libROOTBrowserv7_rdict.pcm
%{_libdir}/%{name}/libROOTBrowserGeomWidget.*
%{_libdir}/%{name}/libROOTBrowserTCanvasWidget.*
%{_libdir}/%{name}/libROOTBrowserTreeWidget.*
%{_libdir}/%{name}/libROOTBrowserWidgets.*
%{_datadir}/%{name}/plugins/TBrowserImp/P030_RWebBrowserImp.C

%files geom-webviewer -f includelist-geom-webviewer
%{_libdir}/%{name}/libROOTGeomViewer.*
%{_libdir}/%{name}/libROOTGeomViewer_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualGeoPainter/P020_RGeoPainter.C

%if %{root7}
%files graf-gpadv7 -f includelist-graf2d-gpadv7
%{_libdir}/%{name}/libROOTGpadv7.*
%{_libdir}/%{name}/libROOTGpadv7_rdict.pcm

%files graf-primitives -f includelist-graf2d-primitivesv7
%{_libdir}/%{name}/libROOTGraphicsPrimitives.*
%{_libdir}/%{name}/libROOTGraphicsPrimitives_rdict.pcm

%files graf3d-eve7 -f includelist-graf3d-eve7
%{_libdir}/%{name}/libROOTEve.*
%{_libdir}/%{name}/libROOTEve_rdict.pcm

%files gui-browsable-v7
%{_libdir}/%{name}/libROOTHistDrawProvider.*
%{_libdir}/%{name}/libROOTLeafDraw7Provider.*
%{_libdir}/%{name}/libROOTNTupleBrowseProvider.*
%{_libdir}/%{name}/libROOTNTupleDraw6Provider.*
%{_libdir}/%{name}/libROOTNTupleDraw7Provider.*
%{_libdir}/%{name}/libROOTObjectDraw7Provider.*

%files gui-browserv7-v7
%{_libdir}/%{name}/libROOTBrowserRCanvasWidget.*

%files gui-canvaspainter
%{_libdir}/%{name}/libROOTCanvasPainter.*

%files gui-fitpanelv7 -f includelist-gui-fitpanelv7
%{_libdir}/%{name}/libROOTFitPanelv7.*
%{_libdir}/%{name}/libROOTFitPanelv7_rdict.pcm

%files histv7 -f includelist-hist-histv7
%{_libdir}/%{name}/libROOTHist.*
%{_libdir}/%{name}/libROOTHist_rdict.pcm

%files hist-draw -f includelist-hist-histdrawv7
%{_libdir}/%{name}/libROOTHistDraw.*
%{_libdir}/%{name}/libROOTHistDraw_rdict.pcm

%files tree-ntuple -f includelist-tree-ntuple
%{_libdir}/%{name}/libROOTNTuple.*
%{_libdir}/%{name}/libROOTNTuple_rdict.pcm
%dir %{_includedir}/%{name}/ROOT/libdaos_mock

%files tree-ntuple-utils -f includelist-tree-ntupleutil
%{_libdir}/%{name}/libROOTNTupleUtil.*
%{_libdir}/%{name}/libROOTNTupleUtil_rdict.pcm
%endif

%changelog
* Wed Jan 15 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.34.02-3
- Don't add dependencies on root-roofit-multiprocess and root-roofit-zmq
  to root-roofit-core for EPEL builds

* Sun Jan 12 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.34.02-2
- Adjust stressGraphics.ref
- Build for EPEL 10
- Disable the R interface for EPEL 10 (R not yet abailable)
- Enable uring support for EPEL 9 (supported in kernel since RHEL 9.3)

* Wed Dec 25 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.34.02-1
- Update to 6.34.02
- Build CLAD plugin
- Removed package: root-roofit-dataframe-helpers

* Wed Nov 27 2024 Richard W.M. Jones <rjones@redhat.com> - 6.32.08-2
- Rebuild for libarrow 18

* Thu Nov 14 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.08-1
- Update to 6.32.08

* Mon Sep 23 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.06-1
- Update to 6.32.06
- Split out ROOT 7 dependent parts of root-browsable to a separate package
- Split out ROOT 7 dependent parts of root-browserv7 to a separate package

* Wed Aug 21 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.04-2
- Re-enable Qt5 Web display for Fedora 41+ (qt5-qtwebengine fixed)

* Wed Aug 14 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.04-1
- Update to 6.32.04
- Drop patches accepted upstream
- Disable Qt5 Web display for Fedora 41+ (broken qt5-qtwebengine package)

* Sun Jul 21 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.02-4
- Update ROOT's R interface for Rcpp 1.0.13

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.32.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.02-2
- Add openssl-devel-engine build requirement on Fedora 41+
- Fixes for TUri class (PCRE2 compatibility)
- Fix test failure with tbb 2021.13.0

* Tue Jun 18 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.02-1
- Update to 6.32.02
- Drop patches accepted upstream

* Mon Jun 17 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.00-5
- Add dependency on liburing-devel to root-io
- Exclude failing tutorial-tmva-RBatchGenerator_filters_vectors-py test
  on aarch64 (Fedora 40+)

* Mon Jun 10 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.00-4
- Backport fix for failing test with Python 3.13

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 6.32.00-3
- Rebuilt for Python 3.13

* Sat Jun 08 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.00-2
- Python 3.13 compatibility

* Mon Jun 03 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.32.00-1
- Update to 6.32.00
- Drop EPEL 8 build (now requires Python >= 3.7 and tbb >= 2020)
- Dropped patches: 12
- New patches: 6
- The JsMVA python module is now a submodule of the ROOT python module
- The notebook package was merged with the JupyROOT package

* Wed May 15 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.06-5
- Rebuilt for libarrow.so.1601
- Improved fontconfig support

* Sun Apr 28 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 6.30.06-4
- Do not test with Pandas on 32-bit architectures

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 6.30.06-3
- R-maint-sig mass rebuild

* Tue Apr 23 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.06-2
- Rebuilt for libarrow.so.1600

* Fri Apr 05 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.06-1
- Update to 6.30.06

* Mon Mar 25 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.04-2
- Support StandardSymbolsPS.otf

* Wed Jan 31 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.04-1
- Update to 6.30.04
- Drop patch root-adjust-test-for-failures-on-aarch64-ppc64le-s390x.patch
  (accepted upstrem)
- Exclude failing TClingDataMemberInfo.Offset test on s390x

* Fri Jan 26 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.02-9
- Rebuilt for libarrow.so.1500

* Fri Jan 26 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.02-8
- Exclude failing gtest-math-matrix-test-testMatrixTSparse on Fedora 40
  (aarch64, ppc64le and s390x)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 6.30.02-6
- Rebuilt for TBB 2021.11

* Fri Jan 12 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.02-5
- Define PYTHON_EXECUTABLE when calling cmake (Fixes EPEL 8 build)

* Thu Dec 21 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.02-4
- Adjust tests for zlib-ng

* Mon Dec 18 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.02-3
- Use "standardsymbolsps" instead of "symbol" when searching for the
  Symbols font in order to not find Noto Symbols instead

* Fri Dec 15 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.02-2
- Exclude pyunittests-pyroot-numbadeclare test

* Sat Dec 02 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.02-1
- Update to 6.30.02

* Sat Nov 25 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.30.00-1
- Update to 6.30.00
- Removed subpackages: root-io-gfal and root-roofit-common
- Dropped patches: 6
- New patches: 6

* Thu Nov 02 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.08-3
- Rebuilt for libarrow.so.1400

* Wed Nov 01 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.08-2
- Enable RooFit::MultiProcess on Fedora 40+

* Sat Oct 14 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.08-1
- Update to 6.28.08
- New subpackage root-tmva-utils (split off from root-tmva)
- Port to pcre2

* Tue Sep 05 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.06-1
- Update to 6.28.06
- Drop patches root-testRooAbsL-test-compares-two-doubles-and-fails.patch and
  root-strlcpy.patch (fixed upstream)

* Sun Aug 06 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.04-5
- Rebuilt for libarrow.so.1300

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.28.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 09 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.04-3
- Fix build on Fedora 39+ where glibc has strlcpy and strlcat
- Enable build of root-gui-qt6webdisplay sub-package if Qt6 is available

* Mon Jun 26 2023 Orion Poplawski <orion@nwra.com> - 6.28.04-2
- Rebuilt for Python 3.12

* Mon May 08 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.04-1
- Update to 6.28.04
- Drop patch root-RF-Rewrite-RooProdPdf.TestGetPartIntList-unit-test.patch
  (previously backported)
- Enable Apache Arrow support (64 bit architectures only)

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 6.28.02-3
- R-maint-sig mass rebuild

* Thu Mar 23 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.02-2
- Disable uring in EPEL 9 (liburing is available, but uring not
  supported by kernel)

* Wed Mar 22 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.02-1
- Update to 6.28.02
- Dropped patches: 13
- New patches: 1

* Sat Mar 18 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.28.00-1
- Update to 6.28.00
- ROOT now uses llvm/clang version 13 (updated from version 9)
- Clean up specfile by removing EPEL 7 conditionals
- Drop dataframe, roofit and tmva-sofieparser on EPEL 8 ppc64le due to
  "pure virtual method called" errors
- Split the root-geom sub-package into three separate sub-packages:
  root-geom, root-geom-builder and root-geom-painter
- Enable uring support in EPEL 9 (liburing now available)
- New sub-packages: root-geom-webviewer, root-roofit-jsoninterface,
  root-testsupport, root-tree-ntuple-utils, root-tree-webviewer, root-xroofit
- Dropped patches: 31
- New patches: 17
- Updated patches: 4

* Mon Jan 30 2023 Miro Hrončok <mhroncok@redhat.com> - 6.26.10-2
- Rebuilt to change Python shebangs to /usr/bin/python3.6 on EPEL 8

* Mon Jan 30 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.10-5
- Adapt to numpy 1.24

* Fri Jan 20 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.10-4
- Add missing #include <cstdint>

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.26.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 6.26.10-2
- Rebuild for cfitsio 4.2

* Wed Nov 16 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.10-1
- Update to 6.26.10
- Drop patches root-Fixes-for-garbage-collection-in-Python-3.11.patch
  and root-Guard-gInterpreterMutex-in-TClingClassInfo-IsEnum.patch
  (fixed upstream)
- Use different filenames in io/loopdir tests
- Update root-test-timeout.patch to address one more issue

* Fri Oct 28 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.08-2
- Avoid race condition between C++ and Python version of a roofit test

* Wed Oct 19 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.08-1
- Update to 6.26.08
- Drop patch root-move-private-decl.patch (fixed upstream)
- Drop some previously backported patches
- Rename patch root-blas-linking-and-ignore-prefix.patch (partially fixed)
- Backport locking of gInterpreterMutex in TClingClassInfo::IsEnum

* Sat Oct 01 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.06-5
- Use upstream's proposed change for the Python garbage collection issue

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.26.06-4
- Rebuild for gsl-2.7.1

* Fri Aug 19 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.06-3
- Use the json 3.11 fix upstream settled on

* Wed Aug 17 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.06-2
- Compatibility with nlohmann json 3.11+
- Enable gfal support in EPEL 9 (gfal2 now available)

* Sat Jul 30 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.06-1
- Update to 6.26.06

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.26.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.04-4
- Don't use yuicompressor on Fedora (Java no longer available on ix86)

* Sun Jul 03 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.04-3
- Backport python 3.11 fixes from upstream
- Backport additional python 3.11 fixes from CPyCppyy upstream
- Exclude some failing tests on Fedora 37+
  (segfaults during Python garbage collection with Python 3.11)
- Adjust some test timeouts

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 6.26.04-2
- Rebuilt for Python 3.11

* Tue Jun 14 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.04-1
- Update to 6.26.04
- Drop patch root-missing-include.patch (accepted upstream)

* Fri May 20 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.02-3
- Rebuild for gcc 12.1 (Fedora 36)
- Update the root-tmva-threads patch

* Fri Apr 29 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.02-2
- Rebuild for gcc 11.3 (Fedora 35)
- Use upstream's version of the dataframe-snapshot on 32 bit patch

* Thu Apr 14 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.02-1
- Update to 6.26.02
- Drop patch root-roofit-overflow.patch (previously backported)

* Sat Mar 26 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.26.00-1
- Update to 6.26.00
- New subpackages: root-roofit-common, root-roofit-dataframe-helpers,
  root-roofit-hs3, root-tmva-sofie and root-tmva-sofie-parser
- Removed subpackages: root-memstat and root-montecarlo-vmc
- Drop the doxygen generated root-doc package (doxygen runs out of memory)
- Dropped patches: 17
- New patches: 22
- Updated patches: 5

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 6.24.06-6
- Rebuild for glew 2.2

* Fri Jan 28 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.24.06-5
- Exclude failing test on Fedora 36 ppc64le:
  test-stressHistFactory(-interpreted)
- Disable package note flags

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.24.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.24.06-3
- Backport gcc 12 fix from LLVM
- Fix test failure on ppc64le and aarch64 with gcc 12

* Tue Dec 07 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.24.06-2
- Fix segfaults on ppc64le when using the large code model

* Thu Nov 04 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.24.06-1
- Update to 6.24.06

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 6.24.04-2
- Rebuilt with OpenSSL 3.0.0

* Fri Aug 27 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.24.04-1
- Update to 6.24.04
- Add dependency on json-devel to root-core
- Disable uring in EPEL 8 (liburing is available, but uring not
  supported by kernel)

* Wed Aug 04 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.24.02-1
- Update to 6.24.02
- ROOT now uses llvm/clang version 9 (updated from version 5)
- No longer exclude arch s390x (better supported in llvm/clang 9)
- Drop patches accepted upstream or previously backported
- Backport some fixes that make more tests work
- New subpackages: python{2,3}-distrdf, root-roofit-batchcompute
- Require js-jsroot >= 6

* Mon Jul 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.08-11
- Drop the memstat module for Fedora 35+
  The required __malloc_hook was removed from glibc 2.33.9000-48
  The memstat module is deprecated and will be removed in root 6.26

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.22.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.08-9
- Backport fix for jsroot loading in jupyterlab

* Mon Jun 14 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.08-8
- Add configuration for jupyterlab

* Sun Jun 13 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.08-7
- cmake in EPEL 8 no longer provides cmake3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.22.08-6
- Rebuilt for Python 3.10

* Thu Jun 03 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.08-5
- Use C++17 for Fedora 34+ (gcc 11)

* Tue Jun 01 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.08-4
- Adapt to new Python RPM generators (empty .egg-info no longer works)
- Filter out parts of tests that require remote network access instead of
  excluding the whole test
- Fix multicore tests when running on machines with few cores

* Mon May 10 2021 Jonathan Wakely <jwakely@redhat.com> - 6.22.08-3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 6.22.08-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Fri Mar 19 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.08-1
- Update to 6.22.08

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 6.22.06-4
- rebuild for libpq ABI fix rhbz#1908268

* Wed Feb 03 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.06-3
- Rebuilt for cfitsio 3.490

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.22.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.06-1
- Update to 6.22.06
- Filter out additional vDSO names for ppc

* Thu Nov 26 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.04-2
- Do not attempt to load_library the ROOT Pythonizations module

* Fri Nov 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.04-1
- Update to 6.22.04
- Drop patch root-xrootd5-compat.patch (accepted upstream)

* Sat Nov 07 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.02-4
- Rebuild for C++ standard library __GLIBCXX__ 20201016

* Fri Oct 02 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.02-3
- Drop obsolete patch root-add-flexiblas-detection.patch (cmake's
  FindBLAS.cmake supports flexiblas now)
- Drop the workaround for the bug in doxygen causing different results
  on 32 and 64 bit architectures (use doxygen < 1.8.17 or >= 1.8.20-3)
- Build require xrootd 5 (Fedora 33+, EPEL 7+)

* Sun Aug 30 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.02-2
- Adapt to xrootd 5 (Fedora 33+, EPEL 7+)
  - Don't build the old proof client (xproofd)
  - Don't build the old NetX module

* Fri Aug 21 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.02-1
- Update to 6.22.02
- Drop patch previously backported: root-doxygen-endof-part1.patch
- Drop patch accepted upstream: root-python2-compat.patch
- Add back line accidentally removed in root-config
- Install headers in new PyROOT with COMPONENT headers
- Increase test timeout for ppc64le

* Thu Aug 20 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.00-7
- Avoid unneeded build requirement on srm-ifce-devel
- Do not export Python modules in CMake config
- Drop patch root-clang-ignore-gcc-options.patch
  ("Recent ROOT does not send all possible compiler flags to rootcling.")

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 6.22.00-6
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Aug 11 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.00-5
- Fix wrong symlinks in EPEL 7 python2-root package

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.22.00-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.22.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.00-2
- Fix broken update on EPEL 7 with python34-root installed

* Tue Jul 14 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.22.00-1
- Update to 6.22.00
- Drop patches accepted upstream
  - root-FitData-assert-fix.patch
  - root-clang-altivec-vector.patch
  - root-format-fix.patch
  - root-moved-file.patch
  - root-xmlmodify-dep.patch
- New and improved Python bindings
- The new Python bindings can be built for both Python 2 and Python 3
  out of the box. Dropped the workaround in specfile for this (EPEL 7)
- Dropped the python3-other packages (EPEL 7)
- The new Python bindings has split the TPython interface to a separate
  library. Now in a separate root-tpython package
- root-tpython and root-tmva-python are now using Python 3 on EPEL 7
- New subpackage root-gui-browsable
- New patches (submitted upstream)
  - Fix too aggressive -Werror replacements
  - Add missing call to TFile::SetCacheFileDir in a TMVA tutorial
  - Adjust stressGraphics.ref
  - Fix off-by-one error in histogram v7 bin iterator
  - Compatibility with python 2.7 versions before 2.7.9
  - Fix the RNTuple.LargeFile test on 32bit (i386 and armv7hf)
  - Fix doxygen issues
  - Fix bad regex in TProofMgr
  - Compatibility with xrootd 5
- Add workaround for a bug in doxygen 1.8.17 and later causing different
  results on 32 and 64 bit

* Sat Jul 11 2020 Jeff Law <law@redhat.com> - 6.20.06-2
- Disable LTO

* Thu Jun 11 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.20.06-1
- Update to 6.20.06
- Fix test failure on ppc64le and aarch64

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.20.04-3
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.20.04-2
- Replace BR qt5-devel with qt5-qtbase-devel

* Wed Apr 01 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.20.04-1
- Update to 6.20.04
- Drop previously backported patch root-tutorials-unique-filenames.patch
- Improved patch for the PyROOT issue on EPEL 7 ppc64le

* Sun Mar 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.20.02-1
- Update to 6.20.02
- Drop patches accepted upstream
  - root-dont-download-input-file-if-it-already-exists.patch
  - root-fix-plugin-definition.patch
  - root-man-install.patch
  - root-pretty-printers.patch
  - root-python3.patch
  - root-stress-aarch64-ppc64le.patch
- Drop patches no longer relevant due to changes to the code
  - root-missing-include-string.patch
  - root-static-constexpr.patch
- Add workaround for PyROOT issues on ppc64le in EPEL 7
  - root-epel7-ppc64le-pyroot.patch (patch conditionally applied)
- Fix path to moved data file in tutorial
  - root-moved-file.patch
- Split the root-roofit subpackage into four different packages
  - root-roofit, root-roofit-core, root-roofit-more and root-roostats
  - The root-roofit-more library splits out the part of roofit that depends on
    the root-mathmore package
- New subpackage: root-histv7

* Sat Mar 14 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.04-6
- Build for 32 bit ARM again - gcc-10.0.1-0.9 fixes the problem

* Sat Feb 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.04-5
- Fixes and workarounds for gcc 10
- ExcludeArch for 32 bit ARM because rootcling_stage1 segfaults (bug #1811604)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.04-3
- Fix shebangs in root-cli for EPEL 8

* Tue Dec 03 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.04-2
- Remove workarounds for RHEL 7 aarch64 (architecture dropped by EPEL 7)
- Enable QtWebEngine dependent modules on EPEL 8 (now available)

* Mon Sep 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.04-1
- Update to 6.18.04
- First build for EPEL 8

* Thu Sep 12 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.02-2
- Rebuild for g++ 9.2

* Mon Aug 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.02-1
- Update to 6.18.02
- Add workarounds for issues caused by the RHEL 7.7 update, that left the
  aarch64 architecture at RHEL 7.6.

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.18.00-5
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.18.00-4
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.00-3
- Root 6.18 requires pcm files to be in the same directory as libraries
- Add libPyROOT.rootmap and libPyROOT_rdict.pcm as slaves to libPyROOT.so
  in update-alternatives

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.18.00-1
- Update to 6.18.00
- Drop patches accepted upstream:
  - root-avoid-gui-crash.patch
  - root-doxygen-generation-with-python-3.patch
- Drop patches with alternative fix implemented upstream:
  - root-dont-install-eve7-files.patch
  - root-ix32-geom-opt.patch
- Drop ppc64 specific workaround (ppc64 no longer built in Fedora or EPEL):
  - root-ppc64-doc.patch
- Dropped subpackages:
  - root-geocad
  - root-graf-qt
  - root-gui-qt
  - root-gui-qtgsi
  - root-io-hdfs
  - root-io-rfio
  - root-net-bonjour
  - root-net-globus
  - root-net-ldap
  - root-net-krb5
  - root-table
- Drop BuildRequires needed by the dropped subpackages
- New subpackages:
  - root-graf3d-csg (split off from root-graf3d-gl)
  - root-gui-browserv7
  - root-tree-ntuple
- Don't build python2-root for Fedora >= 31
- Include desktop and MIME type files in source RPM (removed from source)
- Install man pages in correct directory
- Use correct library names in plugin definitions
- Don't download test input file if it already exists
- Python 3 fixes
- Increase test tolerance (aarch64 and ppc64le)
- Fix GDB pretty printers install name and location

* Tue Jun 11 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.16.00-6
- Use python-embed pkg-config module if it exists (python 3.8 compatibility)

* Fri May 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.16.00-5
- Build without HDFS support on Fedora 31+
  - Hadoop is FTBFS and uninstallable due to missing Java dependencies
- Build without HDFS support for 32 bit architectures on Fedora 30
  - Hadoop is not installable due to missing Eclipse dependencies

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 6.16.00-4
- Rebuilt to change main python from 3.4 to 3.6

* Mon Feb 18 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.16.00-3
- Fix typo in patch (missing space)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.16.00-2
- Rebuild for readline 8.0

* Mon Feb 11 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.16.00-1
- Update to 6.16.00
- Drop patches accepted upstream:
  - root-adjust-allowed-test-difference-for-32-bit-ix86.patch
  - root-crypto.patch
  - root-js-syntax.patch
  - root-missing-header.patch
  - root-set-cache-file-dir.patch
  - root-stressgraphics-ref.patch
  - root-test-compilation-epel7.patch
  - root-test-subdirs.patch
  - root-unique-filenames.patch
- Dropped subpackages:
  - root-rootd (obsolete - use xrootd)
  - root-proofd (obsolete - use root-xproofd)
  - root-proof-pq2
- New ROOT 7 subpackage:
  - root-graf3d-eve7
  - root-gui-webgui6
- Make tutorial/v7/line.cxx run in batch mode

* Mon Feb 04 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.14.08-4
- Remove obsolete /sbin/ldconfig scriptlets
- The root-core package installs a file in /etc/ld.so.conf.d, so it should
  always call /sbin/ldconfig and not use the macros

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 6.14.08-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Nov 23 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.14.08-1
- Update to 6.14.08
- Make tutorial filenames unique to avoid overwrites

* Tue Nov 06 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.14.06-1
- Update to 6.14.06
- Let clang ignore some gcc options it hasn't implemented
- Don't build python2-jupyroot/jsmva packages for Fedora >= 29
- Drop previously backported patch root-TGHtmlBrowser-crash.patch

* Thu Oct 25 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.14.04-3
- Fix crash in TBrowser when root-gui-html is not installed
- Use empty .egg-info files instead of empty .dist-info files to make
  virtualenv happy
- Add Requires on root-mathmore to root-mathcore (for default integrator)

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 6.14.04-2
- Rebuild for tbb 2019_U1

* Fri Aug 24 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.14.04-1
- Update to 6.14.04
- Drop patch accepted upstream: root-python-3.7.patch

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 6.14.02-2
- Rebuilt for glew 2.1.0

* Mon Aug 06 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.14.02-1
- Update to 6.14.02
- Make python3 the preferred python for Fedora 29+:
  - Give python3 libPyROOT higher priority than python2 libPyROOT
  - The python scripts in root-cli use python3-root
  - Let root-tmva-python use python3-numpy
- Fix build issue with undefined symbols in libSrvAuth
- Make ROOTConfig-targets.cmake not error on missing files to work better with
  subpackages

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.14.00-2
- Add Python 3.6 packages for EPEL 7

* Sun Jul 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.14.00-1
- Update to 6.14.00
- Drop patches previously backported:
  - root-doxygen-makefile.patch
  - root-crash-fix.patch
  - root-test-stress-32bit.patch
- Drop patches accepted upstream:
  - root-test-subdirs.patch
  - root-test-fixes.patch
  - root-out-of-bounds.patch
  - root-doxygen-tilde.patch
  - root-noinst.patch
- Drop patches for issues fixed upstream:
  - root-dont-link-jvm.patch
  - root-system-pythia.patch
- Drop patch root-urw-otf-hack.patch - broken font file no longer present
- Drop Google Droid Sans Fallback font from EPEL 7 root-fonts package
  (the font is now available in EPEL 7)
- Use two more patches from Fedora's llvm5.0 package
- New root-test-subdirs.patch patch for more instances of the same issue
- Fix a test not setting cache file directory so that it works offline
- Fix a compatibility issue with the EPEL 7 gtest version
- Fix a missing include
- Workaround optimization problems in the Geom library
- New subpackages due to library splits
  - root-tree-dataframe and root-vecops from root-tree-player
  - root-net-httpsniff from root-net-http
- New subpackages due to package splits
  - root-gui-html from root-gui
  - root-gui-qtgsi from root-gui-qt
  - root-io-xmlparser from root-io-xml
  - root-proof-player from root-proof
- New ROOT 7 subpackages
  - root-graf-gpadv7
  - root-graf-primitives
  - root-gui-fitpanelv7
  - root-gui-qt5webdisplay
- Rename root-guibuilder package to root-gui-builder
- Create empty .dist-info files so that rpm auto-generates provides

* Sat Jun 30 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.12.06-5
- Adjust Vavilov test for Fedora 29 ix86
- Adapt to python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.12.06-4
- Rebuilt for Python 3.7

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 6.12.06-3
- rebuilt for cfitsio 3.450
- Adjust allowed deviation for PDF file sizes in stressGraphics test (aarch64)

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 6.12.06-2
- rebuilt for cfitsio 3.420 (so version bump)
- modified patch 13 to also produce smaller debuginfo on x86 (ld out of memory)
- disabled test gtest-tree-treeplayer-test-dataframe-snapshot on ARM

* Sat Feb 17 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.12.06-1
- Update to 6.12.06
- Drop patch root-Fix-constructing-the-GSL-MC-Integrator.patch (previously
  backported)

* Fri Feb 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.12.04-4
- Fix test failures found with new default compiler flags in Fedora 28

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.12.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 6.12.04-2
- Rebuilt for switch to libxcrypt

* Tue Dec 19 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.12.04-1
- Update to 6.12.04
- Drop patches accepted upstream
- Drop previously backported patches
- Unbundle jsroot in root-net-http
- Add hack to work around broken charmaps in StandardSymbolsPS.otf
- Use local static script and style files for JupyROOT
- Fix some javascript errors
- Fix build rules for test binaries so that they are not installed
- Address memory usage issue for ARM build
- Drop pre-minified javascript and style files (Fedora packaging guidelines)
- Enable builds on ppc/ppc64/ppc64le (do not pass all tests, but the list
  of failing tests is much shorter with this release)
- Add dependency on python[23]-jsmva to python[23]-jupyroot
- New sub-packages: root-gui-canvaspainter, root-gui-webdisplay and
  root-hist-draw (not for EPEL 7 since they are root7 specific and
  require c++-14)

* Fri Oct 20 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.08-1
- Update to 6.10.08
- Add BuildRequires on lz4-devel and xxhash-devel
- Workaround for missing gmock libraries only needed for gmock < 0.1.8
- Address some warnings during documentation generation

* Wed Sep 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.06-1
- Update to 6.10.06
- Fixes for new mysql_config

* Sat Aug 05 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.04-1
- Update to 6.10.04
- Add temporary workaround for broken mariadb headers in Fedora 27

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.02-3
- Remove additional references in cmake files

* Mon Jul 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.02-2
- Fix removal of mathtext, minicern and JupyROOT references from cmake files

* Fri Jul 07 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.02-1
- Update to 6.10.02

* Wed Jun 14 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10.00-1
- Update to 6.10.00
- Drop patches accepted upstream
- Drop previously backported patches
- New sub-package: root-unfold
- Dropped sub-package: root-vdt

* Tue May 16 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.08.06-7
- Remove JupyROOT references from cmake files
- Do not generate autoprovides for libJupyROOT.so

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.08.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri May 12 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.08.06-5
- Fix for macro scope issue (backport from upstream)
- Fix a problem loading the libJupyROOT CDLL module (use absolute path)
- Add ipython dependencies to the jupyroot packages
- Exclude s390x - endian issues
- Re-enable two tests on 32 bit arm - no longer failing
- Add BuildRequires on blas-devel (for TMVA)

* Thu May 11 2017 Richard Shaw <hobbes1069@gmail.com> - 6.08.06-4
- Rebuild for OCE 0.18.1.

* Fri Apr 21 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.08.06-3
- Python 3 compatibility fixes (backport from upstream)

* Wed Mar 15 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.08.06-2
- Fix relocation problems on aarch64 - using patch from the llvm package
- Re-enable building on aarch64 - works again with the above patch

* Thu Mar 02 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.08.06-1
- Update to 6.08.06
- Drop obsolete patch: root-tformulaparsingtests.patch
- Drop patches accepted upstream: root-spectrum-batch.patch and
  root-missing-header-gcc7.patch
- Disable failing tests on s390x

* Wed Mar 01 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.08.04-3
- Disable building on aarch64 (it is now broken again)
- Add missing header (gcc 7)
- Fix a test failure on Fedora 26 i686
- Fix some format warnings/errors in GlobusAuth
- Use the right delimiter when splitting the icon path in TASImage
- Disable two more tests on 32 bit arm

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.08.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.08.04-1
- Update to 6.08.04
- Fix broken TPad::WaitPrimitive (backport from git)
- Rebuild for gcc 6.3

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 6.08.02-4
- Rebuild for readline 7.x

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 6.08.02-3
- Rebuild for glew 2.0.0

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 6.08.02-2
- Rebuild for Python 3.6

* Tue Dec 06 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.08.02-1
- Update to 6.08.02
- Drop patches accepted upstream
- Drop previously backported patches
- Drop obsolete patches
- Enable hadoop/hdfs support for all architectures
  * libhdfs is now available for more architectures than ix86 and x86_64
- Enable building on aarch64
- Rename the python packages to python2-root and python3-root
- New sub-packages: python{2,3}-jupyroot, python{2,3}-jsmva
- Dropped sub-package: root-rootaas (replaced by python{2,3}-jupyroot)

* Wed Sep 28 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.06.08-2
- Rebuild for gcc 6.2

* Thu Sep 08 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.06.08-1
- Update to 6.06.08
- Add the packages providing the libraries listed by "root-config --libs"
  as dependencies to root-core
- Add missing scriptlets to root-multiproc

* Sun Aug 14 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.06.06-4
- Convert init scripts to systemd unit files

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.06.06-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 18 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.06.06-2
- Add requires on redhat-rpm-config to root-cling

* Sun Jul 10 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.06.06-1
- Update to 6.06.06
- Drop patches root-gfal2.patch and root-keysymbols.patch
- Make root-vdt package noarch

* Sun Jun 19 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.06.04-4
- Add GuiTypes.h, KeySymbols.h and Buttons.h to dict (backport)
- Minor updates to patches - mostly backported from upstream
- Reenable hadoop/hdfs support for F24+

* Mon Jun 13 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.06.04-3
- Remove mathtext and minicern references from cmake files
- Fix the spelling of CMAKE_Fortran_FLAGS in a few places

* Sat Jun 04 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.06.04-2
- Disable hadoop/hdfs support for F24+ (hadoop was retired)

* Mon May 09 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.06.04-1
- Update to 6.06.04
- Drop patch root-no-hexfloat-const.patch
- Add requires on gcc-c++ to root-cling

* Fri Apr 15 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.06.02-2
- Rebuild for OCE-0.17.1

* Fri Apr 08 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.06.02-1
- Update to 6.06.02 (F24+, EPEL7)
- Change to cmake configuration (was using ./configure)
- Change to doxygen documentation generation (was using THTML)
- Run the test suite
- Remove compatibility with older EPEL (Group tags, BuildRoot tag, etc.)
- New sub-packages: root-multiproc, root-cling, root-r, root-r-tools,
  root-geocad, root-tmva-python, root-tmva-r, root-tmva-gui, root-cli,
  root-notebook and root-rootaas
- New subpackage for EPEL7: root-python34
- Dropped sub-packages: root-cint, root-reflex, root-cintex, root-ruby

* Fri Apr 08 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.36-1
- Update to 5.34.36

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.32-8
- Rebuild again for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 5.34.32-7
- Rebuild for glew 1.13

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 5.34.32-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Tue Nov 17 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.32-5
- Adapt to gfal 2.10 - uses a different #define
- Exclude ppc64le - has the same issues with cint as ppc and ppc64

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34.32-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 25 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.32-3
- Add versioned dependencies between packages
- Reenable hadoop/hdfs support for F23+

* Wed Sep 16 2015 David Abdurachmanov <davidlt@cern.ch> - 5.34.32-2
- Disable run-time dependency on gccxml in Reflex (allows installing on aarch64) (#1263206)
- Enable Cintex on aarch64

* Thu Jul 02 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.32-1
- Update to 5.34.32
- New sub-package: root-fonts (STIX version 0.9 required by TMathText)
- Use GNU Free instead of Liberation, works better with TMathText
- Fix segfault when embedding Type 1 fonts
- Drop patch root-no-extra-formats.patch (workaround for above problem)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.30-1
- Update to 5.34.30
- New sub-package: root-python3
- Disable hadoop/hdfs support for F23+ (not installable)
- Drop previously backported gcc 5 patches

* Fri Apr 03 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.28-1
- Update to 5.34.28
- Merge emacs support files into main package (guidelines updated)

* Tue Feb 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.26-1
- Update to 5.34.26
- Drop patch root-xrdversion.patch

* Thu Jan 29 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.24-3
- Rebuild with fixed cairo (bz 1183242)

* Sat Jan 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.34.24-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Fri Dec 19 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.24-1
- Update to 5.34.24
- Drop patch root-bsd-misc.patch

* Thu Aug 28 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.20-2
- Move xproofd binaries from root-proofd to root-xproof
- Adjust EPEL 7 font dependencies
- Rebuild using new binutils (ld bug fixed - F21+)

* Wed Aug 20 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.20-1
- Update to 5.34.20
- Re-enable xrootd support for F21+ and EPEL7 (now ported to xrootd 4)
- Do not depend on wine's fonts
- Drop patch root-gccopt.patch

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.19-1
- Update to 5.34.19
- Disable xrootd support for F21+ and EPEL7 (root not yet ported to xrootd 4)
- New sub-package: root-net-http
- Drop patches root-thtml-revert.patch, root-gfal2.patch and
  root-proofx-link-iolib.patch

* Mon Jun 30 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.18-4
- Add Requires on root-tree-player to root-gui-ged

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.18-2
- Rebuild for ruby 2.1
- Fix build failure on F21 (missing symbol in libProofx linking)

* Sat Mar 22 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.18-1
- Update to 5.34.18
- Build GFAL module using libgfal2
- New sub-package: root-vdt

* Wed Feb 26 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.17-1
- Update to 5.34.17

* Fri Feb 14 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.15-1
- Update to 5.34.15
- Drop patch root-davix.patch

* Thu Jan 09 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.14-3
- Rebuild for cfitsio 3.360

* Mon Dec 23 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.14-2
- Adapt to davix >= 0.2.8

* Thu Dec 19 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.14-1
- Update to 5.34.14
- New sub-package: root-net-davix
- Drop patch root-pythia8-incdir.patch

* Tue Dec 03 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.13-1
- Update to 5.34.13
- Remove java-devel build dependency (not needed with Fedora's libhdfs)
- Adapt to pythia8 >= 8.1.80

* Mon Nov 25 2013 Orion Poplawski <orion@cora.nwra.com> - 5.34.10-3
- Fix hadoop lib location

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 5.34.10-2
- rebuilt for GLEW 1.10

* Mon Sep 09 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.10-1
- Update to 5.34.10
- New sub-package: root-io-hdfs (Fedora 20+)
- New sub-package: root-sql-sqlite

* Thu Aug 08 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.09-5
- Exclude armv7hl - cint is not working
- Use _pkgdocdir when defined
- Use texlive-stix

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 5.34.09-3
- Perl 5.18 rebuild

* Tue Jul 16 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.09-2
- Rebuild for cfitsio 3.350

* Fri Jun 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.09-1
- Update to 5.34.09
- New sub-package: root-montecarlo-pythia8
- Drop patch root-gfal-bits.patch
- Use xz compression for source tarfile
- Update ancient root version in EPEL

* Sat Apr 27 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.07-1
- Update to 5.34.07

* Sat Apr 27 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.06-1
- Update to 5.34.06
- Drop patches root-gviz.patch, root-ruby-version.patch,
  root-rev48681.patch and root-rev48831.patch

* Wed Mar 20 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.05-2
- Rebuild for ruby 2.0
- Rebuild for cfitsio 3.340

* Wed Feb 27 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.05-1
- Update to 5.34.05
- Rebuild for xrootd 3.3
- Patch for latest graphviz (libcgraph)
- Drop patches root-glibc.patch and root-tclass-fix.patch

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 5.34.02-2
- Rebuild for glew 1.9.0

* Fri Oct 12 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.02-1
- Update to 5.34.02

* Sat Jul 28 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.01-2
- Rebuild for glew 1.7

* Tue Jul 17 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.01-1
- Update to 5.34.01
- Remove sub-packages root-clarens and root-peac (dropped by upstream)

* Thu Jul 05 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.00-2
- Do the glibc 2.16 patch properly

* Sat Jun 09 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.34.00-1
- Update to 5.34.00
- New sub-package: root-io-gfal

* Thu May 17 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.32.03-1
- Update to 5.32.03

* Thu Mar 29 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.32.02-1
- Update to 5.32.02

* Sat Mar 17 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.32.01-2
- Rebuild for xrootd 3.1.1

* Sat Mar 03 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.32.01-1
- Update to 5.32.01
- Drop patches fixed upstream

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.32.00-3
- Rebuilt for c++ ABI breakage

* Tue Feb 14 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.32.00-2
- Adapt to new ruby packaging guidelines

* Fri Feb 10 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.32.00-1
- Update to 5.32.00

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 5.30.04-3
- Rebuild against PCRE 8.30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.30.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.30.04-1
- Update to 5.30.04

* Sat Oct 22 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.30.03-1
- Update to 5.30.03

* Fri Sep 23 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.30.02-1
- Update to 5.30.02

* Thu Aug 18 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.30.01-1
- Update to 5.30.01
- Drop patches root-lzma-searchorder.patch and root-cint-i686.patch

* Wed Aug 17 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.30.00-3
- Backport upstream's fix for the i686 rootcint problem

* Tue Jul 26 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.30.00-2
- Add workaround for rootcint problem on i686
- Pass default LDFLAGS (relro) to make

* Sun Jul 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.30.00-1
- Update to 5.30.00
- Drop patch root-listbox-height.patch
- New sub-package: root-proof-bench

* Wed Jun 29 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00e-2
- Change build requires from qt-devel to qt4-devel

* Wed Jun 29 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00e-1
- Update to 5.28.00e

* Mon Jun 20 2011 ajax@redhat.com - 5.28.00d-2
- Rebuild for new glew soname

* Fri May 13 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00d-1
- Update to 5.28.00d

* Mon May 02 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00c-1.1
- Fix emacs Requires on RHEL5

* Thu Apr 21 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00c-1
- Update to 5.28.00c

* Wed Mar 23 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00b-2
- Rebuild for mysql 5.5.10

* Sat Mar 19 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00b-1
- Update to 5.28.00b

* Mon Feb 21 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00a-1
- Update to 5.28.00a
- Drop patches fixed upstream: root-afterimage.patch, root-htmldoc.patch,
  root-xlibs-ppc.patch, root-cstddef.patch
- Remove the fedpkg workaround - no longer needed

* Sat Feb 12 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00-4
- Add workaround for changes in fedpkg

* Thu Feb 10 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00-3
- Add Requires on root-graf-postscript to root-gpad
- Require libAfterImage 1.20 or later to fix issues with circular markers in
  batch mode
- Add python26 subpackage for EPEL 5
- Fix an issue where the last item in a TGFontTypeComboBox is almost
  invisible (backported from upstream)
- Add missing cstddef includes for gcc 4.6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.28.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00-1.1
- Fix linking of Xlibs on ppc

* Wed Dec 15 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.28.00-1
- Update to 5.28.00
- Drop patches fixed upstream: root-linker-scripts.patch, root-dpm-rfio.patch,
  root-missing-explicit-link.patch, root-split-latex.patch,
  root-cern-filename.patch, root-make-3.82.patch,
  root-fonttype-combobox-dtor.patch
- New sub-packages: root-genetic, root-graf-fitsio, root-hist-factory,
  root-proof-pq2
- Make root-io a separate package again - the circular dependency with the
  root-core package was resolved upstream

* Fri Nov 12 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00e-3
- Fix crash in TGFontTypeComboBox destructor
- Add Requires on root-gui-ged to root-gui

* Mon Nov 01 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00e-2
- Rebuild for updated unuran

* Fri Oct 22 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00e-1
- Update to 5.26.00e
- Drop patch fixed upstream: root-tmva-segfault.patch
- Add Requires on root-proof to root-proofd

* Sat Oct 02 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00d-3
- Add Requires on root-graf-asimage to root-core
- Add Requires on root-graf-x11 to root-gui
- Add Requires on root-hist-painter to root-hist
- Add Requires on root-minuit to root-mathcore
- Add Requires on krb5-workstation to root-net-krb5
- Add BuildRequires on krb5-workstation

* Mon Aug 30 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00d-2
- Adapt makefile to changes in make 3.82

* Fri Aug 27 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00d-1
- Update to 5.26.00d
- Improved doc generation script

* Mon Aug 02 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00c-4
- Don't remove the prec_stl directory
- Create a separate tutorial package for the tutorial and test suite

* Thu Jul 29 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00c-3
- Correct license tags for: cint, core and roofit
- Regenerate source tarball due to upstream retag (again)

* Fri Jul 16 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00c-2
- Add dependency on gccxml for globus-reflex
- Split some packages to break circular package dependencies
- Merge libRIO into root-core
- Regenerate source tarball due to upstream retag

* Mon Jul 12 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00c-1
- Update to 5.26.00c
- Disable cint7 package - no longer compiles and has been deprecated upstream

* Wed Jun 09 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00b-3
- Use external xrootd
- Make documentation selfcontained - can be read without network access

* Wed May 19 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00b-2
- Fix library detection when linker scripts are used
- Allow building RFIO IO modules using DPM's RFIO implementation

* Sat Mar 20 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00b-1
- Update to 5.26.00b
- Enable dCache support - dcap library is now in Fedora
- Use system unuran library instead of embedded sources

* Mon Feb 01 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00a-1
- Update to 5.26.00a
- Disable cintex package for non-intel architectures
- Remove embedded gl2ps sources

* Wed Jan 13 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.26.00-1
- Update to 5.26.00
- Drop patches fixed upstream: root-globus.patch, root-dot-png.patch,
  root-loadmeta.patch, root-openssl.patch, root-hash-endian.patch

* Fri Nov 27 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.24.00b-1
- Initial build
