%global debug_package %{nil}
%bcond_without  gui
# Fedora has Qt6
# EPEL9+ has Qt6, but RHEL9 and CentOS Stream 9 do not, while their 10 versions do
%if (0%{?rhel} && 0%{?rhel} < 10)
%global qt_ver 5
%global qmake %{_qt5_qmake}
%else
%global qt_ver 6
%global qmake %{_qt6_qmake}
%endif

Name:           ansifilter
Version:        2.22
Release:        %autorelease
Summary:        ANSI terminal escape code converter
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.andre-simon.de/doku/ansifilter/ansifilter.php
Source0:        http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
%if %{with gui}
Source1:        ansifilter.desktop
Source2:        http://www.andre-simon.de/img/af_icon.png
%endif

%description
Ansifilter handles text files containing ANSI terminal escape codes. The
command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

%if %{with gui}
%package        gui
Summary:        GUI for %{name} based on Qt5
BuildRequires:  desktop-file-utils
BuildRequires:  qt%{qt_ver}-qtbase-devel
BuildRequires: make

%description    gui
Ansifilter handles text files containing ANSI terminal escape codes. The
command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

This is a GUI of %{name} based on Qt%{qt_ver}.
%endif

%prep
%autosetup

# Preserve timestamps.
sed -i 's|install -m|install -pm|g' makefile

%if %{with gui}
# Remove pre-configured files which may cause errors during building.
rm -frv src/qt-gui/moc_*.cpp
rm -frv src/qt-gui/Makefile*
%endif

# CRLF quickfix
find . -type f -exec sed -i 's/\r$//' {} + -print

%build
# Upstream embeds the cli code in gui so no need to require cli to use GUI
# program, in order to achieve this we need to preserve the objects with -c.
%make_build CFLAGS+="%{optflags} -c" LDFLAGS="%{?__global_ldflags}"

%if %{with gui}
# %%_qt5/6_qmake will respect the redhat-rpm-config
%make_build all-gui QMAKE="%{qmake}"
%endif

%install
%make_install

%if %{with gui}
make install-gui DESTDIR=%{buildroot}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
install -pDm644 %{S:2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%endif

# Use %%doc and %%license to handle docs.
rm -frv %{buildroot}%{_docdir}

%files
%doc ChangeLog* README*
%license COPYING
%{_bindir}/ansifilter
%{_mandir}/man1/ansifilter.1*
%{_datadir}/bash-completion/completions/ansifilter
%{_datadir}/fish/vendor_completions.d/ansifilter.fish
%{_datadir}/zsh/site-functions/_ansifilter

%if %{with gui}
%files gui
%doc ChangeLog* README*
%license COPYING
%{_bindir}/ansifilter-gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ansifilter.*
%endif

%changelog
%autochangelog
