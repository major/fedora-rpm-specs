%bcond_without tests

Name:		oomd
Summary:	Userspace Out-Of-Memory (OOM) killer
Version:	0.5.0
Release:	13%{dist}
License:	GPL-2.0-only
URL:		https://github.com/facebookincubator/oomd/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Check return value for mkstemp()
Patch0:         %{url}/commit/076af42b270388f38055fdf60dccbb3001de723a.patch
# Fix ODR violation in tests
Patch1:         %{url}/commit/3989e169fc0da9c29da8dd692427d4f4c1ace413.patch
# Resolved a compiler error due to lacking include
Patch2:         %{url}/commit/83a6742f08349fbc93f459228dcc3d1f56eac411.patch
# Disable a test that seems to fail on kernel 6.6.9-100.fc38
Patch3:         oomd-disable-datalifecycle-children-test.patch

ExcludeArch:	i686 armv7hl

BuildRequires:	gcc-c++
BuildRequires:	meson >= 0.45
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(libsystemd)
%if %{with tests}
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
%endif
BuildRequires:	systemd-rpm-macros
%{?systemd_requires}

%description
Out of memory killing has historically happened inside kernel space. On a
memory overcommitted linux system, malloc(2) and friends usually never fail.
However, if an application dereferences the returned pointer and the system has
run out of physical memory, the linux kernel is forced take extreme measures,
up to and including killing processes. This is sometimes a slow and painful
process because the kernel can spend an unbounded amount of time swapping in
and out pages and evicting the page cache. Furthermore, configuring policy is
not very flexible while being somewhat complicated.

oomd aims to solve this problem in userspace. oomd leverages PSI and cgroupv2
to monitor a system holistically. oomd then takes corrective action in
userspace before an OOM occurs in kernel space. Corrective action is configured
via a flexible plugin system, in which custom code can be written. By default,
this involves killing offending processes. This enables an unparalleled level
of flexibility where each workload can have custom protection rules.
Furthermore, time spent livedlocked in kernelspace is minimized.

%prep
%autosetup -p1

%build
%meson
%meson_build

%if %{with tests}
%check
%meson_test -v
%endif

%install
%meson_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md docs/
%{_bindir}/oomd
%{_unitdir}/oomd.service
%{_mandir}/man1/oomd.*
%config(noreplace) %{_sysconfdir}/oomd/

%post
%systemd_post oomd.service

%preun
%systemd_preun oomd.service

%postun
%systemd_postun_with_restart oomd.service

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Michel Lind <salimma@fedoraproject.org> - 0.5.0-11
- Enable verbose test output
- Use SPDX license identifier
- Disable DataLifeCycle children comparison while we investigate failure
  with newer kernels

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 09 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.5.0-6
- Backport upstream commit to add a missing include
  Fixes: RHBZ#2113559

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 0.5.0-3
- Rebuild (jsoncpp)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.0-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.4.0-5
- Build for EPEL 8
- Make tests conditional
- Replace gcc-11 patch with upstream commits

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Jeff Law <law@redhat.com> - 0.4.0-3
- Fix missing #includes for gcc-11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Filipe Brandenburger <filbranden@gmail.com> - 0.4.0-1
- Upgrade to v0.4.0

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.3.2-2
- Rebuild (jsoncpp)

* Wed Feb 19 2020 Filipe Brandenburger <filbranden@gmail.com> - 0.3.2-1
- Update to v0.3.2

* Tue Feb 18 2020 Filipe Brandenburger <filbranden@gmail.com> - 0.3.1-1
- Update to v0.3.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.2.0-5
- Rebuild (jsoncpp)

* Thu Sep 12 2019 Filipe Brandenburger <filbranden@gmail.com> - 0.2.0-4
- First official build for Fedora
- Exclude 32-bit architectures, which fail to build.

* Tue Sep 10 2019 Filipe Brandenburger <filbranden@gmail.com> - 0.2.0-3
- Initial release of oomd RPM package
