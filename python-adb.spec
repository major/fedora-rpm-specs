%global pypi_name adb

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        13%{?dist}
Summary:        Python implementation of the Android ADB and Fastboot protocols

License:        ASL 2.0
URL:            https://github.com/google/python-adb
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# Replace M2Crypto with py-cryptography
Patch0:         %{url}/commit/4b555e64d1e49d91ed851c59bb11b734b302f71d.patch
BuildArch:      noarch

%description
This module contains a pure Python implementation of the Android ADB and
Fastboot protocols, using libusb1 for USB communications.This is a complete
replacement and rearchitecture of the Android project's ADB and fastboot code
available at code is mainly targeted to users that need to communicate with
Android devices in an automated fashion, such as in automated testing.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-libusb1
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module contains a pure Python implementation of the Android ADB and
Fastboot protocols, using libusb1 for USB communications. This is a complete
replacement and rearchitecture of the Android project's ADB and fastboot code
available at code is mainly targeted to users that need to communicate with
Android devices in an automated fashion, such as in automated testing.

%prep
%autosetup -n %{name}-%{version} -p 1
rm -rf %{pypi_name}.egg-info
# Remove shebang
sed -i -e '/^#!\//, 1d' {adb/adb_debug.py,adb/fastboot_debug.py}

%build
%py3_build

%install
%py3_install

# https://github.com/google/python-adb/pull/174
#%check
#%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/pyadb
%{_bindir}/pyfastboot
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.0-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 1.3.0-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-3
- Add patch for py-cryptography

* Sun Apr 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-2
- Fix requirements (rhbz#1815091)

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Initial package for Fedora
