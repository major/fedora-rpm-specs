%global common_description %{expand:
TinyGLTF v3 is a pure C11 implementation of a glTF 2.0 loader and writer,
with an arena-based allocator, structured error reporting, and a custom
locale-independent JSON backend. It has no external dependencies.}

# The devel package ships only headers/source and no compiled binaries, so
# there is nothing for find-debuginfo to generate a debugsource package from
%global debug_package %{nil}

Name:           tinygltf
Version:        3.0.1
Release:        %autorelease
Summary:        C11 tiny glTF 2.0 loader/writer library

License:        MIT
URL:            https://github.com/syoyo/tinygltf
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make

%description    %{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

%description    devel %{common_description}

%prep
%autosetup -p1

# attic/ holds the legacy header-only C++11 implementation plus vendored
# copies of catch.hpp, json.hpp, and stb_image*.h kept by upstream for
# reference only; none of it is used by the C11 v3 build
rm -r attic

%build
%cmake -DTINYGLTF3_BUILD_TESTS=ON -DTINYGLTF3_INSTALL=ON
%cmake_build

%install
%cmake_install

%if %{with tests}
%check
%ctest
%endif

%files devel
%license LICENSE
%doc README.md
%{_includedir}/tiny_gltf_v3.h
%{_includedir}/tiny_gltf_v3.c
%{_includedir}/tinygltf_json_c.h

%changelog
%autochangelog
