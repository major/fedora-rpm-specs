%bcond tests 1
%bcond pypi_source 0

%global forgeurl https://codeberg.org/allauth/django-allauth

Name:           python-django-allauth
Version:        65.18.0
Release:        %autorelease
Summary:        Integrated set of Django authentication apps
License:        MIT
URL:            https://allauth.org/
%if %{with pypi_source}
# PyPI source has no tests
# Source:         %%{pypi_source django-allauth}
%else
Source:         %{forgeurl}/archive/%{version}.tar.gz#/django-allauth-%{version}.tar.gz
%endif
Patch:          django-allauth-no-setuptools_scm.diff

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  sed
%if %{with tests}
BuildRequires:  python3dist(pytest)
# pytest-django reads DJANGO_SETTINGS_MODULE from pytest.ini and runs
# django.setup() before conftest.py is imported; without it the test suite
# fails to collect (INSTALLED_APPS undefined / "Apps aren't loaded yet")
BuildRequires:  python3dist(pytest-django)
# async tests require the asyncio plugin
BuildRequires:  python3dist(pytest-asyncio)
# other test dependencies
BuildRequires:  python3dist(djangorestframework)
BuildRequires:  python3dist(psycopg)
BuildRequires:  python3dist(pyyaml)
%endif

%global _description %{expand:
Integrated set of Django applications addressing authentication, registration,
account management as well as 3rd party (social) account authentication.

## Rationale
Most existing Django apps that address the problem of social authentication
focus on just that. You typically need to integrate another app in order to
support authentication via a local account.

This approach separates the worlds of local and social authentication. However,
there are common scenarios to be dealt with in both worlds. For example, an
e-mail address passed along by an OpenID provider is not guaranteed to be
verified. So, before hooking an OpenID account up to a local account the e-mail
address must be verified. So, e-mail verification needs to be present in both
worlds.

Integrating both worlds is quite a tedious process. It is definitely not a
matter of simply adding one social authentication app, and one local account
registration app to your INSTALLED_APPS list.

This is the reason this project got started – to offer a fully integrated
authentication app that allows for both local and social authentication, with
flows that just work.}

%description %{_description}


%package -n python%{python3_pkgversion}-django-allauth
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-allauth %{_description}

%pyproject_extras_subpkg -n python%{python3_pkgversion}-django-allauth mfa openid saml socialaccount steam


%prep
%autosetup -p1 -n django-allauth
# we don't have django-ninja packaged yet: remove the unusable ninja modules
# (deleting source so an unsatisfiable `import ninja` fails at build, not at the
# user's runtime), their now-dead tests, and the test-project URLs that include
# them -- otherwise the broken include cascades through the shared URLconf and
# fails ~all tests.
rm -rf allauth/headless/contrib/ninja/
rm -rf allauth/idp/oidc/contrib/ninja/
rm -rf tests/apps/headless/contrib/ninja/
rm -rf tests/apps/idp/oidc/contrib/ninja/
rm -rf tests/projects/common/idp/ninja/
rm -rf tests/projects/common/headless/ninja/
sed -i '/ninja/d' tests/projects/common/idp/urls.py \
                   tests/projects/common/headless/urls.py
# the JWT strategy tests also probe a removed /headless/ninja/resource endpoint
# inline; drop those list entries so the (non-ninja) JWT/DRF coverage still runs
sed -i '\#/headless/ninja/resource#d' \
    tests/apps/headless/tokens/test_jwttokenstrategy.py


%generate_buildrequires
%pyproject_buildrequires -x mfa,openid,saml,socialaccount,steam


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files allauth


%check
%if %{with tests}
%pytest -v
%endif


%files -n python%{python3_pkgversion}-django-allauth -f %{pyproject_files}
%doc AUTHORS ChangeLog.rst README.rst


%changelog
%autochangelog
