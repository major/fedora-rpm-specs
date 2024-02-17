%bcond_without check

%global crate bootupd

Name:           rust-%{crate}
Version:        0.2.18
Release:        %autorelease
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
%autochangelog
