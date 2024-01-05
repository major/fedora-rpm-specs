%bcond_without tests

%global desc %{expand: \
Messy datasets? Missing values? missingno provides a small toolset
of flexible and easy-to-use missing data visualizations and utilities
that allows you to get a quick visual summary of the completeness
(or lack thereof) of your dataset.}

Name:           python-missingno
Version:        0.5.2
Release:        %autorelease
Summary:        Missing data visualization module for Python
# SPDX
License:        MIT
URL:            https://github.com/ResidentMario/missingno
Source0:        %{url}/archive/%{version}/missingno-%{version}.tar.gz
BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
%{desc}

%package -n python3-missingno
Summary:        %{summary}

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: quilt

%description -n python3-missingno
%{desc}

%prep
%autosetup -n missingno-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l missingno

%check
mkdir -p ~/.config/matplotlib/
echo "backend: Agg" > ~/.config/matplotlib/matplotlibrc
export PYTHONPATH=".:$RPM_BUILD_ROOT/%{python3_sitelib}"
# https://github.com/ResidentMario/missingno/blob/master/CONTRIBUTING.md#testing
# temporarily disabled: failing unreliably
#%%{pytest} --mpl-generate-path=tests/baseline tests/viz_tests.py
%{pytest} tests/test_util.py

%files -n python3-missingno  -f %{pyproject_files}
%doc README.md CONFIGURATION.md paper.bib paper.md

%changelog
%autochangelog
