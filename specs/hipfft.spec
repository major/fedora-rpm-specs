%global upstreamname hipFFT
%global rocm_release 6.3
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# $gpu will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio

Name:           hipfft
Version:        %{rocm_version}
Release:        4%{?dist}
Summary:        ROCm FFT marshalling library
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT

# Only x86_64 works right now
ExclusiveArch:  x86_64

Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-rocm-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocprim-devel
BuildRequires:  rocfft-devel

%if %{with test}
BuildRequires:  boost-devel
BuildRequires:  fftw-devel
BuildRequires:  gtest-devel
BuildRequires:  hiprand-devel
BuildRequires:  rocrand-devel
%if 0%{?suse_version}
BuildRequires:  libboost_program_options-devel
%endif
%endif

%description
hipFFT is an FFT marshalling library. Currently, hipFFT supports
the rocFFT backends

hipFFT exports an interface that does not require the client to
change, regardless of the chosen backend. It sits between the
application and the backend FFT library, marshalling inputs into
the backend and results back to the application.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p 1

%build
for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu

    %cmake \
	-DCMAKE_CXX_COMPILER=hipcc \
	-DCMAKE_C_COMPILER=hipcc \
	-DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
	-DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
	-DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
           -DCMAKE_BUILD_TYPE=%{build_type} \
	   -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
	   -DCMAKE_SKIP_RPATH=ON \
	   -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
	   -DAMDGPU_TARGETS=${ROCM_GPUS} \
	   -DCMAKE_INSTALL_LIBDIR=$ROCM_LIB \
	   -DCMAKE_INSTALL_BINDIR=$ROCM_BIN \
           -DBUILD_CLIENTS_TESTS=%{build_test} \
	   -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
	   -DROCM_SYMLINK_LIBS=OFF \
           -DHIP_PLATFORM=amd

    %cmake_build
    module purge
done

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

echo s@%{buildroot}@@ > br.sed
find %{buildroot}%{_libdir} -name '*.so.*.[0-9]' | sed -f br.sed >  %{name}.files
find %{buildroot}%{_libdir} -name '*.so.[0-9]'   | sed -f br.sed >> %{name}.files
find %{buildroot}%{_libdir} -name '*.so'         | sed -f br.sed >  %{name}.devel
find %{buildroot}%{_libdir} -name '*.cmake'      | sed -f br.sed >> %{name}.devel
%if %{with test}
find %{buildroot}           -name '%{name}-*'    | sed -f br.sed >  %{name}.test
%endif

if [ -f %{buildroot}%{_prefix}/share/doc/hipfft/LICENSE.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/hipfft/LICENSE.md
fi


%files -f %{name}.files
%license LICENSE.md

%files devel -f %{name}.devel
%doc README.md
%dir %{_libdir}/cmake/%{name}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-4
- multithread compress

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Tue Dec 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed


