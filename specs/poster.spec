Summary:        Scales PostScript images to span multiple pages
Name:           poster
Version:        20060221
Release:        %autorelease
License:        GPL-2.0-only
Source:         ftp://ftp.kde.org/pub/kde/printing/%{name}.tar.bz2
URL:            https://web.archive.org/web/20110122073259/http://printing.kde.org/downloads/

# Fixes a gs crash, see https://bugzilla.redhat.com/show_bug.cgi?id=436969
Patch0:         poster.fixes_gs_crash.patch

BuildRequires:  gcc
%description
Poster scales PostScript images to a larger size, and prints them on
larger media and/or tiles them to print on multiple sheets.


%prep
%autosetup


%build
# The included Makefile is badly written
%{__cc} %{optflags} -lm -o poster poster.c %{?__global_ldflags}


%install
%{__install} -D -m755 -p poster   %{buildroot}%{_bindir}/poster
%{__install} -D -m644 -p poster.1 %{buildroot}%{_mandir}/man1/poster.1


%files
%doc ChangeLog README manual.ps
%license COPYING
%{_mandir}/man1/poster.1*
%{_bindir}/poster


%changelog
%autochangelog
