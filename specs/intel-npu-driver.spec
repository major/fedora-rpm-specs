
Name:		intel-npu-driver
Version:	1.35.0
Release:	%autorelease
Summary:	Intel Neural Processing Unit Driver

License:	MIT AND Apache-2.0
URL:		https://github.com/intel/linux-npu-driver
Source0:	%url/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/intel/level-zero-npu-extensions/archive/f9ad3bf89c2418d714aef2e6b96a5aafb12a1971/level-zero-npu-extensions-f9ad3bf.tar.gz
Source2:	https://github.com/openvinotoolkit/npu_compiler_elf/archive/a301d97e0717fb797c79ec51f8cdc13152878700/npu_compiler_elf-a301d97.tar.gz

%if 0%{?fedora} > 44
Patch0:         add-initializer-umd-level_zero_driver-ze_device.patch
%endif

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
Intel NPU device is an AI inference accelerator integrated with Intel client
CPUs, starting from Intel Core Ultra generation of CPUs (formerly known as
Meteor Lake). It enables energy-efficient execution of artificial neural
network tasks.

%package test
Summary:	Test files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description test
The %{name}-test package contains kernel-mode (kmd) and user-mode (umd)
parts of the %{name}.

%package -n intel-npu-smi
Summary:        Utility tool to track NPU telemetry data

%description -n intel-npu-smi
The intel-npu-smi package utility tool for tracking NPU telemetry power reporting

%prep
%autosetup -N -n linux-npu-driver-%{version}

# thirdparty deps
rm -rf third_party/googletest \
  third_party/level-zero-npu-extensions \
  third_party/npu_compiler_elf \
  third_party/yaml-cpp
tar xf %{SOURCE1}
mv level-zero-npu-extensions-* third_party/level-zero-npu-extensions
tar xf %{SOURCE2}
mv npu_compiler_elf-* third_party/npu_compiler_elf

%autopatch -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DUSE_SYSTEM_LIBRARIES=ON \
	-DENABLE_NPU_PERFETTO_BUILD=ON \
	-DENABLE_TOOLS_BUILD=ON \
	-DENABLE_NPU_COMPILER_BUILD=OFF
%cmake_build

%install
%cmake_install

# remove the unversioned so file
rm -vf %{buildroot}%{_libdir}/libze_intel_npu.so

# install NPU shared tests
install -d %{buildroot}%{_bindir}
install -m 0755 redhat-linux-build/bin/*npu_*tests %{buildroot}%{_bindir}/

# Stage source trees inside the cmake build dir so debugedit/cpio can find
# files for /usr/src/debug/. DWARF records paths as "redhat-linux-build/<sub>/..."
# but the real sources live at "<sub>/..." in the unpacked tarball.
mkdir -p redhat-linux-build/third_party/npu_compiler_elf
cp -a third_party/npu_compiler_elf/. redhat-linux-build/third_party/npu_compiler_elf/
cp -a umd/.                          redhat-linux-build/umd/
cp -a validation/.                   redhat-linux-build/validation/
mkdir -p redhat-linux-build/third_party/perfetto/sdk
cp -a third_party/perfetto/sdk/.     redhat-linux-build/third_party/perfetto/sdk/
cp -a tools/intel-npu-smi/.          redhat-linux-build/tools/intel-npu-smi/

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libze_intel_npu.so.1
%{_libdir}/libze_intel_npu.so.%{version}

%files test
%{_bindir}/npu-kmd-test
%{_bindir}/npu-umd-test
%{_bindir}/*npu_*tests

%files -n intel-npu-smi
%{_bindir}/intel-npu-smi

%changelog
%autochangelog
