%global desc %{expand:
Behavior-driven development (or BDD) is an agile software development technique
that encourages collaboration between developers, QA and non-technical or
business participants in a software project.

behave uses tests written in a natural language style, backed up by Python
code.}

# RHBZ #2179979
%undefine _py3_shebang_s

Name:           python-behave
Version:        1.3.3
Release:        %autorelease
Summary:        Behavior-driven development, Python style

License:        BSD-2-Clause
URL:            https://pypi.org/project/behave
%global forgeurl https://github.com/behave/behave
Source:         %{forgeurl}/archive/v%{version}/behave-%{version}.tar.gz

# Downstream-only: omit pytest options for pytest-html
# (We patch it out in %%prep because we do not need HTML reports.)
Patch:          0001-Downstream-only-omit-pytest-options-for-pytest-html.patch

# CLEANUP: Use "unittest.mock" instead of "mock"
# https://github.com/behave/behave/commit/90e20ba935a440975440edce9eeebe4492c9367b
# Backported to v1.3.3.
Patch:          0001-CLEANUP-Use-unittest.mock-instead-of-mock.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  help2man
BuildRequires:  tomcli

%description %{desc}


%package -n python3-behave
Summary:        %{summary}

# Sphinx-generated HTML documentation has issues with bundled JavaScript, etc.
# (https://bugzilla.redhat.com/show_bug.cgi?id=2006555). While
# https://pagure.io/fesco/issue/3177 and https://pagure.io/fesco/issue/3269
# have improved the situation, it is still troublesome to package correctly,
# and the package is greatly simplified by removing it.
Obsoletes:      python-behave-doc < 1.3.3-1

%description -n python3-behave %{desc}


%prep
%autosetup -n behave-%{version} -p1

# We do not need HTML reports from pytest.
tomcli set pyproject.toml lists delitem \
    project.optional-dependencies.testing 'pytest-\bhtml.*'


%generate_buildrequires
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l behave

mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} help2man \
  --no-info \
  --name="Run a number of feature tests with behave." \
  --output=%{buildroot}%{_mandir}/man1/behave.1 \
  %{buildroot}%{_bindir}/behave


%check
%pytest -v


%files -n python3-behave -f %{pyproject_files}
%doc README.rst
%{_bindir}/behave
%{_mandir}/man1/behave.1*


%changelog
%autochangelog
