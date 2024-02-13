# header-only library
%global debug_package %{nil}

%global forgeurl https://github.com/contour-terminal/boxed-cpp
Version:        1.3.0
%forgemeta

Name:           boxed-cpp
Release:        %autorelease
Summary:        Boxing primitive types in C++

License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
%if 0%{?fedora} >= 39
BuildRequires:  catch-devel
%endif

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if 0%{?fedora} >= 39
    -DBOXED_CPP_TESTS=ON \
%else
    -DBOXED_CPP_TESTS=OFF \
%endif

%cmake_build

%install
%cmake_install

%if 0%{?fedora} >= 39
%check
%ctest
%endif

%files devel
%license LICENSE.txt
%doc README.md
%dir %{_includedir}/boxed-cpp
%{_includedir}/boxed-cpp/boxed.hpp
%{_libdir}/cmake/boxed-cpp/

%changelog
%autochangelog
