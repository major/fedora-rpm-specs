Name:           units-llnl
Version:        0.13.1
%global soname_version 0
Release:        %autorelease
Summary:        The Units library

# The entire source is BSD-3-Clause, except:
#
# - The source includes a bundled copy of json (nlohmann-json, “JSON for Modern
#   C++”) in ThirdParty/json.hpp. It is MIT and is removed in %%prep, replaced
#   with a dependency on the system json package. Since it’s used only for the
#   tests, its license does not contribute to the licenses of the binary RPMs
#   even though it is header-only.
# - The source includes a bundled copy of tinyxlml2 in ThirdParty/xml/. It is
#   Zlib and is removed in %%prep, replaced with a dependency on the system
#   tinyxml2 package.
#
# Additionally:
#
# - The source includes a bundled copy of CLI11 in ThirdParty/CLI11.hpp. It is
#   is BSD-3-Clause and is removed in %%prep, replaced with a dependency on the
#   system cli11 package. Since this is a header-only library, its license
#   still contributes to the license of the binary RPM containing the
#   command-line tool (that is, the base package). (CLI11 is not used in the
#   shared library.) Since this is the same license as units-llnl itself, this
#   doesn’t end up mattering in practice.
# - Some of the build-system files in ThirdParty/cmake/ have their own license
#   headers; currently, these are all also BSD-3-Clause, and in any case these
#   do not contribute to the licenses of the binary RPMs.
License:        BSD-3-Clause
SourceLicense:  %{license} AND MIT AND Zlib
# While the python3-nanobind package is not a header-only library, it functions
# rather like one, in that it ships C++ sources that are compiled into
# extensions that use it. Furthermore, it brings in an indirect dependency on
# the header-only robin-map library.
#   - python3-nanobind is BSD-3-Clause
#   - robin-map-static is MIT
# Therefore, these licenses also apply to the python3-unit-llnl subpackage.
%global python_license %{license} AND MIT
URL:            https://github.com/LLNL/units
Source0:        %{url}/archive/v%{version}/units-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on --help
Source1:        units_convert.1

# Downstream-only: Use system tinyxml2 for unit tests
#
# Downstream-only because it is much easier to patch this unconditionally
# than to add an option similer to the existing UNITS_USE_EXTERNAL_GTEST
# and make it work properly.
Patch:          0001-Downstream-only-Use-system-tinyxml2-for-unit-tests.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

# Unbundled: for the command-line tool
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  cli11-static

# For tests
BuildRequires:  cmake(gtest)
BuildRequires:  pkgconfig(gmock)
# Unbundled: for tests only
BuildRequires:  json-static
BuildRequires:  tinyxml2-devel

# A Python extension built with nanobind uses the C++ sources shipped inside
# the package, and therefore also the header-only robin-map library. This
# -static dependency is for tracking, required by guidelines.
BuildRequires:  robin-map-static

Requires:       units-llnl-libs%{?_isa} = %{version}-%{release}

%global common_description %{expand:
The Units library provides a means of working with units of measurement at
runtime, including conversion to and from strings. It provides a small number
of types for working with units and measurements and operations necessary for
user input and output with units.}

%description %{common_description}


%package libs
Summary:        Shared libraries for units-llnl

%description libs %{common_description}


%package devel
Summary:        Development files for units-llnl
Requires:       units-llnl-libs%{?_isa} = %{version}-%{release}

%description devel %{common_description}


%package -n python3-units-llnl
Summary:        %{summary}
License:        %{python_license}

Requires:       units-llnl-libs%{?_isa} = %{version}-%{release}

%description -n python3-units-llnl %{common_description}


%prep
%autosetup -C -p1

# Unbundle cli11 by replacing the bundled single-header library with a trivial
# header that re-includes the system copy.
printf '#include <%s>\n' 'CLI/CLI.hpp' > ThirdParty/CLI11.hpp

# This should be empty (it’s a git submodule), but let’s make sure:
rm --recursive --verbose ThirdParty/googletest

# Unbundle tinyxml2
rm --recursive --verbose ThirdParty/xml

# Unbundle json (nlohmann-json, “JSON for Modern C++”) by replacing the bundled
# single-header amalgamated copy of the library with a trivial header that
# re-includes the system copy.
printf '#include <%s>\n' 'nlohmann/json.hpp' > ThirdParty/json.hpp

# Did we miss anything? All that remains in ThirdParty/ should be .cmake
# build-system files and headers that we have replaced above.
[ -z "$(
  find ThirdParty/ -type f ! -name '*.cmake' ! -name CLI11.hpp ! -name json.hpp
)" ]


%generate_buildrequires
%pyproject_buildrequires --extras=test


%conf
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DUNITS_BUILD_SHARED_LIBRARY:BOOL=ON \
    -DUNITS_ENABLE_TESTS:BOOL=ON \
    -DUNITS_BUILD_CONVERTER_APP:BOOL=ON \
    -DUNITS_ENABLE_SUBMODULE_UPDATE:BOOL=OFF \
    -DUNITS_USE_EXTERNAL_GTEST:BOOL=ON


%build
%cmake_build

# https://scikit-build-core.readthedocs.io/en/latest/configuration/index.html
%{pyproject_wheel %{shrink:
    --config-settings=cmake.build-type=RelWithDebInfo
    --config-settings=cmake.define.UNITS_BUILD_SHARED_LIBRARY:BOOL=ON
    --config-settings=cmake.define.UNITS_ENABLE_SUBMODULE_UPDATE:BOOL=OFF
    --config-settings=logging.level=INFO
    --config-settings=build.verbose=true
    }}


%install
%cmake_install

%pyproject_install
%pyproject_save_files --assert-license units_llnl

install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_mandir}/man1' '%{SOURCE1}'


%check
%ctest --verbose

export LD_LIBRARY_PATH='%{buildroot}%{_libdir}'
%pyproject_check_import
%pytest -rs --verbose test/python


%files
%{_bindir}/units_convert
%{_mandir}/man1/units_convert.1*


%files libs
%license LICENSE
%license NOTICE
%doc CONTRIBUTORS.md
%doc CHANGELOG.md

%{_libdir}/libunits.so.%{soname_version}{,.*}


%files devel
%{_includedir}/units/
%{_libdir}/cmake/units/
%{_libdir}/libunits.so


%files -n python3-units-llnl -f %{pyproject_files}
%doc python/README.md


%changelog
%autochangelog
