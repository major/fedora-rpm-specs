Name:		retis
Version:	1.5.2
Release:	0%{?dist}
Summary:	Tracing packets in the Linux networking stack
License:	GPL-2.0-only

URL:		https://github.com/retis-org/retis
Source:		https://github.com/retis-org/retis/archive/v%{version}/%{name}-%{version}.tar.gz
# Manually created to use the rpm profile when building and installing the
# release target.
Patch:		retis-release-profile.diff
# Manually created to:
# - Remove the rbpf dependency (was in the unused 'debug' feature).
# - Remove the dev-dependencies.
# - Relax the bindgen version requirement to allow using the one packaged in
#   Fedora.
# - Relax the dependency on cargo-platform (only required for c8s).
Patch:		retis-fix-deps.diff
# Manually created to remove CFLAGS for BPF targets as the default ones are
# incompatible with the 'bpf' target (e.g. -mtls-dialect=gnu or
# -mbranch-protection).
Patch:		retis-cflags.diff
# Manually created to fix a build error linked to using libbpf-rs 0.24.4, which
# is not reproducible upstream while using newer versions.
Patch:		retis-libbpf-rs-fix.diff

ExclusiveArch:	x86_64 aarch64

Requires:	elfutils-libelf
Requires:	python3
Requires:	zlib

BuildRequires:	rust-packaging
BuildRequires:	clang
BuildRequires:	git
BuildRequires:	jq
BuildRequires:	llvm
BuildRequires:	make
BuildRequires:	python3-devel

%description
Tracing packets in the Linux networking stack, using eBPF and interfacing with
control and data paths such as OpenVSwitch.

%prep
%autosetup -n %{name}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
make release %{?_smp_mflags}

%install
env CARGO_INSTALL_OPTS="--no-track" make install
install -m 0755 -d %{buildroot}%{_sysconfdir}/retis/profiles
install -m 0644 retis/profiles/* %{buildroot}%{_sysconfdir}/retis/profiles
rm -rf %{buildroot}/include
rm -rf %{buildroot}/pkgconfig
rm -f %{buildroot}/libbpf.a

%files
%license retis/LICENSE
%doc README.md
%{_bindir}/retis
%{_sysconfdir}/retis/profiles

%changelog
%autochangelog
