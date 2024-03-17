%global debug_package %{nil}

Name: semver
Version: 0.3.1
Release: %autorelease

License: MIT
Summary: Semantic Versioning for modern C++
URL: https://github.com/Neargye/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

# semver currently support only catch v2
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10
BuildRequires: catch2-devel
%else
BuildRequires: catch-devel
%endif

%description
C++ library compare and manipulate versions are available as extensions to the
<major>.<minor>.<patch>-<prerelease_type>.<prerelease_number> format complying
with Semantic Versioning 2.0.0.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1

# Unbundling catch...
rm -rf test/3rdparty/Catch2
ln -svf %{_includedir}/catch2 test/3rdparty/Catch2

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DSEMVER_OPT_BUILD_EXAMPLES:BOOL=ON \
    -DSEMVER_OPT_BUILD_TESTS:BOOL=ON \
    -DSEMVER_OPT_INSTALL:BOOL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
