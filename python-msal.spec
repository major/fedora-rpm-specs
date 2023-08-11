%bcond tests 1
# For testing/development purposes, it could make sense to do a mock build with
# --with network_tests --enable-network.
%bcond network_tests 0

Name:           python-msal
Version:        1.24.0~b1
Release:        %autorelease
Summary:        Microsoft Authentication Library (MSAL) for Python

# SPDX
License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python
%global srcversion %(echo '%{version}' | tr -d '~')
Source:         %{url}/archive/%{srcversion}/microsoft-authentication-library-for-python-%{srcversion}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
The Microsoft Authentication Library for Python enables applications to
integrate with the Microsoft identity platform. It allows you to sign in users
or apps with Microsoft identities (Azure AD, Microsoft Accounts and Azure AD
B2C accounts) and obtain tokens to call Microsoft APIs such as Microsoft Graph
or your own APIs registered with the Microsoft identity platform. It is built
using industry standard OAuth2 and OpenID Connect protocols.}

%description %{_description}


%package -n python3-msal
Summary:        %{summary}
%description -n python3-msal %{_description}


%pyproject_extras_subpkg -n python3-msal broker


%prep
%autosetup -n microsoft-authentication-library-for-python-%{srcversion} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files msal


%check
%if %{with tests}
%if %{without network_tests}
# All of the following require network access:
k="${k-}${k+ and }not TestClientApplicationAcquireTokenSilentErrorBehaviors"
k="${k-}${k+ and }not TestClientApplicationAcquireTokenSilentFociBehaviors"
k="${k-}${k+ and }not TestClientApplicationForAuthorityMigration"
k="${k-}${k+ and }not TestTelemetryMaintainingOfflineState"
k="${k-}${k+ and }not TestClientApplicationWillGroupAccounts"
k="${k-}${k+ and }not TestClientCredentialGrant"
k="${k-}${k+ and }not TestScopeDecoration"
k="${k-}${k+ and }not (TestAuthority and test_unknown_host_wont_pass_instance_discovery)"
k="${k-}${k+ and }not (TestAuthority and test_wellknown_host_and_tenant)"
k="${k-}${k+ and }not (TestAuthority and test_wellknown_host_and_tenant_using_new_authority_builder)"
k="${k-}${k+ and }not TestAuthorityInternalHelperUserRealmDiscovery"
k="${k-}${k+ and }not TestCcsRoutingInfoTestCase"
k="${k-}${k+ and }not TestApplicationForRefreshInBehaviors"
k="${k-}${k+ and }not TestTelemetryOnClientApplication"
k="${k-}${k+ and }not TestTelemetryOnPublicClientApplication"
k="${k-}${k+ and }not TestTelemetryOnConfidentialClientApplication"
# Without network access, this even errors during test collection!
ignore="${ignore-} --ignore=tests/test_e2e.py"
%else
# This test requires browser interaction.
k="${k-}${k+ and }not (SshCertTestCase and test_ssh_cert_for_user_should_work_with_any_account)"
%endif

%pytest --disable-warnings tests ${ignore-} -k "${k-}" -v

%else
# The msal.broker module requires pymsalruntime, which is provided on Windows
# when the broker extra is installed, but which is not available at all
# otherwise.
%pyproject_check_import -e msal.broker
%endif


%files -n python3-msal -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
