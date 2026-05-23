# Whether to run tests
%bcond ctest 1

Name:           json-schema-validator
Version:        2.4.0
Release:        %autorelease
Summary:        Modern C++ JSON schema validator

# The entire source is MIT; the header-only json library dependency is
# (MIT AND CC0-1.0), where the CC0-1.0 comes from bundled hedley.
License:        MIT AND CC0-1.0
SourceLicense:  MIT
URL:            https://github.com/pboettch/json-schema-validator
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix a test failure on platforms where char is unsigned
Patch:          %{url}/pull/376.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): -DJSON_VALIDATOR_BUILD_EXAMPLES:BOOL=OFF

BuildRequires:  gcc-c++
BuildRequires:  json-static

# src/smtp-address-validator.cpp is derived from
# https://github.com/gene-hightower/smtp-address-validator
Provides:       bundled(smtp-address-validator)

%description
This is a C++ library for validating JSON documents based on a JSON Schema
which itself should validate with draft-7 of JSON Schema Validation.

%package        devel
Summary:        Development files for json-schema-validator
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       json-devel%{?_isa}

%description    devel
Header files and library links for developing applications that use
%{name}.

%prep
%autosetup -p1

%files
%doc ChangeLog.md README.md
%license LICENSE
%{_libdir}/libnlohmann_json_schema_validator.so.2{,.*}

%files devel
%doc example/
%{_includedir}/nlohmann/json-schema.hpp
%{_libdir}/cmake/nlohmann_json_schema_validator/
%{_libdir}/libnlohmann_json_schema_validator.so

%changelog
%autochangelog
