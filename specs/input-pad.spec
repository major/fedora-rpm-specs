%global have_pygobject3_devel 1
%global have_xtest_devel  1

%global sub_version             1.1
%global libxklavier_version     4.0
%global libxml2_version         2.0

%global libinput_paddir %{_libdir}/%{name}-%sub_version
%global moduledir       %{_libdir}/%{name}-%sub_version/modules
%global kbduidir        %{_libdir}/%{name}-%sub_version/modules/kbdui
%global xkeysenddir     %{_libdir}/%{name}-%sub_version/modules/xkeysend


Name:       input-pad
Version:    1.1.0
Release:    %autorelease
Summary:    On-screen Input Pad to Send Characters with Mouse
License:    LGPL-2.0-or-later
URL:        https://github.com/fujiwarat/input-pad/wiki
Source0:    https://github.com/fujiwarat/input-pad/releases/download/%{version}/%{name}-%{version}.tar.gz
# Patch0:     %%{name}-HEAD.patch


BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  gtk3-devel
BuildRequires:  libtool
BuildRequires:  libxkbfile-devel
BuildRequires:  libxklavier-devel       >= %libxklavier_version
BuildRequires:  libxml2-devel           >= %libxml2_version
BuildRequires:  pkgconfig
%if %have_xtest_devel
BuildRequires:  libXtst-devel
%endif
%if %have_pygobject3_devel
BuildRequires:  gobject-introspection-devel
%endif
BuildRequires: make
%if %have_pygobject3_devel
Requires:       gobject-introspection
Requires:       python3-gobject
%endif
Provides:       %{name}-xtest = %{version}-%{release}
Obsoletes:      %{name}-xtest < %{version}-%{release}

%description
The input pad is a tool to send a character on button to text applications.

%package devel
Summary:    Development tools for input-pad
Requires:   %{name} = %{version}-%{release}

%description devel
The input-pad-devel package contains the header files.


%prep
%setup -q
%autosetup -S git

%build
#autoreconf -v
%configure \
%if %have_xtest_devel
    --enable-xtest              \
%endif
    --disable-static
%make_build

%install
%make_install

if [ ! -d $RPM_BUILD_ROOT%kbduidir ] ; then
    mkdir -p $RPM_BUILD_ROOT%kbduidir
fi
if [ ! -d $RPM_BUILD_ROOT%xkeysenddir ] ; then
    mkdir -p $RPM_BUILD_ROOT%xkeysenddir
fi

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
%if %have_xtest_devel
rm -f $RPM_BUILD_ROOT%xkeysenddir/*.la
rm -f $RPM_BUILD_ROOT%xkeysenddir/*.a
%endif

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/input-pad
%dir %libinput_paddir
%dir %moduledir
%dir %xkeysenddir
%xkeysenddir/libinput-pad-xtest-gdk.so
%dir %kbduidir
%{_libdir}/libinput-pad-*.so.*
%if %have_pygobject3_devel
%{_libdir}/girepository-1.0/InputPad-%{sub_version}.typelib
%endif
%{_datadir}/%name
%{_datadir}/pixmaps/input-pad.png
%{_mandir}/man1/input-pad.1.gz

%files devel
%{_includedir}/%{name}-%sub_version
%{_libdir}/libinput-pad-*.so
%{_libdir}/pkgconfig/*.pc
%if %have_pygobject3_devel
%{_datadir}/gir-1.0/InputPad-%{sub_version}.gir
%endif

%changelog
%autochangelog
