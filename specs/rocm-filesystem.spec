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

%global rocm_release 7.2
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           rocm-filesystem
Version:        %{rocm_version}
Release:        1%{?dist}

Summary:        ROCm directories

Url:            https://fedoraproject.org
License:        MIT

%description
%{summary}

%prep
# Empty

%build
# Empty

%install

# Make directories users of rocm-rpm-modules will install to
%global modules_gpu_list gfx8 gfx9 gfx10 gfx11 gfx12 gfx906 gfx908 gfx90a gfx942 gfx950 gfx1031 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103 gfx1150 gfx1151 gfx1152 gfx1153 gfx1200 gfx1201
for gpu in %{modules_gpu_list}
do
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/lib/cmake
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/bin
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/include
done
mkdir -p %{buildroot}%{_libdir}/rocm/lib/cmake
mkdir -p %{buildroot}%{_libdir}/rocm/bin
mkdir -p %{buildroot}%{_libdir}/rocm/include

%files
%dir %{_libdir}/rocm
%dir %{_libdir}/rocm/bin
%dir %{_libdir}/rocm/include
%dir %{_libdir}/rocm/lib
%dir %{_libdir}/rocm/gfx8
%dir %{_libdir}/rocm/gfx8/bin
%dir %{_libdir}/rocm/gfx8/include
%dir %{_libdir}/rocm/gfx8/lib
%dir %{_libdir}/rocm/gfx8/lib/cmake
%dir %{_libdir}/rocm/gfx9
%dir %{_libdir}/rocm/gfx9/bin
%dir %{_libdir}/rocm/gfx9/include
%dir %{_libdir}/rocm/gfx9/lib
%dir %{_libdir}/rocm/gfx9/lib/cmake
%dir %{_libdir}/rocm/gfx10
%dir %{_libdir}/rocm/gfx10/bin
%dir %{_libdir}/rocm/gfx10/include
%dir %{_libdir}/rocm/gfx10/lib
%dir %{_libdir}/rocm/gfx10/lib/cmake
%dir %{_libdir}/rocm/gfx11
%dir %{_libdir}/rocm/gfx11/bin
%dir %{_libdir}/rocm/gfx11/include
%dir %{_libdir}/rocm/gfx11/lib
%dir %{_libdir}/rocm/gfx11/lib/cmake
%dir %{_libdir}/rocm/gfx12
%dir %{_libdir}/rocm/gfx12/bin
%dir %{_libdir}/rocm/gfx12/include
%dir %{_libdir}/rocm/gfx12/lib
%dir %{_libdir}/rocm/gfx12/lib/cmake
%dir %{_libdir}/rocm/gfx906
%dir %{_libdir}/rocm/gfx906/bin
%dir %{_libdir}/rocm/gfx906/include
%dir %{_libdir}/rocm/gfx906/lib
%dir %{_libdir}/rocm/gfx906/lib/cmake
%dir %{_libdir}/rocm/gfx908
%dir %{_libdir}/rocm/gfx908/bin
%dir %{_libdir}/rocm/gfx908/include
%dir %{_libdir}/rocm/gfx908/lib
%dir %{_libdir}/rocm/gfx908/lib/cmake
%dir %{_libdir}/rocm/gfx90a
%dir %{_libdir}/rocm/gfx90a/bin
%dir %{_libdir}/rocm/gfx90a/include
%dir %{_libdir}/rocm/gfx90a/lib
%dir %{_libdir}/rocm/gfx90a/lib/cmake
%dir %{_libdir}/rocm/gfx942
%dir %{_libdir}/rocm/gfx942/bin
%dir %{_libdir}/rocm/gfx942/include
%dir %{_libdir}/rocm/gfx942/lib
%dir %{_libdir}/rocm/gfx942/lib/cmake
%dir %{_libdir}/rocm/gfx950
%dir %{_libdir}/rocm/gfx950/bin
%dir %{_libdir}/rocm/gfx950/include
%dir %{_libdir}/rocm/gfx950/lib
%dir %{_libdir}/rocm/gfx950/lib/cmake
%dir %{_libdir}/rocm/gfx1031
%dir %{_libdir}/rocm/gfx1031/bin
%dir %{_libdir}/rocm/gfx1031/include
%dir %{_libdir}/rocm/gfx1031/lib
%dir %{_libdir}/rocm/gfx1031/lib/cmake
%dir %{_libdir}/rocm/gfx1036
%dir %{_libdir}/rocm/gfx1036/bin
%dir %{_libdir}/rocm/gfx1036/include
%dir %{_libdir}/rocm/gfx1036/lib
%dir %{_libdir}/rocm/gfx1036/lib/cmake
%dir %{_libdir}/rocm/gfx1100
%dir %{_libdir}/rocm/gfx1100/bin
%dir %{_libdir}/rocm/gfx1100/include
%dir %{_libdir}/rocm/gfx1100/lib
%dir %{_libdir}/rocm/gfx1100/lib/cmake
%dir %{_libdir}/rocm/gfx1101
%dir %{_libdir}/rocm/gfx1101/bin
%dir %{_libdir}/rocm/gfx1101/include
%dir %{_libdir}/rocm/gfx1101/lib
%dir %{_libdir}/rocm/gfx1101/lib/cmake
%dir %{_libdir}/rocm/gfx1102
%dir %{_libdir}/rocm/gfx1102/bin
%dir %{_libdir}/rocm/gfx1102/include
%dir %{_libdir}/rocm/gfx1102/lib
%dir %{_libdir}/rocm/gfx1102/lib/cmake
%dir %{_libdir}/rocm/gfx1103
%dir %{_libdir}/rocm/gfx1103/bin
%dir %{_libdir}/rocm/gfx1103/include
%dir %{_libdir}/rocm/gfx1103/lib
%dir %{_libdir}/rocm/gfx1103/lib/cmake
%dir %{_libdir}/rocm/gfx1150
%dir %{_libdir}/rocm/gfx1150/bin
%dir %{_libdir}/rocm/gfx1150/include
%dir %{_libdir}/rocm/gfx1150/lib
%dir %{_libdir}/rocm/gfx1150/lib/cmake
%dir %{_libdir}/rocm/gfx1151
%dir %{_libdir}/rocm/gfx1151/bin
%dir %{_libdir}/rocm/gfx1151/include
%dir %{_libdir}/rocm/gfx1151/lib
%dir %{_libdir}/rocm/gfx1151/lib/cmake
%dir %{_libdir}/rocm/gfx1152
%dir %{_libdir}/rocm/gfx1152/bin
%dir %{_libdir}/rocm/gfx1152/include
%dir %{_libdir}/rocm/gfx1152/lib
%dir %{_libdir}/rocm/gfx1152/lib/cmake
%dir %{_libdir}/rocm/gfx1153
%dir %{_libdir}/rocm/gfx1153/bin
%dir %{_libdir}/rocm/gfx1153/include
%dir %{_libdir}/rocm/gfx1153/lib
%dir %{_libdir}/rocm/gfx1153/lib/cmake
%dir %{_libdir}/rocm/gfx1200
%dir %{_libdir}/rocm/gfx1200/bin
%dir %{_libdir}/rocm/gfx1200/include
%dir %{_libdir}/rocm/gfx1200/lib
%dir %{_libdir}/rocm/gfx1200/lib/cmake
%dir %{_libdir}/rocm/gfx1201
%dir %{_libdir}/rocm/gfx1201/bin
%dir %{_libdir}/rocm/gfx1201/include
%dir %{_libdir}/rocm/gfx1201/lib
%dir %{_libdir}/rocm/gfx1201/lib/cmake

%changelog
* Wed Feb 4 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-1
- Initial package
