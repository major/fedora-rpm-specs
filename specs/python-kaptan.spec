%global srcname kaptan

Name:           python-%{srcname}
Version:        0.6.0
Release:        %autorelease
Summary:        Configuration parser

# Automatically converted from old format: BSD - review is highly recommended.
License:        BSD-3-Clause
URL:            https://github.com/emre/kaptan
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch0:         python-kaptan-importlib.patch
BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-yaml

%description -n python3-%{srcname}
%{summary}.

%prep
%autosetup -n %{srcname}-%{version} -p1
sed -i -e 's/PyYAML>=3.13,<6/PyYAML/' requirements/base.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest -v tests

# A man page has been requested upstream here:
# https://github.com/emre/kaptan/issues/44
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/%{srcname}

%changelog
%autochangelog
