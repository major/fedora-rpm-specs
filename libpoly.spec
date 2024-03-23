Name:           libpoly
Version:        0.1.13
Release:        %autorelease
Summary:        C library for manipulating polynomials

License:        LGPL-3.0-or-later
URL:            https://sri-csl.github.io/libpoly/
VCS:            https://github.com/SRI-CSL/libpoly
Source0:        %{vcs}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix incompatible pointer type, an error with GCC 14
# See https://github.com/SRI-CSL/libpoly/pull/76
Patch0:         %{name}-gcc14.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist sympy}

%description
LibPoly is a C library for manipulating polynomials.  The target
applications are symbolic reasoning engines, such as SMT solvers, that
need to reason about polynomial constraints.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n python3-%{name}
Summary:        Python 3 interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
This package contains a python 3 interface to %{name}.

%prep
%autosetup -p1

# Install in the right place
if [ "%{_lib}" != "lib" ]; then
  sed -i 's/\(DESTINATION \)lib/\1%{_lib}/' src/CMakeLists.txt
fi

# Clean up hidden files before they get installed
find . -name .gitignore -delete

%generate_buildrequires
cd python
sed 's/\${LIBPOLY_VERSION}/%{version}/' setup.py.in > setup.py
%pyproject_buildrequires
rm setup.py

%build
%cmake %{_cmake_skip_rpath} \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DLIBPOLY_BUILD_STATIC:BOOL=OFF \
  -DLIBPOLY_BUILD_STATIC_PIC:BOOL=OFF
%cmake_build

# Build the python interface the Fedora way
sed -i "s|library_dirs = \[|&'$PWD/%{_vpath_builddir}/src', |" python/setup.py
cd python
%pyproject_wheel
cd -

%install
%cmake_install

# Install the python interface the Fedora way
cd python
%pyproject_install
%pyproject_save_files polypy
cd -

%check
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/src
%ctest

%files
%license LICENCE
%doc README.md
%{_libdir}/libpoly.so.0*
%{_libdir}/libpolyxx.so.0*

%files devel
%{_includedir}/poly/
%{_libdir}/libpoly.so
%{_libdir}/libpolyxx.so

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
