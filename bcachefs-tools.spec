# Note that this blocks 32-bit arch builds
%bcond rust 1

# Requires forked dependencies, particularly a forked bindgen
# Related: https://github.com/rust-lang/rust/issues/118018
%bcond rust_vendorized 1

# Fails to compile at the moment and is totally broken
%bcond fuse 0

# While there are no observable issues with LTO, Kent thinks it's bad,
# so disable for now until more testing can be done.
%global _lto_cflags %{nil}

%global make_opts VERSION="%{version}" %{?with_fuse:BCACHEFS_FUSE=1} %{!?with_rust:NO_RUST=1} BUILD_VERBOSE=1 PREFIX=%{_prefix} ROOT_SBINDIR=%{_sbindir}

Name:           bcachefs-tools
Version:        1.4.0
Release:        1%{?dist}
Summary:        Userspace tools for bcachefs

# --- rust ---
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# --- misc ---
# GPL-2.0-only
# GPL-2.0-or-later
# LGPL-2.1-only
# BSD-3-Clause
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only AND BSD-3-Clause AND (Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 with LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND MPL-2.0 AND (Unlicense OR MIT))
URL:            https://bcachefs.org/
Source0:        https://evilpiepirate.org/%{name}/%{name}-vendored-%{version}.tar.zst
Source1:        https://evilpiepirate.org/%{name}/%{name}-vendored-%{version}.tar.sign
Source2:        https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/13AB336D8DCA6E76.asc

# Upstream patches
## From: https://evilpiepirate.org/git/bcachefs-tools.git/commit/?id=89abdd87271e237141a9d4f44d531f7c53353b83
Patch0001:      0001-Makefile-fsck-Use-libexec-instead-of-lib.patch
## From: https://evilpiepirate.org/git/bcachefs-tools.git/commit/?id=44bf7868e5c2c4a52aef67e55aab1e904147dad4
Patch002:       0001-fix-missing-atomic64_read_acquire-on-32-bit.patch

# Upstreamable patches

# Fedora-specific patches
## Ensure that the makefile doesn't run rust itself, so we can build with our flags properly
Patch1001:      bcachefs-tools-no-make-rust.patch

BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-rpm-macros

%if %{with rust}
BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  cargo
BuildRequires:  rust
%if %{with rust_vendorized}
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
%endif
%endif

%description
The bcachefs-tools package provides all the userspace programs needed to create,
check, modify and correct any inconsistencies in the bcachefs filesystem.

%files
%license COPYING
%if %{with rust}
%license rust-src/LICENSE.rust-deps
%if %{with rust_vendorized}
%license rust-src/cargo-vendor.txt
%license COPYING.rust-dependencies
%endif
%endif
%doc doc/bcachefs-principles-of-operation.tex
%doc doc/bcachefs.5.rst.tmpl
%{_sbindir}/bcachefs
%{_sbindir}/mount.bcachefs
%{_sbindir}/fsck.bcachefs
%{_sbindir}/mkfs.bcachefs
%{_mandir}/man8/bcachefs.8*
%{_libexecdir}/bcachefsck*
%{_unitdir}/bcachefsck*
%{_unitdir}/system-bcachefsck.slice
%{_udevrulesdir}/64-bcachefs.rules

%if %{with fuse}
%dnl ----------------------------------------------------------------------------

%package fuse
Summary:        FUSE implementation of bcachefs
BuildRequires:  pkgconfig(fuse3) >= 3.7
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description fuse
The bcachefs-tools-fuse package is an experimental implementation of bcachefs-tools
leveraging FUSE to mount, create, check, modify and correct any inconsistencies in
the bcachefs filesystem.

%files fuse
%license COPYING
%{_sbindir}/mount.fuse.bcachefs
%{_sbindir}/fsck.fuse.bcachefs
%{_sbindir}/mkfs.fuse.bcachefs

%dnl ----------------------------------------------------------------------------
%endif


%prep
# Verify the integrity of the sources
zstdcat '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
# Prep sources
%autosetup -S git_am
%if ! %{with rust_vendorized}
# Purge the vendor tree
rm -rf vendor
%endif


%if %{with rust} && ! %{with rust_vendorized}
%generate_buildrequires
cd rust-src
%cargo_generate_buildrequires
cd bch_bindgen
%cargo_generate_buildrequires
cd ../..
%endif


%build
%if %{with rust}
pushd rust-src
%cargo_prep -v ../vendor
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.rust-deps
%if %{with rust_vendorized}
%cargo_vendor_manifest
# fix broken version string for forked bindgen
sed -e 's|bindgen v0.64.0 (https://evilpiepirate.org/git/rust-bindgen.git#f773267b)|bindgen v0.64.0+bcfsmod.git20230227.f773267b|' -i cargo-vendor.txt
%endif

popd
%endif
%make_build %{make_opts}


%install
%make_install %{make_opts}


# Purge debian stuff
rm -rfv %{buildroot}/%{_datadir}/initramfs-tools

%if ! %{with fuse}
# Purge useless symlink stubs
rm -rf %{buildroot}%{_sbindir}/*.fuse.bcachefs
%endif


%changelog
* Sun Dec 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0
- Backport patch to move systemd unit helpers to libexecdir
- Backport patch to fix builds on 32-bit architectures

* Tue Dec 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.3.5-1
- Update to 1.3.5

* Mon Nov 20 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.3.4-3
- Verify signatures for sources

* Sun Nov 19 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.3.4-2
- Disable LTO for now

* Fri Nov 17 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Wed Nov 08 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3

* Tue Nov 07 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2
- Use vendorized rust for now

* Sat Nov 04 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Wed Nov 01 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.2^git20231027.d320a4e-1
- Initial package

