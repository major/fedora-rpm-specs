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
Version:        1.20.0
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
## From: https://evilpiepirate.org/git/bcachefs-tools.git/commit/?id=3e15e96cb9c90cca6f7fa3465697933c53f51228
Patch0001:      0001-Switch-to-c11-atomics.patch

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

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  cargo
BuildRequires:  rust
%if %{with rust_vendorized}
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
%endif

%description
The bcachefs-tools package provides all the userspace programs needed to create,
check, modify and correct any inconsistencies in the bcachefs filesystem.

%files
%license COPYING
%license LICENSE.rust-deps
%if %{with rust_vendorized}
%license cargo-vendor.txt
%license COPYING.rust-dependencies
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


%if ! %{with rust_vendorized}
%generate_buildrequires
%cargo_generate_buildrequires
cd bch_bindgen
%cargo_generate_buildrequires
cd ../
%endif


%build
%make_build %{make_opts}
%cargo_prep %{?with_rust_vendorized:-v vendor}
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.rust-deps
%{?with_rust_vendorized:%cargo_vendor_manifest}


%install
%make_install %{make_opts}


# Purge debian stuff
rm -rfv %{buildroot}/%{_datadir}/initramfs-tools

%if ! %{with fuse}
# Purge useless symlink stubs
rm -rf %{buildroot}%{_sbindir}/*.fuse.bcachefs
%endif


%changelog
* Thu Feb 13 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0
- Backport fix to build with GCC 15

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 10 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0
- Remove unusable condition to build without rust (it's been required for a while)

* Thu Aug 29 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun May 12 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Fri Feb 23 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.6.4-1
- Update to 1.6.4
- Drop backported patches

* Fri Feb 23 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.6.3-2
- Backport patches to fix the build

* Tue Feb 20 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.6.3-1
- Update to 1.6.3

* Fri Feb 16 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Wed Feb 14 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

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

