Name:           python-parallel-web
Version:        0.4.2
Release:        %autorelease
Summary:        The official Python library for the Parallel API

License:        MIT
URL:            https://github.com/parallel-web/parallel-sdk-python
Source:         %{pypi_source parallel_web}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
The Parallel Python library provides convenient access to the Parallel REST API
from any Python 3.9+ application. The library includes type definitions for all
request params and response fields, and offers both synchronous and
asynchronous clients powered by httpx.

The REST API documentation can be found on docs.parallel.ai. The full API of
this library can be found in api.md.}

%description %_description

%package -n     python3-parallel-web
Summary:        %{summary}

%description -n python3-parallel-web %_description


%pyproject_extras_subpkg -n python3-parallel-web aiohttp


%prep
%autosetup -p1 -n parallel_web-%{version}
%pyproject_patch_dependency hatchling:drop_upper

rm src/parallel/lib/.keep


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l parallel


%check
%pyproject_check_import


%files -n python3-parallel-web -f %{pyproject_files}
%doc api.md CHANGELOG.md CONTRIBUTING.md SECURITY.md README.md
%license LICENSE


%changelog
%autochangelog
