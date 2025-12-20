%undefine _hardened_build

Name:           btop
Version:        1.4.5
Release:        1%{?dist}
Summary:        Modern and colorful command line resource monitor that shows usage and stats

# The entire source code is ASL 2.0 except:
# ISC:
#  - src/openbsd/internal.h
#  - src/openbsd/sysctlbyname.cpp
#  - src/openbsd/sysctlbyname.h
# MIT:
#  - include/fmt/
#  - src/linux/intel_gpu_top/
# Public Domain
#  - include/widechar_width.hpp
License:        Apache-2.0 AND ISC AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/aristocratos/btop
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  lowdown
%if 0%{?el8}
BuildRequires:  gcc-toolset-12-gcc-c++
BuildRequires:  gcc-toolset-12-annobin-plugin-gcc
BuildRequires:  gcc-toolset-12-binutils
%endif
%if 0%{?el9}
BuildRequires:  gcc-toolset-13-gcc-c++
BuildRequires:  gcc-toolset-13-annobin-plugin-gcc
BuildRequires:  gcc-toolset-13-binutils
%endif

# AMD GPU support
%if 0%{?fedora}
%ifnarch i686 s390x
BuildRequires:  rocm-smi-devel
Recommends: rocm-smi
%endif
%endif

Requires:       hicolor-icon-theme

# Include file from https://gitlab.freedesktop.org/drm/igt-gpu-tools
# Snapshot from 0f02dc176959e6296866b1bafd3982e277a5e44b
Provides:       bundled(igt-gpu-tools) = 1.28^20240731git0f02dc17-1
# Bundling was chosen for widecharwidth as it is not versioned upstream
# and doesn't appear to be a widely-used lib.
Provides:       bundled(widecharwidth)

%description
Resource monitor that shows usage and stats for processor,
memory, disks, network and processes.

C++ version and continuation of bashtop and bpytop.

%prep
%autosetup


%build
%{?el8:. /opt/rh/gcc-toolset-12/enable}
%{?el9:. /opt/rh/gcc-toolset-13/enable}

# to build debuginfo
export CXXFLAGS="${CXXFLAGS} -g"
%make_build


%install
%make_install PREFIX=%{_prefix}
rm -fv %{buildroot}%{_datadir}/btop/README.md
desktop-file-validate %{buildroot}%{_datadir}/applications/btop.desktop


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/btop.desktop
%{_datadir}/btop
%{_datadir}/icons/hicolor/*/apps/btop.*
%{_mandir}/man1/%{name}.1.*


%changelog
* Sat Sep 27 2025 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.5-1
- Update to 1.4.5
- Close: rhbz#2397033
- Refresh license field (analysed with scancode-toolkit)

* Sat Sep 27 2025 Timothée Ravier <tim@siosm.fr> - 1.4.4-2
- Recommend rocm-smi for AMD GPU support.

* Fri Aug 08 2025 Jonathan Wright <jonathan@almalinux.org> - 1.4.4-1
- update to 1.4.4 rhbz#2362554

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 15 2024 Jonathan Wright <jonathan@almalinux.org> - 1.4.0-1
- update to 1.4.0 rhbz#2314092
- add man page

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 12 2024 Jonathan Wright <jonathan@almalinux.org> - 1.3.2-1
- update to 1.3.2 rhbz#2263799

* Tue Jan 30 2024 Jonathan Wright <jonathan@almalinux.org> - 1.3.0-4
- Fix FTBFS by fixing BR for certain arches
- Build EPEL9 with gcc13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Jonathan Wright <jonathan@almalinux.org> - 1.3.0
- Update to 1.3.0 rhbz#2257235
- Add AMD GPU support

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Jonathan Wright <jonathan@almalinux.org> - 1.2.13-3
- fix ftbfs
- update license to SPDX
- use latest gcc on el8/el9
- remove <f36 code from spec

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 08 2022 Jonathan Wright <jonathan@almalinux.org> - 1.2.13-1
- update to 1.2.13 (rhbz#2140887)

* Mon Oct 10 2022 Jonathan Wright <jonathan@almalinux.org> - 1.2.12-1
- update to 1.2.12 (rhbz#2133121)

* Mon Aug 29 2022 Jonathan Wright <jonathan@almalinux.org> - 1.2.9-1
- update to 1.2.9
- rhbz#2122053

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jonathan Wright <jonathan@almalinux.org> - 1.2.8-2
- Update spec file to build on epel8

* Thu Jul 14 2022 Jonathan Wright <jonathan@almalinux.org> - 1.2.8-1
- Initial version of package
