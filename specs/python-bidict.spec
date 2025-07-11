Name:           python-bidict
Version:        0.23.1
Release:        %autorelease
Summary:        Bidirectional mapping library for Python

License:        MPL-2.0
URL:            https://bidict.readthedocs.io
Source:         https://github.com/jab/bidict/archive/v%{version}/bidict-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l bidict

BuildArch:      noarch

# In 0.23.1, test dependencies are in dev-deps/test.in. Later, they are moved
# to a test dependency group in pyproject.toml. In either case, we must curate
# them: we don’t want benchmarks, coverage analysis, linters, etc, and
# pytest-sphinx, while perhaps potentially useful, is not packaged. See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist hypothesis}
BuildRequires:  %{py3_dist pytest-xdist}
BuildRequires:  %{py3_dist typing-extensions}
# Used for only one doctest!
BuildRequires:  %{py3_dist sortedcollections}
# The sortedcontainers dependency is mentioned in documentation, but does not
# appear in a doctest that we actually run.

%global common_description %{expand:
The bidirectional mapping library for Python.}

%description %{common_description}


%package -n     python3-bidict
Summary:        %{summary}

%description -n python3-bidict %{common_description}


%prep -a
# Since we have patched out pytest-benchmark, this would not be recognized.
sed -r -i '/--benchmark/d' pytest.ini


%check -a
%pytest


%files -n python3-bidict -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
