Name:           thonny
Version:        4.0.0
Release:        1%{?dist}
Summary:        Python IDE for beginners

# Code is MIT, toolbar icons are EPL-1.0
# Vendored python-pipkin is MIT, python-filelock is Unlicense
License:        MIT AND EPL-1.0 AND Unlicense
URL:            https://thonny.org
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-tkinter
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  pyproject-rpm-macros
# To compile the localization files
BuildRequires:  babel

Requires:       python3-tkinter
# Pip is necessary for pip_gui plugin, therefore explicit Requires
Requires:       python3-pip
Requires:       hicolor-icon-theme

# Vendor Libraries
Provides:       bundled(python3dist(pipkin)) = 1.0~b4
Provides:       bundled(python3dist(filelock)) = 3.6

Recommends:     python3-asttokens
Recommends:     python3-distro
Recommends:     zenity
Recommends:     xsel

%description
Thonny is a simple Python IDE with features useful for learning programming.
It comes with a debugger which is able to visualize all the conceptual steps
taken to run a Python program (executing statements, evaluating expressions,
maintaining the call stack). There is a GUI for installing 3rd party packages
and special mode for learning about references.

%prep
%autosetup -p1

# Remove localization helper scripts, we don't need them in the package
rm thonny/locale/compile_mo.bat thonny/locale/update_pot.bat thonny/locale/thonny.pot

%generate_buildrequires
%pyproject_buildrequires -r

%build
# Don't use the upstream compiled language files, compile them during the build
rm thonny/locale/*/LC_MESSAGES/*.mo
pybabel compile -d thonny/locale/ -D thonny
rm thonny/locale/*/LC_MESSAGES/*.po

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files thonny

install -m 0644 -D -T packaging/icons/thonny-256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-64x64.png   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-48x48.png   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-32x32.png   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-22x22.png   %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/thonny.png
install -m 0644 -D -T packaging/icons/thonny-16x16.png   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/thonny.png

install -D -m 0644 -t %{buildroot}%{_datadir}/metainfo                    packaging/linux/org.thonny.Thonny.appdata.xml
install -D -m 0644 -t %{buildroot}%{_mandir}/man1                         packaging/linux/thonny.1
desktop-file-install --dir=%{buildroot}%{_datadir}/applications           packaging/linux/org.thonny.Thonny.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.thonny.Thonny.appdata.xml


%check
# test_pip_gui is temporarily disabled, the failure was reported upstream:
# https://github.com/thonny/thonny/issues/2413
# Enable it again with Thonny 4.0.1
xvfb-run py.test-3 --pyargs thonny -k 'not test_pip_gui'

%files -f %{pyproject_files}
%license LICENSE.txt licenses/ECLIPSE-ICONS-LICENSE.txt
%doc README.rst CHANGELOG.rst CREDITS.rst
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/thonny.png
%{_datadir}/applications/org.thonny.Thonny.desktop
%{_datadir}/metainfo/org.thonny.Thonny.appdata.xml
%{_mandir}/man1/thonny.1*


%changelog
* Thu Sep 01 2022 abrarwali <abrarwali@tutanota.com> - 4.0.0-1
- New upstream version 4.0.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.14-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Karolina Surma <ksurma@redhat.com> - 3.3.14-1
- New upstream version 3.3.14
Resolves: rhbz#1985771
- Compile language files during the build instead of using the ones from upstream

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Karolina Surma <ksurma@redhat.com> - 3.3.11-1
- New upstream version 3.3.11
Resolves: rhbz#1976139
- Don't include localization helper scripts

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.10-2
- Rebuilt for Python 3.10

* Tue May 25 2021 Karolina Surma <ksurma@redhat.com> - 3.3.10-1
- New upstream version 3.3.10
Resolves: rhbz#1961524

* Mon May 03 2021 Karolina Surma <ksurma@redhat.com> - 3.3.7-1
- New upstream version 3.3.7
Resolves: rhbz#1955597

* Wed Mar 24 2021 Karolina Surma <ksurma@redhat.com> - 3.3.6-1
- New upstream version 3.3.6
Resolves: rhbz#1875293
- Correct the license tag
- Mark the lang files as %%lang

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Aivar Annamaa <aivar.annamaa@gmail.com> - 3.3.3-1
- New upstream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.7-4
- Rebuilt to fix dependencies (#1841813)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.7-3
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Aivar Annamaa <aivar.annamaa@gmail.com> - 3.2.7-1
- New upstream version 3.2.6

* Sun Sep 08 2019 Aivar Annamaa <aivar.annamaa@gmail.com> - 3.2.1-1
- New upstream version 3.2.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.2-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.2-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.2-1
- New upstream version 3.1.2

* Sun Feb 10 2019 Aivar Annamaa <aivar.annamaa@gmail.com> - 3.1.1-1
- New upstream version (breakpoints, themes, etc.)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.18-1
- Update to 2.1.18 to fix new jedi incompatibilities

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.17-2
- Rebuilt for Python 3.7

* Wed Mar 21 2018 Aivar Annamaa <aivar.annamaa@gmail.com> - 2.1.17-1
- New upstream version (fixes a bug in pip package manager)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.16-2
- Remove obsolete scriptlets

* Fri Nov 10 2017 Aivar Annamaa <aivar.annamaa@gmail.com> - 2.1.16-1
- Initial package
