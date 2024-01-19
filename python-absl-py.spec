Name:           python-absl-py
Version:        2.1.0
Release:        %autorelease
Summary:        Abseil Python Common Libraries

License:        Apache-2.0
URL:            https://github.com/abseil/abseil-py/
Source:         %{url}/archive/v%{version}/abseil-py-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
This repository is a collection of Python library code for building Python
applications. The code is collected from Google’s own Python code base, and has
been extensively tested and used in production.

Features:

  • Simple application startup
  • Distributed commandline flags system
  • Custom logging module with additional features
  • Testing utilities}

%description %{common_description}


%package -n     python3-absl-py
Summary:        %{summary}

%py_provides python3-absl

%description -n python3-absl-py %{common_description}


%prep
%autosetup -n abseil-py-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l absl


%check
# Since we cannot run the full upstream test suite (see comments below), we
# start with an import “smoke test”:
%pyproject_check_import

# Upstream provides some “smoke tests” that we can run, too. We cannot use the
# wrapper smoke_tests/smoke_test.sh because it downloads things from the
# Internet, but we can run the Python scripts manually.
%{py3_test_envvars} %{python3} smoke_tests/sample_app.py --echo smoke 2>&1 |
  grep -F 'echo is smoke.'
%{py3_test_envvars} %{python3} smoke_tests/sample_test.py |
  grep -Fq 'msg_for_test'

# Running the actual test suite requires bazel, which will almost certainly
# never be packaged for Fedora due to its Byzantine mass of bundled
# dependencies. It is possible to invoke the tests with another runner, such as
# pytest, but there are many spurious failures due to the incorrect
# environment, so it is useless to do so.


%files -n python3-absl-py -f %{pyproject_files}
%doc AUTHORS
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%doc smoke_tests


%changelog
%autochangelog
