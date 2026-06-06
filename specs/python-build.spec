# uv has many build dependencies which are not included in RHEL;
# virtualenv is not included in RHEL
%bcond extras %{undefined rhel}
# not all test dependencies are included in RHEL: filelock, pytest-mock
# test dependencies also drag in extra dependencies, so if we want a build without
# extras, we can't run tests either
%bcond tests %[%{undefined rhel} && %{with extras}]

Name:           python-build
Version:        1.5.0
Release:        %autorelease
Summary:        A simple, correct PEP517 package builder

License:        MIT
URL:            https://github.com/pypa/build
Source:         %{pypi_source build}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros >= 0-41

%description
A simple, correct PEP517 package builder.


%package -n     python3-build
Summary:        %{summary}

%description -n python3-build
A simple, correct PEP517 package builder.


# Even --without extras, we still build the extras in ELN
# to make it available in ELN Extras (e.g. tox).
# Note that due to technical limitations,
# we must *not* generate their runtime deps as BuildRequires
# or else they are pulled into ELN proper (not ELN Extras).
# https://github.com/fedora-eln/eln/issues/309
%if %{with extras} || %{defined eln}
%pyproject_extras_subpkg -n python3-build virtualenv uv
%endif


%prep
%autosetup -p1 -n build-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency pytest-cov:ignore
%pyproject_patch_dependency covdefaults:ignore


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g test} %{?with_extras:-x virtualenv,uv}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l build

%check
%pyproject_check_import
%if %{with tests}
# Upstream has integration tests that can be run with the --run-integration
# flag, but currently that only includes one network test and one test that is
# xfail when flit-core is installed (which it will be during our package
# build), so including that flag doesn't run any additional tests.
%pytest -v -m "not network"
%endif

%files -n python3-build -f %{pyproject_files}
%doc README.md
%{_bindir}/pyproject-build

%changelog
%autochangelog
