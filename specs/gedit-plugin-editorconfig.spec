# Disable debuginfo generation — this is not a noarch package only because
# the gedit plugin directory is arch-dependent, so despite having no arch
# components this package will need to install in the arch-dependent libdir.
%global debug_package %{nil}

Name:           gedit-plugin-editorconfig
Version:        0.5.3
Release:        18%{?dist}
Summary:        EditorConfig plugin for Gedit

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://editorconfig.org/
Source0:        https://github.com/editorconfig/editorconfig-gedit/archive/v%{version}/editorconfig-gedit-%{version}.tar.gz

# Patch to avoid tracebacks due to GeditDocument.newline-type being
# deprecated and replaced with a read-only GtkSourceFile.newline-type
#
# Submitted upstream: https://github.com/editorconfig/editorconfig-gedit/pull/23
Patch1:         gedit-newlinetype-deprecated.patch

# Submitted upstream: https://github.com/editorconfig/editorconfig-gedit/pull/25
Patch2:         gedit-3.36-location-api.patch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
Requires:       python%{python3_pkgversion}-editorconfig
Requires:       gedit%{_isa} >= 3.14

%description
EditorConfig helps maintain consistent coding styles for multiple developers
working on the same project across various editors and IDEs. The EditorConfig
project consists of a file format for defining coding styles and a collection of
text editor plugins that enable editors to read the file format and adhere to
defined styles. EditorConfig files are easily readable and they work nicely with
version control systems.

This package contains the EditorConfig plugin for GEdit.

%prep
%autosetup -p1 -n editorconfig-gedit-%{version}


%build
sed -i -e 's|^Loader=python$|Loader=python3|' editorconfig.plugin


%install
mkdir -p %{buildroot}%{_libdir}/gedit/plugins/
cp -rL editorconfig_plugin %{buildroot}%{_libdir}/gedit/plugins/
cp editorconfig.plugin %{buildroot}%{_libdir}/gedit/plugins/
cp editorconfig_gedit3.py %{buildroot}%{_libdir}/gedit/plugins/

# Manually byte-compile the python files in the plugin dir
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gedit/plugins/editorconfig_plugin


%files
%license LICENSE
%doc README.md
%{_libdir}/gedit/plugins/editorconfig.plugin
%{_libdir}/gedit/plugins/editorconfig_gedit3.py
%dir %{_libdir}/gedit/plugins/editorconfig_plugin
%{_libdir}/gedit/plugins/editorconfig_plugin/*.py
%{_libdir}/gedit/plugins/editorconfig_plugin/__pycache__/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.3-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.5.3-9
- Raise gedit minimum version to match API patches applied
- Build for EL8 and EL9, now that python-editorconfig will be available

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.5.3-5
- Add setuptools build requirement

* Fri Jun 05 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.5.3-4
- Patch around gedit 3.36 get_location() API change

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.5.3-2
- Add patch to handle deprecated 'newline-type' gracefully

* Mon Sep 30 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.5.3-1
- Initial Fedora package
