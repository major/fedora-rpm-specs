# Use clang by default.
%bcond          gcc 0
%bcond          hip %{undefined flatpak}
%bcond          ninja 1
#%%global               prerelease beta
Name:           oidn
Version:        2.5.1
Release:        %autorelease %{?prerelease: -p -e %{prerelease}}
Summary:        Library of noise reduction filters for images rendered with ray tracing
License:        Apache-2.0
URL:            https://openimagedenoise.github.io/

Source0:        https://github.com/OpenImageDenoise/%{name}/releases/download/v%{version}%{?prerelease:-%{prerelease}}/%{name}-%{version}%{?prerelease:-%{prerelease}}.src.tar.gz

%if %{without gcc}
%global toolchain clang
%endif

%if %{with hip}
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong//' -e 's/-fcf-protection//' -e 's/-mtls-dialect=gnu2//' )
%endif

# This package currently enables only x86_64 builds.
ExclusiveArch:  x86_64

BuildRequires:  cmake >= 3.21
# Enable HIP support
%if %{with hip}
BuildRequires:  hipcc
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime
%endif
# Needed to remove rpath from apps
BuildRequires:  chrpath
BuildRequires:  binutils
%if %{with gcc}
BuildRequires:  gcc-c++
%else
BuildRequires:  clang
%endif
BuildRequires:  help2man
BuildRequires:  cmake(ispcrt)
BuildRequires:  ispc >= 1.30.0
BuildRequires:  python3
%if %{with ninja}
BuildRequires:  ninja-build
%endif
BuildRequires:  pkgconfig(OpenImageIO) > 3.0
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tbb)

%description
Intel Open Image Denoise is an open source library of high-performance,
high-quality noise reduction filters for images rendered with ray tracing.

%package        libs
Summary:        Libraries for %{name}
%if %{with hip}
Recommends:     %{name}-libs-hip%{?_isa} = %{version}-%{release}
%endif

%description    libs
The %{name}-libs package contains shared library for %{name}.

# Enable HIP support
%if %{with hip}
%package        libs-hip
Summary:        HIP backend for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    libs-hip
The %{name}-libs-hip package provides the AMD GPU noise reduction backend.
%endif

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
The %{name}-docs package contains documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}%{?prerelease:-%{prerelease}}

%build
%cmake \
%if %{with ninja}
    -G Ninja \
%endif
    -DOIDN_DEVICE_CPU=ON \
    -DOIDN_DEVICE_HIP=%{?with_hip:ON}%{!?with_hip:OFF} \
%if %{with hip}
    -DROCM_PATH=%{_libdir} \
    -DOIDN_DEVICE_HIP_COMPILER=%{_bindir}/hipcc \
%endif
    -DOIDN_APPS=ON \
    -DOIDN_APPS_OPENIMAGEIO=ON \
    -DOIDN_INSTALL_DEPENDENCIES=OFF \
    %{nil}

%cmake_build

%install
%cmake_install

# Generate and install man pages.
install -d '%{buildroot}%{_mandir}/man1'
for app in %{name}Denoise %{name}Test %{name}Benchmark
do
  cmd="%{buildroot}%{_bindir}/${app}"
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done

# Remove RPATH/RUNPATH from regular ELF files, skipping symlinks.
find %{buildroot}%{_bindir} %{buildroot}%{_libdir} -type f | while IFS= read -r elf
do
  if readelf -h "$elf" >/dev/null 2>&1; then
    if readelf -d "$elf" | grep -qE '\((RPATH|RUNPATH)\)'; then
      chrpath --delete "$elf"
    fi
  fi
done

# Remove duplicated documentation
rm -rf %{buildroot}%{_docdir}/OpenImageDenoise

%check
# Run upstream tests on the CPU; builders do not need GPU access.
OIDN_DEVICE_HIP=0 OIDN_DEVICE_SYCL=0 OIDN_DEVICE_CUDA=0 OIDN_DEVICE_METAL=0 \
LD_LIBRARY_PATH="%{buildroot}%{_libdir}" \
    %{buildroot}%{_bindir}/oidnTest --device cpu

%files
%doc CHANGELOG.md
%{_bindir}/%{name}{Denoise,Test,Benchmark}
%{_mandir}/man1/%{name}{Denoise,Test,Benchmark}.1.gz

%files libs
%license LICENSE.txt
%{_libdir}/libOpenImageDenoise{,_core,_device_cpu}.so.2
%{_libdir}/libOpenImageDenoise{,_core,_device_cpu}.so.%{version}

%if %{with hip}
%files libs-hip
%{_libdir}/libOpenImageDenoise_device_hip.so.%{version}
%endif

%files docs
%license LICENSE.txt
%doc README.md readme.pdf

%files devel
%doc README.md
%{_libdir}/cmake/OpenImageDenoise-%{version}/
%{_includedir}/OpenImageDenoise/
%{_libdir}/libOpenImageDenoise.so

%changelog
%autochangelog
