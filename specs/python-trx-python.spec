Name:           python-trx-python
Version:        0.4.0
Release:        %{autorelease}
Summary:        Community-oriented file format for tractography

License:        BSD-2-Clause
# Test datasets (additional source files) are licensed CC-BY-4.0
SourceLicense:  %{license} AND CC-BY-4.0
URL:            https://github.com/tee-ar-ex/trx-python
Source0:        %{url}/archive/%{version}/trx-python-%{version}.tar.gz
# Test files defined in trx/fetcher.py
# All are (per their respective entries on figshare.com) CC-BY-4.0
%global test_data_repo tee-ar-ex/trx-test-data
%global test_data_tag v0.1.0
%global test_data_base_url https://github.com/%{test_data_repo}/releases/download/%{test_data_tag}
# https://figshare.com/articles/dataset/DSI/20001554/1?file=37624154
Source1:        %{test_data_base_url}/DSI.zip
# https://figshare.com/articles/dataset/memmap_test_data_zip/20020460
Source2:        %{test_data_base_url}/memmap_test_data.zip
# https://figshare.com/articles/dataset/trx_from_scratch_zip/20020412
Source3:        %{test_data_base_url}/trx_from_scratch.zip
# https://figshare.com/articles/dataset/gold_standard_zip/21520557
Source4:        %{test_data_base_url}/gold_standard.zip

BuildArch:      noarch

# This would enable more tests, but it was orphaned and retired.
# BuildRequires:  %%{py3_dist dipy}

%global _description %{expand:
This is a Python implementation of the trx file-format for tractography
data.

For details, please visit the documentation web-page at
https://tee-ar-ex.github.io/trx-python/.}

%description %_description


%package -n python3-trx-python
Summary:        %{summary}

%description -n python3-trx-python %_description


%prep
%autosetup -C -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency pytest-cov:ignore


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires --extras test


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files --assert-license trx


%check
%pyproject_check_import

export TRX_HOME="${PWD}/_home"
mkdir --parents "${TRX_HOME}"
ln '%{SOURCE1}' '%{SOURCE2}' '%{SOURCE3}' '%{SOURCE4}' "${TRX_HOME}"
%pytest -rs --verbose


%files -n python3-trx-python -f %{pyproject_files}
%doc README.md
%{_bindir}/trx
%{_bindir}/trx_concatenate_tractograms
%{_bindir}/trx_convert_dsi_studio
%{_bindir}/trx_convert_tractogram
%{_bindir}/trx_generate_from_scratch
%{_bindir}/trx_info
%{_bindir}/trx_manipulate_datatype
%{_bindir}/trx_simple_compare
%{_bindir}/trx_validate
%{_bindir}/trx_verify_header_compatibility
%{_bindir}/trx_visualize_overlap


%changelog
%autochangelog
