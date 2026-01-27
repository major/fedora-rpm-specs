Name:               python-arrow
Version:            1.4.0
Release:            %autorelease
Summary:            Better dates and times for Python

License:            Apache-2.0
URL:                https://github.com/arrow-py/arrow
Source:             %{pypi_source arrow}
# downstream-only
Patch:              0002-Fedora-dependency-adjustments.patch


BuildArch:          noarch

%global _description %{expand:
Arrow is a Python library that offers a sensible and human-friendly approach to
creating, manipulating, formatting and converting dates, times and timestamps.
It implements and updates the datetime type, plugging gaps in functionality and
providing an intelligent module API that supports many common creation
scenarios.  Simply put, it helps you work with dates and times with fewer
imports and a lot less code.}


%description %_description


%package -n         python3-arrow
Summary:            %{summary}
BuildRequires:      python3-devel


%description -n python3-arrow %_description


%prep
%autosetup -p 1 -n arrow-%{version}
# Fix python tzdata dependency
sed -i 's/tzdata;python_version/pytzdata;python_version/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files arrow


%check
%pytest


%files -n python3-arrow -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSE


%changelog
%autochangelog
