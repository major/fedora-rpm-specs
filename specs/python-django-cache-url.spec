%global pypi_name django-cache-url

Name:           python-%{pypi_name}
Version:        3.4.5
Release:        %autorelease
Summary:        Use Cache URLs in your Django application

License:        MIT
URL:            https://github.com/epicserve/django-cache-url
Source:         %{pypi_source}

BuildArch:      noarch

# for import checks
BuildRequires:  python3dist(django)

%description
This simple Django utility allows you to utilize the 12factor inspired
CACHE_URL environment variable to configure your Django application.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
This simple Django utility allows you to utilize the 12factor inspired
CACHE_URL environment variable to configure your Django application.


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l django_cache_url


%check
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
