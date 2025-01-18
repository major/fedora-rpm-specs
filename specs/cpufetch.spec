Name: cpufetch
Summary: Simple tool for determining CPU architecture
License: GPL-2.0-only

Version: 1.06
Release: 2%{?dist}

URL: https://github.com/Dr-Noob/cpufetch
Source0: %{URL}/archive/v%{version}/%{name}-v%{version}.tar.gz

# The program has a couple of off-by-one errors
# which make it allocate buffers that can't fit the data.
#
# Reported upstream: https://github.com/Dr-Noob/cpufetch/issues/264
Patch0: 0000-off-by-one-errors.patch

# Program assumes that a processor must have an L2 cache,
# and crashes if it does not.
Patch1: 0001-L2-cache-may-not-exist.patch

BuildRequires: gcc
BuildRequires: make

# Supports only x86_64, ARM, PowerPC and RISC-V
ExclusiveArch: %{arm} aarch64 x86_64 ppc ppc64 ppc64le %{riscv}


%description
%{name} is a simple, yet fancy, CPU architecture fetching tool.
It currently supports x86_64 CPUs (both Intel and AMD), ARM, and PowerPC.


%prep
%autosetup -p1


%build
%make_build


%install
%make_install

# "make install" installs the LICENSE file as well
rm %{buildroot}%{_datadir}/licenses/cpufetch-git/LICENSE
# The man page is not actually gzipped
mv %{buildroot}%{_mandir}/man1/%{name}.1{.gz,}


%check
# Try running the program to see if it doesn't crash
%{buildroot}%{_bindir}/%{name} --debug


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 18 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.06-1
- Update to v1.06

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.05-1
- Update to v1.05

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 06 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.04-1
- Update to v1.04
- Drop Patch0 (build failure on PowerPC - fixed upstream)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.03-1
- Update to v1.03
- Add a patch to fix build failures on PowerPC
- Migrate License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 24 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.02-1
- Update to v1.02
- Update License tag: license changed from MIT to GPLv2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.01-1
- Update to v1.01

* Mon Aug 23 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.00-1
- Update to v1.00

* Tue Aug 17 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.99-1
- Update to v0.99
- Add PowerPC to ExclusiveArch list (now supported)
- Try running the program in %%check

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.98-1
- Update to v0.98
- Use "make install" instead of copying files manually

* Mon Apr 05 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.94-2
- Preserve timestamps when installing

* Sat Apr 03 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.94-1
- Initial packaging
