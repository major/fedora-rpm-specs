%global commit 8739c5c1d6621e4fd1e9618f19671c304cd91d84
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20260116

Name:           dynamic-hibernate
Version:        0.1.0%{?commitdate:~git%{commitdate}.%{shortcommit}}
Release:        1%{?dist}
Summary:        Automatic dynamic swapfile management on Btrfs for hibernation

# No code uses CC0, just documentation and unused Cargo.lock
SourceLicense:  (GPL-2.0-only or GPL-3.0-only) and BSD-3-Clause and CC0-1.0
### BEGIN LICENSE SUMMARY ###
#
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
###  END LICENSE SUMMARY  ###
License:        (GPL-2.0-only OR GPL-3.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (Unlicense OR MIT)
URL:            https://invent.kde.org/tduck/dynamic-hibernate
Source:         %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# Manually created patch for downstream crate metadata changes
# * Allow sysinfo versions through 0.39:
#   https://invent.kde.org/tduck/dynamic-hibernate/-/merge_requests/2
Patch:          dynamic-hibernate-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 28
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
BuildRequires:  cmake(KF6I18n)

Requires:       dbus-common

# Does not build on 32-bit architectures
ExcludeArch:   %{ix86} %{arm32} %{riscv32}

%description
This software enables dynamically creating swapfiles before hibernation
on btrfs-based systems (as well as automatically hiding the bootloader
on systemd-boot based systems), and then allows you to hibernate to it.

This circumvents the requirement for a swap partition or pre-existing swapfile.

It also provides a notifier which alerts the user if and why hibernation fails.


%prep
%autosetup -p1 -C
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires


%conf
%cmake_kf6 -DCARGO_BUILD_PROFILE=rpm


%build
%cmake_build

# Get Rust licensing data
%{cargo_license_summary}
# LICENSE.dependencies contains a full license breakdown
%{cargo_license} > LICENSE.dependencies


%install
%cmake_install


%post
%systemd_post %{name}-prepare.service %{name}-cleanup.service
%systemd_user_post %{name}-notifier.service


%preun
%systemd_preun %{name}-prepare.service %{name}-cleanup.service
%systemd_user_preun %{name}-notifier.service


%postun
%systemd_postun_with_restart %{name}-prepare.service %{name}-cleanup.service
%systemd_user_postun_with_restart %{name}-notifier.service



%files
%license LICENSES/* REUSE.toml
%license LICENSE.dependencies
%doc README.md
%{_libexecdir}/%{name}{,-*}
%{_unitdir}/%{name}-cleanup.service
%{_unitdir}/%{name}-prepare.service
%{_userunitdir}/%{name}-notifier.service
%dir %{_unitdir}/systemd-logind.service.d
%{_unitdir}/systemd-logind.service.d/00-dynamic-hibernate-logind.conf
%dir %{_prefix}/lib/systemd/sleep.conf.d
%{_prefix}/lib/systemd/sleep.conf.d/00-dynamic-hibernate-sleep.conf
%{_datadir}/dbus-1/system.d/org.dynamic_hibernate.DynamicHibernate.conf


%changelog
* Mon Aug 31 2026 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1.0~git20260116.8739c5c-1
- Update to latest upstream commit
- Update License field based on a current build in Rawhide

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20251209.aaf963c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20251209.aaf963c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Dec 29 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0~git20251209.aaf963c-1
- Initial packaging
