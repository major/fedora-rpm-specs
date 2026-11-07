%global         forgeurl0 https://github.com/carlbyington2/dupeguru
%global         version0  4.3.1
%global         date      20261106
%global         commit    7a2c79ff790ccc7c0f8ec3181ef1eba411026e55
%forgemeta

Summary:        GUI tool to find duplicate files by content
Name:           dupeguru
Version:        %forgeversion
Release:        %autorelease
Source:         %forgesource
URL:            %forgeurl

# The upstream should be https://github.com/arsenetar/dupeguru but
# that version is almost dormant. The last release was four years ago,
# and there are many critical outstanding pull requests that have
# not been merged.
#
# https://github.com/carlbyington2/dupeguru/tree/fedora-build is a
# fork with most of the open pull requests from arsenetar applied.


# the source code in the tarball is GPL-3.0-only
# the Sphinx generated HTML static assets use the other licenses
License:        GPL-3.0-only AND BSD-2-Clause AND BSD-3-Clause AND MIT AND LicenseRef-Fedora-Public-Domain

# remove the about box check for new releases - that should be done via dnf
Patch0:         remove-check-for-updates.patch

# change github issues references from arsenetar to carlbyington2 repo
Patch1:         github-references-carlbyington2.patch


# tools to build the project
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  pyside6-tools
BuildRequires:  python3-devel
BuildRequires:  python3-polib
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# for % check section
BuildRequires:  desktop-file-utils
BuildRequires:  python3-defusedxml
BuildRequires:  python3-mutagen
BuildRequires:  python3-pyqt6
BuildRequires:  python3-pytest
BuildRequires:  python3-semantic_version
BuildRequires:  python3-send2trash

# packages required at runtime
# since we have icons
Requires:       hicolor-icon-theme

%description

dupeGuru is a cross-platform (Linux and OS X) GUI tool to find
duplicate files.  It is written mostly in Python 3 and uses Qt6 for
the UI.


%prep
%forgeautosetup -p1
%py3_shebang_fix .
# put the full fedora version in the about box
fn=dupeguru/core/__init__.py
sed -i -e 's/__version__.*/__version__ = "%{version0}"/' $fn
sed -i -e 's/__full_version__.*/__full_version__ = "%{version}-%{release}"/' $fn


%generate_buildrequires
%pyproject_buildrequires


%build
# create one source file
make %{?_smp_mflags} dupeguru/qt/dg_rc.py RCC=pyside6-rcc
# build the python code
%pyproject_wheel
# build the locale files
make %{?_smp_mflags} i18n
# build the help files
%{python3} build.py --alldoc
# remove sphinx artifacts
rm -rf build/help/*/.buildinfo
rm -rf build/help/*/.doctrees


%install
%pyproject_install
%pyproject_save_files dupeguru
# install in the proper places
mkdir -p                                       %{buildroot}%{_datadir}/%{name}
cp -a locale                                   %{buildroot}%{_datadir}/%{name}
cp -a build/help                               %{buildroot}%{_datadir}/%{name}
install -p -m 644 -D pkg/dupeguru.desktop      %{buildroot}%{_datadir}/applications/dupeguru.desktop
install -p -m 644 -D images/dgse_logo_128.png  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -p -m 755 -D run.py                    %{buildroot}%{_bindir}/%{name}
install -p -m 644 -D README.md                 %{buildroot}%{_pkgdocdir}/README.md
install -p -m 644    help/changelog            %{buildroot}%{_pkgdocdir}/changelog
## symlinks since dupeguru wants locale and help in %%{python3_sitearch}/%%{name}
## but we want those in installed in %%{_datadir}/%%{name}
ln -sf %{_datadir}/%{name}/locale  %{buildroot}%{python3_sitearch}/%{name}/locale
ln -sf %{_datadir}/%{name}/help    %{buildroot}%{python3_sitearch}/%{name}/help

# remove installed but unpackaged files
find %{buildroot} -name '*.po' -delete
find %{buildroot} -name '*.pot' -delete
rm  %{buildroot}%{_includedir}/python%{python3_version}/%{name}/common.h
find %{buildroot}%{python3_sitearch}/%{name} -name '*.c' -delete

%find_lang columns
%find_lang core
%find_lang ui

# combine the language files into one file for the files section
# pyproject_files contains some .c files that should not be packaged and were removed above
cat columns.lang core.lang ui.lang %{pyproject_files} | grep -v '\.c$' | sort >dupeguru.lang


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/dupeguru.desktop
%pytest dupeguru/core dupeguru/hscommon
%pyproject_check_import


%files -f dupeguru.lang
%{_bindir}/%{name}
%license LICENSE
%license pkg/debian/copyright
%{python3_sitearch}/%{name}/help
%{python3_sitearch}/%{name}/locale
%{_datadir}/applications/dupeguru.desktop
%{_datadir}/icons/*/*/*/%{name}.png
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/locale/*
%dir %{_datadir}/%{name}/locale/*/LC_MESSAGES
%{_datadir}/%{name}/help/
%docdir %{_pkgdocdir}
%{_pkgdocdir}


%changelog
%autochangelog
