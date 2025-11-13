# need to debug test failures
%bcond tests 0

Name:           python-terminaltables3
Version:        4.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Generate simple tables in terminals from a nested list of strings. Fork of terminaltables.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/matthewdeanmartin/terminaltables3
# PyPI source does not contain tests
#Source:         %%{pypi_source terminaltables3}
Source:         %{url}/archive/v%{version}/terminaltables3-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'terminaltables3' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-terminaltables3
Summary:        %{summary}

%description -n python3-terminaltables3 %_description


%prep
%autosetup -p1 -n terminaltables3-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L terminaltables3


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-terminaltables3 -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.md


%changelog
%autochangelog
