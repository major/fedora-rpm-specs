Name:           mu
Version:        1.2.0
Release:        %autorelease
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
%autochangelog
