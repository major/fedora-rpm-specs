Name:           opencsg
Version:        1.8.0
Release:        %autorelease
Summary:        Library for Constructive Solid Geometry using OpenGL
# Most source code is GPL-2.0-or-later.
# src/glad/include/KHR/khrplatform.h is MIT-Khronos-old.
# src/glad/include/glad/gl.h and src/glad/src/gl.cpp are (WTFPL OR CC0-1.0) AND Apache-2.0.
# However, since CC0-1.0 is not allowed for code in Fedora, we reduce that to WTFPL AND Apache-2.0.
# https://docs.fedoraproject.org/en-US/legal/license-field/#_special_rules_for_or_expressions
License:        GPL-2.0-or-later AND MIT-Khronos-old AND WTFPL AND Apache-2.0
URL:            https://www.opencsg.org/
Source:         https://www.opencsg.org/OpenCSG-%{version}.tar.gz

BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
OpenCSG is a library that does image-based CSG rendering using OpenGL.

CSG is short for Constructive Solid Geometry and denotes an approach to model
complex 3D-shapes using simpler ones. I.e., two shapes can be combined by
taking the union of them, by intersecting them, or by subtracting one shape
of the other. The most basic shapes, which are not result of such a CSG
operation, are called primitives. Primitives must be solid, i.e., they must
have a clearly defined interior and exterior. By construction, a CSG shape is
also solid then.

Image-based CSG rendering (also z-buffer CSG rendering) is a term that denotes
algorithms for rendering CSG shapes without an explicit calculation of the
geometric boundary of a CSG shape. Such algorithms use frame-buffer settings
of the graphics hardware, e.g., the depth and stencil buffer, to compose CSG
shapes. OpenCSG implements a variety of those algorithms, namely the
Goldfeather algorithm and the SCS algorithm, both of them in several variants.

%package devel
Summary: OpenCSG development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for OpenCSG.

%package doc
Summary: OpenCSG documentation
BuildArch: noarch

%description doc
Documentation for OpenCSG.

%prep
%autosetup -p1 -n OpenCSG-%{version}

# Encoding
iconv --from=ISO-8859-1 --to=UTF-8 changelog.txt > changelog.txt.new && \
touch -r changelog.txt changelog.txt.new && \
mv changelog.txt.new changelog.txt


%build
%cmake -DBUILD_EXAMPLE=OFF
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license copying.txt
%{_libdir}/libopencsg.so.1
%{_libdir}/libopencsg.so.%{version}

%files devel
%{_includedir}/opencsg.h
%{_libdir}/libopencsg.so

%files doc
%doc changelog.txt doc
%license copying.txt


%changelog
%autochangelog
