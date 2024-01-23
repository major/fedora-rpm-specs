%global srcname ccdproc
%global summary Astropy affiliated package for reducing optical/IR CCD data

Name:           python-%{srcname}
Version:        2.4.1
Release:        2%{?dist}
Summary:        %{summary}

License:        BSD-3-Clause
URL:            http://ccdproc.readthedocs.io/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The ccdproc package is a collection of code that will be helpful in basic CCD
processing. These steps will allow reduction of basic CCD data as either a
stand-alone processing or as part of a pipeline.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files ccdproc

%check
# Tests require memory-profiler, not in Fedora
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst licenses/LICENSE_STSCI_TOOLS.txt
%doc CHANGES.rst README.rst

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Sergio Pascual <sergiopr@fedoraproject.com> - 2.4.1-1
- New upstream source 2.4.1
- New style python macros
- Updated to SPDX license

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 2.3.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Python Maint <python-maint@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Christian Dersch <lupinix@fedoraproject.org> - 2.3.0-1
- new version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Christian Dersch <lupinix@fedoraproject.org> - 2.1.0-1
- new version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Christian Dersch <lupinix@fedoraproject.org> - 2.0.1-1
- new version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-7.post1
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4.post1
- Remove python2 subpackage (#1632571)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2.post1
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 1.3.0-1.post1
- New version (1.3.0.post1)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Christian Dersch <lupinix@mailbox.org> - 1.2.0-1
- new version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuild for Python 3.6

* Tue Oct 11 2016 Christian Dersch <lupinix@mailbox.org> - 1.1.0-2
- Added dependencies for astroscrappy and reproject

* Sun Sep 25 2016 Christian Dersch <lupinix@mailbox.org> - 1.1.0-1
- Added BuildRequires for astropy-helpers
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 29 2016 Christian Dersch <lupinix@mailbox.org> - 1.0.1-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Christian Dersch <lupinix@mailbox.org> - 0.3.3-2
- fixed requirements

* Sun Nov 22 2015 Christian Dersch <lupinix@mailbox.org> - 0.3.3-1
- initial spec


