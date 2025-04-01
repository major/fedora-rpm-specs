# https://github.com/syoyo/tinygltf/issues/484
%ifarch ppc64le s390x
%bcond tests 0
%else
%bcond tests 1
%endif

%global common_description %{expand:
TinyGLTF is a header only C++11 glTF 2.0 library.}

Name:           tinygltf
Version:        2.9.5
Release:        %autorelease
Summary:        Header only C++11 tiny glTF 2.0 library

License:        MIT
URL:            https://github.com/syoyo/tinygltf
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  catch1-devel
BuildRequires:  json-devel
BuildRequires:  stb_image-devel
BuildRequires:  stb_image_write-devel

%description    %{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
Requires:       cmake-filesystem

%description    devel %{common_description}

%package        examples
Summary:        Examples for %{name}

%description    examples %{common_description}

This package provides examples exercising %{name}.

%prep
%autosetup -p1

# Replace bundled headers with system versions
ln -sf %{_includedir}/catch/catch.hpp tests/
rm json.hpp stb_image.h stb_image_write.h tests/catch.hpp
sed -i CMakeLists.txt \
  -e '/json.hpp/d' \
  -e '/stb_image.h/d' \
  -e '/stb_image_write.h/d'
sed -i tiny_gltf.h tests/tester.cc \
  -e 's:#include "catch.hpp":#include <catch/catch.hpp>:' \
  -e 's:#include "json.hpp":#include <nlohmann/json.hpp>:' \
  -e 's:#include "stb_image.h":#include <stb_image.h>:' \
  -e 's:#include "stb_image_write.h":#include <stb_image_write.h>:'

# The examples bundle a slew of third party libraries; these aren't built by
# default, so we just clobber them for now instead of unbundling
rm -r examples

# Drop unused bundled deps
rm -r deps tools

# Use our compiler and build flags to build the tests
sed -i tests/Makefile \
  -e 's:clang++:%{__cxx}:g' \
  -e 's:-O0:%{build_cxxflags} %{build_ldflags}:g'

%build
%cmake -DTINYGLTF_HEADER_ONLY=ON
%cmake_build
%make_build -C tests

%install
%cmake_install

# Install the examples
install -Dpm0755 %{_vpath_builddir}/loader_example \
  %{buildroot}%{_bindir}/%{name}_loader_example

%if %{with tests}
%check
for t in tester tester_noexcept; do
  echo "Running $t"
  (cd tests && ./"$t")
done
%endif

%files devel
%license LICENSE
%doc README.md
%{_includedir}/tiny_gltf.h
%{_libdir}/cmake/%{name}/

%files examples
%license LICENSE
%{_bindir}/%{name}_loader_example

%changelog
%autochangelog
