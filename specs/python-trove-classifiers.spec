Name:           python-trove-classifiers
Version:        2026.1.14.14
Release:        %autorelease
Summary:        Canonical source for classifiers on PyPI (pypi.org)

License:        Apache-2.0
URL:            https://github.com/pypa/trove-classifiers
Source:         %{pypi_source trove_classifiers}

# Drop dependency on calver which is not packaged in Fedora.
# This patch is rebased version of upstream PR:
# https://github.com/pypa/trove-classifiers/pull/126/commits/809156bb35852bcaa1c753e0165f1814f2bcedf6
Patch:          Move-to-PEP-621-declarative-metadata.patch

BuildArch:      noarch
BuildRequires:  python3-devel

# Tests require python-iniconfig which requires python-trove-classifiers
# The bcond is needed for new Python bootstrap
%bcond tests 1

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%global _description %{expand:
Canonical source for classifiers on PyPI.
Classifiers categorize projects per PEP 301. Use this package to validate
classifiers in packages for PyPI upload or download.
}

%description %_description

%package -n python3-trove-classifiers
Summary:        %{summary}

%description -n python3-trove-classifiers %_description


%prep
%autosetup -p1 -n trove_classifiers-%{version}
# Replace @@VERSION@@ with %%version
%writevars -f pyproject.toml version

# Make the the CLI tests work in %%check
# https://github.com/pypa/trove-classifiers/issues/219
sed -i 's@{BINDIR}/@@' tests/test_cli.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files trove_classifiers


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-trove-classifiers -f %{pyproject_files}
%doc README.*
%{_bindir}/trove-classifiers


%changelog
%autochangelog
