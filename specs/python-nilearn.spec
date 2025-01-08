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
Version:        0.11.1
Release:        %autorelease
Summary:        Python module for fast and easy statistical learning on NeuroImaging data

%global tag %{version}
%forgemeta

# SPDX
License:        BSD-3-Clause
URL:            %forgeurl
# Use GitHub tar: pypi does not include all test data
Source:         %forgesource

# python-scikit-learn is ExcludeArch: %%{ix86}
ExcludeArch:    %{ix86}

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
%forgeautosetup -p1
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

# Remove shebangs
find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;
# Remove pre-compiled files
find . -name "*pyc" -exec rm -f '{}' \;

# Correct python command
sed -i 's/python/python3/' nilearn/plotting/html_document.py
#sed -i 's/python/python3/' nilearn/plotting/glass_brain_files/generate_json.sh

# Remove pytest-reporter-html1 arguments
sed -r -i 's/--template=[^[:blank:]"]+//' pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -r

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

# Documentation also fetches imaging data set from online sources, so we cannot
# generate it. We include the link to the documentation in the description.

%install
%pyproject_install
%pyproject_save_files -l nilearn

%check
%ifarch x86_64
# [BUG] test_canica_square_img fails on some x86_64 machines
# https://github.com/nilearn/nilearn/issues/4876
k="${k-}${k+ and }not test_canica_square_img"
%endif

# Requires kaleido (not available in Fedora)
k="${k-}${k+ and }not test_plot_surf[plotly]"
%{pytest} -v "${k:+-k $k}" nilearn

%files -n python3-nilearn -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
