%if 0%{!?_with_xfce:1} && 0%{!?_without_xfce:1}
%if 0%{?rhel}
%global _with_xfce 0
%else
%global _with_xfce 1
%endif
%endif

Name:		im-chooser
Version:	1.7.7
Release:	%autorelease
License:	GPL-2.0-or-later AND LGPL-2.0-or-later
URL:		http://pagure.io/im-chooser/
%{?_with_gtk2:BuildRequires:	gtk2-devel}
%{!?_with_gtk2:BuildRequires:	gtk3-devel}
BuildRequires:	libSM-devel imsettings-devel >= 1.8.9
%if 0%{?_with_xfce}
BuildRequires:	libxfce4util-devel
%endif
BuildRequires:	desktop-file-utils gettext
BuildRequires:	gcc
BuildRequires: make

Source0:	http://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2

Summary:	Desktop Input Method configuration tool
Obsoletes:	im-chooser-gnome3 < 1.4.2-2
Provides:	im-chooser-gnome3 = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%description
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

%package	common
Summary:	Common files for im-chooser subpackages
Requires:	imsettings >= 1.8.9
Obsoletes:	im-chooser < 1.5.0.1
## https://fedorahosted.org/fpc/ticket/174
Provides:	bundled(egglib)

%description	common
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

This package contains the common libraries/files to be used in
im-chooser subpackages.

%if 0%{?_with_xfce}
%package	xfce
Summary:	XFCE settings panel for im-chooser
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	im-chooser < 1.5.0.1

%description	xfce
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

This package contains the XFCE settings panel for im-chooser.
%endif


%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/im-chooser.desktop
%if 0%{?_with_xfce}
desktop-file-validate %{buildroot}%{_datadir}/applications/xfce4-im-chooser.desktop
%endif
#%%{!?_with_gtk2:desktop-file-validate %{buildroot}%%{_datadir}/applications/im-chooser-panel.desktop}

rm -rf %{buildroot}%{_libdir}/libimchooseui.{so,la,a}
#%%{!?_with_gtk2:rm -rf %{buildroot}%%{_libdir}/control-center-1/panels/libim-chooser.{a,la}}

# disable panel so far
rm -rf %{buildroot}%{_libdir}/control-center-1/panels/libim-chooser.so
rm -rf %{buildroot}%{_datadir}/applications/im-chooser-panel.desktop

%find_lang %{name}


%ldconfig_scriptlets	common

%files
%{_bindir}/im-chooser
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-im-chooser.desktop
%else
%{_datadir}/applications/im-chooser.desktop
%endif
%{_mandir}/man1/im-chooser.1*

%files	common -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/libimchooseui.so.*
%{_datadir}/icons/hicolor/*/apps/im-chooser.png
%dir %{_datadir}/imchooseui
%{_datadir}/imchooseui/imchoose.ui

%if 0%{?_with_xfce}
%files	xfce
%{_bindir}/xfce4-im-chooser
%{_datadir}/applications/xfce4-im-chooser.desktop
%endif

%changelog
%autochangelog
