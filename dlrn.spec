%global pkg_name dlrn
%global py_name DLRN
%global desc DLRN builds and maintains yum repositories following upstream commits from a Git repo.

Name:           %{pkg_name}
Version:        0.14.0
Release:        15%{?dist}
Summary:        Build and maintain yum repositories following upstream commits

License:        ASL 2.0
URL:            https://github.com/softwarefactory-project/DLRN
Source0:        https://pypi.io/packages/source/D/%{py_name}/%{py_name}-%{version}.tar.gz
Source1:        run-dlrn.sh
Source2:        projects.ini
Source3:        dlrn.service
Source4:        dlrn.timer
# https://softwarefactory-project.io/r/17981
Patch0001:      0001-Fixes-to-unit-tests.patch
BuildArch:      noarch

BuildRequires:  systemd-units
Requires:       python3-%{pkg_name} == %{version}-%{release}
Requires(pre):  shadow-utils
%{?systemd_requires}

%description
%{desc}

%package doc
Summary: Documentation for DLRN
BuildRequires:  %{py3_dist Sphinx} >= 1.1.2
BuildRequires:  %{py3_dist oslosphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}

%description doc
%{desc}

This package contains the DLRN documentation.

%package -n python3-%{pkg_name}
Summary: Build and maintain yum repositories following OpenStack upstream commits
%{?python_provide:%python_provide python3-%{pkg_name}}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Flask-HTTPAuth}
BuildRequires:  %{py3_dist distroinfo}
BuildRequires:  %{py3_dist fixtures}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist passlib}
BuildRequires:  %{py3_dist pbr}
BuildRequires:  %{py3_dist pymod2pkg}
BuildRequires:  %{py3_dist rdopkg}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sh}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist SQLAlchemy}
BuildRequires:  %{py3_dist python-subunit}
BuildRequires:  %{py3_dist stestr}
BuildRequires:  %{py3_dist testscenarios}
BuildRequires:  %{py3_dist testtools}
BuildRequires:  %{py3_dist PyYAML}
Requires:       mock
Requires:       rpm-build
Requires:       rpmdevtools
Requires:       createrepo_c
Requires:       git
Requires:       %{py3_dist alembic} >= 0.7
Requires:       %{py3_dist Flask}
Requires:       %{py3_dist Flask-HTTPAuth}
Requires:       %{py3_dist distroinfo}
Requires:       %{py3_dist Jinja2}
Requires:       %{py3_dist passlib} >= 1.6.5
Requires:       %{py3_dist pbr}
Requires:       %{py3_dist pymod2pkg} >= 0.5.5
Requires:       %{py3_dist PyMySQL}
Requires:       %{py3_dist renderspec}
Requires:       %{py3_dist requests}
Requires:       %{py3_dist sh} >= 1.12.6
Requires:       %{py3_dist six}
Requires:       %{py3_dist SQLAlchemy}
Requires:       %{py3_dist PyYAML}
Requires:       %{py3_dist rdopkg} >= 0.45

%description -n python3-%{pkg_name}
%{desc}

This package contains the Python 3 binaries.


%prep
%autosetup -p1 -n %{py_name}-%{version}
# Let's handle dependencies ourselves
rm -f *requirements.txt
# Fix shebangs
find scripts -type f -a \( -name '*.py' -o -name 'map-*-name' \) \
   -exec sed -i 's/^#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' {} \; \

%build
%py3_build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install
mv %{buildroot}%{_bindir}/dlrn %{buildroot}%{_bindir}/dlrn-%{python3_version}
ln -s %{_bindir}/dlrn-%{python3_version} %{buildroot}%{_bindir}/dlrn-3
ln -s %{_bindir}/dlrn-%{python3_version} %{buildroot}%{_bindir}/dlrn

# Setup directories
install -d -m 755 %{buildroot}%{_sysconfdir}/%{pkg_name}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{pkg_name}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{pkg_name}/data

# Install execution script
install -p -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/run-dlrn

# Install default configuration
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{pkg_name}/projects.ini

# Install systemd files
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/dlrn.service
install -p -D -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/dlrn.timer

%check
stestr run --test-path=dlrn/tests

%pre
getent group %{pkg_name} >/dev/null || groupadd -r %{pkg_name}
getent passwd %{pkg_name} >/dev/null || \
    useradd -m -r -g %{pkg_name} -G mock -s /bin/bash -c "DLRN user" %{pkg_name}
exit 0

%post
%systemd_post dlrn.service dlrn.timer

%preun
%systemd_preun dlrn.service dlrn.timer

%postun
%systemd_postun_with_restart dlrn.service dlrn.timer

%files
%license LICENSE
%dir %attr(0750, %{pkg_name}, %{pkg_name}) %{_sysconfdir}/%{pkg_name}
%dir %attr(0750, %{pkg_name}, %{pkg_name}) %{_sharedstatedir}/%{pkg_name}
%dir %attr(0750, %{pkg_name}, %{pkg_name}) %{_sharedstatedir}/%{pkg_name}/data
%dir %attr(0750, %{pkg_name}, %{pkg_name}) %{_datarootdir}/%{pkg_name}
%config(noreplace) %attr(0640, %{pkg_name}, %{pkg_name}) %{_sysconfdir}/%{pkg_name}/projects.ini
%{_unitdir}/dlrn.service
%{_unitdir}/dlrn.timer
%{_bindir}/delorean
%{_bindir}/dlrn
%{_bindir}/dlrn-user
%{_bindir}/dlrn-purge
%{_bindir}/dlrn-remote
%{_bindir}/run-dlrn
%{_datarootdir}/%{pkg_name}/scripts

%files doc
%doc README.rst HACKING.rst CONTRIBUTING.rst html
%license LICENSE

%files -n python3-%{pkg_name}
%license LICENSE
%{python3_sitelib}/dlrn
%{python3_sitelib}/DLRN-%{version}-py%{python3_version}.egg-info
%{_bindir}/dlrn-3
%{_bindir}/dlrn-%{python3_version}


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.14.0-14
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.14.0-11
- Rebuilt for Python 3.11

* Wed Jun 15 2022 Javier Peña <jpena@redhat.com> - 0.14.0-10
- Change to stestr for tests to fix issue with recent setuptools (bz#2097130)
- Remove python2 bits

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.14.0-7
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.0-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-3
- Rebuilt for Python 3.9

* Wed Apr 01 2020 Javier Peña <jpena@redhat.com> - 0.14.0-2
- Run unit tests sequentially

* Wed Apr 01 2020 Javier Peña <jpena@redhat.com> - 0.14.0-1
- Update to upstream version 0.14.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Javier Peña <jpena@redhat.com> - 0.9.1-1
- Updated to version 0.9.1
- Changed createrepo dependency to createrepo_c

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Javier Peña <jpena@redhat.com> - 0.9.0-1
- Updated to version 0.9.0
- Made python2 and python3 versions mutually exclusive

* Mon Jul 30 2018 Javier Peña <jpena@redhat.com> - 0.5.1-5
- Fix builds for Fedora 29 (bz#1603799)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 8 2017 Javier Peña <jpena@redhat.com> - 0.5.1-1
* Updated to version 0.5.1

* Wed Sep 27 2017 Javier Peña <jpena@redhat.com> - 0.5.0-1
* Updated to version 0.5.0

* Tue Sep 26 2017 Javier Peña <jpena@redhat.com> - 0.4.0-2
- Fixed permissions for files and directories

* Mon Sep 25 2017 Javier Peña <jpena@redhat.com> - 0.4.0-1
- First version
