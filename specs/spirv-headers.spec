%global commit a8637796c28386c3cf3b4e8107020fbb52c46f3f
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:           spirv-headers
Version:        1.5.5
Release:        %autorelease
Summary:        Header files from the SPIR-V registry

License:        MIT
URL:            https://github.com/KhronosGroup/SPIRV-Headers/
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# build: Update SPV_INTEL_variable_length_array to rev 3
Patch0:         %url/commit/3397e1e4fe0a9964e1837c2934b81835093494b8.patch

BuildArch:      noarch

BuildRequires:  cmake3
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
%{summary}

This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file

%package        devel
Summary:        Development files for %{name}

%description    devel
%{summary}

This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry fil

%prep
%autosetup -n SPIRV-Headers-%{commit} -p1
chmod a-x include/spirv/1.2/spirv.py


%build
%cmake3 -DCMAKE_INSTALL_LIBDIR=%{_lib} -GNinja
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/spirv/
%{_datadir}/cmake/SPIRV-Headers/*.cmake
%{_datadir}/pkgconfig/SPIRV-Headers.pc

%changelog
%autochangelog
