%{?python_enable_dependency_generator}

# Default to Python 3
%global __python %{__python3}
%global python_pkgversion %{python3_pkgversion}

Name:               pagure-dist-git
Version:            1.15
Release:            2%{?dist}
Summary:            Pagure Git auth backend for Dist-Git setups

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:            GPL-2.0-or-later
URL:                https://pagure.io/pagure-dist-git
Source0:            https://releases.pagure.org/pagure-dist-git/pagure_dist_git-%{version}.tar.gz
BuildArch:          noarch

BuildRequires:      python%{python_pkgversion}-devel
BuildRequires:      python%{python_pkgversion}-setuptools

Requires:           pagure >= 5.2
Requires:           python%{python_pkgversion}-requests

# This is actually an extension to Pagure itself and can't be built this way
# So we're changing it all up..
Obsoletes:          python-%{name} < 0.12
Obsoletes:          python2-%{name} < 0.12
Obsoletes:          python3-%{name} < 0.12
# However, we'll preserve some backwards compatibility here
Provides:           python%{python_pkgversion}-%{name} = %{version}-%{release}

%description
This project hosts the logic to generate gitolite's configuration file for
Dist-Git, which has a different access model than regular Pagure Git systems.


%prep
%autosetup -n pagure_dist_git-%{version}


%build
%py_build


%install
%py_install


# Install the different cron job scripts
mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/pagure-dist-git/
install -p -m 644 scripts/*.py $RPM_BUILD_ROOT/%{_libexecdir}/pagure-dist-git/

%if 0%{?fedora} || 0%{?rhel} >= 8
# Byte compile everything not in sitelib
%py_byte_compile %{__python} %{buildroot}%{_libexecdir}/pagure-dist-git/
%endif

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/pagure_distgit/
%{python_sitelib}/dist_git_auth.py*
%{python_sitelib}/pagure_dist_git-%{version}*
%if 0%{?python_pkgversion} != 2
%{python3_sitelib}/__pycache__/dist_git_auth*.pyc
%endif
%{_libexecdir}/pagure-dist-git/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Carl George <carlwgeorge@fedoraproject.org> - 1.15-1
- Update to 1.15 to resolve epel10 issue
- https://pagure.io/releng/issue/12236

* Thu Aug 08 2024 Tomas Hrcka <thrcka@redhat.com> - 1.14-1
- Update to 1.14
- Remove pdc from plugin.py
- Remove pdc query from is_supported_branch function

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.13-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.13-7
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.13-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Lenka Segura <lsegura@redhat.com> - 1.13-1
- Update to 1.13
- Include the sync_fas_group and load_from_disk utility scripts (Pierre-Yves Chibon)
- Script to sync all the ACLs from pkgdb to pagure
- Add utility script to migrate a single project from pkgdb to pagure_poc
- Include pkgdb2pagure_acls.py in the releases
- Multiple fixes in the pkgdb2pagure_acls.py scripts
- Updated the load_from_disk and other scripts to python3 (Adam Saleh)
- search exact build NVRs in Koji (Ken Dreyer)
- Add new monitoring options for release-monitoring (Michal Konecny)
- Consistent order of users in pagure_owner_alias.json (Anatoli Babenia)
- Explain relation to src.fedoraproject.org (Anatoli Babenia)
- Add a hint for rejecting a push to disabled branch (Lenka Segura)
- Add give_orphan endpoint (Mattia Verga)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.12-4
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Kevin Fenzi <kevin@scrye.com> - 1.12-1
- Update to 1.12. Fixes rhbz#1945101

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.1-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Neal Gompa <ngompa13@gmail.com> - 1.10.1-1
- Update to 1.10.1

* Tue Aug 04 2020 Neal Gompa <ngompa13@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.9

* Thu May 14 2020 Neal Gompa <ngompa13@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Mon Mar 30 2020 Neal Gompa <ngompa13@gmail.com> - 1.6.1-1
- Update to 1.6.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Neal Gompa <ngompa13@gmail.com> - 1.5.0-1
- Rebase to 1.5.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Neal Gompa <ngompa13@gmail.com> - 1.2.1-1
- Rebase to 1.2.1

* Tue Sep 18 2018 Neal Gompa <ngompa13@gmail.com> - 0.12-1
- Rework and simplify packaging to mimic pagure's package setup
- Rebase to the latest version of the extension
- Drop Python 2 build for F29+ (#1627133)

* Mon Sep 10 2018 Ralph Bean <rbean@redhat.com> - 0.1-4
- Enable python 3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jun 30 2017 Ralph Bean <rbean@redhat.com> - 0.1-1
- Initial packaging for Fedora
