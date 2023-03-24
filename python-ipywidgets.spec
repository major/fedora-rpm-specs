%global pypi_name ipywidgets

Name:           python-%{pypi_name}
Version:        8.0.5
Release:        %autorelease
Summary:        IPython HTML widgets for Jupyter

License:        BSD
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
%autosetup -p1 -n %{pypi_name}-%{version}
# Jupyterlab_widgets is a new dependency in ipywidgets 7.6
# and it contains code which enables widgets in Jupyter lab
# not requiring any manual steps. But we don't have Jupyter lab
# in Fedora yet so we do not need this package at all.
sed -i "/jupyterlab_widgets/d" setup.cfg

# Fix for ipython 8.11.0
# reported and proposed upstream
# https://github.com/jupyter-widgets/ipywidgets/issues/3711
sed -i "/Zm9vYmFy/s/\\\n//" ipywidgets/widgets/tests/test_widget_output.py

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
