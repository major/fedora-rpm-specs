# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

%global pypi_name nbclient

%global _description %{expand:
NBClient, a client library for programmatic notebook execution, is a tool for 
running Jupyter Notebooks in different execution contexts. NBClient was spun 
out of nbconvert (formerly ExecutePreprocessor). NBClient lets you execute notebooks.
}

Name:           python-%{pypi_name}
Version:        0.10.2
Release:        %autorelease
Summary:        A client library for executing notebooks

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://jupyter.org
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

%bcond bootstrap 0
%bcond check %{without bootstrap}

%description
%_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name}
%_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Drop version limit from pytest
sed -i "/pytest/s/,<8//" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with check}
%check
%pytest -vv
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/jupyter-execute


%changelog
%autochangelog
