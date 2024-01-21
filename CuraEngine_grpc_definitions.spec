Name:           CuraEngine_grpc_definitions
Version:        0.1.0
Release:        3%{?dist}
Summary:        gRPC Proto Definitions for CuraEngine
License:        MIT
URL:            https://github.com/Ultimaker/CuraEngine_grpc_definitions
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         CuraEngine_grpc_definitions-installfix.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  grpc-devel
BuildRequires:  asio-grpc-devel
BuildRequires:  protobuf-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  c-ares-devel
BuildRequires:  re2-devel
BuildRequires:  abseil-cpp-devel

%description
This package contains the gRPC proto definitions for CuraEngine. These
definitions are used to generate the gRPC code for the CuraEngine gRPC
plugin system.

%package        devel
Summary:        Development files for CuraEngine_grpc_definitions
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The CuraEngine_grpc_definitions-devel package contains libraries and header
files for developing applications that use CuraEngine_grpc_definitions.

%prep
%autosetup -n %{name}-%{version} -p1

%build
CURAENGINE_PROTOS=`find . |grep "\.proto" | paste -sd ";"`

%cmake -DGRPC_PROTOS="$CURAENGINE_PROTOS"
%cmake_build

%install
%cmake_install

pushd %__cmake_builddir/generated
mkdir -p %{buildroot}%{_includedir}/cura/plugins/
cp -a cura/plugins/* %{buildroot}%{_includedir}/cura/plugins/
popd

%check
# no tests

%files
%license LICENSE
%doc README.md
%{_libdir}/libcuraengine_grpc_definitions.so.*

%files devel
%{_includedir}/cura/plugins
%{_libdir}/libcuraengine_grpc_definitions.so

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Tom Callaway <spot@fedoraproject.org> - 0.1.0-1
- Initial packaging
