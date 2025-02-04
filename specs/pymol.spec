Name: pymol
Summary: PyMOL Molecular Graphics System
Version: 3.1.0
Release: %autorelease

# Which files use following license:
# BSD: main license of open source PyMOL and some plugins
# MIT: modules/pymol_web/examples/sample13/jquery.js
# Bitstream Vera: layer1/FontTTF.h
# OFL: layer1/FontTTF2.h
# Automatically converted from old format: MIT and BSD and Bitstream Vera and OFL - review is highly recommended.
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND Bitstream-Vera AND LicenseRef-Callaway-OFL
URL: http://www.pymol.org
Source0: https://github.com/schrodinger/pymol-open-source/archive/v%{version}/%{name}-open-source-%{version}.tar.gz
Source1: %{name}.png
Source2: %{name}.desktop
Source3: %{name}.appdata.xml

# https://bugzilla.redhat.com/show_bug.cgi?id=1311626
Patch1: %{name}-wmclass-main.patch
Patch2: %{name}-wmclass-pmgapp.patch

Patch3: %{name}-mmtf.patch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: glew-devel
BuildRequires: glm-devel
BuildRequires: libGL-devel
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
BuildRequires: mmtf-cpp-devel
BuildRequires: msgpack-devel
BuildRequires: netcdf-devel
BuildRequires: catch2-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
# pymol-3.1.0 exactly requires pytest-8.2.2 and pillow-10.3.0
BuildRequires: python3-pytest
BuildRequires: python3-pillow

# Qt interface
BuildRequires: python3-qt5-devel
BuildRequires: freeglut-devel

# Optional, will fall back to Tk interface if compiled with --glut
BuildRequires: python3-pyside6-devel

Requires: apbs%{?_isa}
Requires: chemical-mime-data

Provides: PyMOL%{?_isa} = 0:%{version}-%{release}
%py_provides python3-%{name}

%description
PyMOL is a molecular graphics system with an embedded Python
interpreter designed for real-time visualization and rapid generation
of high-quality molecular graphics images and animations. It is fully
extensible and available free to everyone via the "Python"
license. Although a newcomer to the field, PyMOL can already be used
to generate stunning images and animations with ease. It can also
perform many other valuable tasks (such as editing PDB files) to
assist you in your research.

%prep
%autosetup -n %{name}-open-source-%{version} -p1

ln -sr modules/web modules/pymol_web

# Forcing numpy version
sed -e 's|1.26.4,<2|1.26.4,<3|g' -i ./pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name} chempy web pymol2 pymol_web pmg_tk pmg_qt

# Create executable script for running PyMOL
echo "#!/bin/sh" > pymol
echo "export PYMOL_PATH=%{python3_sitearch}/%{name}" >> %{name}
echo "exec %{__python3} %{python3_sitearch}/%{name}/__init__.py \"\$@\"" >> %{name}

mkdir -p %{buildroot}%{_bindir}
install -p -m 755 pymol %{buildroot}%{_bindir}/

desktop-file-install --vendor='' --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

mkdir -p %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml

%check
%py3_check_import -t %{name} chempy web pymol2 pymol_web pmg_tk pmg_qt

%files -n %{name} -f %{pyproject_files}
%doc AUTHORS DEVELOPERS README.* ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
