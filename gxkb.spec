Name: gxkb
Version: 0.9.5
Release: %autorelease
Summary: X11 keyboard indicator and switcher

License: GPL-2.0-or-later
URL: https://github.com/zen-tools/gxkb
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: make

BuildRequires: pkgconfig(glib-2.0) >= 2.16.0
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(libxklavier) >= 5.0

%description
gxkb is a tiny indicator applet which allows to quickly switch between
different keyboard layouts in X. A flag corresponding to the country of the
active layout is shown in the indicator area. The applet is written in C and
uses GTK+ library and therefore does not depend on any GNOME components.


%prep
%autosetup -p1


%build
./autogen.sh
%configure \
    --enable-appindicator=no
%make_build


%install
%make_install

# Move license file in proper location
mkdir -p %{buildroot}%{_licensedir}/%{name}/
mv %{buildroot}%{_docdir}/%{name}/COPYING %{buildroot}%{_licensedir}/%{name}/
# Copy README.md to bypass "file listed twice" by rpm %doc macros
cp -p README.md %{buildroot}%{_docdir}/%{name}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.xpm
%{_docdir}/%{name}/
%{_licensedir}/%{name}/
%{_mandir}/man1/*.1*


%changelog
%autochangelog
