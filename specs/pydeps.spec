%global pypi_name pydeps

%global desc %{expand: \
Python module dependency visualization. This package installs the pydeps
command, and normal usage will be to use it from the command line.}

%bcond tests 1
%bcond html_docs 0

%global forgeurl https://github.com/thebjorn/pydeps

Name:       %{pypi_name}
Version:    3.0.1
Release:    %autorelease
Summary:    Display module dependencies
License:    BSD-2-Clause
%forgemeta
URL:        %forgeurl
Source0:    %forgesource
BuildArch:  noarch

%{?python_enable_dependency_generator}

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3dist(pyyaml)
BuildRequires:  graphviz
%endif
BuildRequires:  make
BuildRequires:  python3-sphinx

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
make %{?_smp_mflags} man

%if %{with html_docs}
make %{?_smp_mflags} html
%endif
popd


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

# Install man page and html docs
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a docs/_build/man/*.1 %{buildroot}/%{_mandir}/man1
%if %{with html_docs}
rm docs/_build/html/.buildinfo
%endif


%check
%pyproject_check_import
%if %{with tests}
  %pytest -v
%endif

%files -n %{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/pydeps
%{_mandir}/man1/%{pypi_name}.1*
%if %{with html_docs}
%doc docs/_build/html
%endif

%changelog
%autochangelog
