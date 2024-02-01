%global rocm_release 6.0
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname rocm_smi_lib

Name:       rocm-smi
Version:    %{rocm_version}
Release:    %autorelease
Summary:    ROCm System Management Interface Library

License:    NCSA and MIT and BSD
URL:        https://github.com/RadeonOpenCompute/%{upstreamname}
Source0:    %{url}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# https://github.com/ROCm/rocm_smi_lib/pull/156
Patch0:     0001-remove-const-for-ScopeGuard-operator.patch

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
%{_libdir}/librocm_smi64.so.1{,.*}
%{_libdir}/liboam.so.1{,.*}
%exclude %{_docdir}/rocm_smi/LICENSE.txt

%files devel
%{_includedir}/rocm_smi/
%{_includedir}/oam/
%{_libdir}/librocm_smi64.so
%{_libdir}/liboam.so
%{_libdir}/cmake/rocm_smi/

%changelog
%autochangelog
