# All of the tests require either docker, network access, or both.
%bcond_with  tests

%global         reponame    azure-sdk-for-python
%global         srcname     azure-servicebus

Name:           python-%{srcname}
Version:        7.11.1
Release:        %autorelease
Summary:        Microsoft Azure Service Bus Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        %{url}/archive/%{srcname}_%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch


BuildRequires:  python3-devel

# For import checks.
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(certifi)

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-identity)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-mgmt-servicebus)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Service Bus Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
# Upstream buries the package into a subdirectory. 😭
%setup -c -T
tar xzf %{SOURCE0} --strip-components=4 \
    %{reponame}-%{srcname}_%{version}/sdk/servicebus/%{srcname}
ls -alR


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md migration_guide.md README.md samples


%changelog
%autochangelog
