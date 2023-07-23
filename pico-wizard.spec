%global snapdate 20220929
%global commit 934dbcf34e829860a0c79cad704cf4e90966587c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pico-wizard
Version:        0.1.0^git%{snapdate}.%{shortcommit}
Release:        4%{?dist}
Summary:        Post-installation configuration wizard

License:        MIT
URL:            https://invent.kde.org/plasma/pico-wizard
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

# Proposed upstream
## From https://invent.kde.org/plasma/pico-wizard/-/merge_requests/3
Patch0101:      0001-pyproject-setuptools-Put-dependencies-in-the-right-p.patch
Patch0102:      0002-files-Disable-overrides-for-PASSWORD_TYPE-and-LOGLEV.patch
## From https://invent.kde.org/plasma/pico-wizard/-/merge_requests/4
Patch0201:      0001-Improve-integration-with-Plasma.patch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros

Requires:       qt5-qtquickcontrols
Requires:       kf5-kirigami2
Requires:       NetworkManager

BuildArch:      noarch


%description
Pico Wizard is a setup wizard meant for configuring pre-installed operating systems.


%prep
%autosetup -n %{name}-%{commit} -S git_am


%build
%py3_build


%install
%py3_install

# Install polkit rules
install -Dpm 0644 files/polkit-1/rules.d/pico-wizard.rules -t %{buildroot}%{_datadir}/polkit-1/rules.d/
# Install icon logo
install -Dpm 0644 pico-wizard.svg -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/



%files
%license LICENSE LICENSES/
%doc README.rst
%{python3_sitelib}/PicoWizard/
%{python3_sitelib}/pico_wizard-*/
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_datadir}/wayland-sessions/%{name}-session.desktop
%{_datadir}/polkit-1/rules.d/%{name}.rules
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg



%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0^git20220929.934dbcf-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.0^git20220929.934dbcf-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0^git20220929.934dbcf-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.1.0^git20220929.934dbcf-1
- Initial packaging
