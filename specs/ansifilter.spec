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
License:        GPL-3.0-or-later
URL:            http://www.andre-simon.de/doku/ansifilter/ansifilter.php
Source0:        http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2
%if %{with gui}
Source1:        ansifilter.desktop
Source2:        http://www.andre-simon.de/img/af_icon.png
%endif

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  desktop-file-utils

%description
Ansifilter handles text files containing ANSI terminal escape codes. The
command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

%if %{with gui}
%package        gui
Summary:        GUI for %{name} based on Qt%{qt_ver}
BuildRequires:  qt%{qt_ver}-qtbase-devel

%description    gui
Ansifilter handles text files containing ANSI terminal escape codes. The
command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

This is a GUI of %{name} based on Qt%{qt_ver}.
%endif

%prep
%autosetup

# CRLF quickfix
find . -type f -exec sed -i 's/\r$//' {} +

%build
# Upstream embeds the cli code in gui so no need to require cli to use GUI
# program, in order to achieve this we need to preserve the objects with -c.
%make_build CXXFLAGS+="%{optflags}" LDFLAGS="%{?__global_ldflags}"

%if %{with gui}
# %%_qt5/6_qmake will respect the redhat-rpm-config
pushd src/qt-gui
%{qmake} ansifilter-gui.pro \
    "QMAKE_CXXFLAGS+=%{optflags}" \
    "QMAKE_LFLAGS+=%{?__global_ldflags}"
%make_build
popd
%endif

%install
%make_install \
    INSTALL_DATA="install -p -m644" \
    INSTALL_PROGRAM="install -p -m755"

%if %{with gui}
%make_install install-gui \
    INSTALL_DATA="install -p -m644" \
    INSTALL_PROGRAM="install -p -m755" \
    DESTDIR=%{buildroot}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
install -pDm644 %{S:2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%endif

# Use %%doc and %%license to handle docs.
rm -rf %{buildroot}%{_docdir}/ansifilter

%files
%doc ChangeLog.adoc README.adoc
%license COPYING
%{_bindir}/ansifilter
%{_mandir}/man1/ansifilter.1*
%{_datadir}/bash-completion/completions/ansifilter
%{_datadir}/fish/vendor_completions.d/ansifilter.fish
%{_datadir}/zsh/site-functions/_ansifilter

%if %{with gui}
%files gui
%doc ChangeLog.adoc README.adoc
%license COPYING
%{_bindir}/ansifilter-gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ansifilter.*
%endif

%changelog
%autochangelog
