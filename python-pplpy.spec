Name:           python-pplpy
Version:        0.8.7
Release:        11%{?dist}
Summary:        Python PPL wrapper

License:        GPL-3.0-or-later
URL:            https://pypi.org/project/pplpy/
Source0:        %pypi_source pplpy
# Fix the Cython include path and set the language level to 3
Patch0:         %{name}-cython.patch

BuildRequires:  gcc-c++
BuildRequires:  libmpc-devel
BuildRequires:  make
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  ppl-devel
BuildRequires:  python3-cysignals-devel
BuildRequires:  python3-devel

%description
This package provides a Python wrapper to the C++ Parma Polyhedra
Library (PPL).

%package     -n python3-pplpy
Summary:        Python 3 PPL wrapper
Recommends:     %{py3_dist cysignals}
Recommends:     %{py3_dist gmpy2}

%description -n python3-pplpy
This package provides a Python 3 wrapper to the C++ Parma Polyhedra
Library (PPL).

%package     -n python3-pplpy-devel
# The content is GPL-3.0-or-later.  Other licenses are due to files copied in
# by Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/classic.css: BSD-2-Clause
# _static/default.css: BSD-2-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sidebar.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT
Summary:        Development files for the python 3 PPL wrapper
Requires:       python3-pplpy%{?_isa} = %{version}-%{release}

%description -n python3-pplpy-devel
Development files for the python 3 PPL wrapper.

%prep
%autosetup -p0 -n pplpy-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
# Do not pass -pthread to the compiler or linker
export CC=gcc
export LDSHARED="gcc -shared"
%pyproject_wheel

# Build the documentation
PYTHONPATH=$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots} \
make -C docs html
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files 'ppl*'

%check
%tox

%files -n python3-pplpy -f %{pyproject_files}
%doc CHANGES.txt README.html
%exclude %{python3_sitearch}/ppl/*.hh
%exclude %{python3_sitearch}/ppl/*.pxd

%files -n python3-pplpy-devel
%doc docs/build/html/*
%{python3_sitearch}/ppl/*.hh
%{python3_sitearch}/ppl/*.pxd

%changelog
* Tue Jul 25 2023 Jerry James <loganjerry@gmail.com> - 0.8.7-11
- Update cython patch for Cython 3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.8.7-10
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.8.7-9
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.8.7-8
- Move API documentation to the devel subpackage
- Convert License tags to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.7-7
- Rebuilt for Python 3.11

* Mon Mar 21 2022 Jerry James <loganjerry@gmail.com> - 0.8.7-6
- Rebuild for python-cysignals 1.11.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.7-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Jerry James <loganjerry@gmail.com> - 0.8.7-1
- Version 0.8.7

* Mon Jan 18 2021 Jerry James <loganjerry@gmail.com> - 0.8.6-1
- Version 0.8.6
- Drop unneeded pari-devel BR

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-5
- Invoke cython at language level 3
- Do not link with libpthread unnecessarily

* Tue Sep 10 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-4
- Install the documentation where sagemath wants it

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-1
- Initial RPM
