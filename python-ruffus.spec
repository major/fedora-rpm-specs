%global srcname ruffus

Name:           python-%{srcname}
Version:        2.8.4
Release:        10%{?dist}
Summary:        Light-weight Python computational pipeline management

License:        MIT
URL:            https://github.com/cgat-developers/ruffus
Source0:        %pypi_source
# See Debian Patches: https://sources.debian.org/patches/python-ruffus/2.8.1-6/
Patch0001:      use_libjs-mathjax.patch
# https://github.com/cgat-developers/ruffus/pull/126
Patch0002:      0001-Fix-doc-build-with-Sphinx-4.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
The Ruffus module is a lightweight way to add support for running computational
pipelines. Computational pipelines are often conceptually quite simple,
especially if we breakdown the process into simple stages, or separate tasks.
Each stage or task in a computational pipeline is represented by a Python
function. Each Python function can be called in parallel to run multiple jobs.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
The Ruffus module is a lightweight way to add support for running computational
pipelines. Computational pipelines are often conceptually quite simple,
especially if we breakdown the process into simple stages, or separate tasks.
Each stage or task in a computational pipeline is represented by a Python
function. Each Python function can be called in parallel to run multiple jobs.


%package -n python-%{srcname}-doc
Summary:        Documentation for %{srcname}

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  mathjax

Requires:       mathjax

%description -n python-%{srcname}-doc
Documentation for ruffus


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Fix permissions and shebangs.
chmod -x %{srcname}/{parse_old_style_ruffus,test/*}.py
for f in %{srcname}/*.py %{srcname}/test/*.py; do
    sed -e '1{\@^#!/usr/bin/env python@d}' -e '1{\@^#!/usr/bin/python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
done
for f in doc/static_data/example_scripts/*.py; do
    sed -i -e '1d;2i#!%{__python3}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
done

sed -i -e 's/unittest/unittest -v/' %{srcname}/test/*.cmd


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
pushd ruffus/test
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    bash run_all_unit_tests3.cmd
popd


%files -n python3-%{srcname}
%license LICENSE.TXT
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info/

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.TXT


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.8.4-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.8.4-6
- Fix docs with Sphinx 4

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.8.4-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.4-2
- Rebuilt for Python 3.9

* Sat Apr 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.8.4-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.3-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.8.3-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.8.1-3
- Add explicit sphinx_rtd_theme BuildRequires

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.8.1-1
- Update to latest version

* Tue Aug 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7.0-1
- Initial package.
