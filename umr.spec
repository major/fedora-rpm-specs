%global commit 02f162c927d729b4cb4513c784868f7a0b624d34
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20220107
%global fgittag %{gitdate}git%{shortcommit}

Summary: AMDGPU Userspace Register Debugger
Name: umr
Version: 1.0
Release: 14%{?fgittag:.%{fgittag}}%{?dist}
License: MIT
URL: https://gitlab.freedesktop.org/tomstdenis/umr
Source0: https://gitlab.freedesktop.org/tomstdenis/%{name}/-/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.gz
#This will be sent to the mailing list, upstream already acked the issue
Patch0: 0001-umr-gui-fix-ARM-build.patch

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
BuildRequires: gcc-c++
BuildRequires: libpciaccess-devel
BuildRequires: ncurses-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-devel
Requires: bash-completion

%description
AMDGPU Userspace Register Debugger (UMR) is a tool to read and display, as well
as write to AMDGPU device MMIO, PCIE, SMC, and DIDT registers via userspace.

%package devel
Summary: UMR development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}

%description devel
AMDGPU Userspace Register Debugger header files and libraries

%prep
%autosetup -p1 -n %{name}-%{shortcommit}

%build
%{!?cmake:%global cmake %%cmake3}
%cmake %{?disablellvm:-DUMR_NO_LLVM=ON} \
	%{?disablelibdrm:-DUMR_NO_DRM=ON} \
	%{?enablert:-DUMR_NEED_RT=ON} \
	-DCMAKE_BUILD_TYPE="RELEASE"
%cmake_build

%install
%cmake_install

%files
%doc README
%license LICENSE
#Note: umrgui is a symlink to umr, so a gui subpackage doesn't seem valuable
%{_bindir}/%{name}*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/bash-completion/completions/%{name}

%files devel
%{_includedir}/umr*
%{_libdir}/*.a

%changelog
* Mon Sep 19 2022 Pete Walter <pwalter@fedoraproject.org> - 1.0-14.20220107git02f162c
- Rebuild for llvm 15

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13.20220107git02f162c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12.20220107git02f162c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.0-11.20220107git02f162c
- Update to newer git

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.20210115git8bf83ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 20 2021 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.0-9.20210115git8bf83ae
- Update to newer git

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8.20200709gitcf9e2f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.0-7.20200709gitcf9e2f8
- Update to newer git
- Drop static llvm dependency

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6.20191210git0affde7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5.20191210git0affde7
- Update to newer git

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4.20190514gitcb1cb54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> 1.0-3.20190514gitcb1cb54
- Update to newer git, switch to gitlab

* Wed Apr 03 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> 1.0-2.20190403git1139876
- Update to newer git, fixes install issues and all patches upstreamed
- Add missing static provides for devel

* Thu Mar 21 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> 1.0-1.20190322.git51112c7
- Intial Package
