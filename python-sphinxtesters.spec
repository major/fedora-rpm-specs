Name:           python-sphinxtesters
Version:        0.2.3
Release:        15%{?dist}
Summary:        Utilities for testing Sphinx extensions

# The code is BSD-2-Clause.  Other licenses are due to files copied in by
# Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/alabaster.css: BSD-3-Clause
# _static/basic.css: BSD-2-Clause
# _static/custom.css: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/matthew-brett/sphinxtesters
Source0:        https://github.com/matthew-brett/sphinxtesters/archive/%{version}/sphinxtesters-%{version}.tar.gz
# Work around a changing sphinx interface
Patch0:         %{name}-config-error.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist numpydoc}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}

%description
This package contains utilities for testing Sphinx extensions.

%package -n     python3-sphinxtesters
Summary:        Utilities for testing Sphinx extensions
Requires:       %{py3_dist sphinx}

%description -n python3-sphinxtesters
This package contains utilities for testing Sphinx extensions.

%prep
%autosetup -n sphinxtesters-%{version} -p1

%build
%pyproject_wheel
rst2html --no-datestamp README.rst README.html
python3 setup.py build_sphinx
rm -f build/sphinx/html/.{buildinfo,nojekyll}

%install
%pyproject_install
%pyproject_save_files sphinxtesters

%check
%pytest

%files -n python3-sphinxtesters -f %{pyproject_files}
%doc README.html build/sphinx/html

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.2.3-14
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.2.3-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 19 2021 Jerry James <loganjerry@gmail.com> - 0.2.3-11
- Add -config-error patch to fix FTBFS with sphinx 4.2.0
- Modernize the python macros

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.3-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Jerry James <loganjerry@gmail.com> - 0.2.3-4
- Build and ship the documentation
- Ship the README as an html file

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Jerry James <loganjerry@gmail.com> - 0.2.3-1
- New upstream version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Jerry James <loganjerry@gmail.com> - 0.2.1-2
- Drop the python2 subpackage (bz 1653087)

* Wed Aug 29 2018 Jerry James <loganjerry@gmail.com> - 0.2.1-1
- Initial RPM
