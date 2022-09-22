%{?!_without_python2:%global with_python2 0%{?_with_python2:1} || !(0%{?fedora} >= 30 || 0%{?rhel} >= 8)}
%{?!_without_python3:%global with_python3 0%{?_with_python3:1} || !0%{?rhel} || 0%{?rhel} >= 7}

%global srcname vcstool

Name:           python-%{srcname}
Version:        0.2.15
Release:        7%{?dist}
Summary:        Tool to invoke vcs commands on multiple repositories

License:        ASL 2.0
URL:            https://github.com/dirk-thomas/%{srcname}
Source0:        https://github.com/dirk-thomas/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Vcstool is a version control system (VCS) tool, designed to make working with
multiple repositories easier.

Note: This tool should not be confused with vcstools (with a trailing s) which
provides a Python API for interacting with different version control systems.
The biggest differences between the two are:

- vcstool doesn't use any state beside the repository working copies available
  in the filesystem.
- The file format of vcstool export uses the relative paths of the repositories
  as keys in YAML which avoids collisions by design.
- vcstool has significantly less lines of code than vcstools including the
  command line tools built on top.


%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python2-pyyaml
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python2-pyyaml
Requires:       python2-setuptools
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     git
%endif

%description -n python2-%{srcname}
Vcstool is a version control system (VCS) tool, designed to make working with
multiple repositories easier.

Note: This tool should not be confused with vcstools (with a trailing s) which
provides a Python API for interacting with different version control systems.
The biggest differences between the two are:

- vcstool doesn't use any state beside the repository working copies available
  in the filesystem.
- The file format of vcstool export uses the relative paths of the repositories
  as keys in YAML which avoids collisions by design.
- vcstool has significantly less lines of code than vcstools including the
  command line tools built on top.
%endif


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  git
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-setuptools
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     git
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Vcstool is a version control system (VCS) tool, designed to make working with
multiple repositories easier.

Note: This tool should not be confused with vcstools (with a trailing s) which
provides a Python API for interacting with different version control systems.
The biggest differences between the two are:

- vcstool doesn't use any state beside the repository working copies available
  in the filesystem.
- The file format of vcstool export uses the relative paths of the repositories
  as keys in YAML which avoids collisions by design.
- vcstool has significantly less lines of code than vcstools including the
  command line tools built on top.
%endif


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif


%install
# There are three extra things we're doing here:
# 1. Making each executable available with a -X and -X.Y suffix
# 2. Giving each python version a directory of executables for %%check
# 3. Integrating with the bash-completion package

install -d %{buildroot}%{_datadir}/bash-completion/completions %{buildroot}%{_bindir}

%if 0%{?with_python2}
%py2_install -- --install-scripts %{_bindir}2

echo -n "" > py2_bins
for f in `ls %{buildroot}%{_bindir}2`; do
  mv %{buildroot}%{_bindir}2/$f %{buildroot}%{_bindir}/$f-%{python2_version}
  ln -s $f-%{python2_version} %{buildroot}%{_bindir}/$f-2
%if !(0%{?with_python3})
  ln -s $f-%{python2_version} %{buildroot}%{_bindir}/$f
  echo "%{_bindir}/$f" >> py2_bins
%endif
  echo -e "%{_bindir}/$f-2\n%{_bindir}/$f-%{python2_version}" >> py2_bins
done

# Integrate bash completion with the bash-completion package
cp -f %{buildroot}%{_datadir}/%{srcname}-completion/vcs.bash %{buildroot}%{_datadir}/bash-completion/completions/vcs
ln -sf vcs %{buildroot}%{_datadir}/bash-completion/completions/vcs-2
ln -s vcs %{buildroot}%{_datadir}/bash-completion/completions/vcs-%{python2_version}
%endif

%if 0%{?with_python3}
%py3_install -- --install-scripts %{_bindir}%{python3_pkgversion}

echo -n "" > py3_bins
for f in `ls %{buildroot}%{_bindir}%{python3_pkgversion}`; do
  mv %{buildroot}%{_bindir}%{python3_pkgversion}/$f %{buildroot}%{_bindir}/$f-%{python3_version}
  ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f-3
  ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f
  echo -e "%{_bindir}/$f\n%{_bindir}/$f-3\n%{_bindir}/$f-%{python3_version}" >> py3_bins
done

# Integrate bash completion with the bash-completion package
cp -f %{buildroot}%{_datadir}/%{srcname}-completion/vcs.bash %{buildroot}%{_datadir}/bash-completion/completions/vcs
ln -sf vcs %{buildroot}%{_datadir}/bash-completion/completions/vcs-3
ln -s vcs %{buildroot}%{_datadir}/bash-completion/completions/vcs-%{python3_version}
%endif


%check
# We skip two classes of test:
# 1. Code style
# 2. Tests which require network access
%define pytest_options \\\
  --ignore=test/test_flake8.py \\\
  --ignore test/test_commands.py \\\
  test

%if 0%{?with_python2}
%{__python2} -m pytest %pytest_options
%endif

%if 0%{?with_python3}
%{__python3} -m pytest %pytest_options
%endif


%if 0%{?with_python2}
%files -n python2-%{srcname} -f py2_bins
%license LICENSE
%doc CONTRIBUTING.md README.rst
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info/
%{_datadir}/%{srcname}-completion
%{_datadir}/bash-completion/completions/vcs
%{_datadir}/bash-completion/completions/vcs-2
%{_datadir}/bash-completion/completions/vcs-%{python2_version}
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname} -f py3_bins
%license LICENSE
%doc CONTRIBUTING.md README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_datadir}/%{srcname}-completion
%{_datadir}/bash-completion/completions/vcs
%{_datadir}/bash-completion/completions/vcs-3
%{_datadir}/bash-completion/completions/vcs-%{python3_version}
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.15-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.15-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Scott K Logan <logans@cottsay.net> - 0.2.15-1
- Update to 0.2.15 (rhbz#1891662)

* Sun Aug 16 2020 Scott K Logan <logans@cottsay.net> - 0.2.14-1
- Update to 0.2.14 (rhbz#1862412)

* Mon Jul 27 2020 Scott K Logan <logans@cottsay.net> - 0.2.13-1
- Update to 0.2.13 (rhbz#1859022)

* Thu Jul 02 2020 Scott K Logan <logans@cottsay.net> - 0.2.12-1
- Update to 0.2.12 (rhbz#1853214)

* Thu Jun 18 2020 Scott K Logan <logans@cottsay.net> - 0.2.11-1
- Update to 0.2.11 (rhbz#1847809)

* Mon Jun 15 2020 Scott K Logan <logans@cottsay.net> - 0.2.10-1
- Update to 0.2.10 (rhbz#1846217)

* Fri May 29 2020 Scott K Logan <logans@cottsay.net> - 0.2.9-1
- Update to 0.2.9 (rhbz#1838404)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.8-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Scott K Logan <logans@cottsay.net> - 0.2.8-1
- Update to 0.2.8 (rhbz#1833742)

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.2.7-1
- Update to 0.2.7 (rhbz#1787844)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.2.4-1
- Update to 0.2.4 (rhbz#1764143)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.8

* Thu Aug 08 2019 Scott K Logan <logans@cottsay.net> - 0.2.3-1
- Update to 0.2.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Scott K Logan <logans@cottsay.net> - 0.2.2-1
- Update to 0.2.2

* Mon Jun 10 2019 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Update to 0.2.1 (rhbz#1718722)

* Mon Mar 18 2019 Scott K Logan <logans@cottsay.net> - 0.1.40-1
- Update to 0.1.40
- Drop python3_other subpackage

* Tue Feb 19 2019 Scott K Logan <logans@cottsay.net> - 0.1.39-1
- Update to 0.1.39

* Thu Jan 17 2019 Scott K Logan <logans@cottsay.net> - 0.1.38-1
- Update to 0.1.38

* Tue Oct 16 2018 Scott K Logan <logans@cottsay.net> - 0.1.37-1
- Initial package
