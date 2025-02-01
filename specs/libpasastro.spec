# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global forgeurl https://github.com/pchev/libpasastro/

Version:        1.4.3
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

# Make sure Fedora's C(XX)FLAGS and LDFLAGS are applied
Patch2:         apply_fedora_archflags.patch
# https://github.com/pchev/libpasastro/pull/4
Patch3:         fix_gcc15-c++23.patch

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
%make_build arch_flags="%{optflags}"


%install
make install PREFIX=%{buildroot}%{_prefix}


%files
%doc changelog copyright README.md
%{_libdir}/libpas*.so.1
%{_libdir}/libpas*.so.1.1


%changelog
%autochangelog
