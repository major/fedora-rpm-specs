%global modname  irc
%global projname %{modname}

%bcond_without tests

Name:           python-%{projname}
Version:        20.3.1
Release:        %autorelease
Summary:        Full-featured Python IRC library for Python

License:        MIT
URL:            https://github.com/jaraco/%{projname}
Source0:        %{pypi_source %{projname}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This library provides a low-level implementation of the IRC protocol for
Python. It provides an event-driven IRC client framework. It has a fairly
thorough support for the basic IRC protocol, CTCP, and DCC connections.}

%description %_description

%package     -n python3-%{projname}
Summary:        %{summary}

%description -n python3-%{projname} %_description

%prep
%autosetup -n %{projname}-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -E -i '/\t(pytest-|python_implementation )/d' setup.cfg

%if 0%{?rhel}
# relax setuptools requirement in EPEL
sed -i 's/setuptools>=56/setuptools/' pyproject.toml
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
