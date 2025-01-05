%global srcname constantly

%global common_description %{expand:
A library that provides symbolic constant support. It includes collections and
constants with text, numeric, and bit flag values. Originally
twisted.python.constants from the Twisted project.}

Name:           python-%{srcname}
Version:        23.10.4
Release:        %autorelease
Summary:        Symbolic constants in Python

License:        MIT
URL:            https://github.com/twisted/constantly
Source0:        %url/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx-rtd-theme)

# the tests are enabled by default but can be disabled
# to avoid a circular dependency on twisted->constantly
%if %{with bootstrap}
BuildRequires:  python3dist(twisted)
%endif

Patch:          disable-pip-in-tox.patch


%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{!?_with_bootstrap:-t}

%build
%pyproject_wheel

sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with bootstrap}
%pyproject_check_import
%tox
%else
%py3_check_import %{srcname}
%endif

%files -n python3-%{srcname} -f %{pyproject_files}

%files -n python-%{srcname}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
