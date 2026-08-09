%global forgeurl https://github.com/FreeCAD/pivy
Version:        0.6.10
%global tag     %{version}
%forgemeta

Name:           python-pivy
Release:        %autorelease
Summary:        Python binding for Coin

License:        ISC
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         pivy-fake-memory-header.patch
Patch1:         pivy-python-3.15.patch

BuildRequires:  Coin4-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  python3-devel
BuildRequires:  swig



%global _description\
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics library with\
a C++ Application Programming Interface. Coin uses scene-graph data structures\
to render real-time graphics suitable for mostly all kinds of scientific and\
engineering visualization applications.\

%description %_description


%package -n python3-pivy
Summary: %summary

%description -n python3-pivy %_description


%package examples
Summary: Pivy example files
BuildArch: noarch

%description examples
%{summary}

%prep
%autosetup -p1 -n pivy-%{version}

# Examples in the docs and examples folder should not be set executable.
find ./docs -name "*.py" -exec chmod -x {} \;
find ./examples -name "*.py" -exec chmod -x {} \;


%generate_buildrequires
%pyproject_buildrequires


%build
%cmake
%cmake_build


%install
%cmake_install

chmod +x %{buildroot}%{python3_sitearch}/pivy/sogui.py

find %{buildroot}%{python3_sitearch} -name "*.py" -exec sed -i "s|#!/usr/bin/env python|#!%{__python3}|" {} \;


%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{__python3} tests/coin_tests.py


%files -n python3-pivy
%license LICENSE
%doc AUTHORS NEWS README.md THANKS docs/* HACKING
%{python3_sitearch}/pivy/

%files examples
%doc examples


%changelog
%autochangelog
