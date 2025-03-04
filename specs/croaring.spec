%global forgeurl https://github.com/RoaringBitmap/CRoaring
Version:        4.3.0
%forgemeta

%global sover 18

Name:           croaring
Release:        %autorelease
Summary:        Roaring bitmaps in C (and C++), with SIMD (AVX2, AVX-512 and NEON) optimizations
License:        Apache-2.0 OR MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libcmocka-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -DROARING_USE_CPM=OFF \
    -DROARING_LIB_VERSION=%{version} \
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libroaring.so.%{sover}
%{_libdir}/libroaring.so.%{version}

%files devel
%{_includedir}/roaring/
%{_libdir}/cmake/roaring/
%{_libdir}/libroaring.so
%{_libdir}/pkgconfig/roaring.pc

%changelog
%autochangelog
