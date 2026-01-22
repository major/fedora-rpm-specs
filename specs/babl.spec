# skip tests known to be problematic in a specific version
%global skip_checks_version 0.1.58
%ifarch ppc64 ppc64le
%global skip_checks %nil
%else
  %ifarch s390x
  %global skip_checks float-to-8bit
  %else
  %global skip_checks %nil
  %endif
%endif

%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 20 || 0%{?rhel} > 7
%global develdocdir %{_docdir}/%{name}-devel/html
%else
%global develdocdir %{_docdir}/%{name}-devel-%{version}/html
%endif

Summary:    A dynamic, any to any, pixel format conversion library
Name:       babl
Version:    0.1.120
Release:    %autorelease

# Compute some version related macros
# In the case of a snapshot version (e.g. "Version: 2.99.19^20240814git256e0ca5a0"), this computes
# the "plain" version (as defined in upstream sources), %%snapshot and %%git_rev macros. In the case
# of a normal release, %%plain_version will be the same as %%version.
%global plain_version %{lua:
    local plain_version = (string.gsub(macros.version, '^(.*)[%^~].*$', '%1'))
    print(plain_version)
    if plain_version ~= macros.version then
        macros.snapshot = (string.gsub(macros.version, '^.*[%^~](.*)$', '%1'))
        macros.git_rev = (string.gsub(macros.snapshot, '^.*git(.*)$', '%1'))
    end
}
%global major %{lua:
    print((string.gsub(macros.plain_version, '^(%d+)%..*$', '%1')))
}
%global minor %{lua:
    print((string.gsub(macros.plain_version, '^%d+%.(%d+)%..*$', '%1')))
}
%global micro %{lua:
    print((string.gsub(macros.plain_version, '^%d+%.%d+%.(%d+).*$', '%1')))
}

%global apiver %major.%minor

# The gggl codes contained in this package are under the GPL, with exceptions allowing their use under libraries covered under the LGPL
License:    LGPL-3.0-or-later AND GPL-3.0-or-later
URL:        https://www.gegl.org/babl/
Source0:    https://download.gimp.org/pub/babl/%{apiver}/%{name}-%{plain_version}.tar.xz
%if %defined git_rev
Patch:      babl-%{plain_version}-git%{git_rev}.patch
%endif

BuildRequires:  gcc
BuildRequires:  openssh-clients
BuildRequires:  gobject-introspection-devel
BuildRequires:  gi-docgen
BuildRequires:  librsvg2-tools
BuildRequires:  meson, vala
BuildRequires:  pkgconfig(lcms2)

%description
Babl is a dynamic, any to any, pixel format conversion library. It
provides conversions between the myriad of buffer types images can be
stored in. Babl doesn't only help with existing pixel formats, but also
facilitates creation of new and uncommon ones.

%package devel
Summary:    Headers for developing programs that will use %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig
%if ! (0%{?fedora} >= 22 || 0%{?rhel} > 7)
# Split off devel docs from 0.1.2-2 on
Obsoletes:  %{name}-devel < 0.1.2-2%{?dist}
Conflicts:  %{name}-devel < 0.1.2-2%{?dist}
%endif

%description devel
This package contains the libraries and header files needed for
developing with %{name}.

%package devel-docs
Summary:    Documentation for developing programs that will use %{name}
BuildArch:  noarch
Requires:   %{name}-devel = %{version}-%{release}
# Split off devel docs from 0.1.2-2 on
Obsoletes:  %{name}-devel < 0.1.2-2%{?dist}
Conflicts:  %{name}-devel < 0.1.2-2%{?dist}

%description devel-docs
This package contains documentation needed for developing with %{name}.

%prep
%autosetup -p1 -n babl-%{plain_version}

%build
%meson
%meson_build

%install
%meson_install

mkdir -p "%{buildroot}/%{develdocdir}"
cp -pr "%{_vpath_builddir}"/docs/* "%{buildroot}/%{develdocdir}"
rm -f "%{buildroot}/%{develdocdir}/index.html.tmp"

mv "%{buildroot}/%{_docdir}/%{name}-%{apiver}" "%{buildroot}/%{develdocdir}"

%check
# skip tests known to be problematic in a specific version
%if "%version" == "%skip_checks_version"
pushd tests
for problematic in %skip_checks; do
    rm -f "$problematic"
    cat << EOF > "$problematic"
#!/bin/sh
echo Skipping test "$problematic"
EOF
    chmod +x "$problematic"
done
popd
%endif
%meson_test

%ldconfig_scriptlets

%files
%license docs/COPYING*
%doc AUTHORS NEWS
%{_bindir}/babl
%{_libdir}/libbabl-%{apiver}.so.0*
%{_libdir}/babl-%{apiver}/
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Babl-%{apiver}.typelib

%files devel
%{_includedir}/babl-%{apiver}/
%{_libdir}/libbabl-%{apiver}.so
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Babl-%{apiver}.gir
%{_datadir}/vala/

%files devel-docs
%doc %{develdocdir}

%changelog
%autochangelog
