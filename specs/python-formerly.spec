Name:           python-formerly
Version:        0.1.0
Release:        %autorelease
Summary:        Deprecate a class that users inherit from

License:        BSD-3-Clause
URL:            https://github.com/scrapy/formerly
Source:         %{pypi_source formerly}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
formerly renames a class that users inherit from, without breaking them.
It provides a deprecated alias for the old class name that keeps working
for isinstance() and issubclass() checks and for subclassing, while
emitting a deprecation warning when the old name is used.}

%description %_description

%package -n     python3-formerly
Summary:        %{summary}

%description -n python3-formerly %_description


%prep
%autosetup -p1 -n formerly-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l formerly


%check
%pyproject_check_import
# upstream's addopts only adds --doctest-modules, and there are no doctests
%pytest -o addopts="" -v tests


%files -n python3-formerly -f %{pyproject_files}
%doc README.rst CHANGELOG.rst


%changelog
%autochangelog
