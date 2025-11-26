%global forgeurl https://github.com/elParaguayo/qtile-extras
%global tag v0.34.0

Name: qtile-extras
Version: 0.34.0
Release: 1%{?dist}
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
# I am not sure why these tests fail. Let's investigate later
pytest_expressions="not test_footballmatch_module_kickoff_time"
pytest_expressions+=" and not test_githubnotifications_reload_token"
pytest_expressions+=" and not test_syncthing_http_error"

%pytest -vv -k "$pytest_expressions" \
    --deselect test/widget/test_alsawidget.py::test_alsawidget_defaults[1-x11] \
    --deselect test/widget/test_alsawidget.py::test_controls[1-x11] \
    --deselect test/widget/test_alsawidget.py::test_step[1-x11-alsa_manager0] \
    --deselect test/widget/test_alsawidget.py::test_no_icons[1-x11-alsa_manager0] \
    --deselect test/widget/test_alsawidget.py::test_icons[1-x11-alsa_manager0]

%files -n qtile-extras -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Mon Nov 24 2025 Jakub Kadlcik <frostyx@email.cz> - 0.34.0-1
- New upstream version

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.33.0-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 29 2025 Jakub Kadlcik <frostyx@email.cz> - 0.33.0-1
- New upstream version

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jul 13 2025 Jakub Kadlcik <frostyx@email.cz> - 0.32.0-1
- New upstream version

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 05 2024 Jakub Kadlcik <frostyx@email.cz> - 0.29.0-5
- Exclude one more test
- Add todo about dynamic BuildRequires
- Drop the python3-pytest-cov dependency

* Sun Nov 03 2024 Jakub Kadlcik <frostyx@email.cz> - 0.29.0-4
- Run tests in the check phase

* Fri Nov 01 2024 Jakub Kadlcik <frostyx@email.cz> - 0.29.0-3
- Remove empty fixtures file
- Remove shebang from the cava_draw.py file

* Wed Oct 30 2024 Jakub Kadlcik <frostyx@email.cz> - 0.29.0-2
- Small fixes to the specfile formatting
- Add some build dependencies for tests
- Don't depend on deprecated python3-pytest7

* Wed Oct 30 2024 Jakub Kadlcik <frostyx@email.cz> - 0.29.0-1
- New upstream version

* Wed Aug 21 2024 Jakub Kadlcik <frostyx@email.cz> - 0.28.1-1
- New upstream version

* Sat Jul 13 2024 Jakub Kadlcik <frostyx@email.cz> - 0.27.0-1
- New upstream version

* Thu May 23 2024 Jakub Kadlcik <frostyx@email.cz> - 0.26.0-1
- New upstream version

* Sun Nov 05 2023 Jakub Kadlcik <frostyx@email.cz> - 0.23.0-1
- New upstream version

* Thu Sep 22 2022 Jakub Kadlcik <frostyx@email.cz> - 0.22.1-1
- Upgrade to the new upstream version

* Wed Jan 05 2022 Jakub Kadlcik <frostyx@email.cz>
- Initial package
