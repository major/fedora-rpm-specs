%bcond_without check

%global forgeurl https://github.com/blend2d/blend2d
%global date 20240224
%global commit 5a263ce51f3f880ee6c60f6345d18c3eccbe200f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           blend2d
Version:        0.10.6
Release:        %autorelease
Summary:        2D Vector Graphics Engine Powered by a JIT Compiler

%forgemeta

License:        Zlib
URL:            %{forgeurl}
Source0:        %{forgesource}

# Fix build on big endian systems
Patch0:         https://github.com/blend2d/blend2d/pull/197.patch
# [Bug] Fixed PRGB32->A8 conversion on big endian targets
Patch1:         https://github.com/blend2d/blend2d/commit/e4656f4317b79891c85865023039507db142e6d3.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

%description
Blend2D is a high performance 2D vector graphics engine written in C++ and
released under the Zlib license. The engine utilizes a built-in JIT compiler to
generate optimized pipelines at runtime and is capable of using multiple threads
to boost the performance beyond the possibilities of single-threaded rendering.
Additionally, the engine features a new rasterizer that has been written from
scratch. It delivers superior performance while quality is comparable to
rasterizers used by AGG, FreeType, and Qt. The performance has been optimized by
using an innovative approach to index data that is built during rasterization
and scanned during composition. The rasterizer is robust and excels in rendering
basic shapes, complex vector art, and text.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

sed -i 's/set_target_properties(${target} PROPERTIES DEFINE_SYMBOL "")/set_target_properties(${target} PROPERTIES SOVERSION 0 DEFINE_SYMBOL "")/' CMakeLists.txt

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBLEND2D_NO_JIT=ON \
%if %{with check}
    -DBLEND2D_TEST=ON \
%endif

%cmake_build

%install
%cmake_install

%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libblend2d.so.0

%files devel
%{_includedir}/blend2d-debug.h
%{_includedir}/blend2d-impl.h
%{_includedir}/blend2d.h
%{_includedir}/blend2d/
%{_libdir}/cmake/blend2d/
%{_libdir}/libblend2d.so

%changelog
%autochangelog
