# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           python-pynest2d
Version:        4.8.0
Release:        9%{?dist}
Summary:        Python bindings for libnest2d
License:        LGPLv3
URL:            https://github.com/Ultimaker/pynest2d
Source:         %{url}/archive/%{version}/pynest2d-%{version}.tar.gz
# Downstream patch: add PyQt5 namespace
Patch0:         pynest2d-PyQt5.sip.patch
# Retrieve required flags from Libnest2D target
# https://github.com/Ultimaker/pynest2d/pull/3
Patch1:         Retrieve-required-flags-from-Libnest2D-target.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libnest2d-static
BuildRequires:  python3-devel
BuildRequires:  python3-sip-devel < 5
BuildRequires:  python3-pyqt5-sip
Requires:       python3-pyqt5-sip

# we add a dependency on setuptools to provide the distutils module
# upstream already removed the distutils usage in version 5+
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)

%description
Binding allowing libnest2d to be called from Python using NumPy.

%package -n python3-pynest2d
Summary:        %{summary}

%description -n python3-pynest2d
Binding allowing libnest2d to be called from Python using NumPy.


%prep
%autosetup -n pynest2d-%{version} -p1

# Boost 1.75+ needs C++14, upstream: https://github.com/Ultimaker/pynest2d/pull/7
sed -i 's/CMAKE_CXX_STANDARD 11/CMAKE_CXX_STANDARD 14/' CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install


%files -n python3-pynest2d
%license LICENSE
%doc README.md
%{python3_sitearch}/pynest2d.so


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 4.8.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.8.0-4
- Rebuilt for Python 3.10

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 4.8.0-3
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Miro Hrončok <mhroncok@redhat.com> - 4.8.0-1
- Initial package adapted from SUSE (by Stefan Brüns <stefan.bruens@rwth-aachen.de>)
