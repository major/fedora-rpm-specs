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
%global upstreamname rocminfo
%global rocm_release 6.4
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:       rocminfo
Version:    %{rocm_version}
Release:    3%{?dist}
Summary:    ROCm system info utility

License:    NCSA
URL:        https://github.com/ROCm/rocminfo
Source0:    %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch0:     0001-adjust-CMAKE_CXX_FLAGS.patch
Patch1:     0002-fix-buildtype-detection.patch

ExclusiveArch:  x86_64

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  rocm-runtime-devel >= %{rocm_release}.0
BuildRequires:  python3-devel

# rocminfo calls lsmod to check the kernel mode driver status
Requires:       kmod

%description
ROCm system info utility

%prep
%autosetup -n %{name}-rocm-%{version} -p1

%if 0%{?fedora} || 0%{?rhel}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} rocm_agent_enumerator
%endif

%build
%cmake -DROCM_DIR=/usr
%cmake_build

%install
%cmake_install

#FIXME:
chmod 755 %{buildroot}%{_bindir}/*

%files
%doc README.md
%license License.txt
%{_bindir}/rocm_agent_enumerator
%{_bindir}/rocminfo
#Duplicated files:
%exclude %{_docdir}/*/License.txt

%changelog
* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-3
- Add Fedora copyright

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Apr 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-1
- Update to 6.4.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 7 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3.0

* Sat Nov 9 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed



