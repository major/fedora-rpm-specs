%global debug_package %{nil}

# rhbz #1923589
%define _legacy_common_support 1
%global _lto_cflags %nil

# prefer new (rpm >= 4.11) macrosdir if present
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] ||
d=%{_sysconfdir}/rpm; echo $d)

Name:           gnustep-make
Version:        2.9.3
Release:        %autorelease
Summary:        GNUstep makefile package
License:        GPL-3.0-or-later
URL:            https://www.gnustep.org/
Source0:        https://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz

# Taken from git://fedorahosted.org/git/gnustep-rpm-macros.git
Source1:        %{name}-macros.gnustep

BuildRequires:  gcc-objc
BuildRequires:  texinfo-tex tetex-latex tetex-dvips latex2html texi2html
BuildRequires:  make
Requires:       gnustep-filesystem%{?_isa} = %{version}-%{release}


%description
The makefile package is a simple, powerful and extensible way to write
makefiles for a GNUstep-based project.  It allows the user to write a
project without having to deal with the complex issues associated with
configuration, building, installation, and packaging.  It also allows
the user to easily create cross-compiled binaries.


%package -n     gnustep-filesystem
Summary:        The basic directory layout for GNUstep packages
License:        LicenseRef-Not-Copyrightable

%description -n gnustep-filesystem
The gnustep-filesystem package contains the basic directory layout for
GNUstep packages.


%package        doc
Summary:        Documentation for %{name}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
BuildArch:      noarch
Requires:       gnustep-filesystem = %{version}-%{release}

%description    doc
The makefile package is a simple, powerful and extensible way to write
makefiles for a GNUstep-based project.  It allows the user to write a
project without having to deal with the complex issues associated with
configuration, building, installation, and packaging.  It also allows
the user to easily create cross-compiled binaries.
This package contains documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

cp %{SOURCE1} macros.gnustep

sed -i "s|/@libdir@|/%{_lib}|g" FilesystemLayouts/fhs-system
sed -i "s|/@libdir@|/%{_lib}|g" FilesystemLayouts/fhs

# /usr/share/GNUstep/Makefiles/config-noarch.make and
# /usr/share/GNUstep/Makefiles/ix86/linux-gnu/gnu-gnu-gnu/config.make
# are spoiling a pure /usr/share install
sed -i "s|=/share/GNUstep/Makefiles|=/%{_lib}/GNUstep/Makefiles|" \
    FilesystemLayouts/fhs-system

# Fix files location except GNUSTEP_LOCAL_*
sed -i "67,77!s|=/local|=|" FilesystemLayouts/fhs-system 

%build
%if 0%{?rhel} >= 8
export CC=gobjc
%endif

%configure --with-layout=fhs-system --enable-flattened
%make_build V=1

%install
%make_install GNUSTEP_INSTALLATION_DOMAIN=SYSTEM
%make_install -C Documentation GNUSTEP_INSTALLATION_DOMAIN=SYSTEM GNUSTEP_MAKEFILES=%{buildroot}%{_libdir}/GNUstep/Makefiles
%make_install -C Documentation GNUSTEP_INSTALLATION_DOMAIN=SYSTEM GNUSTEP_MAKEFILES=%{buildroot}%{_libdir}/GNUstep/Makefiles

# create remaining GNUstep directories
for i in Applications WebApplications; do
    mkdir -p %{buildroot}%{_prefix}{,/local}/lib{,64}/GNUstep/$i
done
mkdir -p %{buildroot}%{_prefix}{,/local}/share/GNUstep/Documentation/Developer

# INstall rpm macros
install -d %{buildroot}%{macrosdir}
install -p -m 644 macros.gnustep %{buildroot}%{macrosdir}

%files
%config(noreplace) %{_sysconfdir}/GNUstep/GNUstep.conf
%{_bindir}/gnustep-config
%{_bindir}/gnustep-tests
%{_bindir}/openapp
%{_bindir}/debugapp
%{_bindir}/opentool
%{_libdir}/GNUstep/Makefiles/*
%{_mandir}/man*/*
%{_infodir}/gnustep*.info*
%{macrosdir}/macros.gnustep

%files -n gnustep-filesystem
%doc ANNOUNCE FAQ NEWS README
%license COPYING
%dir %{_sysconfdir}/GNUstep
%dir %{_libdir}/GNUstep
%dir %{_libdir}/GNUstep/Makefiles
%dir %{_libdir}/GNUstep/Applications
%dir %{_libdir}/GNUstep/WebApplications
%dir %{_datadir}/GNUstep
%dir %{_datadir}/GNUstep/Documentation
%dir %{_datadir}/GNUstep/Documentation/Developer

%files doc
%doc %{_datadir}/GNUstep/Documentation/*

%changelog
%autochangelog
