%global pypi_name ipywidgets

Name:           python-%{pypi_name}
Version:        8.1.9
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
sed -i 's/widgetsnbextension~=4.*/widgetsnbextension>=4/' setup.cfg
sed -i 's/jupyterlab_widgets~=3.*/jupyterlab_widgets>=3/' setup.cfg

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
