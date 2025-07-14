# header-only library
%global debug_package %{nil}

%bcond tests 1

Name:           valijson
Version:        1.0.6
Release:        %autorelease
Summary:        Header-only JSON Schema validation library for C++11

%global forgeurl0 https://github.com/tristanpenman/valijson
%global forgeurl1 https://github.com/json-schema-org/JSON-Schema-Test-Suite
# Use the same commit upstream uses in the submodule, otherwise some
# tests may fail.
%global tag1 8c3d56df71754e6b1fd4c5e48e93e4047840bbe5
%forgemeta -a

# valijson is distributed under BSD-2-Clause license, except for two
# files which are BSL-1.0:
#   - examples/valijson_nlohmann_bundled.hpp (not shipped)
#   - include/compat/optional.hpp
#     (moved to include/valijson/compat/optional.hpp in %%prep)
# It appears `optional.hpp` is derived/forked from Boost.Optional.
# The test suite (Source1) is MIT, but not shipped with the binary RPM.
License:        BSD-2-Clause AND BSL-1.0
URL:            %forgeurl
Source0:        %forgesource0
Source1:        %forgesource1
# Use system libraries and tools where available.
# Don't use or ship `json11`. It has been retired upstream.
# Downstream only patch
Patch:          thirdparty_cleanup.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with tests}
BuildRequires:  boost-devel
BuildRequires:  cmake(gtest)
BuildRequires:  cmake(jsoncpp)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(pocojson)
BuildRequires:  cmake(qt5core)
BuildRequires:  cmake(rapidjson)
BuildRequires:  cmake(yaml-cpp)
BuildRequires:  picojson-devel
%endif

%global _description %{expand:
Valijson provides a simple validation API that allows you to load JSON
Schemas, and validate documents loaded by one of several supported
parser libraries.

The goal of this project is to support validation of all constraints
available in JSON Schema v7, while being competitive with the
performance of a hand-written schema validator.}

%description %_description

%package devel
Summary:        Header files for %{name}

Requires:       boost-devel
Requires:       cmake(jsoncpp)
Requires:       cmake(nlohmann_json)
Requires:       cmake(pocojson)
Requires:       cmake(qt5core)
Requires:       cmake(rapidjson)
Requires:       cmake(yaml-cpp)
Requires:       picojson-devel

Provides:       valijson-static = %{version}-%{release}

%description devel
%{summary}

%prep
%forgeautosetup -p1

# Move compat/optional.hpp to avoid possible conflict
mv include/compat/ include/valijson/
sed -r 's|compat/optional.hpp|valijson/compat/optional.hpp|' \
    -i include/valijson/internal/optional.hpp

# Remove bundled libs (git submodule stubs)
rm -rfv thirdparty/*

# Remove examples (not shipped)
rm -rv examples/

# Install test data
tar xzf %{SOURCE1} -C thirdparty
mv -v thirdparty/JSON-Schema-Test-Suite-%{tag1}/ thirdparty/JSON-Schema-Test-Suite/

# Remove `json11` headers
rm -v include/valijson/utils/json11_utils.hpp
rm -v include/valijson/adapters/json11_adapter.hpp

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    %{?with_tests:-Dvalijson_BUILD_TESTS:BOOL=ON}
%cmake_build --config Release

%install
%cmake_install

%if %{with tests}
%check
pushd %{_vpath_builddir}
./test_suite
popd
%endif

%files devel
%doc Authors README.md
%license LICENSE
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
