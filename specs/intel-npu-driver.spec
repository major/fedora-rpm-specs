%global desc %{expand: \
Intel NPU device is an AI inference accelerator integrated with Intel client
CPUs, starting from Intel Core Ultra generation of CPUs (formerly known as
Meteor Lake). It enables energy-efficient execution of artificial neural
network tasks.}

Name:		intel-npu-driver
Version:	1.16.0
Release:	%autorelease
Summary:	Intel Neural Processing Unit Driver

License:	MIT AND Apache-2.0
URL:		https://github.com/intel/linux-npu-driver
Source0:	%url/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/intel/level-zero-npu-extensions/archive/c0156a3390ae39671ff8f2a6f5471f04bb65bb12/level-zero-npu-extensions-c0156a3.tar.gz
Source2:	https://github.com/openvinotoolkit/npu_plugin_elf/archive/ce501d3059c81fd6bd0ad7165ab823838fa5d851/npu_plugin_elf-ce501d3.tar.gz

Patch0:		npu-driver-fedora.patch

ExclusiveArch:	x86_64

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
BuildRequires:	libudev-devel
BuildRequires:	oneapi-level-zero-devel
BuildRequires:	openssl-devel
BuildRequires:	yaml-cpp-devel
# openvino-npu_plugin_elf
Provides:	bundled(openvino-npu_plugin_elf)
# level-zero-npu-extensions
Provides:	bundled(level-zero-npu-extensions)
Requires:	oneapi-level-zero

%description
%{desc}

%package test
Summary:	Test files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description test
The %{name}-test package contains kernel-mode (kmd) and user-mode (umd)
parts of the %{name}.

%prep
%autosetup -N -n linux-npu-driver-%{version}

# thirdparty deps
rm -rf thirdparty/googletest thirdparty/level-zero third_party/level-zero-npu-extensions thirdparty/perfetto thirdparty/yaml-cpp third_party/vpux_elf
tar xf %{SOURCE1}
mv level-zero-npu-extensions-* third_party/level-zero-npu-extensions
tar xf %{SOURCE2}
mv npu_plugin_elf-* third_party/vpux_elf

%autopatch -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DUSE_SYSTEM_LIBRARIES=ON \
	-DENABLE_NPU_COMPILER_BUILD=OFF \
%cmake_build

%install
%cmake_install
# remove the unversioned so file
rm -vf %{buildroot}%{_libdir}/libze_intel_npu.so

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libze_intel_npu.so.1
%{_libdir}/libze_intel_npu.so.%{version}

%files test
%{_bindir}/npu-kmd-test
%{_bindir}/npu-umd-test

%changelog
%autochangelog
