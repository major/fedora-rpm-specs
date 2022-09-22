%global _docdir_fmt python3-primecountpy

Name:           python-primecountpy
Version:        0.1.0
Release:        6%{?dist}
Summary:        Python Primecount wrapper

License:        GPLv3
URL:            https://github.com/dimpase/primecountpy
Source0:        %{url}/archive/v%{version}/primecountpy-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(primecount)
BuildRequires:  python3-cysignals-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist myst-parser}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist wheel}

%description
This package provides a Cython interface to the C++ library primecount.

%package     -n python3-primecountpy
Summary:        Python 3 Primecount wrapper

%description -n python3-primecountpy
This package provides a Cython interface to the C++ library primecount.

%package        doc
Summary:        API documentation for %{name}
# The docs are GPLv3.  The bundled jquery and underscore are MIT.
License:        GPLv3 and MIT
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

# Remove as-you-type search capability from the docs due to missing dependency
sed -i '/readthedocs-sphinx-search/d' docs/requirements.txt

%build
# Do not pass -pthread to the compiler or linker
export CC=gcc
export LDSHARED="gcc -shared"
%pyproject_wheel

# Build the documentation
PYTHONPATH=%{pyproject_build_lib} make -C docs html
rm docs/build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files primecountpy

%check
# If Fedora gets pytest-cython, we can do this instead:
#%%pytest --doctest-cython primecountpy -v
%pyproject_check_import

%files -n python3-primecountpy -f %{pyproject_files}
%doc README.md

%files doc
%doc docs/build/html/
%license LICENSE

%changelog
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
