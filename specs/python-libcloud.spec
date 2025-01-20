%global srcname apache-libcloud
%global shortname libcloud

%global _description %{expand:
libcloud is a client library for interacting with many of
the popular cloud server providers.  It was created to make
it easy for developers to build products that work between
any of the services that it supports.}

# Don't duplicate the same documentation
%global _docdir_fmt %{name}

Name:           python-%{shortname}
Version:        3.6.0
Release:        12%{?dist}
Summary:        A Python library to address multiple cloud provider APIs

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://libcloud.apache.org/
Source0:        %{pypi_source}
BuildArch:      noarch

# This is a downstream only patch persuant to
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch0:         000-remove-linter-deps.patch

# https://issues.apache.org/jira/browse/LEGAL-572
# Removing version restriction on python-requests
%{?el9:Patch1:  001-requests-chardet-unbundled.patch}

%description %{_description}


%package -n python3-%{shortname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{shortname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Don't package the test suite. We dont run it anyway
# because it requires valid cloud credentials.
rm -r %{shortname}/test/

# Delete shebang lines in the demos
sed -i '1d' demos/gce_demo.py demos/compute_demo.py

# Fix permissions for demos
chmod -x demos/gce_demo.py demos/compute_demo.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{shortname}


%files -n python3-%{shortname} -f %{pyproject_files}
%doc README.rst demos/
%license LICENSE


%check
%pyproject_check_import -t %{shortname}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.6.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.6.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.6.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 30 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 3.6.0-3
- Removed python-requests 2.26 requirement for epel9 build

* Fri Aug 26 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 3.6.0-2
- Fixed typo in specfile

* Sun Jul 31 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 3.6.0-1
- Rebased to 3.6.0
- Cleaned up spec
- Resolves rhbz#2013008

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.1-20
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.1-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-12
- Subpackage python2-libcloud has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Marcel Plch <mplch@redhat.com> - 2.2.1-8
- Patch for Python 3.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-6
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> 2.2.1-5
- Rebuilt the package to enable the python3-libcloud package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 2.2.1-3
- Fix the gitignore file for the package

* Wed Nov 22 2017 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 2.2.1-2
- Add package python-pytest-runner as BuildRequires

* Wed Oct 25 2017 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 2.2.1-1
- Apache Libcloud version 2.2.1 upgrade

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Daniel Bruno <dbruno@fedoraproject.org> - 2.0.0-1
- Apache Libcloud version 2.0.0rc2 upgrade

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuild for Python 3.6

* Wed Nov 16 2016 Dominika Krejci <dkrejci@redhat.com> - 1.3.0-2
- Add python3 subpackage
- Include the upstream demos
- Don't package the test suite

* Mon Oct 24 2016 Daniel Bruno <dbruno@fedoraproject.org> - 1.3.0-1
- Python Libcloud 1.3.0 release

* Tue Jul 12 2016 Daniel Bruno <dbruno@fedoraproject.org> - 1.1.0-1
- Python Libcloud 1.1.0 release

* Sun Jan 24 2016 Daniel Bruno <dbruno@fedoraprojec.org> - 0.20.1-1
- This is a bug-fix release of the 0.20 series.

* Thu Jan 07 2016 Daniel Bruno dbruno@fedoraproject.org - 0.20.0-1
- Release 0.20.0 with new features and improvements

* Mon Aug 10 2015 Daniel Bruno <dbruno@fedoraproject.org> - 0.18.0-1
- Apache Libcloud 0.18.0 release with bug fixes and new features

* Fri Feb 20 2015 Daniel Bruno <dbruno@fedoraproject.org> - 0.17.0-1
- Apache Libcloud 0.17.0 release

* Wed Nov 12 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.16.0-1
- First release in the 0.16 series

* Mon Jul 21 2014 Daniel Bruno <dbruno@fedoraproject.org - 0.15.1-2
- Libcloud 0.15.1 bug-fix release

* Fri Jun 27 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.15.0-1
- First release in the 0.15 series which it brings many new features,
  improvements and bug fixes

* Mon Feb 10 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.14.1-1
- Release 0.14.1 includes some bug-fixes, improvements and new features

* Fri Jan 31 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.14.0-1
- Libcloud new release 0.14.0

* Fri Jan 03 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.13.3-1
- Security Fix - BUG: 1047867 1047868

* Thu Sep 19 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.13.2-11
- Some bug fixes from Upstream

* Mon Sep 09 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.13.1-10
- Update to upstream release 0.13.1

* Mon Jul 01 2013 Daniel Bruno dbruno@fedoraproject.org - 0.13.0-9
- Update to upstream release 0.13.0, more details on Release Notes.

* Thu May 16 2013 Daniel Bruno dbruno@fedoraproject.org - 0.12.4-8
- Update to upstream version 0.12.4

* Tue Mar 26 2013 Daniel Bruno dbruno@fedoraproject.org - 0.12.3-6
- Update to upstream version 0.12.3

* Tue Feb 19 2013 Daniel Bruno dbruno@fedoraproject.org - 0.12.1-5
- Update to upstream version 0.12.1

* Wed Oct 10 2012 Daniel Bruno dbruno@fedoraproject.org - 0.11.3-4
- Update to 0.11.3

* Thu Aug 02 2012 Daniel Bruno dbruno@fedoraproject.org - 0.11.1-3
- Updating to upstream release 0.11.1

* Fri Jun 15 2012 Daniel Bruno dbruno@fedoraproject.org - 0.9.1-2
- Update to upstream version 0.10.1

* Mon Apr 16 2012 Daniel Bruno dbruno@fedoraproject.org - 0.9.1-1
- update to 0.9.1

* Mon Mar 26 2012 Daniel Bruno dbruno@fedoraproject.org - 0.8.0-4
- Updating release to 0.8.0

* Fri Dec 30 2011 Daniel Bruno dbruno@fedoraproject.org - 0.6.2-3
- Standardizing the description

* Tue Nov 22 2011 Daniel Bruno dbruno@fedoraproject.org - 0.6.2-2
- First build package build

