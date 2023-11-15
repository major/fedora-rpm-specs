# Use forge macros for pulling from GitHub
%global forgeurl https://github.com/spyder-ide/spyder/

Name:           spyder
Version:        6.0.0~a1
Release:        %autorelease
Summary:        Scientific Python Development Environment
%global tag v%{version_no_tilde %{quote:%nil}}
%forgemeta
License:        MIT
URL:            https://www.spyder-ide.org/
Source:         %forgesource

# Bump jedi upper bound from <0.19.0 to <0.20.0
# https://github.com/spyder-ide/spyder/pull/21367 (backported)
Patch:          21367.patch

# Ensure no source files have useless shebangs
# https://github.com/spyder-ide/spyder/pull/21372 (backported)
Patch:          21372.patch

# Bump python-lsp-server upper bound to <=1.9.0
# https://github.com/spyder-ide/spyder/pull/21501 (backported)
Patch:          21501.patch

# Remove upper bound from spyder-kernels
# We are a little out of sync with spyder-kernels
Patch:          no_upper_bound_for_kernels.patch

# Fix deprecated top-level developer_name in AppData XML
# https://github.com/spyder-ide/spyder/pull/21510
Patch:          %{forgeurl}/pull/21510.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# Taken from pyqtwebengine's spec file. Since we require this, we need
# to follow suit.
ExclusiveArch:  %{qt5_qtwebengine_arches}

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
# Drop upper bound for pylint (3.0.0~a7 > 3.0)
sed -r -i 's|(pylint.*),<3.0|\1|' setup.py
# Do the same for qtconsole (5.5.0 > 5.5~~)
sed -r -i 's|(qtconsole.*),<5.5.0|\1|' setup.py
# And for qdarkstyle (3.2.1 > 3.2~~)
sed -r -i 's|(qdarkstyle.*),<3.2.0|\1|' setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files spyder

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
