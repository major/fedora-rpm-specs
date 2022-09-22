# Lots of tests fail, even in a clean pip environment
%bcond_with tests

%global _description %{expand:
PyBIDS is a Python module to interface with datasets conforming BIDS.}

%global srcname     pybids

Name:       python-%{srcname}
Version:    0.13.1
Release:    6%{?dist}
Summary:    Interface with datasets conforming to BIDS

License:    MIT
URL:        https://bids.neuroimaging.io
Source0:    https://github.com/INCF/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:    Interface with datasets conforming to BIDS
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist grabbit} >= 0.2.5
BuildRequires:  %{py3_dist num2words}
BuildRequires:  %{py3_dist duecredit}
BuildRequires:  %{py3_dist nibabel}
BuildRequires:  %{py3_dist patsy}
BuildRequires:  %{py3_dist bids-validator}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist sqlalchemy}

%description -n python3-%{srcname} %{_description}

%package doc
Summary:    Interface with datasets conforming to BIDS
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist m2r}
BuildRequires:  %{py3_dist numpydoc}

%description doc
Description for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

# stray backup file?
rm -rf *.egg-info

# Remove bundled six and inflect
rm -rf bids/external

pushd bids
    sed -ibackup 's/from.*external import/import/' layout/{layout,index,models}.py utils.py
popd


%build
%py3_build

pushd doc && \
    PYTHONPATH=.. sphinx-build-3 . html
    rm -fv .buildinfo
popd


%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=. %{pytest} -s -v -k-test_split .
%endif

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{_bindir}/pybids
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/bids/

%files doc
%doc examples/ doc/html
%license LICENSE

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.13.1-5
- Fix extra newline in description
- Drop unnecessary python_enable_dependency_generator macro
- Switch URL to HTTPS

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.13.1-2
- Rebuilt for Python 3.10

* Sat May 22 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.13.1-1
- Update to latest release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.4-1
- Update to 0.12.4

* Sun Sep 13 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.1-1
- Update to new release

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.0-1
- Update to 0.12.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.10.2-1
- Update to 0.10.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Aniket Pradhan <major@fedoraproject.org> - 0.10.0-1
- Bumped to v0.10.0

* Tue Oct 1 2019 Aniket Pradhan <major@fedoraproject.org> - 0.9.4-1
- Bumped to v0.9.4

* Thu Aug 22 2019 Aniket Pradhan <aniket17133@iiitd.ac.in> - 0.9.3-1
- Bumped to v0.9.3

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-1
- Update to 0.9.1

* Mon Apr 08 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.0-1
- Update the latest release
- Drop dropped grabbit dep
- Add new BR: python-bids-validator: requires review: 1697498
- Unbundle new bundled libs

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3.gite35ced6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.5-2.gite35ced6
- Use bconds

* Wed Nov 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.5-1.gite35ced6
- Use latest git snapshot that fixes tests
- Add documentation and examples in subpackage

* Wed Nov 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.3-2
- Enable tests now that duecredit is available in rawhide
- Disable py2 build since python-nibabel is only py3 even in F29

* Fri Jul 20 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.3-1
- Update to latest release
- Use py.test
- Disable tests until nibabel is fixed

* Mon Jan 15 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.2-2
- Use github source for license and test suite
- Fix requires and build requires

* Fri Jan 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.2-1
- Initial build
