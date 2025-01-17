Name:           scip
Version:        9.2.0
Release:        %autorelease
Summary:        Solving Constraint Integer Programs

%global upver   %(sed 's/\\.//g' <<< %{version})
%global giturl  https://github.com/scipopt/scip

# Apache-2.0: the project as a whole
# EPL-1.0: the bundled cppad project
# MIT: the bundled fmt project and the header-only sassy package
# SMLNJ: bundled headers from the mp package
License:        Apache-2.0 AND EPL-1.0 AND MIT AND SMLNJ
URL:            https://scipopt.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{upver}/%{name}-%{version}.tar.gz
# Do not add an rpath
Patch:          %{name}-no-rpath.patch
# Unbundle nauty and tinycthread
Patch:          %{name}-unbundle.patch
# Install the header files in a private directory
Patch:          %{name}-headers.patch
# Silence valgrind complaints about use of uninitialized memory
Patch:          %{name}-uninitialized-memory.patch
# Patch from sassy upstream to avoid vector overruns
Patch:          %{name}-sassy-overrun.patch
# Use zlib-ng directly rather than via the compatibility interface
Patch:          %{name}-zlib-ng.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  cmake(soplex)
BuildRequires:  cmake(zimpl)
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gnuplot
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(ipopt)
BuildRequires:  pkgconfig(libnauty)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  soplex
BuildRequires:  zimpl

# Documentation
BuildRequires:  doxygen
BuildRequires:  mathjax
BuildRequires:  php-cli
BuildRequires:  python3

Requires:       libscip%{?_isa} = %{version}-%{release}

%global _desc %{expand:
Welcome to what is currently one of the fastest academically developed
solvers for mixed integer programming (MIP) and mixed integer nonlinear
programming (MINLP).  In addition, SCIP provides a highly flexible
framework for constraint integer programming and branch-cut-and-price.
It allows for total control of the solution process and the access of
detailed information down to the guts of the solver.}

%description %_desc

This package contains a command-line tool to access SCIP
functionality.

%package -n     libscip
Summary:        Library for solving constraint integer programs

# SCIP includes a modified version of cppad, incompatible with the Fedora
# version
Provides:       bundled(cppad) = 20180000

# SCIP bundles a few header files from mp.  We don't want to make it depend on
# mp, however, since mp depends on SCIP, thus leading to a circular dependency.
Provides:       bundled(mp) = 20231229

# The bundled version of fmt is incompatible with version 10 in Rawhide.
Provides:       bundled(fmt) = 3.0.1

# We bundle sassy temporarily until it can be included as a Fedora package
Provides:       bundled(sassy) = 1.1

%description -n libscip %_desc

This package contains a library for solving constraint integer programs.

%package -n     libscip-devel
Summary:        Headers and library links for libscip
Requires:       scip%{?_isa} = %{version}-%{release}
Requires:       libscip%{?_isa} = %{version}-%{release}
Requires:       libnauty-devel%{?_isa}
Requires:       zlib-devel%{?_isa}

%description -n libscip-devel
This package contains headers and library links for developing
applications that use libscip.

%package -n     libscip-doc
# The content is licensed with Apache-2.0.  The other licenses are due to files
# added by doxygen.  Most such files are licensed with GPL-1.0-or-later, but
# the JavaScript files are licensed with MIT.
License:        Apache-2.0 AND GPL-1.0-or-later AND MIT
Summary:        API documentation for libscip
BuildArch:      noarch

Provides:       bundled(jquery) = 3.6.0

%description -n libscip-doc
API documentation for libscip.

%prep
%autosetup -n %{name}-%{upver} -p1

%conf
# We want to know about overflow errors, as the compiler can do surprising
# things if we don't fix them!
sed -i 's/ -Wno-strict-overflow//' CMakeLists.txt make/make.project

# Turn off HTML timestamps for repeatable builds
sed -i '/HTML_TIMESTAMP/s/= YES/= NO/' doc/scip.dxy
sed -i 's/ on \$date//' doc/scipfooter.html

# Use a fixed 'linux' value in OSTYPE for repeatable builds
sed -i 's/OSTYPE=@.*@/OSTYPE=linux/' src/scipbuildflags.c.in

# Ensure we cannot use the bundled bliss, nauty, or tinycthreads
rm -fr src/{bliss,nauty,tinycthread}

%build
CFLAGS='%{build_cflags} -D_Thread_local=thread_local'
CXXFLAGS='%{build_cxxflags} -D_Thread_local=thread_local'
%cmake -DNAUTY_DIR=%{_prefix} -DSYM=snauty
%cmake_build

# Build documentation
cd doc
ln -s %{_datadir}/javascript/mathjax MathJax
../%{_vpath_builddir}/bin/scip < inc/shelltutorial/commands \
  > inc/shelltutorial/shelltutorialraw.tmp
python3 inc/shelltutorial/insertsnippetstutorial.py
cd inc/faq
python3 parser.py --linkext shtml
php localfaq.php > faq.inc
cd -
../%{_vpath_builddir}/bin/scip -c "set default set save inc/parameters.set quit"
../%{_vpath_builddir}/bin/scip -c "read inc/simpleinstance/simple.lp optimize quit" \
  > inc/simpleinstance/output.log
doxygen scip.dxy
cd ..

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
# The BendersQP-benders-qp-classical_20_0.mps test often triggers a timeout.
# We could make the timeout longer (1500 seconds by default), but it sometimes
# times out even at 3000 seconds.  Let's just skip it.
%ctest -E classical_20_0

%files
%{_bindir}/scip

%files -n libscip
%doc CHANGELOG README.md
%license LICENSE
%{_libdir}/libscip.so.9.2*

%files -n libscip-devel
%{_includedir}/scip/
%{_libdir}/libscip.so
%{_libdir}/cmake/scip/

%files -n libscip-doc
%doc doc/html

%changelog
%autochangelog
