Name:           bibletime
Version:        3.2.0
Release:        %autorelease
Summary:        An easy to use Bible study tool
License:        GPL-2.0-only
URL:            https://www.bibletime.info/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch:          bibletime-c++20-spaceship.patch

# These lack qtwebengine/qtwebkit
ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  gcc-c++
BuildRequires:  clucene-core-devel >= 2.0
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  openssl-devel
BuildRequires:  sword-devel >= 1.8.1-15
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtspeech-devel
BuildRequires:  po4a
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  make

# fop is java_arches exclusive
# However, this line is more inclusive of arches that do not have
# qtwebengine
#ExclusiveArch:  %%{java_arches}
BuildRequires:  fop

%description
BibleTime is a free and easy to use cross-platform bible study tool. It
provides easy handling of digitalized texts (Bibles, commentaries and
lexicons) and powerful features to work with these texts (search in
texts, write own notes, save, print etc.). BibleTime is a front-end for
the SWORD Bible Framework.

%package doc
Summary:        Documentation and handbooks for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation and handbooks for %{name}.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

# CMake installs doc files under BibleTime instead of bibletime
mv %{buildroot}%{_docdir}/BibleTime %{buildroot}%{_docdir}/%{name}

# rename wrongly-named locale
mv %{buildroot}%{_docdir}/%{name}/handbook/html/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/handbook/pdf/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/howto/html/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/howto/pdf/{br,BR} || :

# Symlink duplicate license file to avoid duplication and rpmlint error
rm -f %{buildroot}%{_datadir}/%{name}/license/LICENSE
ln -s ../../licenses/%{name}/LICENSE %{buildroot}%{_datadir}/%{name}/license/LICENSE

# locale's
%find_lang %{name} || touch %{name}.lang
BT_DOC_DIR=%{_docdir}/%{name}/
for doctype in handbook howto ; do
    for fmt in html pdf; do
        for lang_dir in %{buildroot}/$BT_DOC_DIR/$doctype/$fmt/* ; do
            lang=$(basename $lang_dir)
            echo "%lang($lang) $BT_DOC_DIR/$doctype/$fmt/$lang/*" >> %{name}.lang
        done
    done
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/info.%{name}.BibleTime.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/info.%{name}.BibleTime.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/display-templates/
%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/license/
%{_datadir}/%{name}/locale/
%{_datadir}/%{name}/pics/
%{_datadir}/metainfo/info.%{name}.BibleTime.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/info.%{name}.BibleTime.svg

%files doc -f %{name}.lang
%dir %{_docdir}/%{name}/
%dir %{_docdir}/%{name}/handbook/
%dir %{_docdir}/%{name}/howto/

%changelog
%autochangelog
