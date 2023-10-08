Name:           python-aiofiles
Version:        23.2.1
Release:        %autorelease
Summary:        File support for asyncio

License:        Apache-2.0
URL:            https://github.com/Tinche/aiofiles
Source:         %{pypi_source aiofiles}

BuildArch:      noarch

BuildRequires:  python3-devel

# For tests, from pyproject.toml [tool.poetry.dev-dependencies]:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
# We do not require coverage and tox simply to run pytest.

%global _description %{expand:
aiofiles is an Apache2 licensed library, written in Python, for handling
local disk files in asyncio applications.}

%description %{_description}

%package -n python3-aiofiles
Summary:        %{summary}

%description -n python3-aiofiles %{_description}

%prep
%autosetup -n aiofiles-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aiofiles

%check
%pytest

%files -n python3-aiofiles -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
