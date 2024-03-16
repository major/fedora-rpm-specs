%global pypi_name sip

Name:           sip6
Version:        6.8.3
Release:        2%{?dist}
Summary:        SIP - Python/C++ Bindings Generator
%py_provides    python3-sip6

License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.riverbankcomputing.com/software/sip
Source0:        %{pypi_source}

# Workaround hang/OOM kill in Python 3.13, avoid calling list.remove() in try-except.
# See commit message in the patch for details.
Patch:          Workaround-hang-OOM-kill-in-Python-3.13.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
SIP is a collection of tools that makes it very easy to create Python bindings
for C and C++ libraries.  It was originally developed in 1998 to create PyQt,
the Python bindings for the Qt toolkit, but can be used to create bindings for
any C or C++ library.  For example it is also used to generate wxPython, the
Python bindings for wxWidgets.}

%description %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%py3_check_import sipbuild sipbuild.distinfo sipbuild.module sipbuild.tools


%files
%doc README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{_bindir}/sip*
%{python3_sitelib}/sip-*
%{python3_sitelib}/sipbuild/

%changelog
* Thu Mar 14 2024 Miro Hrončok <mhroncok@redhat.com> - 6.8.3-2
- Workaround hang/OOM kill in Python 3.13

* Wed Feb 21 2024 Scott Talbert <swt@techie.net> - 6.8.3-1
- Update to new upstream release 6.8.3 (#2263494)

* Mon Feb 12 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.2-2
- Rebuild (fixed SPDX license)

* Thu Jan 25 2024 Scott Talbert <swt@techie.net> - 6.8.2-1
- Update to new upstream release 6.8.2 (#2252260)

* Mon Oct 16 2023 Jan Grulich <jgrulich@redhat.com> - 6.7.12-1
- 6.7.12

* Wed Aug 02 2023 Scott Talbert <swt@techie.net> - 6.7.11-1
- Update to new upstream release 6.7.11 (#2225117)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 6.7.9-2
- Rebuilt for Python 3.12

* Wed Apr 26 2023 Scott Talbert <swt@techie.net> - 6.7.9-1
- Update to new upstream release 6.7.9 (#2185559)

* Tue Feb 07 2023 Scott Talbert <swt@techie.net> - 6.7.7-1
- Update to new upstream release 6.7.7 (#2167385)

* Tue Jan 31 2023 Scott Talbert <swt@techie.net> - 6.7.6-1
- Update to new upstream release 6.7.6 (#2165207)
- Modernize python packaging

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Scott Talbert <swt@techie.net> - 6.7.5-1
- Update to new upstream release 6.7.5 (#2131647)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Scott Talbert <swt@techie.net> - 6.6.2-1
- Update to new upstream release 6.6.2 (#2074712)

* Wed Jun 15 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 6.5.1-3
- Add patch for Python 3.11 compatibility

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.5.1-2
- Rebuilt for Python 3.11

* Fri Feb 18 2022 Scott Talbert <swt@techie.net> - 6.5.1-1
- Update to new upstream release 6.5.1 (#2049172)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Scott Talbert <swt@techie.net> - 6.5.0-1
- Update to new upstream release 6.5.0 (#2028405)

* Sat Oct 30 2021 Scott Talbert <swt@techie.net> - 6.4.0-1
- Update to new upstream release 6.4.0 (#2018175)

* Wed Oct 13 2021 Scott Talbert <swt@techie.net> - 6.3.1-1
- Update to new upstream release 6.3.1 (#2013781)

* Tue Oct 12 2021 Scott Talbert <swt@techie.net> - 6.3.0-1
- Update to new upstream release 6.3.0 (#2013274)

* Mon Oct 04 2021 Scott Talbert <swt@techie.net> - 6.2.0-1
- Update to new upstream release 6.2.0 (#2010059)

* Wed Aug 04 2021 Scott Talbert <swt@techie.net> - 6.1.1-3
- Fix handling of Unicode docstrings

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Scott Talbert <swt@techie.net> - 6.1.1-1
- Initial package.
