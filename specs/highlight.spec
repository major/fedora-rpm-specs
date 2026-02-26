Name:           highlight
Summary:        Universal source code to formatted text converter
Version:        4.19
Release:        %autorelease
License:        GPL-3.0-only
URL:            http://www.andre-simon.de/
Source0:        http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2

%bcond qt %[%{undefined rhel} || 0%{?rhel} < 10]

BuildRequires:  gcc-c++
%if %{with qt}
BuildRequires:  qt5-qtbase-devel
%endif
BuildRequires:  lua-devel, boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make

%{?filter_setup:
%filter_from_provides /^perl(/d;
%filter_from_requires /^perl(/d;
%filter_from_requires /^\/bin\/lua/d;
%filter_setup
}

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
%autosetup

%build
CFLAGS="$CFLAGS -fPIC %{optflags}"; export CFLAGS
CXXFLAGS="$CXXFLAGS -fPIC %{optflags}"; export CXXFLAGS
LDFLAGS="$LDFLAGS %{?__global_ldflags}"; export LDFLAGS

# disabled paralell builds to fix FTBFS on rawhide & highlight 3.52+
#make_build all gui           CFLAGS="${CFLAGS}"          \
 %{__make} all                CFLAGS="${CFLAGS}"          \
                              CXXFLAGS="${CXXFLAGS}"      \
                              LDFLAGS="${LDFLAGS}"        \
                              LFLAGS="-Wl,-O1 ${LDFLAGS}" \
                              PREFIX="%{_prefix}"         \
                              conf_dir="%{_sysconfdir}/"

%if %{with qt}
 %{__make} gui                CFLAGS="${CFLAGS}"          \
                              CXXFLAGS="${CXXFLAGS}"      \
                              LDFLAGS="${LDFLAGS}"        \
                              LFLAGS="-Wl,-O1 ${LDFLAGS}" \
                              PREFIX="%{_prefix}"         \
                              conf_dir="%{_sysconfdir}/" \
                              QMAKE="%{_qt5_qmake}"       \
                              QMAKE_STRIP=
%endif

%install
%make_install PREFIX="%{_prefix}" conf_dir="%{_sysconfdir}/"

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%if %{with qt}
make install-gui DESTDIR=$RPM_BUILD_ROOT PREFIX="%{_prefix}" conf_dir="%{_sysconfdir}/"
%endif

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}/

desktop-file-install \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
   highlight.desktop

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
%else
%exclude %{_datadir}/applications/highlight.desktop
%endif


%changelog
%autochangelog
