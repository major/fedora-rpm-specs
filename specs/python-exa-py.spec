Name:           python-exa-py
Version:        2.10.2
Release:        %autorelease
Summary:        Python SDK for Exa API

License:        MIT
URL:            https://github.com/exa-labs/exa-py
Source:         %{pypi_source exa_py}
# Fetched from exa-py repository.
# Since upstream version 2.12.1, sdist includes LICENSE.
# When build for this version, remove this patch.
Patch:          add-license.patch

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
The official Python SDK for Exa, the web search API for AI.}

%description %_description

%package -n     python3-exa-py
Summary:        %{summary}

%description -n python3-exa-py %_description


%prep
%autosetup -p1 -n exa_py-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l exa_py


%check
# exa-py repository does not include other exa_py.websets.async_* modules.
# hermes-agent does not rely on those async modules. It is okay to package without them.
%pyproject_check_import -e exa_py.websets.async_client


%files -n python3-exa-py -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
