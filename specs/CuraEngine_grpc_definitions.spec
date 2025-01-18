Name:           CuraEngine_grpc_definitions
Version:        0.1.0
Release:        9%{?dist}
Summary:        gRPC Proto Definitions for CuraEngine
License:        MIT
URL:            https://github.com/Ultimaker/CuraEngine_grpc_definitions
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         CuraEngine_grpc_definitions-installfix.patch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:    %{ix86}
%endif
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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 15 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1.0-8
- Drop i686 support beginning with Fedora 42 (leaf package)

* Sun Aug 25 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1.0-7
- Rebuilt for abseil-cpp-20240722.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1.0-5
- Rebuilt for abseil-cpp-20240116.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Tom Callaway <spot@fedoraproject.org> - 0.1.0-1
- Initial packaging
