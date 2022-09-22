%global pypi_name anyjson
%global sum Wraps the best available JSON implementation

Name:           python-%{pypi_name}
Version:        0.3.3
Release:        %autorelease
Summary:        %{sum}

License:        BSD
URL:            http://pypi.python.org/pypi/anyjson
Source0:	%{pypi_source}

# Fix Python 3 compatibility
Patch0:         anyjson-python3.patch
# Include cjson, raise priority of cjson and drop the 'deprecation'
# warning (it's about as alive as half the others), drop jsonlib,
# jsonlib2 and django.utils.simplejson (which all appear to be dead
# as doornails)
Patch1:         python-anyjson-update-order.patch
Patch2:		do-not-use-2to3.patch

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-nose
BuildRequires:	python3-pytest
BuildRequires:	python3-six
BuildRequires:	pyproject-rpm-macros
%py_provides python3-%{pypi_name}

%description
Anyjson loads whichever is the fastest JSON module installed and
provides a uniform API regardless of which JSON implementation is used.

%package -n python3-%{pypi_name}
Summary:        %{sum}

%description -n python3-%{pypi_name}
Anyjson loads whichever is the fastest JSON module installed and
provides a uniform API regardless of which JSON implementation is used.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v
 
%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG README
%license LICENSE

%changelog
%autochangelog
