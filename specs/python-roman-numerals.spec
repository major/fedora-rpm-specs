Name:           python-roman-numerals
Version:        4.1.0
Release:        %autorelease
Summary:        Manipulate well-formed Roman numerals

# Upstream says: Zero-Clause BSD license or the CC0 1.0 Universal license
# CC0-1.0 is not allowed for Fedora, hence declaring only 0BSD
License:        0BSD
URL:            https://github.com/AA-Turner/roman-numerals/
Source:         %{pypi_source roman_numerals}

BuildArch:      noarch
BuildRequires:  python3-devel
# Upstream defines a `test` extra, but it contains only pytest which is
# needlessly strictly versioned, hence explicit BR:
BuildRequires:  python3-pytest

%global _description %{expand:
This project provides utilities manipulating well-formed Roman numerals,
in various programming languages.}

%description %_description

%package -n     python3-roman-numerals
Summary:        %{summary}

%py_provides    python3-roman-numerals-py
Obsoletes:      python3-roman-numerals-py < 4~~

%description -n python3-roman-numerals %_description


%prep
%autosetup -p1 -n roman_numerals-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L roman_numerals


%check
%pyproject_check_import
%pytest


%files -n python3-roman-numerals -f %{pyproject_files}
%license LICENCE.rst
%doc README.rst


%changelog
%autochangelog
