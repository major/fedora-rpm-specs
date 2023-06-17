%global srcname hpilo
%global desc %{expand: \
HP iLO XML interface access from Python (Python 3)
This module will make it easy for you to access the Integrated Lights Out
management interface of your HP hardware. It supports RILOE II, iLO, iLO 2, iLO
3 and iLO 4. It uses the XML interface or hponcfg to access and change the iLO.}

Name:           python-%{srcname}
Version:        4.4.3
Release:        3%{?dist}
Summary:        Accessing the HP iLO XML interface from python

License:        ASL 2.0 or GPLv3+
URL:            https://github.com/seveas/python-hpilo
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-case
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description 
%{_desc}

%package     -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{desc}
%{desc}

%package        doc
Summary:        Documentation for %{name}

%description    doc
%{summary}.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sphinx-build -b html docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# remove version-control-internal-file
rm examples/elasticsearch/.gitignore

%install
%pyproject_install
%pyproject_save_files hpilo hpilo_fw

%check
# https://github.com/seveas/python-hpilo/issues/272
# pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES examples ilo.conf.example
%{_bindir}/hpilo_cli

%files doc
%license COPYING
%doc html

%changelog
* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 4.4.3-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 06 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 4.4.3-1
- Update to 4.4.3 (RHBZ #1885695)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.3-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.3-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 12:36:09 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.3-1
- Initial package
