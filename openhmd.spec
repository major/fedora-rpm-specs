%global srcname OpenHMD
%global forgeurl https://github.com/OpenHMD/OpenHMD
%global date 20230112
%global commit e64708b8213c52a6b0bbd7ad77e0ab910b5af6b8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           openhmd
Version:        0.3.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Free and Open Source API and drivers for immersive technology

# OpenHMD is BSL-1.0, the rest comes from bundled dependencies
License:        BSL-1.0 AND MIT AND Unlicense
URL:            http://www.openhmd.net
Source0:        %{forgeurl}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
# License text based on the comment on top of src/ext_deps/nxjson.c
Source1:        LICENSE.miniz
# License text extracted from the comment at the bottom of src/ext_deps/miniz.c
Source2:        LICENSE.nxjson

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  glew-devel
BuildRequires:  hidapi-devel
BuildRequires:  SDL2-devel

Recommends:     xr-hardware

# Vendored under src/ext_deps/miniz.c and included via a header wrapper
# License: Unlicense
Provides:       bundled(miniz) = 1.15
# Vendored under src/ext_deps/nxjson.{c,h} and modified
# License: MIT
Provides:       bundled(nxjson) = 20180520

%description
OpenHMD aims to provide a Free and Open Source API and drivers for immersive
technology, such as head mounted displays with built in head tracking.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       %{name}-doc = %{version}-%{release}

%description    devel
This package contains development headers and libraries for %{name}.

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains developer documentation for %{name}.

%package        examples
Summary:        Examples for %{name}

%description    examples
This package contains examples making use of %{name}.

%prep
%autosetup -n %{srcname}-%{commit}

# Copy license texts for bundled dependencies
cp -p %SOURCE1 %SOURCE2 .

%build
%meson -Dexamples=simple,opengl
%meson_build

# Build documentation
doxygen

%install
%meson_install

%check
%meson_test

%files
%license LICENSE LICENSE.miniz LICENSE.nxjson
%doc README.md
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license LICENSE
%doc html

%files examples
%{_bindir}/openhmd_simple_example
%{_bindir}/openhmd_opengl_example

%changelog
%autochangelog
