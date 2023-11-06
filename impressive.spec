Name:           impressive
Version:        0.13.2
Release:        %autorelease
Summary:        A program that displays presentation slides

License:        GPL-2.0-or-later
URL:            http://impressive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/Impressive-%{version}.tar.gz
# Wrapper script for making sure hardware acceleration is available
Source1:        %{name}.sh
Patch:          impressive-0.13-escape-escape-sequence.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# The following requires are not picked up by rpm:
# - imported modules (required):
Requires:       python3-imaging
Requires:       python3-pygame
Requires:       opengl-games-utils
# - external tools for displaying and parsing pdf (required):
Requires:       mupdf
# - external tool for acting on links (strongly recommended):
Requires:       xdg-utils
# - font for on screen display (recommended):
Requires:       dejavu-sans-fonts


%description
Impressive is a program that displays presentation slides. But unlike 
OpenOffice.org Impress or other similar applications, it does so with 
style. 

Smooth alpha-blended slide transitions are provided for the sake 
of eye candy, but in addition to this, Impressive offers some unique tools 
that are really useful for presentations.


%prep
%autosetup -n Impressive-%{version} -p1
sed -i -e '1s#/usr/bin/env python#/usr/bin/python3#' impressive.py

%build
sed -e "s|@PYTHON_SITELIB@|%{python3_sitelib}|" %{SOURCE1} > impressive.sh
# This package doesn't build anything, just copy files under build root.


%install
rm -rf %{buildroot}
install -D -p -m 755 impressive.py %{buildroot}%{python3_sitelib}/impressive.py
install -D -p -m 644 impressive.1 %{buildroot}%{_mandir}/man1/impressive.1
install -D -p -m 755 impressive.sh %{buildroot}%{_bindir}/impressive



%files
%doc changelog.txt demo.pdf impressive.html license.txt
%{_bindir}/impressive
%{python3_sitelib}/impressive.py
%{python3_sitelib}/__pycache__/*
%{_mandir}/man1/impressive.1*

%changelog
%autochangelog
