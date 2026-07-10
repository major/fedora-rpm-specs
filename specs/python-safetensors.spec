Name:           python-safetensors
Version:        0.8.0
Release:        %autorelease
Summary:        Python bindings for the safetensors library

# Results of the Cargo License Check
#
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
# Zlib
License:        %{shrink:
    Apache-2.0 AND
    MIT AND
    Zlib AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
SourceLicense:  Apache-2.0
# The PyPI package lives at https://pypi.org/project/safetensors/
# But the GitHub URL encompasses the entire project including the separately-packaged Rust crate
URL:            https://github.com/huggingface/safetensors
Source:         %{url}/archive/refs/tags/v%{version}/safetensors-%{version}.tar.gz

# feat: bump pyo3 to 0.29 (#796)
# https://github.com/safetensors/safetensors/commit/b3d8d72f341daa219b7a6c7e9e7335f5a14348a4
# Without changes to .github/workflows/python.yml or to
# bindings/python/Cargo.lock, which are not relevant here and are more likely
# to produce conflicts.
Patch:          safetensors-0.8.0-pyo3-0.29.patch

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust2rpm-helper
BuildRequires:  tomcli
# Test requirements
BuildRequires:  python3dist(pytest)
# https://github.com/huggingface/safetensors/pull/640
BuildRequires:  python3dist(fsspec)

# Exclude i686 because rust-safetensors does
ExcludeArch:    %{ix86}

# Define our own pytorch_arches macro until we have one system-wide.
%if %{undefined pytorch_arches}
%global pytorch_arches %{x86_64} %{arm64}
%endif

# Only include the torch extras on arches with PyTorch
%ifarch %{pytorch_arches}
%bcond torch 1
%else
%bcond torch 0
%endif

%global _description %{expand:
This library implements a new simple format for storing tensors safely
(as opposed to pickle) and that is still fast (zero-copy).}

%description %_description

%package -n python3-safetensors
Summary:        %{summary}

%description -n python3-safetensors %_description

%pyproject_extras_subpkg -n python3-safetensors numpy%{?with_torch:,torch}


%prep
%autosetup -p1 -n safetensors-%{version}
# Delete the bundled crate
rm -r safetensors/
# Replace the path-based dependency on the bundled crate with an exact-version
# dependency.
tomcli set bindings/python/Cargo.toml del dependencies.safetensors.path
tomcli set bindings/python/Cargo.toml str dependencies.safetensors.version '=%{version}'
# Patch out foreign (e.g. MacOS-only) dependencies.
find . -type f -name Cargo.toml -print \
    -execdir rust2rpm-helper strip-foreign -o '{}' '{}' ';'
# Also delete all the miscellaneous stuff from the GitHub release bundle
rm -r attacks/ docs/ .github/ codecov.y* Dockerfile.* .dockerignore flake.* .gitignore Makefile RELEASE.md
# Move toplevel README.md to eliminate name conflict
mv README.md README-safetensors.md
# cargo_prep needs to be run where Cargo.toml lives
cd bindings/python
%cargo_prep
cd ../..


%generate_buildrequires
# Get the cargo buildrequires first, so that maturin will succeed
cd bindings/python/
%cargo_generate_buildrequires
%pyproject_buildrequires -x numpy%{?with_torch:,torch}
cd ../..

%build
cd bindings/python/
# Generate the dependency license file first, so maturin will find it
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%pyproject_wheel
cd ../..


%install
%pyproject_install
# When saving the files, assert that a license file was found
%pyproject_save_files -l safetensors


%check
cd bindings/python/
# Omit submodules that require unpackaged extras / optional dependencies
%{pyproject_check_import %{shrink:
    --exclude 'safetensors.flax'
    --exclude 'safetensors.mlx'
    --exclude 'safetensors.paddle'
    --exclude 'safetensors.tensorflow'
    %{?!with_torch:--exclude 'safetensors.torch'}
    } }
# Test both the rust part of the bindings and the Python parts
%cargo_test
# But only run the tests/ and not benches/ in Python
# Ignore tests that require unpackaged extras / optional dependencies
# TODO: Should probably submit an upstream bug to skip these automatically if deps are missing
%if %{without torch}
ignore="${ignore-} --ignore=tests/test_multithreaded.py"
ignore="${ignore-} --ignore=tests/test_pread_backend.py"
ignore="${ignore-} --ignore=tests/test_pt_comparison.py"
ignore="${ignore-} --ignore=tests/test_pt_model.py"
ignore="${ignore-} --ignore=tests/test_simple.py"
%endif
ignore="${ignore-} --ignore=tests/test_flax_comparison.py"
ignore="${ignore-} --ignore=tests/test_tf_comparison.py"
%ifarch s390x
# On s390x architecture, test_serialize_file_releases_gil fails
# https://github.com/safetensors/safetensors/issues/812
ignore="${ignore-} --ignore=tests/test_threadable.py"
%endif
%pytest ${ignore-} tests/
cd ../..


%files -n python3-safetensors -f %{pyproject_files}
%doc README-safetensors.md bindings/python/README.md


%changelog
%autochangelog
