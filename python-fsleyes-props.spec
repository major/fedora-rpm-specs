# These are unreliable and often hang
%bcond_with xvfb_tests

%global desc %{expand: \
fsleyes-props is a library which is used by used by FSLeyes , and which allows
you to:

- Listen for change to attributes on a python object,
- Automatically generate wxpython widgets which are bound to attributes of
  a python object
- Automatically generate a command line interface to set values of the
  attributes of a python object.}


Name:           python-fsleyes-props
Version:        1.9.3
Release:        %autorelease
Summary:        [wx]Python event programming framework

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/fsleyes-props
Source0:        %{pypi_source fsleyes-props}

BuildArch:      noarch

%description
%{desc}

%package -n python3-fsleyes-props
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with xvfb_tests}
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  pytest
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-fsleyes-props
%{desc}

%prep
%autosetup -n fsleyes-props-%{version}
rm -rfv fsleyes_props.egg-info

find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;

# Fix requirements files, the auto-dep generator does not like "*".
sed -i 's/fsleyes-widgets.*/fsleyes-widgets>=0.6/' requirements.txt

# disable coverage
sed -i 's/--cov=fsleyes_props//' setup.cfg

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
# Do not use %%pytest: expands to other things
xvfb-run pytest-3 tests --ignore=tests/test_widget_boolean.py --ignore=tests/test_widget_number.py --ignore=tests/test_widget_point.py
%endif


%files -n python3-fsleyes-props -f %{pyproject_files}
%license LICENSE COPYRIGHT
%doc README.rst

%changelog
%autochangelog
