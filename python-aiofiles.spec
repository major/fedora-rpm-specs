%global commit 7a787da8e64d5e070581933a008a683ed7c3f4da
%global snapdate 20230628

Name:           python-aiofiles
Version:        23.2.0~^%{snapdate}git%(c='%{commit}'; echo "${c:0:7}")
Release:        %autorelease
Summary:        File support for asyncio

License:        Apache-2.0
URL:            https://github.com/Tinche/aiofiles
# Source:         %%{url}/archive/v%%{version}/aiofiles-%%{version}.tar.gz
Source:         %{url}/archive/%{commit}/aiofiles-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# For tests, from pyproject.toml [tool.poetry.dev-dependencies]:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
# We do not require coverage and tox simply to run pytest.

%global _description \
aiofiles is an Apache2 licensed library, written in Python, for handling\
local disk files in asyncio applications.

%description %{_description}

%generate_buildrequires
%pyproject_buildrequires -r

%package -n python3-aiofiles
Summary:        %{summary}

%description -n python3-aiofiles %{_description}

%prep
# %%autosetup -n aiofiles-%%{version}
%autosetup -n aiofiles-%{commit}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aiofiles

%check
%pytest

%files -n python3-aiofiles -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
