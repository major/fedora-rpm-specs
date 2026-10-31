#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
%global toolchain rocm

Summary:        Inference engine for AMD Strix Halo
Name:           gufo
Version:        0.28.0
Release:        %autorelease

# Gufo's core code is MIT licensed, but it includes third-party headers/notes
# which the spec file must account for in the %files section.
License:        MIT AND Apache-2.0 AND CC-BY-SA-4.0 AND BSD-3-Clause
# The main license is MIT
# This project has over specified its licenses, so instead of the usual problem of
# tracking down licenses the package uses, we need to track down the licenses it
# does not need to specify.
#
# See the THIRD_PARTY_NOTICES.md file.  In a lot of cases it describes the licenses
# of its build dependences, not the actual source.  There is a table
#
#    ## Runtime and compiled code
# 
# | Component Name | Relationship | License (SPDX) | Pinned Revision / Version | Upstream Source / Location |
# | --- | --- | --- | --- | --- |
# | ROCm / HIP | Linked runtime | `MIT` | ROCm 7.2.3; flake.lock | [ROCm/clr](https://github.com/ROCm/clr) |
#
# Lines from this table will be included at the appropriate location in the next section for the
# license check.

# From the license check
# Apache-2.0
# licenses/openssl.txt
# | OpenSSL | Linked; cryptographic hashes and HTTPS dependency | `Apache-2.0` | 3.6.3; flake.lock | [openssl/openssl](https://github.com/openssl/openssl) |
#
# | Qwen chat templates | Reference Jinja and adapted renderer behavior | `Apache-2.0` | `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0` (27B), `de4b8e4d43b917e7706784d8bb445c9af86a3540` (Flash-Next) | [Qwen](https://huggingface.co/Qwen/Qwen3.8-27B) |
# licenses/qwen.txt
#
# CC-BY-SA-4.0
# tests/models/deepseek_v4_flash/fixtures/antirez-ds4.json
# tools/ds4/import-eval.py
#
# GPL-2.0-or-later, GPL-3.0-or-later 
# licenses/ffmpeg.txt
# licenses/ffmpeg-LGPL-3.0.txt
# | FFmpeg | Separate ffmpeg/ffprobe executables for media | `GPL-3.0-or-later` (Nix build with GPL/version3 components) | 8.1.2; flake.lock | [FFmpeg](https://github.com/FFmpeg/FFmpeg) |
#
# BSD-3-Clause
# licenses/ccv.txt
# | ccv TensorOps ancestry | Attribution retained through h3.c | `BSD-3-Clause` | h3.c pin above | [liuliu/ccv](https://github.com/liuliu/ccv) 
# 
# Unicode License Agreement - Data Files and Software (2016)
# licenses/icu.txt
# | ICU | Linked; Unicode normalization/tokenization | `Unicode-3.0` | 78.3; flake.lock | [unicode-org/icu](https://github.com/unicode-org/icu) |
#
URL:            https://github.com/gufo-org/gufo
Source0:        %{url}/archive/v%{version}.tar.gz#/gufo-%{version}.tar.gz

# Gufo strictly requires x86_64 with ROCm (gfx1151)
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hipblas-devel
BuildRequires:  hipblaslt-devel
BuildRequires:  hipcub-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libswscale-free-devel
BuildRequires:  libwebp-devel
BuildRequires:  openssl-devel
BuildRequires:  ninja-build
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocprim-devel
BuildRequires:  rocwmma-devel
BuildRequires:  soxr-devel

Requires:       ffmpeg-free

%description
Gufo is a vertical local inference engine specifically built and optimized for
the AMD Strix Halo hardware (Ryzen AI MAX+ 395 systems, gfx1151) with up to
128 GiB of unified memory. It supports text, audio, images, and video models
using a single unified executable.

%prep
%autosetup -n gufo-%{version}

%build

%cmake -G Ninja \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_HIP_ARCHITECTURES=gfx1151 \
    -DENGINE_ENABLE_HIP=ON \
    -DGUIFO_BUILD_TOOLS=OFF \
    -DGUIFO_ENABLE_WARNINGS=ON \
    -DGUIFO_ENABLE_SANITIZERS=OFF

%cmake_build

%install
%cmake_install

# Covered by THIRD_PARTY_NOTICES.md
rm -rf %{buildroot}%{_datadir}/licenses/gufo/

%files
%license LICENSE THIRD_PARTY_NOTICES.md
%doc README.md docs/
%{_bindir}/gufo
%{_bindir}/gufo-server
%{_datadir}/gufo/

%changelog
%autochangelog

