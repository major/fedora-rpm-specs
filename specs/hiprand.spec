%global upstreamname hipRAND

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

%bcond_with doc

Name:           hiprand
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        HIP random number generator

Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT and BSD
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocrand-devel

%if %{with test}
BuildRequires:  gtest-devel
%endif

%if %{with doc}
BuildRequires:  doxygen
%endif

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipRAND is a RAND marshalling library, with multiple supported backends. It
sits between the application and the backend RAND library, marshalling inputs
into the backend and results back to the application. hipRAND exports an
interface that does not require the client to change, regardless of the chosen
backend. Currently, hipRAND supports either rocRAND or cuRAND.

%package devel
Summary:        The hipRAND development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rocrand-devel

%description devel
The hipRAND development package.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

#Remove RPATH:
sed -i '/INSTALL_RPATH/d' CMakeLists.txt

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
           -DBUILD_TEST=%{build_test} \
           -DROCM_SYMLINK_LIBS=OFF

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
find %{buildroot}           -name 'test_*'       | sed -f br.sed >  %{name}.test
%endif

if [ -f %{buildroot}%{_prefix}/share/doc/hiprand/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/hiprand/LICENSE.txt
fi
if [ -f %{buildroot}%{_prefix}/bin/hipRAND/CTestTestfile.cmake ]; then
    rm %{buildroot}%{_prefix}/bin/hipRAND/CTestTestfile.cmake
fi

%files -f %{name}.files
%doc README.md
%license LICENSE.txt

%files devel -f %{name}.devel
%dir %{_libdir}/cmake/%{name}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- build requires gcc-c++

* Tue Dec 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed


