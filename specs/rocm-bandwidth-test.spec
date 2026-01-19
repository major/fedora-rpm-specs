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
%global upstreamname rocm_bandwidth_test
%global rocm_release 6.4
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

# GPU HW is required to run %check, and needs to run locally
%bcond_with check

Name:       rocm-bandwidth-test
Version:    %{rocm_version}
Release:    5%{?dist}
Summary:    Bandwidth test for ROCm

# License mismatch
# https://github.com/ROCm/rocm_bandwidth_test/issues/127
License:    NCSA AND MIT
URL:        https://github.com/ROCm/%{upstreamname}
Source0:    %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
# From base_test.cpp
Source1:    LICENSE.NCSA.txt

ExclusiveArch:  x86_64

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  rocm-runtime-devel >= %{rocm_release}.0

%description
ROCm Bandwidth Test is designed to capture the performance
characteristics of buffer copying and kernel read and write
operations. The benchmark help screen shows various options
for initiating copy, read, and write operations. In
addition to this, you can also query the system topology in
terms of memory pools and their agents.

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p1

# Remove execute permissions on docs
# https://github.com/ROCm/rocm_bandwidth_test/issues/128
chmod a-x LICENSE.txt
chmod a-x README.md
chmod a-x ROCmBandwithTest_UserGuide.pdf
cp %{SOURCE1} .

%build
%cmake
%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rocm-bandwidth-test/LICENSE.txt

%check
%if %{with check}
%{_vpath_builddir}/rocm-bandwidth-test
# On a gfx1201, the start should look something like
#          RocmBandwidthTest Version: 2.6.0
#
#          Launch Command is: redhat-linux-build/rocm-bandwidth-test (rocm_bandwidth -a + rocm_bandwidth -A)
#
#
#          Device: 0,  Intel(R) Core(TM) i5-10400 CPU @ 2.90GHz
#          Device: 1,  AMD Radeon Graphics,  GPU-7b2a57bc7a036a5f,  03:0.0
# ...
%endif

%files
%doc README.md ROCmBandwithTest_UserGuide.pdf
%license LICENSE.txt LICENSE.NCSA.txt
%{_bindir}/rocm-bandwidth-test

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Sep 30 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-4
- Rebuild against ROCm 7.0

* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-3
- Add Fedora copyright

* Mon Aug 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-2
- Simplify file removal

* Sat Jul 26 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-1
- Initial package
