%global forgeurl https://github.com/pchev/libpasastro/

Version:        1.4.2
%forgemeta

Name:           libpasastro
Release:        %autorelease
Summary:        Pascal interface for standard astronomy libraries

License:        GPL-2.0-or-later AND LGPL-2.1-only AND BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

# Patch to fix stripping of library files
# Since this is Fedora specific we don't ask upstream to include
Patch1:         libpasastro-1.3-nostrip.patch

# Add LDFLAGS to compiler
Patch2:         libpasastro-1.4-ldflags.patch

BuildRequires:  gcc-c++
BuildRequires:  make

Provides:       bundled(wcstools) = 3.9.5

%description
Libpasastro provides shared libraries to interface Pascal program 
with standard astronomy libraries.
libpasgetdss.so : Interface with GetDSS to work with DSS images.
libpasplan404.so : Interface with Plan404 to compute planets position.
libpaswcs.so : Interface with libwcs to work with FITS WCS.


%prep
%forgeautosetup -p1

# do not install docs, use %%doc macro
sed -i '/\$destdir\/share/d' ./install.sh

# fix library path in install.sh script on 64bit
sed -i 's/\$destdir\/lib/\$destdir\/%{_lib}/g' ./install.sh


%build
%global build_type_safety_c 0
%make_build arch_flags="%{optflags}" FED_LDFLAGS="%{build_ldflags}"


%install
make install PREFIX=%{buildroot}%{_prefix}


%files
%doc changelog copyright README.md
%{_libdir}/libpas*.so.1
%{_libdir}/libpas*.so.1.1


%changelog
%autochangelog
