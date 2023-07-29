Name:           mu
Version:        1.2.0
Release:        3%{?dist}
Summary:        A simple Python editor not only for micro:bit
License:        GPL-3.0-only
URL:            https://github.com/mu-editor/mu
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Mu 1.1+ creates a virtual environment when it starts and installs
# a bunch of packages from PyPI to it.
# See https://github.com/mu-editor/mu/commit/37a0e0df46
# The downloaded wheels from PyPI are cached to %%{python3_sitelib}, which fails without root/sudo.
# See https://github.com/mu-editor/mu/issues/1634
# Downloading software from the internet cannot be required for an official RPM package to function,
# so we disable it here.
# With this patch, the packages normally installed to the virtual environment
# are required on runtime and the virtual environment is created with --system-site-packages.
# This kinda goes against the entire idea of the virtualenv feature,
# but it is the only reasonable way to have Mu packaged.
Patch:          system-site-packages.patch

# Avoid a race condition when creating LOG_DIR
# Fixes https://bugzilla.redhat.com/2106165
# Merged upstream
Patch:          https://github.com/mu-editor/mu/pull/2281.patch

# Fix asserts for called once in Python 3.12
Patch:         	https://github.com/mu-editor/mu/pull/2448.patch

BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# no dist provide for this:
BuildRequires:  python3-qt5
BuildRequires:  python3-qscintilla-qt5
BuildRequires:  qt5-qtserialport >= 5.5.0

BuildRequires:  systemd

BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  /usr/bin/msgfmt

# unbundled
BuildRequires:  python3dist(microfs) >= 1.3
BuildRequires:  python3dist(uflash) >= 2
BuildRequires:  python3dist(esptool) >= 3

Requires:       python%{python3_version}dist(microfs) >= 1.3
Requires:       python%{python3_version}dist(uflash) >= 2
Requires:       python%{python3_version}dist(esptool) >= 3
Requires:       python3-qt5 >= 5.11
Requires:       python3-qscintilla-qt5 >= 2.10.7
Requires:       hicolor-icon-theme

# The name on PyPI and the Shell command
Provides:       mu-editor = %{version}-%{release}

%description
mu is a simple Python editor also for BBC micro:bit devices.

%prep
%autosetup -p1

# make the versions not pinned for the entry_point to work
# also pyqt and qscintilla are not properly provided in Fedora :(
# relax as well the python version requirement
# upstream removes some reqs on arm, we don't
sed -i -e 's/PyQt5==5.13.2"/PyQt5>=5.13.2",/' \
       -e 's/QScintilla==2.11.3"/QScintilla>=2.11.3",/' \
       -e 's/PyQtChart==5.13.1"/PyQtChart >= 5.13.1, < 6",/' \
       -e '/platform_machine/d' \
       -e 's/jupyter-client>=4.1,<6.2/jupyter-client>=4.1/' \
       -e 's/ipykernel>=4.1,<6/ipykernel>=4.1/' \
       -e 's/qtconsole==4.7.7/qtconsole >= 4.7.7, < 6/' \
       -e 's/pyserial~=3.5/pyserial>=3.4/' \
       -e 's/click<=8.0.4/click/' \
       -e 's/black>=19.10b0,<22.1.0/black>=19.10b0/' \
       -e 's/platformdirs>=2.0.0,<3.0.0/platformdirs>=2.0.0,<4.0.0/' \
       -e 's/python_requires=">=3.5,<3.9"/python_requires=">=3.5"/' \
       setup.py

# unbundle things
sed -i 's/from mu.contrib import /import /' mu/modes/microbit.py tests/modes/test_microbit.py \
                                            mu/modes/base.py
sed -i 's/mu.contrib.esptool/esptool/'      mu/interface/dialogs.py
rm -rf mu/contrib
sed -i '/"mu.contrib",/d' setup.py
sed -i 's/mu.contrib.//' tests/modes/test_microbit.py

# Remove the pytest-random-order requirement as it's not packaged in Fedora
sed -i '/random-order/d' pytest.ini


%generate_buildrequires
%pyproject_buildrequires -r


%build
# rebuild locales
cd mu/locale
for FILE in *; do
  rm $FILE/LC_MESSAGES/mu.mo
  msgfmt $FILE/LC_MESSAGES/mu.po -o $FILE/LC_MESSAGES/mu.mo
  rm $FILE/LC_MESSAGES/mu.po
done
cd -
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files mu

mkdir -p %{buildroot}%{_datadir}/applications \
         %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ \
         %{buildroot}%{_udevrulesdir} \
         %{buildroot}%{_metainfodir}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications conf/mu.codewith.editor.desktop
cp -p conf/mu.codewith.editor.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
cp -p conf/90-usb-microbit.rules %{buildroot}%{_udevrulesdir}/
cp -p conf/mu.appdata.xml %{buildroot}%{_metainfodir}/


%check
%global __pytest xvfb-run %__pytest
# test_Window_connect_zoom is temporarily disabled
# upstream issue: https://github.com/mu-editor/mu/issues/2449
%pytest -vv -k "not test_Window_connect_zoom"


%files -f %{pyproject_files}
%doc README.rst LICENSE
%{_bindir}/mu-editor
%{_udevrulesdir}/90-usb-microbit.rules
%{_datadir}/icons/hicolor/256x256/apps/mu.codewith.editor.png
%{_datadir}/applications/mu.codewith.editor.desktop
%{_metainfodir}/mu.appdata.xml


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.2.0-2
- Relax version constraint to allow compatibility with the latest platformdirs

* Thu Mar 23 2023 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-1
- Update to 1.2.0
- Update the License identifier to SPDX
- Avoid a race condition when creating LOG_DIR
- Fixes rhbz#2143537
- Fixes rhbz#2106165

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 09 2022 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-6
- Make mu work with pyflakes 2.5

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.11

* Wed Jun 08 2022 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Relax esptool version requirement
- Fixes: rhbbz#2095054

* Thu May 12 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-2
- Relax flask version requirement

* Tue Apr 19 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Tue Apr 19 2022 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-16
- Allow pyserial 3.5
- Fixes rhbz#2074419

* Mon Mar 07 2022 Karolina Surma <ksurma@redhat.com> - 1.0.3-15
- Skip test that fails with setuptools >= 60.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-13
- Allow pyflakes 2.4
- Fixes rhbz#2016933

* Tue Oct 12 2021 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-12
- Allow pycodestyle 2.8
- Fixes rhbz#2013269

* Tue Sep 28 2021 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-11
- Fix crash on startup on Python 3.10+
- Fixes: rhbz#2008378

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-9
- Relax the required versions of pyflakes and pycodestyle
- Fixes rhbz#1979411

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.3-8
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-6
- Mark language files as such
- Remove *.po files
- Remove useless shebang

* Wed Nov 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-5
- Allow qtconsole 5
- Fixes: rhbz#1901573

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Allow pyflakes 2.2 and pycodestyle 2.6 (#1841648)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-1
- Update to 1.0.3
- Provide mu-editor

* Thu Feb 06 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-8
- Adapt the shebang to use the -s flag and only use system installed modules (#1799790)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-5
- Relax the dependency version restrictions for matplotlib

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Relax the dependency version restrictions even further (#1731655)

* Sun Mar 24 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-1
- Update to 1.0.2
- Loosen some strict dependency declarations
- Fix test failure

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Mu works with matplotlib 3.0

* Thu Sep 13 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Fix requires to allow startup
- Fix the desktop file

* Tue Aug 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1
- Update to 1.0.0 (#1387943)
- Move udev rules to /usr/lib/udev/rules.d (#1602361)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.13-3
- Rebuilt for Python 3.7

* Sun May 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.13-2
- Add missing requires (pyflakes, pep8) (#1582237)

* Tue Apr 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.13-1
- Updated to 0.9.13
- Unbundle things
- Run tests

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 13 2016 Kushal Das <kushal@fedoraprojects.org> - 0.2-1
- Updates to 0.2 release

* Fri Feb 26 2016 Kushal Das <kushal@fedoraprojects.org> - 0.1-2
- Updates the desktop file creation

* Tue Feb 02 2016 Kushal Das <kushal@fedoraprojects.org> - 0.1-1
- Initial package creation
