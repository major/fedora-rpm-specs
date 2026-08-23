%global sname blazarclient

%global _description %{expand:
This is a client for the OpenStack Blazar API. It provides a Python
API (the blazarclient module) and a command-line script (blazar).}

Name:             python-%{sname}
Version:          4.5.0
Release:          %autorelease
Summary:          Python API and CLI for the Blazer Client
License:          Apache-2.0
URL:              https://launchpad.net/blazar
Source0:          %{pypi_source python_%{sname}}

BuildArch:        noarch


%description %{_description}


%package -n python3-%{sname}
Summary:          %{summary}


%description -n python3-%{sname} %{_description}


%prep
%autosetup -n python_%{sname}-%{version}

# Ignore global online constraints file
sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

# Drop dependencies for lint, coverage, ...
%pyproject_patch_dependency reno:ignore
%pyproject_patch_dependency hacking:ignore
%pyproject_patch_dependency coverage:ignore


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l %{sname}


%check
%tox


%files -n python3-%{sname} -f %{pyproject_files}
%doc ChangeLog README.rst
%{_bindir}/blazar


%changelog
%autochangelog
