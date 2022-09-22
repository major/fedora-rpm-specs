%bcond_with tests

Name: upt
Version:  0.10.3
Release:  13%{?dist}
Summary:  Package software from any package manager to any distribution

License:  BSD
URL:      https://framagit.org/upt/upt
Source0:  %pypi_source
BuildArch:  noarch
# setuptools 40.6 added section [options.data_files]to setup.cfg. Having 
# setuptools < 40.6 results in this error upon trying to install a Python 
# package:
# distutils.errors.DistutilsOptionError: Unsupported distribution option section
# el7 and el8 come with version 39.2
%if 0%{?rhel}
Patch0:    remove-options_data_files.patch
Requires: python%{python3_pkgversion}-spdx-lookup
Requires: python%{python3_pkgversion}-packaging
%endif
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
%if 0%{?fedora} || 0%{?rhel_version} >= 8
Recommends: python%{python3_pkgversion}-upt-fedora
Recommends: python%{python3_pkgversion}-upt-pypi
Recommends: python%{python3_pkgversion}-upt-cpan
Recommends: python%{python3_pkgversion}-upt-rubygems
%endif

%description
A unified CLI tool that converts a package from a language-specific package
manager (such as PyPI or NPM) to an almost ready-to-use package for Free
Unix-based operating systems (such as a GNU/Linux distribution or *BSD).

%prep
%setup -q -n %{name}-%{version}
%if 0%{?rhel}
%patch0 -p0
%endif

%build
%py3_build

%install
%py3_install
%{__install} -d %{buildroot}%{_mandir}/man1
%{__cp} upt.1 %{buildroot}%{_mandir}/man1/

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m unittest
%endif

%files
%doc README.md CHANGELOG
%license LICENSE
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/
%{_bindir}/upt
%{_mandir}/man1/upt*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10.3-12
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10.3-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.3-6
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Jeremy Bertozzi <jeremy.bertozzi@gmail.com> - 0.10.3-4
- Bump release due to weird state in Koji

* Sun Dec 22 2019 Jeremy Bertozzi <jeremy.bertozzi@gmail.com> - 0.10.3-3
- Add missing requires for rhel7

* Sun Oct 20 2019 Jeremy Bertozzi <jeremy.bertozzi@gmail.com> - 0.10.3-2
- Build for rhel

* Sun Sep 29 2019 Jeremy Bertozzi <jeremy.bertozzi@gmail.com> - 0.10.3-1
- Initial package

