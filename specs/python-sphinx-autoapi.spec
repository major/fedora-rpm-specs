%global srcname sphinx-autoapi
%global srcname_ sphinx_autoapi

Name:           python-%{srcname}
Version:        3.8.0
Release:        %autorelease
Summary:        Sphinx API documentation generator

License:        MIT
URL:            https://github.com/readthedocs/sphinx-autoapi
Source:         %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Sphinx AutoAPI is a Sphinx extension for generating complete API documentation
without needing to load, run, or import the project being documented.

In contrast to the traditional Sphinx autodoc, which requires manual authoring
and uses code imports, AutoAPI finds and generates documentation by parsing
source code.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname_}-%{version} -p1
# These symlinks are lost from the sdist.
# https://github.com/readthedocs/sphinx-autoapi/issues/565
ln -s ../pyexample/example tests/python/pymovedconfpy/example
ln -s ../example_2 tests/toctreeexample/example/example_2

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l autoapi

%check
%{pytest} -m 'not network'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
