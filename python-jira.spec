Name:               python-jira
Version:            3.8.0
Release:            %autorelease
Summary:            Python library for interacting with JIRA via REST APIs

License:            BSD-2-Clause
URL:                https://pypi.io/project/jira
Source0:            https://github.com/pycontribs/jira/archive/%{version}/jira-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-keyring
BuildRequires:      python3-pytest
BuildRequires:      python3-requests-mock

%global _description %{expand:
Python library for interacting with JIRA via REST APIs
}
%description %_description

%package -n python3-jira
Summary:        %{summary}

%description -n python3-jira %_description


%package -n jirashell
Requires: python3-ipython
Requires: python3-keyring
Requires: python3-jira == %{version}
Summary: Interactive Jira shell
%description -n jirashell
Interactive Jira shell using jira Python library.


%prep
%autosetup -p1 -n jira-%{version}

sed -i "s/--cov-report=xml --cov jira//" pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -r

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
rm -r %{buildroot}/%{python3_sitelib}/tests
%pyproject_save_files jira

# clone file list to split off jirashell things (will be part of jirashell.rpm)
grep -v -w 'jirashell' "%{pyproject_files}" >python3-jira.files
grep    -w 'jirashell' "%{pyproject_files}" >jirashell.files


%check
# Subset of tests we can run
# The rest of skipped tests need internet connection or running Jira instance as well.
%pytest tests/resources/test_customer.py tests/resources/test_generic_resource.py \
        tests/resources/test_issue_link_type.py tests/resources/test_request_type.py \
        tests/resources/test_role.py tests/test_client.py tests/test_exceptions.py \
        tests/test_resilientsession.py tests/test_qsh.py tests/test_shell.py \
        -k "not test_delete_project and \
            not test_delete_inexistent_project and \
            not test_templates and \
            not test_token_auth and \
            not test_cookie_auth and \
            not test_cookie_auth_retry and \
            not test_createmeta_issuetypes_pagination and \
            not test_createmeta_fieldtypes_pagination"

%files -n python3-jira -f python3-jira.files
%doc README.rst
%license LICENSE

%files -n jirashell -f jirashell.files
%{_bindir}/jirashell


%changelog
%autochangelog
