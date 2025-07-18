Name: rednotebook
Version: 2.39
Release: %autorelease
Summary: Daily journal with calendar, templates and keyword searching

License: GPL-2.0-or-later
URL: http://rednotebook.sourceforge.net
Source0: https://github.com/jendrikseipp/rednotebook/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: desktop-file-utils

Requires: python3-PyYAML
Requires: webkit2gtk4.1
Requires: python3-chardet
Requires: python3-enchant
Requires: hicolor-icon-theme
Requires: gtksourceview4

%generate_buildrequires
%pyproject_buildrequires

%description
RedNotebook is a modern desktop journal. It lets you format, tag and
search your entries. You can also add pictures, links and customizable
templates, spell check your notes, and export to plain text, HTML,
Latex or PDF.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
desktop-file-install                                    \
    --add-category="Calendar"                           \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}/%{_datadir}/appdata/
mv %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
# Be careful to not list locales twice
%dir %{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}/*.py*
%{python3_sitelib}/%{name}/external/
%{python3_sitelib}/%{name}/files/
%{python3_sitelib}/%{name}/gui/
%{python3_sitelib}/%{name}/images/
%{python3_sitelib}/%{name}/util/
%{python3_sitelib}/%{name}*.dist-info
%{python3_sitelib}/%{name}/__pycache__

%changelog
%autochangelog
