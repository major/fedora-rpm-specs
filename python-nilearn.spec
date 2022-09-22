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

Name:           python-nilearn
Version:        0.9.1
Release:        %autorelease
Summary:        Python module for fast and easy statistical learning on NeuroImaging data

License:        BSD
URL:            https://pypi.python.org/pypi/nilearn
# Use GitHub tar: pypi does not include all test data
Source0:        https://github.com/nilearn/nilearn/archive/%{version}/%{name}-%{version}.tar.gz


BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

Recommends:  %{py3_dist matplotlib}

%description
%{desc}

%package -n python3-nilearn
Summary:        %{summary}
BuildArch:      noarch

%description -n python3-nilearn
%{desc}

%prep
%autosetup -n nilearn-%{version}
# Remove shebangs
find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;
# Remove pre-compiled files
find . -name "*pyc" -exec rm -f '{}' \;

# Correct python command
sed -i 's/python/python3/' nilearn/plotting/html_document.py
#sed -i 's/python/python3/' nilearn/plotting/glass_brain_files/generate_json.sh

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

# Documentation also fetches imaging data set from online sources, so we cannot
# generate it. We include the link to the documentation in the description.

%install
%pyproject_install
%pyproject_save_files nilearn

%check

# https://github.com/nilearn/nilearn/issues/3232
%ifarch s390x %{power64} %{arm64} %{arm32} %{ix86}
k="${k:-}${k:+ and} not test_load_confounds"
%endif

%{pytest} -k "${k:-}" nilearn

%files -n python3-nilearn -f %{pyproject_files}
%doc AUTHORS.rst README.rst

%changelog
%autochangelog
