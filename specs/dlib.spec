%global forgeurl https://github.com/davisking/dlib

# Compiling and running tests takes quite long and is resource intensive.
# Turn them off using `--without ctest`.
%bcond ctest 1

Name:       dlib
Version:    19.24.8
Release:    %autorelease
Summary:    A modern C++ toolkit containing machine learning algorithms
%forgemeta
License:    BSL-1.0
URL:        http://dlib.net
Source:     %forgesource
# Fix build issue with GCC 15
Patch:      https://github.com/davisking/dlib/pull/3067.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(pybind11)
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  pkgconfig(fftw3)
# BLAS and LAPACK support
# We need to depend on `flexiblas` rather than `cblas` and `lapack`
# https://docs.fedoraproject.org/en-US/packaging-guidelines/BLAS_LAPACK/
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(more-itertools)
BuildRequires:  time

# Stop building for i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# While fix_aarch64.patch (see above) also fixes the s390x build of tests,
# running those tests results in lots of failures and even coredumps.
ExcludeArch:    %{ix86} s390x

%description
Dlib is a general purpose cross-platform open source software library written
in the C++ programming language. Its design is heavily influenced by ideas from
design by contract and component-based software engineering. It contains
components for dealing with networking, threads, graphical user interfaces,
data structures, linear algebra, machine learning, image processing, data
mining, XML and text parsing, numerical optimization, Bayesian networks, and
numerous other tasks.


%package devel
Summary:    Development files for dlib
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Dlib is a general purpose cross-platform open source software library written
in the C++ programming language. This package contains development files for
the library.


%package -n python3-%{name}
Summary:    Python 3 interface to %{name}

%description -n python3-%{name}
Dlib is a general purpose cross-platform open source software library written
in the C++ programming language. This package contains Python 3 API for the
library.


%package doc
Summary:    Documentation for dlib
License:    CC0-1.0 AND CC-BY-SA-3.0
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description doc
Dlib is a general purpose cross-platform open source software library written
in the C++ programming language. This package contains the library
documentation and examples.


%prep
%forgeautosetup -p1

find docs -type f -exec chmod 644 {} +
find examples -type f -exec chmod 644 {} +

# Remove empty files
find docs/docs -size 0 -print -delete

# Move license files out of examples
mv -v examples/LICENSE_FOR_EXAMPLE_PROGRAMS.txt .
mv -v examples/video_frames/license.txt video_frames_license.txt

# unbundle pybind11, see https://bugzilla.redhat.com/2098694
rm -r dlib/external/pybind11
sed -i 's@add_subdirectory(../../dlib/external/pybind11 pybind11_build)@find_package(pybind11 CONFIG)@' tools/python/CMakeLists.txt

# Do not treat warnings as errors when compiling tests
sed -r -i 's/[[:space:]]+-Werror//' dlib/test/CMakeLists.txt


%generate_buildrequires
%pyproject_buildrequires


%build
# dlib requires `libjxl_cms` provided by libjxl >= 0.10` currently only
# available in rawhide (F41)
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DDLIB_USE_CUDA:BOOL=OFF \
%if 0%{?fedora} >= 41
  -DDLIB_JXL_SUPPORT:BOOL=ON
%else
  -DDLIB_JXL_SUPPORT:BOOL=OFF
%endif
%cmake_build

%if %{with ctest}
# Use `-O` instead of `-O2`. Reduces max memory for single thread from
# 17GB to 12GB. It also reduces time to build.
# Also reduce debuginfo using `-g1` instead of `-g` (aka `-g2`).
# Memory consumption drops further to ~6GiB and build speeds up again.
CXXFLAGS="${CXXFLAGS/-O2/-O}"
CXXFLAGS="${CXXFLAGS/-g /-g1 }"

# Unit tests
#
# On small builders (~15GiB) the build fails running out of memory.
# With a few tweaks memory consumption peaks at just over 6GiB.
# Constrain the build to 7GiB per core.
#
# RHEL doesn't support `%%constrain_build` nor `%%{limit_build ...}`.

MAX_CPUS="$(($(cat /proc/meminfo | grep MemTotal | awk '{print $2}') / $((7168 * 1024))))"
%global _smp_mflags "-j${MAX_CPUS}"

pushd dlib/test
%cmake \
  -DDLIB_USE_CUDA:BOOL=OFF \
%if 0%{?fedora} >= 41
  -DDLIB_JXL_SUPPORT:BOOL=ON
%else
  -DDLIB_JXL_SUPPORT:BOOL=OFF
%endif
%cmake_build
popd
%endif

%pyproject_wheel


%install
%cmake_install

%pyproject_install
%pyproject_save_files %{?fedora:-l} %{name}

find %{buildroot} -name '.*' -exec rm -rf {} +


%check
%if %{with ctest}
pushd dlib/test/redhat-linux-build
# tests can be disabled using `--no_${TEST}` with --runall or
# enabled `--${TEST}` without it. `-h` shows all tests.
# test_ffmpeg fails
./dtest --runall --no_test_ffmpeg
popd
%endif
%pytest -v


%files
%license LICENSE.txt
%{_libdir}/libdlib.so.19*

%files devel
%{_libdir}/libdlib.so
%{_includedir}/dlib/
%{_libdir}/cmake/dlib/
%{_libdir}/pkgconfig/*.pc

%files -n python3-%{name} -f %{pyproject_files}
%{python3_sitearch}/_%{name}_pybind11%{python3_ext_suffix}
%doc README.md

%files doc
%doc docs/docs/
%doc examples
%license LICENSE_FOR_EXAMPLE_PROGRAMS.txt
%license video_frames_license.txt


%changelog
%autochangelog
