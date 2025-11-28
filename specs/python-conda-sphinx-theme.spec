%global srcname conda-sphinx-theme
%global modname conda_sphinx_theme

Name:           python-%{srcname}
Version:        0.3.0
Release:        %autorelease
Summary:        A Sphinx theme for conda documentations

# main/conda_sphinx_theme/static/js/count.js is ISC
License:        BSD-3-Clause AND ISC
URL:            https://github.com/conda-incubator/conda-sphinx-theme
Source0:        https://github.com/conda-incubator/conda-sphinx-theme/archive/%{version}/%{srcname}-%{version}.tar.gz
# Use packaged fonts
Patch:          python-conda-sphinx-theme-fonts.patch

BuildArch:      noarch

%global _description %{expand:
This is the Conda Sphinx Theme. It extends the PyData Sphinx Theme
project by adding custom styling.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -p0 -n %{srcname}-%{version}
# Relase dep
sed -i -e '/pydata-sphinx-theme/s/<0.16/<0.17/' pyproject.toml
# Remove bundled fonts
rm -r conda_sphinx_theme/static/fonts

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}
# Doc build needs an installed version so we do it here
#PYTHONPATH=%{buildroot}%{python3_sitearch} make -C docs html
#

%check
# No tests
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CONTRIBUTING.md

%changelog
%autochangelog
