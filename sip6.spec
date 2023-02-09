%global pypi_name sip

Name:           sip6
Version:        6.7.7
Release:        1%{?dist}
Summary:        SIP - Python/C++ Bindings Generator
%py_provides    python3-sip6

# code_generator/parser.{c.h} is GPLv2+ with exceptions (bison)
License:        (GPLv2 or GPLv3) and (GPLv2+ with exceptions)
URL:            https://www.riverbankcomputing.com/software/sip
Source0:        %{pypi_source}

BuildRequires:  gcc
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
%{python3_sitearch}/sip-*
%{python3_sitearch}/sipbuild/

%changelog
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
