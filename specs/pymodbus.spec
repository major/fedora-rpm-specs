%global sum A Modbus Protocol Stack in Python
%global desc Pymodbus is a full Modbus protocol implementation using twisted for its \
asynchronous communications core. \
\
The library currently supports the following: \
\
Client Features \
\
    * Full read/write protocol on discrete and register \
    * Most of the extended protocol (diagnostic/file/pipe/setting/information) \
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary \
    * asynchronous(powered by twisted) and synchronous versions \
    * Payload builder/decoder utilities \
\
Server Features \
\
    * Can function as a fully implemented Modbus server \
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary \
    * asynchronous(powered by twisted) and synchronous versions \
    * Full server control context (device information, counters, etc) \
    * A number of backing contexts (database, redis, a slave device)

Name: pymodbus
Version: 3.7.4
Release: 2%{?dist}
Summary: %{sum}

License: BSD-3-Clause
URL: https://github.com/pymodbus-dev/pymodbus/
Source0: https://github.com/pymodbus-dev/pymodbus/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

%description
%{desc}


%package -n python3-%{name}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{name}}

BuildRequires: python3-devel
Requires: python3-pyserial >= 2.6

%description -n python3-%{name}
%{desc}


%prep
%autosetup -p1
# lower the version requirements for setuptools
sed -i 's/setuptools>=[^"]*"/setuptools>=62.0.0"/' pyproject.toml
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pymodbus

# delete unnecessary shebang
sed -i '/^#!\/usr\/bin\/env.*$/d' $RPM_BUILD_ROOT%{python3_sitelib}/pymodbus/server/simulator/main.py

# remove test files
rm -rf %{buildroot}%{python3_sitelib}/test

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE
%doc *.rst
%{_bindir}/pymodbus.simulator

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 13 2024 Christian Krause <chkr@fedoraproject.org> - 3.7.4-1
- Update to 3.7.4 (#2302441)
- Remove obsolete documentation of bundled pyserial-asyncio

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Christian Krause <chkr@fedoraproject.org> - 3.6.9-1
- Update to 3.6.9 (#2267692)
- Remove example client and server (upstream split the source package)
- Remove according weak requirements for example tools

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.6.4-2
- Rebuilt for Python 3.13

* Tue Feb 06 2024 Christian Krause <chkr@fedoraproject.org> - 3.6.4-1
- Update to 3.6.4 (#2253598)
- Lower version requirements for setuptools

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Christian Krause <chkr@fedoraproject.org> - 3.5.4-1
- Update to 3.5.4 (#2243568)

* Sun Sep 10 2023 Christian Krause <chkr@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2 (#2236129)
- Remove patches already applied upstream

* Sun Sep 03 2023 Christian Krause <chkr@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0 (#2236129)
- Add upstreamed patch to fix a problem running pymodbus.server
- Remove patches already applied upstream

* Sun Aug 13 2023 Christian Krause <chkr@fedoraproject.org> - 3.4.1-2
- Add upstreamed patches to fix problems running pymodbus.server
- Remove unnecessary shebang
- Remove obsolete Requires python3-pyserial-asyncio
- Migrated to SPDX license

* Fri Jul 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 3.3.2-2
- Rebuilt for Python 3.12

* Sun Jun 25 2023 Christian Krause <chkr@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2 (#2212064)
- Remove patch already applied upstream

* Sat Jun 17 2023 Christian Krause <chkr@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1 (#2212064)
- Add upstream patch for pymodbus.server
- Remove patches already applied upstream
- Remove manual installation for pymodbus.simulator, now done
  automatically
- Adjust path for shebang fix to upstream directory changes

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.2.2-3
- Rebuilt for Python 3.12

* Sun Apr 23 2023 Christian Krause <chkr@fedoraproject.org> - 3.2.2-2
- Remove unneeded setuptools requirement which causes a
  FailsToInstall problem in F39 (#2188643) (upstream removed
  it as well in their development branch)

* Fri Mar 31 2023 Christian Krause <chkr@fedoraproject.org> - 3.2.2-1
- Update spec file to latest Python packaging guidelines
- Update to 3.2.2 (#2168739)
- Install files needed for pymodbus.simulator
- Add upstream patches for pymodbus.simulator

* Tue Feb 21 2023 Christian Krause <chkr@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3 (#2168739)
- Added requirement for pymodbus.sever as Recommends to allow
  minimal installation
- Documented bundled library
- Removed unnecessary shebangs

* Sun Jan 29 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.2-1
- Update to 3.1.2

* Tue Jan 24 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Mon Jan 23 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- Update URLs for new location

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Christian Krause <chkr@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2 (#2140564)

* Sat Oct 22 2022 Christian Krause <chkr@fedoraproject.org> - 3.0.0-2
- Added a missing runtime dependency

* Sat Oct 15 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.5.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 07 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.5.3-1
- Update 2.5.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Christian Krause <chkr@fedoraproject.org> - 2.5.2-1
- Updated to the latest upstream release 2.5.2 (#1911593)
- Add BR python3-six
- Add installed binary pymodbus.server to %%files section
- Removed patch (upstream removed installation of ez_setup:
  https://github.com/riptideio/pymodbus/commit/3467d73d703c4f675465c9964887acadf5ae429a)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Christian Krause <chkr@fedoraproject.org> - 2.4.0-1
- Updated to the latest upstream release 2.4.0 (#1862735)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Christian Krause <chkr@fedoraproject.org> - 2.3.0-1
- Updated to the latest upstream release 2.3.0
- Removed patch for dependency issue (fixed upstream)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Christian Krause <chkr@fedoraproject.org> - 2.2.0-2
- Fix dependency issue (package can't be installed since a fixed
  version of python-six was required)

* Fri May 10 2019 Christian Krause <chkr@fedoraproject.org> - 2.2.0-1
- Updated to the latest upstream release 2.2.0
- Add pymodbus.console with weak requirements to allow a minimal installation

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-4
- Remove python2 subpackage (#1627381)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.7

* Sat May 05 2018 Christian Krause <chkr@fedoraproject.org> - 1.5.1-1
- Updated to the latest upstream release 1.5.1

* Thu May 03 2018 Christian Krause <chkr@fedoraproject.org> - 1.5.0-1
- Updated to the latest upstream release 1.5.0

* Thu Apr 19 2018 Christian Krause <chkr@fedoraproject.org> - 1.4.0-1
- Updated to the latest upstream release 1.4.0
- Updated patch to disable ez_setup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Tomas Hozza <thozza@redhat.com> - 1.3.1-1
- Updated project and source URL, the original was redirected
- Updated to the latest upstream release 1.3.1
- Provide Python3 version of the package
- Install LICENSE and CHANGELOG
- Removed Requires on nosetest as tests are not shipped

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 09 2015 Christian Krause <chkr@fedoraproject.org> - 1.2.0-1
- Update to new upstream release 1.2.0
- Add patch to avoid installation of ez_setup
- Change URL and Source URL
- Adjust requirements

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.0-7
- Replace the python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Christian Krause <chkr@fedoraproject.org> - 0.9.0-1
- Initial Spec file

