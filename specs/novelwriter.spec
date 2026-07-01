Name:           novelwriter
Version:        26.1.1
Release:        %autorelease
Summary:        Plain text editor designed for writing novels

# Code is GPL-3.0-or-later, icons are CC-BY-SA-4.0 and Apache-2.0 and MIT
License:        GPL-3.0-or-later AND CC-BY-SA-4.0 AND Apache-2.0 AND MIT
URL:            https://novelwriter.io/
Source:         https://github.com/vkbo/novelwriter/archive/v%{version}/novelwriter-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  adobe-source-sans-pro-fonts
BuildRequires:  enchant2-devel
BuildRequires:  google-noto-sans-fonts
BuildRequires:  hunspell-en
BuildRequires:  hunspell-en-GB
BuildRequires:  hunspell-en-US
BuildRequires:  hunspell-devel
BuildRequires:  python3-enchant
BuildRequires:  python3-zlib-ng
BuildRequires:  qt6-qtimageformats
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtsvg-devel

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
# Generate DocBook for internal documentation
BuildRequires:  python3-sphinx-design
BuildRequires:  python3-sphinx-copybutton
BuildRequires:  texinfo
# Needed for directory ownership
Requires:       hicolor-icon-theme
# Not linked automatically
Requires:  qt6-qtimageformats
Requires:  qt6-qttools
Requires:  qt6-qtsvg
# Bundles svg material design icons
Provides:       bundled(material-design-icons)
# Recommends
Recommends:  adobe-source-sans-pro-fonts
Recommends:  google-noto-sans-fonts

%description
novelWriter is a plain text editor designed for writing novels assembled from
many smaller text documents. It uses a minimal formatting syntax inspired by
Markdown, and adds a meta data syntax for comments, synopsis, and
cross-referencing. It's designed to be a simple text editor that allows for
easy organization of text and notes, using human readable text files as
storage for robustness.

The project storage is suitable for version control software, and also well
suited for file synchronization tools. All text is saved as plain text files
with a meta data header. The core project structure is stored in a single
project XML file. Other meta data is primarily saved as JSON files.

%package doc
Summary: Documentation for novelWriter

BuildArch:  noarch

%description doc
Documentation for novelWriter in docbook format. 

%prep
%autosetup -n novelWriter-%{version} -p1
# Use Fedora specific variant for qt6
sed -i 's/"lrelease"/"lrelease-qt6"/g' utils/assets.py

%generate_buildrequires
%pyproject_buildrequires

%build
# Build translations
%python3 pkgutils.py qtlrelease
# Build sample
%python3 pkgutils.py sample
# Build documentation
pushd docs
sphinx-build source texinfo -b texinfo
pushd texinfo
makeinfo --docbook novelwriter.texi
popd
popd
# Build package
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L novelwriter

desktop-file-install --dir=%{buildroot}%{_datadir}/applications setup/data/novelwriter.desktop
mkdir -p %{buildroot}%{_metainfodir}/
install -m644 setup/novelwriter.appdata.xml %{buildroot}%{_metainfodir}/
mkdir -p %{buildroot}%{_datadir}/icons
cp -r -p setup/data/hicolor %{buildroot}%{_datadir}/icons/
install -pDm0644 docs/texinfo/novelwriter.xml \
  %{buildroot}%{_datadir}/help/en/novelwriter/novelwriter.xml
for file in docs/texinfo/novelwriter-figures/*.*
do
  install -pDm0644 $file \
  %{buildroot}%{_datadir}/help/en/novelwriter/novelwriter-figures/$(basename $file)
done

%find_lang nw --with-qt

%check
QT_QPA_PLATFORM=offscreen %pytest
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/novelwriter.appdata.xml

%files -n novelwriter -f %{pyproject_files} -f nw.lang
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
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/novelwriter

%changelog
%autochangelog
