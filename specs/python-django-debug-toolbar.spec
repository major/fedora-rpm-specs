%global src_name django-debug-toolbar
%global desc %{expand: \
The Django Debug Toolbar is a configurable set of panels that display various
debug information about the current request/response and when clicked, display
more details about the panel's content.}

Name:		python-%{src_name}
Version:	7.1.1
Release:	%autorelease
Summary:	Configurable set of panels that display various debug information

License:	BSD-3-Clause
URL:		https://github.com/django-commons/django-debug-toolbar
Source0:	%{url}/archive/%{version}/%{src_name}-%{version}.tar.gz

Patch0:		python-3.15-cProfile.patch
Patch1:		tests-Ignore-template_partials-in-INSTALLED_APPS.patch

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-jinja2
BuildRequires:	python3-html5lib

%description
%{desc}

%package -n python3-%{src_name}
Summary:        %{summary}
Obsoletes:	python-django-debug-toolbar < 1.9.1-3
Obsoletes:	python2-django-debug-toolbar < 1.9.1-3

%description -n python3-%{src_name} %{desc}

%prep
%autosetup -p1 -n %{src_name}-%{version}

# remove test dependency, django-csp not available in Fedora
rm tests/test_csp_rendering.py

%generate_buildrequires
%pyproject_buildrequires -r
	
%build
%pyproject_wheel
	
%install
%pyproject_install
%pyproject_save_files debug_toolbar

%check
%{python3} -m django test -v 2 --settings tests.settings tests

%files -n python3-%{src_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
