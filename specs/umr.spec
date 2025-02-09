# UMR is designed to be a static lib
%undefine _cmake_shared_libs

Summary: AMDGPU Userspace Register Debugger
Name: umr
Version: 1.0.10
Release: %autorelease
License: MIT
URL: https://gitlab.freedesktop.org/tomstdenis/umr
Source0: https://gitlab.freedesktop.org/tomstdenis/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

# Upstream fixes to newer GCC
#https://gitlab.freedesktop.org/tomstdenis/umr/-/commit/511d5b9bebd91346ee208dfffed304ed05890d8d
Patch0: 0001-Fix-warnings-treewide.patch

#Glibc is too old prior to EL7, enable rt linking to avoid compilation failure
%if 0%{?rhel} && 0%{?rhel} < 7
%global enablert 1
%endif

#UMR requires llvm >= 7 to enable llvm features, enable for EL8+/F29+
%if 0%{?rhel} > 7 || 0%{?fedora} > 28
BuildRequires: llvm-devel
%else
%global disablellvm 1
%endif

#UMR requires a recent libdrm enable libdrm features, enable for EL8+/Fedora
%if 0%{?rhel} > 7 || 0%{?fedora}
BuildRequires: libdrm-devel
%else
%global disablelibdrm 1
%endif

BuildRequires: cmake%{?rhel:3}
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: libpciaccess-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: nanomsg-devel
BuildRequires: ncurses-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-devel
Requires: bash-completion
#Disable unnecessary arches, as umr requires the amdgpu kernel module:
ExclusiveArch:  x86_64 aarch64 ppc64le

%description
AMDGPU Userspace Register Debugger (UMR) is a tool to read and display, as well
as write to AMDGPU device MMIO, PCIE, SMC, and DIDT registers via userspace.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%{!?cmake:%global cmake %%cmake3}
%cmake %{?disablellvm:-DUMR_NO_LLVM=ON} \
        %{?disablelibdrm:-DUMR_NO_DRM=ON} \
        %{?enablert:-DUMR_NEED_RT=ON} \
        -DCMAKE_BUILD_TYPE="RELEASE"
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/%{name}

%files
%doc README
%license LICENSE
#Note: umrgui is a symlink to umr, so a gui subpackage doesn't seem valuable
%{_bindir}/%{name}*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/bash-completion/completions/%{name}

%changelog
%autochangelog
