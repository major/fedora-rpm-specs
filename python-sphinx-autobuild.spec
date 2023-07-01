%global _docdir_fmt %{name}

Name:           python-sphinx-autobuild
Version:        2021.3.14
Release:        5%{?dist}
Summary:        Autobuild a Sphinx directory when a change is detected

License:        MIT
URL:            https://github.com/executablebooks/sphinx-autobuild
Source0:        %{pypi_source sphinx-autobuild}

BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  python3-devel

%description
Rebuild Sphinx documentation on changes, with live-reload in the browser.

%package     -n python3-sphinx-autobuild
Summary:        Autobuild a Sphinx directory when a change is detected

%description -n python3-sphinx-autobuild
Rebuild Sphinx documentation on changes, with live-reload in the browser.

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
Summary:        Documentation for sphinx-autobuild
Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

%description    doc
Documentation for sphinx-autobuild.

%prep
%autosetup -n sphinx-autobuild-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel
rst2html --no-datestamp NEWS.rst NEWS.html

# Build the documentation
mkdir html
sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}

%install
%pyproject_install
%pyproject_save_files sphinx_autobuild

# Install a man page
export PYTHONPATH=%{buildroot}%{python3_sitelib}
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N %{buildroot}%{_bindir}/sphinx-autobuild > \
  %{buildroot}%{_mandir}/man1/sphinx-autobuild.1

%check
%pytest

%files -n python3-sphinx-autobuild -f %{pyproject_files}
%doc AUTHORS NEWS.html README.md
%license LICENSE
%{_bindir}/sphinx-autobuild
%{_mandir}/man1/sphinx-autobuild.1*

%files doc
%doc html

%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2021.3.14-5
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 2021.3.14-4
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 2021.3.14-3
- Convert License tags to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2021.3.14-2
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Jerry James <loganjerry@gmail.com> - 2021.3.14
- Bring back to Fedora

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Sundeep Anand <suanand@redhat.com> - 0.7.1-13
- bump version

* Wed Mar 13 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 0.7.1-12
- Remove python2-sphinx-autobuild without condition, missing run-time requirements

* Tue Mar 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-11
- Remove python2-sphinx-autobuild on Fedora 31

* Fri Mar  1 2019 Nick Cross <ncross@redhat.com> - 0.7.1-10
- Correct dependencies. Patch port-for to unpin it.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl>
- Fix creation of python2- subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Sundeep Anand <suanand@redhat.com> - 0.7.1-1
- Updated to version 0.7.1

* Wed Aug 10 2016 Sundeep Anand <suanand@redhat.com> - 0.6.0-3
- https://bugzilla.redhat.com/show_bug.cgi?id=1365796

* Thu Jun 23 2016 Sundeep Anand <suanand@redhat.com> - 0.6.0-2
- fix: epel py3 dependency

* Mon Jun 20 2016 Sundeep Anand <suanand@redhat.com> - 0.6.0-1
- https://bugzilla.redhat.com/show_bug.cgi?id=1348003

* Tue Feb 16 2016 Sundeep Anand <suanand@redhat.com> - 0.5.2-4
- https://bugzilla.redhat.com/show_bug.cgi?id=1307172

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Sundeep Anand <suanand@redhat.com> - 0.5.2-2
- Fix binary shebang in python3 subpackage

* Fri Jan 22 2016 Sundeep Anand <suanand@redhat.com> - 0.5.2-1
- Initial RPM Package
