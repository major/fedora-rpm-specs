# Most of the tests require network access, so they are disabled by default.
%bcond_with     tests

%global         srcname         msal
%global         forgeurl        https://github.com/AzureAD/microsoft-authentication-library-for-python/
Version:        1.18.0~b1
%global         pypi_version    1.18.0b1
%global         tag             %{pypi_version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Microsoft Authentication Library (MSAL) for Python

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
The Microsoft Authentication Library for Python
enables applications to integrate with the Microsoft identity platform. It
allows you to sign in users or apps with Microsoft identities (Azure AD,
Microsoft Accounts and Azure AD B2Caccounts) and obtain tokens to call Microsoft
APIs such as Microsoft Graph or your own APIs registered with the Microsoft
identity platform. It is built using industry standard OAuth2 and OpenID Connect
protocols.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files msal


%if %{with tests}
%check
%pytest --disable-warnings tests
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
