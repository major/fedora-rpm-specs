%global commit 274745c23398554acc3cf40fefb2ce5ce3c21197
%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%global date 20251201

Name:		gpick
Version:	0.4
Release:	%autorelease -b 1 -s %{date}git%{shortcommit}
Summary:	Advanced color picker

License:	BSD-3-Clause
URL:		http://gpick.org

%{?shortcommit:
Source:		https://github.com/thezbyg/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz}
%{!?shortcommit:
Source:		https://github.com/thezbyg/%{name}/archive/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz}

# https://github.com/thezbyg/gpick/pull/238
Patch0:		gpick-0.4-lua-5.5.patch

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

echo "%{version}" > .version

%build
%cmake \
	-DCFLAGS="%{optflags} -Wl,--as-needed" \
	-DCXXFLAGS="%%{optflags} -Wl,--as-needed --std=c++17" \
	-DLDFLAGS="%%{optflags} -Wl,--as-needed" \
	-DPREFER_VERSION_FILE=True \
	-DLUA_TYPE="C"
%cmake_build

%install
%cmake_install

# copy libraries
#mkdir -p %%{buildroot}%%{_libdir}
#cp -p %%{_builddir}/%%{name}-%%{version}/*.so %%{buildroot}%%{_libdir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.%{name}.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%doc %{_docdir}/%{name}/copyright
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_metainfodir}/org.%{name}.%{name}.metainfo.xml
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_datadir}/mime/packages/org.%{name}.%{name}.xml
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
