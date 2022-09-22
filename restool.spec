# The labled version is different to the tag and we need specific feature
# branch for the NXP LX2160A functionality
# https://source.codeaurora.org/external/qoriq/qoriq-components/restool
# branch integration
# git archive --format=tar --prefix=restool-2.4.0/ abd2f5b | xz > restool-2.4.0.tar.xz

Name:      restool
Version:   2.4.0
Release:   4%{?dist}
Summary:   A tool to create and manage the DPAA2 Management Complex (MC)
License:   BSD or GPLv2+
URL:       https://source.codeaurora.org/external/qoriq/qoriq-components/restool
Source:    %{name}-%{version}.tar.xz
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
%license COPYING
%{_bindir}/restool
%{_bindir}/ls-*
%{_datadir}/bash-completion/completions/restool
%{_mandir}/man1/restool*
%{_sysconfdir}/udev/rules.d/fsl_mc_bus.rules

%changelog
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
