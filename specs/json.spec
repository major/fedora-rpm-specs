%global debug_package %{nil}
%global test_data_version 3.1.0
%global bundled_hedley_version 15

Name:           json
Version:        3.12.0
Release:        %autorelease

# The entire source is MIT except
# include/nlohmann/thirdparty/hedley/hedley.hpp, which is CC0-1.0
License:        MIT AND CC0-1.0
Summary:        JSON for Modern C++
URL:            https://github.com/nlohmann/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/nlohmann/json_test_data/archive/v%{test_data_version}/json_test_data-%{test_data_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

# Build requirements for the tests.
BuildRequires:  doctest-devel
BuildRequires:  gawk

%description
This is a packages version of the nlohmann/json header-only C++
library available at Github.

%package devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
# This package is also known as nlohmann-json, provide some alternate names
# to make it easier to find
Provides:       nlohmann-json-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       nlohmann-json-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       nlohmann_json-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       nlohmann_json-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(hedley) = %{bundled_hedley_version}
Requires:       libstdc++-devel%{?_isa}

%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%prep
%autosetup -p1
%setup -q -D -T -a1

# Unbundle doctest. Used only in tests.
ln -svf %{_includedir}/doctest/doctest.h ./tests/thirdparty/doctest/doctest.h

%build
%cmake -G Ninja \
    -DJSON_BuildTests:BOOL=ON \
    -DJSON_Install:BOOL=ON \
    -DJSON_MultipleHeaders:BOOL=ON \
    -DJSON_TestDataDirectory:STRING=json_test_data-%{test_data_version} \
%cmake_build

%check
%ctest --label-exclude 'git_required' --timeout 3600

# Verify version of virtual Provides for bundled Hedley matches actual header
[ "$(awk '
/^[[:blank:]]*#[[:blank:]]*define[[:blank:]]+JSON_HEDLEY_VERSION[[:blank:]]/ {
  print $NF }' include/nlohmann/thirdparty/hedley/hedley.hpp
)" = '%{bundled_hedley_version}' ]

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE.MIT
%{_includedir}/nlohmann/
%{_datadir}/cmake/nlohmann_json/
%{_datadir}/pkgconfig/nlohmann_json.pc

%changelog
%autochangelog
