Name:           python-anthropic
Version:        0.87.0
Release:        %autorelease
Summary:        The official Python library for the anthropic API

License:        MIT
URL:            https://github.com/anthropics/anthropic-sdk-python
Source:         %{pypi_source anthropic}
Patch:          relax-hatchling.patch

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
The Claude SDK for Python provides access to the Claude API from Python applications.}

%description %_description

%package -n     python3-anthropic
Summary:        %{summary}

%description -n python3-anthropic %_description


%prep
%autosetup -p1 -n anthropic-%{version}


%generate_buildrequires
%pyproject_buildrequires -x aiohttp,bedrock,mcp,vertex


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l anthropic


%check
%pyproject_check_import


%files -n python3-anthropic -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md SECURITY.md api.md helpers.md tools.md examples/
%license LICENSE


%changelog
%autochangelog
