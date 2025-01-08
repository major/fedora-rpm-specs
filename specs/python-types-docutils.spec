Name:           python-types-docutils
Version:        0.21.0.20241128
Release:        %{autorelease}
Summary:        Typing stubs for docutils


License:        Apache-2.0
URL:            https://pypi.org/pypi/types-docutils
Source:         %{pypi_source types_docutils}

BuildArch:      noarch

%global _description %{expand:
This is a PEP 561 type stub package for the docutils package. It can be
used by type-checking tools like mypy, PyCharm, pytype etc. to check
code that uses docutils.}

%description %_description

%package -n python3-types-docutils
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-types-docutils %_description

%prep
%autosetup -n types_docutils-%{version}

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# see pyproject-rpm-macros documentation for more forms
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l docutils-stubs

%check
%pyproject_check_import docutils-stubs

%files -n python3-types-docutils -f %{pyproject_files}
%doc CHANGELOG.md

%changelog
%autochangelog
