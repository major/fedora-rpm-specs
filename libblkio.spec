Version:       1.2.2
%global forgeurl https://gitlab.com/libblkio/libblkio
%global tag    v%{version}
%forgemeta

Summary:       Block device I/O library
Name:          libblkio
Release:       5%{?dist}
URL:           %{forgeurl}
Source0:       %{forgesource}
Patch0:        fix-nix-ioctl-feature.patch
License:       (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND MIT AND BSD-3-Clause AND Unicode-DFS-2016

# Basic build requirements.
BuildRequires: gcc, gcc-c++
BuildRequires: make
BuildRequires: meson
BuildRequires: rust-packaging >= 21
BuildRequires: rustfmt
BuildRequires: cargo
BuildRequires: python3-docutils
BuildRequires: pkgconf

# XXX Eventually use %%generate_buildrequires but it does not support
# workspaces yet.  See
# https://bugzilla.redhat.com/show_bug.cgi?id=2124697#c57
#
# For major version >= 1, we are requiring that the major version does
# not change.
#
# For major version >= 0, we are requiring that the minor version does
# not change.
BuildRequires: (crate(autocfg/default) >= 1.0.0 with crate(autocfg/default) < 2.0.0~)
BuildRequires: (crate(bitflags/default) >= 1.0.0 with crate(bitflags/default) < 2.0.0~)
BuildRequires: (crate(cc/default) >= 1.0.0 with crate(cc/default) < 2.0.0~)
BuildRequires: (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0~)
BuildRequires: (crate(concat-idents/default) >= 1.0.0 with crate(concat-idents/default) < 2.0.0~)
BuildRequires: (crate(const-cstr/default) >= 0.3.0 with crate(const-cstr/default) < 0.4.0~)
BuildRequires: (crate(io-uring/default) >= 0.5.10 with crate(io-uring/default) < 0.6.0~)
BuildRequires: (crate(lazy_static/default) >= 1.0.0 with crate(lazy_static/default) < 2.0.0~)
BuildRequires: (crate(libc/default) >= 0.2.134 with crate(libc/default) < 0.3.0~)
BuildRequires: (crate(memmap2/default) >= 0.5.7 with crate(memmap2/default) < 0.6.0~)
BuildRequires: (crate(nix/default) >= 0.24.2 with crate(nix/default) < 0.25.0~)
BuildRequires: (crate(num-traits/default) >= 0.2.15 with crate(num-traits/default) < 0.3.0~)
BuildRequires: (crate(pci-driver/default) >= 0.1.2 with crate(pci-driver/default) < 0.2.0~)
BuildRequires: (crate(proc-macro2/default) >= 1.0.0 with crate(proc-macro2/default) < 2.0.0~)
BuildRequires: (crate(quote/default) >= 1.0.0 with crate(quote/default) < 2.0.0~)
BuildRequires: (crate(syn/default) >= 1.0.0 with crate(syn/default) < 2.0.0~)
BuildRequires: (crate(unicode-ident/default) >= 1.0.0 with crate(unicode-ident/default) < 2.0.0~)
BuildRequires: (crate(virtio-bindings/default) >= 0.1.0 with crate(virtio-bindings/default) < 0.2.0~)


%description
libblkio is a library for high-performance block device I/O with
support for multi-queue devices. A C API is provided so that
applications can use the library from most programming languages.


%package devel
Summary:       Development tools for %{name}
Requires:      %{name}%{_isa} = %{version}-%{release}


%description devel
This package contains development tools for %{name}.


%prep
%forgeautosetup -p1

%cargo_prep
sed -e 's/--locked//' -i src/cargo-build.sh


%build
export RUSTFLAGS="%build_rustflags"
%{meson}
%{meson_build}


%install
%{meson_install}


%files
%license LICENSE-APACHE LICENSE-MIT LICENSE.crosvm
%doc README.rst
%{_libdir}/libblkio.so.1{,.*}


%files devel
%license LICENSE-APACHE LICENSE-MIT LICENSE.crosvm
%doc README.rst
%{_includedir}/blkio.h
%{_libdir}/libblkio.so
%{_libdir}/pkgconfig/blkio.pc
%{_mandir}/man3/blkio.3*


%changelog
* Wed Apr 19 2023 Stefan Hajnoczi <stefanha@redhat.com> - 1.2.2-5
- Patch Cargo.toml files to enable nix "ioctl" feature (RHBZ#2186159)

* Thu Mar 09 2023 Stefan Hajnoczi <stefanha@redhat.com> - 1.2.2-4
- Update overall license to include crate dependency licenses

* Sun Feb 05 2023 Fabio Valentini <decathorpe@gmail.com> - 1.2.2-3
- Rebuild for fixed frame pointer compiler flags in Rust RPM macros.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-1
- Initial package
