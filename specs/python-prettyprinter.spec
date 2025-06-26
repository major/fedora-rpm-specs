Name:           python-prettyprinter
Version:        0.18.0
Release:        %autorelease
Summary:        Syntax-highlighting, declarative and composable pretty printer
License:        MIT
URL:            https://github.com/tommikaikkonen/prettyprinter
BuildArch:      noarch
Source:         %{pypi_source prettyprinter}
# downstream-only patch
Patch:          0001-Avoid-build-requirement-on-pytest-runner.patch

%global _description %{expand:
Syntax-highlighting, declarative and composable pretty printer.  Drop in
replacement for the standard library pprint: just rename pprint to
prettyprinter in your imports.  Uses a modified Wadler-Leijen layout algorithm
for optimal formatting.  Write pretty printers for your own types with a dead
simple, declarative interface.}


%description %_description


%package -n python3-prettyprinter
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-attrs
BuildRequires:  python3-ipython
BuildRequires:  python3-pytz


%description -n python3-prettyprinter %_description


%prep
%autosetup -p 1 -n prettyprinter-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l prettyprinter


%check
# Many tests do not work with current versions of other software.
%pytest \
    --ignore tests/test_django \
    --ignore tests/test_ast.py \
    --ignore tests/test_numpy.py \
    --ignore tests/test_requests.py \
    --verbose


%files -n python3-prettyprinter -f %{pyproject_files}
%doc HISTORY.rst README.rst


%changelog
%autochangelog
