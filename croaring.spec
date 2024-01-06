%global forgeurl https://github.com/RoaringBitmap/CRoaring
Version:        2.1.2
%forgemeta

Name:           croaring
Release:        %autorelease
Summary:        Roaring bitmaps in C (and C++), with SIMD (AVX2, AVX-512 and NEON) optimizations
License:        Apache-2.0 OR MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  libcmocka-devel

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DROARING_USE_CPM=OFF \

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libroaring.so.14
%{_libdir}/libroaring.so.%{version}

%files devel
%{_includedir}/roaring/
%{_libdir}/cmake/roaring/
%{_libdir}/libroaring.so
%{_libdir}/pkgconfig/roaring.pc

%changelog
%autochangelog
