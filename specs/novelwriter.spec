Name:           novelwriter
Version:        2.6.3
Release:        %autorelease
Summary:        Plain text editor designed for writing novels

# Code is GPL-3.0-or-later, icons are CC-BY-SA-4.0
License:        GPL-3.0-or-later AND CC-BY-SA-4.0 
URL:            https://novelwriter.io/
Source:         https://github.com/vkbo/novelwriter/archive/v%{version}/novelwriter-%{version}.tar.gz
# https://github.com/vkbo/novelWriter/issues/907
Patch:          doctheme.patch

BuildArch:      noarch
BuildRequires:  adobe-source-sans-pro-fonts
BuildRequires:  hunspell-en
BuildRequires:  hunspell-en-GB
BuildRequires:  hunspell-en-US
BuildRequires:  enchant2-devel
BuildRequires:  hunspell-devel
BuildRequires:  python3-enchant
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  python3-devel

BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

# Test requirements
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-qt)
BuildRequires:  python3dist(pytest-xvfb)
# Documentation requirements
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
# Use lv_2 instead instead of book-theme
BuildRequires:  python3-sphinx_lv2_theme
BuildRequires:  python3dist(sphinx-intl)
# Needed for directory ownership
Requires:       hicolor-icon-theme

%description
novelWriter is a plain text editor designed for writing novels assembled from
many smaller text documents. It uses a minimal formatting syntax inspired by
Markdown, and adds a meta data syntax for comments, synopsis, and
cross-referencing. It's designed to be a simple text editor that allows for
easy organisation of text and notes, using human readable text files as
storage for robustness.

The project storage is suitable for version control software, and also well
suited for file synchronisation tools. All text is saved as plain text files
with a meta data header. The core project structure is stored in a single
project XML file. Other meta data is primarily saved as JSON files.

%package doc
Summary: Documentation for novelWriter

BuildArch:  noarch

%description doc
Documentation for novelWriter in HTML format.  The sphinx-_lv2_theme is used
because t does not contain javascript.  The original theme used is
sphinx-book-theme.

%prep
%autosetup -n novelWriter-%{version} -p1
# https://github.com/vkbo/novelWriter/issues/2276
sed -i 's/self.spellLanguage = "en"/self.spellLanguage = "en_US"/g' novelwriter/config.py
sed -i 's/spellcheck = en/spellcheck = en_US/g' tests/reference/baseConfig_novelwriter.conf

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Build documentation
pushd docs
sphinx-build source html -b html
# remove build uneeded artifacts
rm -rf html/.buildinfo
rm -rf html/.doctrees
popd

%install
%pyproject_install
%pyproject_save_files novelwriter
desktop-file-install --dir=%{buildroot}%{_datadir}/applications setup/data/novelwriter.desktop
mkdir -p %{buildroot}%{_metainfodir}/
install -m644 setup/novelwriter.appdata.xml %{buildroot}%{_metainfodir}/
mkdir -p %{buildroot}%{_datadir}/icons
cp -r -p setup/data/hicolor %{buildroot}%{_datadir}/icons/

%check
QT_QPA_PLATFORM=offscreen %pytest
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/novelwriter.appdata.xml

%files -n novelwriter -f %{pyproject_files}
%license LICENSE.md
%doc README.md
%{_bindir}/novelwriter
%{_datadir}/applications/novelwriter.desktop
%{_metainfodir}/novelwriter.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/icons/hicolor/*/mimetypes/*.svg

%files doc
%license LICENSE.md
%doc docs/html

%changelog
%autochangelog
