Name:           python-lazr-config
Version:        3.1
Release:        %autorelease
Summary:        Create configuration schemas, and process and validate configurations.

License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.config
Source:         %{pypi_source lazr_config}
# /usr/bin/zope-testrunner could not find lazr.config due to lazr.delegates being in
# a different directory *and* being invoked with python -sP
Patch:          lazr.config-avoid-python-sP.diff

BuildArch:      noarch
BuildRequires:  python3-devel
%if 0%{?python3_version_nodots} >= 315
# only needed for tests
# at runtime there is a fallback if this is not available, though somehow
# pkg_resources is still tried first
# see
# src/lazr/__init__.py:    import pkg_resources
# src/lazr/config/tests/test_config.py:import pkg_resources
# src/lazr/config/tests/test_docs.py:from pkg_resources import (
BuildRequires:  python3-pkg-resources
%endif


%global _description %{expand:
The LAZR config system is typically used to manage process configuration.
Process configuration is for saying how things change when we run systems on
different machines, or under different circumstances.

This system uses ini-like file format of section, keys, and values. The config
file supports inheritance to minimize duplication of information across files.
The format supports schema validation.}


%description %_description

%package -n     python3-lazr-config
Summary:        %{summary}
Requires:       python3-pkg-resources

%description -n python3-lazr-config %_description


%prep
%autosetup -p1 -n lazr_config-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files lazr


%check
%pyproject_check_import
%tox


%files -n python3-lazr-config -f %{pyproject_files}
%{python3_sitelib}/lazr.config-%{version}-py%{python3_version}-nspkg.pth
%exclude %{python3_sitelib}/lazr/config/tests


%changelog
%autochangelog
