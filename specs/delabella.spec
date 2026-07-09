%global commit 0b8d371c28c82492d0a945f535bd7d73c467b630
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260402

Name:     delabella
Version:  2.0^%{commitdate}git%{shortcommit}
Release:  %autorelease
Summary:  2D Delaunay triangulation (dela) - super stable (bella!)
License:  MIT AND BSD-3-Clause
URL:      https://github.com/msokalski/delabella
Source:   %{url}/archive/%{commit}/delabella-%{shortcommit}.tar.gz
Patch0:   include_ctime_sdl2.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: sdl2-compat, sdl2-compat-devel
# bundled package includes modifications from source
Provides:  bundled(GeometricPredicates)

%description
2D Exact Delaunay triangulation

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and static library for delabella.

%prep
%autosetup -n delabella-%{commit} -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

# Compile temporary benchmark binary
%{__cxx} %{optflags} -DBENCH -I.. \
    -o delabella_bench \
    delabella-sdl2.cpp \
    %{buildroot}%{_libdir}/libdelabella.so \
    $(pkg-config --cflags --libs sdl2-compat) \
    -Wl,-rpath,%{buildroot}%{_libdir}

./delabella_bench

if [ ! -f "bench_uni.txt" ]; then
    echo "ERROR: Benchmark failed to generate output."
    exit 1
fi

echo "Benchmark completed successfully."


%files
%doc README.md
%license LICENSE
%{_libdir}/libdelabella.so.2{,.*}

%files devel
%{_includedir}/delabella.h
%{_libdir}/libdelabella.so

%changelog
%autochangelog
