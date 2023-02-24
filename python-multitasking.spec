%global         srcname     multitasking

Name:           python-%{srcname}
Version:        0.0.11
Release:        %autorelease
Summary:        Non-blocking Python methods using decorators
License:        Apache-2.0
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
MultiTasking is a tiny Python library lets you convert your Python methods
into asynchronous, non-blocking methods simply by using a decorator.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Remove the python shebang from non-executable files.
sed -i '1{\@^#!/usr/bin/env python@d}' multitasking/__init__.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
