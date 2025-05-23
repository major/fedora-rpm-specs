%global srcname prometheus_client

Name:           python-%{srcname}
Version:        0.21.1
Release:        %autorelease
Summary:        Python client for Prometheus

License:        Apache-2.0
URL:            https://github.com/prometheus/client_python
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch0001:      0001-Remove-the-bundled-decorator-package.patch

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.

%package -n python3-%{srcname}+twisted
Summary:        %{summary}
Requires:       python3-%{srcname} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python%{python3_version}dist(twisted)
BuildRequires:  python3dist(twisted)
%{?python_provide:%python_provide python3-%{srcname}+twisted}

%description -n python3-%{srcname}+twisted
%{summary}.

"twisted" extras.

%prep
%autosetup -p1 -n client_python-%{version}
sed -i -e '1{/^#!/d}' prometheus_client/__init__.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -v

%files -n python3-%{srcname}
%license LICENSE
%doc README.md MAINTAINERS.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%files -n python3-%{srcname}+twisted
%{?python_extras_subpkg:%ghost %{python3_sitelib}/%{srcname}-*.egg-info/}

%changelog
%autochangelog
