%global srcname empy

Name:           python-empy
Version:        4.2.1
Release:        %autorelease
Summary:        A powerful and robust template system for Python

License:        BSD-3-Clause
URL:            http://www.alcyone.com/software/empy/
Source:         http://www.alcyone.com/software/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
EmPy is a system for embedding Python expressions and statements in template
text; it takes an EmPy source file, processes it, and produces output.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files em emdoc emhelp emlib

%check
%pyproject_check_import
./test.sh -p %{__python3} @suites/python3

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/em.py

%changelog
%autochangelog
