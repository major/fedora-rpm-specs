Name:           python-lazr-config
Version:        3.0
Release:        %autorelease
Summary:        Create configuration schemas, and process and validate configurations.

License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.config
Source:         %{pypi_source lazr.config}
# /usr/bin/zope-testrunner could not find lazr.config due to lazr.delegates being in
# a different directory *and* being invoked with python -sP
Patch:          lazr.config-avoid-python-sP.diff

BuildArch:      noarch
BuildRequires:  python3-devel


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

%description -n python3-lazr-config %_description


%prep
%autosetup -p1 -n lazr.config-%{version}


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


%changelog
%autochangelog
