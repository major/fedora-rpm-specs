%global pypi_name trx-python
%global forgeurl https://github.com/tee-ar-ex/trx-python

Name:           python-%{pypi_name}
Version:        0.2.9
Release:        %{autorelease}
Summary:        Experiments with new file format for tractography
%global tag %{version}
%forgemeta
# Test datasets (additional source files) are licensed CC-BY-4.0
License:        BSD-2-Clause
URL:            %forgeurl
Source0:        %forgesource
# Test files
# Test suite tries to download them, but will only do a checksum check
# if they already exist.
# Source URLs and file version and their md5sum are listed in
# https://github.com/tee-ar-ex/trx-python/blob/master/trx/fetcher.py
#
# https://figshare.com/articles/dataset/DSI/20001554/1?file=37624154
# CC-BY-4.0
Source1:        https://figshare.com/ndownloader/files/37624154#/DSI.zip
# https://figshare.com/articles/dataset/memmap_test_data_zip/20020460
# CC-BY-4.0
Source2:        https://figshare.com/ndownloader/files/37624148#/memmap_test_data.zip
# https://figshare.com/articles/dataset/trx_from_scratch_zip/20020412
# CC-BY-4.0
Source3:        https://figshare.com/ndownloader/files/37624151#/trx_from_scratch.zip
# https://figshare.com/articles/dataset/gold_standard_zip/21520557
# CC-BY-4.0
Source4:        https://figshare.com/ndownloader/files/38146098#/gold_standard.zip
# Fix setuptools_scm listed as install requirement
# https://github.com/tee-ar-ex/trx-python/pull/75
Patch:          %{forgeurl}/pull/75.patch
# Fix shebangs and file mode
# https://github.com/tee-ar-ex/trx-python/pull/78
Patch:          %{forgeurl}/pull/78.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist psutil}
# For man pages
BuildRequires:  help2man

%global _description %{expand:
This is a Python implementation of the trx file-format for tractography
data.

For details, please visit the documentation web-page at
https://tee-ar-ex.github.io/trx-python/.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

# Install test files
install -p -m 644 -D -t tests %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4}

# Remove .py extension from executables
for SCRIPT in $(ls scripts/tff_*.py); do
  mv ${SCRIPT} ${SCRIPT//.py/}
done
# Fix glob in setup.py
sed -r -i 's|(scripts/)\*\.py|\1tff_*|' setup.py


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l trx

# Don't ship the tests
rm -rf %{buildroot}%{python3_sitelib}/trx/tests
sed -i '/tests/d' %{pyproject_files}

# Create man pages from --help and --version
mkdir man
mkdir -p %{buildroot}%{_mandir}/man1
for BIN in $(ls scripts/tff_*); do
    echo "Generating man page for ${BIN//*\//}"
    %{py3_test_envvars} help2man --section 1 --no-discard-stderr \
    --no-info --output man/${BIN//*\//}.1 ${BIN//*\//}
    install -m 0644 man/${BIN//*\//}.1 %{buildroot}%{_mandir}/man1
done


%check
# Tests require network for downloading test data. We can provide those
# without downloading. Use get_test_files.sh for updating if needed.
# Set directory for test files
export TRX_HOME="${PWD}/tests"
# scripts/tests is for internal testing (GitHub workflow)
%pytest -v --ignore=scripts/tests
%pyproject_check_import -e trx.tests*


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*
%{_bindir}/tff_*
%{_mandir}/man1/tff_*.1*


%changelog
%autochangelog
