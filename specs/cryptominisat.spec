# We bundle cadiback because it has been modified by the cryptominisat team to
# present a library interface to cryptominisat
%global cadiurl     https://github.com/meelgroup/cadiback
%global cadicommit  69255f55e411207c4bdea02c6c2ab1ef29740ce1
%global shortcommit %(c=%{cadicommit}; echo ${c:0:7})
%global giturl      https://github.com/msoos/cryptominisat

Name:           cryptominisat
Version:        5.11.22
Release:        %autorelease
Summary:        SAT solver

License:        MIT
URL:            https://www.msoos.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{cadiurl}/archive/%{cadicommit}/cadiback-%{shortcommit}.tar.gz
# Change the CMake files to not change Fedora build flags
Patch:          %{name}-cmake.patch
# Unbundle picosat
Patch:          %{name}-picosat.patch
# Do not rebuild the entire library for python; just link the existing library
Patch:          %{name}-python-library.patch
# Use tomllib instead of tomli
Patch:          %{name}-toml.patch
## Post 5.11.22-release bug fixes
# https://github.com/msoos/cryptominisat/commit/2905d6d9a755e9f20ec4a4c22f7f27070c4455e7
# https://github.com/msoos/cryptominisat/commit/1d735b6ce0e3d17cdec182db491646fc89aa8cf4
Patch:          %{name}-remove-old-api.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cadical-devel
BuildRequires:  cmake
BuildRequires:  cmake(breakid)
BuildRequires:  gcc-c++
BuildRequires:  gperftools-devel
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  picosat-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
CryptoMiniSat is a modern, multi-threaded, feature-rich, simplifying SAT
solver. Highlights:
- Instance simplification at every point of the search (inprocessing)
- Over 100 configurable parameters to tune to specific needs
- Collection of statistical data to MySQL database + javascript-based
  visualization of it
- Clean C++ and python interfaces

%package devel
Summary:        Header files for developing with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cadical-devel%{?_isa}
Requires:       zlib-devel%{?_isa}

%description devel
Header files for developing applications that use %{name}.

%package libs
Summary:        Cryptominisat library

# Cadiback upstream has not tagged any releases, so there is no version number
Provides:       bundled(cadiback)

%description libs
The %{name} library.

%package -n python3-pycryptosat
Summary:        Python 3 interface to %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# This can be removed when F41 reaches EOL
Obsoletes:      python3-%{name} < 5.11.15
Provides:       python3-%{name} = %{version}-%{release}

%description -n python3-pycryptosat
Python 3 interface to %{name}.

%prep
%autosetup -p1 -b1

%conf
# Make cadiback visible to cmake
mv ../cadiback-%{cadicommit} ../cadiback

# Fix install paths
if [ "%{_lib}" != "lib" ]; then
  sed -i 's,${dir}/lib,&64,g' cmake/FindPkgMacros.cmake
  sed -i 's,lib/cmake,%{_lib}/cmake,' CMakeLists.txt
fi

# Defeat attempt to add an rpath
sed -i 's/INSTALL_RPATH_USE_LINK_PATH TRUE//' src/CMakeLists.txt

# Ensure the bundled picosat is not used
rm -fr src/mpicosat

%generate_buildrequires
# Do not confuse pyproject_buildrequires by requiring a python builtin
sed -i 's/, "pathlib"//' pyproject.toml
%pyproject_buildrequires

%build
# Build cadiback first
cd ../cadiback
sed -i '/-d \.git/d;s/^GITID=.*/GITID=%{cadicommit}/' generate
sed -e 's|@COMPILE@|g++ %{build_cxxflags} -fPIC -std=c++17 -DNDEBUG -I%{_includedir}/cadical %{build_ldflags} -Wl,-h,libcadiback.so.0|' \
    -e 's| \.\./cadical/build/libcadical\.a||' \
    -e 's|\.\./cadical/build/libcadical\.so|%{_libdir}/libcadical.so|' \
    -e 's|\.\./cadical/src/cadical\.hpp|%{_includedir}/cadical/cadical.hpp|' \
    makefile.in > makefile
%make_build
mv libcadiback.so libcadiback.so.0.0.0
ln -s libcadiback.so.0.0.0 libcadiback.so.0
ln -s libcadiback.so.0 libcadiback.so
cd -

%cmake \
    -DCMAKE_INSTALL_BINDIR=bin \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DENABLE_ASSERTIONS:BOOL=OFF \
    -DEXTFEAT:BOOL=ON \
    -DNOBREAKID:BOOL=OFF
%cmake_build
%pyproject_wheel

%install
%cmake_install
%pyproject_install
%pyproject_save_files pycryptosat
sed -i '/msvc/d;/oracle/d' \
  %{buildroot}%{python3_sitearch}/pycryptosat-%{version}.dist-info/top_level.txt

# Install cadiback
cd ../cadiback
cp -p libcadiback.so.0.0.0 %{buildroot}%{_libdir}
ln -s libcadiback.so.0.0.0 %{buildroot}%{_libdir}/libcadiback.so.0
ln -s libcadiback.so.0 %{buildroot}%{_libdir}/libcadiback.so
cp -p cadiback.h %{buildroot}%{_includedir}
cd -

# Fix the cmake files
sed -i 's,/builddir.*cadiback/,%{_libdir}/,' %{buildroot}%{_libdir}/cmake/cryptominisat5/cryptominisat5Targets.cmake

%files
%doc README.markdown
%{_bindir}/cryptominisat5
%{_mandir}/man1/cryptominisat5.1*

%files devel
%{_includedir}/cadiback.h
%{_includedir}/cryptominisat5/
%{_libdir}/libcadiback.so
%{_libdir}/libcryptominisat5.so
%{_libdir}/cmake/cryptominisat5/

%files libs
%doc AUTHORS
%license LICENSE.txt
%{_libdir}/libcadiback.so.0*
%{_libdir}/libcryptominisat5.so.5.11

%files -n python3-pycryptosat -f %{pyproject_files}
%doc python/README.md
%exclude %{python3_sitearch}/msvc
%exclude %{python3_sitearch}/oracle

%changelog
%autochangelog
