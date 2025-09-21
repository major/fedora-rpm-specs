# Requires forked dependencies, particularly a forked bindgen
# Related: https://github.com/rust-lang/rust/issues/118018
%bcond rust_vendorized 1

# For non-Fedora builds
%bcond dkms 0

# For FUSE fallback
%bcond fuse 1

# While there are no observable issues with LTO, Kent thinks it's bad,
# so disable for now until more testing can be done.
%global _lto_cflags %{nil}

%global make_opts VERSION="%{version}" %{?with_fuse:BCACHEFS_FUSE=1} %{!?with_rust:NO_RUST=1} BUILD_VERBOSE=1 PREFIX=%{_prefix} ROOT_SBINDIR=%{_sbindir}

Name:           bcachefs-tools
Version:        1.31.2
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

%if %{with dkms}
Requires:       (dkms-bcachefs = %{version}-%{release} if kernel-core%{?_isa})
%endif

# Rust parts FTBFS on 32-bit arches
ExcludeArch:    %{ix86} %{arm32}

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
%{_udevrulesdir}/64-bcachefs.rules

%if %{with fuse}
%dnl ----------------------------------------------------------------------------

%package -n fuse-bcachefs
Summary:        FUSE implementation of bcachefs
BuildRequires:  pkgconfig(fuse3) >= 3.7
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-fuse < %{version}-%{release}
Provides:       %{name}-fuse = %{version}-%{release}
Provides:       %{name}-fuse%{?_isa} = %{version}-%{release}

%description -n fuse-bcachefs
This package is an experimental implementation of bcachefs leveraging FUSE to
mount, create, check, modify and correct any inconsistencies in the bcachefs filesystem.

%files -n fuse-bcachefs
%license COPYING
%{_sbindir}/mount.fuse.bcachefs
%{_sbindir}/fsck.fuse.bcachefs
%{_sbindir}/mkfs.fuse.bcachefs

%dnl ----------------------------------------------------------------------------
%endif

%if %{with dkms}
%dnl ----------------------------------------------------------------------------

%package -n dkms-bcachefs
Summary:        Bcachefs kernel module managed by DKMS
Requires:       diffutils
Requires:       dkms >= 3.2.1
Requires:       gcc
Requires:       make
Requires:       perl
Requires:       python3

Requires:       %{name} = %{version}-%{release}

BuildArch:      noarch

%description -n dkms-bcachefs
This package is an implementation of bcachefs built using DKMS to offer the kernel
module to mount, create, check, modify and correct any inconsistencies in the bcachefs
filesystem.

%preun -n dkms-bcachefs
if [  "$(dkms status -m bcachefs -v %{version})" ]; then
   dkms remove -m bcachefs -v %{version} --all --rpm_safe_upgrade
fi

%post -n dkms-bcachefs
if [ "$1" -ge "1" ]; then
   if [ -f /usr/lib/dkms/common.postinst ]; then
      /usr/lib/dkms/common.postinst bcachefs %{version}
      exit $?
   fi
fi

%files -n dkms-bcachefs
%license COPYING
%{_usrsrc}/bcachefs-%{version}/

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

%if ! %{with dkms}
# Purge dkms files
rm -rf %{buildroot}%{_usrsrc}
%endif


%changelog
* Fri Sep 19 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.31.2-1
- Update to 1.31.2

* Thu Sep 18 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.31.1-1
- Update to 1.31.1

* Sun Sep 14 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.31.0-1
- Update to 1.31.0

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Apr 19 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.25.2-1
- Update to 1.25.2

* Thu Feb 13 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0
- Backport fix to build with GCC 15
- Drop 32-bit architectures as they FTBFS on the Rust parts

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

