Name:           python-dbus-fast
Version:        2.44.5
Release:        %autorelease
Summary:        A faster version of dbus-next
License:        MIT
URL:            https://github.com/bluetooth-devices/dbus-fast
Source:         %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc

# Cherry-picked from pyproject.toml section [tool.poetry.group.dev.dependencies]
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-asyncio
BuildRequires: python3-cairo
BuildRequires: python3-gobject
# Used to run the tests
BuildRequires: /usr/bin/dbus-run-session


%global _description %{expand:
dbus-fast is a Python library for DBus that aims to be a performant fully
featured high level library primarily geared towards integration of
applications into Linux desktop and mobile environments.}

%description %_description


%package -n     python3-dbus-fast
Summary:        %{summary}

%description -n python3-dbus-fast %_description


%prep
%autosetup -n dbus-fast-%{version}

# Relax poetry dependencies
sed -i 's/Cython>=3,<3.1.0/Cython>=3/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L dbus_fast


%check
%global __pytest dbus-run-session -- %{__pytest}
%pytest --no-cov --ignore tests/benchmarks

%pyproject_check_import


%files -n python3-dbus-fast -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc CHANGELOG.md


%changelog
%autochangelog
