%global pypi_name nikola

Name:           python-%{pypi_name}
Version:        8.2.4
Release:        5%{?dist}
Summary:        A modular, fast, simple, static website and blog generator

License:        MIT and CC0 and BSD
URL:            https://getnikola.com/
Source0:        https://github.com/getnikola/nikola/archive/v%{version}/nikola-%{version}.tar.gz
# https://github.com/getnikola/nikola/issues/3700
# https://github.com/getnikola/nikola/pull/3701
# Fix to work with Python 3.12-compatible yapsy
Patch:          0001-Handle-change-to-plugin-loading-in-recent-yapsy-3700.patch
BuildArch:      noarch

BuildRequires:  python3-devel
# Sphinx required for documentation
BuildRequires:  python3dist(sphinx)

# Required for testing ( requires + extras + testing)
#  * from requirements.txt
BuildRequires:  python3dist(doit)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(mako)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(unidecode)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(yapsy)
BuildRequires:  python3dist(pyrss2gen)
BuildRequires:  python3dist(blinker)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(natsort)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(piexif)
BuildRequires:  python3dist(babel)
# * from requirements-extras.txt
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(husl)
BuildRequires:  python3dist(pyphen)
BuildRequires:  python3dist(micawber)
BuildRequires:  python3dist(pygal)
BuildRequires:  python3dist(typogrify)
BuildRequires:  python3dist(phpserialize)
BuildRequires:  python3dist(notebook)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(ghp-import)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(watchdog)
BuildRequires:  python3dist(ruamel-yaml)
BuildRequires:  python3dist(toml)
# * from requirements-tests.txt
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(freezegun)
BuildRequires:  python3dist(flake8)

%description
Nikola is a static site and blog generator using Python. It generates sites
with tags, feeds, archives, comments, and more from plain text files. Source
 can be unformatted, or formatted with reStructuredText or Markdown.
It also automatically builds image galleries.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       glyphicons-halflings-fonts
# Extra requirements to enable plugins
Requires:  python3dist(jinja2)
Requires:  python3dist(husl)
Requires:  python3dist(pyphen)
Requires:  python3dist(micawber)
Requires:  python3dist(pygal)
Requires:  python3dist(typogrify)
Requires:  python3dist(phpserialize)
Requires:  python3dist(notebook)
Requires:  python3dist(ipykernel)
Requires:  python3dist(ghp-import)
Requires:  python3dist(aiohttp)
Requires:  python3dist(watchdog)
Requires:  python3dist(ruamel-yaml)
Requires:  python3dist(toml)

# nikola carries these python modules bundled
## a modified version to use dateutil instead of pytz
Provides:  bundled(python3-pytzlocal)
## this is a small module made by Chris Warrick (a Nikola main contributor)
Provides:  bundled(python3-datecond) = 0.1.6
## this is a small module made by Chris Warrick (a Nikola main contributor)
Provides:  bundled(python3-pygments_better_html)

%description -n python3-%{pypi_name}
Nikola is a static site and blog generator using Python. It generates sites
with tags, feeds, archives, comments, and more from plain text files. Source
 can be unformatted, or formatted with reStructuredText or Markdown.
This package contains the Python implementation of nikola.


%package -n python-%{pypi_name}-doc
Summary:        python-nikola documentation
Obsoletes:      python2-nikola < 8
Obsoletes:      python3-nikola < 8
%description -n python-%{pypi_name}-doc
Documentation for python-nikola


%package -n %{pypi_name}
Summary:        %{summary}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n %{pypi_name}
Documentation for python-nikola
Nikola is a static site and blog generator using Python. It generates sites
with tags, feeds, archives, comments, and more from plain text files. Source
 can be unformatted, or formatted with reStructuredText or Markdown.
It also automatically builds image galleries.


%prep
%autosetup -p1 -n nikola-%{version}
# Remove bundled egg-info
rm -rf Nikola.egg-info


%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/sphinx html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
pytest


%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/nikola
%{python3_sitelib}/Nikola-%{version}-py%{python3_version}.egg-info


%files -n python-%{pypi_name}-doc
%license LICENSE.txt
%doc html


%files -n %{pypi_name}
%license LICENSE.txt
%{_bindir}/nikola
%dir %{_datadir}/doc/%{pypi_name}
%{_datadir}/doc/%{pypi_name}/*.rst
%{_mandir}/man1/nikola.1.gz


%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Adam Williamson <awilliam@redhat.com> - 8.2.4-3
- Improve the plugin template loading patch

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 8.2.4-2
- Rebuilt for Python 3.12

* Mon May 01 2023 Sandro Mani <manisandro@gmail.com> - 8.2.4-1
- Update to 8.2.4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Adam Williamson <awilliam@redhat.com> - 8.2.3-1
- Update to 8.2.3 (#2113070)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Adam Williamson <awilliam@redhat.com> - 8.2.2-3
- Backport PR #3631 to fix gist processor for Python 3.11

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 8.2.2-2
- Rebuilt for Python 3.11

* Wed May 11 2022 Charalampos Stratakis <cstratak@redhat.com> - 8.2.2-1
- Update to 8.2.2
Resolves: rhbz#2035816, rhbz#2081902

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 28 2021 Sandro Mani <manisandro@gmail.com> - 8.1.3-5
- Use switch to the original ghp-import rather than ghp-import2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul  6 2021 José Matos <jamatos@fedoraproject.org> - 8.1.3-3
- off by one type (larger than 34 and not larger or equal to 34)

* Tue Jul  6 2021 José Matos <jamatos@fedoraproject.org> - 8.1.3-2
- make pygments-2.8 patch conditional on the Fedora versions where it is needed

* Tue Jun 29 2021 José Matos <jamatos@fedoraproject.org> - 8.1.3-1
- update to 8.1.3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 8.1.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 José Matos <jamatos@fedoraproject.org> - 8.1.2-1
- update to 8.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 José Matos <jamatos@fedoraproject.org> - 8.1.1-1
- update to 8.1.1

* Fri Jul  3 2020 José Matos <jamatos@fedoraproject.org> - 8.1.0-1
- update to 8.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.0.4-10
- Rebuilt for Python 3.9

* Sat Mar 21 2020 José Matos <jamatos@fedoraproject.org> - 8.0.4-9
- Claim ownership of nikola documentation directory

* Sat Mar 21 2020 José Matos <jamatos@fedoraproject.org> - 8.0.4-8
- change Source0 to a more canonical form regarding github archives

* Fri Mar 20 2020 José Matos <jamatos@fedoraproject.org> - 8.0.4-7
- pass all the Requires: and Provides: fields to the python3
  subpackage (where they belong)

* Fri Mar 20 2020 José Matos <jamatos@fedoraproject.org> - 8.0.4-6
- document the two python modules bundled with nikola

* Mon Mar 16 2020 José Matos <jamatos@fedoraproject.org> - 8.0.4-5
- add Obsoletes to nikola for versions < 8 to ensure a clean upgrade path
- simplify the testing now that Fedora 31 has the new python-markdown

* Fri Mar  6 2020 José Matos <jamatos@fedoraproject.org> - 8.0.4-4
- Require git-core instead of git to support "%%autosetup -S git"

* Thu Mar  5 2020 José Matos <jamatos@fedoraproject.org> - 8.0.4-3
- use directly pytest for tests instead of using setup.py
- add upstream patch to fix a test

* Tue Feb 25 2020 José Matos <jamatos@fedoraproject.org> - 8.0.4-2
- Reenable tests to see if they now work
- Add extra requirements to enable plugins

* Tue Feb 25 2020 José Matos <jamatos@fedoraproject.org> - 8.0.4-1
- update to 8.0.4

* Sun Jun  9 2019 José Matos <jamatos@fedoraproject.org> - 8.0.2-1
- package resubmitted to Fedora.

* Sat Sep  8 2018 José Matos <jamatos@fedoraproject.org> - 7.8.15-2
- make Requires dependencies greater or equal rather than just equal.

* Sat Sep  1 2018 José Matos <jamatos@fedoraproject.org> - 7.8.15-1
- initial package.
- disable for now the dependency on ws4py because it does not build with python3.7
