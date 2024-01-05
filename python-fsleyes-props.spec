# These may be disabled if they become unreliable
%bcond xvfb_tests 1

%global desc %{expand:
fsleyes-props is a library which is used by FSLeyes, and which allows you to:

- Listen for change to attributes on a python object,
- Automatically generate wxpython widgets which are bound to attributes of a
  python object
- Automatically generate a command line interface to set values of the
  attributes of a python object.}

Name:           python-fsleyes-props
Version:        1.11.0
Release:        %autorelease
Summary:        [wx]Python event programming framework

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/fsleyes-props
Source:         %{pypi_source fsleyes-props}

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description %{desc}


%package -n python3-fsleyes-props
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with xvfb_tests}
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  %{py3_dist pytest}
%endif


%description -n python3-fsleyes-props %{desc}


%prep
%autosetup -n fsleyes-props-%{version}

find fsleyes_props -name '*.py' -exec sed -r -i '1{/^#!/d}' '{}' '+'

# disable coverage
sed -i 's/--cov=fsleyes_props//' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fsleyes_props


%check
%if %{with xvfb_tests}
# These tests fail. Upstream says tests are not reliable, but work on his Ubuntu setup.
ignore="${ignore-} --ignore=tests/test_widget_boolean.py"
ignore="${ignore-} --ignore=tests/test_widget_number.py"
ignore="${ignore-} --ignore=tests/test_widget_point.py"

%global __pytest xvfb-run -a pytest
%pytest -v ${ignore-}
%endif


%files -n python3-fsleyes-props -f %{pyproject_files}
# The .dist-info directory contains LICENSE but not COPYRIGHT, so manual
# handling is still required:
%license LICENSE COPYRIGHT
%doc CHANGELOG.rst
%doc README.rst

%changelog
%autochangelog
