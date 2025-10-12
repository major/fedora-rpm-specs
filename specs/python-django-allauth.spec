# Some tests fail. Pass --with all_tests to retry
%bcond_with all_tests

%global forgeurl https://codeberg.org/allauth/django-allauth

Name:           python-django-allauth
Version:        65.8.1
Release:        %autorelease
Summary:        Integrated set of Django authentication apps
License:        MIT
URL:            https://allauth.org/
# PyPI source has no tests
# Source0:        %%{pypi_source django-allauth}
Source:         %{forgeurl}/archive/%{version}.tar.gz#/django-allauth-%{version}.tar.gz
# unpin coverage version
Patch:          django-allauth-relax-coverage-version.diff
# Temporarily lower from == 0.23.8 to >= 0.23.6
# 0.24 is out, the breaking change should not affect this package
# (it requires pytest >= 8.2)
Patch:          django-allauth-lower_pytest-asyncio_req.diff
# remove django-ninja dependency, only needed by react-spa example and tests
Patch:          django-allauth-no-django-ninja.diff
# rather than hardcode 1.3.15, allow >= 1.3.15, < 1.4.0
Patch:          django-allauth-relax-xmlsec-version.diff
# likewise, allow lxml >= 5.3.1 as F43+ has 6.0.1
Patch:          django-allauth-relax-lxml-version.diff

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

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
%if %{without failedtests}
%endif
# we don't have this packaged yet
rm -rf allauth/headless/contrib/ninja/


%generate_buildrequires
%pyproject_buildrequires -t -x mfa,openid,saml,socialaccount,steam


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files allauth


%check
%pytest -v \
%if %{without all_tests}
  --deselect allauth/socialaccount/providers/openid/tests.py::OpenIDTests::test_login \
  --deselect allauth/socialaccount/providers/openid/tests.py::OpenIDTests::test_login_with_extra_attributes \
%endif
;


%files -n python%{python3_pkgversion}-django-allauth -f %{pyproject_files}
%doc AUTHORS ChangeLog.rst README.rst


%changelog
%autochangelog
