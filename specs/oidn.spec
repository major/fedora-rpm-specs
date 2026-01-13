%bcond 	        hip 1
%bcond          ninja 1
#%%global	        prerelease beta
Name:           oidn
Version:        2.4.0
Release:        %autorelease %{?prerelease: -p -e %{prerelease}}
Summary:        Library of denoising filters for images rendered with ray tracing
License:        Apache-2.0
URL:            https://openimagedenoise.github.io/

Source0:        https://github.com/OpenImageDenoise/%{name}/releases/download/v%{version}%{?prerelease:-%{prerelease}}/%{name}-%{version}%{?prerelease:-%{prerelease}}.src.tar.gz

%if %{with hip}
# hipcc is clang based and the extra rpm induced gcc args confuse it
%global toolchain clang
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong//' -e 's/-fcf-protection//' -e 's/-mtls-dialect=gnu2//' )
%endif

# Library only available on x86_64
ExclusiveArch:  x86_64

BuildRequires:  cmake >= 3.13.0
# Enable HIP support
%if %{with hip}
BuildRequires:  hipcc
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime
%endif
# Needed to remove rpath from apps
BuildRequires:  chrpath
%if %{with hip}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  help2man
BuildRequires:  ispc
Recommends:     ispc-gpu
%if %{with ninja}
BuildRequires:  ninja-build
%endif
BuildRequires:  pkgconfig(OpenImageIO)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tbb)

%description
Intel Open Image Denoise is an open source library of high-performance, 
high-quality denoising filters for images rendered with ray tracing.

%package        libs
Summary:        Libraries for %{name}

%description    libs
The %{name}-libs package contains shared library for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        docs
Summary:        Documentation for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
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
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
%if %{with hip}
    -DOIDN_DEVICE_HIP=ON \
    -DOIDN_DEVICE_HIP_COMPILER=%{_bindir}/hipcc \
    -DROCM_PATH=%{_libdir}
%endif
%cmake_build

%install
%cmake_install

# Generate and install man pages.
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done

# Remove rpath
chrpath --delete %{buildroot}%{_bindir}/%{name}{Denoise,Test,Benchmark}
chrpath --delete %{buildroot}%{_libdir}/libOpenImageDenoise{,_core,_device_cpu}.so.*
%if %{with hip}
chrpath --delete %{buildroot}%{_libdir}/libOpenImageDenoise_device_hip.so.*
%endif

# Remove duplicated documentation
rm -rf %{buildroot}%{_docdir}/OpenImageDenoise

%files
%license LICENSE.txt
%doc CHANGELOG.md 
%{_bindir}/%{name}{Denoise,Test,Benchmark}
%{_mandir}/man1/%{name}{Denoise,Test,Benchmark}.1.gz

%files libs
%{_libdir}/libOpenImageDenoise{,_core,_device_cpu}.so.2
%{_libdir}/libOpenImageDenoise{,_core,_device_cpu}.so.%{version}
%if %{with hip}
%{_libdir}/libOpenImageDenoise_device_hip.so.%{version}
%endif

%files docs
%doc README.md readme.pdf 

%files devel
%{_libdir}/cmake/OpenImageDenoise-%{version}/*.cmake
%{_includedir}/OpenImageDenoise
%{_libdir}/libOpenImageDenoise.so

%changelog
%autochangelog
