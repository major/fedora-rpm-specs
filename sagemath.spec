%global __provides_exclude_from	.*/site-packages/.*\\.so

# This package installs python files in nonstandard places
%global _python_bytecompile_extra 0

%bcond_with bundled_pexpect
%bcond_with bundled_ipython
%bcond_without bundled_jupyter_jsmol
%bcond_without bundled_memory_allocator
%bcond_without bundled_threejs
%bcond_without install_hack

# for faster full rpm test builds
%ifarch %{ix86} x86_64
%bcond_without docs
%else
%bcond_with docs
%endif

# use a workaround to match upstream sagemath patched sphinx
%bcond_with sphinx_hack

# use workaround to match upstream sagemath patched cython
%bcond_with cython_hack

# switch to run make -testall
%bcond_with check
%global SAGE_TIMEOUT		60
%global SAGE_TIMEOUT_LONG	180

%global combinatorial_designs_pkg	combinatorial_designs-20140630
%global conway_polynomials_pkg	conway_polynomials-0.5
%global cremona_ver		2019-10-29
%global	elliptic_curves_pkg	elliptic_curves-0.8.1
%global graphs_pkg		graphs-20210214
%if %{with bundled_ipython}
%global ipython_ver		8.6.0
%global ipython_pkg		ipython-%{ipython_ver}
%global prompt_toolkit_ver	3.0.24
%global prompt_tookit_pkg	prompt_toolkit-%{prompt_toolkit_ver}
%endif
%if %{with bundled_jupyter_jsmol}
%global jupyter_jsmol_ver	2022.1.0
%global jupyter_jsmol_pkg	jupyter_jsmol-%{jupyter_jsmol_ver}
%endif
%if %{with bundled_memory_allocator}
%global memory_allocator_ver	0.1.3
%global memory_allocator_pkg	memory_allocator-%{memory_allocator_ver}
%endif
%if %{with bundled_pexpect}
%global pexpect_pkg		pexpect-4.8.0
%endif
%global polytopes_db_pkg	polytopes_db-20170220
%global sagetex_pkg		sagetex-3.6.1
%global Sphinx_pkg		Sphinx-5.2.3
%global singular_pkg		singular-4.3.1p1
%if %{with bundled_threejs}
%global threejs_ver		r122
%global threejs_pkg		threejs-sage-%{threejs_ver}
%endif

# Spkg equivalents of required rpms; we pretend they are installed as spkgs.
%global SAGE_REQUIRED_PKGS 4ti2-1.6.9 bliss-0.77 CoCoALib-0.99800 coxeter3-3.1 cryptominisat-5.8.0 database_cremona_ellcurve-%{cremona_ver} gap_packages-4.11.2 libsirocco-2.1.0 lrslib-072 mcqd-1.0.0 meataxe-1.0.1 qepcad-B.1.74 saclib-2.2.8 tdlib-0.9.2

%global SAGE_ROOT		%{_libdir}/sagemath
%global SAGE_LOCAL		%{SAGE_ROOT}/local
%global SAGE_SRC		%{SAGE_ROOT}/src
%global SAGE_DOC		%{_docdir}/%{name}
%global SAGE_SHARE		%{_datadir}/sagemath
%global SAGE_ETC		%{SAGE_SHARE}/etc
%global SAGE_PYTHONPATH		%{SAGE_ROOT}/site-packages
%global SAGE_SPKG_INST		%{SAGE_LOCAL}/var/lib/sage/installed

Name:		sagemath
Summary:	A free open-source mathematics software system
Version:	9.8
Release:	2%{?dist}
# The file ${SAGE_ROOT}/COPYING.txt is the upstream license breakdown file.
# Note that many of the components listed in that file are not built in, but
# are used as external libraries, and therefore do not affect the License tag.
# Additionally, every $files section has a comment with the license name
# before files with that license
License:	GPL-3.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:		http://www.sagemath.org
Source0:	http://files.sagemath.org/src/sage-%{version}.tar.gz
Source1:	https://github.com/JohnCremona/ecdata/archive/%{cremona_ver}/cremona-%{cremona_ver}.tar.gz
Source2:	gprc.expect
Source3:	org.sagemath.sage.metainfo.xml
# Follow maxima's ExclusiveArch.  The source RPM is now about 2GB in size.  The
# 32-bit ARM builders run out of memory trying to create the SRPM and also
# trying to unpack the SRPM before starting a build.  The i386 builders
# sometimes fail as well, so exclude all 32-bit platforms.
ExclusiveArch:	aarch64 x86_64

# Fix stray escapes in python strings
Patch0:		%{name}-escape.patch

# Fix a "random" bit chooser that always chooses 0
Patch1:		%{name}-random.patch

# Set of patches to work with system wide packages
Patch2:		%{name}-scripts.patch

# Fix building extensions with system header files and libraries
Patch3:		%{name}-extensions.patch

# helper to:
#	o respect a DESTDIR environment variable
#	o avoid double '//' in pathnames, which can confuse debugedit & co
#	o minor change to help in incremental builds by avoiding rebuilding
#	  files
#	o do not assume there is an installed sagemath
Patch4:		%{name}-rpmbuild.patch

# build documentation in buildroot environment
Patch5:		%{name}-sagedoc.patch

# work with all maxima-runtime lisp backend packages
Patch6:		%{name}-maxima.patch

# use jmol itself to export preview images
# FIXME besides not using X and told so, fails if DISPLAY is not set
Patch7:		%{name}-jmol.patch

# tell the user how to install the large Cremona database
# add a missing commit() that causes large database construction to fail
# https://github.com/sagemath/sage/pull/35050
Patch8:		%{name}-cremona.patch

# adapt to python 3 and cython running in python 3 mode
Patch9:		%{name}-python3.patch

# remove the buildroot path from Cython output
Patch10:	%{name}-buildroot.patch

# update c++ standard to fix FTBFS
Patch11:	%{name}-lcalc.patch

# Use system gap directories and modernize libgap interface
Patch12:	%{name}-libgap.patch

# Catch polymorphic types by reference instead of by value
Patch13:	%{name}-catch-value.patch

# Side effect of using distro packages
# https://bugzilla.redhat.com/show_bug.cgi?id=974769
Patch14:	%{name}-env.patch

# Correct unable to start QEPCAD within sage
# https://bugzilla.redhat.com/show_bug.cgi?id=1243590
Patch15:	%{name}-qepcad.patch

# Make the cvxopt backend check for 'optimal' as well as 'optimized'
Patch16:	%{name}-cvxopt.patch

# Use flexiblas
Patch17:	%{name}-flexiblas.patch

# Fix paths to latte-integrale binaries
Patch18:	%{name}-latte.patch

# Adapt to recent tdlib 0.9
Patch19:	%{name}-tdlib.patch

# Use local objects.inv for intersphinx since no network on koji builders
Patch20:	%{name}-intersphinx.patch

# Replace a deprecated call to std::bind2nd
Patch21:	%{name}-bind2nd.patch

# Temporary workaround for https://bugzilla.redhat.com/show_bug.cgi?id=2160197
# Remove this when that bug is fixed
Patch22:	%{name}-giac.patch

# Replace a deprecated call to std::mem_fun_ref
Patch23:	%{name}-mem-fun-ref.patch

BuildRequires:	4ti2
BuildRequires:	4ti2-devel
BuildRequires:	appstream
BuildRequires:	arb-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bc
BuildRequires:	bliss-devel
BuildRequires:	boost-devel
BuildRequires:	brial-devel
BuildRequires:	chrpath
BuildRequires:	cmake
BuildRequires:	cddlib-devel
BuildRequires:	cddlib-tools
BuildRequires:	cliquer-devel
BuildRequires:	cocoalib-devel
BuildRequires:	coxeter-devel
BuildRequires:	cryptominisat-devel
BuildRequires:	csdp-devel
BuildRequires:	desktop-file-utils
BuildRequires:	dvipng
BuildRequires:	ecl
BuildRequires:	ffmpeg-free
BuildRequires:	flexiblas-devel
BuildRequires:	flint-devel
BuildRequires:	flintqs
BuildRequires:	fonttools
BuildRequires:	gap-devel
BuildRequires:	gap-pkg-aclib
BuildRequires:	gap-pkg-alnuth
BuildRequires:	gap-pkg-atlasrep
BuildRequires:	gap-pkg-autodoc
BuildRequires:	gap-pkg-autpgrp
BuildRequires:	gap-pkg-cohomolo
BuildRequires:	gap-pkg-corelg
BuildRequires:	gap-pkg-crime
BuildRequires:	gap-pkg-crisp
BuildRequires:	gap-pkg-cryst
BuildRequires:	gap-pkg-crystcat
BuildRequires:	gap-pkg-ctbllib
BuildRequires:	gap-pkg-design
BuildRequires:	gap-pkg-edim
BuildRequires:	gap-pkg-factint
BuildRequires:	gap-pkg-fga
BuildRequires:	gap-pkg-gbnp
BuildRequires:	gap-pkg-genss
BuildRequires:	gap-pkg-guava
BuildRequires:	gap-pkg-hap
BuildRequires:	gap-pkg-hapcryst
BuildRequires:	gap-pkg-hecke
BuildRequires:	gap-pkg-images
BuildRequires:	gap-pkg-irredsol
BuildRequires:	gap-pkg-jupyterkernel
BuildRequires:	gap-pkg-laguna
BuildRequires:	gap-pkg-liealgdb
BuildRequires:	gap-pkg-liepring
BuildRequires:	gap-pkg-liering
BuildRequires:	gap-pkg-loops
BuildRequires:	gap-pkg-lpres
BuildRequires:	gap-pkg-mapclass
BuildRequires:	gap-pkg-polenta
BuildRequires:	gap-pkg-polycyclic
BuildRequires:	gap-pkg-polymaking
BuildRequires:	gap-pkg-qpa
BuildRequires:	gap-pkg-quagroup
BuildRequires:	gap-pkg-radiroot
BuildRequires:	gap-pkg-repsn
BuildRequires:	gap-pkg-resclasses
BuildRequires:	gap-pkg-singular
BuildRequires:	gap-pkg-sla
BuildRequires:	gap-pkg-sonata
BuildRequires:	gap-pkg-sophus
BuildRequires:	gap-pkg-tomlib
BuildRequires:	gap-pkg-toric
BuildRequires:	gap-pkg-utils
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	gcc-objc
BuildRequires:	gcc-objc++
BuildRequires:	gdb
BuildRequires:	gengetopt
BuildRequires:	gfan
BuildRequires:	giac-devel
BuildRequires:	giac-doc
BuildRequires:	git-core
BuildRequires:	glpk-devel
BuildRequires:	glpk-utils
BuildRequires:	gmp-ecm
BuildRequires:	gmp-ecm-devel
BuildRequires:	gnupg2
BuildRequires:	gp2c
BuildRequires:	ImageMagick
BuildRequires:	iml-devel
BuildRequires:	jmol
# To have a proper link
BuildRequires:	jsmol
BuildRequires:	jsmath-fonts
BuildRequires:	L-function-devel
BuildRequires:	latexmk
BuildRequires:	latte-integrale
BuildRequires:	libbraiding-devel
BuildRequires:	libfrobby-devel
BuildRequires:	libgap
BuildRequires:	libhomfly-devel
BuildRequires:	libmpc-devel
BuildRequires:	libtool
BuildRequires:	lrcalc-devel
BuildRequires:	lrslib-utils
BuildRequires:	make
BuildRequires:	mathjax
BuildRequires:	maxima-runtime-ecl
BuildRequires:	mcqd-devel
BuildRequires:	meson
BuildRequires:	mpfi-devel
BuildRequires:	nauty
BuildRequires:	ninja-build
BuildRequires:	ntl-devel
BuildRequires:	openssh
BuildRequires:	openssl
BuildRequires:	palp
BuildRequires:	pandoc
BuildRequires:	pari-devel
BuildRequires:	pari-elldata
BuildRequires:	pari-galdata
BuildRequires:	pari-galpol
BuildRequires:	pari-gp
BuildRequires:	pari-nftables
BuildRequires:	pari-seadata
BuildRequires:	patchelf
BuildRequires:	pdf2svg
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Slurp)
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	pkgconfig(cbc)
BuildRequires:	pkgconfig(eclib)
BuildRequires:	pkgconfig(factory)
BuildRequires:	pkgconfig(fplll)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gdlib)
BuildRequires:	pkgconfig(gf2x)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(igraph)
BuildRequires:	pkgconfig(isl)
BuildRequires:	pkgconfig(libavdevice)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgvc)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libsemigroups)
BuildRequires:	pkgconfig(libzmq)
BuildRequires:	pkgconfig(linbox)
BuildRequires:	pkgconfig(m4ri)
BuildRequires:	pkgconfig(m4rie)
BuildRequires:	pkgconfig(nauty)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(primecount)
BuildRequires:	pkgconfig(primesieve)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(Singular)
BuildRequires:	pkgconfig(tbb)
BuildRequires:	pkgconfig(tk)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	planarity-devel
BuildRequires:	polymake
BuildRequires:	ppl-devel
BuildRequires:	python3-devel
BuildRequires:	python3-docs
BuildRequires:	python3-cypari2-devel
BuildRequires:	python3-cysignals-devel
%if %{without bundled_ipython}
BuildRequires:	python3-ipython-sphinx
%endif
BuildRequires:	python3-pillow-devel
BuildRequires:	python3-pplpy-devel
BuildRequires:	python3-tdlib-devel
BuildRequires:	python3-tkinter
BuildRequires:	pythran
BuildRequires:	%{py3_dist argon2-cffi}
BuildRequires:	%{py3_dist asttokens}
%if %{with bundled_ipython}
BuildRequires:	%{py3_dist backcall}
%endif
BuildRequires:	%{py3_dist beautifulsoup4}
BuildRequires:	%{py3_dist beniget}
BuildRequires:	%{py3_dist brial}
BuildRequires:	%{py3_dist charset-normalizer}
BuildRequires:	%{py3_dist colorlog}
BuildRequires:	%{py3_dist contourpy}
BuildRequires:	%{py3_dist cppy}
BuildRequires:	%{py3_dist cvxopt}
BuildRequires:	%{py3_dist cython}
BuildRequires:	%{py3_dist deprecation}
BuildRequires:	%{py3_dist docutils}
BuildRequires:	%{py3_dist editables}
BuildRequires:	%{py3_dist executing}
BuildRequires:	%{py3_dist flit-core}
BuildRequires:	%{py3_dist fpylll}
BuildRequires:	%{py3_dist furo}
BuildRequires:	%{py3_dist gast}
BuildRequires:	%{py3_dist gmpy2}
BuildRequires:	%{py3_dist hatch-fancy-pypi-readme}
BuildRequires:  %{py3_dist hatchling}
%if %{with sphinx_hack}
BuildRequires:	%{py3_dist html5lib}
BuildRequires:	%{py3_dist imagesize}
%endif
BuildRequires:	%{py3_dist idna}
BuildRequires:	%{py3_dist importlib-metadata}
BuildRequires:	%{py3_dist ipykernel}
%if %{without bundled_ipython}
BuildRequires:	%{py3_dist ipython}
%endif
BuildRequires:	%{py3_dist ipywidgets}
%if %{with bundled_ipython}
BuildRequires:	%{py3_dist jedi}
%endif
BuildRequires:	%{py3_dist jupyter-packaging}
BuildRequires:	%{py3_dist jupyter-sphinx}
BuildRequires:	%{py3_dist jupyterlab-pygments}
BuildRequires:	%{py3_dist kiwisolver}
BuildRequires:	%{py3_dist lrcalc}
BuildRequires:	%{py3_dist matplotlib}
BuildRequires:	%{py3_dist matplotlib-inline}
BuildRequires:	%{py3_dist nbclient}
BuildRequires:	%{py3_dist nbconvert}
BuildRequires:	%{py3_dist nbformat}
BuildRequires:	%{py3_dist nest-asyncio}
BuildRequires:	%{py3_dist networkx}
BuildRequires:	%{py3_dist notebook}
BuildRequires:	%{py3_dist pari-jupyter}
%if %{with bundled_ipython}
BuildRequires:	%{py3_dist path.py}
%endif
BuildRequires:	%{py3_dist pathspec}
%if %{without bundled_pexpect}
BuildRequires:	%{py3_dist pexpect}
%endif
%if %{with bundled_ipython}
BuildRequires:	%{py3_dist pickleshare}
%endif
BuildRequires:	%{py3_dist pip}
BuildRequires:	%{py3_dist pkgconfig}
BuildRequires:	%{py3_dist platformdirs}
BuildRequires:	%{py3_dist pluggy}
BuildRequires:	%{py3_dist ply}
BuildRequires:	%{py3_dist poetry-core}
BuildRequires:	%{py3_dist primecountpy}
BuildRequires:	%{py3_dist ptyprocess}
BuildRequires:	%{py3_dist pure-eval}
BuildRequires:	%{py3_dist py}
BuildRequires:	%{py3_dist pycryptosat}
BuildRequires:	%{py3_dist pyopenssl}
BuildRequires:	%{py3_dist pyproject-metadata}
BuildRequires:	%{py3_dist pytest}
BuildRequires:	%{py3_dist pytest-xdist}
BuildRequires:	%{py3_dist pytz}
BuildRequires:	%{py3_dist pytzdata}
BuildRequires:	%{py3_dist pytz-deprecation-shim}
%if %{with bundled_ipython}
BuildRequires:	%{py3_dist pyzmq}
%endif
BuildRequires:	%{py3_dist rpy2}
BuildRequires:	%{py3_dist scipy}
BuildRequires:	%{py3_dist scons}
BuildRequires:	%{py3_dist setuptools}
BuildRequires:	%{py3_dist setuptools_scm}
BuildRequires:	%{py3_dist setuptools_scm_git_archive}
%if %{with bundled_ipython}
BuildRequires:	%{py3_dist simplegeneric}
%endif
BuildRequires:	%{py3_dist six}
BuildRequires:	%{py3_dist soupsieve}
BuildRequires:	%{py3_dist sphinx}
BuildRequires:	%{py3_dist sphinx-basic-ng}
BuildRequires:	%{py3_dist stack-data}
BuildRequires:	%{py3_dist sympy}
BuildRequires:	%{py3_dist tinycss2}
BuildRequires:	%{py3_dist tomlkit}
BuildRequires:	%{py3_dist tox}
BuildRequires:	%{py3_dist typing-extensions}
BuildRequires:	%{py3_dist urllib3}
BuildRequires:	%{py3_dist wheel}
BuildRequires:	%{py3_dist widgetsnbextension}
BuildRequires:	%{py3_dist zodb3}
BuildRequires:	qepcad-B
BuildRequires:	qhull
BuildRequires:	qhull-devel
BuildRequires:	R
BuildRequires:	R-devel
BuildRequires:	rubiks
BuildRequires:	rw-devel
BuildRequires:	saclib-devel
BuildRequires:	sharedmeataxe-devel
BuildRequires:	sirocco-devel
BuildRequires:	suitesparse-devel
BuildRequires:	surf-geometry
BuildRequires:	symmetrica-devel
BuildRequires:	sympow
BuildRequires:	tachyon
BuildRequires:	texlive
BuildRequires:	tex(anyfontsize.sty)
BuildRequires:	tex(fncychap.sty)
BuildRequires:	tex(makecmds.sty)
BuildRequires:	tex(subfigure.sty)
BuildRequires:	tex(tgtermes.sty)
BuildRequires:	tex(tikz-qtree.sty)
BuildRequires:	tex(tkz-berge.sty)
BuildRequires:	tex(xy.sty)
# For _jsdir macro
BuildRequires:	web-assets-devel
BuildRequires:	xorg-x11-fonts-Type1
BuildRequires:	xorg-x11-server-Xvfb
BuildRequires:	yarnpkg

Requires:	hicolor-icon-theme
Requires:	rubiks
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}
%if %{with docs}
Requires:	%{name}-doc = %{version}-%{release}
%endif
Requires:	%{name}-jupyter = %{version}-%{release}
Requires:	%{name}-sagetex = %{version}-%{release}

%if %{with bundled_threejs}
Provides:	bundled(threejs) = %{threejs_ver}
%endif

%description
Sage is a free open-source mathematics software system licensed
under the GPL. It combines the power of many existing open-source
packages into a common Python-based interface.

#------------------------------------------------------------------------
%package	core
License:	GPL-3.0-only AND GPL-2.0-or-later AND GPL-1.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND MIT AND BSD-3-Clause AND BSD-2-Clause AND EPL-1.0 AND PSF-2.0
Summary:	Open Source Mathematics Software
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	4ti2
Requires:	cddlib-tools
Requires:	flintqs
Requires:	gap
Requires:	gap-pkg-aclib
Requires:	gap-pkg-alnuth
Requires:	gap-pkg-atlasrep
Requires:	gap-pkg-autodoc
Requires:	gap-pkg-autpgrp
Requires:	gap-pkg-cohomolo
Requires:	gap-pkg-corelg
Requires:	gap-pkg-crime
Requires:	gap-pkg-crisp
Requires:	gap-pkg-cryst
Requires:	gap-pkg-crystcat
Requires:	gap-pkg-ctbllib
Requires:	gap-pkg-design
Requires:	gap-pkg-edim
Requires:	gap-pkg-factint
Requires:	gap-pkg-fga
Requires:	gap-pkg-gbnp
Requires:	gap-pkg-genss
Requires:	gap-pkg-guava
Requires:	gap-pkg-hap
Requires:	gap-pkg-hapcryst
Requires:	gap-pkg-hecke
Requires:	gap-pkg-images
Requires:	gap-pkg-irredsol
Requires:	gap-pkg-jupyterkernel
Requires:	gap-pkg-laguna
Requires:	gap-pkg-liealgdb
Requires:	gap-pkg-liepring
Requires:	gap-pkg-liering
Requires:	gap-pkg-loops
Requires:	gap-pkg-lpres
Requires:	gap-pkg-mapclass
Requires:	gap-pkg-polenta
Requires:	gap-pkg-polycyclic
Requires:	gap-pkg-polymaking
Requires:	gap-pkg-qpa
Requires:	gap-pkg-quagroup
Requires:	gap-pkg-radiroot
Requires:	gap-pkg-repsn
Requires:	gap-pkg-resclasses
Requires:	gap-pkg-singular
Requires:	gap-pkg-sla
Requires:	gap-pkg-sonata
Requires:	gap-pkg-sophus
Requires:	gap-pkg-tomlib
Requires:	gap-pkg-toric
Requires:	gap-pkg-utils
Requires:	gfan
Requires:	gmp-ecm
Requires:	gp2c
Requires:	jmol
Requires:	jsmol
Requires:	jsmath-fonts
Requires:	latte-integrale
Requires:	libgap
Requires:	lrslib-utils
Requires:	mathjax
Requires:	maxima-runtime-ecl
Requires:	nauty
Requires:	palp
Requires:	pari-elldata
Requires:	pari-galdata
Requires:	pari-galpol
Requires:	pari-gp
Requires:	pari-nftables
Requires:	pari-seadata
Requires:	python3-tdlib
Requires:	%{py3_dist asttokens}
%if %{with bundled_ipython}
Requires:	%{py3_dist backcall}
%endif
Requires:	%{py3_dist beautifulsoup4}
Requires:	%{py3_dist beniget}
Requires:	%{py3_dist brial}
Requires:	%{py3_dist charset-normalizer}
Requires:	%{py3_dist contourpy}
Requires:	%{py3_dist cppy}
Requires:	%{py3_dist cypari2}
Requires:	%{py3_dist cysignals}
Requires:	%{py3_dist cvxopt}
Requires:	%{py3_dist cython}
Requires:	%{py3_dist docutils}
Requires:	%{py3_dist executing}
Requires:	%{py3_dist flit-core}
Requires:	%{py3_dist fpylll}
Requires:	%{py3_dist gast}
Requires:	%{py3_dist gmpy2}
%if %{with sphinx_hack}
Requires:	%{py3_dist html5lib}
Requires:	%{py3_dist imagesize}
%endif
Requires:	%{py3_dist idna}
Requires:	%{py3_dist importlib-metadata}
Requires:	%{py3_dist ipykernel}
%if %{without bundled_ipython}
Requires:	%{py3_dist ipython}
%endif
Requires:	%{py3_dist ipywidgets}
%if %{with bundled_ipython}
Requires:	%{py3_dist jedi}
%endif
Requires:	%{py3_dist lrcalc}
Requires:	%{py3_dist matplotlib}
Requires:	%{py3_dist nbclient}
Requires:	%{py3_dist nbconvert}
Requires:	%{py3_dist nbformat}
Requires:	%{py3_dist nest-asyncio}
Requires:	%{py3_dist networkx}
%if %{with bundled_ipython}
Requires:	%{py3_dist path.py}
%endif
%if %{without bundled_pexpect}
Requires:	%{py3_dist pexpect}
%endif
%if %{with bundled_ipython}
Requires:	%{py3_dist pickleshare}
%endif
Requires:	%{py3_dist pplpy}
Requires:	%{py3_dist primecountpy}
Requires:	%{py3_dist ptyprocess}
Requires:	%{py3_dist pure-eval}
Requires:	%{py3_dist pycryptosat}
Requires:	%{py3_dist pytz}
Requires:	%{py3_dist pytzdata}
Requires:	%{py3_dist pytz-deprecation-shim}
%if %{with bundled_ipython}
Requires:	%{py3_dist pyzmq}
%endif
Requires:	%{py3_dist rpy2}
Requires:	%{py3_dist scipy}
%if %{with bundled_ipython}
Requires:	%{py3_dist simplegeneric}
%endif
Requires:	%{py3_dist six}
Requires:	%{py3_dist sphinx}
Requires:	%{py3_dist stack-data}
Requires:	%{py3_dist sympy}
Requires:	%{py3_dist tinycss2}
Requires:	%{py3_dist tomlkit}
Requires:	%{py3_dist urllib3}
Requires:	%{py3_dist zodb3}
Requires:	qepcad-B
Requires:	Singular
Requires:	sympow
Requires:	tachyon
Requires:	texlive
%if %{with bundled_ipython}
Provides:	bundled(ipython) = %{ipython_ver}
Provides:	bundled(prompt_toolkit) = %{prompt_toolkit_ver}
%endif
%if %{with bundled_jupyter_jsmol}
Provides:	bundled(jupyter-jsmol) = %{jupyter_jsmol_ver}
%endif
%if %{with bundled_memory_allocator}
Provides:	bundled(memory-allocator) = %{memory_allocator_ver}
%endif

# This can be removed when Fedora 40 reaches EOL
Obsoletes:      pynac < 0.7.29-3
Obsoletes:      pynac-devel < 0.7.29-3

%description	core
This package contains the core sagemath python modules.

#------------------------------------------------------------------------
%package	data
Summary:	Databases and scripts for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-data-combinatorial_designs = %{version}-%{release}
Requires:	%{name}-data-conway_polynomials = %{version}-%{release}
Requires:	%{name}-data-elliptic_curves = %{version}-%{release}
Requires:	%{name}-data-etc = %{version}-%{release}
Requires:	%{name}-data-graphs = %{version}-%{release}
Requires:	%{name}-data-polytopes_db = %{version}-%{release}
BuildArch:	noarch

%description	data
Collection of databases and interface customization scripts for sagemath.

#------------------------------------------------------------------------
%package	data-combinatorial_designs
License:	LicenseRef-Fedora-Public-Domain
Summary:	Table of MOLS from the Handbook of Combinatorial Designs
Requires:	%{name}-data = %{version}-%{release}
BuildArch:	noarch

%description	data-combinatorial_designs
The table of MOLS (10000 integers) from the Handbook of Combinatorial
Designs, 2nd edition.

#------------------------------------------------------------------------
%package	data-conway_polynomials
License:	GPL-2.0-or-later
Summary:	Conway Polynomials Database
Requires:	%{name}-data = %{version}-%{release}
BuildArch:	noarch

%description	data-conway_polynomials
Small database of Conway polynomials for sagemath.

#------------------------------------------------------------------------
%package	data-elliptic_curves
License:	Artistic-2.0
Summary:	Databases of elliptic curves
Requires:	%{name}-data = %{version}-%{release}
BuildArch:	noarch

%description	data-elliptic_curves
Includes two databases:

 * A small subset of the data in John Cremona's database of elliptic curves up
   to conductor 10000. See http://johncremona.github.io/ecdata/.

 * William Stein's database of interesting curves

#------------------------------------------------------------------------
%package	data-elliptic_curves_large
License:	Artistic-2.0
Summary:	Large database of elliptic curves
Requires:	%{name}-data = %{version}-%{release}
BuildArch:	noarch

%description	data-elliptic_curves_large
John Cremona's full database of elliptic curves, and also data related to
the BSD conjecture and modular degrees for all of these curves, and
generators for the Mordell-Weil groups.  See
http://johncremona.github.io/ecdata/.

#------------------------------------------------------------------------
%package	data-etc
License:	GPL-2.0-or-later
Summary:	Extcode for Sagemath
Requires:	%{name}-data = %{version}-%{release}
BuildArch:	noarch

%description	data-etc
Collection of scripts and interfaces to sagemath.

#------------------------------------------------------------------------
%package	data-graphs
License:	LicenseRef-Fedora-Public-Domain
Summary:	Sagemath database of graphs
Requires:	%{name}-data = %{version}-%{release}
BuildArch:	noarch

%description	data-graphs
A database of graphs. Created by Emily Kirkman based on the work of Jason
Grout. Since April 2012 it also contains the ISGCI graph database.

#------------------------------------------------------------------------
%package	data-polytopes_db
License:	GPL-3.0-or-later
Summary:	Lists of 2- and 3-dimensional reflexive polytopes
Requires:	%{name}-data = %{version}-%{release}
BuildArch:	noarch

%description	data-polytopes_db
The list of polygons is quite easy to get and it has been known for a while.
The list of 3-polytopes was originally obtained by Maximilian Kreuzer and
Harald Skarke using their software PALP, which is included into the standard
distribution of Sage. To work with lattice and reflexive polytopes from Sage
you can use sage.geometry.lattice_polytope module, which relies on PALP for
some of its functionality. To get access to the databases of this package, use
ReflexivePolytope and ReflexivePolytopes commands.

%if %{with docs}
#------------------------------------------------------------------------
%package	doc
License:	CC-BY-SA-3.0
Summary:	Documentation infrastructure files for %{name}
Requires:	mathjax

%description	doc
This package contains the documentation infrastructure for %{name}.

#------------------------------------------------------------------------
%package	doc-ca
License:	CC-BY-SA-3.0
Summary:	Catalan documentation files for %{name}
Requires:	%{name}-doc = %{version}-%{release}

%description	doc-ca
This package contains the Catalan %{name} documentation.

#------------------------------------------------------------------------
%package	doc-de
License:	CC-BY-SA-3.0
Summary:	German documentation files for %{name}
Requires:	%{name}-doc = %{version}-%{release}

%description	doc-de
This package contains the German %{name} documentation.

#------------------------------------------------------------------------
%package	doc-en
License:	CC-BY-SA-3.0
Summary:	English documentation files for %{name}
Requires:	%{name}-doc = %{version}-%{release}

%description	doc-en
This package contains the English %{name} documentation.

#------------------------------------------------------------------------
%package	doc-fr
License:	CC-BY-SA-3.0
Summary:	French documentation files for %{name}
Requires:	%{name}-doc = %{version}-%{release}

%description	doc-fr
This package contains the French %{name} documentation.

#------------------------------------------------------------------------
%package	doc-hu
License:	CC-BY-SA-3.0
Summary:	Hungarian documentation files for %{name}
Requires:	%{name}-doc = %{version}-%{release}

%description	doc-hu
This package contains the Hungarian %{name} documentation.

#------------------------------------------------------------------------
%package	doc-it
License:	CC-BY-SA-3.0
Summary:	Italian documentation files for %{name}
Requires:	%{name}-doc = %{version}-%{release}

%description	doc-it
This package contains the Italian %{name} documentation.

#------------------------------------------------------------------------
%package	doc-pt
License:	CC-BY-SA-3.0
Summary:	Portuguese documentation files for %{name}
Requires:	%{name}-doc = %{version}-%{release}

%description	doc-pt
This package contains the Portuguese %{name} documentation.

#------------------------------------------------------------------------
%package	doc-ru
License:	CC-BY-SA-3.0
Summary:	Russian documentation files for %{name}
Requires:	%{name}-doc = %{version}-%{release}

%description	doc-ru
This package contains the Russian %{name} documentation.

#------------------------------------------------------------------------
%package	doc-tr
License:	CC-BY-SA-3.0
Summary:	Turkish documentation files for %{name}
Requires:	%{name}-doc = %{version}-%{release}

%description	doc-tr
This package contains the Turkish %{name} documentation.
# with docs
%endif

#------------------------------------------------------------------------
%package	jupyter
License:	GPL-2.0-or-later AND MIT
Summary:	Jupyter integration for sagemath
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python-jupyter-filesystem
Requires:	%{py3_dist argon2-cffi}
Requires:	%{py3_dist deprecation}
Requires:	%{py3_dist editables}
Requires:	%{py3_dist hatchling}
Requires:	%{py3_dist jupyter-sphinx}
Requires:	%{py3_dist jupyterlab-pygments}
Requires:	%{py3_dist matplotlib-inline}
Requires:	%{py3_dist pari-jupyter}
Requires:	%{py3_dist widgetsnbextension}

%description	jupyter
This package contains a Jupyter integration for sagemath, replacing the
defunct notebook functionality.

#------------------------------------------------------------------------
%package	sagetex
License:	GPL-2.0-or-later
Summary:	Sagemath into LaTeX documents
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{py3_dist pillow}
Requires:	tex(color.sty)
Requires:	tex(fancyvrb.sty)
Requires:	tex(graphicx.sty)
Requires:	tex(hyperref.sty)
Requires:	tex(ifpdf.sty)
Requires:	tex(ifthen.sty)
Requires:	tex(ifxetex.sty)
Requires:	tex(listings.sty)
Requires:	tex(makecmds.sty)
Requires:	tex(tikz.sty)
Requires:	tex(verbatim.sty)
Requires:	tex(xspace.sty)

%description	sagetex
This is the SageTeX package. It allows you to embed code, results of
computations, and plots from the Sage mathematics software suite
(http://sagemath.org) into LaTeX documents.

########################################################################
%prep
%setup -q -n sage-%{version}
%setup -q -n sage-%{version} -T -D -a 1

pushd build/pkgs/combinatorial_designs
    tar jxf ../../../upstream/%{combinatorial_designs_pkg}.tar.bz2
    mv %{combinatorial_designs_pkg} src
popd

pushd build/pkgs/conway_polynomials
    tar jxf ../../../upstream/%{conway_polynomials_pkg}.tar.bz2
    mv %{conway_polynomials_pkg} src
popd

pushd build/pkgs/elliptic_curves
    tar jxf ../../../upstream/%{elliptic_curves_pkg}.tar.bz2
    mv %{elliptic_curves_pkg} src
popd

pushd build/pkgs/graphs
    tar jxf ../../../upstream/%{graphs_pkg}.tar.bz2
    mv %{graphs_pkg} src
popd

%if %{with bundled_ipython}
pushd build/pkgs/ipython
    tar zxf ../../../upstream/%{ipython_pkg}.tar.gz
    mv %{ipython_pkg} src
popd

pushd build/pkgs/prompt_toolkit
    tar zxf ../../../upstream/%{prompt_tookit_pkg}.tar.gz
    mv %{prompt_tookit_pkg} src
popd
%endif

%if %{with bundled_jupyter_jsmol}
pushd build/pkgs/jupyter_jsmol
    tar zxf ../../../upstream/%{jupyter_jsmol_pkg}.tar.gz
    mv %{jupyter_jsmol_pkg} src
popd
%endif

%if %{with bundled_memory_allocator}
pushd build/pkgs/memory_allocator
    tar zxf ../../../upstream/%{memory_allocator_pkg}.tar.gz
    mv %{memory_allocator_pkg} src
popd
%endif

%if %{with bundled_pexpect}
pushd build/pkgs/pexpect
    tar zxf ../../../upstream/%{pexpect_pkg}.tar.gz
    mv %{pexpect_pkg} src
popd
%endif

pushd build/pkgs/polytopes_db
    tar jxf ../../../upstream/%{polytopes_db_pkg}.tar.bz2
    mv %{polytopes_db_pkg} src
popd

pushd build/pkgs/sagetex
    tar zxf ../../../upstream/%{sagetex_pkg}.tar.gz
    mv %{sagetex_pkg} src
    # Fix the style file install path
    texmfdir=$(cut -d/ -f3- <<< "%{_texmf}")
    sed -i "s,share/texmf,$texmfdir," src/setup.py
popd

%if %{with docs}
%if %{with sphinx_hack}
pushd build/pkgs/sphinx
    tar zxf ../../../upstream/%{Sphinx_pkg}.tar.gz
    mv %{Sphinx_pkg} src
    pushd src
	for diff in ../patches/*.patch; do
	    patch -p1 < $diff
	done
    popd
popd
%endif
%endif

%if %{with bundled_threejs}
pushd build/pkgs/threejs
    tar zxf ../../../upstream/%{threejs_pkg}.tar.gz
    mv %{threejs_pkg} src
popd
%endif

%autopatch -p0

sed -i 's|@@SAGE_LOCAL@@|%{SAGE_LOCAL}|' src/sage/env.py

sed -e 's|@@CYSIGNALS@@|%{python3_sitearch}/cysignals|' \
    -e 's|@@BUILDROOT@@|%{buildroot}|' \
    -i src/sage_setup/command/sage_build_cython.py

#------------------------------------------------------------------------
# some .c files are not (re)generated
find src/sage \( -name \*.pyx -o -name \*.pxd \) -exec touch {} \+

# fix shebangs; some paths contains spaces, so use the null byte facility
grep -FrlZ '#!%{_bindir}/env python3' | \
  xargs -0 sed -i 's,#!%{_bindir}/env python3,#!%{python3},g'
grep -FrlZ '#!%{_bindir}/env python' | \
  xargs -0 sed -i 's,#!%{_bindir}/env python,#!%{python3},g'
grep -FrlZ '#!%{_bindir}/env sage-bootstrap-python' | \
  xargs -0 sed -i 's,#!%{_bindir}/env sage-bootstrap-python,#!%{python3},g'
grep -FrlZ '#!%{_bindir}/env sage-python' | \
  xargs -0 sed -i 's,#!%{_bindir}/env sage-python,#!%{python3},g'
grep -FrlZ '#!%{_bindir}/env' | \
  xargs -0 sed -i 's,#!%{_bindir}/env ,#!%{_bindir}/,'
grep -rlZ '#!%{_bindir}/python$' | xargs -0 sed -i 's,#!%{_bindir}/python$,&3,'
sed -i 's,%{_bindir}/env python,%{python3},' \
%if %{with bundled_pexpect}
    build/pkgs/pexpect/src/examples/python.py \
%endif
    build/pkgs/sagetex/src/sagetex.ins
sed -i 's,%{_bindir}/python,&3,' src/sage/misc/dev_tools.py
sed -e 's,local/bin/python,bin/python,' \
    -e 's,#!%{_bindir}/python,&3,' \
    -i src/sage/repl/preparse.py
%if %{with bundled_ipython}
sed -e "s|'%{_bindir}/env', 'which'|'%{_bindir}/which'|" \
    -i build/pkgs/ipython/src/IPython/utils/_process_posix.py
%endif

# Remove bogus executable bits
chmod a-x src/sage/modules/fp_graded/{,steenrod/}*.py

# GAP does not have enough memory to load the entire workspace
sed -i 's/64m/256m/' src/sage/interfaces/gap.py

# Fix detection of Fedora
sed -i 's/yum/rpm/' build/bin/sage-guess-package-system

# Allow use of gcc 13
sed -i 's/1\[3-9\].*)/1[4-9].*)/' configure

# Allow use of eclib 20221012
sed -i 's/20220621/20221012/g' configure

# Do not build with -march=native
sed -i 's/CFLAGS_MARCH="-march=native"/CFLAGS_MARCH=""/' configure


########################################################################
%build
export LC_ALL=C.UTF-8
export CPPFLAGS="-I%{_includedir}/4ti2 -I%{_includedir}/arb -I%{_includedir}/cddlib"
export ECMBIN=%{_bindir}/gmp-ecm
export SAGE_ROOT=%{buildroot}%{SAGE_ROOT}
export SAGE_LOCAL=%{buildroot}%{SAGE_LOCAL}
# Avoid buildroot in gcc command line (use _builddir instead)
export SAGE_SRC="$PWD/src"
export SAGE_INC=%{_includedir}
export DESTDIR=%{buildroot}
export SAGE_DEBUG=no
# Use file in /tmp because there are issues with long pathnames
export DOT_SAGE=/tmp/sage$$
mkdir -p $DOT_SAGE/tmp

# Avoid surprises due to change to src/build/temp.*$ARCH.*/...
export SAGE_CYTHONIZED=$SAGE_SRC/build/cythonized

# match system packages as sagemath packages
mkdir -p $SAGE_ROOT $SAGE_LOCAL
ln -sf %{_libdir} $SAGE_LOCAL/lib
ln -sf %{_includedir} $SAGE_LOCAL/include
ln -sf %{_datadir} $SAGE_LOCAL/share

export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHON=%{_bindir}/python3
export PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$PYTHONPATH

# Make various programs visible to configure
module load 4ti2-%{_arch}
module load lrcalc-%{_arch}
module load surf-geometry-%{_arch}

# Initialize polymake
polymake --reconfigure - <<< exit;

#------------------------------------------------------------------------
# Run the configure script to generate files
export GSL_LIBS="-lgsl -lflexiblas -lm"
%configure \
  --prefix=$SAGE_LOCAL \
  --disable-rpath \
  --disable-silent-rules \
  --enable-4ti2 \
  --enable-bliss \
  --enable-cocoalib \
  --enable-cryptominisat \
  --enable-csdp \
  --enable-database_cremona_ellcurve \
  --enable-frobby \
  --enable-mcqd \
  --enable-meataxe \
  --enable-qepcad \
  --enable-saclib \
  --enable-sirocco \
  --enable-surf \
  --enable-tdlib

#------------------------------------------------------------------------
# Link with flexiblas instead of gslcblas
grep -FrlZ gslcblas | xargs -0 sed -i 's/gslcblas/flexiblas/g'

#------------------------------------------------------------------------
# Save and update environment to generate bundled interfaces
save_PATH=$PATH
save_LOCAL=$SAGE_LOCAL
export PATH=%{_builddir}/bin:$PATH
export SAGE_LOCAL=%{_builddir}

%if %{with bundled_ipython}
pushd build/pkgs/ipython/src
    %{python3} setup.py build
    %{python3} setup.py install --root %{_builddir}
popd

pushd build/pkgs/prompt_toolkit/src
    %{python3} setup.py build
    %{python3} setup.py install --root %{_builddir}
popd
%endif

%if %{with bundled_jupyter_jsmol}
pushd build/pkgs/jupyter_jsmol/src
    %{python3} setup.py build
    %{python3} setup.py install --root %{_builddir}
popd
%endif

%if %{with bundled_memory_allocator}
pushd build/pkgs/memory_allocator/src
    %{python3} setup.py build
    %{python3} setup.py install --root %{_builddir}
popd
%endif

%if %{with cython_hack}
    cp -far %{python3_sitearch}/Cython %{_builddir}%{python3_sitearch}
    BASE=$PWD/build/pkgs/cython/patches/
    pushd %{_builddir}%{python3_sitearch}
	for PATCH in pxi_sys_path.patch
	do
	    patch -p1 < $BASE/$PATCH
	done
    popd
%endif

# Restore environment used to generate bundled interfaces
export PATH=$save_PATH
export SAGE_LOCAL=$save_LOCAL
export PYTHONPATH=$PYTHONPATH:%{_builddir}%{python3_sitelib}:%{_builddir}%{python3_sitearch}
mkdir -p %{buildroot}%{SAGE_SPKG_INST}
mkdir -p %{buildroot}%{_libdir}/sagemath/build/pkgs

pushd src
    %{python3} -u ./setup.py build
    tar cf - $(find sage -type f \! \( -name \*.c -o -name \*.cc -o -name \*.cpp -o -name .gitignore -o -name \*.hpp \) ) | (cd build/lib.*; tar xf -)
    tar cf - $(find sage_setup -name \*.py) | (cd build/lib.*; tar xf -)
popd

#------------------------------------------------------------------------
pushd build/pkgs/sagetex/src
    %{python3} ./setup.py build
popd

# last build command
rm -fr $DOT_SAGE

########################################################################
%install
export LC_ALL=C.UTF-8
export CC=%{__cc}
export SAGE_ROOT=%{buildroot}%{SAGE_ROOT}
export SAGE_LOCAL=%{buildroot}%{SAGE_LOCAL}
# Avoid buildroot in gcc command line (use _builddir instead)
export SAGE_SRC="$PWD/src"
export SAGE_INC=%{_includedir}
#export SAGE_SRC=#%#{buildroot}#%#{SAGE_SRC}
export SAGE_SHARE=%{buildroot}%{SAGE_SHARE}
export SAGE_ETC=%{buildroot}%{SAGE_ETC}
export SAGE_EXTCODE=%{buildroot}%{SAGE_ETC}
export SAGE_DOC=%{buildroot}%{SAGE_DOC}
export SAGE_PYTHONPATH=%{buildroot}%{SAGE_PYTHONPATH}
export DESTDIR=%{buildroot}
export SAGE_DEBUG=no
export DOT_SAGE=/tmp/sage$$
mkdir -p $DOT_SAGE/tmp

export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHON=%{_bindir}/python3
export PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$PYTHONPATH
export PYTHONPATH=%{_builddir}%{python3_sitearch}:%{_builddir}%{python3_sitelib}:$PYTHONPATH

#------------------------------------------------------------------------
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p $SAGE_PYTHONPATH
rm -fr $SAGE_LOCAL/{include,lib,share,notebook}
mkdir -p $SAGE_SHARE $SAGE_DOC $SAGE_LOCAL/bin %{buildroot}%{SAGE_SRC}
ln -sf $PWD/src/sage %{buildroot}%{SAGE_SRC}/sage
ln -sf %{_libdir} $SAGE_LOCAL/lib
ln -sf %{_includedir} $SAGE_LOCAL/include
ln -sf %{_datadir} $SAGE_LOCAL/share

#------------------------------------------------------------------------
cp -a src/sage/ext_data $SAGE_ETC
cp -p %{SOURCE2} $SAGE_ETC

#------------------------------------------------------------------------
pushd src
%if %{without install_hack}
    %py3_install
%else
    mkdir -p %{buildroot}%{python3_sitearch}
    cp -far build/lib.linux-*/sage %{buildroot}%{python3_sitearch}
%endif
%if %{with docs}
    # install documentation sources
    rm -fr $SAGE_DOC/{common,en,fr}
    cp -far doc/{common,ca,de,en,fr,hu,it,pt,ru,tr} $SAGE_DOC
%endif
popd

#------------------------------------------------------------------------
%if %{with bundled_pexpect}
pushd build/pkgs/pexpect/src
    cp -fa pexpect $SAGE_PYTHONPATH
popd
%endif

#------------------------------------------------------------------------
cp -fa COPYING.txt $SAGE_ROOT
pushd src/bin
    mkdir -p $SAGE_LOCAL/bin
    cp -fa sage-* $SAGE_LOCAL/bin
    pushd $SAGE_LOCAL/bin
	ln -sf %{_bindir}/jmol jmol
	ln -sf %{_bindir}/python3 sage.bin
	ln -sf %{_bindir}/python3 python
	ln -sf %{_bindir}/gp sage_pari
	ln -sf %{_bindir}/gap gap
	ln -sf %{_bindir}/gmp-ecm ecm
	rm -f sage-env-config.in
    popd
popd
install -p -m755 src/bin/sage $SAGE_LOCAL/bin

#------------------------------------------------------------------------
pushd $SAGE_LOCAL/bin/
    rm -f \
	sage-arch-env \
	sage-bdist \
	sage-build \
	sage-clone \
	sage-clone-source \
	sage-combinat \
	sage-crap \
	sage-dev \
	sage-download-file \
	sage-download-upstream \
	sage-env \
	sage-fix-pkg-checksums \
	sage-list-experimental \
	sage-list-optional \
	sage-list-packages \
	sage-list-standard \
	sage-location \
	sage-omega \
	sage-open \
	sage-pkg \
	sage-pull \
	sage-push \
	sage-pypkg-location \
	sage-README-osx.txt \
	sage-rebaseall.bat \
	sage-rebaseall.sh \
	sage-rebase.bat \
	sage-rebase.sh \
	sage-rebase \
	sage-rsyncdist \
	sage-sdist \
	sage-spkg \
	sage-starts \
	sage-sync-build.py \
	sage-test-import \
	sage-update-src \
	sage-update-version \
	sage-upgrade \
	spkg-install
popd

#------------------------------------------------------------------------
(
    source build/bin/sage-dist-helpers

#------------------------------------------------------------------------
pushd build/pkgs/combinatorial_designs
    mkdir -p $SAGE_SHARE/combinatorial_designs
    cp -fa src/* $SAGE_SHARE/combinatorial_designs
popd

#------------------------------------------------------------------------
pushd build/pkgs/conway_polynomials
    %{python3} ./spkg-install.py
popd

#------------------------------------------------------------------------
pushd build/pkgs/elliptic_curves
    # --short-circuit -bi debug build helper
    if [ ! -e src/ellcurves ]; then
	rm -fr src
	tar jxf ../../../upstream/%{elliptic_curves_pkg}.tar.bz2
	mv %{elliptic_curves_pkg} src
    fi
    %{python3} ./spkg-install.py
popd

#------------------------------------------------------------------------
pushd build/pkgs/graphs
    mkdir -p $SAGE_SHARE/graphs
    cp -fa src/* $SAGE_SHARE/graphs
popd

#------------------------------------------------------------------------
pushd build/pkgs/polytopes_db
    mkdir -p $SAGE_SHARE/reflexive_polytopes
    cp -fa src/* $SAGE_SHARE/reflexive_polytopes
popd

#------------------------------------------------------------------------
pushd build/pkgs/sagetex/src
    %py3_install "--install-purelib=%{python3_sitearch}"
    mv %{buildroot}%{_texmf}/tex/latex/sagetex/CONTRIBUTORS \
	 %{buildroot}%{_docdir}/sagetex
    for file in PKG-INFO; do
	install -p -m 0644 $file %{buildroot}%{_docdir}/sagetex/$file
    done
popd

#------------------------------------------------------------------------
%if %{with bundled_ipython}
mv %{_builddir}%{python3_sitelib}/IPython %{buildroot}%{SAGE_PYTHONPATH}
mv %{_builddir}%{python3_sitelib}/prompt_toolkit* %{buildroot}%{SAGE_PYTHONPATH}
mv %{_builddir}%{_bindir}/ip* %{buildroot}%{SAGE_LOCAL}/bin
%endif

#------------------------------------------------------------------------
%if %{with bundled_jupyter_jsmol}
mv %{_builddir}%{python3_sitelib}/jupyter_jsmol* %{buildroot}%{SAGE_PYTHONPATH}
%endif

#------------------------------------------------------------------------
%if %{with bundled_memory_allocator}
mv %{_builddir}%{python3_sitearch}/memory_allocator* %{buildroot}%{SAGE_PYTHONPATH}
%endif

#------------------------------------------------------------------------
%if %{with bundled_threejs}
pushd build/pkgs/threejs
    mkdir -p $SAGE_SHARE/threejs-sage
    cp -a src/build $SAGE_SHARE/threejs-sage/%{threejs_ver}
popd
%endif

#------------------------------------------------------------------------
) # source build/bin/sage-dist-helpers

#------------------------------------------------------------------------
singver=$(sed 's/^.*-\([.[:digit:]]*\).*$/\1/' <<< %{singular_pkg})
cat > %{buildroot}%{SAGE_LOCAL}/bin/sage-env << EOF
export CUR=\$PWD
##export DOT_SAGE="\$HOME/.sage"
mkdir -p \$DOT_SAGE/{maxima,sympow,tmp}
export SAGE_TESTDIR=\$DOT_SAGE/tmp
export SAGE_ROOT="$SAGE_ROOT"
export SAGE_LOCAL="$SAGE_LOCAL"
export SAGE_SHARE="$SAGE_SHARE"
export SAGE_EXTCODE="$SAGE_ETC"
export SAGE_ETC="$SAGE_ETC"
export SAGE_SRC="%{buildroot}%{SAGE_SRC}"
##export SAGE_DOC="$SAGE_DOC"
##export SAGE_DOC_SRC="\$SAGE_DOC"
##export SAGE_PKGS="\$SAGE_LOCAL/var/lib/sage/installed"
module load 4ti2-%{_arch}
module load lrcalc-%{_arch}
module load surf-geometry-%{_arch}
export PATH=$SAGE_LOCAL/bin:\$PATH
export SINGULAR_DATA_DIR=%{_datadir}
export SINGULAR_BIN_DIR=%{_libdir}/Singular
export LIBSINGULAR_PATH=%{_libdir}/libSingular-$singver.so
##export PYTHONPATH="$SAGE_PYTHONPATH:\$SAGE_LOCAL/bin"
export SYMPOW_DIR="\$DOT_SAGE/sympow"
# Required for sage -gdb
: \${SAGE_DEBUG:=no}
export SAGE_DEBUG
EOF
cat > %{buildroot}%{_bindir}/sage << EOF
#!/bin/bash

source $SAGE_LOCAL/bin/sage-env
exec $SAGE_LOCAL/bin/sage "\$@"
EOF
#------------------------------------------------------------------------
chmod +x %{buildroot}%{_bindir}/sage

#------------------------------------------------------------------------
# adjust cython interface:
# o install csage headers
# o install .pxi and .pxd files
pushd src
    for f in `find sage \( -name \*.pxi -o -name \*.pxd -o -name \*.pyx \)`; do
	install -p -D -m 0644 $f %{buildroot}%{python3_sitearch}/$f
    done
    # need this or will not "find" the files in the directory, and
    # fail to link with gmp
    touch %{buildroot}%{python3_sitearch}/sage/libs/gmp/__init__.py
popd

%if %{with docs}
#------------------------------------------------------------------------
%if %{with bundled_pexpect}
cp -fa $SAGE_PYTHONPATH/pexpect %{buildroot}%{python3_sitearch}
%endif

# Build documentation, using %#{buildroot} environment
export SAGE_SETUP=$PWD/src/sage_setup
pushd src/doc
    export SAGE_DOC=$PWD
    export PATH=%{buildroot}%{_bindir}:$SAGE_LOCAL/bin:$PATH
    export SINGULARPATH=%{_datadir}/singular/LIB
    export SINGULAR_BIN_DIR=%{_libdir}/Singular
    export PYTHONPATH=$SAGE_SETUP:%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$SAGE_PYTHONPATH:$SAGE_SRC

%if %{with sphinx_hack}
    pushd ../../build/pkgs/sphinx/src
	%py3_build
	%py3_install "--install-purelib=%{python3_sitearch}"
	rm -f %{buildroot}%{_bindir}/sphinx*
    popd
%endif

    # there we go
    ln -sf %{buildroot}%{SAGE_DOC} %{buildroot}%{SAGE_SRC}/doc
    export SAGE_DOC=%{buildroot}%{SAGE_DOC}
    export SAGE_DOC_SRC=$SAGE_DOC
    export JUPYTER_PATH=%{buildroot}%{_datadir}/jupyter
    # Build with an X server running, required by some doc builders
    SAGE_NUM_THREADS=2 \
	xvfb-run -d %{python3} -m sage_docbuild --no-pdf-links -k all html -j
    rm -f %{buildroot}%{SAGE_SRC}/doc
    ln -sf %{SAGE_DOC} %{buildroot}%{SAGE_SRC}/doc

    # should not be required and encodes buildroot
    rm -fr $SAGE_DOC/output/doctrees
popd

%if %{with check}
export SAGE_TIMEOUT=%{SAGE_TIMEOUT}
export SAGE_TIMEOUT_LONG=%{SAGE_TIMEOUT_LONG}
sage -testall --verbose || :
install -p -m644 $DOT_SAGE/tmp/test.log $SAGE_DOC/test.log
# remove buildroot references from test.log
sed -i 's|%{buildroot}||g' $SAGE_DOC/test.log
%endif

%if %{with bundled_pexpect}
    rm -f %{buildroot}%{python3_sitearch}/pexpect
%endif

%if %{with sphinx_hack}
    rm -fr %{buildroot}%{python3_sitearch}/sphinx \
	%{buildroot}%{python3_sitearch}/Sphinx*
%endif

# More wrong buildroot references
perl -pi -e 's|%{buildroot}||g;' \
	 -e "s|$PWD/src/doc|%{SAGE_DOC}|g;" \
    %{buildroot}%{SAGE_DOC}/html/en/reference/combinat/sage/combinat/posets/poset_examples.html \
    %{buildroot}%{SAGE_DOC}/html/en/reference/graphs/sage/graphs/graph_generators.html
# with docs
%endif

# Even more wrong buildroot references
for shared in $(find %{buildroot}%{python3_sitearch} -name \*.so); do
  if chrpath -l $shared | grep -Fq BUILDROOT; then
    chrpath -r %{SAGE_LOCAL}/lib $shared
  fi
done

#------------------------------------------------------------------------
# Fix links
export SAGE_SRC=%{buildroot}%{SAGE_SRC}
rm -fr $SAGE_SRC/sage $SAGE_ETC/sage $SAGE_ROOT/doc $SAGE_SRC/doc
rm -fr $SAGE_ROOT/share $SAGE_ROOT/devel
ln -sf %{python3_sitearch}/sage $SAGE_SRC/sage
ln -sf %{python3_sitearch} $SAGE_ETC/sage
ln -sf %{SAGE_DOC} $SAGE_ROOT/doc
%if %{with docs}
ln -sf %{SAGE_DOC} $SAGE_SRC/doc
%endif
ln -sf %{SAGE_SHARE} $SAGE_ROOT/share
# compat devel symlink
ln -sf src $SAGE_ROOT/devel

# Install menu and icons
install -p -m644 -D src/sage/ext_data/notebook-ipython/logo.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/sagemath.svg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/org.%{name}.sage.desktop << EOF
[Desktop Entry]
Name=Sagemath
Comment=A free open-source mathematics software system
Exec=sage
Icon=%{name}
Terminal=true
Type=Application
Categories=Education;Science;Math;
EOF
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.sage.desktop

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
cp -p %{SOURCE3} %{buildroot}%{_metainfodir}
appstreamcli validate --no-net \
    %{buildroot}%{_metainfodir}/org.%{name}.sage.metainfo.xml

# Fix permissions
find %{buildroot} -name '*.so' -exec chmod 755 {} \+
chmod 755 %{buildroot}%{python3_sitearch}/sage/ext_data/pari/dokchitser/testall
for file in `find %{buildroot} -name \*.py`; do
    if head -1 $file | grep -q '^#!'; then
	chmod +x $file
    fi
done

%if %{with docs}
chmod -x %{buildroot}%{SAGE_DOC}/en/prep/media/Rplot001.png

# Documentation is not rebuilt (also corrects rpmlint warning of hidden file)
find %{buildroot}%{SAGE_DOC} -name .buildinfo -delete
rm -fr %{buildroot}%{SAGE_DOC}/output/inventory
find %{buildroot}%{SAGE_DOC} -type d -name _sources -exec rm -fr {} \+
%endif

# remove build directory in buildroot
[ -d %{buildroot}%{SAGE_SRC}/build ] &&
    rm -r %{buildroot}%{SAGE_SRC}/build

%if %{without install_hack}
# remove sage_setup
rm -r %{buildroot}%{python3_sitearch}/sage_setup
%endif

# remove files we do not want to install
rm %{buildroot}%{SAGE_LOCAL}/bin/sage-src-env-config.in

# pretend sagemath spkgs are installed to reduce number of errors
# in doctests
mkdir -p %{buildroot}%{SAGE_SPKG_INST}
pushd upstream
for file in *.tar.*; do
    mkdir %{buildroot}%{SAGE_SPKG_INST}/${file%.tar.*}
done
for file in *.zip; do
    mkdir %{buildroot}%{SAGE_SPKG_INST}/${file%.zip}
done
popd
pushd %{buildroot}%{SAGE_SPKG_INST}
    for pkg in %{SAGE_REQUIRED_PKGS}; do
	mkdir $pkg
    done
popd

#------------------------------------------------------------------------
cat > %{buildroot}%{SAGE_LOCAL}/bin/sage-list-packages << EOF
#!/bin/sh
NOVERSION=false
INSTALLED=no
while [ \$# -gt 0 ]; do
    if [ x\$1 = x--no-version ]; then
	NOVERSION=true
    elif [ x\$1 = xinstalled ]; then
	INSTALLED=yes
    fi
    shift
done
if [ \$INSTALLED = no ]; then
    exit 0
fi
LIST=\$(ls -1 %{SAGE_SPKG_INST})
if [ \$NOVERSION = false ]; then
    for pkg in \$LIST; do
	echo \$pkg | sed -e 's/-/ /'
    done
else
    for pkg in \$LIST; do
	echo \$pkg | sed -e 's/-.*//'
    done
fi
EOF
chmod +x %{buildroot}%{SAGE_LOCAL}/bin/sage-list-packages
#------------------------------------------------------------------------

%if %{with docs}
    rm -fr %{buildroot}%{SAGE_DOC}/doctrees
    rm -fr %{buildroot}%{SAGE_DOC}/inventory
%endif

#------------------------------------------------------------------------
# Byte compile python files in nonstandard places
%py_byte_compile %{python3} %{buildroot}%{_texmf}/tex/latex/sagetex

#------------------------------------------------------------------------
# Do not bundle mathjax
for dir in $(find %{buildroot}%{_docdir} -name _static); do
    pushd $dir
    for d in config extensions fonts jax localization MathJax.js test; do
        if [ -d "$PWD/$d" ]; then
	    rm -fr $d
	    ln -s %{_datadir}/javascript/mathjax/$d $d
	fi
    done
    popd
done

#------------------------------------------------------------------------
# Jupyter integration
pushd src
%{python3} << EOF
from sage.repl.ipython_kernel.install import SageKernelSpec
SageKernelSpec.update(prefix='%{buildroot}%{_prefix}')
EOF
popd
# Remove buildroot from the json and symbolic links
pushd %{buildroot}%{_datadir}/jupyter
    sed -i 's,%{buildroot},,g' kernels/sagemath/kernel.json
    for link in $(find . -type l); do
	target=$(readlink $link)
	if [[ "$target" =~ "%{buildroot}" ]]; then
	   rm $link
	   ln -s ${target#%{buildroot}} $link
	fi
    done
popd

#------------------------------------------------------------------------
# Build the large Cremona database
export PATH=%{buildroot}%{SAGE_LOCAL}/bin:$PATH
export PYTHONPATH=%{buildroot}%{SAGE_PYTHONPATH}:%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}
touch %{buildroot}%{SAGE_SHARE}/cremona/cremona.db
cat > cremona.sage << EOF
import sage.env
import sage.databases.cremona
sage.env.SAGE_SHARE = '%{buildroot}%{SAGE_SHARE}'
c = sage.databases.cremona.LargeCremonaDatabase('cremona', False, True)
c._init_from_ftpdata('ecdata-%{cremona_ver}')
EOF
%{buildroot}%{SAGE_LOCAL}/bin/sage cremona.sage

#------------------------------------------------------------------------
# Scripts were used to build documentation and possibly other operations
sed -i 's|%{buildroot}||g;s|^##||g;' \
	%{buildroot}%{_bindir}/sage \
	%{buildroot}%{SAGE_LOCAL}/bin/sage-env \
	%{buildroot}%{SAGE_LOCAL}/bin/sage-env-config \
	%{buildroot}%{SAGE_LOCAL}/bin/sage-src-env-config
sed -i "s|$PWD|%{SAGE_ROOT}|g" \
	%{buildroot}%{SAGE_LOCAL}/bin/sage-env-config \
	%{buildroot}%{SAGE_LOCAL}/bin/sage-src-env-config

# last install command
rm -fr $DOT_SAGE

########################################################################
# Update sagemath's view of installed packages as RPM packages are added
# and removed.
%triggerin -- %{name}-data-elliptic_curves_large
mkdir -p %{SAGE_LOCAL}/var/lib/sage/installed/database_cremona_ellcurve-%{cremona_ver} 2>&1 || :

%triggerun -- %{name}-data-elliptic_curves_large
rm -fr %{SAGE_LOCAL}/var/lib/sage/installed/database_cremona_ellcurve-%{cremona_ver}

%if %{with docs}
%pretrans -n sagemath-doc-en -p <lua>
-- Fix directory/symlink conflicts introduced by fix for bz 1875606.
-- This can be removed when Fedora 36 reaches EOL.
paths = {
  "%{SAGE_DOC}/html/en/_static/config",
  "%{SAGE_DOC}/html/en/_static/extensions",
  "%{SAGE_DOC}/html/en/_static/fonts",
  "%{SAGE_DOC}/html/en/_static/jax",
  "%{SAGE_DOC}/html/en/_static/localization",
  "%{SAGE_DOC}/html/en/_static/test",
  "%{SAGE_DOC}/html/en/a_tour_of_sage/_static/config",
  "%{SAGE_DOC}/html/en/a_tour_of_sage/_static/extensions",
  "%{SAGE_DOC}/html/en/a_tour_of_sage/_static/fonts",
  "%{SAGE_DOC}/html/en/a_tour_of_sage/_static/jax",
  "%{SAGE_DOC}/html/en/a_tour_of_sage/_static/localization",
  "%{SAGE_DOC}/html/en/a_tour_of_sage/_static/test",
  "%{SAGE_DOC}/html/en/constructions/_static/config",
  "%{SAGE_DOC}/html/en/constructions/_static/extensions",
  "%{SAGE_DOC}/html/en/constructions/_static/fonts",
  "%{SAGE_DOC}/html/en/constructions/_static/jax",
  "%{SAGE_DOC}/html/en/constructions/_static/localization",
  "%{SAGE_DOC}/html/en/constructions/_static/test",
  "%{SAGE_DOC}/html/en/developer/_static/config",
  "%{SAGE_DOC}/html/en/developer/_static/extensions",
  "%{SAGE_DOC}/html/en/developer/_static/fonts",
  "%{SAGE_DOC}/html/en/developer/_static/jax",
  "%{SAGE_DOC}/html/en/developer/_static/localization",
  "%{SAGE_DOC}/html/en/developer/_static/test",
  "%{SAGE_DOC}/html/en/faq/_static/config",
  "%{SAGE_DOC}/html/en/faq/_static/extensions",
  "%{SAGE_DOC}/html/en/faq/_static/fonts",
  "%{SAGE_DOC}/html/en/faq/_static/jax",
  "%{SAGE_DOC}/html/en/faq/_static/localization",
  "%{SAGE_DOC}/html/en/faq/_static/test",
  "%{SAGE_DOC}/html/en/installation/_static/config",
  "%{SAGE_DOC}/html/en/installation/_static/extensions",
  "%{SAGE_DOC}/html/en/installation/_static/fonts",
  "%{SAGE_DOC}/html/en/installation/_static/jax",
  "%{SAGE_DOC}/html/en/installation/_static/localization",
  "%{SAGE_DOC}/html/en/installation/_static/test",
  "%{SAGE_DOC}/html/en/prep/_static/config",
  "%{SAGE_DOC}/html/en/prep/_static/extensions",
  "%{SAGE_DOC}/html/en/prep/_static/fonts",
  "%{SAGE_DOC}/html/en/prep/_static/jax",
  "%{SAGE_DOC}/html/en/prep/_static/localization",
  "%{SAGE_DOC}/html/en/prep/_static/test",
  "%{SAGE_DOC}/html/en/reference/_static/config",
  "%{SAGE_DOC}/html/en/reference/_static/extensions",
  "%{SAGE_DOC}/html/en/reference/_static/fonts",
  "%{SAGE_DOC}/html/en/reference/_static/jax",
  "%{SAGE_DOC}/html/en/reference/_static/localization",
  "%{SAGE_DOC}/html/en/reference/_static/test",
  "%{SAGE_DOC}/html/en/thematic_tutorials/_static/config",
  "%{SAGE_DOC}/html/en/thematic_tutorials/_static/extensions",
  "%{SAGE_DOC}/html/en/thematic_tutorials/_static/fonts",
  "%{SAGE_DOC}/html/en/thematic_tutorials/_static/jax",
  "%{SAGE_DOC}/html/en/thematic_tutorials/_static/localization",
  "%{SAGE_DOC}/html/en/thematic_tutorials/_static/test",
  "%{SAGE_DOC}/html/en/tutorial/_static/config",
  "%{SAGE_DOC}/html/en/tutorial/_static/extensions",
  "%{SAGE_DOC}/html/en/tutorial/_static/fonts",
  "%{SAGE_DOC}/html/en/tutorial/_static/jax",
  "%{SAGE_DOC}/html/en/tutorial/_static/localization",
  "%{SAGE_DOC}/html/en/tutorial/_static/test",
  "%{SAGE_DOC}/html/en/website/_static/config",
  "%{SAGE_DOC}/html/en/website/_static/extensions",
  "%{SAGE_DOC}/html/en/website/_static/fonts",
  "%{SAGE_DOC}/html/en/website/_static/jax",
  "%{SAGE_DOC}/html/en/website/_static/localization",
  "%{SAGE_DOC}/html/en/website/_static/test"
}

for _, path in ipairs(paths) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end

-- Fix directory/symlink conflicts introduced by sagemath 3.5 -> 3.6 upgrade.
-- This can be removed when Fedora 40 reaches EOL.
paths2 = {
  "%{SAGE_DOC}/html/en/reference/plot3d/_static",
  "%{SAGE_DOC}/html/en/reference/repl/_static"
}

for _, path in ipairs(paths2) do
  st = posix.stat(path)
  if st and st.type == "link" then
    os.remove(path)
  end
end
%endif


%files
# GPL-2.0-or-later
%license COPYING.txt
%doc %{SAGE_ROOT}/COPYING.txt
%dir %{SAGE_ROOT}
%dir %{SAGE_LOCAL}/
%dir %{SAGE_SHARE}/
%{SAGE_LOCAL}/bin/
%{SAGE_LOCAL}/include
%{SAGE_LOCAL}/lib
%{SAGE_LOCAL}/share
%{SAGE_LOCAL}/var/
%ghost %{SAGE_LOCAL}/var/lib/sage/installed/database_cremona_ellcurve-%{cremona_ver}
%{SAGE_ROOT}/devel
%{SAGE_ROOT}/doc
%{SAGE_ROOT}/share
%{SAGE_SRC}/
%dir %{SAGE_PYTHONPATH}
%{_bindir}/sage
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/org.%{name}.sage.desktop
%{_metainfodir}/org.%{name}.sage.metainfo.xml
%if %{with bundled_threejs}
# MIT
%{SAGE_SHARE}/threejs-sage/
%endif

#------------------------------------------------------------------------
%files		core
# GPL-2.0-or-later
%{python3_sitearch}/sage/
%if %{without install_hack}
%{python3_sitearch}/sage-*.egg-info
%endif
%if %{with bundled_ipython}
# BSD-3-Clause
%{SAGE_PYTHONPATH}/IPython
%{SAGE_PYTHONPATH}/prompt_toolkit*
%endif
%if %{with bundled_jupyter_jsmol}
# MIT AND BSD-3-Clause AND EPL-1.0
%{SAGE_PYTHONPATH}/jupyter_jsmol*
%endif
%if %{with bundled_memory_allocator}
# GPL-3.0-only AND LGPL-3.0-or-later
%{SAGE_PYTHONPATH}/memory_allocator*
%endif

#------------------------------------------------------------------------
%files		data
%dir %{SAGE_ETC}/
%{SAGE_ETC}/sage
%{SAGE_ETC}/gprc.expect

#------------------------------------------------------------------------
%files		data-combinatorial_designs
# Public Domain
%{SAGE_SHARE}/combinatorial_designs/

#------------------------------------------------------------------------
%files		data-conway_polynomials
# GPL-2.0-or-later
%{SAGE_SHARE}/conway_polynomials/

#------------------------------------------------------------------------
%files		data-elliptic_curves
# Artistic-2.0
%dir %{SAGE_SHARE}/cremona/
%{SAGE_SHARE}/cremona/cremona_mini.db
%{SAGE_SHARE}/ellcurves/

#------------------------------------------------------------------------
%files		data-elliptic_curves_large
# Artistic-2.0
%dir %{SAGE_SHARE}/cremona/
%{SAGE_SHARE}/cremona/cremona.db

#------------------------------------------------------------------------
%files		data-etc
# GPL-2.0-or-later
%{SAGE_ETC}/doctest/
%{SAGE_ETC}/gap/
%{SAGE_ETC}/kenzo/
%{SAGE_ETC}/magma/
%{SAGE_ETC}/mwrank/
%{SAGE_ETC}/nbconvert/
%{SAGE_ETC}/nodoctest
%{SAGE_ETC}/pari/
%{SAGE_ETC}/singular/
%{SAGE_ETC}/threejs/
%{SAGE_ETC}/valgrind/

#------------------------------------------------------------------------
%files		data-graphs
# Public Domain
%{SAGE_ETC}/graphs/
%{SAGE_SHARE}/graphs/

#------------------------------------------------------------------------
%files		data-polytopes_db
# GPL-3.0-or-later
%{SAGE_SHARE}/reflexive_polytopes/

%if %{with docs}
#------------------------------------------------------------------------
%files		doc
# CC-BY-SA-3.0
%license COPYING.txt
%dir %{SAGE_DOC}/
%{SAGE_DOC}/index.html
%{SAGE_DOC}/common/
%dir %{SAGE_DOC}/html/

#------------------------------------------------------------------------
%files		doc-ca
# CC-BY-SA-3.0
%{SAGE_DOC}/ca/
%{SAGE_DOC}/html/ca/

#------------------------------------------------------------------------
%files		doc-de
# CC-BY-SA-3.0
%{SAGE_DOC}/de/
%{SAGE_DOC}/html/de/

#------------------------------------------------------------------------
%files		doc-en
# CC-BY-SA-3.0
%{SAGE_DOC}/en/
%{SAGE_DOC}/html/en/

# Fix directory/symlink conflicts introduced by fix for bz 1875606.
# This can be removed when Fedora 36 reaches EOL.
%ghost %{SAGE_DOC}/html/en/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/a_tour_of_sage/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/a_tour_of_sage/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/a_tour_of_sage/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/a_tour_of_sage/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/a_tour_of_sage/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/a_tour_of_sage/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/constructions/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/constructions/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/constructions/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/constructions/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/constructions/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/constructions/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/developer/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/developer/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/developer/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/developer/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/developer/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/developer/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/faq/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/faq/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/faq/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/faq/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/faq/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/faq/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/installation/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/installation/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/installation/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/installation/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/installation/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/installation/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/prep/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/prep/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/prep/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/prep/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/prep/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/prep/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/reference/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/reference/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/reference/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/reference/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/reference/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/reference/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/thematic_tutorials/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/thematic_tutorials/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/thematic_tutorials/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/thematic_tutorials/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/thematic_tutorials/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/thematic_tutorials/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/tutorial/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/tutorial/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/tutorial/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/tutorial/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/tutorial/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/tutorial/_static/test.rpmmoved
%ghost %{SAGE_DOC}/html/en/website/_static/config.rpmmoved
%ghost %{SAGE_DOC}/html/en/website/_static/extensions.rpmmoved
%ghost %{SAGE_DOC}/html/en/website/_static/fonts.rpmmoved
%ghost %{SAGE_DOC}/html/en/website/_static/jax.rpmmoved
%ghost %{SAGE_DOC}/html/en/website/_static/localization.rpmmoved
%ghost %{SAGE_DOC}/html/en/website/_static/test.rpmmoved

#------------------------------------------------------------------------
%files		doc-fr
# CC-BY-SA-3.0
%{SAGE_DOC}/fr/
%{SAGE_DOC}/html/fr/

#------------------------------------------------------------------------
%files		doc-hu
# CC-BY-SA-3.0
%{SAGE_DOC}/hu/
%{SAGE_DOC}/html/hu/

#------------------------------------------------------------------------
%files		doc-it
# CC-BY-SA-3.0
%{SAGE_DOC}/it/
%{SAGE_DOC}/html/it/

#------------------------------------------------------------------------
%files		doc-pt
# CC-BY-SA-3.0
%{SAGE_DOC}/pt/
%{SAGE_DOC}/html/pt/

#------------------------------------------------------------------------
%files		doc-ru
# CC-BY-SA-3.0
%{SAGE_DOC}/ru/
%{SAGE_DOC}/html/ru/

#------------------------------------------------------------------------
%files		doc-tr
# CC-BY-SA-3.0
%{SAGE_DOC}/tr/
%{SAGE_DOC}/html/tr/
# with docs
%endif

#------------------------------------------------------------------------
%files		jupyter
# GPL-2.0-or-later
%{SAGE_ETC}/notebook-ipython/
%{_datadir}/jupyter/kernels/sagemath/
# MIT
%{_datadir}/jupyter/nbextensions/threejs-sage

#------------------------------------------------------------------------
%files		sagetex
# GPL-2.0-or-later
%{_bindir}/sagetex*
%{python3_sitearch}/sagetex*
%{python3_sitearch}/__pycache__/sagetex*
%{_texmf}/tex/latex/sagetex/
%doc %{_docdir}/sagetex/

########################################################################
%changelog
* Thu Mar 16 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 9.8-2
- Rebuild for libbraiding 1.2

* Mon Mar 13 2023 Jerry James <loganjerry@gmail.com> - 9.8-1
- Version 9.8
- Drop upstreamed patches: -fes-build, -python3.11
- Add patches: -catch-value, -gap-split-root, -bind2nd, -mem-fun-ref

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Jerry James <loganjerry@gmail.com> - 9.7-1
- Version 9.7
- Drop upstreamed patches: -infinite-recursion, -use-after-free, -sphinx

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 9.6-8
- Update for split GAP tree
- Add patch for FTBFS with latest giac (see bz 2160197)
- Fix eclib detection
- Add BR on pcre-devel
- Add BR on texlive-tex-gyre
- Rebuild for libfplll 5.4.4

* Tue Dec 20 2022 Jerry James <loganjerry@gmail.com> - 9.6-7
- Fix failure to install (bz 2154932)
- Fix failure to find nauty binaries (bz 2125737)
- Convert License tags to SPDX

* Wed Sep 21 2022 Jerry James <loganjerry@gmail.com> - 9.6-6
- Rebuild for gap 4.12.0 and pari 2.15.0

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 9.6-5
- Rebuild for gsl-2.7.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 9.6-3
- Add patch for python 3.11 compatibility (bz 2099168)
- Add workaround for symlink/directory conflict (bz 2097773)
- Modify the jmol patch to timeout after 5 minutes.  This is a workaround for
  recently observed jmol hangs, but is not a proper fix.

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 9.6-2
- Rebuilt for Python 3.11

* Wed Jun  1 2022 Jerry James <loganjerry@gmail.com> - 9.6-1
- Version 9.6
- Fix path to libSingular.so (bz 2073208)
- Fix threejs install location (bz 2081720)
- Drop upstreamed -rubiks and -intersphinx-disabled-reftypes patches
- Drop no longer used ratpoints BR
- Thebe is no longer bundled

* Sun Mar 27 2022 Jerry James <loganjerry@gmail.com> - 9.5-2
- Remove all support for 32-bit platforms
- Remove the interactive shell argument from /usr/bin/sage (rhbz#2028403)

* Mon Mar 21 2022 Jerry James <loganjerry@gmail.com> - 9.5-1
- Version 9.5
- Drop unnecessary -4ti2 and -primecount patches

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct  7 2021 Jerry James <loganjerry@gmail.com> - 9.4-2
- Rebuild for polymake 4.5

* Fri Aug 27 2021 Jerry James <loganjerry@gmail.com> - 9.4-1
- Version 9.4
- Drop upstreamed -eclib patch
- Drop unnecessary -readonly patch
- Unbundle ipywidgets
- Bundle memory_allocator for now

* Wed Aug 18 2021 Jerry James <loganjerry@gmail.com> - 9.3-5
- Unbundle flintqs
- Require gp2c and pari-nftables
- Add requirement for python3-pari-jupyter to the -jupyter subpackage

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Jerry James <loganjerry@gmail.com> - 9.3-3
- Rebuild for flint 2.7.1 and normaliz 3.9.0
- Add -eclib patch to adapt to eclib 20210625

* Tue Jun 29 2021 Jerry James <loganjerry@gmail.com> - 9.3-2
- Rebuild for ntl 11.5.1

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 9.3-1
- Version 9.3
- Drop -arb and -openblas patches
- Add -cvxopt patch
- Add metainfo file

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 9.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 9.2-3
- Try again to fix upgrade conflicts due to the fix for bz 1875606

* Tue Nov 17 2020 Jerry James <loganjerry@gmail.com> - 9.2-2
- Fix upgrade conflicts due to the fix for bz 1875606

* Tue Nov 10 2020 Jerry James <loganjerry@gmail.com> - 9.2-1
- Version 9.2 (bz 1891244)
- Unbundle widgetsnbextension (bz 1856311)
- Unbundle mathjax fonts (bz 1875606)
- Do not require the -doc subpackage from the main package (bz 1867123)
- Drop upstreamed patches: -ecl, -fes, -includes, -sagetex, -sigfpe, -sympy

* Wed Sep 30 2020 Jerry James <loganjerry@gmail.com> - 9.1-4
- Rebuild for primecount 6.1
- Bring back jmol/jsmol support

* Thu Aug 13 2020 Iñaki Úcar <iucar@fedoraproject.org> - 9.1-3
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jerry James <loganjerry@gmail.com> - 9.1-1
- Version 9.1
- Drop upstreamed -nauty patch
- Drop -cbc patch; upstream uses the system Cbc now
- Add -ecl patch for ecl 20.4.24

* Wed May 27 2020 Miro Hrončok <mhroncok@redhat.com> - 9.0-8
- Rebuilt for Python 3.9

* Wed May 13 2020 Jerry James <loganjerry@gmail.com> - 9.0-7
- Require libgap-devel so libgap.so can be found

* Mon May 11 2020 Jerry James <loganjerry@gmail.com> - 9.0-6
- Install threejs_template.html (bz 1832673)

* Fri May  8 2020 Jerry James <loganjerry@gmail.com> - 9.0-5
- Attempt 2 at fixing bundled ipython (bz 1832673)

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 9.0-4
- Fix bundled ipython incompatibility with python 3.8 (bz 1832673)

* Mon Apr 27 2020 Jerry James <loganjerry@gmail.com> - 9.0-3
- Build without jmol/jsmol support due to retirement of jmol from Fedora

* Fri Mar 13 2020 Jerry James <loganjerry@gmail.com> - 9.0-2
- Rebuild for gap 4.11.0
- Update libgap interface for gap 4.11.0
- Adjust list of gap packages to match build/pkgs/gap_packages
- Point sharedmeataxe to a writable directory for its multiplication tables

* Fri Feb 28 2020 Jerry James <loganjerry@gmail.com> - 9.0-1
- Version 9.0 (bz 1756780, 1770880)
- Drop upstreamed -ecm and -primecount patches
- Add -escape patch
- The old notebook (sagenb) is no longer shipped, so drop the -sagenb and
  -sagenb-python3 patches, the -notebook subpackage, and some BRs
- New -jupyter subpackage
- Add suitesparse BR
- Drop pathlib2 BR (bz 1797116)
- Do not build for 32-bit ARM, which is unable to unpack the source RPM without
  running out of memory

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 8.9-2
- Build with sharedmeataxe and tdlib support
- Use local objects.inv when building documentation

* Thu Nov  7 2019 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 8.9-1
- Update to latest upstream release
- Drop no longer need patches and rediff current ones

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 8.8-7
- Rebuild for mpfr 4
- Drop -mpfr patch

* Thu Sep 26 2019 Jerry James <loganjerry@gmail.com> - 8.8-6
- Rebuild for ntl 11.4.0
- Add primecount support, including the -primecount patch
- Add still more gap packages, nearly finishing the set shipped by upstream

* Thu Sep 12 2019 Jerry James <loganjerry@gmail.com> - 8.8-5
- Improve the -ecm patch
- Add -formatargspec patch to silence doc-building warnings
- Add -data-elliptic_curves_large subpackage
- Build with bliss, coxeter3, and mcqd support
- Fix typo that made the singular.hlp file inaccessible
- Add more gap packages to get closer to the set shipped by upstream
- Refactor Requires so they apply to the correct subpackages
- More python 3 patching due to changes in python 3.8
- Use upstream's method of installing jupyter support
- Obsolete the sagemath-notebook-export subpackage

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 8.8-4
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul  1 2019 Jerry James <loganjerry@gmail.com> - 8.8-1
- Update to sagemath 8.8 (bz 1724394)
- Remove configparser dependencies (bz 1706597)
- Fix broken sed conversion (bz 1706234)
- Fix python2 versus python3 snafu (bz 1706337, 1707166)
- Build and install sagetex (bz 1706322)

* Sat Apr 27 2019 Jerry James <loganjerry@gmail.com> - 8.7-1
- Update to sagemath 8.7
- Drop upstreamed -giac patch
- Add -sagetex patch to fix a python indentation error
- Add -rubiks patch to fix compilation of the rubiks library
- Add -random patch to fix a non-random random bit generator
- Drop pip3 workaround; the binary is now named just pip again

* Mon Feb 18 2019 Jerry James <loganjerry@gmail.com> - 8.6-1
- Update to sagemath 8.6
- Install an SVG icon instead of a fixed size (128x128) icon
- Require hicolor-icon-theme since we install an icon
- Drop obsolete Obsoletes

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.5-4
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Jerry James <loganjerry@gmail.com> - 8.5-2
- Add Education category to the desktop file (bz 1624545)
- Improve jupyter integration (bz 1663165)
- Move existing jupyter integration into the notebook subpackage
- Require python-jupyter-filesystem instead of owning its directories
- Drop one more remnant of the F24 to F25 upgrade fixup

* Thu Jan 17 2019 Jerry James <loganjerry@gmail.com> - 8.5-1
- Update to sagemath 8.5
- Bundle ipython again; Fedora version is too far ahead.  Also have to bundle
  prompt_toolkit since Fedora version is too far ahead of bundled ipython.
- Drop LANGUAGES variable setting, now ignored by the sagemath build system
- Drop unused SAGE_CBLAS variable from /usr/bin/sage
- Do not force the C locale when launching sagemath
- Allow the user to override SAGE_DEBUG in /usr/bin/sage
- Add -ecm, -giac, and -latte patches to fix interactions with external tools
- Add -sigfpe patch from upstream

* Thu Oct 25 2018 Jerry James <loganjerry@gmail.com> - 8.4-1
- Update to sagemath 8.4
- Build for python 3 instead of python 2 due to upcoming python 2 removal
- Add -python3 and -escape patches to fix problems with python 3
- Drop -nofstring patch, only needed for python 2
- Drop upstreamed -eclib patch
- Switch from atlas to openblas and rename -atlas patch to -openblas
- Add -buildroot patch and only build cython interfaces once

* Sat Sep 22 2018 Jerry James <loganjerry@gmail.com> - 8.3-1
- Update to sagemath 8.3 (bz 1612867)
- Drop -lrslib, -gap-hap, and -flask patches
- Drop obsolete scriplets to fix F24 to F25 upgrade (bz 1594429 and 1618934)
- Drop obsolete mktexlsr invocations
- Fix more Singular paths
- Fix still more uses of /usr/bin/env
- Drop disallow/dissallow fixup for cython; now fixed in cython itself

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 8.2-4
- Rebuild for arb 2.14.0, eclib 20180710, ntl 11.2.1, and pari 2.11.0
- Drop unneeded genus2reduction dependency; pari is used instead now

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 8.2-2
- Rebuild for ntl 11.1.0
- Optionally bundle thebe, threejs, and widgetsnbextension
- Add provides for the optionally bundled packages
- Add -flask patch
- Apply new guidelines for python files in nonstandard places

* Fri May 18 2018 Jerry James <loganjerry@gmail.com> - 8.2-1
- Update to sagemath 8.2
- Create the sagemath-data-combinatorial_designs subpackage
- Create the sagemath-notebook-export subpackage
- Unbundle the LaTeX makecmds style
- Install LaTeX style files in a more canonical place

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Jerry James <loganjerry@gmail.com> - 8.0-2
- Do not interpret GAP library informational messages as a libgap failure
- Build with cryptominisat5
- Sagemath now invokes gap instead of gap_stamp

* Thu Nov 23 2017 Jerry James <loganjerry@gmail.com> - 8.0-1
- Build with bundled ipywidgets for now
- Drop unneeded -givaro patch
- Lots of new BRs for building documentation
- R python-backports-shutil_get_terminal_size and python-traitlets (bz 1464520)
- Fix Singular LIB path
- Make sure install operates in a UTF-8 environment
- Build documention with an X server running
- Build HTML documentation with mathjax

* Fri Nov 10 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 8.0-1
- Update to sagemath 8.0
- Remove cryptominisat build requires
- Remove no longer needed -singular patch (upstream updated)
- Remove no longer -flask patch (upstream updated)
- Remove no longer -pari patch (used now by cypari2)
- Disable option to use bundled cysignals
- Disable option to use bundled pari
- Use system ipython

* Sat Sep 30 2017 Jerry James <loganjerry@gmail.com> - 7.6-6
- Rebuild for arb 2.11.1, eclib 20170815, and libfplll 5.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 7.6-4
- Add missing python-psutil dependency
- Add extra environment variable to avoid Singular-devel dependency

* Tue May 23 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 7.6-3
- Correct singular data dir path
- Correct sage -testall initialization
- Switch to empty directory to pass check for sage packages
- Correct SAGE_SRC symbolic link
- Remove explicit firefox dependency (#1446508)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Apr 11 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 7.6-1
- Update to sagemath 7.6
- Switch back to system pari

* Thu Apr  6 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 7.5.1-1
- Update to sagemath 7.5.1

* Fri Mar  3 2017 Jerry James <loganjerry@gmail.com> - 7.4-4
- Rebuild for ppl 1.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 7.4-2
- Rebuild for readline 7.x

* Fri Dec 30 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 7.4-1
- Update to sagemath 7.4

* Tue Dec 20 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 7.3.7
- Correct f24 to f25 upgrade, sagemath 6.8 to 7.3 (#1396848)

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 7.3-6
- Rebuild for ntl 10.1.0

* Sun Oct 09 2016 Dominik Mierzejewski <rpm@greysector.net> - 7.3-5
- rebuild for aarch64 (#1380191 fixed)

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 7.3-4
- rebuilt for matplotlib-2.0.0
- sync supported arches with maxima

* Mon Sep  5 2016 Jerry James <loganjerry@gmail.com> - 7.3-3
- Rebuild for ntl 9.11.0
- Add gap-pkg-guava requirement

* Wed Aug 24 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 7.3-2
- Make notebook functional with python-flask-0.11.1

* Sat Aug 20 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 7.3-1
- Update to sagemath 7.3
- Switch from polybori to brial
- Default to use system pexpect
- Use system mathjax

* Fri Aug 12 2016 Jerry James <loganjerry@gmail.com> - 6.8-14
- Rebuild for fflas-ffpack 2.2.2, givaro 4.0.2, and linbox 1.4.2
- GAP packages atlasrep, design, and hap are now available

* Sat Jul 23 2016 Jerry James <loganjerry@gmail.com> - 6.8-13
- Rebuild for ntl 9.10.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 6.8-11
- Rebuild for ntl 9.9.1

* Fri Apr 29 2016 Jerry James <loganjerry@gmail.com> - 6.8-10
- Rebuild for ntl 9.8.0
- Nauty is now available under a free license

* Wed Apr 13 2016 Jerry James <loganjerry@gmail.com> - 6.8-9
- Rebuild for linbox 1.4.1

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 6.8-8
- Rebuild for libgap 4.8.3

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 6.8-7
- Rebuild for glpk 4.59, ntl 9.7.0 and gmp-ecm 7.0

* Mon Mar  7 2016 Jerry James <loganjerry@gmail.com> - 6.8-6
- Doc packages cannot be noarch since they are not built for all arches

* Sat Feb 27 2016 Jerry James <loganjerry@gmail.com> - 6.8-6
- Rebuild for givaro 4.0.1, fflas-ffpack 2.2.0, and linbox 1.4.0
- Add -givaro patch to adapt to header file changes in those releases

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 6.8-5
- Rebuild for gsl 2.1

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 6.8-4
- Rebuild for ntl 9.6.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Jerry James <loganjerry@gmail.com> - 6.8-2
- Rebuild for arb 2.8.0

* Tue Dec 22 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.8-1
- Update to sagemath 6.8
- Remove scons, lrcalc, cryptominisat, parallel and ipython3 patches
- Add lcalc, fes-build and arb patches

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 6.5-14
- Rebuild for ntl 9.6.2

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 6.5-13
- Rebuild for m4rie 20150908 and ntl 9.4.0

* Sat Oct  3 2015 Jerry James <loganjerry@gmail.com> - 6.5-12
- Rebuild for ecl 16.0.0

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 6.5-11
- Rebuild for eclib 20150827, flint 2.5.2, and ntl 9.3.0

* Fri Sep  4 2015 Jerry James <loganjerry@gmail.com> - 6.5-10
- Rebuild for cryptominisat 2.9.10

* Sat Aug 29 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.5-9
- Apply conditionally not required for f22 ipython3 patch (#1258006)
- Add missing sphinx requires (#1229283)

* Mon Aug  3 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.5-8
- Bump release for f23 rebuild

* Sun Jul 19 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.5-7
- Correct unable to start QEPCAD within sage (#1243590)
- Use interactive bash on wrappers to work with other login shells (#1238341)
- Properly generate localized translations

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 6.5-5
- Rebuild for ntl 9.1.1 and cddlib 094h

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 6.5-4
- Rebuild for ntl 9.1.0

* Tue May  5 2015 Peter Robinson <pbrobinson@fedoraproject.org> 6.5-3
- Drop old F-18 comparisions
- Build on ARMv7, all deps now met

* Sun Apr 26 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.5-2
- Add patch to work with ipython 3

* Fri Apr  3 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.5-1
- Update to sagemath 6.5
- Add new Catalan and Hungarian doc subpackages
- Add customizations to not need a patched pari
- Add "with docs" test build option
- Convert build conditionals to use bcond
- Correct deprecated warning when loading sagenb

* Sat Feb  7 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.4.1-4
- Rebuild with a functional jsmol interface (#1190356)

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 6.4.1-3
- Rebuild for ntl 8.1.2

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 6.4.1-2
- Rebuild for ntl 8.1.0
- Future-proof the gap package names

* Wed Nov 26 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.4.1-1
- Update to sagemath 6.4.1 (#1095282)

* Sat Nov 1 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.3-4
- Install 128x128 icon (#1157575)

* Mon Oct 27 2014 Jerry James <loganjerry@gmail.com>
- Rebuild for m4ri 20140914 and ntl 6.2.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.3-1
- Update to sagemath 6.3 (#1095282)
- Add new doc-it Italian documentation subpackage

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.2-1
- Update to sagemath 6.2 (#1095282)
- Rebuild with Singular 3.1.6 (#1074597)
- Add missing python-docutils requires (#1056374)
- Correct uninstall of sagemath-notebook (#1097428)
- Enable coin-or-Cbc interface
- Make coin-or-Cbc not optional
- Make lrcalc not optional
- Use upstream patch to support pari 2.7
- Rediff ntl6 patch

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 6.1.1-5
- Rebuild for ntl 6.1.0
- Fix ld ignoring __global_ldflags due to embedded trailing space
- Fix Singular paths in the build environment

* Wed Mar 19 2014 Jerry James <loganjerry@gmail.com> - 6.1.1-4
- Rebuild for libgap 4.7.4 and cryptominisat 2.9.9

* Mon Mar 10 2014 Rex Dieter <rdieter@fedoraproject.org> 6.1.1-3
- rebuild (Singular)

* Wed Feb 12 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.1.1-2
- Enable optional fes dependency
- Correct jmol applet interface
- Add missing python-twisted-mail requires (#1063061)
- Correct problems when starting sage for the first time as a new user
- Correct atlas library path for f21 or newer

* Fri Feb  7 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 6.1.1-1
- Update to sagemath 6.1.1

* Tue Jan 28 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.13-1
- Update to sagemath 5.13

* Fri Jan 17 2014 Jerry James <loganjerry@gmail.com> - 5.12-3
- Also adapt Requires to the new gap subpackage structure

* Wed Jan 15 2014 Jerry James <loganjerry@gmail.com> - 5.12-2
- Rebuild for libgap 4.7.2
- Adapt gap BRs to new gap subpackage structure

* Wed Oct 16 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.12-1
- Update to sagemath 5.12.

* Sat Sep 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.10-4
- Do not hardcode SAGE_BROWSER (#967251)
- Remove pre(trans) scriptlet used to upgrade from prototype packages

* Tue Sep 10 2013 Rex Dieter <rdieter@fedoraproject.org> 5.10-3
- pretrans scriplet uses shell commands (#1006230)

* Mon Aug 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.10-2
- Correct side effect of using system mpmath (#974769)

* Mon Aug  5 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.10-1
- Update to sagemath 5.10.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul  3 2013 Jerry James <loganjerry@gmail.com> - 5.9-8
- Rebuild for maxima 5.30.0

* Wed Jun 12 2013 Remi Collet <rcollet@redhat.com> - 5.9-7
- rebuild for new GD 2.1.0

* Tue Jun  4 2013 Jerry James <loganjerry@gmail.com> - 5.9-6
- Rebuild for ecl 2013.5.1

* Sun May 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.9-5
- Need one extra directory derefence in symlink SAGE_SRC symlink.

* Sun May 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.9-4
- Correct wrong symlink to /builddir if not using pretrans (first install).

* Sat May 11 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.9-3
- Add pretrans for clean upgrade after rename of SAGE_DEVEL to SAGE_SRC.

* Sat May 11 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.9-2
- Build in f18 and f18 with workaround to cython wrong defines (#961372)

* Mon May 6 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.9-1
- Update to sagemath 5.9.
- Match upstream rename of SAGE_DEVEL to SAGE_SRC.
- Merged -buildroot in -rpmbuild patch.
- Drop cython 0.19 patch already applied to sagemath 5.9.
- Add macro conditionals to use same spec and patches in f18, f19 and f20.

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 5.8-9
- Rebuild for libfplll 4.0.3, m4ri and m4rie 20130416, and ntl 6.0.0
- Drop sagemath-unpatched_ntl.patch now that Fedora's NTL is patched
- Add sagemath-ntl6.patch to adapt to NTL 6
- Add sagemath-m4rie.patch to adapt to m4rie 20130416

* Sat Apr 27 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.8-8
- Add surf-geometry to path for proper Singular plotting
- Add workaround to an rpm scriptlet problem (#877651#89)

* Tue Apr 23 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.8-7
- Correct problem of package requiring a -devel file to work.

* Tue Apr 23 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.8-6
- Correct a remaining arch specific file (symlink) in noarch package.

* Mon Apr 22 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.8-5
- Do not build requires optional rpy in f18 due to it being broken in f18
- Correct koji sanity check finding arch specific file in noarch package
- Add patch to build with just upgraded cython in rawhide

* Mon Apr 22 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.8-4
- Remove noop icon cache regeneration scriplets (#877651#72)
- First Fedora 18 and Fedora 19 approved package

* Sun Apr 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.8-3
- Use proper license tag for non versioned GPL attribution (#877651#63)
- Remove no longer required workarounds for clean upgrades (#877651#63)

* Fri Apr 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.8-2
- Properly describe the license breakdown in the spec (#877651#60)
- Correct lrslib requires to lrslib-utils (#877651#60)
- Remove zero length files (#877651#60)
- Correct png file with executable permission (#877651#60)
- Avoid rpmlint warning in rubiks subpackage description (#877651#60)

* Tue Mar 19 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.8-1
- Update to sagemath 5.8.
- Do full cleanup of notebook package on uninstall.
- Remove with_sage_cython build conditional.
- Remove with_sage_networkx build conditional.
- Add nopari2.6 patch to not rely on not yet available interfaces.
- Add cryptominisat patch to build package in f18.

* Sat Mar 16 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.7-3
- Create jmol symbolic links in post and remove in postun.
- Disable libgap by default as it does not work with rawhide gap.
- Also add python-ipython to build requires to regenerate documentation.

* Wed Mar  6 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.7-2
- Add missing python-ipython requires (#877651#52)
- Enable libgap build in packager debug build (#877651#52)

* Fri Feb 22 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.7-1
- Update to sagemath 5.7.
- Add conditional patch for libgap.
- Add conditional patch for fes.
- Remove with_sage_ipython conditional.
- Add patch to create a libcsage with a soname.

* Mon Feb 18 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.6-6
- Rebuild with latest rawhide and f18 updates
- Make sagemath-notebook owner of its base data directory
- Explicitly mark notebook translations as %%lang (#877651#c46)
- Remove sage3d as it is not functional in the rpm package (#877651#c46)
- Remove reference to buildroot in libcsage.so debuginfo

* Fri Feb 15 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.6-5
- Export CFLAGS and CXXFLAGS (#877651#c45)
- Make sagemath-data owner of SAGE_SHARE (#877651#c45)
- Relocate SAGE_DOC and make sagemath-doc packages noarch (#877651#c45)
- Relocate SAGE_SHARE and make sagemath-data packages noarch (#877651#c45)
- Remove sagenb binary egg bundled in tarball (#877651#c45)
- Update license tag due to unlisted Apache v2 license (#877651#c45)
- Break down licenses in files listing (#877651#c45)
- Add post scriplets to handle the installed icon (#877651#c45)
- Do not install empty directories in SAGE_EXTCODE (#877651#c45)
- Do not install bundled mathjax fonts (#877651#c45)
- Add a descriptive comment to patches without one (#877651#c45)
- Correct mispelled donwload_tarball macro name (#877651#c45)
- Remove reference to buildroot in prep (#877651#c45)
- Simplify coin-or-Cbc build requires as it has proper dependencies

* Sun Feb 10 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.6-4
- Correct "canonicalization unexpectedly shrank by one character" error.
- Add packager_debug macro for conditional package debug mode build.
- Add donwload_tarball macro to avoid fedora-review donwloading it every run.

* Sat Feb  9 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.6-3
- Add cryptominisat-devel to build requires.
- Add conditional build for lrcalc (fedora review rhbz #909510)
- Add conditional build for coin-or-CoinUtils (fedora review rhbz #894585)
- Add conditional build for coin-or-Osi (fedora review rhbz #894586)
- Add conditional build for coin-or-Clp (fedora review rhbz #894587)
- Add conditional build for coin-or-Cgl (fedora review rhbz #894588)
- Add conditional build for coin-or-Cbc (fedora review rhbz #894597)
- Rebuild with latest rawhide and f18 dependency updates.

* Mon Jan 28 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.6-2
- Rebuild with latest rawhide and f18 updates.

* Fri Jan 25 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.6-1
- Update to sagemath 5.6.
- Remove no longer required patch to build with system cython.

* Sat Jan 19 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.5-3
- Rediff rpmbuild patch to address some underlinked modules.
- Make gap-sonata a mandatory requires.
- Add cremona patch to adjust logic as only cremona mini is built.
- Add lrslib patch to know lrslib is available.
- Add nauty patch and comment about reason it cannot be made available.
- Add gap-hap patch for better description of missing gap hap package.

* Fri Jan 04 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.5-2
- Add cython to build requires (#877651#c28).

* Sat Dec 29 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.5-1
- Update to sagemath 5.5.
- Add maxima.system patch to work with maxima 5.29.1 package.

* Fri Dec 14 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.1-5
- Build with system cython by default on fedora 18 or newer (#877651).

* Fri Dec 14 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.1-4
- The fplll patch is also required to build in f18.
- Add factory include to plural.pyx build.

* Wed Dec 05 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.1-3
- Revert requires python-matplotlib-tk as it was a python-matplotlib bug.
- Add stix-fonts requires.

* Sat Dec 01 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.1-2
- Change back to install .c and .h files in bundled cython.
- Make symlink of gmp-ecm to $SAGE_LOCAL/bin/ecm.
- Add SAGE_LOCAL/bin to python path so that "sage -gdb" works.
- Require python-matplotlib-tk to avoid possible import error in doctests.

* Fri Nov 30 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.1-1
- Update to sagemath 5.4.1.

* Tue Nov 20 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4-2
- Do not install alternate cygdb in %%_bindir
- Create the sagemath-core subpackage
- Create the sagemath-doc subpackage
- Create the sagemath-doc-en subpackage
- Create the sagemath-doc-de subpackage
- Create the sagemath-doc-fr subpackage
- Create the sagemath-doc-pt subpackage
- Create the sagemath-doc-ru subpackage
- Create the sagemath-doc-tr subpackage
- Create the sagemath-data metapackage
- Create the sagemath-data-conway_polynomials subpackage
- Create the sagemath-data-elliptic_curves subpackage
- Create the sagemath-data-extcode subpackage
- Do not install pickle_jar extcode contents
- Do not install notebook extcode contents
- Create the sagemath-data-graphs subpackage
- Create the sagemath-data-polytopes_db subpackage
- Create the sagemath-notebook subpackage
- Create the sagemath-rubiks subpackage
- Create the sagemath-sagetex subpackage

* Mon Nov 12 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4-1
- Update to sagemath 5.4.
- Build with system networkx.
- Install only one fallback icon.
- Prevent rpm from providing private shared object.
- Change base directory to %%{_libdir} to avoid rpmlint errors.
- Correct permissions of installed shared objects.
- Rename most patches to use %%{name} prefix as "suggested" by fedora-review.
- Remove bundled jar files before %%build.
- Make cube solvers build optional and disabled by default.
- Add option to run "sage -testall" during package build.

* Sat Nov 10 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.beta1-4
- Add patch to make jmol export image functional
- Update pari patch to use proper path to gprc.expect
- Force usage of firefox in notebook (known to work are firefox and chromium)

* Fri Oct 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.beta1-3
- Add support for releases with libmpc 0.9.

* Wed Oct 24 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.beta1-2
- Add Portuguese translations of Tutorial and A Tour of Sage

* Sat Oct 20 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.beta1-1
- Update to sagemath 5.4.beta1
- Removed already applied upstream linbox upgrade patch
- Removed already applied upstream givaro upgrade patch
- Removed already applied upstream singular upgrade patch
- Install rubiks spkg binaries

* Wed Sep 12 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.3-1
- Update to sagemath 5.3.
- Remove version from patches name.
- Drop m4ri patch already applied to upstream.

* Fri Sep 7 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.2-2
- Add sphinx workaround to have editable tutorial forms (#839321)
- Make interactive 3d plots using jmol applet functional (#837166)
- Use system genus2reduction
- Add workaround to mp_set_memory_functions call from pari library

* Sat Aug 4 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.2-1
- Update to sagemath 5.2.

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.0.1-1
- Initial sagemath spec.
