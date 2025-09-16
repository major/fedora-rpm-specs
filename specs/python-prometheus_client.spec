%global srcname prometheus_client

Name:           python-%{srcname}
Version:        0.23.0
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

%description -n python3-%{srcname}
%{summary}.

%pyproject_extras_subpkg -n python3-%{srcname} twisted

%prep
%autosetup -p1 -n client_python-%{version}
sed -i -e '1{/^#!/d}' prometheus_client/__init__.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md MAINTAINERS.md

%changelog
%autochangelog
