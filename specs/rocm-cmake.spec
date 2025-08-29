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

# there is no debug package - this is just cmake modules
%global debug_package %{nil}

%global rocm_release 6.4
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:     rocm-cmake
Version:  %{rocm_version}
Release:  5%{?dist}
Summary:  CMake modules for common build and development tasks for ROCm
License:  MIT
URL:      https://github.com/ROCm/rocm-cmake
Source:   %{url}/archive/rocm-%{version}.tar.gz#/rocm-cmake-rocm-%{version}.tar.gz
# https://github.com/ROCm/rocm-cmake/issues/276
Patch0:   0001-rocm-cmake-follow-cmake-install-rules.patch

BuildArch: noarch
BuildRequires: cmake
Requires: cmake

%description
rocm-cmake is a collection of CMake modules for common build and development
tasks within the ROCm project. It is therefore a build dependency for many of
the libraries that comprise the ROCm platform.

rocm-cmake is not required for building libraries or programs that use ROCm; it
is required for building some of the libraries that are a part of ROCm.

%prep
%autosetup -p1 -n rocm-cmake-rocm-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rocm-cmake/LICENSE

%files
%dir %{_datadir}/rocm
%dir %{_datadir}/rocmcmakebuildtools

%doc CHANGELOG.md
%license LICENSE
%{_datadir}/rocm/*
%{_datadir}/rocmcmakebuildtools/*

%changelog
* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-5
- Add Fedora copyright

* Mon Aug 25 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- Simplify file removal

* Sat Aug 16 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-3
- Use the default cmake rules for installing

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Apr 16 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.0-1
- Update to 6.4.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 8 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sat Nov 9 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed



