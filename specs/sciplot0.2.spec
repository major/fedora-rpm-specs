%global debug_package %{nil}
%global forgeurl https://github.com/sciplot/sciplot

%global common_description %{expand:
The goal of the sciplot project is to enable a C++ programmer to conveniently
plot beautiful graphs as easy as in other high-level programming languages.
sciplot is a header-only library that needs a C++17-capable compiler, but has
no external dependencies for compiling.}

Name:           sciplot0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Modern C++ scientific plotting library (0.2 compatibility package)

# tests/catch.hpp is Boost Software License 1.0
License:        MIT and BSL-1.0
URL:            https://sciplot.github.io/
Source:         %{forgeurl}/archive/v%{version}/sciplot-%{version}.tar.gz
# Enable testing with CMake and ctest
# https://github.com/sciplot/sciplot/pull/115
Patch0:         %{forgeurl}/pull/115.patch
# Update catch.hpp header for tests
# https://github.com/sciplot/sciplot/a7dd232928dbb4205f281112c43019ef32dfbbd6
Patch1:         %{forgeurl}/commit/a7dd232928dbb4205f281112c43019ef32dfbbd6.patch


BuildRequires:  cmake
BuildRequires:  gcc-c++

%description    %{common_description}

%package        devel
Summary:        %{summary}
Conflicts:      sciplot-devel

%description    devel %{common_description}

%prep
%autosetup -p1 -n sciplot-%{version}

# Fix permissions
chmod -x LICENSE README.md

%build
%cmake \
    -DSCIPLOT_BUILD_DOCS=OFF \
    -DSCIPLOT_BUILD_EXAMPLES=OFF \
    -DSCIPLOT_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/sciplot/
%{_datadir}/sciplot/

%changelog
%autochangelog
