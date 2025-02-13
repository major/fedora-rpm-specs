Name:           spyder
Version:        6.0.4
Release:        %autorelease
Summary:        Scientific Python Development Environment

%global forgeurl https://github.com/spyder-ide/spyder/
%global tag v%{version_no_tilde %{quote:%nil}}
%forgemeta

# Spyder is licensed under MIT with the exception of the following
# code, which is licensed BSD-3-Clause.
#
# spyder/widgets/calltip.py
# spyder/utils/introspection/module_completion.py
# spyder/plugins/editor/utils/kill_ring.py
# spyder/plugins/help/utils/conf.py
# spyder/plugins/help/utils/sphinxify.py
# spyder/plugins/help/utils/js/collapse_sections.js
License:        MIT AND BSD-3-Clause
URL:            https://www.spyder-ide.org/
Source:         %forgesource

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# Taken from pyqtwebengine's spec file. Since we require this, we need
# to follow suit.
# Add 'noarch' as per packaging guidelines
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_noarch_with_unported_dependencies
ExclusiveArch:  %{qt5_qtwebengine_arches} noarch

BuildRequires:  python3-devel

BuildRequires:  dos2unix

BuildRequires:  desktop-file-utils
# Still required by guidelines for now since Fedora uses appstream-builder
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

%global appname org.spyder_ide.spyder

%global _description %{expand:
Spyder is a powerful scientific environment written in Python, for Python, and
designed by and for scientists, engineers and data analysts. It offers a unique
combination of the advanced editing, analysis, debugging, and profiling
functionality of a comprehensive development tool with the data exploration,
interactive execution, deep inspection, and beautiful visualization
capabilities of a scientific package.

Beyond its many built-in features, its abilities can be extended even further
via its plugin system and API. Furthermore, Spyder can also be used as a PyQt5
extension library, allowing you to build upon its functionality and embed its
components, such as the interactive console, in your own software.}

%description %_description


%package -n python3-spyder
Summary:    %{summary}

# For %%{_datadir}/icons
Requires:       hicolor-icon-theme
# Unbundled from spyder/plugins/help/utils/js/mathjax
Requires:       mathjax
# Required for the plugins (but not for building Spyder)
Requires:       python3-pylint
Requires:       python3-pylint-venv

%description -n python3-spyder %_description


%prep
%forgeautosetup -p1

# Remove bundled external dependencies
rm -rvf external-deps/ spyder/plugins/help/utils/js/mathjax

# Fix DOS/CRNL line endings in files that may be installed
find . -type f \( \
    -name '*.rst' -o -name '*.md' -o -name '*.py' -o -name '*.css' \
    \) -exec dos2unix --keepdate '{}' '+'

# Temporary measure since the 6.x pre-releases are behind stable 5.x
# releases wrt to the version boundaries of dependencies, but we would
# like to keep rawhide and F39 in sync.
# Drop dependency on linters (pylint and pylint-venv)
sed -i \
-e '/pylint>.*/d' \
-e '/pylint-venv>.*/d' setup.py

# Don't show warning regarding newer version
sed -r -i "s|(PYLINT_REQVER.*),<.*'|\1'|" spyder/dependencies.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l spyder

desktop-file-install --dir=%{buildroot}%{_datadir}/applications scripts/spyder.desktop

# cleanup
rm -rvf %{buildroot}%{_bindir}/spyder_win_post_install.py

# replace bundled mathjax with a symlink to the system mathjax
ln -s %{_datadir}/javascript/mathjax/ \
    %{buildroot}%{python3_sitelib}/spyder/plugins/help/utils/js/mathjax

# provide spyder3 as symlink to spyder binary for continuity
ln -s spyder %{buildroot}%{_bindir}/spyder3


%check
# Still required by guidelines for now since Fedora uses appstream-builder
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml


%pretrans -n python3-spyder -p <lua>
--[[Back up any bundled mathjax directory from the old package. See:
https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement
]]
path = "%{python3_sitelib}/spyder/plugins/help/utils/js/mathjax"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end


%files -n python3-spyder -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

# A backed-up bundled mathjax directory from a previous upgrade may be present:
%ghost %{python3_sitelib}/spyder/plugins/help/utils/js/mathjax.rpmmoved
%{python3_sitelib}/spyder/plugins/help/utils/js/mathjax

%{_bindir}/spyder
%{_bindir}/spyder3

%{_metainfodir}/%{appname}.appdata.xml
%{_datadir}/applications/spyder.desktop
%{_datadir}/icons/spyder.png


%changelog
%autochangelog
