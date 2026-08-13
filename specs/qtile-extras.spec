%bcond x11 %[!(0%{?rhel} >= 10)]

%global forgeurl https://github.com/elParaguayo/qtile-extras
%global tag v0.36.0

Name: qtile-extras
Version: 0.36.0
Release: %{autorelease}
Summary: A collection of mods for Qtile
%forgemeta

License: MIT
URL: https://github.com/elParaguayo/qtile-extras
Source0: %{forgesource}

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: qtile = %{version}
BuildRequires: qtile-wayland = %{version}

# Test dependencies
BuildRequires: python3-pytest
%if %{with x11}
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: xorg-x11-server-Xephyr
%endif
BuildRequires: ImageMagick
BuildRequires: pulseaudio-libs
# test/scripts/window.py GI deps
BuildRequires: gobject-introspection
BuildRequires: gtk3
BuildRequires: gtk-layer-shell

# The tarball is missing .git directory, we need to create it during build
BuildRequires: git-core

Requires: qtile = %{version}


%description
A collection of third-party widgets, toolkits, wallpapers, and other extras for
Qtile. For more, please read https://qtile-extras.readthedocs.io


%generate_buildrequires
%pyproject_buildrequires -x dev,widgets


%prep
%forgesetup
# not needed with latest setuptools
%pyproject_patch_dependency wheel:ignore
# no coverage tests in downstream packaging
%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency coveralls:ignore
%pyproject_patch_dependency pytest-cov:ignore
# widget deps not in Fedora
%pyproject_patch_dependency stravalib:ignore
%pyproject_patch_dependency iwlib:ignore
# test deps not in Fedora, or different versions
%pyproject_patch_dependency pytest:drop_upper
%pyproject_patch_dependency check-manifest:ignore

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
    --backend wayland \
%if %{with x11}
    --backend x11 \
    --deselect test/widget/test_alsawidget.py::test_alsawidget_defaults[1-x11] \
    --deselect test/widget/test_alsawidget.py::test_controls[1-x11] \
    --deselect test/widget/test_alsawidget.py::test_step[1-x11-alsa_manager0] \
    --deselect test/widget/test_alsawidget.py::test_no_icons[1-x11-alsa_manager0] \
    --deselect test/widget/test_alsawidget.py::test_icons[1-x11-alsa_manager0] \
    --deselect test/widget/test_githubnotifications.py::test_githubnotifications_reload_token[1-x11-False-githubnotification_manager0] \
%endif
    --deselect test/widget/test_widget_init.py::test_init_import_error_no_fallback

%files -n qtile-extras -f %{pyproject_files}
%license LICENSE
%doc README.md


%autochangelog
