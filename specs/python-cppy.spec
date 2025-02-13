%global srcname cppy

Name:           python-%{srcname}
Version:        1.3.1
Release:        %autorelease
Summary:        C++ headers for C extension development

License:        BSD-3-Clause
URL:            https://github.com/nucleic/cppy
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
A small C++ header library which makes it easier to write Python extension
modules. The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for performing
common object operations.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
A small C++ header library which makes it easier to write Python extension
modules. The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for performing
common object operations.


%package -n python-%{srcname}-doc
Summary:        cppy documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description -n python-%{srcname}-doc
Documentation for cppy


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="$PWD/build/lib" sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files -n python-%{srcname}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
