# Generated by go2rpm 1.14.0
%bcond check 0
%ifarch x86_64
%bcond rocm 1
%else
%bcond rocm 0
%endif

# build problems on aarch64
ExcludeArch:    aarch64

# Build the next version of ollama
%bcond next 0

# https://github.com/ollama/ollama
%global goipath         github.com/ollama/ollama
%global forgeurl        https://github.com/ollama/ollama
Version:                0.9.4

%gometa -L -f

%global common_description %{expand:
Get up and running with Llama 3.2, Mistral, Gemma 2, and other large language
models.}

%global golicenses      LICENSE
%global godocs          docs examples CONTRIBUTING.md README.md SECURITY.md\\\
                        app-README.md integration-README.md llama-README.md\\\
                        macapp-README.md

Name:           ollama
Release:        %autorelease
Summary:        Get up and running AI LLMs

License:        Apache-2.0 AND MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  cmake

%if %{with rocm}
BuildRequires:  hipblas-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocminfo

Requires:       hipblas
Requires:       rocblas
%endif

# Only tested on x86_64:

%description %{common_description}

%gopkg

%prep
%goprep -A
# Remove some .git cruft
for f in `find . -name '.gitignore'`; do
    rm $f
done

# Rename README's
mv app/README.md app-README.md
mv integration/README.md integration-README.md
mv llama/README.md llama-README.md
mv macapp/README.md macapp-README.md

# gcc 15 cstdint
sed -i '/#include <vector.*/a#include <cstdint>' llama/llama.cpp/src/llama-mmap.h

# install dir is off, lib -> lib64
sed -i -e 's@set(OLLAMA_INSTALL_DIR ${CMAKE_INSTALL_PREFIX}/lib/ollama)@set(OLLAMA_INSTALL_DIR ${CMAKE_INSTALL_PREFIX}/lib64/ollama)@' CMakeLists.txt
echo -e 'package discover\nvar LibOllamaPath string = "/usr/lib64/ollama"' > discover/path.go
sed -i -e 's@"lib/ollama"@"lib64/ollama"@' ml/backend/ggml/ggml/src/ggml.go

# _build/src/github.com/ollama/ollama/model/bytepairencoding.go:25:43: undefined: regexp2.Unicode
# https://src.fedoraproject.org/rpms/golang-github-dlclark-regexp2/pull-request/2
# In the meantime, hack it out
sed -i -e 's@regexp2.Unicode|regexp2.RE2@regexp2.RE2@' model/bytepairencoding.go

%generate_buildrequires
%go_generate_buildrequires

%build

%cmake \
%if %{with rocm}
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/clang++ \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default}
%endif

%cmake_build

# Debug with:
# Manual build when there are problems
# export GOPATH=$(pwd)/_build:%{gopath}
# export GO111MODULE=off
# go build -o %{gobuilddir}/bin/ollama %{goipath}
# Release with
# cmake sets LDFLAGS env, this confuses gobuild
export LDFLAGS=
%gobuild -o %{gobuilddir}/bin/ollama %{goipath}

%install
%cmake_install

# remove copies of system libraries
runtime_removal="hipblas rocblas amdhip64 rocsolver amd_comgr hsa-runtime64 rocsparse tinfo rocprofiler-register drm drm_amdgpu numa elf"
for rr in $runtime_removal; do
    rm -rf %{buildroot}%{_libdir}/ollama/rocm/lib${rr}*
done
rm -rf %{buildroot}%{_libdir}/ollama/rocm/rocblas

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/ollama/bin
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_libdir}/ollama/bin/

pushd .
cd %{buildroot}%{_bindir}
ln -s ../%{_lib}/ollama/bin/ollama ollama
popd

#Clean up dupes:
%fdupes %{buildroot}%{_prefix}

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md SECURITY.md README.md app-README.md integration-README.md
%doc llama-README.md macapp-README.md
%dir %{_libdir}/ollama
%{_libdir}/ollama/libggml-base.so
%{_libdir}/ollama/libggml-cpu-alderlake.so
%{_libdir}/ollama/libggml-cpu-haswell.so
%{_libdir}/ollama/libggml-cpu-icelake.so
%{_libdir}/ollama/libggml-cpu-sandybridge.so
%{_libdir}/ollama/libggml-cpu-skylakex.so
%{_libdir}/ollama/libggml-cpu-sse42.so
%{_libdir}/ollama/libggml-cpu-x64.so

%dir %{_libdir}/ollama/bin
%{_libdir}/ollama/bin/ollama
%{_bindir}/ollama

%if %{with rocm}
%{_libdir}/ollama/libggml-hip.so
%endif

%changelog
%autochangelog
