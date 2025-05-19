%global commit 4816a508f696dc9aff65e7ae5fd250b5e3585cb2
%global snapdate 20250517

Name:           xxhashct
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/#_upstream_has_never_chosen_a_version
Version:        0^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Compile-time xxhash implementation

License:        MIT
URL:            https://github.com/ekpyron/xxhashct
Source:         %{url}/archive/%{commit}/xxhashct-%{commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
# For tests:
BuildRequires:  xxhash-devel

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
An implementation of the 64-bit xxhash algorithm (see
https://github.com/Cyan4973/xxHash) as C++11 constexpr expression.}

%description %{common_description}


%package devel
Summary:        Development files for xxhashct

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_use_noarch_only_in_subpackages
BuildArch:      noarch

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       xxhashct-static = %{version}-%{release}

%description devel %{common_description}

The xxhashct-devel package contains libraries and header files for developing
applications that use xxhashct.


%prep
%autosetup -n xxhashct-%{commit} -p1


%conf
%cmake


%build
%cmake_build


%install
# The upstream CMake build system only builds tests.
install -D -p -m 0644 -t '%{buildroot}%{_includedir}' xxh32.hpp xxh64.hpp


%check
# The test executable is not set up for use with CTest; run it directly.
%{_vpath_builddir}/xxhashct_tests


%files devel
%license LICENSE
%doc README.md

%{_includedir}/xxh32.hpp
%{_includedir}/xxh64.hpp


%changelog
%autochangelog
