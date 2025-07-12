Name:			gimp-paint-studio
Version:		2.0
Release:		%autorelease
Summary:		A collection of tool option presets and brushes for GIMP
License:		CC-BY-SA-3.0 AND GPL-2.0-only
URL:			https://code.google.com/p/gps-%{name}/
Source0:		https://gps-%{name}.googlecode.com/files/GPS_2_0.tar.gz
Source1:		%{name}.metainfo.xml

Patch0:                 gps-2.0-rateRange.patch
Patch1:                 gps-2.0-replaceBlends.patch

BuildRequires:          fdupes
BuildArch:              noarch
Requires:               gimp >= 2.10

%description
GIMP Paint Studio(GPS) is a collection of brushes and accompanying tool
presets. Tool presets are a simply saved tool options, highly useful feature of
the GIMP. The goal of GPS is to provide an adequate working environment for
graphic designers and artists to begin to paint and feel comfortable with GIMP
from their first use.

%prep
%autosetup -c -p1 %{name}-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/gimp/3.0
# Remove xcf files from patterns directory
rm -rf %{_builddir}/%{name}-%{version}/patterns/GPS-Pat/*.xcf
# Remove duplicated files
fdupes -rdN %{_builddir}/%{name}-%{version}/patterns/GPS-Pat/
cp -pr %{_builddir}/%{name}-%{version}/brushes \
                %{_builddir}/%{name}-%{version}/dynamics \
                %{_builddir}/%{name}-%{version}/gradients \
                %{_builddir}/%{name}-%{version}/splashes\
                %{_builddir}/%{name}-%{version}/palettes \
                %{_builddir}/%{name}-%{version}/patterns \
                %{_builddir}/%{name}-%{version}/tool-presets \
                %{buildroot}%{_datadir}/gimp/3.0

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
                %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
#CC-BY-SA
%{_datadir}/gimp/3.0/brushes/GPS-Brushes/
%{_datadir}/gimp/3.0/dynamics/GPS-Eraser/
%{_datadir}/gimp/3.0/dynamics/GPS-Fx/
%{_datadir}/gimp/3.0/dynamics/GPS-Set1/
%{_datadir}/gimp/3.0/dynamics/GPS-Set2/
%{_datadir}/gimp/3.0/dynamics/GPS-Sketch/
%{_datadir}/gimp/3.0/dynamics/GPS-Smudge/
%{_datadir}/gimp/3.0/gradients/GPS-Grad/
%{_datadir}/gimp/3.0/splashes/GPS-2_0--splash-techno-dark.jpg
%{_datadir}/gimp/3.0/palettes/GPS-Pal/
%{_datadir}/gimp/3.0/patterns/GPS-Pat/
#GPLv2
%{_datadir}/gimp/3.0/tool-presets/GPS-Eraser/
%{_datadir}/gimp/3.0/tool-presets/GPS-Fx/
%{_datadir}/gimp/3.0/tool-presets/GPS-Ink/
%{_datadir}/gimp/3.0/tool-presets/GPS-Set1/
%{_datadir}/gimp/3.0/tool-presets/GPS-Set2/
%{_datadir}/gimp/3.0/tool-presets/GPS-Sketch/
%{_datadir}/gimp/3.0/tool-presets/GPS-Smudge/
#AppStream metadata
%{_metainfodir}/%{name}.metainfo.xml

%doc "License for Contents" License_gpl-2.0.txt Readme.txt

%changelog
%autochangelog
