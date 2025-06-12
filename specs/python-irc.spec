%global modname  irc
%global projname %{modname}

%bcond_without tests
# Change the build backend in EPEL9 because `setuptools>=61.2`
# is needed for PEP621
%if 0%{?epel} == 9
%bcond_without hatch
%else
%bcond_with    hatch
%endif

Name:           python-%{projname}
Version:        20.5.0
Release:        %autorelease
Summary:        Full-featured Python IRC library for Python

License:        MIT
URL:            https://github.com/jaraco/%{projname}
Source0:        %{pypi_source %{projname}}

Patch1:         %{url}/pull/236.patch#/001-fix-for-py314.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with hatch}
BuildRequires:  tomcli
%endif

%global _description %{expand:
This library provides a low-level implementation of the IRC protocol for
Python. It provides an event-driven IRC client framework. It has a fairly
thorough support for the basic IRC protocol, CTCP, and DCC connections.}

%description %_description

%package     -n python3-%{projname}
Summary:        %{summary}

%description -n python3-%{projname} %_description

%prep
%autosetup -p1 -n %{projname}-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -E -i '/\t"pytest-/d' pyproject.toml

%if %{with hatch}
tomcli set pyproject.toml lists str "build-system.requires" "hatchling" "hatch-vcs"
tomcli set pyproject.toml str "build-system.build-backend" "hatchling.build"
tomcli set pyproject.toml str "tool.hatch.version.source" "vcs"
tomcli set pyproject.toml lists str "tool.hatch.build.targets.wheel.packages" %{modname}
%endif

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%if %{with tests}
%tox
%else
%pyproject_check_import -e irc.tests*
%endif

%files -n python3-%{projname} -f %{pyproject_files}
%license LICENSE
%doc README.rst NEWS.rst

%changelog
%autochangelog
