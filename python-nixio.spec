%global forgeurl    https://github.com/G-node/nixpy

Name:       python-nixio
Version:    1.5.3
Release:    4%{?dist}
Summary:    Python bindings for NIX

%global     tag     %version
%forgemeta

License:    BSD
URL:        %forgeurl
Source0:    %forgesource
# The tagged snapshot on GitHub still says "dev" but the manually uploaded
# release does not, so use the info.json from there
# https://github.com/G-Node/nixpy/issues/528
Source1:    info.json


BuildArch:      noarch
# No need for nix, they're uncoupling it from the C++
# https://github.com/G-Node/nixpy/pull/276

%description
The NIX project started as an initiative within the Electrophysiology Task
Force a part of the INCF Data sharing Program. The NIX data model allows to
store fully annotated scientific data-set, i.e. the data together with its
metadata within the same container. Our aim is to achieve standardization by
providing a common/generic data structure for a multitude of data types. See
the wiki for more information

The current implementations store the actual data using the HDF5 file format as
a storage backend.

%package -n python3-nixio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  gcc
# use tests_require which is deprecated
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-runner}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist matplotlib}

%description -n python3-nixio
%{description}

%package doc
Summary:        %{summary}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description doc
Documentation files for %{name}.

%prep
%forgesetup

# it sets examples_path based on the name of the cwd
sed -i "s/nixpy/nixpy-%{version}/" nixio/test/test_doc_examples.py

cp %{SOURCE1} nixio/info.json -v -p

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

PYTHONPATH=. sphinx-build-3 docs/source html
# Remove unneeded files
rm -fr html/.{buildinfo,doctrees}

# Remove shebang from documentation examples
for f in html/_downloads/*/*.py; do
    sed '1{\@^#!/usr/bin/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
done

%install
%pyproject_install
%pyproject_save_files nixio

%check
%{pytest}

%files -n python3-nixio -f %{pyproject_files}
%{_bindir}/nixio

%files doc
%doc README.rst html
%license LICENSE

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.5.3-2
- Rebuilt for Python 3.11

* Sat Apr 02 2022 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.3-1
- Update to latest release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Vanessa Christopher <vanessaigwe1@gmail.com> - 1.5.2-1
- Update to latest release

* Sun Oct 03 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.1-1
- Update to latest release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.9-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.9-10
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.9-4
- Fix build: rhbz 1706159

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.9-2
- Enable python dependency generator

* Sat Jan 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.9-1
- Update to 1.4.9

* Thu Oct 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.6-2
- Subpackage python2-nixio has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jul 18 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.6-1
- Update to 1.4.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.5-1
- Update to latest upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.3-1
- Use newer release and GitHub sources
- Run tests
- Define summary macro
- Add doc sub package

* Fri Jan 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.2-1
- Initial build
- use pydist macro
