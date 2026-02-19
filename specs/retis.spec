Name:           retis
Version:        1.6.4
Release:        %autorelease
Summary:        Tracing packets in the Linux networking stack
License:        GPL-2.0-only

URL:            https://github.com/retis-org/retis
Source:         https://github.com/retis-org/retis/archive/v%{version}/%{name}-%{version}.tar.gz
# Manually created to use the rpm profile when building and installing the
# release target.
Patch:          retis-release-profile.diff
# Manually created to:
# - Remove the rbpf dependency (was in the unused 'debug' feature).
# - Remove the dev-dependencies.
# - Downgrade the libbpf-rs/cargo and pcap dependencies.
Patch:          retis-fix-deps.diff
# Manually created to downgrade the elf dependency and fix its use.
Patch:          retis-downgrade-elf.diff

ExclusiveArch:  x86_64 aarch64

Requires:       python3

BuildRequires:  rust-packaging
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  python3-devel

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
install -m 0755 -d %{buildroot}%{_datadir}/retis/profiles
install -m 0644 retis/profiles/* %{buildroot}%{_datadir}/retis/profiles
rm -rf %{buildroot}/include
rm -rf %{buildroot}/pkgconfig
rm -f %{buildroot}/libbpf.a

%files
%license LICENSE
%doc README.md
%{_bindir}/retis
%{_datadir}/retis/profiles

%changelog
%autochangelog
