# F35: Do not update past 1.6.2. F35's protobuf is too old.

# tests are enabled by default
%bcond_without  tests

%global         srcname     google-cloud-billing-budgets
%global         forgeurl    https://github.com/googleapis/python-billingbudgets
Version:        1.7.2
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python Client for Google Cloud Billing Budget API

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
The Google Cloud Billing Budget API stores Cloud Billing budgets, which define a
budget plan and the rules to execute as spend is tracked against that plan.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1

# Replace mock imports with unittest.mock.
grep -rl "^[[:space:]]*import mock" tests | \
    xargs sed -i -E 's/^([[:space:]]*)import mock/\1from unittest import mock/'

# Allow an older protobuf.
sed -i 's/protobuf >= 3.20.2/protobuf >= 3.19.4/' setup.py

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google

# Remove unnecessary script.
rm -f %{buildroot}%{_bindir}/fixup_budgets*.py


%if %{with tests}
%check
# Work around an usual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest --disable-warnings tests/unit
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_cloud_billing_budgets-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
