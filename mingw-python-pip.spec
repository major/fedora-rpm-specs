%{?mingw_package_header}

%global pypi_name pip

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       22.3.1
Release:       1%{?dist}
BuildArch:     noarch


# We bundle a lot of libraries with pip, which itself is under MIT license.
# Here is the list of the libraries with corresponding licenses:

# MIT:
# - LICENSE.txt: MIT
# - pep517/LICENSE: MIT
# - pkg_resources/LICENSE: MIT
# - platformdirs/LICENSE.txt: MIT
# - pyparsing/LICENSE: MIT
# - rich/LICENSE: MIT
# - tomli/LICENSE: MIT
# - urllib3/LICENSE.txt: MIT
# CNRI-Python-GPL-Compatible:
# - distlib/LICENSE.txt: CNRI-Python-GPL-Compatible
# Apache-2.0:
# - cachecontrol/LICENSE.txt: Apache-2.0
# - distro/LICENSE: Apache-2.0
# - requests/LICENSE: Apache-2.0
# - tenacity/LICENSE: Apache-2.0
# BSD-2-Clause:
# - pygments/LICENSE: BSD-2-Clause
# BSD-3-Clause:
# - colorama/LICENSE.txt: BSD-3-Clause
# - idna/LICENSE.md: BSD-3-Clause
# - webencodings/LICENSE: BSD-3-Clause
# ISC:
# - resolvelib/LICENSE: ISC
# LGPL-2.1+:
# - chardet/LICENSE: LGPL-2.1+
# MPL-2.0:
# - certifi/LICENSE: MPL-2.0
# Apache-2.0 or BSD-2-Clause:
# - packaging/LICENSE.APACHE: Apache-2.0
# - packaging/LICENSE.BSD: BSD-2-Clause
License:       MIT and CNRI-Python-GPL-Compatible and Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and LGPL-2.1+ and MPL-2.0 and (Apache-2.0 or BSD-2-Clause)
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:       %{pypi_source}
# Handle sysconfig.get_platform() = mingw
Patch0:        pip-platform-mingw.patch

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
%{mingw32_bindir}/pip%{mingw32_python3_version}
%endif
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%license vendor_licenses
%if %{without bootstrap}
%{mingw64_bindir}/pip
%{mingw64_bindir}/pip3
%{mingw64_bindir}/pip%{mingw64_python3_version}
%endif
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
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
