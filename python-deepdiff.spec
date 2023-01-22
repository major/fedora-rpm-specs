# Don't have sphinx-sitemaps for now...
%bcond_with docs

Name:           python-deepdiff
Version:        6.1.0
Release:        2%{?dist}
Summary:        Deep Difference and search of any Python object/data
License:        MIT
URL:            https://github.com/seperman/deepdiff/
Source0:        https://github.com/seperman/deepdiff/archive/%{version}/%{name}-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-ordered-set
BuildRequires:  python3-pytest
BuildRequires:  python3dist(jsonpickle)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(setuptools)
# For docs
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-dotenv
BuildRequires:  python3-sphinx-sitemap
%endif
# For tests
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(pyyaml)

%description
Deep Difference of dictionaries, iterables, strings and other
objects. It will recursively look for all the changes.

%package     -n python3-deepdiff
Summary:        Python 3 package of %{name}
Requires:       python3-jsonpickle

%description -n python3-deepdiff
Deep Difference of dictionaries, iterables, strings and other
objects. It will recursively look for all the changes.

This is the Python 3 package.


%prep
%autosetup -n deepdiff-%{version} -p1
# these tests require CleverCSV, which we don't package
rm -f tests/test_command.py
# so does this other test, unless we cut the csv line out of its
# parametrization
sed -i '/t1.csv/d' tests/test_serialization.py
find deepdiff/ -name \*.py -exec sed -i '/#!\/usr\/bin\/env /d' {} \;

%build
%{py3_build}

%if %{with docs}
# Build docs
make -C docs html
# remove the sphinx-build leftovers
rm -rf docs/_build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
%{pytest}-3 tests/

%files -n python3-deepdiff
%license LICENSE
%doc AUTHORS.md README.md
%if %{with docs}
%doc docs/_build/html
%endif
%{_bindir}/deep
%{python3_sitelib}/deepdiff/
%{python3_sitelib}/deepdiff-%{version}-py*.egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 01 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.1.0-1
- Update to 6.1.0.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Adam Williamson <awilliam@redhat.com> - 5.8.2-1
- Update to 5.8.2
- Drop all Python 2 bits from spec
- Actually run the test suite
- Backport PR #327 to fix tests with Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-2
- Rebuilt for Python 3.9

* Fri Mar 13 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.7-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.7-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.7-1
- Update to 4.0.7.

* Wed May 15 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.6-1
- Update to 4.0.6.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.3.0-3
- Further review fixes.

* Mon Sep 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.3.0-2
- Review fixes.

* Sat Sep 22 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.3.0-1
- First release.

