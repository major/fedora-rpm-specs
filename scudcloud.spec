Name:           scudcloud
Version:        1.65
Release:        16%{?dist}
Summary:        Non official desktop client for Slack

License:        MIT
URL:            https://github.com/raelgc/scudcloud
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-jsmin

Requires:       python3-dbus
Requires:       python3-qt5
Requires:       python3-qt5-webkit
Requires:       lato-fonts
Requires:       hicolor-icon-theme
Recommends:     pyhunspell-python3
# It is possible to use self-written notifier, but better to use libnotify
# via GObject Introspection
Recommends:     (libnotify and python3-gobject-base)

BuildRequires:  desktop-file-utils

%description
ScudCloud improves the Slack integration with Linux desktops featuring:
* multiple teams support
* native system notifications
* count of unread direct mentions at launcher/sytray icon
* alert/wobbling on new messages
* optional tray notifications and "Close to Tray"
* follow your desktop activity and will stay online while you're logged in

%prep
%autosetup
# Drop shebang
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{name}/{__main__,cookiejar}.py

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{_datadir}/icons/{elementary,ubuntu*}/
rm -rf %{buildroot}%{_datadir}/doc/%{name}/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}*.svg
%{_datadir}/pixmaps/%{name}.png
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.65-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.65-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.65-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.65-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.65-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.65-1
- Update to 1.65

* Wed Jan 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.64-1
- Update to 1.64

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.63-2.1
- Remove obsolete scriptlets

* Thu Nov 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.63-2
- Remove obsolete scriptlets

* Wed Sep 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.63-1
- Update to 1.63

* Sat Sep 09 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.62-1
- Update to 1.62

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.60-1
- Update to 1.60

* Wed Mar 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.50-2
- Adopt to qt5
- Fix shebang

* Wed Mar 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.50-1
- Update to 1.50

* Fri Mar 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.48-1
- Update to 1.48

* Sat Mar 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.43-1
- Update to 1.43

* Sat Mar 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.40-1
- Update to 1.40 (RHBZ #1429150)

* Tue Feb 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.39-1
- Update to 1.39 (RHBZ #1421894)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.37-2
- Rebuild for Python 3.6

* Wed Nov 16 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.37-1
- Update to 1.37 (RHBZ #1395685)

* Wed Nov 16 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.34-1
- Update to 1.34 (RHBZ #1383856)

* Mon Oct 10 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.33-2
- Remove shebang in %%prep

* Mon Oct 10 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.33-1
- Update to 1.33 (RHBZ #1383343)

* Wed Jul 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.31-1
- Update to 1.31 (RHBZ #1360333)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 05 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.30-1
- Update to 1.30 (RHBZ #1352898)

* Mon Jul 04 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.29-1
- Update to 1.29 (RHBZ #1352582)

* Mon Jun 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.25-1
- Update to 1.25 (RHBZ #1350359)

* Fri Jun 17 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.24-2
- Add Requires: hicolor-icon-theme
- Fix typo in lato-fonts

* Mon Jun 13 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.24-1
- Initial package
