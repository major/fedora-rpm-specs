%global pypi_name djangorestframework

# Some test dependencies are missing
%bcond_with tests
Name:           python-django-rest-framework
Version:        3.16.0
Release:        %autorelease
Summary:        Web APIs for Django, made easy

License:        BSD-3-Clause
URL:            http://www.django-rest-framework.org
Source:         https://github.com/encode/django-rest-framework/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Django REST framework is a powerful and flexible toolkit that makes it easy
to build Web APIs.

Some reasons you might want to use REST framework:

* The Web browsable API is a huge usability win for your developers.
* Authentication policies including OAuth1a and OAuth2 out of the box.
* Serialization that supports both ORM and non-ORM data sources.
* Customizable all the way down - just use regular function-based views if
  you don't need the more powerful features.
* Extensive documentation, and great community support.


%package -n python3-django-rest-framework
Summary:        Web APIs for Django, made easy
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-django-rest-framework
Django REST framework is a powerful and flexible toolkit that makes it easy
to build Web APIs.

Some reasons you might want to use REST framework:

* The Web browsable API is a huge usability win for your developers.
* Authentication policies including OAuth1a and OAuth2 out of the box.
* Serialization that supports both ORM and non-ORM data sources.
* Customizable all the way down - just use regular function-based views if
  you don't need the more powerful features.
* Extensive documentation, and great community support.


%prep
%autosetup -n django-rest-framework-%{version}

echo "recursive-include rest_framework/locale *.mo" >> MANIFEST.in

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove .po files
find . -name *.po -exec rm -f '{}' \;


%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l rest_framework

%find_lang django


%check
%if %{with tests}
%tox
%endif


%files -n python3-django-rest-framework -f %{pyproject_files}
%doc CONTRIBUTING.md README.md SECURITY.md


%changelog
%autochangelog
