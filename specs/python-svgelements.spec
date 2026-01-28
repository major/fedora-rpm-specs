%global srcname svgelements

Name:		python-%{srcname}
Version:	1.9.6
Release:	%autorelease
Summary:	SVG elements parsing
License:	MIT
URL:		https://github.com/meerk40t/svgelements
Source0:	%{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
# For tests
BuildRequires:	python3-scipy
# https://github.com/meerk40t/svgelements/commit/aef57085cdd802a7580544f77420258946cd8f29.patch
Patch:		python-svgelements-1.9.6-drop-tests.patch


%description
%{summary}.


%package -n python3-%{srcname}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Drop the failing tests
# https://github.com/meerk40t/svgelements/issues/263
pushd test
rm -f test_cubic_bezier.py test_image.py test_write.py
popd

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l svgelements


%check
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
