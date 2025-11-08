%global srcname empy
%global sum A powerful and robust template system for Python

Name:           python-empy
Version:        4.2
Release:        %autorelease
Summary:        %{sum}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.alcyone.com/software/empy/
Source:         http://www.alcyone.com/software/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
EmPy is a system for embedding Python expressions and statements in template
text; it takes an EmPy source file, processes it, and produces output. 

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
EmPy is a system for embedding Python expressions and statements in template
text; it takes an EmPy source file, processes it, and produces output. 

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

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/em.py

%changelog
%autochangelog
