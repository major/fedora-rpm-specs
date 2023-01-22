%global upstreamname ROCm-OpenCL-Runtime
%global rocm_release 5.4
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

#Set enable_ocltst to enable HW OCL test suite
%if 0%{?enable_ocltst}
#Using -Werror=format-security fails to compile ocltst:
%global _warning_options -Wall
%endif

Name:           rocm-opencl
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        ROCm OpenCL Runtime

Url:            https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime
License:        MIT
Source0:        https://github.com/RadeonOpenCompute/%{upstreamname}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Source1:        https://github.com/ROCm-Developer-Tools/ROCclr/archive/refs/tags/rocm-%{version}.tar.gz#/ROCclr-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  clang-devel
%if 0%{?enable_ocltst}
BuildRequires:  pkgconfig(glew)
%endif
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-runtime-devel

Requires:       comgr(rocm) = %{rocm_release}
Requires:       ocl-icd%{?_isa}
Requires:       opencl-filesystem

#Only the following architectures are supported:
# The kernel support only exists for x86_64, aarch64, and ppc64le
# 32bit userspace is excluded based on current Fedora policies
#TODO: ppc64le doesn't build on EPEL8 due to type casting issue
%if 0%{?rhel} <= 8 && 0%{?rhel}
ExclusiveArch:  x86_64 aarch64
%else
ExclusiveArch:  x86_64 aarch64 ppc64le
%endif

#rocm-opencl bundles OpenCL 2.2 headers
# Some work is needed to unbundle this, as it fails to compile with latest
Provides:       bundled(opencl-headers) = 2.2

%description
ROCm OpenCL language runtime.
Supports offline and in-process/in-memory compilation.

%package devel
Summary:        ROCm OpenCL development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocl-icd-devel%{?_isa}

%description devel
The AMD ROCm OpenCL development package.

%package -n rocm-clinfo
Summary:        ROCm OpenCL platform and device tool

%description -n rocm-clinfo
A simple ROCm OpenCL application that enumerates all possible platform and
device information.

%if 0%{?enable_ocltst}
%package -n rocm-ocltst
Summary:        ROCm OpenCL test suite

%description -n rocm-ocltst
Test suite provided with rocm-opencl.
%endif

%prep
%autosetup -N -a 1 -n %{upstreamname}-rocm-%{version}

pushd ROCclr-rocm-%{version}
%autopatch -p1 -m 0 -M 99
# Enable experimental pre vega platforms
sed -i 's/\(ROC_ENABLE_PRE_VEGA.*\)false/\1true/' utils/flags.hpp
popd
%autopatch -p1 -m 100
#Disable RPATH in clinfo:
sed -i "/RPATH/d" tools/clinfo/CMakeLists.txt

#Add soname to amdocl and cltrace:
# Upstream doesn't want this because they don't guarentee ABI.
# Just use the package version. SOVERSION can be major.minor as patch releases
# are unlikely to break anything.
#TODO: make a patch for upstream to allow setting a soname optionally
echo "set_target_properties(amdocl PROPERTIES VERSION %{version} SOVERSION %(v=%{version};echo ${v%%.*}))" \
    >> amdocl/CMakeLists.txt
echo "libamdocl64.so.%{rocm_release}" > config/amdocl64.icd
echo "set_target_properties(cltrace PROPERTIES VERSION %{version} SOVERSION %(v=%{version};echo ${v%%.*}))" \
    >> tools/cltrace/CMakeLists.txt

#Clean up unused bundled code:
# bundled opencl2.2 headers are needed as ocl doesn't compile against latest:
ls -d khronos/* | grep -v headers | xargs rm -r
ls -d khronos/headers/* | grep -v opencl2.2 | xargs rm -r
# unused opencl 2.2 test code:
rm -r khronos/headers/opencl2.2/tests/

%if 0%{?enable_ocltst}
#Change install location for ocltst test suite:
sed -i "s|\(DESTINATION \)tests/ocltst|\1\${CMAKE_INSTALL_LIBDIR}|" \
    tests/ocltst/log/CMakeLists.txt tests/ocltst/module/*/CMakeLists.txt
sed -i "s|\(DESTINATION \)tests/ocltst|\1\${CMAKE_INSTALL_BINDIR}|" \
    tests/ocltst/env/CMakeLists.txt
%endif

%build
%cmake \
    -DAMD_OPENCL_PATH=$(pwd) \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DROCCLR_PATH=$(pwd)/ROCclr-rocm-%{version} \
    -DBUILD_ICD=OFF \
    -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF \
%if 0%{?enable_ocltst}
    -DBUILD_TESTS=ON \
%endif
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

#Install ICD configuration:
install -D -m 644 config/amdocl64.icd \
    %{buildroot}%{_sysconfdir}/OpenCL/vendors/amdocl64.icd

#Avoid file conflicts with opencl-headers package:
mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/CL %{buildroot}%{_includedir}/%{name}/CL

#Avoid file conflicts with clinfo package:
mv %{buildroot}%{_bindir}/clinfo %{buildroot}%{_bindir}/rocm-clinfo

%files
%license LICENSE.txt
%config(noreplace) %{_sysconfdir}/OpenCL/vendors/amdocl64.icd
%{_libdir}/libamdocl64.so.5{,.*}
%{_libdir}/libcltrace.so.5{,.*}
#Duplicated files:
%exclude %{_docdir}/*/LICENSE*

%files devel
%{_libdir}/libamdocl64.so
%{_libdir}/libcltrace.so
%{_includedir}/%{name}

%if 0%{?enable_ocltst}
%files -n rocm-ocltst
%license LICENSE.txt
%{_bindir}/ocltst
%{_libdir}/libocl*.so
%{_libdir}/ocl*.exclude
%{_libdir}/libTestLog.so
%endif

%files -n rocm-clinfo
%license LICENSE.txt
%{_bindir}/rocm-clinfo

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.4.1-1
- Update to 5.4.1

* Thu Nov 10 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.3.2-1
- Update to 5.3.2

* Mon Oct 17 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.3.0-1
- Update to 5.3.0

* Thu Aug 18 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.3-1
- Update to 5.2.3

* Tue Jul 26 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.1-3
- Add missing ocl-icd-devel requires on devel package, fixes RHBZ#2111024

* Mon Jul 25 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.1-2
- Enable pre vega HW (experimental)

* Sun Jul 24 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.1-1
- Update to 5.2.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.0-1
- Update to 5.2.0
- Use comgr(rocm) instead of rocm-comgr for requires for easier maintenance

* Tue Jul 05 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.2-1
- Initial package
