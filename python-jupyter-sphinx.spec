Name:           python-jupyter-sphinx
Version:        0.5.3
Release:        1%{?dist}
Summary:        Jupyter Sphinx extensions
License:        BSD-3-Clause
URL:            https://jupyter-sphinx.readthedocs.io/
Source0:        https://github.com/jupyter/jupyter-sphinx/archive/v%{version}/jupyter-sphinx-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel

%global _desc %{expand:
Jupyter-Sphinx enables running code embedded in Sphinx documentation and
embedding output of that code into the resulting document.  It has
support for rich output such as images and even Jupyter interactive
widgets.}

%description %_desc

%package -n python3-jupyter-sphinx
Summary:        %{summary}

%description -n python3-jupyter-sphinx %_desc

%package        doc
# The content is BSD-3-Clause.  Other licenses are due to files copied in by
# Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/alabaster.css: BSD-3-Clause
# _static/basic.css: BSD-2-Clause
# _static/custom.css: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause AND MIT
Summary:        Documentation for %{name}

%description    doc
Documentation for %{name}.

%prep
%autosetup -n jupyter-sphinx-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x doc,test

%build
%pyproject_wheel

# Build the documentation
PYTHONPATH=$PWD make -C doc html
rm doc/build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files jupyter_sphinx

%check
export JUPYTER_PLATFORM_DIRS=1
%pytest

%files -n python3-jupyter-sphinx -f %{pyproject_files}
%doc README.md

%files doc
%doc doc/build/html

%changelog
* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0.5.3-1
- Stop building for 32-bit x86

* Thu Dec 28 2023 Jerry James <loganjerry@gmail.com> - 0.5.3-1
- Version 0.5.3
- Drop upstreamed Sphinx 7.2 patch

* Mon Oct 30 2023 Jerry James <loganjerry@gmail.com> - 0.4.0-6
- Fix build with Sphinx 7.2.x (rhbz#2246943)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Python Maint <python-maint@redhat.com> - 0.4.0-4
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.4.0-3
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.4.0-2
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 25 2022 Jerry James <loganjerry@gmail.com> - 0.4.0-1
- Version 0.4.0
- Drop upstreamed -bash patch

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.3.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 0.3.2-1
- Initial RPM
