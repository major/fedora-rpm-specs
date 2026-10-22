# TPM1 requires tpm-tools, is unwanted in RHEL
%ifnarch %{ix86}
%bcond tpm1 %{undefined rhel}
%endif

%global dracut_prio 50

Name:           clevis
Version:        24
Release:        %autorelease
Summary:        Automated decryption framework

License:        GPL-3.0-or-later
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        clevis.sysusers

Patch0001:      0001-Fix-truncation-errors-happening-when-O2-enabled.patch
Patch0002:      0002-pkcs11-test-non-root-rejection-in-afunix-socket-unlo.patch
Patch0003:      0003-include-setgroups-and-set-library-as-shared-mod.patch

BuildRequires:  git-core
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  asciidoc
BuildRequires:  ninja-build
BuildRequires:  bash-completion
BuildRequires:  bash-completion-devel

BuildRequires:  libjose-devel >= 8
BuildRequires:  libluksmeta-devel >= 8
BuildRequires:  audit-libs-devel
BuildRequires:  libudisks2-devel
BuildRequires:  openssl-devel

BuildRequires:  tpm2-tools >= 4.0.0
%if %{with tpm1}
BuildRequires:  tpm-tools
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  dracut
BuildRequires:  tang >= 6
BuildRequires:  curl
BuildRequires:  luksmeta
BuildRequires:  openssl
BuildRequires:  diffutils
BuildRequires:  cryptsetup
BuildRequires:  jq
BuildRequires:  pcsc-lite
BuildRequires:  opensc
BuildRequires:  socat
BuildRequires:  lsof


Requires:       tpm2-tools >= 4.0.0
Requires:       coreutils
Requires:       jose >= 8
Requires:       curl
Requires:       jq
Requires(post): systemd
Requires:       clevis-pin-tpm2

%description
Clevis is a framework for automated decryption. It allows you to encrypt
data using sophisticated unlocking policies which enable decryption to
occur automatically.

The clevis package provides basic encryption/decryption policy support.
Users can use this directly; but most commonly, it will be used as a
building block for other packages. For example, see the clevis-luks
and clevis-dracut packages for automatic root volume unlocking of
LUKSv1/LUKSv2 volumes during early boot.

%package luks
Summary:        LUKS integration for clevis
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cryptsetup
Requires:       luksmeta >= 8

%description luks
LUKS integration for clevis. This package allows you to bind a LUKS
volume to a clevis unlocking policy. For automated unlocking, an unlocker
will also be required. See, for example, clevis-dracut and clevis-udisks2.

%package systemd
Summary:        systemd integration for clevis
Requires:       %{name}-luks%{?_isa} = %{version}-%{release}
%if 0%{?fedora} > 27
Requires:       systemd%{?_isa} >= 235-3
%else
%if 0%{?fedora} == 27
Requires:       systemd%{?_isa} >= 234-9
%else
%if 0%{?fedora} == 26
Requires:       systemd%{?_isa} >= 233-7
%else
Requires:       systemd%{?_isa} >= 236
%endif
%endif
%endif

%description systemd
Automatically unlocks LUKS _netdev block devices from /etc/crypttab.

%package dracut
Summary:        Dracut integration for clevis
Requires:       %{name}-systemd%{?_isa} = %{version}-%{release}
Requires:       dracut-network

%description dracut
Automatically unlocks LUKS block devices in early boot.

%package udisks2
Summary:        UDisks2/Storaged integration for clevis
Requires:       %{name}-luks%{?_isa} = %{version}-%{release}

%description udisks2
Automatically unlocks LUKS block devices in desktop environments that
use UDisks2 or storaged (like GNOME).

%package pin-pkcs11
Summary:        PKCS#11 for clevis
Requires:       %{name}-systemd%{?_isa} = %{version}-%{release}
Requires:       %{name}-luks%{?_isa} = %{version}-%{release}
Requires:       %{name}-dracut%{?_isa} = %{version}-%{release}
Requires:       pcsc-lite
Requires:       opensc
Requires:       socat
Requires:       openssl

%description pin-pkcs11
Automatically unlocks LUKS block devices through a PKCS#11 device.

%if %{with tpm1}
%package pin-tpm1
Summary:        TPM 1.2 pin for clevis
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-systemd%{?_isa} = %{version}-%{release}
Requires:       %{name}-dracut%{?_isa} = %{version}-%{release}
Requires:       tpm-tools

%description pin-tpm1
Automated decryption using a TPM 1.2 device.
%endif

%prep
%autosetup -S git

%build
%meson -Duser=clevis -Dgroup=clevis \
%if %{with tpm1}
  -Dtpm1=enabled
%else
  -Dtpm1=disabled
%endif
%meson_build

%install
%meson_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/clevis.conf

%check
desktop-file-validate \
  %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}-luks-udisks2.desktop
%meson_test

%files
%license COPYING
%{_datadir}/bash-completion/
%{_bindir}/%{name}-decrypt-tang
%{_bindir}/%{name}-decrypt-tpm2
%{_bindir}/%{name}-decrypt-sss
%{_bindir}/%{name}-decrypt-null
%{_bindir}/%{name}-decrypt-file
%{_bindir}/%{name}-decrypt
%{_bindir}/%{name}-encrypt-tang
%{_bindir}/%{name}-encrypt-tpm2
%{_bindir}/%{name}-encrypt-sss
%{_bindir}/%{name}-encrypt-null
%{_bindir}/%{name}-encrypt-file
%{_bindir}/%{name}
%{_mandir}/man1/%{name}-encrypt-tang.1*
%{_mandir}/man1/%{name}-encrypt-tpm2.1*
%{_mandir}/man1/%{name}-encrypt-sss.1*
%{_mandir}/man1/%{name}-encrypt-file.1*
%{_mandir}/man1/%{name}-decrypt.1*
%{_mandir}/man1/%{name}.1*
%{_sysusersdir}/clevis.conf

%files luks
%{_mandir}/man7/%{name}-luks-unlockers.7*
%{_mandir}/man1/%{name}-luks-unlock.1*
%{_mandir}/man1/%{name}-luks-unbind.1*
%{_mandir}/man1/%{name}-luks-bind.1*
%{_mandir}/man1/%{name}-luks-list.1.*
%{_mandir}/man1/%{name}-luks-edit.1.*
%{_mandir}/man1/%{name}-luks-regen.1.*
%{_mandir}/man1/%{name}-luks-report.1.*
%{_mandir}/man1/%{name}-luks-pass.1.*
%{_bindir}/%{name}-luks-unlock
%{_bindir}/%{name}-luks-unbind
%{_bindir}/%{name}-luks-bind
%{_bindir}/%{name}-luks-common-functions
%{_bindir}/%{name}-luks-list
%{_bindir}/%{name}-luks-edit
%{_bindir}/%{name}-luks-regen
%{_bindir}/%{name}-luks-report
%{_bindir}/%{name}-luks-pass

%files systemd
%{_libexecdir}/%{name}-luks-askpass
%{_unitdir}/%{name}-luks-askpass.path
%{_unitdir}/%{name}-luks-askpass.service

%files dracut
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}
%dir %{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-null
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-null/module-setup.sh
%dir %{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-sss
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-sss/module-setup.sh
%dir %{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-tang
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-tang/module-setup.sh
%dir %{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-tpm2
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-tpm2/module-setup.sh
%dir %{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-file
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-file/module-setup.sh

%files udisks2
%{_sysconfdir}/xdg/autostart/%{name}-luks-udisks2.desktop
%attr(4755, root, root) %{_libexecdir}/%{name}-luks-udisks2

%files pin-pkcs11
%{_libexecdir}/%{name}-luks-pkcs11-askpass
%{_libexecdir}/%{name}-luks-pkcs11-askpin
%{_bindir}/%{name}-decrypt-pkcs11
%{_bindir}/%{name}-encrypt-pkcs11
%{_bindir}/%{name}-pkcs11-afunix-socket-unlock
%{_bindir}/%{name}-pkcs11-common
%{_unitdir}/%{name}-luks-pkcs11-askpass.service
%{_unitdir}/%{name}-luks-pkcs11-askpass.socket
%{_mandir}/man1/%{name}-encrypt-pkcs11.1*
%dir %{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-pkcs11
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-pkcs11/module-setup.sh
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-pkcs11/%{name}-pkcs11-prehook.sh
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-pkcs11/%{name}-pkcs11-hook.sh

%if %{with tpm1}
%files pin-tpm1
%{_bindir}/%{name}-decrypt-tpm1
%{_bindir}/%{name}-encrypt-tpm1
%{_libdir}/libclevis-tpm1-tcsd-preload.so
%{_libexecdir}/%{name}-luks-tpm1-functions
%{_mandir}/man1/%{name}-encrypt-tpm1.1*
%dir %{_unitdir}/tcsd.service.d
%{_unitdir}/tcsd.service.d/%{name}-tcsd.conf
%dir %{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-tpm1
%{_prefix}/lib/dracut/modules.d/%{dracut_prio}%{name}-pin-tpm1/module-setup.sh
%endif

%post systemd
systemctl preset %{name}-luks-askpass.path >/dev/null 2>&1 || :

%changelog
%autochangelog
