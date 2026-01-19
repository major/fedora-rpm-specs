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
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           rocm
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        ROCm tools for computing on AMD GPU
License:        MIT

Source0:        License.txt

BuildArch: noarch
# ROCm only working on x86_64
ExclusiveArch:  x86_64

Requires: amdsmi >= %{rocm_release}
Requires: hipblas >= %{rocm_release}
Requires: hipcc
Requires: hipfft >= %{rocm_release}
Requires: hiprand >= %{rocm_release}
Requires: hipsolver >= %{rocm_release}
Requires: hipsparse >= %{rocm_release}
Requires: rocblas >= %{rocm_release}
Requires: rocfft >= %{rocm_release}
Requires: rocm-clang
Requires: rocm-hip >= %{rocm_release}
Requires: rocminfo >= %{rocm_release}
Requires: rocm-runtime >= %{rocm_release}
Requires: rocm-smi >= %{rocm_release}
Requires: rocrand >= %{rocm_release}
Requires: rocsolver >= %{rocm_release}
Requires: rocsparse >= %{rocm_release}

%if 0%{?fedora}
Requires: aqlprofile
Requires: hipblaslt >= %{rocm_release}
Requires: hipsparselt
Requires: migraphx
Requires: miopen >= %{rocm_release}
Requires: mivisionx >= %{rocm_release}
Requires: rccl >= %{rocm_release}
Requires: rocal >= %{rocm_release}
Requires: rocalution >= %{rocm_release}
Requires: rocdecode >= %{rocm_release}
Requires: rocjpeg >= %{rocm_release}
Requires: rocm-clinfo >= %{rocm_release}
Requires: rocm-core >= %{rocm_release}
Requires: rocm-omp >= %{rocm_release}
Requires: rocm-opencl >= %{rocm_release}
Requires: rocm-origami
Requires: rocm-rpp >= %{rocm_release}
Requires: rocprofiler-register >= %{rocm_release}
Requires: roctracer >= %{rocm_release}
%endif

%if 0%{?suse_version}
Requires: hipblaslt >= %{rocm_release}
Requires: miopen >= %{rocm_release}
Requires: rccl >= %{rocm_release}
Requires: rocalution >= %{rocm_release}
Requires: rocm-clinfo >= %{rocm_release}
Requires: rocm-core >= %{rocm_release}
Requires: rocm-opencl >= %{rocm_release}
Requires: roctracer >= %{rocm_release}
%endif

%description
This is a collection of ROCm tools and libraries for programming
AMD graphics processing units.

%package devel
Summary:        Development environment for ROCm
Requires: amdsmi-devel >= %{rocm_release}
Requires: half-devel
Requires: hipblas-common-devel >= %{rocm_release}
Requires: hipblas-devel >= %{rocm_release}
Requires: hipcub-devel >= %{rocm_release}
Requires: hipfft-devel >= %{rocm_release}
Requires: hiprand-devel >= %{rocm_release}
Requires: hipsolver-devel >= %{rocm_release}
Requires: hipsparse-devel >= %{rocm_release}
Requires: rocblas-devel >= %{rocm_release}
Requires: rocfft-devel >= %{rocm_release}
Requires: rocm-clang-devel
Requires: rocm-cmake >= %{rocm_release}
Requires: rocm-compilersupport-macros
Requires: rocm-hip-devel >= %{rocm_release}
Requires: rocm-rpm-macros >= %{rocm_release}
Requires: rocm-rpm-macros-modules >= %{rocm_release}
Requires: rocm-runtime-devel >= %{rocm_release}
Requires: rocm-smi-devel >= %{rocm_release}
Requires: rocprim-devel >= %{rocm_release}
Requires: rocrand-devel >= %{rocm_release}
Requires: rocsolver-devel >= %{rocm_release}
Requires: rocsparse-devel >= %{rocm_release}

%if 0%{?fedora}
Requires: aqlprofile-devel
Requires: hipblaslt-devel >= %{rocm_release}
Requires: hipsparselt-devel
Requires: hipify >= %{rocm_release}
Requires: migraphx
Requires: miopen-devel >= %{rocm_release}
Requires: mivisionx-devel >= %{rocm_release}
Requires: python3-tensile-devel >= %{rocm_release}
Requires: rccl-devel >= %{rocm_release}
Requires: rocal-devel >= %{rocm_release}
Requires: rocalution-devel >= %{rocm_release}
Requires: rocdecode-devel >= %{rocm_release}
Requires: rocjpeg-devel >= %{rocm_release}
Requires: rocm-core-devel >= %{rocm_release}
Requires: rocm-examples >= %{rocm_release}
Requires: rocm-omp-static >= %{rocm_release}
Requires: rocm-rpp-devel >= %{rocm_release}
Requires: rocprofiler-register-devel >= %{rocm_release}
Requires: rocthrust-devel >= %{rocm_release}
Requires: roctracer-devel >= %{rocm_release}
Requires: rocm-origami-devel
Requires: rocwmma-devel >= %{rocm_release}
%endif

%if 0%{?suse_version}
Requires: hipblaslt-devel >= %{rocm_release}
Requires: miopen-devel >= %{rocm_release}
Requires: rccl-devel >= %{rocm_release}
Requires: rocalution-devel >= %{rocm_release}
Requires: rocm-core-devel >= %{rocm_release}
Requires: rocm-opencl-devel >= %{rocm_release}
Requires: roctracer-devel >= %{rocm_release}
%endif

%description devel
This is a meta package for all of the ROCm devel packages.

%package test
Summary:        Tests for ROCm
Requires: kfdtest             >= %{rocm_release}
%if 0%{?fedora}
Requires: hip-tests >= %{rocm_release}
Requires: rccl-tests
Requires: rocm-bandwidth-test
Requires: rocblas-test >= %{rocm_release}
Requires: rocm-validation-suite >= %{rocm_release}
%endif

%description test
This is a meta package for all of the ROCm test packages.

%prep
%setup -cT
install -pm 644 %{SOURCE0} .

%build

%install

%files
%license License.txt

%files devel
%license License.txt

%files test
%license License.txt

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Nov 16 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- For fedora add migraphx, rccl-tests, rocm-origami

* Wed Nov 12 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Wed Oct 29 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-2
- Improve description

* Thu Oct 2 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Thu Sep 11 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-4
- Add rocprofiler-register, rocm-validation-suite

* Thu Aug 28 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-3
- Add Fedora copyright

* Mon Aug 18 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-2
- rocm-opencl-devel has a conflict on fedora

* Thu Aug 7 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-1
- Add rocm-bandwidth-test to fedora

* Mon Jul 28 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-1
- Add aqlprofile and hipsparselt to fedora

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 16 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.1-2
- Add a suse version

* Wed Jun 11 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.1-1
- Simplify RHEL changes

* Wed May 28 2025 Tim Flink <tflink@fedoraproject.org> - 6.4.0-3
- hipify is not part of the set we intend to build for EL for now

* Tue May 27 2025 Tim Flink <tflink@fedoraproject.org> - 6.4.0-2
- Don't require yet-unpackaged deps in EL builds

* Tue Apr 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.0-1
- Update to 6.4.0
- Use version requires to pull in newer packages
- Fix rpmlint warnings
- Package is now noarch

* Sat Mar 29 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-3
- Add rocm-examples

* Fri Mar 21 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-2
- Add rocal
- Move hipify to devel

* Fri Mar 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-1
- Initial package
