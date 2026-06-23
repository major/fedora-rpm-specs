%global pkg_name itemadapter
%global desc %{expand:
The ItemAdapter class is a wrapper for data container objects,
providing a common interface to handle objects of different
types in an uniform manner, regardless of their underlying implementation.}
Name:		python-itemadapter
Version:	0.13.1
Release:	%autorelease
Summary:	The ItemAdapter class is a wrapper for data container object

License:	BSD-3-Clause
URL:		https://github.com/scrapy/itemadapter
Source0:	%{pypi_source %pkg_name}

BuildArch:	noarch


%description
%{desc}

%package -n python3-%{pkg_name}
Summary:	%{summary}

BuildRequires:	python3-devel


%description -n python3-%{pkg_name}
%{desc}


%prep
%autosetup -n %{pkg_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t -x attrs,pydantic,scrapy

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l itemadapter

%check
%pyproject_check_import
%pytest

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
