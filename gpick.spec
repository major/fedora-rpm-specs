%global commit 0e858d33fd28d98d2689d0ebb92c975729a9f7bc
%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%global date 20210528

Name:		gpick
Version:	0.2.6
Release:	%autorelease -b 4 -s %{date}git%{shortcommit}
Summary:	Advanced color picker

License:	BSD
URL:		http://gpick.org

%{?shortcommit:
Source:		https://github.com/thezbyg/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz}
%{!?shortcommit:
Source:		https://github.com/thezbyg/%{name}/archive/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz}

BuildRequires:	gcc-c++
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils 
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:  make
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(openthreads)
BuildRequires:	ragel


%description
Advanced color picker

%prep
%{?shortcommit:
%autosetup -p1 -n %{name}-%{commit}}
%{!?shortcommit:
%autosetup -n %name-%{name}-%{version}}
mkdir .git

# Delete external libraries and only use system dependencies to build GPick
rm -rf extern
echo "INTERNAL_EXPAT=False" >> user-config.py
echo "INTERNAL_LUA=False" >> user-config.py
echo "LOCALEDIR=\"%{_datadir}/locale\"" >> user-config.py

%build
%cmake \
	-DCFLAGS="%{optflags} -Wl,--as-needed" \
	-DCXXFLAGS="%%{optflags} -Wl,--as-needed --std=c++17" \
	-DLDFLAGS="%%{optflags} -Wl,--as-needed"
%cmake_build

%install
%cmake_install

# copy libraries
#mkdir -p %%{buildroot}%%{_libdir}
#cp -p %%{_builddir}/%%{name}-%%{version}/*.so %%{buildroot}%%{_libdir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%find_lang %{name}

%files -f %{name}.lang
%doc %{_docdir}/%{name}/copyright
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
