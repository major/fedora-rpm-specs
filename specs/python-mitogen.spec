# what it's called on pypi
%global srcname mitogen
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

Name:           python-%{pkgname}
Version:        0.3.19
Release:        2%{?dist}
Summary:        Distributed self-replicating programs in Python

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/dw/mitogen
Source0:        %pypi_source
BuildArch:      noarch

%global common_description %{expand:
Mitogen is a Python library for writing distributed self-replicating programs.

There is no requirement for installing packages, copying files around, writing
shell snippets, upfront configuration, or providing any secondary link to a
remote machine aside from an SSH connection. Due to its origins for use in
managing potentially damaged infrastructure, the remote machine need not even
have free disk space or a writeable filesystem.

It is not intended as a generic RPC framework; the goal is to provide a robust
and efficient low-level API on which tools like Salt, Ansible, or Fabric can be
built, and while the API is quite friendly and comparable to Fabric, ultimately
it is not intended for direct use by consumer software.

The focus is to centralize and perfect the intricate dance required to run
Python code safely and efficiently on a remote machine, while avoiding
temporary files or large chunks of error-prone shell scripts, and supporting
common privilege escalation techniques like sudo, potentially in combination
with exotic connection methods such as WMI, telnet, or console-over-IPMI.}

%description %{common_description}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}

%prep
%autosetup -n %{srcname}-%{version} -p 1
# No compat support needed
rm -r mitogen/compat ansible_mitogen/compat

%build
%py3_build

%install
%py3_install

%check
# tests/README.md says the tests need:
#    - internet connection
#    - working docker daemon

%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{libname}
%{python3_sitelib}/ansible_%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 04 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.19-1
- Update to latest upstream release (closes rhbz#2329946)

* Wed Nov 13 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.18-1
- Update to latest upstream release (closes rhbz#2324125)

* Tue Oct 29 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.15-1
- Update to latest upstream release

* Fri Oct 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.14-1
- Update to latest upstream release (closes rhbz#2319572)

* Thu Oct 10 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.13-1
- Update to latest upstream release (closes rhbz#2317723)

* Mon Oct 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.12-1
- Update to latest upstream release

* Wed Oct 02 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.11-1
- Update to latest upstream release (closes rhbz#2315800)

* Thu Sep 26 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.10-1
- Update to new upstream version (closes rhbz#2018379)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.9-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.9-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.9-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.9-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.9-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Carl George <carl@george.computer> - 0.2.9-1
- Latest upstream

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.8-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Carl George <carl@george.computer> - 0.2.8-1
- Latest upstream

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Carl George <carl@george.computer> - 0.2.6-2
- Improve patch0

* Tue Apr 16 2019 Carl George <carl@george.computer> - 0.2.6-1
- Latest upstream

* Thu Feb 14 2019 Carl George <carl@george.computer> - 0.2.5-1
- Latest upstream

* Tue Feb 12 2019 Carl George <carl@george.computer> - 0.2.4-1
- Initial package
