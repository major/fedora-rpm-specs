# make main package noarch to run tests on all arches
# but the package is actually noarch, so don't generate debuginfo
%global debug_package %{nil}

%global desc %{expand: \
Nilearn is a Python module for fast and easy statistical learning on
NeuroImaging data.

It leverages the scikit-learn Python toolbox for multivariate statistics with
applications such as predictive modelling, classification, decoding, or
connectivity analysis.

This work is made available by a community of people, amongst which the INRIA
Parietal Project Team and the scikit-learn folks, in particular P. Gervais, A.
Abraham, V. Michel, A. Gramfort, G. Varoquaux, F. Pedregosa, B. Thirion, M.
Eickenberg, C. F. Gorgolewski, D. Bzdok, L. Esteve and B. Cipollini.

Detailed documentation is available at http://nilearn.github.io/.}

%global forgeurl https://github.com/nilearn/nilearn

Name:           python-nilearn
Version:        0.10.3
Release:        %autorelease
Summary:        Python module for fast and easy statistical learning on NeuroImaging data

%global tag %{version}
%forgemeta

# SPDX
License:        BSD-3-Clause
URL:            %forgeurl
# Use GitHub tar: pypi does not include all test data
Source0:        %forgesource

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
BuildRequires:  git-core
# For tests
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist plotly}

# Dependencies of 'plotting' extra
# To build the extra, we'd need kaleido in Fedora
Recommends:     %{py3_dist matplotlib}
Recommends:     %{py3_dist plotly}

%description
%{desc}

%package -n python3-nilearn
Summary:        %{summary}
BuildArch:      noarch

%description -n python3-nilearn
%{desc}

%prep
%forgesetup
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

# Remove shebangs
find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;
# Remove pre-compiled files
find . -name "*pyc" -exec rm -f '{}' \;

# Correct python command
sed -i 's/python/python3/' nilearn/plotting/html_document.py
#sed -i 's/python/python3/' nilearn/plotting/glass_brain_files/generate_json.sh

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -r

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

# Documentation also fetches imaging data set from online sources, so we cannot
# generate it. We include the link to the documentation in the description.

%install
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_install
%pyproject_save_files -l nilearn

%check

# https://github.com/nilearn/nilearn/issues/3232
%ifarch s390x %{power64} %{arm64} %{arm32} %{ix86}
k="${k:-}${k:+ and} not test_load_confounds"
%endif
# test fails on i686
%ifarch s390x %{power64} %{arm64} %{arm32} %{ix86}
k="${k:-}${k:+ and} not test_tfce_smoke"
%endif

# Fails with obscure error:
# _flapack.error: (liwork>=max(1,10*n)||liwork==-1) failed for 10th keyword liwork: dsyevr:liwork=1
k="${k:-}${k:+ and} not test_percentile_range"
# Requires kaleido (not available in Fedora)
k="${k:-}${k:+ and} not test_plot_surf[plotly]"
%{pytest} -v -k "${k:-}" nilearn

%files -n python3-nilearn -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
