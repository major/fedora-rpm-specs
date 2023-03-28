Name:           python-pytest-cython
Version:        0.2.1
Release:        %autorelease
Summary:        Pytest plugin for testing Cython extension modules

License:        MIT
URL:            https://github.com/lgpage/pytest-cython
Source0:        %{url}/archive/v%{version}/pytest-cython-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies
BuildRequires:  gcc-c++
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist nox}

%global _desc %{expand:
This pytest plugin enables the doctesting of C extension modules for
Python, specifically created through Cython.}

%description %_desc

%package     -n python3-pytest-cython
Summary:        %{summary}

%description -n python3-pytest-cython %_desc

%prep
%autosetup -n pytest-cython-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_cython

%check
# Cannot use the %%pytest macro because an import path check fails
pytest

%files -n python3-pytest-cython -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE.md

%changelog
%autochangelog
