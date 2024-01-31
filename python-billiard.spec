%global srcname billiard
%bcond_without tests

Name:           python-%{srcname}
Version:        4.2.0
Release:        %autorelease
Epoch:          1
Summary:        A multiprocessing pool extensions

License:        BSD
URL:            https://github.com/celery/billiard
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This package contains extensions to the multiprocessing pool.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-case
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
%endif

%description -n python3-%{srcname}
This package contains extensions to the multiprocessing pool.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%pytest
%endif

%files -n python3-%{srcname}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
