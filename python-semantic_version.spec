%global pypi_name semantic_version
%global srcname python-semanticversion

Name:           python-%{pypi_name}
Version:        2.10.0
Release:        %autorelease
Summary:        Library implementing the 'SemVer' scheme

License:        BSD
URL:            https://github.com/rbarrois/python-semanticversion
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  sed

%global _description %{expand:
This small python library provides a few tools to handle semantic versioning in
Python.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}

%package doc
Summary:        Documentation for python-%{pypi_name}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Drop unnecessary dependency
sed -i '/zest\.releaser\[recommended\]/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x doc

%build
%pyproject_wheel

# generate html docs
make -C docs html
# remove the sphinx-build leftovers
rm -rf docs/_build/html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst ChangeLog CREDITS

%files doc
%license LICENSE
%doc docs/_build/html

%changelog
%autochangelog
