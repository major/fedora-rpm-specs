# Whether to run tests
%bcond ctest 1

%global giturl  https://github.com/SRI-CSL/libpoly

Name:           libpoly
Version:        0.2.1
Release:        %autorelease
Summary:        C library for manipulating polynomials

License:        LGPL-3.0-or-later
URL:            https://sri-csl.github.io/libpoly/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): %{_cmake_skip_rpath}
BuildOption(conf): -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo
BuildOption(conf): -DLIBPOLY_BUILD_STATIC:BOOL=OFF
BuildOption(conf): -DLIBPOLY_BUILD_STATIC_PIC:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist sympy}

%description
LibPoly is a C library for manipulating polynomials.  The target applications
are symbolic reasoning engines, such as SMT solvers, that need to reason about
polynomial constraints.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package     -n python3-polypy
Summary:        Python 3 interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

# This can be removed when F45 reaches EOL
Obsoletes:      python3-%{name} < 0.1.14
Provides:       python3-%{name} = %{version}-%{release}

%description -n python3-polypy
This package contains a python 3 interface to %{name}.

%prep
%autosetup -p1

sed 's/\${LIBPOLY_VERSION}/%{version}/' python/setup.py.in > python/setup.py

# Install in the right place
sed -i 's/\(DESTINATION \)lib/\1${LIB_INSTALL_DIR}/' src/CMakeLists.txt

# Clean up hidden files before they get installed
find . -name .gitignore -delete

%generate_buildrequires
%pyproject_buildrequires -d python

%conf -p
rm python/setup.py

%build -a
# Build the python interface the Fedora way
sed -i "s|library_dirs = \[|&'$PWD/%{_vpath_builddir}/src', |" python/setup.py
%pyproject_wheel -d python

%install -a
# Install the python interface the Fedora way
cd python
%pyproject_install
%pyproject_save_files -L polypy
cd -

%check -p
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/src

%files
%license LICENCE
%doc README.md
%{_libdir}/libpoly.so.0{,.*}
%{_libdir}/libpolyxx.so.0{,.*}

%files devel
%{_includedir}/poly/
%{_libdir}/libpoly.so
%{_libdir}/libpolyxx.so

%files -n python3-polypy -f %{pyproject_files}
%license LICENCE

%changelog
%autochangelog
