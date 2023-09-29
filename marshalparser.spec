Name:           marshalparser
Version:        0.3.4
Release:        %autorelease
Summary:        Parser for Python internal Marshal format

# SPDX
License:        MIT
URL:            https://github.com/fedora-python/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# For tests on various pyc files
# We intentionally skip those on RHEL to avoid pulling other Pythons into next RHEL.
# When a new Python is added into RHEL, the new version should be explicitly added.
%if %{undefined rhel}
BuildRequires:  python3.6
BuildRequires:  python3.8
BuildRequires:  python3.9
BuildRequires:  python3.10
BuildRequires:  python3.11
BuildRequires:  python3.12
%endif

%generate_buildrequires
%pyproject_buildrequires -x test

%description
Parser for Python internal Marshal format which can fix pyc files
reproducibility.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%pytest

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
