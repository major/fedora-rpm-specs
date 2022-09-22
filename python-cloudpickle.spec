%global pypi_name cloudpickle
%global desc cloudpickle makes it possible to serialize Python constructs \
not supported by the default pickle module from the Python standard \
library. cloudpickle is especially useful for cluster computing where \
Python expressions are shipped over the network to execute on remote \
hosts, possibly close to the data. Among other things, cloudpickle \
supports pickling for lambda expressions, functions and classes defined \
interactively in the __main__ module.

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Extended pickling support for Python objects

License:        BSD
URL:            https://github.com/cloudpipe/cloudpickle
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

# Test requirements
BuildRequires:  %{py3_dist mock pytest tornado psutil}

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Simple backport of https://github.com/cloudpipe/cloudpickle/pull/475
# to make tests pass with Python 3.11b3
sed -i "s/'beta', 2/'beta', 4/" tests/cloudpickle_test.py

%build
%py3_build

%install
%py3_install


%check
# file_handles tests fail, TypeError: cannot pickle '_io.FileIO' object
# GH issue: https://github.com/cloudpipe/cloudpickle/issues/114
PYTHONPATH=tests/cloudpickle_testpkg %{__python3} -m pytest -v -k "not file_handles"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Sep 08 2022 Lumír Balhar <lbalhar@redhat.com> - 2.2.0-1
- Update to 2.2.0
Resolves: rhbz#2124985

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Lumír Balhar <lbalhar@redhat.com> - 2.1.0-3
- Fix tests for Python 3.11b3
Resolves: rhbz#2093921

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.11

* Mon May 23 2022 Lumír Balhar <lbalhar@redhat.com> - 2.1.0-1
- Update to 2.1.0
Resolves: rhbz#2088776

* Thu Mar 17 2022 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-3
- Fix compatibility with Python 3.11
Resolves: rhbz#2062127

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-1
- Update to 2.0.0
Resolves: rhbz#2003099

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.0-4
- Rebuilt for Python 3.10

* Mon May 10 2021 Lumír Balhar <lbalhar@redhat.com> - 1.6.0-3
- Remove patch for 3.10, PEP 563 has been postponed
  Resolves: rhbz#1958163

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Lumír Balhar <lbalhar@redhat.com> - 1.6.0-1
- Update to 1.6.0 (#1872513)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Lumír Balhar <lbalhar@redhat.com> - 1.5.0-1
- Update to 1.5.0 (#1852954)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Lumír Balhar <lbalhar@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Tue Apr 28 2020 Lumír Balhar <lbalhar@redhat.com> - 1.4.0-1
- Update to 1.4.0 (#1828201)

* Tue Feb 11 2020 Lumír Balhar <lbalhar@redhat.com> - 1.3.0-1
- Update to 1.3.0 (#1801277)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Lumír Balhar <lbalhar@redhat.com> - 1.2.2-1
- New upstream version 1.2.2 (bz#1750826)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Lumír Balhar <lbalhar@redhat.com> - 1.2.1-1
- New upstream version

* Wed May 15 2019 Lumír Balhar <lbalhar@redhat.com> - 1.1.1-1
- New upstream release

* Mon May 06 2019 Lumír Balhar <lbalhar@redhat.com> - 1.0.0-1
- New upstream version

* Tue Mar 26 2019 Lumír Balhar <lbalhar@redhat.com> - 0.8.1-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Lumír Balhar <lbalhar@redhat.com> - 0.7.0-1
- New upstream version

* Fri Nov 02 2018 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-1
- New upstream version
- Get rid of Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Lumir Balhar <lbalhar@redhat.com> - 0.3.1-1
- Initial package.
