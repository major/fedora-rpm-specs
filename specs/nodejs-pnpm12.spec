%global pkgname pnpm
%global pnpm_major_version 12

Name:           nodejs-%{pkgname}%{pnpm_major_version}
Version:        12.4.2
Release:        %autorelease
Summary:        Fast, disk space efficient package manager

License:        MIT
URL:            https://pnpm.io
# Pristine upstream monorepo source. NOT %%{pkgname}-%%{version} (the npm
# tarball) -- see the block comment above for why.
Source0:        https://github.com/pnpm/pnpm/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Rust dependency vendoring: pnpm-cli currently needs ~24 crates that are
# either missing from Fedora or are too old (see the bundled(crate()) Provides
# generated from cargo-vendor.txt below for the full, exact list) out of
# roughly 130 direct dependencies. Unbundling all of these (and their own
# transitive dependencies) is future work; for now this package vendors its
# Rust dependencies, per the Rust Packaging Guidelines' documented escape
# hatch for exactly this situation.
#
# Regenerate with: ./generate-vendor-tarball.sh {version}
Source1:        pnpm-%{version}-vendor.tar.xz

BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global _description %{expand:
A fast, disk space efficient package manager for NodeJS.
}

%description %{_description}


%package -n %{pkgname}%{pnpm_major_version}
Summary:        Fast, disk space efficient package manager
# Aggregate SPDX expression for everything statically linked into the
# `pnpm` binary, from `cargo2rpm license-summary` run inside
# pnpm/crates/cli (with the same feature flags as %%cargo_build below).
License:        %{shrink:
    ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND
    ((MIT OR Apache-2.0) AND Unicode-3.0) AND
    (0BSD OR MIT OR Apache-2.0) AND
    Apache-2.0 AND
    (Apache-2.0 OR BSD-2-Clause) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR GPL-2.0-only) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    BSD-3-Clause AND
    (BSD-3-Clause OR MIT OR Apache-2.0) AND
    BSL-1.0 AND
    (CC0-1.0 OR MIT-0 OR Apache-2.0) AND
    CDLA-Permissive-2.0 AND
    ISC AND
    (ISC AND (Apache-2.0 OR ISC)) AND
    (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND
    (LGPL-3.0-or-later OR MPL-2.0) AND
    MIT AND
    (MIT OR Apache-2.0) AND
    (MIT OR Apache-2.0 OR BSD-1-Clause) AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (MIT OR Zlib OR Apache-2.0) AND
    MPL-2.0 AND
    Unicode-3.0 AND
    (Unlicense OR MIT) AND
    Zlib AND
    (Zlib OR Apache-2.0 OR MIT)
}
# LICENSE.dependencies contains a full license breakdown
Requires:       bash
Provides:       npm(%{pkgname}) = %{version}
Requires(post): %{_bindir}/update-alternatives
Requires(postun): %{_bindir}/update-alternatives

# The old unversioned "pnpm" package owns /usr/bin/pnpm and /usr/bin/pnpx as
# real files, not via alternatives. Conflict on its package.
Conflicts:      pnpm

%description -n %{pkgname}%{pnpm_major_version} %{_description}


%prep
%autosetup -n pnpm-%{version} -p1 -a1

# The monorepo's Cargo workspace also contains `pnpr`, pnpm's private
# server-side registry component, which is licensed under the (non-free)
# PolyForm Shield 1.0.0 license. It is only ever a dev-dependency of the CLI
# (used by its test suite), never a normal build dependency, so we delete it.
rm -rf pnpr pnpm/crates/napi
sed -i '/^pnpr[-a-zA-Z]* = { path = "pnpr\//d; /^pnpm-napi = { path = "pnpm\/crates\/napi" }$/d' Cargo.toml
sed -i 's/members = \["pnpm\/crates\/\*", "pnpm\/tasks\/\*", "pnpr\/crates\/\*"\]/members = ["pnpm\/crates\/*"]/' Cargo.toml
sed -i '/^pnpr = { workspace = true }$/d' pnpm/crates/cli/Cargo.toml pnpm/crates/pnpr-client/Cargo.toml pnpm/crates/testing-utils/Cargo.toml
sed -i '/^pnpr-fixtures = { workspace = true }$/d' pnpm/crates/testing-utils/Cargo.toml

# Upstream's own [profile.release] sets `lto = "fat"`, which %%cargo_prep's
# generated [profile.rpm] (inherits = "release") does not override. Combined
# with Fedora's own codegen-units=1 and full debuginfo, fat LTO across this
# many crates blows past available build memory (OOM/SIGKILL during the final
# link). Disable it, see "incompatible compiler flags" in the Rust
# Packaging Guidelines.
sed -i '/^lto = "fat"$/d' Cargo.toml

%cargo_prep -v vendor

# %%cargo_prep only redirects crates-io to the vendor directory; it doesn't
# know about pnpm's one git dependency (a fork used for a Node.js-semver-
# compatible parser), which `cargo vendor` also bundled under vendor/ but
# needs its own source override to be picked up from there instead of git.
cat >> .cargo/config.toml << 'EOF'
[source."git+https://github.com/pnpm/node-semver-rs?rev=1ae976a0023b4dec80b1a5411ccee8343f91320e"]
git = "https://github.com/pnpm/node-semver-rs"
rev = "1ae976a0023b4dec80b1a5411ccee8343f91320e"
replace-with = "vendored-sources"
EOF


%build
LDEPS="$(pwd)/LICENSE.dependencies"
pushd pnpm/crates/cli
%cargo_build
%{cargo_license_summary}
%{cargo_license} > "${LDEPS}"
popd
# %%cargo_vendor_manifest runs `cargo tree --all-features --no-dedupe
# --target=all`, which OOMs on this dependency graph. cargo-vendor.txt is
# instead shipped pre-generated inside Source1 (vendor tarball) -- it
# directly lists what's under vendor/, so nothing needs to be (re)computed
# from the build here.


%install
install -Dpm 0755 target/rpm/pnpm %{buildroot}%{_bindir}/pnpm%{pnpm_major_version}

# pn/pnpx/pnx are upstream's own tiny `sh` shims that just exec the `pnpm`
# binary next to them (injecting `dlx` for pnpx/pnx); point them at our
# versioned binary name instead of the unversioned one they assume.
for shim in pn pnpx pnx; do
    sed 's|/pnpm"|/pnpm%{pnpm_major_version}"|' pnpm/npm/pnpm/${shim} > %{buildroot}%{_bindir}/${shim}%{pnpm_major_version}
    chmod 0755 %{buildroot}%{_bindir}/${shim}%{pnpm_major_version}
done


%check
%{buildroot}%{_bindir}/pnpm%{pnpm_major_version} --version | grep -q .


%post -n %{pkgname}%{pnpm_major_version}
%{_sbindir}/update-alternatives --install %{_bindir}/pnpm pnpm %{_bindir}/pnpm%{pnpm_major_version} %{pnpm_major_version} \
    --slave %{_bindir}/pnpx pnpx %{_bindir}/pnpx%{pnpm_major_version} \
    --slave %{_bindir}/pn pn %{_bindir}/pn%{pnpm_major_version} \
    --slave %{_bindir}/pnx pnx %{_bindir}/pnx%{pnpm_major_version}


%postun -n %{pkgname}%{pnpm_major_version}
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove pnpm %{_bindir}/pnpm%{pnpm_major_version}
fi


%files -n %{pkgname}%{pnpm_major_version}
%license LICENSE LICENSE.dependencies cargo-vendor.txt
%doc README.md
%{_bindir}/pnpm%{pnpm_major_version}
%{_bindir}/pnpx%{pnpm_major_version}
%{_bindir}/pn%{pnpm_major_version}
%{_bindir}/pnx%{pnpm_major_version}
%ghost %{_bindir}/pnpm
%ghost %{_bindir}/pnpx
%ghost %{_bindir}/pn
%ghost %{_bindir}/pnx

%changelog
%autochangelog
