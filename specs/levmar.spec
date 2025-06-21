# SOlib major and minor version
%global major 2
%global minor 6

%bcond flexiblas 1

Name:		levmar
Version:	2.6
Release:	%autorelease
Summary:	Levenberg-Marquardt nonlinear least squares algorithm
URL:		https://www.ics.forth.gr/~lourakis/levmar/

Source:		https://www.ics.forth.gr/~lourakis/levmar/levmar-%{version}.tgz

# Patch to fix compilation of the shared library and compile the demo program
Patch:		levmar-cmake-shared.patch

License:	GPL-2.0-or-later
BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	dos2unix
BuildRequires:	chrpath
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel, lapack-devel
%endif

%description
levmar is a native ANSI C implementation of the Levenberg-Marquardt
optimization algorithm.  Both unconstrained and constrained (under linear
equations, inequality and box constraints) Levenberg-Marquardt variants are
included.  The LM algorithm is an iterative technique that finds a local
minimum of a function that is expressed as the sum of squares of nonlinear
functions.  It has become a standard technique for nonlinear least-squares
problems and can be thought of as a combination of steepest descent and the
Gauss-Newton method.  When the current solution is far from the correct on,
the algorithm behaves like a steepest descent method: slow, but guaranteed
to converge.  When the current solution is close to the correct solution, it
becomes a Gauss-Newton method.

%package devel
Summary:	Development files for levmar library, and demo program
Requires:	levmar = %{version}-%{release}

%description devel
Development files for the levmar library, and demo program.

%prep
%autosetup -p1
dos2unix -k README.txt

%if %{with flexiblas}
sed -i 's/lapack;blas/flexiblas;flexiblas/g' CMakeLists.txt
%endif

%build
%cmake -DLINSOLVERS_RETAIN_MEMORY:BOOL=OFF -DNEED_F2C:BOOL=OFF
%cmake_build

%install
install -D -p -m 755 "%{_vpath_builddir}/liblevmar.so.%{major}.%{minor}" "%{buildroot}%{_libdir}/liblevmar.so.%{major}.%{minor}"
install -D -p -m 644 levmar.h "%{buildroot}%{_includedir}/levmar.h"
install -D -p -m 755 "%{_vpath_builddir}/lmdemo" "%{buildroot}%{_bindir}/lmdemo"
ln -s "liblevmar.so.%{major}.%{minor}" "%{buildroot}%{_libdir}/liblevmar.so.%{major}"
ln -s "liblevmar.so.%{major}.%{minor}" "%{buildroot}%{_libdir}/liblevmar.so"
chrpath --delete "%{buildroot}%{_bindir}/lmdemo"

%check
%{_vpath_builddir}/lmdemo

%files
%doc README.txt LICENSE
%{_libdir}/liblevmar.so.%{major}.%{minor}
%{_libdir}/liblevmar.so.%{major}

%files devel
%{_includedir}/levmar.h
%{_libdir}/liblevmar.so
%{_bindir}/lmdemo

%changelog
%autochangelog
