Name:           scip
Version:        8.1.0
Release:        %autorelease
Summary:        Solving Constraint Integer Programs

%global upver   %(sed 's/\\.//g' <<< %{version})

License:        Apache-2.0
URL:            https://scipopt.org/
VCS:            https://github.com/scipopt/scip
Source0:        %{vcs}/archive/v%{upver}/%{name}-%{version}.tar.gz
# Do not add an rpath
Patch0:         %{name}-no-rpath.patch
# Unbundle nauty
Patch1:         %{name}-unbundle.patch
# Install the header files in a private directory
Patch2:         %{name}-headers.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  cmake(soplex)
BuildRequires:  cmake(zimpl)
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(ipopt)
BuildRequires:  pkgconfig(nauty)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  soplex
BuildRequires:  zimpl

# Documentation
BuildRequires:  doxygen
BuildRequires:  mathjax
BuildRequires:  php-cli
BuildRequires:  python3

Requires:       libscip%{?_isa} = %{version}-%{release}

# SCIP includes a modified version of cppad, incompatible with the Fedora
# version
Provides:       bundled(cppad) = 20180000

# SCIP bundles a few header files from mp.  We don't want to make it depend on
# mp, however, since mp depends on SCIP, thus leading to a circular dependency.
Provides:       bundled(mp) = 20210923

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

# We want to know about overflow errors, as the compiler can do surprising
# things if we don't fix them!
sed -i 's/ -Wno-strict-overflow//' CMakeLists.txt make/make.project

# Fix library directories
if [ "%{_lib}" != "lib" ]; then
  sed -i 's,\(DESTINATION \)lib,\1%{_lib},' src/CMakeLists.txt
fi

# Turn off HTML timestamps for repeatable builds
sed -i '/HTML_TIMESTAMP/s/= YES/= NO/' doc/scip.dxy
sed -i 's/ on \$date//' doc/scipfooter.html

# Look for python3 instead of python
sed -i 's/PYTHON python/&3/' doc/CMakeLists.txt

# Ensure we cannot use the bundled bliss, nauty, sassy, or tinycthreads
rm -fr src/{bliss,nauty,sassy,tinycthread}

%build
%cmake
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
%{_libdir}/libscip.so.8.1*

%files -n libscip-devel
%{_includedir}/scip/
%{_libdir}/libscip.so
%{_libdir}/cmake/scip/

%files -n libscip-doc
%doc doc/html

%changelog
%autochangelog
