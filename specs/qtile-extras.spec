%global forgeurl https://github.com/elParaguayo/qtile-extras
# Upstream tagged 0.34.1 early and didn't include the commit that fixed the test
# suite. We need to use `commit` instead of `tag` to make sure the fix is
# included for this release.
%global commit 359964520a9dcd2c7e12680bfc53e359d74c489b

Name: qtile-extras
Version: 0.34.1
Release: %{autorelease}
Summary: A collection of mods for Qtile
%forgemeta

License: MIT
URL: https://github.com/elParaguayo/qtile-extras
Source0: %{forgesource}

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-requests
BuildRequires: python3-pip
BuildRequires: python3-wheel
BuildRequires: qtile = %{version}
BuildRequires: pango-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: python3-dbus-next
BuildRequires: python3-gobject
BuildRequires: python3-gobject-base
BuildRequires: python3-dbus-fast
BuildRequires: cairo-devel
BuildRequires: gobject-introspection-devel

# Test dependencies
# In the ideal world, we would generate the Python dependencies dynamically
# through `%%pyproject_buildrequires -e %%{toxenv}`
# The problem is, that some of the dependencies are not packaged for Fedora
# (e.g. iwlib, stravalib, pulsectl-asyncio) and we won't provide the widgets
# that depends on them
# We should patch the tox.ini file and remove the missing dependencies instead
# of installing everything manually
BuildRequires: tox
BuildRequires: python3-anyio
BuildRequires: python3-tox-current-env
BuildRequires: python3-pytest
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: xorg-x11-server-Xephyr
BuildRequires: rsvg-pixbuf-loader
BuildRequires: ImageMagick
BuildRequires: pango-devel
BuildRequires: python3-setuptools
BuildRequires: python3-dbus-next
BuildRequires: python3-xcffib
BuildRequires: rsvg-pixbuf-loader

# The tarball is missing .git directory, we need to create it during build
BuildRequires: git

Requires: qtile = %{version}


%description
A collection of third-party widgets, toolkits, wallpapers, and other extras for
Qtile. For more, please read https://qtile-extras.readthedocs.io


%generate_buildrequires
%pyproject_buildrequires


%prep
%forgesetup

git init

# The stravalib isn't packaged for Fedora yet
# https://pypi.org/project/stravalib/
rm -rf qtile_extras/widget/strava.py
rm -rf qtile_extras/resources/stravadata
rm -rf test/widget/test_strava.py

# The iwlib isn't packaged for Fedora anymore
# https://pypi.org/project/iwlib/
rm -rf qtile_extras/widget/network.py
rm -rf test/widget/test_network.py

# Remove empty fixtures file
# https://github.com/elParaguayo/qtile-extras/pull/386
rm -rf qtile_extras/resources/footballscores/fixtures.py

# This test requires pytest_lazyfixture which is not compatible with pytest 8
# https://github.com/elParaguayo/qtile-extras/issues/388
rm -rf test/widget/test_currentlayouticon.py

# Remove shebang
sed -e "\|#! /usr/bin/python3 -sP|d" -i qtile_extras/resources/visualiser/cava_draw.py
sed -e "\|#!/usr/bin/env python|d" -i qtile_extras/resources/visualiser/cava_draw.py

# In the minimal buildroot, there is no python command, only python3
# https://github.com/elParaguayo/qtile-extras/pull/390
sed "s/python/python3/" -i test/widget/test_scriptexit.py

# This test downloads an asset (github.svg) from the internet which won't work
# when building in Koji
rm -rf test/widget/test_image.py


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files qtile_extras

rm -rf %{buildroot}%{python3_sitelib}/test


%check
# Avoid `OSError: [Errno 24] Too Many Open Files` error
ulimit -n 10240

%pytest -vv \
    --deselect test/widget/test_alsawidget.py::test_alsawidget_defaults[1-x11] \
    --deselect test/widget/test_alsawidget.py::test_controls[1-x11] \
    --deselect test/widget/test_alsawidget.py::test_step[1-x11-alsa_manager0] \
    --deselect test/widget/test_alsawidget.py::test_no_icons[1-x11-alsa_manager0] \
    --deselect test/widget/test_alsawidget.py::test_icons[1-x11-alsa_manager0] \
    --deselect test/widget/test_githubnotifications.py::test_githubnotifications_reload_token[1-x11-False-githubnotification_manager0]

%files -n qtile-extras -f %{pyproject_files}
%license LICENSE
%doc README.md


%autochangelog
