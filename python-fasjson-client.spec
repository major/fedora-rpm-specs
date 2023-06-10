%bcond_without tests

Name:           python-fasjson-client
Version:        1.0.8
Release:        %autorelease
Summary:        An OpenAPI client for FASJSON

License:        LGPL-3.0-or-later
URL:            https://github.com/fedora-infra/fasjson-client
Source:         %{pypi_source fasjson-client}
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-requests-mock
%endif

%global _description %{expand:
A python client library for the FASJSON API.}


%description %_description


%package -n     python3-fasjson-client
Summary:        %{summary}


%description -n python3-fasjson-client %_description


%pyproject_extras_subpkg -n python3-fasjson-client cli


%package -n     fasjson-client
Summary:        %{summary} - CLI
Requires:       python3-fasjson-client+cli = %{version}-%{release}


%description -n fasjson-client
A command line interface for the FASJSON API.


%prep
%autosetup -n fasjson-client-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires -x cli


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fasjson_client

# extra files we don't want to package
rm %{buildroot}%{python3_sitelib}/{config.toml.example,tox.ini}


%check
%if %{with tests}
# upstream runs pytest from within tox, but that includes lots of coverage
# flags we don't want
%pytest -v fasjson_client/tests/unit
%else
# even when tests are skipped, make sure the module imports correctly
%pyproject_check_import -e 'fasjson_client.tests*'
%endif


%files -n python3-fasjson-client -f %{pyproject_files}
%license LICENSE
%doc README.md


%files -n fasjson-client
%{_bindir}/fasjson-client


%changelog
%autochangelog
