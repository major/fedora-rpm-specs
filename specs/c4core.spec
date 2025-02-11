# Upstream defaults to C++11, but recommends building c4core and rapidyaml with
# the same standard; and rapidyaml is built as C++14 because gtest 1.13.0 or
# later requires C++14 or later. See:
# https://github.com/biojppm/rapidyaml/issues/465#issuecomment-2307668270
%global cxx_std 14

Name:           c4core
Summary:        C++ core utilities
Version:        0.2.3
# This is the same as the version number. To prevent undetected soversion
# bumps, we nevertheless express it separately.
%global so_version 0.2.3
Release:        %autorelease

URL:            https://github.com/biojppm/c4core
# The entire source is MIT, except:
#
# BSL-1.0:
#   - src/c4/ext/sg14/inplace_function.h
SourceLicense:  MIT AND BSL-1.0
# Additionally, the following dependencies contribute to the License of the
# binary RPMs because they are header-only and are therefore treated as static
# libraries:
#   - debugbreak is BSD-2-Clause
#   - fast-float (5.0+) is Apache-2.0 OR MIT OR BSL-1.0
# The doctest-static BR is used only for tests and does not contribute to the
# binary RPMs.
License:        %{shrink:
                MIT AND
                BSL-1.0 AND
                BSD-2-Clause AND
                (Apache-2.0 OR MIT OR BSL-1.0)
                }
Source:         %{url}/archive/v%{version}/c4core-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  c4project
# Our choice; the default make backend should work just as well
BuildRequires:  ninja-build

# For each header-only library, the guidelines require us to BR the -static
# package for tracking.
BuildRequires:  debugbreak-static
BuildRequires:  fast_float-static
BuildRequires:  doctest-static

%global common_description %{expand:
c4core is a library of low-level C++ utilities, written with low-latency
projects in mind.

Some of the utilities provided by c4core have already equivalent functionality
in the C++ standard, but they are provided as the existing C++ equivalent may
be insufficient (e.g., std::string_view), inefficient (e.g., std::string),
heavy (e.g. streams), or plainly unusable on some platforms/projects, (e.g.
exceptions); some other utilities have equivalent under consideration for C++
standardization; and yet some other utilities have (to the author’s knowledge)
no equivalent under consideration.}

%description %{common_description}


%package devel
Summary:        %{summary}

Requires:       %{name}%{?_isa} = %{version}-%{release}

# Each of these header-only libraries is made available under c4/ext/… in the
# API of this package. Dependent packages that use them should really have
# BuildRequires on the corresponding -static packages for header-only package
# tracking.
Requires:       debugbreak-devel
Requires:       fast_float-devel

# The bundled copy was forked from the original header-only library published
# as a gist at
# https://gist.github.com/Leandros/6dc334c22db135b033b57e9ee0311553 (see also
# the blog post at https://arvid.io/2018/07/02/better-cxx-prng/). The original
# was never versioned, but only one revision was ever published, so we can
# infer the commit hash (6dc334c22db135b033b57e9ee0311553) from which the
# bundled copy was forked and assign a snapshot version.
Provides:       bundled(ag-random) = 0^20180702git6dc334c
# One header is bundled from https://github.com/WG21-SG14/SG14/ (commit
# 3aeb80676ff3e7a974678bd3fd826ffe55a0c4ab), which has never been versioned and
# is not currently suitable to be packaged in its entirety—if nothing else, due
# to unresolved licensing in some of its other source files that are not
# bundled here, https://github.com/WG21-SG14/SG14/issues/163.
Provides:       bundled(SG14) = 0^20190524git3a3b806

%description devel %{common_description}


%prep
%autosetup -n c4core-%{version}

# Remove/unbundle additional dependencies

# c4project (CMake build scripts)
rm -rvf cmake
ln -s '%{_datadir}/cmake/c4project' cmake

# Do not try to link against a nonexistent doctest library (doctest is
# header-only, and we do not have the complete CMake project for doctest that
# would provide a target that knows this):
sed -r -i \
    -e 's/(LIBS.*)\bdoctest\b/\1/' \
    -e 's/(c4_setup_testing\()DOCTEST\)/\1\)/' \
    test/CMakeLists.txt

# Normally, in releases, the “current.md” changelog file is empty and
# zero-length. When this is true, we remove it so it is not packaged.
if [ "$(stat -c '%s' changelog/current.md)" = '0' ]
then
  rm -vf changelog/current.md
fi

# debugbreak
rm -rvf src/c4/ext/debugbreak
mkdir src/c4/ext/debugbreak
ln -sv %{_includedir}/debugbreak.h src/c4/ext/debugbreak/

# fast_float
#
# The build system expects to produce an amalgamated header, fast_float_all.h,
# from the bundled fast_float. We therefore use a symbolic link to preserve the
# original bundled header path. The amalgamated header will be produced from
# the *system* fast_float headers. Once the amalgamated header is produced, we
# again replace it with a symbolic link to the main system fast_float header,
# thereby fully unbundling fast_float.
rm -rv src/c4/ext/fast_float
mkdir -p src/c4/ext/fast_float/include
ln -sv %{_includedir}/fast_float src/c4/ext/fast_float/include/
# Replace amalgamated single-file header produced by build system with one that
# trivially includes the main system fast_float header.
cat > src/c4/ext/fast_float_all.h <<EOF
#include <fast_float/fast_float.h>
EOF


%conf
# We can stop the CMake scripts from downloading doctest by setting
# C4CORE_CACHE_DOWNLOAD_DOCTEST to any directory that exists.
%cmake -GNinja \
  -DCMAKE_CXX_STANDARD=%{cxx_std} \
  -DC4CORE_CACHE_DOWNLOAD_DOCTEST:PATH=/ \
  -DC4CORE_BUILD_TESTS=ON


%build
%cmake_build


%install
%cmake_install
# Fix wrong installation paths for multilib; it would be nontrivial to patch
# the source to get this right in the first place. The installation path is
# determined by the scripts in https://github.com/biojppm/cmake, packaged as
# c4project.
#
# Installation directory on Linux 64bit OS
# https://github.com/biojppm/rapidyaml/issues/256
if [ '%{_libdir}' != '%{_prefix}/lib' ]
then
  mkdir -p '%{buildroot}%{_libdir}'
  mv -v %{buildroot}%{_prefix}/lib/libc4core.so* '%{buildroot}%{_libdir}/'
  mkdir -p '%{buildroot}%{_libdir}/cmake'
  mv -v %{buildroot}%{_prefix}/lib/cmake/c4core '%{buildroot}%{_libdir}/cmake/'
  find %{buildroot}%{_libdir}/cmake/c4core -type f -name '*.cmake' -print0 |
    xargs -r -t -0 sed -r -i "s@/lib/@/$(basename '%{_libdir}')/@"
fi

# Some unbundled header-only libraries that appear in the API may have had
# their symlinks dereferenced during installation. Make sure they aren’t
# “re-bundled” as a result.

# debugbreak
ln -svf '%{_includedir}/debugbreak.h' \
    '%{buildroot}%{_includedir}/c4/ext/debugbreak/'


%check
%cmake_build --target c4core-test-run-verbose

# Verify that we did not accidentally bundle a real copy of fast_float
if grep -F 'FASTFLOAT_' \
    '%{buildroot}%{_includedir}/c4/ext/fast_float_all.h' >/dev/null
then
  echo 'Unwanted bundling of fast_float was detected!' 1>&2
  exit 1
fi


%files
%license LICENSE.txt LICENSE-BOOST.txt
%doc README.md
%doc ROADMAP.md
%doc changelog/
%{_libdir}/libc4core.so.%{so_version}


%files devel
%{_includedir}/c4/
%{_libdir}/libc4core.so
%{_libdir}/cmake/c4core/


%changelog
%autochangelog
