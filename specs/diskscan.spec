Summary: Scan disk for bad or near failure sectors, performs disk diagnostics
Name: diskscan
Version: 0.21
Release: 4%{?dist}
URL: https://github.com/baruch/diskscan
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: %{name}-version.patch
Patch1: %{name}-cmake-4.0.patch
# hdrhistogram: CC0 or BSD (2-clause)
# libscsicmd: ASL 2.0
# progressbar: BSD (3-clause, no advertising)
# the rest: GPLv3+
License: Apache-2.0 AND BSD-3-Clause AND (BSD-2-Clause OR CC0-1.0) AND GPL-3.0-or-later
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ncurses-devel
BuildRequires: ninja-build
BuildRequires: zlib-devel

%description
DiskScan is a Unix/Linux tool to scan a block device and check if there are
unreadable sectors, in addition it uses read latency times as an assessment for
a near failure as sectors that are problematic to read usually entail many
retries. This can be used to assess the state of the disk and maybe decide on a
replacement in advance to its imminent failure. The disk self test may or may
not pick up on such clues depending on the disk vendor decision making logic.

%prep
%autosetup -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 18 2025 Dominik Mierzejewski <dominik@greysector.net> 0.21-1
- update to 0.21
- clarify BSD variants in the License tag
- fix build with CMake 4.0 (resolves rhbz#2380542)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 29 2022 Dominik Mierzejewski <dominik@greysector.net> 0.20-2
- add a break-down of all licenses

* Fri Mar 18 2022 Dominik Mierzejewski <dominik@greysector.net> 0.20-1
- initial build
