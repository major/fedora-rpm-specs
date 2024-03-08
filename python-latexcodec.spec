Name:           python-latexcodec
Version:        3.0.0
Release:        1%{?dist}
Summary:        Lexer and codec to work with LaTeX code in Python

License:        MIT
URL:            https://latexcodec.readthedocs.io/
VCS:            https://github.com/mcmtroffaes/latexcodec/
Source0:        %pypi_source latexcodec
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}

%description
This package contains a lexer and codec to work with LaTeX code in Python.

%package -n python3-latexcodec
Summary:        Lexer and codec to work with LaTeX code in Python

%description -n python3-latexcodec
This package contains a lexer and codec to work with LaTeX code in Python.

%package doc
# The content is MIT.  Other licenses are due to files copied in by Sphinx.
# _static/basic.css: BSD-2-Clause
# _static/classic.css: BSD-2-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sidebar.js: BSD-2-Clause
# _static/sphinx_highlight.js: BSD-2-Clause
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        MIT AND BSD-2-Clause
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup -n latexcodec-%{version}

# Update the sphinx theme name
sed -i 's/default/classic/' doc/conf.py

# Use local objects.inv for intersphinx
sed -i "s|\('http://docs\.python\.org/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" doc/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=$PWD make -C doc html
rm -f doc/_build/html/.buildinfo
rst2html --no-datestamp LICENSE.rst LICENSE.html

%install
%pyproject_install
%pyproject_save_files latexcodec

%check
%pytest

%files -n python3-latexcodec -f %{pyproject_files}

%files doc
%license LICENSE.html
%doc doc/_build/html/*

%changelog
* Wed Mar  6 2024 Jerry James <loganjerry@gmail.com> - 3.0.0-1
- Version 3.0.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.0.1-11
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 2.0.1-10
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 2.0.1-9
- Convert License tags to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 2.0.1-8
- Expand %%srcname for clarity
- Use %%pyproject_save_files

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.1-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.1-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-3
- Fix build with tox 3.19 (by not using it without tox config)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jerry James <loganjerry@gmail.com> - 2.0.1-1
- Version 2.0.1

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Version 2.0.0 (bz 1789613, 1791202)
- Add -doc subpackage
- Use pytest instead of nose
- Use local objects.inv to create documentation links

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May  3 2019 Jerry James <loganjerry@gmail.com> - 1.0.7-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Jerry James <loganjerry@gmail.com> - 1.0.6-1
- New upstream version
- Drop upstreamed -hyphen patch

* Thu Nov 22 2018 Jerry James <loganjerry@gmail.com> - 1.0.5-6
- Drop python2 subpackage (bz 1647376)
- Add -hyphen patch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- New upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-2
- Rebuild for Python 3.6

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- New upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Mar 26 2016 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- New upstream version

* Fri Mar  4 2016 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- New upstream version

* Tue Feb  2 2016 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Initial RPM
