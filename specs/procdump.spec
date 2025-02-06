# Name of the upstream GitHub repository.
%global repo_name ProcDump-for-Linux

Name:           procdump
Version:        3.4.0
Release:        1%{?dist}
Summary:        Sysinternals process dump utility

License:        MIT
URL:            https://github.com/Microsoft/%{repo_name}
Source:         %{url}/archive/%{version}/%{repo_name}-%{version}.tar.gz
Patch1:         0001-Monitor-remove-useless-variables-267.patch
Patch2:         0002-CMake-Add-ability-to-use-system-installed-libbpf-rat.patch
Patch3:         0003-cmake-Include-install-section-for-procdump-and-its-m.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  libbpf-devel
BuildRequires:  bpftool
BuildRequires:  git
BuildRequires:  zlib-devel
Requires:       gdb >= 7.6.1

%undefine _annotated_build
%undefine _hardened_build

# ProcDump does not support PPC64 (#163) and s390x.
# For further information see ./ebpf/vmlinux.h.
ExclusiveArch:    x86_64 aarch64

%description
ProcDump is a command-line utility whose primary purpose is monitoring an application
for various resources and generating crash dumps during a spike that an administrator
or developer can use to determine the cause of the issue. ProcDump also serves as a
general process dump utility that you can embed in other scripts.


%prep
%autosetup -p1 -n %{repo_name}-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%doc procdump.gif
%{_bindir}/procdump
%{_mandir}/man1/procdump.1.gz



%changelog
* Tue Feb 04 2025 Julio Faracco <jfaracco@redhat.com> - 3.4.0-1
- Add ARM64 support
- Fix clang compilation errors due to variable length arrays

* Wed Jan 22 2025 Julio Faracco <jfaracco@redhat.com> - 3.3.0-1
- Adds improvements related to containerized workflows (3.3)
- Adds mmap/munmap to resource tracking (3.2)
- Adds ability to specify multiple comma separated signals (3.1)
- Adds the new -mc switch which controls what type of memory is included in the core dumps (3.1)
- Adds resource tracking and reporting feature (3.0)
- Adds Azure Linux package (2.2)
- Fixes memory leaks (2.2)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 28 2023 Julio Faracco <jfaracco@redhat.com> - 2.1-1
- New upstream release 2.1
- Fix issue with missing va_end() call inside GetClientDataHelper (#204).

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Matěj Grabovský <mgrabovs@redhat.com> - 1.3-1
- New upstream release 1.3
- BREAKING CHANGE: CLI interface has been changed to match ProcDump for Windows.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Matěj Grabovský <mgrabovs@redhat.com> - 1.2-3
- Fix failing build (patch by Sergei Trofimovich)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Matěj Grabovský <mgrabovs@redhat.com> - 1.2-1
- New upstream release 1.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Matěj Grabovský <mgrabovs@redhat.com> - 1.1.1-1
- Added -T thread count trigger and -F file descriptor count trigger

* Thu Feb 20 2020 Matěj Grabovský <mgrabovs@redhat.com> - 1.1-3
- Fix build with GCC 10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Matěj Grabovský <mgrabovs@redhat.com> - 1.1-1
- Add command line parameter (-w) for targetting the name of a process
- Small bug fixes

* Fri Oct 04 2019 Matěj Grabovský <mgrabovs@redhat.com> - 1.0.1-1
- Initial release
