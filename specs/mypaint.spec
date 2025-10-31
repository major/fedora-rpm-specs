Name:           mypaint
Version:        2.0.1
Release:        %autorelease
Summary:        A fast and easy graphics application for digital painters

# MyPaint is GPLv2+, brush library LGPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ and CC-BY - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-CC-BY
URL:            http://mypaint.org
Source0:        https://github.com/mypaint/mypaint/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Backport of https://github.com/mypaint/mypaint/pull/1183
Patch0:         0001-setuptools-fixes.patch
# https://github.com/mypaint/mypaint/pull/1193
Patch1:         0002-python311.patch
# Backport of https://github.com/mypaint/mypaint/pull/1259
Patch2:         0003-fix-deprecations.patch
# https://github.com/mypaint/mypaint/issues/1292
Patch3:         0004-pygobject352.patch
# Backport of https://github.com/mypaint/mypaint/pull/1300
Patch4:         0005-numpy23.patch

BuildRequires:  gcc, gcc-c++

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-scons >= 3.0
BuildRequires:  swig
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  python3-numpy
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(mypaint-brushes-2.0)

Requires:       python3
Requires:       python3-numpy%{?_isa}
Requires:       python3-protobuf
Requires:       python3-gobject%{?_isa}
Requires:       %{name}2-brushes
Requires:       %{name}-data = %{version}-%{release}

%description
MyPaint is a fast and easy graphics application for digital painters. It lets
you focus on the art instead of the program. You work on your canvas with
minimum distractions, bringing up the interface only when you need it.


%package        data
Summary:        Common data files for for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    data
The %{name}-data package contains common data files for %{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

# for 64 bit
sed -i 's|lib/mypaint|%{_lib}/mypaint|g' mypaint.py
sed -i "s|'lib', 'mypaint'|'%{_lib}', 'mypaint'|" mypaint.py

%build
%{__python3} setup.py build_ext
%{__python3} setup.py build_py
%{__python3} setup.py build_translations
%{__python3} setup.py build_config

%install
%{__python3} setup.py managed_install --prefix=%{buildroot}%{_prefix}
[[ %{_lib} != lib ]] && mv %{buildroot}%{_prefix}/lib %{buildroot}%{_prefix}/%{_lib}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'


%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc Changelog.md README*
%{_bindir}/%{name}
%{_bindir}/%{name}-ora-thumbnailer
%{_datadir}/thumbnailers
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/actions/*.svg
%{_datadir}/icons/hicolor/*/actions/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg

%files data
%{_datadir}/%{name}/backgrounds
%{_datadir}/%{name}/palettes
%{_datadir}/%{name}/pixmaps

%changelog
%autochangelog
