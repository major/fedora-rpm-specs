# We bundle cadiback because it has been modified by the cryptominisat team to
# present a library interface to cryptominisat
%global cadiurl     https://github.com/meelgroup/cadiback
%global cadicommit  35f027383abf3b4b52bbc8af789c8f1aa3d84ad2
%global giturl      https://github.com/msoos/cryptominisat

Name:           cryptominisat
Version:        5.14.5
Release:        %autorelease
Summary:        SAT solver

License:        MIT
URL:            https://www.msoos.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/release/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{cadiurl}/archive/%{cadicommit}/cadiback-%{sub %{cadicommit} 1 7}.tar.gz
# Change the CMake files to not change Fedora build flags
Patch:          %{name}-cmake.patch
# Unbundle picosat
Patch:          %{name}-picosat.patch
# Use zlib-ng instead of zlib
Patch:          %{name}-zlib-ng.patch
# Adapt to a changed function name in breakid 3.1.3
Patch:          %{name}-breakid.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): -Dcadical_DIR:PATH=%{_prefix}
BuildOption(conf): -DBUILD_PYTHON_EXTENSION:BOOL=ON
BuildOption(conf): -DCMAKE_INSTALL_BINDIR=bin
BuildOption(conf): -DCMAKE_INSTALL_LIBDIR=%{_lib}
BuildOption(conf): -DENABLE_ASSERTIONS:BOOL=OFF
BuildOption(conf): -DNOBREAKID:BOOL=OFF

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(breakid)
BuildRequires:  cmake(cadical)
BuildRequires:  gcc-c++
BuildRequires:  gperftools-devel
BuildRequires:  help2man
BuildRequires:  ninja-build
BuildRequires:  picosat-devel
BuildRequires:  pkgconfig(zlib-ng)
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
Requires:       zlib-ng-devel%{?_isa}

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

%description -n python3-pycryptosat
Python 3 interface to %{name}.

%prep
%autosetup -N -n %{name}-release-v%{version} -a1

# Make cadiback visible to cmake
mkdir -p %{_vpath_builddir}
mv cadiback-%{cadicommit} cadiback
sed -i '/CADIBACK_GITID/s/unknown/%{cadicommit}/' cadiback/CMakeLists.txt

# Apply patches after the cadiback rename
%autopatch -p1

# Permit use of cmake 4
%pyproject_patch_dependency cmake:drop_upper

# Do not try to checkout cadiback with git
sed -e '/GIT_REPOSITORY.*cadiback/i\            SOURCE_DIR     ../cadiback)' \
    -e '/GIT_REPOSITORY.*cadiback/,/GIT_SHALLOW/d' \
    -i CMakeLists.txt

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
%pyproject_buildrequires

%conf -p
export CFLAGS='%{build_cflags} -DNTRACING'
export CXXFLAGS='%{build_cxxflags} -DNTRACING'

%install -a
# We don't want the bundled cadiback
rm -fr %{buildroot}%{_includedir}/cadiback
rm -fr %{buildroot}%{_libdir}/cmake/cadiback
rm %{buildroot}%{_libdir}/*.a

# Remove a bogus dependency that leads to cvc5 build failures
sed -i 's/;PkgConfig::GMP//' \
    %{buildroot}%{_libdir}/cmake/cryptominisat5/cryptominisat5Targets.cmake

# The Python interface is installed in the wrong place
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_prefix}/pycryptosat* %{buildroot}%{python3_sitearch}

# Fake some Python metadata
%global metadata %{buildroot}%{python3_sitearch}/pycryptosat-%{version}.dist-info
mkdir -p %{metadata}
cat > %{metadata}/INSTALLER << EOF
rpm
EOF
cat > %{metadata}/METADATA << EOF
Metadata-Version: 2.4
Name: pycryptosat
Version: %{version}
Summary: Bindings to CryptoMiniSat, an advanced SAT solver
Home-page: https://github.com/msoos/cryptominisat
Author-email: Mate Soos <soos.mate@gmail.com>
Maintainer-email: Mate Soos <soos.mate@gmail.com>
License: MIT
Keywords: sat,cryptography
Classifier: Development Status :: 4 - Beta
Classifier: Intended Audience :: Developers
Classifier: Operating System :: OS Independent
Classifier: Programming Language :: C++
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.5
Classifier: License :: OSI Approved :: MIT License
Classifier: Topic :: Utilities
Requires-Python: >=3.5
Description-Content-Type: text/markdown
License-File: LICENSE.txt
License-File: AUTHORS
Dynamic: license-file
EOF
cat > %{metadata}/top_level.txt << EOF
pycryptosat
EOF

# Avoid a name clash
mv %{buildroot}%{_bindir}/oracle %{buildroot}%{_bindir}/cryptominisat5-oracle

%files
%doc README.md
%{_bindir}/cryptominisat5
%{_bindir}/cryptominisat5-oracle
%{_mandir}/man1/cryptominisat5.1*

%files devel
%{_includedir}/cryptominisat5/
%{_includedir}/oracle/
%{_libdir}/libcryptominisat5.so
%{_libdir}/liboracle.so
%{_libdir}/cmake/cryptominisat5/

%files libs
%doc AUTHORS
%license LICENSE.txt
%{_libdir}/libcryptominisat5.so.5.14
%{_libdir}/liboracle.so.5.14

%files -n python3-pycryptosat
%doc python/README.md
%license python/LICENSE
%{python3_sitearch}/pycryptosat.*.so
%{python3_sitearch}/pycryptosat-%{version}.dist-info/

%changelog
%autochangelog
