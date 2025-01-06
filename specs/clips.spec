%global sover 2

Summary:	Language for developing expert systems
Name:		clips
# Versioning scheme changed 6.31 -> 6.4.1
Epoch:    1
Version:	6.4.1
%global stripped_version %{lua: print((rpm.expand("%{version}"):gsub("%.", "")))}

Release:	%{autorelease}
Url:		http://clipsrules.sourceforge.net
License:	MIT-0
Source0:  https://downloads.sourceforge.net/clipsrules/CLIPS/%{version}/clips_core_source_%{stripped_version}.tar.gz
Source1:  https://downloads.sourceforge.net/clipsrules/CLIPS/%{version}/clips_documentation_%{stripped_version}.tar.gz
Patch0:   clips.shared-lib.patch
BuildRequires:  gcc-c++
BuildRequires:	ncurses-devel 
BuildRequires:	libXt-devel libXext-devel libXmu-devel libXaw-devel 
BuildRequires:	xorg-x11-proto-devel xorg-x11-xbitmaps 
BuildRequires:	desktop-file-utils
BuildRequires:	automake autoconf libtool
BuildRequires:	pkgconfig
BuildRequires:	ImageMagick
BuildRequires: make

Obsoletes: %{name}-xclips < 6.31-1
Obsoletes: %{name}-emacs < 6.31-1

%define _legacy_common_support 1

%description
CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

This package provides the CLIPS command line environment and the clips
library.

%package	libs
Summary:	Run-time C libraries for CLIPS applications

%description	libs
This package contains the run-time libraries needed for CLIPS applications.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

%package	devel
Summary:	C headers for developing programs that will embed CLIPS
Requires:	clips-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	ncurses-devel pkgconfig

%description	devel
This package contains the libraries and header files needed for
developing embedded CLIPS applications.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

%package	doc
Summary:	Documentation and examples for the CLIPS expert system
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:	noarch
%endif

%description	doc
This package contains documentation for the CLIPS library as well as numerous 
examples.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

The following are some of the documents in this package:
- Proceedings of the Third Conference on CLIPS, 1994 (3CCP.pdf)
- Application abstracts (abstract.pdf)
- CLIPS Reference Manual, Volume I, Basic Programming Guide (bpg.pdf,bpg.htm)
- CLIPS Reference Manual, Volume II, Adv. Programming Guide (apg.pdf, apg.htm)
- CLIPS Reference Manual, Volume III, Interfaces Guide (ig.pdf,ig.htm)
- CLIPS Architecture Manual (arch5-1.pdf)
- CLIPS Users Guide (ug.pdf,ug.htm)

%prep
%autosetup -p1 -n clips_core_source_%{stripped_version} -a 1
%{__mv} clips_documentation_%{stripped_version} documentation

%build
cd core
%{__make} %{?_smp_mflags}

# This is a terrible way to create a pkgconfig file, but upstream does not provide one.
sed -i 's$^prefix=.*$prefix=%{_prefix}$' clips-6.pc
sed -i 's$^libdir=.*$libdir=%{_libdir}$' clips-6.pc
sed -i 's$^includedir=.*$includedir=%{_includedir}$' clips-6.pc
sed -i 's$^Version:.*$Version: %{version}$' clips-6.pc

%install
cd core
%{__install} -p --mode=0755 -D -t %{buildroot}/%{_bindir} clips
%{__install} -p --mode=0755 -D -t %{buildroot}/%{_libdir} libclips.so.%{sover}
ln -s libclips.so.%{sover} %{buildroot}/%{_libdir}/libclips.so
%{__install} -p --mode=0644 -D -t %{buildroot}/%{_includedir}/%{name} *.h
%{__install} -p --mode=0644 -D -t %{buildroot}/%{_libdir}/pkgconfig clips-6.pc


%files
%{_bindir}/clips

%files libs
%{_libdir}/*.so.*
%license readme.txt

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}/

%files doc
%doc documentation/*

%changelog
%autochangelog
