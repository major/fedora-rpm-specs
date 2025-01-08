Name:           auditwheel
Version:        6.2.0
Release:        %autorelease
Summary:        Cross-distribution Linux wheels auditing and relabeling

License:        MIT
URL:            https://github.com/pypa/auditwheel
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

# For tests and runtime
BuildRequires:  patchelf >= 0.14
Requires:       patchelf >= 0.14

# From src/auditwheel/_vendor/wheel/__init__.py
# See the rationale in https://github.com/pypa/auditwheel/pull/275
# This is also MIT
%global wheel_version 0.36.2
Provides:       bundled(python3dist(wheel)) = %{wheel_version}

%description
auditwheel is a command-line tool to facilitate the creation of Python wheel
packages for Linux (containing pre-compiled binary extensions)
that are compatible with a wide variety of Linux distributions,
consistent with the PEP 600 manylinux_x_y, PEP 513 manylinux1,
PEP 571 manylinux2010 and PEP 599 manylinux2014 platform tags.

auditwheel show: shows external shared libraries that the wheel depends on
(beyond the libraries included in the manylinux policies),
and checks the extension modules for the use of versioned symbols that exceed
the manylinux ABI.

auditwheel repair: copies these external shared libraries into the wheel
itself, and automatically modifies the appropriate RPATH entries such that
these libraries will be picked up at runtime.
This accomplishes a similar result as if the libraries had been statically
linked without requiring changes to the build system.
Packagers are advised that bundling,
like static linking, may implicate copyright concerns.


%prep
%autosetup -p1
# pypatchelf is patchelf, packaged for pip -- we'll use the native one instead
sed -E -i 's/(, )?"pypatchelf"//' setup.py

# docker is only used for integration testing we don't run
sed -E -i 's/(, )?"docker"//' setup.py


%generate_buildrequires
%pyproject_buildrequires -r -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l auditwheel


%check
# Upstream uses nox, so we invoke pytest directly
# Integration tests need docker manylinux images, so we only run unit
%pytest -v tests/unit

export %{py3_test_envvars}

# Sanity check for the command line tool
%{buildroot}%{_bindir}/auditwheel --help
%{buildroot}%{_bindir}/auditwheel lddtree %{python3}

# Assert the bundled wheel version
test "$(%{python3} -c 'from auditwheel._vendor import wheel; print(wheel.__version__)')" == "%{wheel_version}"

# Assert the policy files are installed
# Regression test for https://github.com/pypa/auditwheel/issues/321
for json in manylinux-policy.json musllinux-policy.json policy-schema.json; do
  test -f %{buildroot}%{python3_sitelib}/auditwheel/policy/${json}
done


%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/auditwheel


%changelog
%autochangelog
