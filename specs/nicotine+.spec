%global altname nicotine
%global appdata_id org.nicotine_plus.Nicotine

Name:           nicotine+
Version:        3.3.7
Release:        1%{?dist}
Summary:        A graphical client for Soulseek

# - pynicotine/external/ip2location.py and pynicotine/external/tinytag.py are
#   MIT
# - IP2Location Country Database (pynicotine/external/ipcountrydb.bin) is
#   CC-BY-SA-4.0 (see pynicotine/external/README.md)
License:        GPL-3.0-or-later AND MIT AND CC-BY-SA-4.0
URL:            https://nicotine-plus.github.io/nicotine-plus/
Source0:        https://github.com/nicotine-plus/nicotine-plus/archive/%{version}/%{name}-%{version}.tar.gz
# - Disable tests requiring an Internet connection
# - Disable metadata tests because they fail on Koji builders, while they pass
#   locally with mock (builder architecture? SELinux issues?)
Patch0:         %{name}-3.3.4-tests.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
# Needed for tests
BuildRequires:  gtk4
# Runtime dependencies are not declared in setup.py (except pygobject) but are
# actually required (see doc/DEPENDENCIES.md)
Requires:       gspell
Requires:       (gtk4 or gtk3)
Requires:       hicolor-icon-theme
# pynicotine/external/ip2location.py is a bundled fork of
# https://pypi.org/project/IP2Location/
Provides:       bundled(python3dist(ip2location))
# pynicotine/external/tinytag.py is a bundled fork of
# https://pypi.org/project/tinytag/
Provides:       bundled(python3dist(tinytag))
BuildArch:      noarch

%description
Nicotine+ is a graphical client for the Soulseek peer-to-peer file sharing
network. It is an attempt to keep Nicotine working with the latest libraries,
kill bugs, keep current with the Soulseek protocol, and add some new features
that users want and/or need.


%prep
%autosetup -n nicotine-plus-%{version} -p0


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pynicotine


%check
%python3 -m unittest

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{appdata_id}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{appdata_id}.appdata.xml


%files -f %{pyproject_files}
%doc AUTHORS.md NEWS.md README.md
%license COPYING
%{_bindir}/%{altname}
%{_datadir}/applications/%{appdata_id}.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/%{appdata_id}.appdata.xml
%{_mandir}/man1/%{altname}.1.*


%changelog
* Sat Jan 25 2025 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.7-1
- Update to 3.3.7

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 28 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.6-1
- Update to 3.3.6

* Sun Oct 13 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.5-1
- Update to 3.3.5

* Fri Aug 23 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.4-4
- Fix FTBFS on Fedora >= 41 (RHBZ #2300994)
- Add bundled Provides
- Fix license

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.3.4-2
- Rebuilt for Python 3.13

* Wed May 08 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.4-1
- Update to 3.3.4

* Sun Feb 25 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Sun Feb 25 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 3.2.9-2
- Rebuilt for Python 3.12

* Sun Mar 26 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.9-1
- Update to 3.2.9

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.8-1
- Update to 3.2.8

* Thu Dec 01 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.7-1
- Update to 3.2.7

* Mon Oct 24 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.6-1
- Update to 3.2.6

* Sat Sep 03 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.5-1
- Update to 3.2.5

* Tue Aug 09 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.4-1
- Update to 3.2.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2.2-2
- Rebuilt for Python 3.11

* Sun Mar 20 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.2-1
- Update to 3.2.2

* Fri Feb 18 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Mon Aug 02 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Sun Jul 25 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.6-2
- Rebuilt for Python 3.10

* Thu Jun 03 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.6-1
- Update to 3.0.6

* Mon Apr 12 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.4-1
- Update to 3.0.4

* Thu Apr 01 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.3-1
- Update to 3.0.3

* Mon Mar 01 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Sun Feb 28 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Mon Feb 15 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Sat Dec  5 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.0-2
- Remove useless dependency on xdg-utils

* Sat Dec  5 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- Update License tag

* Tue Oct 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Sun Sep 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1
- Update License tag

* Sat Sep 12 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.1-1
- Initial RPM release
