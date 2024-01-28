%global _docdir_fmt python3-primecountpy

Name:           python-primecountpy
Version:        0.1.0
Release:        13%{?dist}
Summary:        Python Primecount wrapper

# GPL-3.0-only: setup.py
# GPL-2.0-or-later: primecountpy/primecount.pyx
License:        GPL-3.0-only AND GPL-2.0-or-later
URL:            https://github.com/dimpase/primecountpy
Source0:        %{url}/archive/v%{version}/primecountpy-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(primecount)
BuildRequires:  python3-cysignals-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest-cython}

%description
This package provides a Cython interface to the C++ library primecount.

%package     -n python3-primecountpy
Summary:        Python 3 Primecount wrapper

%description -n python3-primecountpy
This package provides a Cython interface to the C++ library primecount.

%package        doc
# The content is GPL-3.0-only AND GPL-2.0-or-later.  Other licenses are due to
# files copied in by Sphinx.
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
License:        GPL-3.0-only AND GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND MIT
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

%description    doc
This package contains API documentation for %{name}.

%prep
%autosetup -n primecountpy-%{version}

# Remove docs self-dependency
sed -i '/primecountpy/d' docs/requirements.txt

# Remove as-you-type search capability from the docs due to missing dependency
sed -i '/readthedocs-sphinx-search/d' docs/requirements.txt

%generate_buildrequires
%pyproject_buildrequires docs/requirements.txt

%build
# Do not pass -pthread to the compiler or linker
export CC=gcc
export LDSHARED="gcc -shared"
%pyproject_wheel

# Build the documentation
PYTHONPATH=$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots} \
make -C docs html
rm docs/build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files primecountpy

%check
ln -s ../$(find build -name \*.so) primecountpy
%pytest --doctest-cython primecountpy -v

%files -n python3-primecountpy -f %{pyproject_files}
%doc README.md

%files doc
%doc docs/build/html/
%license LICENSE

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0.1.0-11
- Stop building for 32-bit x86

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 0.1.0-10
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-9
- Don't needlessly BuildRequire self

* Sun Mar 26 2023 Jerry James <loganjerry@gmail.com> - 0.1.0-8
- Test with pytest-cython

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.1.0-7
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.1.0-6
- Convert License tags to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.1.0-5
- Rebuilt for Python 3.11

* Wed Mar 16 2022 Jerry James <loganjerry@gmail.com> - 0.1.0-4
- Add MIT tag to doc subpackage license due to bundled JavaScript

* Tue Mar 15 2022 Jerry James <loganjerry@gmail.com> - 0.1.0-3
- Ship license file with doc subpackage
- Require sphinx-referenced fonts from the doc subpackage
- Note bundling of jquery and underscore in the doc subpackage

* Mon Mar 14 2022 Jerry James <loganjerry@gmail.com> - 0.1.0-2
- Python macro improvements suggested by Miro

* Mon Mar  7 2022 Jerry James <loganjerry@gmail.com> - 0.1.0-1
- Initial RPM
