%{?mingw_package_header}

%global pypi_name pip

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       24.3.1
Release:       2%{?dist}
BuildArch:     noarch


# We bundle a lot of libraries with pip, which itself is under MIT license.
# Here is the list of the libraries with corresponding licenses:

# appdirs: MIT
# certifi: MPL-2.0
# chardet: LGPL-2.1-only
# colorama: BSD-3-Clause
# CacheControl: Apache-2.0
# distlib: Python-2.0.1
# distro: Apache-2.0
# html5lib: MIT
# idna: BSD-3-Clause
# ipaddress: Python-2.0.1
# msgpack: Apache-2.0
# packaging: Apache-2.0 OR BSD-2-Clause
# progress: ISC
# pygments: BSD-2-Clause
# pyparsing: MIT
# pyproject-hooks: MIT
# requests: Apache-2.0
# resolvelib: ISC
# rich: MIT
# setuptools: MIT
# six: MIT
# tenacity: Apache-2.0
# truststore: MIT
# tomli: MIT
# typing-extensions: Python-2.0.1
# urllib3: MIT
# webencodings: BSD-3-Clause
License:       MIT AND Python-2.0.1 AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LGPL-2.1-only AND MPL-2.0 AND (Apache-2.0 OR BSD-2-Clause)
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


%description
MinGW Windows Python %{pypi_name} library.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Copy vendor licenses for %%license
mkdir vendor_licenses
destdir=$PWD/vendor_licenses
(cd src/pip/_vendor && find  -name 'LICENSE*' -exec install -Dp {} $destdir/{} \;)


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

# Strip shebangs from non-executable scripts
sed -i '1d' %{buildroot}%{mingw32_python3_sitearch}/pip/_vendor/distro/distro.py
sed -i '1d' %{buildroot}%{mingw64_python3_sitearch}/pip/_vendor/distro/distro.py
sed -i '1d' %{buildroot}%{mingw32_python3_sitearch}/pip/_vendor/requests/certs.py
sed -i '1d' %{buildroot}%{mingw64_python3_sitearch}/pip/_vendor/requests/certs.py


%files -n mingw32-python3-%{pypi_name}
%license LICENSE.txt
%license vendor_licenses
%if %{without bootstrap}
%{mingw32_bindir}/pip
%{mingw32_bindir}/pip3
%endif
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%license vendor_licenses
%if %{without bootstrap}
%{mingw64_bindir}/pip
%{mingw64_bindir}/pip3
%endif
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 16 2024 Sandro Mani <manisandro@gmail.com> - 24.3.1-1
- Update to 24.3.1

* Mon Aug 12 2024 Sandro Mani <manisandro@gmail.com> - 24.2-1
- Update to 24.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Sandro Mani <manisandro@gmail.com> - 24.1.1-1
- Update to 24.1.1

* Fri Mar 08 2024 Sandro Mani <manisandro@gmail.com> - 24.0-1
- Update to 24.0

* Fri Mar 08 2024 Sandro Mani <manisandro@gmail.com> - 24.0.0-1
- Update to 24.0.0

* Fri Jan 26 2024 Sandro Mani <manisandro@gmail.com> - 23.3.2-1
- Update to 23.3.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Sandro Mani <manisandro@gmail.com> - 23.3.1-1
- Update to 23.3.1

* Tue Aug 08 2023 Sandro Mani <manisandro@gmail.com> - 23.2.1-1
- Update to 23.2.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Sandro Mani <manisandro@gmail.com> - 23.1.2-1
- Update to 23.1.2

* Tue Feb 28 2023 Sandro Mani <manisandro@gmail.com> - 23.0.1-1
- Update to 23.0.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Sandro Mani <manisandro@gmail.com> - 22.3.1-1
- Update to 22.3.1

* Sat Oct 15 2022 Sandro Mani <manisandro@gmail.com> - 22.2.2-3
- Strip shebang from non-exec scripts
- Install all license files
- Use SPDX license identifiers, list full license breakup

* Tue Sep 27 2022 Sandro Mani <manisandro@gmail.com> - 22.2.2-2
- Add pip-platform-mingw.patch

* Tue Sep 27 2022 Sandro Mani <manisandro@gmail.com> - 22.2.2-1
- Initial build
