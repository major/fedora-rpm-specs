%global forgeurl https://github.com/jschobben/colorscad

Name:    colorscad
Version: 0.6.1
Release: 1%{?dist}
Summary: Helps with exporting an OpenSCAD model with color information preserved

%forgemeta
License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}

Patch0:  https://patch-diff.githubusercontent.com/raw/jschobben/colorscad/pull/23.patch

Requires: openscad
Requires: sed

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig(lib3mf)

BuildRequires: openscad
BuildRequires: sed

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
    ExcludeArch: %{ix86}
%endif

%description
This script helps with exporting an OpenSCAD model to AMF or 3MF format,
with color information preserved. The colors are simply assigned using
OpenSCADs color() statement, so generally speaking the output will look
like the preview (F5) view in OpenSCAD.

%prep
%forgesetup
%patch 0 -p1

%build
%cmake
%cmake_build


%install
%cmake_install


%check
PATH=%{buildroot}%{_bindir}:$PATH test/run.sh


%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%doc %attr(0644, -, -) colors.scad
%{_bindir}/colorscad
%{_bindir}/3mfmerge

%changelog
* Sat Mar 15 2025 Jonny Heggheim <hegjon@gmail.com> - 0.6.1-1
- Initial package
