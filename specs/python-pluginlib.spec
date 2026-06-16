%global pypi_name pluginlib
%global sum  A framework for creating and importing plugins in Python
%global _description \
Pluginlib is a Python framework for creating and importing plugins. \
Pluginlib makes creating plugins for your project simple.

Name:           python-%{pypi_name}
Version:        0.11.0
Release:        %autorelease
Summary:        %{sum}

License:        MPL-2.0
URL:            https://github.com/Rockhopper-Technologies/pluginlib
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}


%prep
%autosetup -p0 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
