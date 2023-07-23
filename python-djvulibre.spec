%global srcname	djvulibre

Name:		python-%{srcname}
Version:	0.8.7
Release:	5%{?dist}
Summary:	Python support for the DjVu image format
License:	GPLv2
URL:		https://jwilk.net/software/python-djvulibre

Source0:	%{pypi_source %name}

# https://github.com/jwilk/python-djvulibre/pull/21
Patch0:		deprecated-notify.patch

BuildRequires:	gcc
BuildRequires:	djvulibre
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-sphinx
BuildRequires:	pyproject-rpm-macros

%description
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open-source implementation of DjVu.

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname}
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open-source implementation of DjVu.

%package -n python-%{srcname}-doc
Summary:    Documentation for python-djvulibre
BuildArch:  noarch

%description -n python-%{srcname}-doc
Documentation for python-djvulibre.

%prep
%autosetup -p1 -n %{name}-%{version}

# Make sure scripts in the examples directory aren't executable
chmod 0644  ./examples/*
# Replace obsolete references to Sphinx's `add_stylesheet` method.
sed -i 's/add_stylesheet/add_css_file/g' doc/api/conf.py
sed -i 's/static/_static/g' doc/api/conf.py	
# Move license file to the root
mv ./doc/COPYING ./
# This module is for Windows only
rm djvu/dllpath.py

%generate_buildrequires

%pyproject_buildrequires -r

%build
%pyproject_wheel

# Generate the HTML documentation.
PYTHONPATH=${PWD} sphinx-build-3 doc/api html
# Remove the sphinx-build leftovers.
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files djvu

%ifarch %ix86 x86_64
%check
%pytest -v
%endif

%files -n python3-%{srcname} -f %{pyproject_files}

%files -n python-%{srcname}-doc
%license COPYING
%doc html examples

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.8.7-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.8.7-1
- Update to 0.8.7 (RHBZ #2046871 and #2098892)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.6-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 9 2021 Audrey Toskin <audrey@tosk.in> - 0.8.6-4
- Patch out obsolete references to Sphinx's `add_stylesheet` method.
  See <https://fedoraproject.org/wiki/Changes/Sphinx4>

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.6-2
- Rebuilt for Python 3.10

* Wed Mar 10 2021 Audrey Toskin <audrey@tosk.in> - 0.8.6-1
- Bump to upstream version 0.8.6, which drops support for Python 3.2,
  but adds support for Python 3.10, and improves memory usage.

* Wed Mar 10 2021 Audrey Toskin <audrey@tosk.in> - 0.8.5-5
- Minor update to show maximum version of Python supported by
  python-djvulibre v0.8.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
