%global desc cloudpickle makes it possible to serialize Python constructs \
not supported by the default pickle module from the Python standard \
library. cloudpickle is especially useful for cluster computing where \
Python expressions are shipped over the network to execute on remote \
hosts, possibly close to the data. Among other things, cloudpickle \
supports pickling for lambda expressions, functions and classes defined \
interactively in the __main__ module.

Name:           python-cloudpickle
Version:        3.1.1
Release:        %autorelease
Summary:        Extended pickling support for Python objects

License:        BSD-3-Clause
URL:            https://github.com/cloudpipe/cloudpickle
Source0:        %{url}/archive/v%{version}/cloudpickle-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# Test requirements
BuildRequires:  python3-pytest
BuildRequires:  python3-psutil
BuildRequires:  python3-tornado

%description
%{desc}

%package -n     python3-cloudpickle
Summary:        %{summary}
%{?python_provide:%python_provide python3-cloudpickle}

%description -n python3-cloudpickle
%{desc}

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -p1 -n cloudpickle-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cloudpickle

%check
%pytest -v

%files -n python3-cloudpickle -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
