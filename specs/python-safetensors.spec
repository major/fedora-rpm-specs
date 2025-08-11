Name:           python-safetensors
Version:        0.6.2
Release:        %autorelease
Summary:        Python bindings for the safetensors library

# Results of the Cargo License Check
#
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND MIT AND (Unlicense OR MIT)
SourceLicense:  Apache-2.0
# The PyPI package lives at https://pypi.org/project/safetensors/
# But the GitHub URL encompasses the entire project including the separately-packaged Rust crate
URL:            https://github.com/huggingface/safetensors
Source:         %{url}/archive/refs/tags/v%{version}/safetensors-%{version}.tar.gz

# Exclude i686 because rust-safetensors does
ExcludeArch:   %{ix86}
# Right now, torch is exclusive to x86_64 and aarch64 so only build the torch extra on those arches.
%ifarch %{x86_64} %{arm64}
%bcond torch 1
%else
%bcond torch 0
%endif

BuildRequires:	python3-devel
BuildRequires:	cargo-rpm-macros >= 24
BuildRequires:	tomcli
# Test requirements
BuildRequires:	python3dist(pytest)
# https://github.com/huggingface/safetensors/pull/640
BuildRequires:	python3dist(fsspec)

%global _description %{expand:
This library implements a new simple format for storing tensors safely
(as opposed to pickle) and that is still fast (zero-copy).}

%description %_description

%package -n python3-safetensors
Summary:	%{summary}

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
# Also delete all the miscellaneous stuff from the GitHub release bundle
rm -r attacks/ docs/ .github/ codecov.y* Dockerfile.* .dockerignore flake.* .gitignore Makefile RELEASE.md
# Move toplevel README.md to eliminate name conflict
mv README.md README-safetensors.md
# cargo_prep needs to be run where Cargo.toml lives
cd bindings/python
%cargo_prep
cd ../..
# The following Python sources are part of extras with dependencies not packaged in Fedora
# If that changes, we should enable and build the extras as well as not removing the sources
rm bindings/python/py_src/safetensors/flax.py
rm bindings/python/py_src/safetensors/mlx.py
rm bindings/python/py_src/safetensors/paddle.py
rm bindings/python/py_src/safetensors/tensorflow.py
%if %{without torch}
rm bindings/python/py_src/safetensors/torch.py
%endif
# Also remove test cases that require unpackaged dependencies
# TODO: Should probably submit an upstream bug to skip these automatically if deps are missing
rm bindings/python/tests/test_flax_comparison.py
rm bindings/python/tests/test_tf_comparison.py
%if %{without torch}
rm bindings/python/tests/test_pt_comparison.py
rm bindings/python/tests/test_pt_model.py
rm bindings/python/tests/test_simple.py
%endif


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
%pyproject_check_import
# Test both the rust part of the bindings and the Python parts
%cargo_test
# But only run the tests/ and not benches/ in Python
%pytest tests/
cd ../..


%files -n python3-safetensors -f %{pyproject_files}
%doc README-safetensors.md bindings/python/README.md


%changelog
%autochangelog
