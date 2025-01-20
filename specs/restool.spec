# The labled version is different to the tag and we need specific feature
# branch for the NXP LX2160A functionality
# https://github.com/nxp-qoriq/restool
# git archive --format=tar --prefix=restool-2.4.0/ abd2f5b | xz > restool-%{version}-%{gittag}.tar.xz
%define gittag 443e5fa

Name:      restool
Version:   2.4.0
Release:   12.%{gittag}%{?dist}
Summary:   A tool to create and manage the DPAA2 Management Complex (MC)
# Automatically converted from old format: BSD or GPLv2+ - review is highly recommended.
License:   LicenseRef-Callaway-BSD OR GPL-2.0-or-later
URL:       https://github.com/nxp-qoriq/restool
Source:    %{name}-%{version}-%{gittag}.tar.xz
# udev rule for creating ethX devices
Source1:   fsl_mc_bus.rules

# HW specific to NXP Layerscape arm SoCs with DPAA2
ExclusiveArch: aarch64
BuildRequires: gcc
BuildRequires: make
BuildRequires: pandoc

%description
restool is a user space application providing the ability to dynamically
create and manage DPAA2 containers and objects from Linux.

restool interacts with the DPAA2 Management Complex (MC).  It uses an ioctl to
send MC commands, and thus requires a Linux kernel driver providing the needed
ioctl support.

%prep
%autosetup -p1

%build
# the maybe-uninitialized has been reported to upstream
%{make_build} EXTRA_CFLAGS="%{build_cflags} -Wno-error=maybe-uninitialized" LDFLAGS="%{build_ldflags}"

%install
%{make_install} prefix=%{_usr}
mkdir -p %{buildroot}/etc/udev/rules.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/udev/rules.d/

%files
%license LICENSE
%{_bindir}/restool
%{_bindir}/ls-*
%{_datadir}/bash-completion/completions/restool
%{_mandir}/man1/restool*
%{_sysconfdir}/udev/rules.d/fsl_mc_bus.rules

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12.443e5fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 30 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 2.4.0-11.443e5fa
- Move to new upstream and a git snapshot

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 06 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2.4.0-4
- Add udev rules for configurations (jlinton)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Wed Jul 28 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.3.0-1
- Initial package
