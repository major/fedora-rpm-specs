%bcond check 1

# Fedora and EPEL have patchelf; RHEL/ELN don’t want it.
%bcond patchelf %[ %{undefined rhel} || %{defined epel} ]

Name:           maturin
Version:        1.14.1
Release:        %autorelease
Summary:        Build and publish Rust crates as Python packages
SourceLicense:  MIT OR Apache-2.0

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Apache-2.0 AND CC0-1.0
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 AND MIT
# Apache-2.0 OR BSD-2-Clause
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MIT-0
# MIT-0 OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
# bzip2-1.0.6
License:        %{shrink:
    0BSD AND
    Apache-2.0 AND
    Apache-2.0 WITH LLVM-exception AND
    BSD-3-Clause AND
    CC0-1.0 AND
    MIT AND
    MIT-0 AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    bzip2-1.0.6 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSD-2-Clause) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (MIT-0 OR Apache-2.0) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/PyO3/maturin
Source:         %{url}/archive/v%{version}/maturin-%{version}.tar.gz

# * Remove unwanted feature groups and optional dependencies, and/or those with
#   missing dependencies:
#
#   - “cross compile”: optional dependencies cargo-zigbuild, cargo-xwin, xz2.
#     Neither cargo-zigbuild nor cargo-xwin is packaged.
#   - “cross compile using zig or xwin”: features cross-compile, zig, xwin.
#     These would depend on “cross compile” optional dependencies. Note that
#     “cross-compile” is removed from the “full” feature, which is a default
#     feature.
#   - arwen-codesign, “Pure-Rust ad-hoc codesigning, only needed for
#     cross-compilation from non-macOS”, dropped with cross-compiling features
#     and not packaged anyway
#   - static feature: only applies to xz2, which we dropped, and we would not
#     want to link liblzma or any other system libraries statically anyway.
#
#   - upload feature: The “maturin upload” command is deprecated since 1.11.0,
#     and we lack some dependencies. Note that upload is removed from the
#     full feature, which is a default feature.
#   - “upload”: optional dependencies bytesize, configparser, dirs, ureq,
#     native-tls, rustls, rustls-pki-types, keyring, wild. These all support
#     the upload feature.
#   - rustls, native-tls; also only needed for the upload feature. Note that
#     rustls is removed from the default features.
#   - password-storage feature; associated with and requires the upload feature
#
#   - auditwheel feature: requires arwen, arwen-codesign, which we *could*
#     package but haven’t. Note that auditwheel is removed from the full
#     feature, which is a default feature.
Patch:          0001-drop-unavailable-features.patch

# * drop incompatible arguments from setuptools_rust cargo invocations
Patch:          0002-drop-incompatible-cargo-flags-from-setuptools_rust.patch

# * revert to building maturin with setuptools instead of bootstrapping maturin
Patch:          0003-revert-to-using-setuptools-for-non-maturin-bootstrap.patch

# Don’t specify generate-import-lib for PyO3 0.29
# https://github.com/PyO3/maturin/pull/3258
Patch:          %{url}/pull/3258.patch

BuildRequires:  cargo-rpm-macros >= 24
%if %{with patchelf}
BuildRequires:  tomcli
%endif

# Some sdist tests expect to see .gitignore files in the sdist, which only
# happens when they are run from inside a git repository, which we create via
# %%autosetup -S git, regardless of whether the check bcond is enabled or not.
BuildRequires:  git-core
# Some tests need to create virtualenvs, preferring “uv venv” (which would be a
# circular dependency) and falling back to “virtualenv.” It turns out that all
# such tests would try to pip-install things from PyPI and therefore must be
# skipped, so we don’t need either of these possible dependencies.

# maturin requires cargo to be available in $PATH
Requires:       cargo

%py_provides python3-maturin

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.

# There are two Python extras defined in pyproject.toml:
# zig:
#   We do have zig in Fedora. We don’t have python3dist(ziglang), which is just
#   a hack for installing the zig toolchain via PyPI, but we could work around
#   that. More importantly, we have patched out support for cross-compiling
#   with cargo-zigbuild, so there is no point in exposing this extra.
%if %{with patchelf}
# Based on %%pyproject_extras_subpkg -n maturin patchelf, but we have added
# a dependency on the patchelf command-line tool.
%package -n maturin+patchelf
Summary:        Metapackage for maturin: patchelf extras

Requires:       maturin%{?_isa} = %{version}-%{release}
Requires:       /usr/bin/patchelf

%description -n maturin+patchelf
This is a metapackage bringing in patchelf extras requires for maturin.
It makes sure the dependencies are installed.

%files -n maturin+patchelf -f %{_pyproject_ghost_distinfo}
%endif

%prep
%autosetup -n maturin-%{version} -p1 -S git
%cargo_prep

%if %{with patchelf}
# We don’t have python3dist(patchelf), corresponding to
# https://pypi.org/project/patchelf/, which is just a hack for installing the
# patchelf tool via PyPI. We can still provide the extra by ensuring the
# system-wide patchelf command-line tool is installed.
tomcli set pyproject.toml lists delitem \
    project.optional-dependencies.patchelf patchelf
%endif

# Ensure we don’t use Cargo.lock files from any of the test crates.
find test-crates -type f -name Cargo.lock -print -delete

# Remove pre-compiled Windows executable, “Mock for the windows python launcher
# we can insert in path,” to prove it is unused.
rm test-data/py.exe

%generate_buildrequires
%pyproject_buildrequires -x patchelf
%cargo_generate_buildrequires -f schemars

%if %{with check}
for toml in test-crates/*/Cargo.toml
do
  dir="$(dirname "${toml}")"
  case "${dir}" in
  # Relies on pinned PyO3 0.25; avoid a compat-package dependency.
  test-crates/pyo3-no-extension-module) continue ;;
  # We have no rust-uniffi package.
  test-crates/uniffi-*) continue ;;
  esac
  pushd "${dir}" >/dev/null
  %cargo_generate_buildrequires -a
  popd >/dev/null
done
%endif

%build
# No longer needs to be done manually in Fedora; needed in EPEL
export RUSTFLAGS="%{build_rustflags}"

# write license summary and breakdown
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l maturin

# generate and install shell completions
target/rpm/maturin completions bash > maturin.bash
target/rpm/maturin completions fish > maturin.fish
target/rpm/maturin completions zsh > _maturin

install -Dpm 0644 maturin.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 maturin.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _maturin -t %{buildroot}/%{zsh_completions_dir}

%if %{with check}
%check
# We chose not to generate a dependency on a pinned PyO3 0.25 in order to avoid
# an otherwise-unnecessary dependency on a rust-pyo3_0.25 compat package.
skip="${skip-} --skip=errors::pyo3_no_extension_module"

# These would try to install Python packages into virtualenvs from the network,
# such as cffi, pip, or uv, even if they are already installed system-wide.
# Some may also have other obstacles, e.g. no uniffi crate.
skip="${skip-} --skip=develop::develop_backend_parameterized_cases::"
skip="${skip-} --skip=develop::develop_cffi_cases::"
skip="${skip-} --skip=develop::develop_pip_cases::"
skip="${skip-} --skip=develop::develop_uv_cases::"
skip="${skip-} --skip=integration::integration_cases::"
skip="${skip-} --skip=integration::integration_cffi_cases::"
skip="${skip-} --skip=integration::integration_pyo3_abi3t"
skip="${skip-} --skip=integration::integration_pyo3_bin"
skip="${skip-} --skip=integration::pyo3_cffi_build_script"
skip="${skip-} --skip=pep517::pep517_default_profile"
skip="${skip-} --skip=pep517::pep517_editable_profile"

# Don’t attempt WASM-related tests.
# (“Failed to build a native library through cargo”)
skip="${skip-} --skip=integration::integration_wasm_hello_world"

# We are not sure why this sdist has extra contents:
#   pyo3_pure-0.1.0+abc123de/.cargo/.global-cache
#   pyo3_pure-0.1.0+abc123de/.cargo/.package-cache
#   pyo3_pure-0.1.0+abc123de/.cargo/.package-cache-mutate
#   pyo3_pure-0.1.0+abc123de/.cargo/registry/CACHEDIR.TAG
skip="${skip-} --skip=sdist::workspace_members_non_local_dep_sdist"

# Unclear exactly what’s going wrong here (“`cargo metadata` exited with an
# error:” with no further output), but this test is creating a local git
# repository and then a dependency on it, and it is little surprise that this
# turns out to be a bit brittle.
skip="${skip-} --skip=sdist::lib_with_parent_workspace_git_dep_sdist"

%{cargo_test -- -- ${skip-}}
%endif

%files -f %{pyproject_files}
%license license-apache
%license license-mit
%license LICENSE.dependencies
%doc README.md
%doc Changelog.md

%{_bindir}/maturin

%{bash_completions_dir}/maturin.bash
%{fish_completions_dir}/maturin.fish
%{zsh_completions_dir}/_maturin

%changelog
%autochangelog
