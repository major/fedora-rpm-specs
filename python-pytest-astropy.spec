%global srcname pytest-astropy
%global modname pytest_astropy
%global sum The py.test astropy plugin

Name:           python-%{srcname}
Version:        0.10.0
Release:        %autorelease
Summary:        %{sum}

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
This package provides a plugin for the pytest framework that is used for
testing Astropy and its affiliated packages. 


%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
This package provides a plugin for the pytest framework that is used for
testing Astropy and its affiliated packages. 


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
