%global modname ReText

Name:           retext
Version:        8.1.0
Release:        %autorelease
Summary:        Simple editor for Markdown and reStructuredText

# BSD-2-clause:
#   - ReText/mdx_posmap.py
# GPL-3.0-or-later:
#   - ReText/icons/*-*.png
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND BSD-2-Clause
URL:            https://github.com/retext-project/retext
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Man pages are taken from the Debian package.
Source1:        %{name}.1

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  ImageMagick
BuildRequires:  python3-devel

Requires:       hicolor-icon-theme

%description
ReText is simple text editor that supports Markdown and reStructuredText markup
languages. It is written in Python using PyQt libraries. It supports live
preview, tabs, math formulas, export to various formats including PDF and
HTML.

%prep
%autosetup

# Remove shebang from Python module
sed -i '1{/^#!/d;}' ReText/__main__.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{modname}

mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 0644 %SOURCE1 %{buildroot}/%{_mandir}/man1

# Generate resized icons
pushd ReText/icons
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/{16x16,22x22,24x24,32x32,48x48,64x64,72x72,96x96,128x128,scalable}/apps
for s in 16x16 22x22 24x24 32x32 48x48 64x64 72x72 96x96 128x128
do
    convert ./retext.png -resize $s %{buildroot}/%{_datadir}/icons/hicolor/$s/apps/retext.png;
done
install -p -m 0644 retext.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
popd

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{_builddir}/%{name}-%{version}/data/me.mitya57.ReText.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/me.mitya57.ReText.metainfo.xml


%files -f %{pyproject_files}
%doc changelog.md configuration.md README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/me.mitya57.ReText.metainfo.xml
%{_datadir}/applications/me.mitya57.ReText.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/*.1.*


%changelog
%autochangelog
