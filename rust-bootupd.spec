%bcond_without check
%global __cargo_skip_build 0

%global crate bootupd

Name:           rust-%{crate}
Version:        0.2.7
Release:        2%{?dist}
Summary:        Bootloader updater

License:        ASL 2.0
URL:            https://crates.io/crates/bootupd
Source0:        https://github.com/coreos/bootupd/releases/download/v%{version}/bootupd-%{version}.crate
Source1:        https://github.com/coreos/%{crate}/releases/download/v%{version}/%{crate}-%{version}-vendor.tar.gz

# For now, see upstream
ExclusiveArch:  x86_64 aarch64
BuildRequires: make
BuildRequires:  openssl-devel
%if 0%{?rhel} && !0%{?eln}
BuildRequires: rust-toolset
%else
BuildRequires: rust-packaging
%endif
BuildRequires:  systemd

%global _description %{expand:
Bootloader updater}
%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        ASL 2.0
%{?systemd_requires}

%description -n %{crate} %{_description}

%files -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/bootupctl
%{_libexecdir}/bootupd
%{_unitdir}/*

%prep
%autosetup -n %{crate}-%{version} -p1
mkdir vendor
tar -xv -C vendor -f %{SOURCE1}
mkdir -p .cargo
cat >.cargo/config << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%cargo_build

%install
%make_install INSTALL="install -p -c"

%post        -n %{crate}
%systemd_post bootupd.service bootupd.socket

%preun       -n %{crate}
%systemd_preun bootupd.service bootupd.socket

%postun      -n %{crate}
%systemd_postun bootupd.service bootupd.socket

%changelog
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

