%global srcname spur
%global sum Run commands locally or over SSH using the same interface
%global desc Run commands and manipulate files locally or over SSH using the same interface.

Name:           python-%{srcname}
Version:        0.3.23
Release:        %autorelease
Summary:        %{sum}

License:        BSD-2-Clause
URL:            https://github.com/mwilliamson/spur.py
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}.py-%{version}
sed -i -e "s/’/'/g" README.rst

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %srcname

%check
# Exclude tests which require SSH server
%pytest --ignore tests/ssh_tests.py

%files -n python3-%srcname -f %pyproject_files
%doc CHANGES CONTRIBUTING.rst README.rst

%changelog
%autochangelog
