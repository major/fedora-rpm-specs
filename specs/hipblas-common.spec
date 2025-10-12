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
%global upstreamname hipBLAS-common
%global rocm_release 7.0
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           hipblas-common
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        Common files shared by hipBLAS and hipBLASLt
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake

# Only headers, cmake infra
BuildArch: noarch
# Only x86_64 works right now:
ExclusiveArch:  x86_64

# Problem on SUSE, nothing really to compile so turn jobs off
%global _smp_mflags %{nil}

%description
%summary

%package devel
Summary:        Libraries and headers for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake -DCMAKE_INSTALL_LIBDIR=share
%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/hipblas-common/LICENSE.md

%files devel
%license LICENSE.md
%{_includedir}/%{name}
%{_datadir}/cmake/%{name}

%changelog
* Fri Oct 10 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.0-2
- Remove stray backlash

* Fri Sep 19 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.0-1
- Update to 7.0.1

* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- Add Fedora copyright

* Mon Aug 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-3
- Simplify file removal

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Apr 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Initial package

