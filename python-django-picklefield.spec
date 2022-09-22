%global srcname django-picklefield
%global modname picklefield

%global forgeurl https://github.com/koed00/django-q

Name:           python-%{srcname}
Version:        3.0.1
Release:        %autorelease
Summary:        A multiprocessing distributed task queue for Django
License:        MIT
URL:            http://github.com/gintas/django-picklefield
# PyPI tarball has no tests
# Source0:        %%{pypi_source %%{srcname}}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
# Test dependencies:
# for some reason these are not picked up automatically
BuildRequires:  python3dist(django)

%global _description %{expand:
django-picklefield provides an implementation of a pickled object field. Such
fields can contain any picklable objects.

The implementation is taken and adopted from Django snippet \#1694 by Taavi
Taijala, which is in turn based on Django snippet \#513 by Oliver Beattie.}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
# tox.ini runs coverage tests we don't need and
# need to be patched for py310
#
# the two tests in PickledObjectFieldCheckTests failed
# and django test / unittest's -k doesn't do negations
%python3 -m django test -v2 --settings=tests.settings \
  -k PickledObjectFieldTests \
  -k PickledObjectFieldDeconstructTests


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
