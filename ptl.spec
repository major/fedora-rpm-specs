%global forgeurl https://github.com/jrmadsen/PTL
Version:        2.3.3
%global date 20230707
%global commit f892a93d79615ed8f51c1b9c71f0f7b771dd8223
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta

Name:           ptl
Release:        %autorelease
Summary:        Lightweight C++11 mutilthreading tasking system
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  tbb-devel

%description
Parallel Tasking Library (PTL) is a lightweight C++11 multithreading tasking
system featuring thread-pool, task-groups, and lock-free task queue.

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
    -DBUILD_STATIC_LIBS=OFF \
    -DPTL_USE_TBB=ON \

%cmake_build

%install
%cmake_install

%check

%files
%license LICENSE
%doc README.md
%{_libdir}/libptl.so.3*

%files devel
%{_libdir}/libptl.so
%{_includedir}/PTL/
%{_libdir}/cmake/PTL/
%{_libdir}/pkgconfig/ptl.pc

%changelog
%autochangelog
