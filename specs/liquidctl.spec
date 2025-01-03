Name: liquidctl
%global pypi_name %{name}

Summary: Tool for controlling liquid coolers, case fans and RGB LED strips
License: GPL-3.0-or-later

Version: 1.14.0
Release: 1%{?dist}

URL: https://github.com/jonasmalacofilho/liquidctl
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros

# i2c-tools are unavailable on s390{,x}
ExcludeArch: s390 s390x

# Require the python libs in the main package
Requires: python3-%{name} = %{version}-%{release}
# Suggest installing the -udev subpackage
Suggests: %{name}-udev = %{version}-%{release}


%description
liquidctl is a tool for controlling various settings of PC internals, such as:
- liquid cooler pump speed
- case fan speed
- RGB LED strip colors

For a full list of supported devices, visit:
https://github.com/liquidctl/liquidctl#supported-devices


%package -n python3-%{name}
Summary: Module for controlling liquid coolers, case fans and RGB LED devices

%description -n python3-%{name}
A python module providing classes for communicating with various cooling devices
and RGB LED solutions.

Currently supported devices are: %{supported_devices}

Devices with experimental support: %{supported_devices_experimental}


%package udev
Summary: Unprivileged device access rules for %{name}
Requires: %{name} = %{version}-%{release}

%description udev
This package contains udev rules which allow %{name} to access relevant devices
when ran by an unprivileged user.


%package doc
Summary: Documentation for %{name}

%description doc
This package contains documentation for %{name}, including
device-specific guides and developer docs.


%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -t


%build
export DIST_NAME=$(source /etc/os-release && echo "${NAME} ${VERSION_ID}")
export DIST_PACKAGE="%{name}-%{version}-%{release}.%{_build_arch}"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}

install -Dp -m 644 \
	liquidctl.8 \
	%{buildroot}%{_mandir}/man8/%{name}.8

install -Dp -m 644 \
	extra/completions/liquidctl.bash \
	%{buildroot}%{_datadir}/bash-completion/completions/%{name}

install -Dp -m 644 \
	extra/linux/71-%{name}.rules \
	%{buildroot}%{_udevrulesdir}/71-%{name}.rules

install -Dp -m 644 -t %{buildroot}%{_pkgdocdir} \
	CHANGELOG.md README.md
cp -a docs/ %{buildroot}%{_pkgdocdir}/


%check
mkdir ./test-run-dir
XDG_RUNTIME_DIR=$(pwd)/test-run-dir pytest-3


%files
%doc %{_pkgdocdir}/*.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.*
%{_datadir}/bash-completion/completions/%{name}

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE.txt

%files udev
%{_udevrulesdir}/71-%{name}.rules

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/docs


%changelog
* Wed Jan 01 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.14.0-1
- Update to v1.14.0
- Drop Patch0 (test failures - backported from this release)
- Drop Patch1 (kernel 6.11+ issues - backported from this release)

* Sat Nov 23 2024 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.13.0-7
- Add patch for issues with kernel +6.11

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.13.0-5
- Rebuilt for Python 3.13

* Fri Feb 16 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.13.0-4
- Add a patch to fix broken tests (rhbz#2261352)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.13.0-1
- Update to v1.13.0

* Mon Jul 24 2023 Python Maint <python-maint@redhat.com> - 1.12.1-4
- Rebuilt for Python 3.12

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.12.1-1
- Update to v1.12.1

* Sun Jan 08 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.12.0-1
- Update to v1.12.0
- Migrate License tag to SPDX

* Thu Oct 20 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.11.1-1
- Update to v1.11.1

* Sun Oct 16 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.11.0-1
- Update to v1.11.0
- Remove supported device list from package description
- Move documentation to -doc sub-package

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.0-1
- Update to v1.10.0

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.9.1-2
- Rebuilt for Python 3.11

* Wed Apr 06 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.9.1-1
- Update to v1.9.1

* Tue Apr 05 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.9.0-1
- Update to v1.9.0
- Switch to downloading sources from PyPi
- Switch to using pyproject macros instead of py3_build/py3_install

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.8.0-1
- Update to v1.8.0

* Wed Oct 06 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.2-1
- Update to latest upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.1-1
- Update to latest upstream release

* Wed Jul 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.0-1
- Update to latest upstream release
- Add the "udev" subpackage
- Drop Patch0 (doctest failures) - python3.10-specific, fixed in Fedora

* Wed Jun 16 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.6.1-3
- Add a patch to fix test failures (fixes rhbz#1948499)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.1-2
- Rebuilt for Python 3.10

* Sat May 01 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.6.1-1
- Update to latest upstream release

* Thu Apr 08 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.6.0-1
- Update to latest upstream release
- Include the bash completion file

* Sun Feb 28 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.5.1-1
- Update to latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.4.2-1
- Update to latest upstream release

* Sat Aug 08 2020 Artur Iwicki <fedora@svgames.pl> - 1.4.1-1
- Update to latest upstream release

* Fri Jul 31 2020 Artur Iwicki <fedora@svgames.pl> - 1.4.0-1
- Update to latest upstream release
- Add a check section (upstream added a test suite)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Artur Iwicki <fedora@svgames.pl> - 1.3.3-1
- Update to latest upstream release
- Update the list of supported devices in package description

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Artur Iwicki <fedora@svgames.pl> - 1.3.2-1
- Update to latest upstream release
- Preserve timestamp for the man page

* Mon Nov 18 2019 Artur Iwicki <fedora@svgames.pl> - 1.3.0-1
- Update to latest upstream release

* Sun Nov 03 2019 Artur Iwicki <fedora@svgames.pl> - 1.3.0-0.1rc1
- Update to latest upstream release candidate

* Sat Sep 28 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-1
- Update to latest upstream release
- Update the list of supported devices in package description

* Thu Sep 19 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-0.7rc4
- Update to latest upstream release candidate

* Sun Sep 15 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-0.6rc3
- Update to latest upstream release candidate

* Thu Sep 12 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-0.5rc2
- Update to latest upstream release candidate
- Include the version+release number in "Requires: python3-liquidctl"

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-0.3rc1
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.2rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-0.1rc1
- Update to latest upstream pre-release
- Don't mention NZXT in package summary (support for other manufacturers added)
- Put the list of supported devices in a macro

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Artur Iwicki <fedora@svgames.pl> - 1.1.0-2
- Mark the package as noarch
- Split off the python libs into a python3-liquidctl subpackage
- Fix typos in summary and description

* Fri Dec 28 2018 Artur Iwicki <fedora@svgames.pl> - 1.1.0-1
- Initial packaging
