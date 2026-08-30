%global forgeurl https://github.com/spyder-ide/spyder
%global tag v%{version}
Version:        6.1.7
%forgemeta

Name:           spyder
Release:        %autorelease
Summary:        Scientific Python Development Environment

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

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3dist(python-lsp-black) >= 2
BuildRequires:  python3dist(python-lsp-ruff) >= 2.3
BuildRequires:  python3dist(python-lsp-server) >= 1.13
BuildRequires:  python3dist(spyder-kernels) >= 3.1

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

Requires:       hicolor-icon-theme
Requires:       mathjax
Requires:       python3dist(python-lsp-black) >= 2
Requires:       python3dist(python-lsp-ruff) >= 2.3
Requires:       python3dist(python-lsp-server) >= 1.13
Requires:       python3dist(spyder-kernels) >= 3.1

%description -n python3-spyder %_description


%prep
%forgeautosetup -p1

# Remove bundled external dependencies
rm -rvf external-deps/ spyder/plugins/help/utils/js/mathjax

# Fix DOS/CRNL line endings in files that may be installed
find . -type f \( \
    -name '*.rst' -o -name '*.md' -o -name '*.py' -o -name '*.css' \
    \) -exec dos2unix --keepdate '{}' '+'

# Drop runtime requirements from setup.py to avoid build-time dependency issues
sed -i \
    -e '/python-lsp-black/d' \
    -e '/python-lsp-ruff/d' \
    -e '/python-lsp-server/d' \
    -e '/spyder-kernels/d' setup.py
sed -i -e "s/PYLSP_REQVER = .*/PYLSP_REQVER = '>=1.13.0'/g" spyder/dependencies.py
sed -i -e "s/SPYDER_KERNELS_REQVER = .*/SPYDER_KERNELS_REQVER = '>=3.1.0'/g" spyder/dependencies.py


%generate_buildrequires
%pyproject_buildrequires -r


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
desktop-file-validate %{buildroot}%{_datadir}/applications/spyder.desktop
# Still required by guidelines for now since Fedora uses appstream-builder
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml

export QT_QPA_PLATFORM=offscreen
%pyproject_check_import -t


%files -n python3-spyder -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

# A backed-up bundled mathjax directory from a previous upgrade (from Fedora 34
# or older) may be present; if so, we should continue to own it.
%ghost %attr(0644,root,root) %{python3_sitelib}/spyder/plugins/help/utils/js/mathjax.rpmmoved
%{python3_sitelib}/spyder/plugins/help/utils/js/mathjax

%{_bindir}/spyder
%{_bindir}/spyder3

%{_metainfodir}/%{appname}.appdata.xml
%{_datadir}/applications/spyder.desktop
%{_datadir}/icons/spyder.png


%changelog
%autochangelog
