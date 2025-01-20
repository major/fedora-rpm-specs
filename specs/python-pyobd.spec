%global srcname pyobd
%global ver_major 0
%global ver_minor 9
%global ver_patch 3
%global ver %{ver_major}.%{ver_minor}.%{ver_patch}

Name:           python-%{srcname}
Version:        %{ver}
Release:        36%{?dist}
Summary:        OBD-II (SAE-J1979) compliant scan tool software
# CC-BY-SA for icon, see README.Fedora for details
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
# contact for patches: support@secons.com
# upstream refuses patches to support "Chinese" ELM32X
URL:            http://www.obdtester.com/
Source0:        http://www.obdtester.com/download/%{srcname}_%{ver_major}.%{ver_minor}.%{ver_patch}.tar.gz
Source1:        pyobd-icon.svg
Source2:        README.Fedora
BuildArch:      noarch
# import from pyobd module
Patch0:         python-pyobd-0.9.3-pyobd-module.patch
Patch1:         python-pyobd-0.9.3-invalid-device-traceback-fix.patch
Patch2:         python-pyobd-0.9.3-configure-dialog-traceback-fix.patch
# part of the patch provided by Lumír Balhar <lbalhar@redhat.com>
Patch3:         python-pyobd-0.9.3-python3.patch
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix, ImageMagick

%global _description \
pyOBD is an OBD-II (SAE-J1979) compliant scan tool software written \
entirely in Python. It is meant to interface with the low cost ELM 32x \
devices such as ELM-USB.

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel, python3-wxpython4
Provides:       pyobd = %{ver}
Obsoletes:      pyobd < 0.9.3-7
Requires:       python3-pyserial, python3-wxpython4, hicolor-icon-theme

%description -n python3-%{srcname}
%{_description}

Python 3 version of the pyOBD.

%prep
%setup -q -n %{srcname}-%{ver_major}.%{ver_minor}.%{ver_patch}

cp -p %{SOURCE2} README.Fedora

# convert CR/LF to LF
dos2unix pyobd.desktop
# fix encoding settings
sed -i '/Encoding=/ s|UTF8|UTF-8|' pyobd.desktop
# change icon in pyobd.desktop
sed -i 's|/usr/share/pyobd/pyobd.gif|pyobd|' pyobd.desktop
# create dummy module init
[ -f __init__.py ] || echo '# module init' > __init__.py

# remove hashbangs
for f in *.py
do
  sed -i '/^[ \t]*#!\/usr\/bin\/env/ d' $f
done

# fix hashbang
sed -i '1 s|/usr/bin/env python|%{__python3}|' pyobd

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 pyobd %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{python3_sitelib}/%{srcname}
install -pm 0644 -t %{buildroot}%{python3_sitelib}/%{srcname} *.py

# icon
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/pyobd.svg

# desktop file
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --add-category="Utility" \
  --dir=%{buildroot}%{_datadir}/applications \
  pyobd.desktop

%files -n python3-%{srcname}
%license COPYING
%doc README.Fedora
%{_datadir}/icons/hicolor/scalable/apps/%{srcname}.svg
%{_datadir}/applications/pyobd.desktop
%{python3_sitelib}/pyobd/
%{_bindir}/pyobd

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.3-35
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.9.3-33
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 0.9.3-29
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.9.3-26
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.3-23
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov  8 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-18
- Switched to python3
  Resolves: rhbz#1738099

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-16
- Fixed configure dialog traceback
- Unified names of patches

* Mon Mar 25 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-15
- Fixed requires
  Resolves: rhbz#1692145

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug  9 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-13
- Dropped ownership of icon directories
  Resolves: rhbz#1607835

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.3-10
- Remove obsolete scriptlets

* Mon Jan 15 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-9
- Added license for icon
  Resolves: rhbz#1534147

* Fri Nov  3 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-8
- Fixed according to re-review
  Resolves: rhbz#1481645

* Tue Aug 15 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-7
- Renamed to be compliant with Fedora Packaging Guidelines
  Resolves: rhbz#1471175

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-3
- Fixed exception if device cannot be opened
  Resolves: rhbz#1231476

* Tue Mar 22 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-2
- New SVG icon

* Fri Feb 19 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.3-1
- New version
  Resolves: rhbz#1310008

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.2.2-1
- Initial release
