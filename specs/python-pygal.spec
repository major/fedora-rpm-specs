
%global modname pygal

Name:               python-pygal
Version:            3.1.0
Release:            %autorelease
Summary:            A python svg graph plotting library

License:            LGPL-3.0-or-later
URL:                https://pypi.io/project/pygal
Source0:            https://pypi.io/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
# Test requirements
BuildRequires:      python3-pytest
BuildRequires:      python3-pyquery

%global _description\
A python svg graph plotting library.

%description %_description

%package -n python3-pygal
Summary:            A python svg graph plotting library

Requires:           python3-lxml

%description -n python3-pygal
A python svg graph plotting library

%prep
%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pygal

%check
%pytest


%files -n python3-pygal -f %{pyproject_files}
%doc README.md
%{_bindir}/pygal_gen.py

%changelog
%autochangelog
