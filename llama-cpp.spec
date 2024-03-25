# For the extra python package gguf that comes with llama-cpp
%global pypi_name gguf
%global pypi_version 0.7.0

# Some optional subpackages
%bcond_with examples
%bcond_with test

Summary:        Port of Facebook's LLaMA model in C/C++
Name:           llama-cpp

# Licensecheck reports
#
# *No copyright* The Unlicense
# ----------------------------
# common/base64.hpp
# common/stb_image.h
# These are public domain
#
# MIT License
# -----------
# LICENSE
# ...
# This is the main license

License:        MIT AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain
Version:        b2417
Release:        2%{?dist}

URL:            https://github.com/ggerganov/llama.cpp
Source0:        %{url}/archive/%{version}.tar.gz#/llama.cpp-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64
%global toolchain gcc

BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with examples}
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry)

Requires:       cmake-filesystem
%endif

%description
The main goal of llama.cpp is to run the LLaMA model using 4-bit
integer quantization on a MacBook

* Plain C/C++ implementation without dependencies
* Apple silicon first-class citizen - optimized via ARM NEON, Accelerate
  and Metal frameworks
* AVX, AVX2 and AVX512 support for x86 architectures
* Mixed F16 / F32 precision
* 2-bit, 3-bit, 4-bit, 5-bit, 6-bit and 8-bit integer quantization support
* CUDA, Metal and OpenCL GPU backend support

The original implementation of llama.cpp was hacked in an evening.
Since then, the project has improved significantly thanks to many
contributions. This project is mainly for educational purposes and
serves as the main playground for developing new features for the
ggml library.

%package devel
Summary:        Port of Facebook's LLaMA model in C/C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The main goal of llama.cpp is to run the LLaMA model using 4-bit
integer quantization on a MacBook

* Plain C/C++ implementation without dependencies
* Apple silicon first-class citizen - optimized via ARM NEON, Accelerate
  and Metal frameworks
* AVX, AVX2 and AVX512 support for x86 architectures
* Mixed F16 / F32 precision
* 2-bit, 3-bit, 4-bit, 5-bit, 6-bit and 8-bit integer quantization support
* CUDA, Metal and OpenCL GPU backend support

The original implementation of llama.cpp was hacked in an evening.
Since then, the project has improved significantly thanks to many
contributions. This project is mainly for educational purposes and
serves as the main playground for developing new features for the
ggml library.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%if %{with examples}
%package examples
Summary:        Examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description examples
%{summary}
%endif

%prep
%autosetup -p1 -n llama.cpp-%{version}

# verson the *.so
sed -i -e 's/POSITION_INDEPENDENT_CODE ON/POSITION_INDEPENDENT_CODE ON SOVERSION %{version}/' CMakeLists.txt

# no android needed
rm -rf exmples/llma.android
# git cruft
find . -name '.gitignore' -exec rm -rf {} \;
# scripts need to be executable
chmod 755 examples/finetune/convert-finetune-checkpoint-to-gguf.py
chmod 755 examples/finetune/finetune.sh
chmod 755 examples/train-text-from-scratch/convert-train-checkpoint-to-gguf.py


%build
%if %{with examples}
cd %{_vpath_srcdir}/gguf-py
%pyproject_wheel
cd -
%endif

%cmake \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DLLAMA_AVX=OFF \
    -DLLAMA_AVX2=OFF \
    -DLLAMA_AVX512=OFF \
    -DLLAMA_AVX512_VBMI=OFF \
    -DLLAMA_AVX512_VNNI=OFF \
    -DLLAMA_FMA=OFF \
    -DLLAMA_F16C=OFF \
%if %{with examples}
    -DLLAMA_BUILD_EXAMPLES=ON \
%else
    -DLLAMA_BUILD_EXAMPLES=OFF \
%endif
%if %{with test}
    -DLLAMA_BUILD_TESTS=ON
%else
    -DLLAMA_BUILD_TESTS=OFF
%endif
    
%cmake_build

%install
%if %{with examples}
cd %{_vpath_srcdir}/gguf-py
%pyproject_install
cd -
%endif

%cmake_install

rm -rf %{buildroot}%{_libdir}/libggml_shared.*

%if %{with examples}
mkdir -p %{buildroot}%{_datarootdir}/%{name}
cp -r %{_vpath_srcdir}/examples %{buildroot}%{_datarootdir}/%{name}/
cp -r %{_vpath_srcdir}/models %{buildroot}%{_datarootdir}/%{name}/
cp -r %{_vpath_srcdir}/README.md %{buildroot}%{_datarootdir}/%{name}/
rm -rf %{buildroot}%{_datarootdir}/%{name}/examples/llama.android
%else
rm %{buildroot}%{_bindir}/convert*.py
%endif

%if %{with test}
%check
%ctest
%endif

%files
%license LICENSE
%{_libdir}/libllama.so.%{version}

%files devel
%dir %{_libdir}/cmake/Llama
%doc README.md
%{_includedir}/ggml.h
%{_includedir}/ggml-alloc.h
%{_includedir}/ggml-backend.h
%{_includedir}/llama.h
%{_libdir}/libllama.so
%{_libdir}/cmake/Llama/*.cmake

%if %{with test}
%files test
%{_bindir}/test-autorelease
%{_bindir}/test-backend-ops
%{_bindir}/test-chat-template
%{_bindir}/test-grad0
%{_bindir}/test-grammar-parser
%{_bindir}/test-llama-grammar
%{_bindir}/test-model-load-cancel
%{_bindir}/test-quantize-fns
%{_bindir}/test-quantize-perf
%{_bindir}/test-rope
%{_bindir}/test-sampling
%{_bindir}/test-tokenizer-0-falcon
%{_bindir}/test-tokenizer-0-llama
%{_bindir}/test-tokenizer-1-bpe
%{_bindir}/test-tokenizer-1-llama
%endif

%if %{with examples}
%files examples
%{_bindir}/baby-llama
%{_bindir}/batched
%{_bindir}/batched-bench
%{_bindir}/beam-search
%{_bindir}/benchmark
%{_bindir}/convert-lora-to-ggml.py
%{_bindir}/convert.py
%{_bindir}/convert-llama2c-to-ggml
%{_bindir}/embedding
%{_bindir}/export-lora
%{_bindir}/finetune
%{_bindir}/gguf
%{_bindir}/gguf-convert-endian
%{_bindir}/gguf-dump
%{_bindir}/gguf-set-metadata
%{_bindir}/gritlm
%{_bindir}/imatrix
%{_bindir}/infill
%{_bindir}/llama-bench
%{_bindir}/llava-cli
%{_bindir}/lookahead
%{_bindir}/lookup
%{_bindir}/main
%{_bindir}/parallel
%{_bindir}/passkey
%{_bindir}/perplexity
%{_bindir}/quantize
%{_bindir}/quantize-stats
%{_bindir}/save-load-state
%{_bindir}/server
%{_bindir}/simple
%{_bindir}/speculative
%{_bindir}/tokenize
%{_bindir}/train-text-from-scratch
%{_libdir}/libllava_shared.so
%{_datarootdir}/%{name}/
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}.dist-info
%{python3_sitelib}/scripts
%endif

%changelog
* Sat Mar 23 2024 Tom Rix <trix@redhat.com> - b2417-2
- Fix test subpackage

* Thu Mar 14 2024 Tom Rix <trix@redhat.com> - b2417-1
- Update to b2417

* Sat Dec 23 2023 Tom Rix <trix@redhat.com> - b1695-1
- Initial package
