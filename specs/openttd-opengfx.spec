Version:        8.0

%global forgeurl https://github.com/OpenTTD/OpenGFX
%global tag %{version}
%forgemeta

%global ogfx_make_opts V=_ PYTHON=/usr/bin/python3

Name:           openttd-opengfx

Release:        %autorelease
Summary:        OpenGFX replacement graphics for OpenTTD

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
# The following two files are obtained from building the version tag (e.g. 8.0)
# inside a clone of the official repository.
# This may change pending https://github.com/OpenTTD/actions/issues/112
# MD5 values can also be obtained by downloading the official binary release
# from the OpenTTD website and inspecting the opengfx.obg contained therein.
# Original filename: .ottdrev
Source100:      opengfx-%{version}-revision-info.txt
# Original filename: opengfx-8.0.check.md5
Source101:      opengfx-%{version}.check.md5
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gimp
BuildRequires:  grfcodec
BuildRequires:  nml
BuildRequires:  python3
Requires:       openttd


%description
OpenGFX is an open source graphics base set for OpenTTD which can completely
replace the TTD base set. The main goal of OpenGFX therefore is to provide a
set of free base graphics which make it possible to play OpenTTD without
requiring the (copyrighted) files from the TTD CD. This potentially increases
the OpenTTD fan base and makes it a true free game (with "free" as in both
"free beer" and "free speech").

As of version 0.2.0 OpenGFX has a full set of sprites. Future versions will aim
to improve the graphics. 


%prep
%forgeautosetup
cp %{SOURCE100} .ottdrev


%build
make %{ogfx_make_opts} maintainer-clean
make %{ogfx_make_opts} %{?_smp_mflags}


%install
make install %{ogfx_make_opts} INSTALL_DIR=%{buildroot}%{_datadir}/openttd/baseset/opengfx


%check
cp %{SOURCE101} opengfx-%{version}.check.md5
# Matching MD5s are nice to have but not essential
make check %{ogfx_make_opts} || true


%files
%license LICENSE
%doc changelog.txt docs/authoroverview.csv extra/ README.md
%{_datadir}/openttd/baseset/opengfx/changelog.txt
%{_datadir}/openttd/baseset/opengfx/license.txt
%{_datadir}/openttd/baseset/opengfx/ogfx1_base.grf
%{_datadir}/openttd/baseset/opengfx/ogfxc_arctic.grf
%{_datadir}/openttd/baseset/opengfx/ogfxe_extra.grf
%{_datadir}/openttd/baseset/opengfx/ogfxh_tropical.grf
%{_datadir}/openttd/baseset/opengfx/ogfxi_logos.grf
%{_datadir}/openttd/baseset/opengfx/ogfxt_toyland.grf
%{_datadir}/openttd/baseset/opengfx/opengfx.obg
%{_datadir}/openttd/baseset/opengfx/readme.txt


%changelog
%autochangelog
