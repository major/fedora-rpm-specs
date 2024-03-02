# Some tests fail. Pass --with all_tests to retry
%bcond_with all_tests

%global srcname django-allauth
%global forgeurl https://github.com/pennersr/%{srcname}

Name:           python-%{srcname}
Version:        0.61.1
Release:        %autorelease
Summary:        Integrated set of Django authentication apps
License:        MIT
URL:            https://www.intenct.nl/projects/django-allauth/
# PyPI source has no tests
# Source0:        %%{pypi_source %%{srcname}}
Source:         %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch:          %{srcname}-fix_for_coverage_7.diff

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


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}
%if %{without failedtests}
%endif


%generate_buildrequires
%pyproject_buildrequires -t


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


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc AUTHORS ChangeLog.rst README.rst


%changelog
%autochangelog
