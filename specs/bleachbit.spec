Name:		bleachbit
Version:	6.0.0
Release:	3%{?dist}
Summary:	Remove sensitive data and free up disk space

License:	GPL-3.0-or-later
URL:		https://www.bleachbit.org/
Source:		https://github.com/bleachbit/bleachbit/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		no_update.patch
# https://github.com/bleachbit/bleachbit/issues/950
Patch1:		disable_policykit.patch

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-psutil
BuildRequires:	python3-requests
BuildRequires:	pkgconfig(systemd)

Requires:	gtk3
Requires:	python3-chardet
Requires:	python3-gobject
Requires:	python3-psutil


%description
Delete traces of your computer activity and other junk files to free
disk space and maintain privacy.

With BleachBit, you can free cache, delete cookies, clear Internet
history, shred temporary files, delete logs, and discard junk you didn't
know was there. Designed for Linux and Windows systems, it wipes clean
thousands of applications including Firefox, Internet Explorer, Adobe
Flash, Google Chrome, Opera, Safari, and many more. Beyond simply
deleting files, BleachBit includes advanced features such as shredding
files to prevent recovery, wiping free disk space to hide traces of
files deleted by other applications, and cleaning Web browser profiles
to make them run faster.


%prep
%autosetup -p1

# Disable update notifications, since package will be updated by DNF or Packagekit.
sed 's/online_update_notification_enabled = True/online_update_notification_enabled = False/g'  --in-place ./bleachbit/__init__.py
# These get installed to %%{_datadir} as non-executable files, and so shouldn't need a shebang at all.
find ./bleachbit/  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/.+$||g' --in-place '{}' +
# Replace any remaining env shebangs, or shebangs calling unversioned or unnecessarily specifically versioned Python, with plain python3.
find ./  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/usr/bin/env python3?$|#!%{_bindir}/python3|g' --in-place '{}' +
find ./  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/usr/bin/python[[:digit:][:punct:]]*$|#!%{_bindir}/python3|g' --in-place '{}' +


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

make -C po local
# Remove Windows-specific functionality.
%make_build delete_windows_files


%install
%make_install prefix=%{_prefix}

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications/ org.bleachbit.BleachBit.desktop
install -Dp org.bleachbit.BleachBit.metainfo.xml %{buildroot}/%{_metainfodir}/

%find_lang %{name}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.bleachbit.BleachBit.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.bleachbit.BleachBit.metainfo.xml
%pytest -v \
	--ignore=tests/TestWinapp.py \
	--ignore=tests/TestWindows.py \
	--ignore=tests/TestNetwork.py \
	-k 'not (test_Chaff or test_have_models or test_clean_ini_kde or test_detect_encoding or test_run_external_nowait or test_expanduser or test_make_source or test_update_url or test_update_winapp2 or test_download_url_to_fn or test_get_ip_for_url)'


%files -f %{name}.lang
%doc README* doc
%license COPYING
%{_bindir}/bleachbit
%{_datadir}/applications/org.bleachbit.BleachBit.desktop
%{_datadir}/bleachbit
%{_datadir}/pixmaps/bleachbit.png
%{_metainfodir}/org.bleachbit.BleachBit.metainfo.xml


%changelog
* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jun 20 2026 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 6.0.0-2
- Test enablement

* Sun May 24 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 6.0.0-1
- Update to v6.0.0

* Mon Mar 02 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 5.1.0-1
- Update to v5.1.0
- Remove RHEL-7 specific parts of the spec

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 4.6.0-6
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 4.6.0-5
- Rebuilt for Python 3.14.0rc2 bytecode

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 22 2024 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 28 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 4.4.2-4
* Python 3.12 fix (RHBZ #2226993)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 4.4.2-1
- Update to 4.4.2 (RHBZ #2016863)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 13 2021 Audrey Toskin <audrey@tosk.in> - 4.4.0-1
- Bump to upstream version 4.4.0, with upstream enhancements documented
  here: https://www.bleachbit.org/news/bleachbit-440

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Audrey Toskin <audrey@tosk.in> - 4.2.0-2
- Adjust package spec to build for EPEL7.

* Wed Jan 6 2021 Audrey Toskin <audrey@tosk.in> - 4.2.0-1
- Bump to upstream version 4.2.0, which, among other things, adds new
  cleaners and regular expression-based searches during deep scans.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
