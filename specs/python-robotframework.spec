%global srcname robotframework

Name:           python-%{srcname}
Version:        7.1.1
Release:        2%{?dist}
Summary:        Generic automation framework for acceptance testing and RPA
# Robot Framework is licensed as Apache-2.0
# Support libraries to display HTML results:
#  - jQuery, jQuery Highlight plugin: MIT
#  - jQuery Tablesorter, jQuery Templates plugin: MIT or GPLv2
#  - JSXCompressor: Apache-2.0 or LGPLv3
#  - OpenIconic icons (as base64): MIT
License:        Apache-2.0 and MIT
URL:            https://github.com/robotframework/robotframework
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-jsonschema


%global _description %{expand:
Robot Framework is a generic open source automation framework for acceptance
testing, acceptance test driven development (ATDD), and robotic process
automation (RPA).
It has simple plain text syntax and it can be extended easily with libraries
implemented using Python or Java.}


%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

# Bundled JavaScript for reports
Provides:      bundled(jquery) = 3.5.1
Provides:      bundled(jquery-highlight)
Provides:      bundled(jquery-tablesorter) = 2.30.5
Provides:      bundled(jquery-templates) = 1.0.0pre
Provides:      bundled(jsxcompressor)

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p 1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files robot


%check
%{python3} utest/run.py


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst BUILD.rst INSTALL.rst CONTRIBUTING.rst
%license LICENSE.txt
%{_bindir}/{robot,rebot,libdoc}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 27 2024 Federico Pellegrin <fede@evolware.org> - 7.1.1-1
- Upgrade to 7.1.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Federico Pellegrin <fede@evolware.org> - 7.0.1-1
- Upgrade to 7.0.1, remove now upstreamed patch for 3.13 tests

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 7.0-3
- Rebuilt for Python 3.13

* Sun Jan 28 2024 Federico Pellegrin <fede@evolware.org> - 7.0-2
- Fix test on Python 3.13 (resolves rhbz#2259549)

* Wed Jan 24 2024 Federico Pellegrin <fede@evolware.org> - 7.0-1
- Upgrade to 7.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 01 2023 Federico Pellegrin <fede@evolware.org> - 6.1.1-1
- Upgrade to 6.1.1

* Thu Jul 27 2023 Federico Pellegrin <fede@evolware.org> - 6.1-1
- Upgrade to 6.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 6.0.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Federico Pellegrin <fede@evolware.org> - 6.0.2-1
- Upgrade to 6.0.2

* Sun Nov 06 2022 Federico Pellegrin <fede@evolware.org> - 6.0.1-1
- Upgrade to 6.0.1

* Sun Oct 30 2022 Federico Pellegrin <fede@evolware.org> - 6.0-1
- Upgrade to 6.0
- Drop now upstreamed patch for Python 3.11

* Tue Oct 04 2022 Federico Pellegrin <fede@evolware.org> - 5.0.1-6
- Improve spec file after package review (jquery bundling)

* Fri Sep 30 2022 Federico Pellegrin <fede@evolware.org> - 5.0.1-5
- Improve spec file after package review

* Wed Sep 28 2022 Federico Pellegrin <fede@evolware.org> - 5.0.1-4
- Improve spec file after package review

* Fri Aug 05 2022 Federico Pellegrin <fede@evolware.org> - 5.0.1-3
- Fix tests with Python 3.11

* Thu May 19 2022 Piotr Szubiakowski <pszubiak@eso.org> - 5.0.1-2
- Use pyproject_save_files macro

* Tue May 17 2022 Piotr Szubiakowski <pszubiak@eso.org> - 5.0.1-1
- Update to 5.0.1

* Fri May 13 2022 Piotr Szubiakowski <pszubiak@eso.org> - 4.1.3-2
- Adapt to Fedora Python Packaging Guidelines

* Fri Feb 18 2022 Federico Pellegrin <fede@evolware.org> - 4.1.3-1
- First packaging of robotframework
