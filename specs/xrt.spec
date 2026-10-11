# SPDX-License-Identifier: MIT
%global xrt_major 2
%global xrt_minor 25
%global xrt_patch 0
%global xrt_release %{xrt_major}.%{xrt_minor}
%global xrt_version %{xrt_release}.%{xrt_patch}

Name:           xrt
Version:        2.25.0
Release:        %autorelease
Summary:        Run Time for AIE based platforms

License:        Apache-2.0 AND MIT AND GPL-2.0-only
URL:            https://github.com/Xilinx/XRT

# License breakdown:
# Files: *
# - License: Apache-2.0
#
# Files: xrt/XRT/src/runtime_src/core/common/aiebu/*
# - License: MIT
#
# Files: xrt/XRT/src/runtime_src/core/common/aie-codegen/*
# - License: MIT
#
# Files: xrt/XRT/src/runtime_src/core/common/elf/*
# - License: MIT
#
# Files: xrt/XRT/src/runtime_src/core/common/gsl
# - License: MIT
#
# Files: xrt/XRT/src/runtime_src/core/pcie/driver/linux/*
# - License: GPL-2
#
# Files: xrt/XRT/src/runtime_src/core/include/xclbin.h
#        xrt/XRT/src/runtime_src/core/include/xcl_graph.h
#        xrt/XRT/src/runtime_src/core/include/xrt/deprecated/xclerr.h
#        xrt/XRT/src/runtime_src/core/include/xrt/detail/ert.h
#        xrt/XRT/src/runtime_src/core/include/xrt/detail/xclbin.h
#        xrt/XRT/src/runtime_src/core/include/xrt/detail/xrt_error_code.h
#        xrt/XRT/src/runtime_src/core/include/xrt/detail/xrt_mem.h
# - License: Apache-2.0 or GPL-2
#
# Files: xrt/XRT/src/python/pybind11/pyxrt.pyi
# - License: MIT

# Files: xdna/xdna-driver/src/shim/virtio/amdxdna_proto.h
#        xdna/xdna-driver/src/shim/virtio/drm_hw.h
# - License: MIT
#

Source0:        https://github.com/Xilinx/XRT/releases/download/%{version}/%{name}-%{version}.tar.gz

# Man pages not installed by CMake
Source10:       aiebu-asm.1
Source11:       aiebu-dump.1
Source12:       aiebu-transform.1
Source13:       xclbinutil.1
Source14:       xrt-capture.1
Source15:       xrt-runner.1
Source16:       xrt-smi.1

ExclusiveArch:  aarch64 x86_64

# Build toolchain
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

# System/hardware libraries
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  opencl-headers
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  systemtap-sdt-devel

# C++ libraries
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(RapidJSON)

# Python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  pybind11-devel

# Documentation / packaging helpers
BuildRequires:  doxygen
BuildRequires:  bash-completion

%description
AMD Xilinx Runtime (XRT) provides a runtime environment for AMD Ryzen
NPUs. It includes core runtime libraries, Python bindings,
development files, and utilities for managing and programming AMD
Xilinx devices.

This package provides the core runtime environment for XRT.

%package -n python3-xrt
Summary:        AMD Xilinx Runtime (XRT) - Python bindings
License:        Apache-2.0
Requires:       python3%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-xrt
AMD Xilinx Runtime (XRT) provides a runtime environment for AMD Ryzen
NPUs. It includes core runtime libraries, Python bindings,
development files, and utilities for managing and programming AMD
Xilinx devices.

This package provides python bindings for XRT.

%package devel
Summary:        AMD Xilinx Runtime (XRT) - development files
Requires:       python3-xrt%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libuuid-devel
Requires:       rocm-hip-devel%{?_isa}

%description devel
AMD Xilinx Runtime (XRT) provides a runtime environment for AMD Ryzen
NPUs. It includes core runtime libraries, Python bindings,
development files, and utilities for managing and programming AMD
Xilinx devices.

This package provides development libraries and headers for %{name}

%prep
%autosetup -n %{name}-%{version} -p1

# Exclude unused code for easier license review
rm -rf debian
rm -rf xdna/xdna-driver/src/drivers
rm -rf xdna/xdna-driver/src/shim_ve2
rm -rf xdna/xdna-driver/src/shim/virtio
rm -rf xdna/xdna-driver/src/vxdna
rm -rf xdna/xdna-driver/tools
rm -rf xrt/XRT/.clangd
rm -rf xrt/XRT/.github
rm -rf xrt/XRT/.travis.yml
rm -rf xrt/XRT/build
rm -rf xrt/XRT/pyrightconfig.json
rm -rf xrt/XRT/src/.clang-tidy
rm -rf xrt/XRT/src/include
rm -rf xrt/XRT/src/platform
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/.github
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/build.gradle
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/gradle.properties
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/publish
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/pyrightconfig.json
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/settings.gradle
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/.dir-locals.el
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/.clang-format
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/.github
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/.tipi/deps
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/.tipi/opts
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/.travis.yml
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/BUILD.bazel
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/CHANGELOG.md
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/INSTALL
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/README.md
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/WORKSPACE
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/packaging
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/src/.tipi
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/test
rm -rf xrt/XRT/src/runtime_src/core/common/aiebu/templates/aie2/stubs.h
rm -rf xrt/XRT/src/runtime_src/core/common/drv
rm -rf xrt/XRT/src/runtime_src/core/common/elf/.clang-format
rm -rf xrt/XRT/src/runtime_src/core/common/elf/.github
rm -rf xrt/XRT/src/runtime_src/core/common/elf/.vscode
rm -rf xrt/XRT/src/runtime_src/core/common/elf/CMakeLists.txt
rm -rf xrt/XRT/src/runtime_src/core/common/elf/cmake
rm -rf xrt/XRT/src/runtime_src/core/common/elf/doc
rm -rf xrt/XRT/src/runtime_src/core/common/elf/examples
rm -rf xrt/XRT/src/runtime_src/core/common/elf/tests
rm -rf xrt/XRT/src/runtime_src/core/common/runner/test
rm -rf xrt/XRT/src/runtime_src/core/edge
rm -rf xrt/XRT/src/runtime_src/core/include/xgq_*
rm -rf xrt/XRT/src/runtime_src/core/pcie/driver/.dir-locals.el
rm -rf xrt/XRT/src/runtime_src/core/pcie/driver/aws
rm -rf xrt/XRT/src/runtime_src/core/pcie/driver/linux/xocl
rm -rf xrt/XRT/src/runtime_src/core/pcie/driver/windows
rm -rf xrt/XRT/src/runtime_src/core/pcie/emulation
rm -rf xrt/XRT/src/runtime_src/core/pcie/noop
rm -rf xrt/XRT/src/runtime_src/core/pcie/tools
rm -rf xrt/XRT/src/runtime_src/core/pcie/windows
rm -rf xrt/XRT/src/runtime_src/core/tools/xbtracer
rm -rf xrt/XRT/src/runtime_src/doc
rm -rf xrt/XRT/src/runtime_src/ert
rm -rf xrt/XRT/src/runtime_src/tools/xbflash2
rm -rf xrt/XRT/src/runtime_src/tools/xbmgmt2
rm -rf xrt/XRT/src/runtime_src/tools/xbtop
rm -rf xrt/XRT/src/runtime_src/tools/xbtracer
rm -rf xrt/XRT/src/runtime_src/tools/scripts/apu_recipes
rm -rf xrt/XRT/src/runtime_src/tools/scripts/is_supported.json
rm -rf xrt/XRT/src/runtime_src/tools/scripts/pkgapu.sh
rm -rf xrt/XRT/src/runtime_src/tools/scripts/rtplot
rm -rf xrt/XRT/src/runtime_src/tools/xclbinutil/aie-pdi-transform/.clang-tidy
rm -rf xrt/XRT/src/runtime_src/tools/xclbinutil/unittests
rm -rf xrt/XRT/src/runtime_src/xocl
rm -rf xrt/XRT/src/runtime_src/xrt
rm -rf xrt/XRT/tests

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DXRT_NPU=1 \
  -DCMAKE_BUILD_RPATH_USE_ORIGIN=ON \
  -DXRT_ENABLE_HIP=ON \
  -DXRT_ENABLE_TRACER=OFF \
  -DXRT_ENABLE_DKMS=OFF \
  -DXRT_INSTALL_STATIC_LIBRARY=OFF \
  -DXRT_ENABLE_EMULATION=OFF

%cmake_build

%install
%cmake_install

# Man pages, not installed by upstream CMake
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE10} %{SOURCE11} %{SOURCE12} \
   %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} \
   %{buildroot}%{_mandir}/man1/

# Bash completion
# Upstream CMake puts in wrong location - move to correct path
install -d -m 0755 %{buildroot}%{bash_completions_dir}
install -Dpm 0644 %{buildroot}%{_datadir}/completions/xbutil-bash-completion \
   %{buildroot}%{bash_completions_dir}/xrt-smi || :
rm -rf %{buildroot}%{_datadir}/completions 2>/dev/null || :

# Install bundled submodule license files with unique names to avoid collisions
install -d %{buildroot}%{_licensedir}/%{name}
install -pm 0644 xrt/XRT/LICENSE \
   %{buildroot}%{_licensedir}/%{name}/LICENSE.xrt
install -pm 0644 xrt/XRT/NOTICE \
   %{buildroot}%{_licensedir}/%{name}/NOTICE.xrt
install -pm 0644 xrt/XRT/src/runtime_src/core/common/aiebu/LICENSE \
   %{buildroot}%{_licensedir}/%{name}/LICENSE.aiebu
install -pm 0644 xrt/XRT/src/runtime_src/core/common/aiebu/NOTICE \
   %{buildroot}%{_licensedir}/%{name}/NOTICE.aiebu
install -pm 0644 xrt/XRT/src/runtime_src/core/common/elf/LICENSE.txt \
   %{buildroot}%{_licensedir}/%{name}/LICENSE.elf
install -pm 0644 xrt/XRT/src/runtime_src/core/common/gsl/LICENSE \
   %{buildroot}%{_licensedir}/%{name}/LICENSE.gsl
install -pm 0644 xrt/XRT/src/runtime_src/core/common/aiebu/src/cpp/cxxopts/LICENSE \
   %{buildroot}%{_licensedir}/%{name}/LICENSE.cxxopts
install -pm 0644 xrt/XRT/src/runtime_src/aie-codegen/license.txt \
   %{buildroot}%{_licensedir}/%{name}/LICENSE.aie-codegen
install -d %{buildroot}%{_licensedir}/%{name}-npu
install -pm 0644 xdna/xdna-driver/LICENSE.amdnpu \
   %{buildroot}%{_licensedir}/%{name}-npu/LICENSE.amdnpu

# ---------------------------------------------------------------------------
# Remove paths upstream installs but no subpackage lists, so rpmbuild
# check-files does not fail on orphans.
# ---------------------------------------------------------------------------
rm -rf %{buildroot}/bins
find %{buildroot}%{_bindir} -mindepth 1 -maxdepth 1 -type f -name '*.sh' -delete
rm -rf %{buildroot}%{_bindir}/{mpd,msd}
rm -rf %{buildroot}%{_bindir}/xrt-replay
rm -rf %{buildroot}/usr/etc
rm -rf %{buildroot}/etc
find %{buildroot}%{_includedir} -mindepth 1 -maxdepth 1 -name 'm*d_plugin.h' -delete
find %{buildroot}%{_libdir} -mindepth 1 -maxdepth 1 -name 'libaws*.so*' -delete
find %{buildroot}%{_libdir} -mindepth 1 -maxdepth 1 -name 'libazure*.so*' -delete
find %{buildroot}%{_libdir} -mindepth 1 -maxdepth 1 -name 'libcontainer*.so*' -delete
find %{buildroot}%{_libdir} -mindepth 1 -maxdepth 1 -name 'libsched*.so' -delete
rm -rf %{buildroot}%{_libdir}/libcert_dtrace.a
rm -rf %{buildroot}/usr/license
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}/usr/local
rm -rf %{buildroot}/usr/version.json
rm -rf %{buildroot}/.clang-tidy
rm -rf %{buildroot}/CMake
rm -rf %{buildroot}/include
rm -rf %{buildroot}/platform
rm -rf %{buildroot}/python
rm -rf %{buildroot}/runtime_src

%check
XILINX_XRT=%{buildroot}/usr \
%{__ctest} --test-dir redhat-linux-build --output-on-failure --force-new-ctest-process -j%{?_smp_build_ncpus}

%files
%dir %{_licensedir}/%{name}
%dir %{_licensedir}/%{name}-npu
%license %{_licensedir}/%{name}/*
%license %{_licensedir}/%{name}-npu/*
%doc xrt/XRT/README.rst
%doc xdna/xdna-driver/README.md
%{_libdir}/libxrt_core.so.%{xrt_major}{,.*}
%{_libdir}/libxrt_coreutil.so.%{xrt_major}{,.*}
%{_libdir}/libxrt_hip.so.%{xrt_major}{,.*}
%{_libdir}/libxrt_driver_xdna.so.%{xrt_major}{,.*}
%{_libdir}/libxdp*.so.%{xrt_major}{,.*}
%dir %{_libdir}/xrt
%dir %{_libdir}/xrt/module
%{_libdir}/xrt/*/libxdp*.so.%{xrt_major}{,.*}
%{_bindir}/xrt-smi
%{_mandir}/man1/xrt-smi.1*
%{_datadir}/bash-completion/completions/xrt-smi
%{_bindir}/xclbinutil
%{_mandir}/man1/xclbinutil.1*
%{_bindir}/xrt-capture
%{_mandir}/man1/xrt-capture.1*
%{_bindir}/xrt-runner
%{_mandir}/man1/xrt-runner.1*
%{_bindir}/aiebu-*
%{_mandir}/man1/aiebu-asm.1*
%{_mandir}/man1/aiebu-dump.1*
%{_mandir}/man1/aiebu-transform.1*

%files -n python3-xrt
%{python3_sitearch}/pyxrt*.so
%{python3_sitearch}/pyxrt*.pyi

%files devel
%dir %{_includedir}/xrt
%{_includedir}/xrt/*
%{_includedir}/hip/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%dir %{_datadir}/cmake/XRT
%{_datadir}/cmake/XRT/*

%changelog
%autochangelog
