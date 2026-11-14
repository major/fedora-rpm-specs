%global forgeurl https://gitlab.com/saalen/highlight
Version:        4.22
%forgemeta

Name:           highlight
Summary:        Universal source code to formatted text converter
Release:        %autorelease
License:        GPL-3.0-only
URL:            http://www.andre-simon.de/
Source0:        %{forgesource}

# https://gitlab.com/saalen/highlight/-/merge_requests/177
Patch0:         meson-gui-lspconf.patch

# The meson GUI is built with Qt; disable it on RHEL < 10 (no Qt6).
%bcond qt %[%{undefined rhel} || 0%{?rhel} < 10]

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  lua-devel
BuildRequires:  meson
%if %{with qt}
BuildRequires:  qt6-qtbase-devel
%endif

%global __provides_exclude ^perl\\(
%global __requires_exclude ^(perl\\(|/bin/lua)

%description
A utility that converts sourcecode to HTML, XHTML, RTF, LaTeX, TeX,
XSL-FO, XML or ANSI escape sequences with syntax highlighting.
It supports several programming and markup languages.
Language descriptions are configurable and support regular expressions.
The utility offers indentation and reformatting capabilities.
It is easily possible to create new language definitions and colour themes.

%if %{with qt}
%package gui
Summary:        GUI for the highlight source code formatter
Requires:       %{name} = %{version}-%{release}

%description gui
A Qt-based GUI for the highlight source code formatter source.
%endif

%prep
%forgeautosetup -p1
# Fix line endings of extra batch files to avoid rpmlint warnings
find extras/ -type f -name "*.bat" -exec sed -i 's/\r$//' {} +
find extras/ -type f -name "*.pb" -exec sed -i 's/\r$//' {} +

# Fix duplicate UNLICENCE file by symlinking it relatively
rm -f extras/themes-resources/css-themes/UNLICENCE
ln -s ../../langDefs-resources/UNLICENCE extras/themes-resources/css-themes/UNLICENCE

%build
# The GUI build is gated on Qt6 availability (see meson-gui-lspconf.patch)
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_licensedir}/%{name}
mv %{buildroot}%{_docdir}/%{name}/COPYING %{buildroot}%{_licensedir}/%{name}/

%check
# Upstream test suite (src/ci_test.sh) requires network (git clone), so run a
# basic smoke test of the built binary instead
printf 'print("hello")' > test.py
%{buildroot}%{_bindir}/highlight --version
grep -q 'hello' <(%{buildroot}%{_bindir}/highlight test.py)

%if %{with qt}
desktop-file-validate %{buildroot}%{_datadir}/applications/highlight.desktop
%endif

%files
%{_bindir}/highlight
%{_datadir}/highlight/
%{_mandir}/man1/highlight.1*
%{_mandir}/man5/filetypes.conf.5*
%{_datadir}/bash-completion/completions/highlight
%{_datadir}/fish/vendor_completions.d/highlight.fish
%{_datadir}/zsh/site-functions/_highlight
%config(noreplace) %{_sysconfdir}/highlight/

%doc ChangeLog* AUTHORS README* INSTALL extras/
%license COPYING

%if %{with qt}
%files gui
%{_bindir}/highlight-gui
%{_datadir}/applications/highlight.desktop
%{_datadir}/icons/hicolor/256x256/apps/highlight.png
%endif

%changelog
%autochangelog
