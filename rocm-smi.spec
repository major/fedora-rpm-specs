%global rocm_release 5.6
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname rocm_smi_lib

Name:       rocm-smi
Version:    %{rocm_version}
Release:    2%{?dist}
Summary:    ROCm System Management Interface Library

License:    NCSA and MIT and BSD
URL:        https://github.com/RadeonOpenCompute/%{upstreamname}
Source0:    %{url}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

# I've sent these patches upstream by email and have been merged into 5.7:
Patch0:     0001-Fix-python-script-install-permissions.patch
Patch1:     0002-Fix-version-file-generation.patch
Patch2:     0003-Update-default-version-to-match-tags.patch
Patch3:     0004-Improve-handling-of-ContructBDFID-errors.patch
Patch4:     0005-Fix-python-loading-of-librocm_smi64.patch
Patch5:     0006-Only-install-asan-license-if-enabled.patch

# SMI requires the AMDGPU kernel module, which only builds on:
ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  cmake
# Fedora 38 has doxygen 1.9.6
%if 0%{?fedora} > 38
BuildRequires:  doxygen >= 1.9.7
BuildRequires:  doxygen-latex >= 1.9.7
%endif
BuildRequires:  gcc-c++

%description
The ROCm System Management Interface Library, or ROCm SMI library, is part of
the Radeon Open Compute ROCm software stack . It is a C library for Linux that
provides a user space interface for applications to monitor and control GPU
applications.

%package devel
Summary: ROCm SMI Library development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
ROCm System Management Interface Library development files

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p1

# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

%build
%cmake -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF
%cmake_build

%install
%cmake_install

# For Fedora < 38, the README is not installed if doxygen is disabled:
install -D -m 644 README.md %{buildroot}%{_docdir}/rocm_smi/README.md

%files
%doc %{_docdir}/rocm_smi
%license License.txt
%{_bindir}/rocm-smi
%{_libexecdir}/rocm_smi
%{_libdir}/librocm_smi64.so.5{,.*}
%{_libdir}/liboam.so.1{,.*}
%exclude %{_docdir}/rocm_smi/LICENSE.txt

%files devel
%{_includedir}/rocm_smi/
%{_includedir}/oam/
%{_libdir}/librocm_smi64.so
%{_libdir}/liboam.so
%{_libdir}/cmake/rocm_smi/

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.6.0-1
- Update to 5.6.0
- Replace fixes with upstream patches

* Sun Jun 25 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-2
- Rename to rocm-smi to replace existing retired package
- Add patches to fix soversion

* Fri Jun 23 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.5.1-1
- Complete rewrite of spec file (start from scratch)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
 
* Tue Dec 22 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 4.0.0-1
- Upstream version 4.0.0 (no changes whatsoever, still deprecated)
 
* Fri Dec 11 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.10.0-1
- Upstream version 3.10.0 (no changes whatsoever, still deprecated)
 
* Thu Nov 19 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.9.0-1
- Upstream version 3.9.0 (no changes except deprecation)
- Deprecate package
 
* Thu Oct 15 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 3.8.0-1
- Initial import (#1885684)
