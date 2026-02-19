# Test dependencies too old for RHEL 10
%if 0%{?rhel}
%bcond tests 0
%else
%bcond tests 1
%endif

Name: pulp-cli-deb
Version: 0.4.3
Release: %autorelease
Summary: Command line interface to talk to the Pulp 3 REST API (deb plugin)
License: GPL-2.0-or-later
BuildArch: noarch
URL: https://github.com/pulp/%{name}

Source: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel

Requires: pulp-cli >= 0.29.0

Recommends: python3-pygments
Recommends: python3-click-shell
Recommends: python3-secretstorage

%description
pulp-cli provides the "pulp" command, able to communicate with the Pulp3 API in
a more natural way than plain http. Specifically, resources can not only be
referenced by their href, but also their natural key (e.g. name). It also
handles waiting on tasks on behalf of the user.

%prep
%autosetup -p1

# Remove the Python version upper bound to enable building with new versions in Fedora
sed -i '/requires-python =/s/,<3\.[0-9]\+//' pyproject.toml

# Remove upper version bound on setuptools to enable building with new versions in Fedora
sed -i '/requires =.*setuptools/s/<[0-9]\+//' pyproject.toml

# Remove upper version bound on packaging to enable building with new versions in Fedora
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml

# Remove all bounds on test dependencies; we must use what we have
sed -r -Ei 's/^([a-zA-Z0-9._-]+).*/\1/' test_requirements.txt

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires test_requirements.txt
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pulpcore

%if %{with tests}
%check
%pyproject_check_import pulpcore
%pytest -m help_page
%endif

%files -n %{name} -f %{pyproject_files}
%license LICENSE
%doc CHANGES.md

%changelog
%autochangelog
