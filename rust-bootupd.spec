%bcond_without check

%global crate bootupd

Name:           rust-%{crate}
Version:        0.2.17
Release:        4%{?dist}
Summary:        Bootloader updater

License:        Apache-2.0
URL:            https://github.com/coreos/bootupd
Source0:        %{url}/releases/download/v%{version}/bootupd-%{version}.crate
Source1:        %{url}/releases/download/v%{version}/bootupd-%{version}-vendor.tar.zstd

# For now, see upstream
BuildRequires: make
BuildRequires:  openssl-devel
%if 0%{?rhel}
BuildRequires: rust-toolset
%else
BuildRequires:  cargo-rpm-macros >= 25
%endif
BuildRequires:  systemd

%global _description %{expand:
Bootloader updater}
%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
%{?systemd_requires}

%description -n %{crate} %{_description}

%files -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/bootupctl
%{_libexecdir}/bootupd
%{_unitdir}/*
%{_prefix}/lib/bootupd/grub2-static/

%prep
%autosetup -n %{crate}-%{version} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%cargo_vendor_manifest
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%make_install INSTALL="install -p -c"
%{__make} install-grub-static DESTDIR=%{?buildroot} INSTALL="%{__install} -p"

%post        -n %{crate}
%systemd_post bootupd.service bootupd.socket

%preun       -n %{crate}
%systemd_preun bootupd.service bootupd.socket

%postun      -n %{crate}
%systemd_postun bootupd.service bootupd.socket

%changelog
* Thu Feb 01 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 0.2.17-4
- Update Rust macro usage

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Colin Walters <walters@verbum.org> - 0.2.17-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.17

* Wed Dec 13 2023 Colin Walters <walters@verbum.org> - 0.2.16-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.16

* Tue Nov 28 2023 Colin Walters <walters@verbum.org> - 0.2.15-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.15

* Mon Nov 20 2023 Colin Walters <walters@verbum.org> - 0.2.14-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.14

* Tue Nov 14 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.2.13-4
- Fix RHEL build

* Fri Nov 10 2023 Colin Walters <walters@verbum.org> - 0.2.13-3
- Backport patch for not having separate /boot

* Thu Nov 02 2023 Colin Walters <walters@verbum.org> - 0.2.13-2
- Rebase to 0.2.13

* Mon Oct 23 2023 Colin Walters <walters@verbum.org> - 0.2.12-4
- Install static configs

* Fri Oct 20 2023 Colin Walters <walters@verbum.org> - 0.2.12-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.12

* Fri Oct 06 2023 Colin Walters <walters@verbum.org> - 0.2.11-5
- Enable ppc64le, it is supported now

* Sat Sep 30 2023 Fabio Valentini <decathorpe@gmail.com> - 0.2.11-4
- Updates for the latest Rust packaging and license tag / SPDX guidelines.

* Tue Sep 19 2023 Colin Walters <walters@verbum.org> - 0.2.11-3
- https://github.com/coreos/bootupd/releases/tag/v0.2.11

* Mon Sep 11 2023 Colin Walters <walters@verbum.org> - 0.2.10-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.10

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Oct 18 2022 Colin Walters <walters@verbum.org> - 0.2.8-3
- Update to v0.2.8

* Fri Jul 29 2022 Colin Walters <walters@verbum.org> - 0.2.7-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.7

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.6-4
- Rebuild with package notes

* Tue Feb 15 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.6-3
- Rebuild with package notes

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 16 2021 Luca BRUNO <lucab@lucabruno.net> - 0.2.6-1
- New upstream version
  https://github.com/coreos/bootupd/releases/tag/v0.2.6

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.2.5-5
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 14:48:03 UTC 2021 Colin Walters <walters@verbum.org> - 0.2.5-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.5

* Tue Dec 15 14:48:20 UTC 2020 Colin Walters <walters@verbum.org> - 0.2.4-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.4

* Tue Nov 17 14:33:06 UTC 2020 Colin Walters <walters@verbum.org> - 0.2.3-2
- https://github.com/coreos/rpm-ostree/bootupd/tag/v0.2.3

* Wed Nov 11 18:07:38 UTC 2020 Colin Walters <walters@verbum.org> - 0.2.2-2
- Update to 0.2.2

* Mon Nov  2 23:03:03 UTC 2020 Colin Walters <walters@verbum.org> - 0.2.0-3
- Switch to vendored sources since RHEL requires it

* Mon Oct 26 15:06:37 UTC 2020 Colin Walters <walters@verbum.org> - 0.2.0-2
- https://github.com/coreos/bootupd/releases/tag/v0.2.0

* Tue Oct 13 2020 Colin Walters <walters@verbum.org> - 0.1.3-2
- https://github.com/coreos/bootupd/releases/tag/v0.1.3

* Tue Sep 22 2020 Colin Walters <walters@verbum.org> - 0.1.2-2
- New upstream

* Mon Sep 21 2020 Colin Walters <walters@verbum.org> - 0.1.1-2
- Also build on aarch64

* Fri Sep 11 2020 Colin Walters <walters@verbum.org> - 0.1.0-3
- Initial package

