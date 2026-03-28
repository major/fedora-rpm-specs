Name:           python-edgegrid
Version:        2.0.5
Release:        %autorelease
Summary:        Akamai EdgeGrid authentication handler for requests
License:        Apache-2.0
URL:            https://github.com/akamai/AkamaiOPEN-edgegrid-python
BuildArch:      noarch
Source:         %{pypi_source edgegrid_python}
# https://github.com/akamai/AkamaiOPEN-edgegrid-python/pull/133
Patch:          0001-Setuptools-82-compatibility.patch

%global _description %{expand:
This library implements an Authentication handler for HTTP requests using the
Akamai EdgeGrid Authentication scheme for Python.}


%description %_description


%package -n python3-edgegrid
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-edgegrid %_description


%prep
%autosetup -p 1 -n edgegrid_python-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l akamai


%check
%pytest -v


%files -n python3-edgegrid -f %{pyproject_files}


%changelog
%autochangelog
