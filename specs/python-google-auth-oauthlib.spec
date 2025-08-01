%global pypi_name google-auth-oauthlib

Name:           python-%{pypi_name}
Version:        1.2.2
Release:        %autorelease
Summary:        Google oAuth Authentication Library

License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib
Source0:        %{pypi_source google_auth_oauthlib}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)

%description
This library provides oauthlib integration with google-auth.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This library provides oauthlib integration with google-auth.

%prep
%autosetup -n google_auth_oauthlib-%{version}
rm -rf /docs/

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files google_auth_oauthlib

%check
%pytest -k 'not test_run_local_server_bind_addr'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/google-oauthlib-tool
%exclude %{python3_sitelib}/docs/

%changelog
%autochangelog
