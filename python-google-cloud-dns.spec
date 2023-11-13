# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-dns
%global         forgeurl    https://github.com/googleapis/python-dns
Version:        0.34.2
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud DNS

License:        ASL 2.0
URL:            %forgeurl
Source0:        %forgesource
Patch0:         python-google-cloud-dns-mock.patch

BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  python3dist(google-cloud-core)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
The Google Cloud DNS API provides methods that you can use to manage DNS
on Google infrastructure.}

%description %{_description}

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files google

%check
%pyproject_check_import

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md SECURITY.md
%license LICENSE
%{python3_sitelib}/google_cloud_dns-%{version}-py*-nspkg.pth

%changelog
%autochangelog
