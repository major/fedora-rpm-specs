%global pypi_name ipywidgets

Name:           python-%{pypi_name}
Version:        8.1.5
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
