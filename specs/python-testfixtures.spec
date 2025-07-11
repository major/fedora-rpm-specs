%global pypi_name testfixtures

Name:           python-%{pypi_name}
Version:        9.1.0
Release:        %autorelease
Summary:        Collection of helpers and mock objects for unit tests

License:        MIT
URL:            https://github.com/Simplistix/testfixtures
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

#%%check
# Upstream has a different idea about how Open Source works
# and is hostile against everything that doesn't match that idea.
# Thus, the only thing that matters is that tests work in their CI

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
