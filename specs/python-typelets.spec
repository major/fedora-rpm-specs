Name:           python-typelets
Version:        1.1
Release:        %autorelease
Summary:        Type hints and utility objects for Python and Django projects

License:        MIT
URL:            https://typelets.readthedocs.io/
Source:         %{pypi_source typelets}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)


%global _description %{expand:
Typelets is a Python typing utility module designed to augment
some of the types provided in Python and third-party libraries.}

%description %_description

%package -n     python3-typelets
Summary:        %{summary}

%description -n python3-typelets %_description


%prep
%autosetup -p1 -n typelets-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l typelets


%check
# We skip django import checks, because the upstream project intentionally made
# django parts of typelets optional without specifying runtime dependency.
# And likely just as intentionally did not declare it in extras.
#
# Since the expected consumer, RBTools, does not use and should not require
# django, it's actually beneficial for us to verify that everything else can be
# imported without it.
%pyproject_check_import -e 'typelets.django.*'
%pytest


%files -n python3-typelets -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
