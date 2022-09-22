%global srcname libsass

Name:           python-%{srcname}
Version:        0.20.0
Release:        9%{?dist}
Summary:        Python bindings for libsass

License:        MIT
URL:            https://github.com/dahlia/libsass-python
Source0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# Patch for correct naming of manpages
Patch0:     python-libsass-man.patch

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-pytest
BuildRequires:  python3-werkzeug
BuildRequires:  libsass-devel
BuildRequires:  gcc-c++
# Needed for docs
BuildRequires:  python3-sphinx

%description
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung).

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires: python3-six

%description -n python3-%{srcname}
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung).

%prep
%autosetup -n %{srcname}-python-%{version} -p1
sed -i -e '/^#!\//, 1d' sassc.py

%build
# Export SYSTEM_SASS environment variable to use the
# system library, not the bundled one
export SYSTEM_SASS="true"
%py3_build
pushd docs
# There are differences between Python's naming of arches and the
# %%{_arch} macro. We need to ask Python for the platform name
PLATFORM=$(python3 -c "import sysconfig; print(sysconfig.get_platform())")
export PYTHONPATH=$(echo ../build/lib.${PLATFORM}-*)
make man    SPHINXBUILD=sphinx-build-3
popd

%install
# Same as above
export SYSTEM_SASS="true"
%py3_install
install -m 644 -D docs/_build/man/pysassc.1 %{buildroot}%{_mandir}/man1/pysassc.1

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
py.test-3 sasstests.py

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/_sass*.so
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/sass.py
%{python3_sitearch}/sassc.py
%{python3_sitearch}/pysassc.py
%{python3_sitearch}/sasstests.py
%{python3_sitearch}/sassutils/
%{_mandir}/man1/pysassc.1.gz
%{_bindir}/pysassc
# Collides with libsass.
%exclude %{_bindir}/sassc
# Same thing as %%{python3_sitearch}/sassc.py
# Also, we don't want *.py files in bindir.
%exclude %{_bindir}/sassc.py

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Charalampos Stratakis <cstratak@redhat.com> - 0.20.0-8
- Fix FTBFS with setuptools >= 62.1
Resolves: rhbz#2097098

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.20.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.20.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Marcel Plch <marcel.plch@protonmail.com> - 0.20.0-1
- Update to v0.20.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.19.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Marcel Plch <mplch@redhat.com> - 0.19.4-1
- Update to 0.19.4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Marcel Plch <mplch@redhat.com> - 0.18.0-1
- Update to 0.18.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Marcel Plch <mplch@redhat.com> - 0.14.5-3
- Add a needed BuildRequire

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Marcel Plch <mplch@redhat.com> - 0.14.5-1
- Initial version of the package

