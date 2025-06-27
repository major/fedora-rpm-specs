Name:		python-safetensors
Version:	0.5.3
Release:	%autorelease
Summary:	Python bindings for the safetensors library

# Results of the Cargo License Check
# 
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:	Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
SourceLicense:	Apache-2.0
# The PyPI package lives at https://pypi.org/project/safetensors/
# But the GitHub URL encompasses the entire project including the separately-packaged Rust crate
URL:		https://github.com/huggingface/safetensors
Source:		%{pypi_source safetensors}
# Patch the bindings crate to use the upstream crate, rather than the bundled crate sources
Patch:		pysafetensors.patch

# Exclude i686 because rust-safetensors does
ExcludeArch:	%{ix86}
# Right now, torch is exclusive to x86_64 and aarch64
%ifarch x86_64 || arch aarch64
# Temporarily disable torch extra because pytorch is not cmpatible with Python 3.14
# F43FailsToInstall: python3-torch
# https://bugzilla.redhat.com/show_bug.cgi?id=2372164
%bcond_with torch
%else
%bcond_with torch
%endif

BuildRequires:	python3-devel
BuildRequires:	gcc
BuildRequires:	cargo-rpm-macros >= 24
# Test requirements
BuildRequires:	python3-pytest

%global _description %{expand:
This library implements a new simple format for storing tensors safely
(as opposed to pickle) and that is still fast (zero-copy).}

%description %_description

%package -n python3-safetensors
Summary:	%{summary}

%description -n python3-safetensors %_description

%if %{with torch}
%pyproject_extras_subpkg -n python3-safetensors numpy,torch
%else
%pyproject_extras_subpkg -n python3-safetensors numpy
%endif


%prep
%autosetup -p1 -n safetensors-%{version}
%cargo_prep
# Copy the LICENSE file out of the bundled crate
cp -a safetensors/LICENSE LICENSE
# Delete the bundled crate
rm -r safetensors/
# Remove locked Rust dependencies on the bindings
rm bindings/python/Cargo.lock
# The following Python sources are part of extras with dependencies not packaged in Fedora
# If that changes, we should enable and build the extras as well as not removing the sources
rm py_src/safetensors/flax.py
rm py_src/safetensors/mlx.py
rm py_src/safetensors/paddle.py
rm py_src/safetensors/tensorflow.py
%if %{without torch}
rm py_src/safetensors/torch.py
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
cd ../../
%if %{with torch}
%pyproject_buildrequires -x numpy,torch
%else
%pyproject_buildrequires -x numpy
%endif

%build
%pyproject_wheel
cd bindings/python/
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
cd ../../


%install
%pyproject_install
%pyproject_save_files safetensors


%check
%pyproject_check_import
# Test both the rust part of the bindings and the Python parts
cd bindings/python/
%cargo_test
# But only run the tests/ and not benches/ in Python
%pytest tests/
cd ../../


%files -n python3-safetensors -f %{pyproject_files}
%license LICENSE bindings/python/LICENSE.dependencies
%doc bindings/python/README.md


%changelog
%autochangelog
