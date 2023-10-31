%global pypi_name red-black-tree-mod

Name:           python-%{pypi_name}
Version:        1.21
Release:        %{autorelease}
Summary:        Flexible python implementation of red black trees

License:        MIT
URL:            http://stromberg.dnsalias.org/~strombrg/red-black-tree-mod/
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A pair of python modules implementing red black trees is provided.

Red-black trees are a little slower than treaps (some question this),
but they give a nice low standard deviation in operation times, and
this code is rather flexible.

A module is provided for red black trees that enforce uniqueness. They
allow for set-like use and dictionary-like use.

This code is known to work on CPython 2.x, CPython 3.x, Pypy and Jython.

Much of the work here was done by Duncan G. Smith. Dan just put some
finishing touches on it.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'red_black*'


%check
# All tests passed :)
%{py3_test_envvars} %{python3} test-red_black_tree_mod
# Run the import test in addition since above test has no output
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README


%changelog
%autochangelog
