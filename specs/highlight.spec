%global forgeurl https://gitlab.com/saalen/highlight
Version:        4.21
%forgemeta

Name:           highlight
Summary:        Universal source code to formatted text converter
Release:        %autorelease
License:        GPL-3.0-only
URL:            http://www.andre-simon.de/
Source0:        %{forgesource}

%bcond qt %[%{undefined rhel} || 0%{?rhel} < 10]

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  lua-devel
BuildRequires:  make
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
%forgeautosetup
# Fix line endings of extra batch files to avoid rpmlint warnings
find extras/ -type f -name "*.bat" -exec sed -i 's/\r$//' {} +
find extras/ -type f -name "*.pb" -exec sed -i 's/\r$//' {} +

# Fix duplicate UNLICENCE file by symlinking it relatively
rm -f extras/themes-resources/css-themes/UNLICENCE
ln -s ../../langDefs-resources/UNLICENCE extras/themes-resources/css-themes/UNLICENCE

%build
%set_build_flags
# The makefile compiles C++ files using CFLAGS, so we add CXXFLAGS to CFLAGS in the environment
export CFLAGS="$CFLAGS $CXXFLAGS -fPIC"

%make_build all \
    PREFIX="%{_prefix}" \
    conf_dir="%{_sysconfdir}/"

%if %{with qt}
cd src/gui-qt
%qmake_qt6
%make_build
cd ../..
%endif

%install
%make_install PREFIX="%{_prefix}" conf_dir="%{_sysconfdir}/"

%if %{with qt}
make install-gui DESTDIR=%{buildroot} PREFIX="%{_prefix}" conf_dir="%{_sysconfdir}/"
%endif

rm -rf %{buildroot}%{_docdir}/%{name}/

%check
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

%doc ChangeLog* AUTHORS README* extras/
%license COPYING

%if %{with qt}
%files gui
%{_bindir}/highlight-gui
%{_datadir}/applications/highlight.desktop
%{_datadir}/icons/hicolor/256x256/apps/highlight.png
%endif


%changelog
%autochangelog
