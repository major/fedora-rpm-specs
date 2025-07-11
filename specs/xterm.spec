%bcond_with trace

Summary: Terminal emulator for the X Window System
Name: xterm
Version: 401
Release: %autorelease
URL: https://invisible-island.net/xterm
License: MIT AND X11 AND HPND AND CC-BY-4.0
BuildRequires: make
BuildRequires: gcc pkgconfig ncurses-devel libutempter-devel
BuildRequires: libXft-devel libXaw-devel libXext-devel desktop-file-utils
BuildRequires: libxkbfile-devel pcre2-devel pkgconfig(libpcre2-posix)
BuildRequires: gnupg2
Recommends: xorg-x11-fonts-misc

Source0: https://invisible-island.net/archives/xterm/%{name}-%{version}.tgz
Source1: https://invisible-island.net/archives/xterm/%{name}-%{version}.tgz.asc
Source2: https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc
Source3: https://invisible-island.net/archives/xterm/16colors.txt

Patch1: xterm-defaults.patch
Patch2: xterm-desktop.patch
Patch3: xterm-man-paths.patch

%global x11_app_defaults_dir %(pkg-config --variable appdefaultdir xt)

%description
The xterm program is a terminal emulator for the X Window System. It
provides DEC VT102 and Tektronix 4014 compatible terminals for
programs that can't use the window system directly.

%package resize
Summary: Set environment and terminal settings to current window size

%description resize
Prints a shell command for setting the appropriate environment variables to
indicate the current size of the window from which the command is run.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

for f in THANKS; do
	iconv -f iso8859-1 -t utf8 -o ${f}{_,} &&
		touch -r ${f}{,_} && mv -f ${f}{_,}
done

%build
%configure \
	--enable-meta-sends-esc \
	--disable-backarrow-key \
	--enable-exec-xterm \
%{?with_trace: --enable-trace} \
	--enable-warnings \
	--with-app-defaults=%{x11_app_defaults_dir} \
	--with-icon-theme=hicolor \
	--with-icondir=%{_datadir}/icons \
	--with-utempter \
	--with-tty-group=tty \
	--disable-full-tgetent \
	--with-pcre2 \
	--enable-readline-mouse \
	--enable-logging

%make_build

%install
%make_install

cp -fp %{SOURCE3} 16colors.txt

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
	--vendor=fedora \
%endif
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	xterm.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -m644 -p xterm.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata

%files
%doc xterm.log.html ctlseqs.txt 16colors.txt README.i18n THANKS
%{_bindir}/xterm
%{_bindir}/koi8rxterm
%{_bindir}/uxterm
%{_mandir}/man1/koi8rxterm.1*
%{_mandir}/man1/uxterm.1*
%{_mandir}/man1/xterm.1*
%{_datadir}/appdata/xterm.appdata.xml
%{_datadir}/applications/*xterm.desktop
%{_datadir}/icons/hicolor/*/apps/*xterm*
%{_datadir}/pixmaps/*xterm*.xpm
%{x11_app_defaults_dir}/KOI8RXTerm*
%{x11_app_defaults_dir}/UXTerm*
%{x11_app_defaults_dir}/XTerm*

%files resize
%{_bindir}/resize
%{_mandir}/man1/resize.1*

%changelog
%autochangelog
