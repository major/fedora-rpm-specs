Summary:	A text-mode maze game
Name:		lsnipes
Version:	0.9.4
Release:	%autorelease
License:	GPLv2+
Source:		http://www.ugcs.caltech.edu/~boultonj/snipes/%{name}-%{version}.tgz
URL:		http://www.ugcs.caltech.edu/~boultonj/snipes.html
Patch1:		lsnipes-adapt-CFLAGS-LIBS.patch
# Man page update about levels from Debian package
Patch2:		lsnipes-man-levels-doc.patch

BuildRequires:  gcc
BuildRequires:	ncurses-devel
BuildRequires: make

%description
Linux Snipes is a reimplementation of an old text-mode DOS game. You
are in a maze with a number of enemies (the "snipes") and a few
"hives" which create more of the enemies. Your job is to kill the
snipes and their hives before they get the best of you.  26 "option
levels" let you change characteristics of the game such as whether or
not diagonal shots bounce off the walls.  10 levels of difficulty (only
partially implemented) let you build your skills gradually.

%prep
%setup -q
%patch1 -p1 -b .cflags
%patch2 -p1 -b .man-levels

%build
%{__make} RPM_CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -p -m 0755 -d	%{buildroot}%{_bindir}
%{__install} -p -m 0755 snipes	%{buildroot}%{_bindir}/snipes
%{__install} -p -m 0755 -d	%{buildroot}%{_mandir}/man6
%{__install} -p -m 0644 snipes.6 %{buildroot}%{_mandir}/man6/snipes.6

%files
%doc README TODO COPYING CHANGELOG
%{_bindir}/snipes
%{_mandir}/man6/snipes.6*

%changelog
%autochangelog
