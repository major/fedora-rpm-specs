%global pypi_name vulture
%global forgeurl https://github.com/jendrikseipp/vulture
Version:        2.16
%forgemeta

%global common_desc \
Vulture finds unused classes, functions and variables in your code. \
This helps you cleanup and find errors in your programs. If you run it \
on both your library and test suite you can find untested code. \
Due to Python’s dynamic nature, static code analyzers like vulture \
are likely to miss some dead code. Also, code that is only called \
implicitly may be reported as unused. Nonetheless, vulture can be a \
very helpful tool for higher code quality.

Name:           python-%{pypi_name}
Release:        %autorelease
Summary:        Find dead code

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
# Exclude dev directory from being packaged
Patch:          vulture-exclude-dev-packages.patch
BuildArch:      noarch

%description
%{common_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pint)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%description -n python3-%{pypi_name}
%{common_desc}

%prep
%autosetup %{forgesetupargs} -p1
sed -i '1{/^#!/d}' vulture/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import -e 'vulture.whitelists*'
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/%{pypi_name}

%changelog
%autochangelog
