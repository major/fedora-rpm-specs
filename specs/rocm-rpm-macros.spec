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
Name:           rocm-rpm-macros
Version:        7.1.0
Release:        4%{?dist}
Summary:        ROCm RPM macros
License:        GPL-2.0-or-later

URL:            https://github.com/trixirt/rocm-rpm-macros
Source0:        macros.rocm
Source1:        GPL
# Modules
Source2:        default
Source3:        gfx8
Source4:        gfx9
Source5:        gfx10
Source6:        gfx11
Source7:        gfx906
Source8:        gfx908
Source9:        gfx90a
Source10:       gfx942
Source11:       gfx1031
Source12:       gfx1036
Source13:       gfx1100
Source14:       gfx1101
Source15:       gfx1102
Source16:       gfx1103
Source17:       default.rhel
Source18:       gfx12
Source19:       gfx950

# Just some files
%global debug_package %{nil}

Requires:       rpm
%if 0%{?suse_version}
Requires:       Modules
%else
Requires:       environment-modules
%endif
# Only infra files
BuildArch: noarch
# ROCm only working on x86_64
ExclusiveArch:  x86_64
%description
This package contains ROCm RPM macros for building ROCm packages.

# To use, run
# $> source /etc/profile.d/modules.sh
%package modules
Summary: ROCm enviroment modules
%if 0%{?suse_version}
Requires:       Modules
%else
Requires: environment(modules)
Requires: cmake-filesystem
Requires: rocm-llvm-filesystem
%endif

%description modules
This package contains ROCm environment modules for switching
between different GPU families.

%prep
%setup -cT
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
mkdir modules
%if 0%{?rhel}
install -pm 644 %{SOURCE17} modules/default
%else
install -pm 644 %{SOURCE2} modules
%endif
install -pm 644 %{SOURCE3} modules
install -pm 644 %{SOURCE4} modules
install -pm 644 %{SOURCE5} modules
install -pm 644 %{SOURCE6} modules
install -pm 644 %{SOURCE7} modules
install -pm 644 %{SOURCE8} modules
install -pm 644 %{SOURCE9} modules
install -pm 644 %{SOURCE10} modules
install -pm 644 %{SOURCE11} modules
install -pm 644 %{SOURCE12} modules
install -pm 644 %{SOURCE13} modules
install -pm 644 %{SOURCE14} modules
install -pm 644 %{SOURCE15} modules
install -pm 644 %{SOURCE16} modules
install -pm 644 %{SOURCE18} modules
install -pm 644 %{SOURCE19} modules

%install
mkdir -p %{buildroot}%{_rpmmacrodir}/
install -Dpm 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/
%if 0%{?suse_version}
mkdir -p %{buildroot}%{_datadir}/modules/rocm/
cp -p modules/* %{buildroot}%{_datadir}/modules/rocm/
%else
mkdir -p %{buildroot}%{_datadir}/modulefiles/rocm/
cp -p modules/* %{buildroot}%{_datadir}/modulefiles/rocm/
%endif

%files
%license GPL
%{_rpmmacrodir}/macros.rocm

%files modules
%license GPL
%if 0%{?suse_version}
%{_datadir}/modules
%else
%{_datadir}/modulefiles/rocm/
%endif

%changelog
* Sat Dec 6 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-4
- Update hipblaslt list

* Thu Nov 20 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-3
- Update rccl list

* Fri Nov 7 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-2
- Add gfx1036

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Tue Sep 16 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.0-1
- Update to 7.0.0

* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-2
- Add Fedora copyright

* Sun Jul 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.2-1
- Add gfx950,gfx1153 to default list

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri May 9 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.0-4
- Add gfx950 module

* Wed Apr 16 2025 Tim Flink <tflink@fedoraproject.org> - 6.4.0-3
- fixing typo in rocm_gpu_list_test macro

* Tue Apr 15 2025 Tim Flink <tflink@fedoraproject.org> - 6.4.0-2
- renamed rocm_gpu_test_list to rocm_gpu_list_test to better match existing macro names

* Tue Apr 15 2025 Tim Flink <tflink@fedoraproject.org> - 6.4.0-1
- bumped version for 6.4.0 release, corrected one test ISA

* Tue Apr 15 2025 Tim Flink <tflink@fedoraproject.org> - 6.3.2-3
- added rocm_gpu_test_list to specify ISAs that tests are built for

* Sun Feb 9 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-2
- Add ROCM_ALT* env for default module

* Wed Feb 5 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-1
- Update to 6.3.2
- Add some gpu lists

* Thu Jan 23 2025 Christoph Junghans <junghans@votca.org> - 6.3.1-6
- Add ROCM_INCLUDE to modules

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-5
- Move lib64/rocm creation to rocm-compilersupport

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-4
- Cleanup dir ownership

* Thu Jan 16 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-3
- Add gfx1150 to default set

* Wed Jan 15 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- Add gfx1152,gfx1200,gfx1201 to default set

* Mon Dec 30 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Add hipblaslt gpu list

* Sun Dec 8 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed
