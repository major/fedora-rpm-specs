%bcond_without check

Name:           blend2d
Version:        0.21.2
Release:        %autorelease
Summary:        2D Vector Graphics Engine Powered by a JIT Compiler

License:        Zlib
URL:            https://blend2d.com/
Source0:        https://blend2d.com/download/blend2d-%{version}.tar.gz

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
%autosetup -n blend2d -p1

sed -i 's/set_target_properties(${target} PROPERTIES/set_target_properties(${target} PROPERTIES SOVERSION 0/' CMakeLists.txt

%build
%cmake \
    -GNinja \
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
%{_includedir}/blend2d/
%{_libdir}/cmake/blend2d/
%{_libdir}/libblend2d.so

%changelog
%autochangelog
