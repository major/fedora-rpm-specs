%global srcname ijson

Name:           python-%{srcname}
Version:        3.5.1
Release:        %autorelease
Summary:        Iterative JSON parser

License:        BSD-3-Clause AND ISC
URL:            https://github.com/ICRAR/ijson
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Iterative JSON parser with standard Python iterator interfaces.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     yajl
Recommends:     python3dist(cffi)

# Test dependencies
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

# Disable tests for unsupported configurations.
sed -i "s/\['python', 'yajl', 'yajl2', 'yajl2_cffi', 'yajl2_c']/\['python', 'yajl2', 'yajl2_cffi']/" tests/test_base.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import -e "ijson.backends.yajl*"
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
