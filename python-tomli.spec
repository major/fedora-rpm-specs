Name:           python-tomli
Version:        2.0.1
Release:        %autorelease
Summary:        A little TOML parser for Python

License:        MIT
URL:            https://pypi.org/project/tomli/
Source0:        https://github.com/hukkin/tomli/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# The test suite uses the stdlib's unittest framework, but we use %%pytest
# as the test runner.
BuildRequires:  python3-pytest

%global _description %{expand:
Tomli is a Python library for parsing TOML.
Tomli is fully compatible with TOML v1.0.0.}


%description %_description

%package -n python3-tomli
Summary:        %{summary}

%description -n python3-tomli %_description


%prep
%autosetup -p1 -n tomli-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tomli


%check
%py3_check_import tomli
%pytest


%files -n python3-tomli -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%license LICENSE


%changelog
%autochangelog
