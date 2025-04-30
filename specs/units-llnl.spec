%global pypi_name units-llnl
%bcond python 1

Name:           units-llnl
Version:        0.13.1
Release:        %{autorelease}
Summary:        LLNL units library

%global forgeurl https://github.com/LLNL/units
%global tag v%{version}
%forgemeta

License:        BSD-3-Clause
# The source tarball includes:
# - header and source file of tinyxml2 (Zlib)
# - header of CLI11 (BSD-3-Clause)
# - header of Niels Lohmann JSON (MIT)
# Of those only the CLI11 header is used in the code of the units_convert
# app. All others are exclusively used for the test suite.
# We remove the shipped CLI11 header and depend on cli11-devel instead.
SourceLicense:  %license AND Zlib AND MIT
URL:            %forgeurl
Source:         %forgesource

BuildRequires:  cmake
BuildRequires:  cmake(cli11)
BuildRequires:  cmake(gtest)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  gcc-c++

%global _description %{expand:
The Units library provides a means of working with units of measurement
at runtime, including conversion to and from strings. It provides a
small number of types for working with units and measurements and
operations necessary for user input and output with units.}

%description %_description


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %_description


%if %{with python}
%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-nanobind-devel

%description -n python3-%{pypi_name} %_description
%endif


%prep
%forgeautosetup -p1

%if %{with python}
# Drop lower bound from nanobind
sed -r -i 's/(nanobind).*[0-9]\.[0-9]\.[0-9]/\1/' pyproject.toml

# Clean up shipped CLI11 header. It is included in converter/converter.cpp
# which is the source for the units_convert app.
# We use the header files from cli11-devel instead.
rm -vf ThirdParty/CLI11.hpp
# Fix the include. CLI11.hpp is a standalone bundle of all header files
# shipped seperately in cli11-devel. Use CLI/CLI.hpp as entry point.
sed -r -i 's|CLI11\.hpp|CLI/CLI.hpp|' converter/converter.cpp


%generate_buildrequires
%pyproject_buildrequires -x test
%endif


%build
%cmake -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
       -DUNITS_BUILD_SHARED_LIBRARY:BOOL=ON \
       -DUNITS_ENABLE_TESTS:BOOL=OFF \
       -DUNITS_BUILD_CONVERTER_APP:BOOL=ON \
       -DUNITS_ENABLE_SUBMODULE_UPDATE:BOOL=OFF \
       -DUNITS_USE_EXTERNAL_GTEST:BOOL=ON

%cmake_build

%if %{with python}
%pyproject_wheel -C cmake.define.UNITS_BUILD_SHARED_LIBRARY:BOOL=ON
%endif


%install
%cmake_install

%if %{with python}
%pyproject_install
%pyproject_save_files -l units_llnl
%endif


%check
%ctest --verbose

%if %{with python}
# Set LD_LIBRARY_PATH since python module needs acces to libunits
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
%pytest -r fEs test/python
%endif


%files
%license LICENSE
%doc NOTICE CONTRIBUTORS.md CONTRIBUTING.md CHANGELOG.md
%{_bindir}/units_convert
%{_libdir}/libunits.so.0{,.*}

%files devel
%{_includedir}/units/
%{_libdir}/cmake/units/
%{_libdir}/libunits.so

%if %{with python}
%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md python/README.md
%endif


%changelog
%autochangelog
