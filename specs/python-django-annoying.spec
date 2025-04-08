%global pypi_name django-annoying

Name:        python-%{pypi_name}
Version:     0.10.8
%global forgeurl https://github.com/skorokithakis/django-annoying
%forgemeta
Release:     %autorelease
License:     BSD-3-Clause
Summary:     Eliminate annoying things in the Django framework
Summary(sv): Eliminera irriterande saker i Django-ramverket
URL:         %forgeurl
Source:      %forgesource

BuildArch:   noarch

%description
Django-annoying is a django application that tries to
eliminate annoying things in the Django framework.

%description -l sv
Django-annoying är ett django-program so försöker
eliminera irriterande saker i Django-ramverket.

%package -n python3-%{pypi_name}
Summary:        Annoying things elimination in the Django framework
%py_provides    python3-annoying

Obsoletes:      python2-%{pypi_name} < 0.9.0-5
Obsoletes:      python-%{pypi_name} < 0.9.0-5

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Django-annoying is a django application that tries to
eliminate annoying things in the Django framework.
This package provides Python 3 build of %{pypi_name}.

%description -l sv -n python3-%{pypi_name}
Django-annoying är ett django-program so försöker
eliminera irriterande saker i Django-ramverket.
Detta paket tillhandahåller ett Python 3-bygge av %{pypi_name}.

%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc AUTHORS.txt README.md
%license LICENSE.txt
%{python3_sitelib}/annoying/
%{python3_sitelib}/django_annoying-%{version}.dist-info/

%changelog
%autochangelog
