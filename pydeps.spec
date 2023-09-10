%global pypi_name pydeps

%global desc %{expand: \
Python module dependency visualization. This package installs the pydeps
command, and normal usage will be to use it from the command line.}

%bcond_without tests
%bcond_without docs

%global forgeurl https://github.com/thebjorn/pydeps

Name:		%{pypi_name}
Version:	1.12.17
Release:	%autorelease
Summary:	Display module dependencies
License:	BSD-2-Clause
%forgemeta
URL:		%forgeurl
Source0:	%forgesource
BuildArch:	noarch

%{?python_enable_dependency_generator}

BuildRequires:	python3-devel
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3dist(pyyaml)
BuildRequires:	graphviz
%endif
%if %{with docs}
BuildRequires:	make
BuildRequires:	python3-sphinx
%endif

%description
%{desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Generate man pages and docs
pushd docs
make %{?_smp_mflags} man html
popd

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# Install man page and html docs
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a docs/_build/man/*.1 %{buildroot}/%{_mandir}/man1
rm docs/_build/html/.buildinfo


%check
%pyproject_check_import
%if %{with tests}
  # Exclude failing tests:
  # https://github.com/thebjorn/pydeps/issues/71
  %pytest -k "not (test_file or test_relative_imports_same_name_with_std \
  or test_pydeps_colors or test_find_package_names)"
%endif

%files -n %{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/pydeps
%if %{with docs}
%{_mandir}/man1/%{pypi_name}.1*
%doc docs/_build/html
%endif

%changelog
%autochangelog
