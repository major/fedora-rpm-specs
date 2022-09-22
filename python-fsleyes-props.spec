# These are unreliable and often hang
%bcond_with xvfb_tests

%global srcname fsleyes-props

%global desc %{expand: \
fsleyes-props is a library which is used by used by FSLeyes , and which allows
you to:

- Listen for change to attributes on a python object,
- Automatically generate wxpython widgets which are bound to attributes of
  a python object
- Automatically generate a command line interface to set values of the
  attributes of a python object.}


Name:           python-%{srcname}
Version:        1.7.3
Release:        4%{?dist}
Summary:        [wx]Python event programming framework

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist wxPython}
BuildRequires:  %{py3_dist deprecation}
BuildRequires:  %{py3_dist fsleyes-widgets}
BuildRequires:  %{py3_dist fslpy}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist pytest pytest-cov}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  xorg-x11-server-Xvfb

Requires:  %{py3_dist six}
Requires:  %{py3_dist matplotlib}
Requires:  %{py3_dist wxPython}
Requires:  %{py3_dist deprecation}
Requires:  %{py3_dist fsleyes-widgets}
Requires:  %{py3_dist fslpy}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%package doc
Summary:        %{summary}

%description doc
This package contains documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}
rm -rfv fsleyes_props.egg-info

find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;

# Fix requirements files, the auto-dep generator does not like "*".
sed -i 's/fsleyes-widgets.*/fsleyes-widgets>=0.6/' requirements.txt


%build
%py3_build

# Build documentation
PYTHONPATH=.  sphinx-build-3 doc html
# Remove artefacts
rm -frv html/.buildinfo
rm -frv html/.doctrees

%install
%py3_install


%check
%if %{with xvfb_tests}
# These tests fail. Upstream says tests are not reliable, but work on his Ubuntu setup
xvfb-run pytest-3 tests --ignore=tests/test_widget_boolean.py --ignore=tests/test_widget_number.py --ignore=tests/test_widget_point.py
%endif


%files -n python3-%{srcname}
%license LICENSE COPYRIGHT
%doc README.rst
%{python3_sitelib}/fsleyes_props/
%{python3_sitelib}/fsleyes_props-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE COPYRIGHT
%doc html

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Python Maint <python-maint@redhat.com> - 1.7.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.7.3-1
- Update to latest release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.10

* Sun Mar 28 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.7.2-1
- Update to latest release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.7.0-2
- Explicitly BR setuptools

* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.7.0-1
- Update to 1.7.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.7-5
- Rebuilt for Python 3.9

* Fri Mar 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.7-4
- Fix typo in requirements

* Sun Feb 16 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.7-3
- Work around requirement autogenerator limitations

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.7-1
- Update to 1.6.7
- use conditional for unreliable tests

* Mon Oct 28 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.6-2
- Remove python2 code from spec

* Mon Sep 23 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 1.6.6-1
- Update to 1.6.6

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.5-1
- Update to new release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.4-1
- Initial build
