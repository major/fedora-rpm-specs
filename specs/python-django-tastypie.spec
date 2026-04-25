%global pypi_name django-tastypie

%global _description %{expand:
Tastypie is an webservice API framework for Django. It provides a convenient, 
yet powerful and highly customizable, abstraction for creating REST-style 
interfaces.}

Name:           python-%{pypi_name}
Version:        0.15.1
Release:        %autorelease
Summary:        A flexible and capable API layer for Django   

License:        BSD-3-Clause
URL:            https://github.com/toastdriven/django-tastypie/

# Release version doesn't include tests
Source0:        https://github.com/%{pypi_name}/%{pypi_name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name} %_description


%prep 
%autosetup -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l tastypie


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst AUTHORS
%license LICENSE


%changelog
%autochangelog
