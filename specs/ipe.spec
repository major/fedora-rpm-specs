%global majorversion 7.2

Name:           ipe
Version:        7.2.30
Release:        %autorelease
Summary:        Drawing editor for creating figures in PDF or PostScript formats
License:        GPL-3.0-or-later WITH CGAL-linking-exception
URL:            http://ipe.otfried.org/
Source0:        https://github.com/otfried/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         %{name}-%{version}-gcc11.patch

%if 0%{?fedora} >= 39
ExcludeArch:    %{ix86}
%endif

BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig
BuildRequires:	qt6-qtbase-devel
BuildRequires:	cairo-devel
BuildRequires:	freetype-devel
BuildRequires:	libpng-devel
BuildRequires:	lua-devel
BuildRequires:	curl-devel
BuildRequires:	gsl-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libspiro-devel
BuildRequires:	qtspell-qt6-devel
BuildRequires:	make

Requires:       tex(latex)
Requires:       urw-fonts
Requires:       xdg-utils
Requires:       qt5-qtsvg

Provides:       ipe(api) = %{version}
Provides:       ipetoipe = %{version}
Provides:       ipetopng = %{version}

%description
Ipe is a drawing editor for creating figures in PDF or (encapsulated)
Postscript format. It supports making small figures for inclusion into
LaTeX-documents as well as making multi-page PDF presentations that
can be shown on-line with a PDF viewer


%package devel
Summary: Development files and documentation for designing Ipelets
Requires: %{name} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description devel 
This packages contains the files necessary to develop Ipelets, which are
plugins for the Ipe editor.

%package doc
BuildArch: noarch
Summary: Documentation of Ipe
Requires: %{name} = %{version}-%{release}
%description doc
%{summary}.

%prep
%setup -n %{name}-%{version} -q
%patch 0 -p1

# fix files permissions
find src -type f -exec chmod -x {} +


%build
export QTDIR=%{qtdir}

pushd src
%make_build LUA_CFLAGS="`pkg-config --cflags lua`" \
     LUA_LIBS="`pkg-config --libs lua`" \
     MOC=/usr/lib64/qt6/libexec/moc \
     IPEPREFIX="%{_prefix}" IPELIBDIR="%{_libdir}" \
     IPELETDIR="%{_libdir}/%{name}/%{version}/ipelets" \
     IPECURL=1 IPEGSL=1
popd 


%install
pushd src
make INSTALL_ROOT=%{buildroot} install \
     IPEPREFIX="%{_prefix}" IPELIBDIR="%{_libdir}" \
     IPELETDIR="%{_libdir}/%{name}/%{version}/ipelets" \
     INSTALL_PROGRAMS="install -m 0755"
popd

# Install desktop file
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license doc/gpl.txt
%{_bindir}/ipe
%{_bindir}/ipe6upgrade
%{_bindir}/ipecurl
%{_bindir}/ipeextract
%{_bindir}/iperender
%{_bindir}/iperender-par
%{_bindir}/ipescript
%{_bindir}/ipetoipe
%{_bindir}/ipepresenter

%{_libdir}/libipe.so.%{version}
%{_libdir}/libipeui.so.%{version}
%{_libdir}/libipecairo.so.%{version}
%{_libdir}/libipecanvas.so.%{version}
%{_libdir}/libipelua.so.%{version}

%dir %{_libdir}/ipe
%{_libdir}/ipe/%{version}/ipelets/*

%dir %{_datadir}/ipe
%dir %{_datadir}/ipe/%{version}
%{_datadir}/ipe/%{version}/icons
%{_datadir}/ipe/%{version}/lua
%{_datadir}/ipe/%{version}/styles

%{_datadir}/applications/*%{name}*.desktop

%{_mandir}/man1/ipe.1.gz
%{_mandir}/man1/ipe6upgrade.1.gz
%{_mandir}/man1/ipeextract.1.gz
%{_mandir}/man1/iperender.1.gz
%{_mandir}/man1/ipescript.1.gz
%{_mandir}/man1/ipetoipe.1.gz

%files devel
%{_includedir}/*.h
%{_libdir}/libipe.so
%{_libdir}/libipeui.so
%{_libdir}/libipecairo.so
%{_libdir}/libipecanvas.so
%{_libdir}/libipelua.so

%files doc
%{_datadir}/%{name}/%{version}

%changelog
%autochangelog
