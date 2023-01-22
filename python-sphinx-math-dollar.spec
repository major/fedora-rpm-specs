Name:           python-sphinx-math-dollar
Version:        1.2.1
Release:        4%{?dist}
Summary:        Sphinx extension to enable LaTeX math with $$

License:        MIT
URL:            https://www.sympy.org/sphinx-math-dollar/
Source0:        https://github.com/sympy/sphinx-math-dollar/archive/%{version}/sphinx-math-dollar-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pytest-doctestplus}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist wheel}

%global _desc %{expand:
sphinx-math-dollar is a Sphinx extension to let you write LaTeX math
using $$.}

%description %_desc

%package     -n python3-sphinx-math-dollar
Summary:        Sphinx extension to enable LaTeX math with $$

%description -n python3-sphinx-math-dollar %_desc

%package        doc
# The content is MIT.  Other licenses are due to files copied in by Sphinx.
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
License:        MIT AND BSD-2-Clause AND BSD-3-Clause
Summary:        Documentation for sphinx-math-dollar

%description    doc
Documentation for sphinx-math-dollar.

%prep
%autosetup -n sphinx-math-dollar-%{version} -p1

%build
%pyproject_wheel

# Build the documentation
make -C docs html
rst2html --no-datestamp CHANGELOG.rst CHANGELOG.html
rst2html --no-datestamp README.rst README.html
rm -f docs/_build/html/.{buildinfo,nojekyll}

%install
%pyproject_install
%pyproject_save_files sphinx_math_dollar

%check
%pytest

%files -n python3-sphinx-math-dollar -f %{pyproject_files}
%doc CHANGELOG.html README.html

%files doc
%doc docs/_build/html
%license LICENSE

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 1.2.1-3
- Convert License tags to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.11

* Mon Apr 25 2022 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- Version 1.2.1
- Drop all patches

* Thu Feb 17 2022 Miro Hrončok <mhroncok@redhat.com> - 1.2-7
- Drop the dependency on upstream dead sphinx-testing, use sphinx.testing instead

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Jerry James <loganjerry@gmail.com> - 1.2-5
- Add -versioneer patch to fix FTBFS with python 3.11
- Update python macros

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Jerry James <loganjerry@gmail.com> - 1.2-1
- Version 1.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  2 2020 Jerry James <loganjerry@gmail.com> - 1.1.1-1
- Initial RPM
