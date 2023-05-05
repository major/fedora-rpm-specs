%global _description %{expand:
This is a PEP 561 type stub package for the docutils package. It can be used by
type-checking tools like mypy, PyCharm, pytype etc.  to check code that uses
docutils. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/docutils. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.}

Name:           python-types-docutils
Version:        0.19.1.8
Release:        %{autorelease}
Summary:        Typing stubs for docutils


License:        Apache-2.0
URL:            https://pypi.org/pypi/types-docutils
Source0:        %{pypi_source types-docutils}
# not included in pypi tar
Source1:        https://github.com/python/typeshed/raw/main/LICENSE

BuildArch:      noarch

%description %_description

%package -n python3-types-docutils
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-types-docutils %_description

%prep
%autosetup -n types-docutils-%{version}
cp %SOURCE1 .

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
%pyproject_save_files docutils-stubs

%check
%pyproject_check_import docutils-stubs

%files -n python3-types-docutils -f %{pyproject_files}
%doc CHANGELOG.md

%changelog
%autochangelog
