#global commit  f44636f00666b8eb869417960926d01690ff4f42
#global shortcommit #(c=#{commit}; echo ${c:0:7})
#global checkout_date 2023094
%global upstream_version  1.6.1

# setup.py does not list all requirements, and we also unbundle quite a few
# from the externals folder, so we can't only rely on the automatic generator
# here.
# Additionally, requirements.txt seems to be dev requirements, and is not used
# in setup.py for install_requires.

Name:           python-mne

%if "0%{?commit}" != "0"
Version:        %{upstream_version}^%{checkout_date}git%{shortcommit}
%global python_version  %{upstream_version}.dev%{checkout_date}
%else
Version:        %{upstream_version}
%global python_version  %{version}
%endif

Release:        %autorelease
Summary:        Magnetoencephalography (MEG) and Electroencephalography (EEG) data analysis

# Bundled FieldTrip
# https://github.com/fieldtrip/fieldtrip/blob/master/realtime/src/buffer/python/FieldTrip.py
# Not possible to package because it is matlab package with some plugins

# SPDX
License:        BSD-3-Clause
URL:            http://martinos.org/mne/


%if "0%{?commit}" != "0"
Source0:        https://github.com/mne-tools/mne-python/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/mne-tools/mne-python/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

#Source1:        https://s3.amazonaws.com/mne-python/datasets/MNE-sample-data-processed.tar.gz

# Fix pandas test
# https://github.com/mne-tools/mne-python/pull/12347
Patch:          https://patch-diff.githubusercontent.com/raw/mne-tools/mne-python/pull/12347.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# The base package is arched to make it easier for us to detect arch-dependent
# test failures, since the tests will always be run on every platform, and
# easier for us to skip failing tests if necessary, since we can be sure that
# %%ifarch macros work as expected.
#
# Since the package still contains no compiled machine code, we still have no
# debuginfo.
%global debug_package %{nil}

BuildRequires:  python3-devel

%global _description %{expand:
This package is designed for sensor- and source-space analysis of M-EEG data,
including frequency-domain and time-frequency analyses and non-parametric
statistics.}

%description %_description

%package -n python3-mne
Summary:        %{summary}

# This package is now arched because some dependencies are not available on
# every architecture.

Provides:       bundled(bootstrap)
Provides:       bundled(js-jquery)
Provides:       bundled(js-jquery-ui)
Provides:       bundled(js-d3)
Provides:       bundled(js-mpld3)
Provides:       bundled(python3-FieldTrip)
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy

# Test deps
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pandas
BuildRequires:  python3-h5py
BuildRequires:  python3-decorator
%ifnarch s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=2116690
BuildRequires:  python3-pymatreader
%endif
BuildRequires:  python3-h5io
BuildRequires:  python3-jinja2
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-Traits
BuildRequires:  python3-tqdm
BuildRequires:  python3-nibabel
%ifnarch s390x
BuildRequires:  python3-pyedflib
%endif
BuildRequires:  python3-nilearn
BuildRequires:  python3-qt5
BuildRequires:  python3-dipy
BuildRequires:  python3-xlrd
BuildRequires:  python3-nitime
BuildRequires:  python3-pooch
BuildRequires:  python3-nbformat
BuildRequires:  python3-vtk
# Makes pytest segfault
# BuildRequires:  python3-mayavi

Requires:       python3-matplotlib
Requires:       python3-decorator
Requires:       python3-h5io
Requires:       python3-six
Requires:       python3-tempita
Requires:       python3-tqdm
%ifnarch s390x
Requires:       python3-pymatreader
%endif
Recommends:     python3-scikit-learn
Recommends:     python3-pandas
Recommends:     python3-patsy
Recommends:     python3-pillow
Recommends:     python3-h5py
Recommends:     python3-statsmodels
Recommends:     python3-Traits

# Should be included by the dep generator as they're mentioned in setup.py
# Requires:       python3-numpy
# Requires:       python3-scipy

%description -n python3-mne %_description

%prep
%if "0%{?commit}" != "0"
%autosetup -n mne-python-%{commit} -p1
%else
%autosetup -n mne-python-%{version} -p1
%endif

# fix non-executable scripts
sed -i -e '1{\@^#!/usr/bin/env python@d}' mne/commands/*.py
sed -i -e '1{\@^#!/usr/bin/env python@d}' mne/datasets/hf_sef/hf_sef.py
sed -i -e '1{\@^#!/usr/bin/env python@d}' mne/stats/cluster_level.py

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/--cov[^[:blank:]]+//g' pyproject.toml


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{python_version}'
%pyproject_buildrequires

#cp -p %{SOURCE1} .
#python -c "import mne; mne.datasets.sample.data_path(verbose=True, download=False)"

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{python_version}'
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION='%{python_version}'
%pyproject_install
%pyproject_save_files -l mne

%check
export SETUPTOOLS_SCM_PRETEND_VERSION='%{python_version}'
export MNE_SKIP_TESTING_DATASET_TESTS=true
export MNE_SKIP_NETWORK_TESTS=1
export MNE_DONTWRITE_HOME=true
export MNE_FORCE_SERIAL=true

# Deselected tests require additional data or don't work in mock
# Two deselected for sklearn warnings
ignore="${ignore-} --ignore=mne/datasets/tests/test_datasets.py"
ignore="${ignore-} --ignore=mne/utils/tests/test_numerics.py"
# Tools directory ignored as it contains tests for upstream release process

# required for some tests
mkdir subjects

# Hangs:
k="${k-}${k+ and }not test_thresholds[NumPy]"
# FileNotFoundError (file 'test_eyelink.asc' not in repo):
k="${k-}${k+ and }not test_annotations_without_offset"
%ifarch s390x || ppc64le
# Test fails on s390x and ppc64le.
k="${k-}${k+ and }not test_spectrum_complex[welch-False]"
%endif

# https://github.com/mne-tools/mne-python/blob/v1.0.3/tools/github_actions_test.sh#L7
# skip tests that require network
m='not (slowtest or pgtest)'

# Erroring on DeprecationWarnings makes sense upstream, but is probably too
# strict for distribution packaging.
%pytest -v -m "${m}" ${ignore-} -k "${k-}" -W 'ignore::DeprecationWarning'


%files -n python3-mne -f %{pyproject_files}
%doc README.rst examples
%{_bindir}/mne

%changelog
%autochangelog
