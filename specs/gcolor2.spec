Name:           gcolor2
Version:        0.4
Release:        %autorelease
Summary:        A simple color selector for GTK+2

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://gcolor2.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
# Patch extracted from
# http://patch-tracker.debian.org/patch/nondebian/dl/gcolor2/0.4-2.1
Patch0:         %{name}-0.4-missing-includes.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=716100
# bugs.debian.org/cgi-bin/bugreport.cgi?bug=634606
Patch1:         %{name}-0.4-ftbfs.patch
# fix for default -fno-common in GCC10
Patch2:         %{name}-0.4-gcc10.patch
Patch3:         gcolor2-configure-c99.patch
Patch4:         gcolor2-c99.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl(XML::Parser)

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
ExcludeArch:    %{ix86}
%endif

%description
gcolor2 is a simple color selector that was originally based on gcolor, 
ported to use GTK+2, and now has a completely new UI. 

%prep
%autosetup -p1
# make sure path to icon is correct
sed -i 's!/usr/share!%{_datadir}!' %{SOURCE1}


%build
%configure
%make_build


%install
%make_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}



%files
%doc AUTHORS ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
