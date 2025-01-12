%global modname  atlassian
%global projname %{modname}-python-api
%global srcname %{modname}_python_api

%bcond_without tests

Name:           python-%{projname}
Version:        3.41.18
Release:        %autorelease
Summary:        Python Atlassian REST API Wrapper

License:        Apache-2.0
URL:            https://github.com/atlassian-api/%{projname}
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
The atlassian-python-api library provides a simple and convenient way to
interact with Atlassian products (such as Jira Service management, Jira
Software, Confluence, Bitbucket and apps Insight, X-Ray) using Python. It is
based on the official REST APIs of these products, as well as additional private
methods and protocols (such as xml+rpc and raw HTTP requests). This library can
be used to automate tasks, integrate with other tools and systems, and build
custom applications that interact with Atlassian products. It supports a wide
range of Atlassian products, including Jira, Confluence, Bitbucket, StatusPage
and others, and is compatible with both Atlassian Server and Cloud instances.

Overall, the atlassian-python-api is a useful tool for Python developers who
want to work with Atlassian products. It is well-documented and actively
maintained, and provides a convenient way to access the full range of
functionality offered by the Atlassian REST APIs.}

%description %_description

%package     -n python3-%{projname}
Summary:        %{summary}

%description -n python3-%{projname} %_description

%prep
%autosetup -n %{srcname}-%{version}

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
%pyproject_check_import
%endif

%files -n python3-%{projname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
