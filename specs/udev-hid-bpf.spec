%bcond_without check
%global udevdir %(pkg-config --variable=udevdir udev)
%global cargo_install_lib 0
%global crate udev-hid-bpf
%global _firmware /usr/lib/firmware

%if 0%{?rhel}
%global bundled_rust_deps 1
%global build_testing 0
%global build_tracing 1
%else
%global bundled_rust_deps 0
%global build_testing 1
%endif

# Fedora 42 never shipped a kernel 6.12 so no need for our tracing sources
%if 0%{?fedora} >= 42
%global build_tracing "false"
%else
%global build_tracing "true"
%endif

# Upstream uses 1.0.0-20240417 but rpm won't let us use the dash, so let's use a dot instead.
%global upstream_version 2.2.0
%global upstream_version_date 20251121
%global tarball %{upstream_version}-%{upstream_version_date}

Name:           udev-hid-bpf
Version:        %{upstream_version}.%{upstream_version_date}
Release:        %autorelease
Summary:        HID-BPF quirk loader tool

SourceLicense:  GPL-2.0-only
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-3-Clause OR MIT OR Apache-2.0) AND GPL-2.0-only AND (LGPL-2.1-only OR BSD-2-Clause) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
URL:            https://gitlab.freedesktop.org/libevdev/udev-hid-bpf/
Source0:        https://gitlab.freedesktop.org/libevdev/%{name}/-/archive/%{tarball}/%{name}-%{tarball}.tar.bz2
# To recreate tarball:
# $ centpkg prep (do not use fedpkg, it removes Cargo.lock)
# $ pushd udev-hid-bpf-...; cargo vendor && tar Jcvf ../$(basename $PWD)-vendor.tar.xz vendor/ ; popd
Source1:        %{name}-%{upstream_version}-%{upstream_version_date}-vendor.tar.xz

Patch01:        0001-Bump-the-cargo-test-timeout-to-500s.patch
Patch02:        0001-Cargo.toml-drop-libbpf-sys-to-1.5.0.patch

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros >= 26
%endif
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-rpm-macros
BuildRequires:  meson cargo
BuildRequires:  pkgconfig(udev)
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  pkgconfig(libbpf) bpftool
BuildRequires:  pkgconfig(libudev)

Requires:       systemd-udev
Requires:       %{name}-stable%{?_isa} = %{version}-%{release}

# We don't have bpftool (#2294345)
ExcludeArch:    %{ix86}

%description
%{name} is a loader for HID eBPF programs aimed
at making it simple to develop and test eBPF programs
for HID devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries
and header files for developing applications
that use %{name}.

%if 0%{?build_testing}
%package        testing
Summary:        Testing eBPF programs for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    testing
The %{name}-testing package contains HID eBPF programs
for %{name} that have not yet been merged into
an upstream kernel.
%endif

%package        stable
Summary:        Stable eBPF programs for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    stable
The %{name}-stable package contains HID eBPF programs
for %{name} that have been merged into
an upstream kernel.

%prep
%autosetup -S git -p1 -n %{name}-%{tarball}
%py3_shebang_fix $(git grep -l  '#!/usr/bin/.*python3')

# Real build system is meson but upstream makes
# sure cargo on its own works too so this is safe to call here
%if 0%{?bundled_rust_deps}
tar xf %{SOURCE1}
%cargo_prep -v vendor
%else
%cargo_prep
%endif

%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires
%endif

%build
export RUSTFLAGS="%build_rustflags"
%if 0%{?build_testing}
%global bpf_set stable,testing
%else
%global bpf_set stable
%endif

%meson -Dudevdir=%{udevdir} \
       -Dbpfs=%{bpf_set} \
       -Dbpf-tracing=%{build_tracing} \
       -Dtests=disabled \
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif

%install
%meson_install

%if %{with check}
%check
%meson_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%license cargo-vendor.txt
%endif
%doc README.md
%{_bindir}/udev-hid-bpf
%{_mandir}/man1/udev-hid-bpf.1*
%{udevdir}/rules.d/81-hid-bpf.rules
%dir /usr/lib/firmware/hid/bpf
%dir /usr/lib/firmware/hid/

%files stable
%license LICENSE
%license LICENSE.dependencies
%{_udevhwdbdir}/81-hid-bpf-stable.hwdb
%{_firmware}/hid/bpf/*-FR-TEC__Raptor-Mach-2.bpf.o
%{_firmware}/hid/bpf/*-HP__Elite-Presenter.bpf.o
%{_firmware}/hid/bpf/*-Huion__Dial-2.bpf.o
%{_firmware}/hid/bpf/*-Huion__Inspiroy-2-M.bpf.o
%{_firmware}/hid/bpf/*-Huion__Inspiroy-2-S.bpf.o
%{_firmware}/hid/bpf/*-Huion__Kamvas-Pro-19.bpf.o
%{_firmware}/hid/bpf/*-Huion__Kamvas13Gen3.bpf.o
%{_firmware}/hid/bpf/*-Huion__Kamvas16Gen3.bpf.o
%{_firmware}/hid/bpf/*-Huion__KeydialK20.bpf.o
%{_firmware}/hid/bpf/*-IOGEAR__Kaliber-MMOmentum.bpf.o
%{_firmware}/hid/bpf/*-Logitech__SpaceNavigator.bpf.o
%{_firmware}/hid/bpf/*-Microsoft__Xbox-Elite-2.bpf.o
%{_firmware}/hid/bpf/*-Mistel__MD770.bpf.o
%{_firmware}/hid/bpf/*-Rapoo__M50-Plus-Silent.bpf.o
%{_firmware}/hid/bpf/*-TUXEDO__Sirius-16-Gen1-and-Gen2.bpf.o
%{_firmware}/hid/bpf/*-Thrustmaster__TCA-Yoke-Boeing.bpf.o
%{_firmware}/hid/bpf/*-WALTOP__Batteryless-Tablet.bpf.o
%{_firmware}/hid/bpf/*-Wacom__ArtPen.bpf.o
%{_firmware}/hid/bpf/*-XPPen__ACK05.bpf.o
%{_firmware}/hid/bpf/*-XPPen__Artist24.bpf.o
%{_firmware}/hid/bpf/*-XPPen__ArtistPro16Gen2.bpf.o
%{_firmware}/hid/bpf/*-XPPen__Deco01V3.bpf.o
%{_firmware}/hid/bpf/*-XPPen__Deco02.bpf.o
%{_firmware}/hid/bpf/*-XPPen__DecoMini4.bpf.o

%if 0%{?build_testing}
%files testing
%license LICENSE
%license LICENSE.dependencies
%{_udevhwdbdir}/81-hid-bpf-testing.hwdb
%endif

%changelog
%autochangelog
