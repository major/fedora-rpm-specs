# F35: Do not update past 1.5.0. F35's protobuf is too old.

# tests are enabled by default
%bcond_without  tests

%global         srcname     google-cloud-dataproc-metastore
%global         forgeurl    https://github.com/googleapis/python-dataproc-metastore
Version:        1.6.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python SDK for Google Cloud Dataproc Metastore

License:        ASL 2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description %{expand:
Dataproc Metastore is a fully managed, highly available, autoscaled,
autohealing, OSS-native metastore service that greatly simplifies technical
metadata management. Dataproc Metastore service is based on Apache Hive
metastore and serves as a critical component towards enterprise data lakes.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1

# Replace mock imports with unittest.mock.
grep -rl "^[[:space:]]*import mock" tests | \
    xargs sed -i -E 's/^([[:space:]]*)import mock/\1from unittest import mock/'


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google

# Remove unnecessary scripts.
rm -f %{buildroot}%{_bindir}/fixup*


%if %{with tests}
%check
%pytest --disable-warnings tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.rst SECURITY.md
%{python3_sitelib}/google_cloud_dataproc_metastore-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
