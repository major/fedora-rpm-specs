%global pypi_name puremagic

Name:           python-%{pypi_name}
Version:        1.30
Release:        %autorelease
Summary:        Pure python implementation of magic file detection

%global forgeurl https://github.com/cdgriffith/puremagic
%global tag %{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Pure Python module that will identify a file based on its magic numbers.

It does NOT try to match files on non-magic string. In other words it
will not search for a string within a certain window of bytes like
others might.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

# Remove unnecessary shebangs
sed -r \
    -e '/^#!/d' \
    -i puremagic/__init__.py puremagic/__main__.py puremagic/main.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pytest -r fEs
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.md README.rst


%changelog
%autochangelog
