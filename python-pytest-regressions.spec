Name:           python-pytest-regressions
Version:        2.4.2
Release:        4%{?dist}
Summary:        Pytest fixtures for writing regression tests

License:        MIT
BuildArch:      noarch
URL:            https://pytest-regressions.readthedocs.io/
Source0:        https://github.com/ESSS/pytest-regressions/archive/%{version}/pytest-regressions-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}

%global _desc %{expand:
This pytest plugin makes it simple to test general data, images, files,
and numeric tables by saving *expected* data in a *data directory*
(courtesy of pytest-datadir) that can be used to verify that future runs
produce the same data.}

%description %_desc

%package     -n python3-pytest-regressions
Summary:        %{summary}

%description -n python3-pytest-regressions %_desc

%package        doc
# The content is MIT.  Sphinx copies files into the output with these licenses:
# - searchindex.js: BSD-2-Clause
# - _static/basic.css: BSD-2-Clause
# - _static/css/badge_only.css: MIT
# - _static/css/theme.css: MIT
# - _static/doctools.js: BSD-2-Clause
# - _static/documentation_options.js: BSD-2-Clause
# - _static/file.png: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/js/badge_only.js: MIT
# - _static/js/theme.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/minus.png: BSD-2-Clause
# - _static/plus.png: BSD-2-Clause
# - _static/pygments.css: MIT
# - _static/searchtools.js: BSD-2-Clause
# - _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# - _static/underscore*.js: MIT
License:        MIT AND BSD-2-Clause
Summary:        Documentation for %{name}

%description    doc
Documentation for %{name}.

%pyproject_extras_subpkg -n python3-pytest-regressions num,image,dataframe

%prep
%autosetup -n pytest-regressions-%{version}

# Do not attempt to use git to determine the version
sed -e 's/\(version = \).*/\1"%{version}"/' \
    -e 's/\(release = \).*/\1"%{version}"/' \
    -i doc/conf.py
# Remove unnecessary dependencies
sed -e '/"mypy",/d' -e '/"pre-commit",/d' -e '/"restructuredtext-lint",/d' \
    -i setup.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -t -x num,image,dataframe

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

# Build documentation
PYTHONPATH=$PWD/build/lib make -C doc html
rst2html --no-datestamp CHANGELOG.rst CHANGELOG.html
rst2html --no-datestamp README.rst README.html
rm doc/_build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files pytest_regressions

%check
# Adapt the expected ndarray type on s390x
if [ $(uname -m) = s390x ]; then
  sed -i 's/int64/<i8/' tests/test_ndarrays_regression.py
fi
%tox -- -- -Wdefault

%files -n python3-pytest-regressions -f %{pyproject_files}
%doc CHANGELOG.html README.html

%files doc
%doc doc/_build/html

%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2.4.2-4
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 2.4.2-3
- Generate extras subpackages
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Jerry James <loganjerry@gmail.com> - 2.4.2-1
- Version 2.4.2

* Sat Sep 17 2022 Jerry James <loganjerry@gmail.com> - 2.4.1-1
- Version 2.4.1

* Fri Sep 16 2022 Jerry James <loganjerry@gmail.com> - 2.4.0-1
- Version 2.4.0
- Drop obsolete -numexpr patch
- Clarify license of the -doc subpackage
- Fix tests on s390x

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.3.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Version 2.3.1

* Tue Jan  4 2022 Jerry James <loganjerry@gmail.com> - 2.3.0-1
- Version 2.3.0

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- Initial RPM
