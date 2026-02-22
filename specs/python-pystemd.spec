# Enable Python dependency generation
%{?python_enable_dependency_generator}

# Created by pyp2rpm-3.3.2
%global pypi_name pystemd

Name:           python-%{pypi_name}
Version:        0.15.3
Release:        %autorelease
Summary:        A thin Cython-based wrapper on top of libsystemd

License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/pystemd
Source:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Patch:          pystemd-revert-license-change.diff

BuildRequires:  gcc
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This library allows you to talk to systemd over D-Bus from Python,
without actually thinking that you are talking to systemd over D-Bus.

This allows you to programmatically start/stop/restart/kill and verify
service status from systemd point of view, avoiding subprocessing systemctl
and then parsing the output to know the result.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%generate_buildrequires
# with -x t this pulls in too many optional deps like cstq and pytest-cov
#pyproject_buildrequires -x t
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}
# remove installed source files if present
# seems to vary based on dependency versions (EPEL 9 does not install these)
rm -f %{buildroot}%{python3_sitearch}/%{pypi_name}/*.c
sed -i '/pystemd\/.*\.c$/d' %{pyproject_files}


%check
# e2e: no DBUS
# tests/test_daemon.py: This test fails in mock because systemd isn't running
# tests/test_version.py: This test requires additional dependencies (cstq)
# test_pickle.py::test_loaded_unit: no DBUS
%pytest -v \
  --ignore e2e/test_dbus.py \
  --ignore e2e/test_manager.py \
  --ignore e2e/test_pystemd_run.py \
  --ignore tests/test_daemon.py \
  --ignore tests/test_version.py \
  --deselect=tests/test_pickle.py::test_loaded_unit \
%{nil}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
