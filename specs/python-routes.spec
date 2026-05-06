Name: python-routes
Version: 2.5.1
Release: %autorelease
Summary: Routing Recognition and Generation Tools

# tests/test_functional/test_recognition.py is BSD, not shipped in main RPM.
License: MIT
URL: https://github.com/bbangert/routes
Source0: https://pypi.io/packages/source/R/Routes/Routes-%{version}.tar.gz

# https://github.com/bbangert/routes/pull/107
Patch0001: 0001-switch-from-nose-to-pytest.patch

BuildArch: noarch

BuildRequires: python3-devel
# For tests
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(webtest)
BuildRequires: python3dist(webob)


%global _description %{expand:
Routes is a Python re-implementation of the Rails routes system for mapping
URL's to Controllers/Actions and generating URL's. Routes makes it easy to
create pretty and concise URLs that are RESTful with little effort.}


%description %_description


%package -n python3-routes
Summary: %{summary}


%description -n python3-routes %_description


%prep
%autosetup -p1 -n Routes-%{version}


%build
%pyproject_wheel


%generate_buildrequires
%pyproject_buildrequires


%install
%pyproject_install

%pyproject_save_files -l routes


%check
PYTHONPATH=$(pwd) python3 -m pytest


%files -n python3-routes -f %{pyproject_files}
#%%license LICENSE.txt
%doc README.rst CHANGELOG.rst docs



%changelog
%autochangelog
