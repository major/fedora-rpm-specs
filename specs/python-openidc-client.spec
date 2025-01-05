%global commit      0e2ed814497fd850a76c875123a0b0cdfd12ee70
%global shortcommit %{sub %{commit} 1 7}

Name:           python-openidc-client
Version:        0.6.0^1.%{shortcommit}
Release:        %autorelease
Summary:        Python OpenID Connect client with token caching and management

License:        MIT
URL:            https://github.com/puiterwijk/python-openidc-client
Source:         %{url}/archive/%{commit}/python-openidc-client-%{shortcommit}.tar.gz
# https://github.com/puiterwijk/python-openidc-client/pull/10
# Fully fix support for server not sending refresh token
Patch:          0001-feat-really-support-not-receiving-refresh-token.patch

BuildArch:      noarch


%description
%{summary}.


%package     -n python3-openidc-client
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-openidc-client
%{summary}.


%prep
%autosetup -p 1 -n python-openidc-client-%{commit}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l openidc_client


%check
%{py3_test_envvars} %{python3} -m unittest -v tests.test_openidcclient


%files -n python3-openidc-client -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
