%global _firmwarepath /lib/firmware/updates/intel/vpu

%global desc %{expand: \
Intel NPU device is an AI inference accelerator integrated with Intel client
CPUs, starting from Intel Core Ultra generation of CPUs (formerly known as
Meteor Lake). It enables energy-efficient execution of artificial neural
network tasks.}

Name:		intel-npu-driver
Version:	1.28.0
Release:	%autorelease
Summary:	Intel Neural Processing Unit Driver

License:	MIT AND Apache-2.0
URL:		https://github.com/intel/linux-npu-driver
Source0:	%url/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/intel/level-zero-npu-extensions/archive/61e4aeb00afd2a5b6955986269eed3a713c7b562/level-zero-npu-extensions-61e4aeb.tar.gz
Source2:	https://github.com/openvinotoolkit/npu_compiler_elf/archive/9d91134722e70bf52297adaeb221a0be8e408b14/npu_compiler_elf-9d91134.tar.gz

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
# openvino-npu_compiler_elf
Provides:	bundled(openvino-npu_compiler_elf)
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
rm -rf thirdparty/googletest \
  thirdparty/level-zero \
  third_party/level-zero-npu-extensions \
  thirdparty/perfetto \
  thirdparty/yaml-cpp
tar xf %{SOURCE1}
mv level-zero-npu-extensions-* third_party/level-zero-npu-extensions
tar xf %{SOURCE2}
mv npu_compiler_elf-*/* third_party/npu_compiler_elf

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

# install NPU shared tests
install -m 0755 redhat-linux-build/bin/*npu_*tests %{buildroot}/usr/bin/

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libze_intel_npu.so.1
%{_libdir}/libze_intel_npu.so.%{version}
%exclude %{_firmwarepath}/*

%files test
%{_bindir}/npu-kmd-test
%{_bindir}/npu-umd-test
%{_bindir}/*npu_*tests

%changelog
%autochangelog
