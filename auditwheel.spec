Name:           auditwheel
Version:        5.4.0
Release:        2%{?dist}
Summary:        Cross-distribution Linux wheels auditing and relabeling

License:        MIT
URL:            https://github.com/pypa/auditwheel
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

# For tests and runtime
BuildRequires:  patchelf >= 0.9
Requires:       patchelf >= 0.9

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
%pyproject_save_files auditwheel


%check
# Upstream uses nox, so we invoke pytest directly
# Integration tests need docker manylinux images, so we only run unit
%pytest -v tests/unit

# Sanity check for the command line tool
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{buildroot}%{_bindir}/auditwheel --help
%{buildroot}%{_bindir}/auditwheel lddtree %{python3}

# Assert the bundled wheel version, assumes $PYTHONPATH already exported
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
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 29 2023 Charalampos Stratakis <cstratak@redhat.com> - 5.4.0-1
- Update to 5.4.0
Resolves: rhbz#2192317

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 5.3.0-3
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-1
- Update to 5.3.0
- Fixes: rhbz#2136978

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.1.2-3
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Miro Hrončok <mhroncok@redhat.com> - 5.1.2-1
- Update to 5.1.2
- Fixes: files are not compressed with ZIP_DEFLATED
- Fixes: rhbz#2038537

* Mon Jan 03 2022 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-1
- Update to 5.1.1
- Fixes: rhbz#2036781

* Mon Sep 20 2021 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-1
- Update to 5.0.0
- Fixes: rhbz#2005582

* Fri Aug 13 2021 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-1
- Initial package
- Fixes: rhbz#1993535
