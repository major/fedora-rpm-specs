# Whether to run tests
%bcond ctest 1

# We need the MNX schema, which is not suitable for packaging
# The required commit is in cmake/MnxW3C.cmake
%global mnxurl  https://github.com/w3c-cg/mnx
%global commit  d513cf7a28a84c803ed36e448b416cb49c3a22f9
%global shortc  %{sub %{commit} 1 7}

%global giturl  https://github.com/rpatters1/mnxdom

Name:           mnxdom
Version:        3.0
Release:        %autorelease
Summary:        Music Notation Interchange Document Object Model for C++17

# The entire source is MIT; the header-only json library dependency is
# (MIT AND CC0-1.0), where the CC0-1.0 comes from bundled hedley.
# The MNX Schema is W3C.
License:        MIT AND W3C AND CC0-1.0
# Source0 is MIT.  Source1 is W3C.
SourceLicense:  MIT AND W3C
URL:            https://rpatters1.github.io/mnxdom/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{mnxurl}/archive/%{commit}/mnx-%{shortc}.tar.gz
# Give the shared library an soname
Patch:          %{name}-soname.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
%if %{without ctest}
BuildOption(conf): -Dmnxdom_BUILD_TESTING:BOOL=OFF
%endif
BuildOption(conf): -DMNX_W3C_SOURCE:PATH=$PWD/mnx-%{commit}
BuildOption(conf): -DUSE_SYSTEM_GOOGLETEST:BOOL=ON
BuildOption(conf): -DUSE_SYSTEM_JSON_SCHEMA_VALIDATOR:BOOL=ON
BuildOption(conf): -DUSE_SYSTEM_NLOHMANN_JSON:BOOL=ON

%if %{with ctest}
BuildRequires:  cmake(GTest)
%endif
BuildRequires:  cmake(nlohmann_json_schema_validator)
BuildRequires:  gcc-c++
BuildRequires:  json-static
BuildRequires:  xxd

%description
Document object model for the MNX music interchange format.  It is compatible
with the C++17 standard.

- compatible with the C++17 standard and higher (currently tested with C++23)
- uses nlohmann_json as its JSON parser
- allows structured access to MNX objects, without the need of quoted strings
- validates against the MNX schema using json-schema-validator
- no class serialization beyond nlohmann
- every MNX class is a wrapper around the root JSON object and a pointer to
  the location of the instance

%package        devel
Summary:        Development files for mnxdom
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and library links for developing applications that use %{name}.

%prep
%autosetup -a1

%files
%doc README.md
%license LICENSE
%{_libdir}/libmnxdom.so.0{,.*}

%files devel
%{_includedir}/mnxdom/
%{_libdir}/libmnxdom.so
%{_libdir}/pkgconfig/mnxdom.pc

%changelog
%autochangelog
