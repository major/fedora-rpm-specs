# F35: Do not update past 1.3.1. F35's protobuf is too old.

# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-private-ca
%global         forgeurl    https://github.com/googleapis/python-security-private-ca
Version:        1.4.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud Certificate Authority Service

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
Python Client for Google Cloud Certificate Authority Service}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup

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

# Remove unneeded directories and files from the final package.
rm -f %{buildroot}%{_bindir}/fixup_privateca_v1beta1_keywords.py
rm -rf %{buildroot}%{python3_sitelib}/{docs,samples,scripts,tests}


%if %{with tests}
%check
# Work around an unusual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest --disable-warnings tests/unit
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md samples
%{python3_sitelib}/google_cloud_private_ca-%{version}-py%{python3_version}-nspkg.pth



%changelog
%autochangelog
