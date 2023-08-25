%global pypi_name ipywidgets

Name:           python-%{pypi_name}
Version:        8.1.0
Release:        %autorelease
Summary:        IPython HTML widgets for Jupyter

License:        BSD-3-Clause
URL:            http://ipython.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%prep
%autosetup -p3 -n %{pypi_name}-%{version}
# Jupyterlab_widgets is a new dependency in ipywidgets 7.6
# and it contains code which enables widgets in Jupyter lab
# not requiring any manual steps. But we don't have Jupyter lab
# in Fedora yet so we do not need this package at all.
sed -i "/jupyterlab_widgets/d" setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
