Name: liquidctl
%global pypi_name %{name}

Summary: Tool for controlling liquid coolers, case fans and RGB LED strips
License: GPLv3+

Version: 1.10.0
Release: 2%{?dist}

URL: https://github.com/jonasmalacofilho/liquidctl
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires: python3-colorlog
BuildRequires: python3-devel
BuildRequires: python3-docopt
# Upstream doesn't specify any version requirement,
# but the test suite fails with 0.7.99.post20
BuildRequires: python3-hidapi >= 0.9.0
BuildRequires: python3-i2c-tools
BuildRequires: python3-pytest
BuildRequires: python3-pyusb
BuildRequires: python3-setuptools
BuildRequires: systemd-rpm-macros

# i2c-tools are unavailable on s390{,x}
ExcludeArch: s390 s390x

%{?python_enable_dependency_generator}

# Require the python libs in the main package
Requires: python3-%{name} = %{version}-%{release}
# Suggest installing the -udev subpackage
Suggests: %{name}-udev = %{version}-%{release}


%global supported_devices \
- ASUS Strix GTX 1050 OC, Ti OC \
- ASUS Strix GTX 1060, OC \
- ASUS Strix GTX 1070, OC, Ti, Ti Advanced \
- ASUS Strix GTX 1080, OC, Ti, Ti OC, Advanced \
- ASUS Strix GTX 1650 Super OC \
- ASUS Strix GTX 1660 Super OC, Ti OC \
- ASUS Strix GTX 2060 Evo, Evo OC, OC \
- ASUS Strix GTX 2060 Super Advanced, Super Evo Advanced, Super OC \
- ASUS Strix GTX 2070 Advanced, OC \
- ASUS Strix GTX 2070 Super Advanced, Super OC \
- ASUS Strix GTX 2080 OC, Super Advanced, Super OC, Ti, Ti OC \
- ASUS TUF RTX 3060 Ti OC \
- Corsair Commander Pro \
- Corsair Lighting Node Core, Pro \
- Corsair HX750i, HX850i, HX1000i, HX1200i \
- Corsair RM650i, RM750i, RM850i, RM1000i \
- Corsair Hydro v2 H80i, H100i, H115i \
- Corsair Hydro Pro H100i, H115i, H150i \
- Corsair Hydro Platinum H100i, H100i SE, H115i \
- Corsair Hydro Pro XT H60i, H100i, H115i, H150i \
- Corsair Obsidian 1000D \
- Corsair Vengeance RGB RAM \
- EVGA CLC 120 (CL12), 240, 280, 360 \
- EVGA GTX 1070 FTW, 1070 FTW DT Gaming, 1070 FTW Hybrid \
- EVGA GTX 1070 Ti FTW2 \
- EVGA GTX 1080 FTW \
- Gigabyte RGB Fusion 2.0 motherboards \
- NZXT E500, E650, E850 \
- NZXT Grid+ V3 \
- NZXT HUE 2, HUE 2 Ambient \
- NZXT RGB & Fan Controller \
- NZXT Smart Device, Smart Device v2 \
- NZXT Kraken M2 \
- NZXT Kraken X31, X41, X42, X52, X53, X61, X62, X63, X72, X73 \
- NZXT Kraken Z53, Z63, Z73 \

%global supported_devices_experimental \
- ASUS Aura LED motherboards \
- Corsair Commander Core \
- Corsair Hydro GT/GTX H80i, H100i, H110i \
- Corsair iCUE Elite Capellix H100i, H115i, H150i \
- NZXT Kraken X40, X60 \

%description
liquidctl is a tool for controlling various settings of PC internals, such as:
- liquid cooler pump speed
- case fan speed
- RGB LED strip colors

Currently supported devices are: %{supported_devices}

Devices with experimental support: %{supported_devices_experimental}


%package -n python3-%{name}
Summary: Module for controlling liquid coolers, case fans and RGB LED devices
BuildArch: noarch

%description -n python3-%{name}
A python module providing classes for communicating with various cooling devices
and RGB LED solutions.

Currently supported devices are: %{supported_devices}

Devices with experimental support: %{supported_devices_experimental}


%package udev
Summary: Unprivileged device access rules for %{name}

BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description udev
This package contains udev rules which allow %{name} to access relevant devices
when ran by an unprivileged user.


%prep
%setup -q -n %{name}-%{version}

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


%check
mkdir ./test-run-dir
XDG_RUNTIME_DIR=$(pwd)/test-run-dir pytest-3


%files
%doc CHANGELOG.md README.md
%doc docs/
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.*
%{_datadir}/bash-completion/completions/%{name}

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE.txt

%files udev
%{_udevrulesdir}/71-%{name}.rules


%changelog
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
