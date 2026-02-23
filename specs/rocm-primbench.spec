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

%global upstreamname primbench
%global rocm_release 7.11
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# there is no debug package, this just headers
%global debug_package %{nil}

Name:           rocm-primbench
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        A single-header HIP benchmarking library
# No toplevel license file
# https://github.com/ROCm/rocm-libraries/issues/4580
# Only one file, it is MIT
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/releases/download/therock-%{rocm_release}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

# Only a header
BuildArch: noarch
# But, ROCm only working on x86_64
ExclusiveArch:  x86_64

%description
Primbench is a single-header HIP benchmarking library.
Features
* Simple benchmarking API
* Colored progress output
* GPU warming and cooling
* GPU cache clearing
* Batching and stream blocking
* Detailed JSON output

The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%package devel
Summary:  A single-header HIP benchmarking library
Provides: primbench-static = %{version}-%{release}
Requires: amdsmi-devel
Requires: rocm-hip-devel

%description devel
Primbench is a single-header HIP benchmarking library.
Features
* Simple benchmarking API
* Colored progress output
* GPU warming and cooling
* GPU cache clearing
* Batching and stream blocking
* Detailed JSON output

%prep
%autosetup -n %{upstreamname} -p1

%build
# Empty

%install
install -D -m 644 primbench.hpp %{buildroot}%{_includedir}/primbench.hpp

%files devel
%doc README.md
%{_includedir}/primbench.hpp

%changelog
* Sat Feb 14 2026 Tom Rix <Tom.Rix@amd.com> - 7.11.0-1
- Initial package
